#!/usr/bin/env python3
"""
RVx Index MVP scorer.

Implements the Chapter 3 power form:
  RVx = (E**beta * S) / (L**alpha + epsilon)

Defaults: beta=1.2, alpha=0.8, epsilon=0.1
Does not change book thresholds; zone labels are informational only.

MVP only. See docs/RVX-SPEC.md.
"""

from __future__ import annotations

import argparse
import json
import math
import subprocess
from collections import defaultdict
from pathlib import Path
from typing import Iterable


DEFAULT_BETA = 1.2
DEFAULT_ALPHA = 0.8
DEFAULT_EPSILON = 0.1


def clamp01(x: float) -> float:
    return max(0.0, min(1.0, x))


def cognitive_load(loc: float, complexity: float) -> float:
    """Chapter 3 style normalization; clamp to [0, 1]."""
    return clamp01((complexity + loc / 1000.0) / 200.0)


def kinetic_from_trace(summary: dict) -> float:
    """Expect keys: compute_ms, network_ms, serialize_ms, mesh_ms."""
    c = float(summary.get("compute_ms", 0.0))
    n = float(summary.get("network_ms", 0.0))
    s = float(summary.get("serialize_ms", 0.0))
    m = float(summary.get("mesh_ms", 0.0))
    denom = c + n + s + m
    if denom <= 0:
        return 0.0
    return clamp01(c / denom)


def semantic_from_git(repo: Path, service_path: str, days: int = 90) -> float:
    """
    Proxy for Semantic Distinctness:
    1 - (commits that touch service_path and other paths) / (commits touching service_path).
    """
    try:
        raw = subprocess.check_output(
            [
                "git",
                "-C",
                str(repo),
                "log",
                f"--since={days}.days",
                "--name-only",
                "--pretty=format:COMMIT",
            ],
            text=True,
            stderr=subprocess.DEVNULL,
        )
    except (subprocess.CalledProcessError, FileNotFoundError):
        return 0.5  # neutral if git unavailable

    commits: list[list[str]] = []
    current: list[str] = []
    for line in raw.splitlines():
        if line == "COMMIT":
            if current:
                commits.append(current)
            current = []
        elif line.strip():
            current.append(line.strip().replace("\\", "/"))
    if current:
        commits.append(current)

    service_commits = 0
    multi = 0
    prefix = service_path.replace("\\", "/").rstrip("/")
    for files in commits:
        hits = [f for f in files if f == prefix or f.startswith(prefix + "/")]
        if not hits:
            continue
        service_commits += 1
        if any(not (f == prefix or f.startswith(prefix + "/")) for f in files):
            multi += 1

    if service_commits == 0:
        return 0.5
    return clamp01(1.0 - (multi / service_commits))


def rvx(e: float, s: float, l: float, beta: float, alpha: float, eps: float) -> float:
    return (e**beta * s) / (l**alpha + eps)


def zone(rvx_score: float, e: float, s: float, l: float) -> str:
    if rvx_score <= 0.3 and e < 0.3:
        return "MERGE_CANDIDATE"
    if l > 0.7:
        return "SPLIT_CANDIDATE"
    if rvx_score > 0.6 and s > 0.6 and l < 0.7:
        return "HEALTHY"
    return "REVIEW"


def main(argv: Iterable[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="RVx Index MVP scorer")
    p.add_argument("--loc", type=float, required=True)
    p.add_argument("--complexity", type=float, required=True)
    p.add_argument("--git-repo", type=Path, default=Path("."))
    p.add_argument("--service-path", type=str, default=".")
    p.add_argument("--days", type=int, default=90)
    p.add_argument("--trace-file", type=Path, help="JSON with compute_ms, network_ms, ...")
    p.add_argument("--e", type=float, help="Override Kinetic Efficiency [0,1]")
    p.add_argument("--s", type=float, help="Override Semantic Distinctness [0,1]")
    p.add_argument("--beta", type=float, default=DEFAULT_BETA)
    p.add_argument("--alpha", type=float, default=DEFAULT_ALPHA)
    p.add_argument("--epsilon", type=float, default=DEFAULT_EPSILON)
    args = p.parse_args(list(argv) if argv is not None else None)

    l_hat = cognitive_load(args.loc, args.complexity)

    if args.e is not None:
        e_hat = clamp01(args.e)
    elif args.trace_file:
        summary = json.loads(args.trace_file.read_text(encoding="utf-8"))
        e_hat = kinetic_from_trace(summary)
    else:
        e_hat = 0.5

    if args.s is not None:
        s_hat = clamp01(args.s)
    else:
        s_hat = semantic_from_git(args.git_repo, args.service_path, args.days)

    score = rvx(e_hat, s_hat, l_hat, args.beta, args.alpha, args.epsilon)
    result = {
        "E_hat": round(e_hat, 4),
        "S_hat": round(s_hat, 4),
        "L_hat": round(l_hat, 4),
        "beta": args.beta,
        "alpha": args.alpha,
        "epsilon": args.epsilon,
        "RVx": round(score, 4),
        "zone": zone(score, e_hat, s_hat, l_hat),
        "form": "power",
        "mvp": True,
    }
    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
