#!/usr/bin/env python3
"""Editorial SVG diagrams for Microservices Recipes (atelier look)."""

from __future__ import annotations

import html
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DIAG_DIR = ROOT / "assets" / "images" / "diagrams"
IMAGE_DIR = ROOT / "assets" / "images"

INK = "#15252f"
INK_SOFT = "#3d5260"
PAPER = "#f7f3eb"
PAPER_EDGE = "#ebe4d6"
DESK = "#1b3a4b"
DESK_DEEP = "#122833"
COPPER = "#9a6b3f"
GILT = "#c4a574"
GOOD = "#2f6b55"
WARN = "#b8860b"
BAD = "#8b3a3a"
CARD = "#fffaf2"
GOOD_WASH = "#e7f0eb"
WARN_WASH = "#f6eed8"
BAD_WASH = "#f3e4e1"
DESK_WASH = "#e4eef2"
GILT_WASH = "#f4ecdc"

FONT = "'IBM Plex Sans', system-ui, 'Segoe UI', sans-serif"
MONO = "'IBM Plex Mono', ui-monospace, Consolas, monospace"
DISPLAY = "Fraunces, 'Iowan Old Style', Georgia, serif"

TONES = {
    "neutral": (CARD, PAPER_EDGE, INK),
    "desk": (DESK_WASH, DESK, DESK),
    "good": (GOOD_WASH, GOOD, GOOD),
    "warn": (WARN_WASH, WARN, WARN),
    "bad": (BAD_WASH, BAD, BAD),
    "gilt": (GILT_WASH, GILT, COPPER),
    "paper": (PAPER, PAPER_EDGE, INK_SOFT),
}


def esc(text: object) -> str:
    return html.escape(str(text), quote=True)


class Svg:
    def __init__(self, width: int, height: int, title: str, subtitle: str = "") -> None:
        self.w = width
        self.h = height
        self.title = title
        self.subtitle = subtitle
        self.parts: list[str] = []
        self._n = 0

    def uid(self, prefix: str = "i") -> str:
        self._n += 1
        return f"{prefix}{self._n}"

    def add(self, markup: str) -> None:
        self.parts.append(markup)

    def text(
        self,
        x: float,
        y: float,
        text: str,
        *,
        size: float = 13,
        fill: str = INK,
        weight: str = "500",
        anchor: str = "start",
        family: str = FONT,
        italic: bool = False,
        extra: str = "",
    ) -> None:
        style = f"font-style:italic;" if italic else ""
        self.add(
            f'<text x="{x:.1f}" y="{y:.1f}" fill="{fill}" font-size="{size}" '
            f'font-weight="{weight}" text-anchor="{anchor}" font-family="{family}" '
            f'style="{style}" {extra}>{esc(text)}</text>'
        )

    def lines(
        self,
        x: float,
        y: float,
        texts: list[str],
        *,
        size: float = 12,
        fill: str = INK_SOFT,
        weight: str = "400",
        gap: float = 16,
        anchor: str = "start",
        family: str = FONT,
        italic: bool = False,
    ) -> None:
        for i, line in enumerate(texts):
            if line:
                self.text(
                    x,
                    y + i * gap,
                    line,
                    size=size,
                    fill=fill,
                    weight=weight,
                    anchor=anchor,
                    family=family,
                    italic=italic,
                )

    def rect(
        self,
        x: float,
        y: float,
        w: float,
        h: float,
        *,
        fill: str = CARD,
        stroke: str = PAPER_EDGE,
        sw: float = 1,
        rx: float = 10,
        shadow: bool = False,
        extra: str = "",
    ) -> None:
        filt = 'filter="url(#cardShadow)"' if shadow else ""
        self.add(
            f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" rx="{rx}" '
            f'fill="{fill}" stroke="{stroke}" stroke-width="{sw}" {filt} {extra}/>'
        )

    def card(
        self,
        x: float,
        y: float,
        w: float,
        h: float,
        *,
        tone: str = "neutral",
        title: str = "",
        body: list[str] | None = None,
        shadow: bool = True,
        rx: float = 10,
        title_size: float = 13.5,
    ) -> None:
        fill, stroke, accent = TONES[tone]
        self.rect(x, y, w, h, fill=fill, stroke=stroke, sw=1.25, rx=rx, shadow=shadow)
        self.add(
            f'<path d="M{x + 12:.1f} {y + 1:.1f} h{max(w - 24, 20):.1f}" '
            f'stroke="{COPPER}" stroke-width="1.15" stroke-linecap="round" opacity="0.85"/>'
        )
        if title:
            self.text(x + w / 2, y + 26, title, size=title_size, fill=INK, weight="600", anchor="middle")
        if body:
            self.lines(x + w / 2, y + 46, body, size=11.5, fill=INK_SOFT, anchor="middle", gap=15)

    def panel(
        self,
        x: float,
        y: float,
        w: float,
        h: float,
        label: str,
        *,
        tone: str = "paper",
    ) -> None:
        fill, stroke, _ = TONES[tone]
        self.rect(x, y, w, h, fill=fill, stroke=stroke, sw=1, rx=14, shadow=False)
        self.text(x + 16, y + 22, label, size=11, fill=COPPER, weight="600")

    def pill(self, x: float, y: float, w: float, h: float, label: str, *, tone: str = "desk") -> None:
        fill, stroke, accent = TONES[tone]
        self.rect(x, y, w, h, fill=fill, stroke=stroke, sw=1, rx=h / 2, shadow=False)
        self.text(x + w / 2, y + h / 2 + 4, label, size=11, fill=accent, weight="600", anchor="middle")

    def arrow(
        self,
        x1: float,
        y1: float,
        x2: float,
        y2: float,
        *,
        color: str = COPPER,
        dashed: bool = False,
        width: float = 1.35,
        marker: str = "arrowCopper",
    ) -> None:
        dash = 'stroke-dasharray="5 4"' if dashed else ""
        self.add(
            f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" '
            f'stroke="{color}" stroke-width="{width}" {dash} marker-end="url(#{marker})" '
            f'stroke-linecap="round"/>'
        )

    def hrule(self, x: float, y: float, w: float, *, color: str = COPPER, opacity: float = 0.7) -> None:
        self.add(
            f'<path d="M{x:.1f} {y:.1f} h{w:.1f}" stroke="{color}" stroke-width="1.1" '
            f'stroke-linecap="round" opacity="{opacity}"/>'
        )

    def cylinder(self, x: float, y: float, w: float, h: float, label: str, *, tone: str = "good") -> None:
        fill, stroke, _ = TONES[tone]
        rx, ry = w / 2, 9
        cx = x + w / 2
        self.add(
            f'<path d="M{x:.1f} {y + ry:.1f} v{h - 2 * ry:.1f} '
            f'a{rx:.1f} {ry:.1f} 0 0 0 {w:.1f} 0 v{-h + 2 * ry:.1f} '
            f'a{rx:.1f} {ry:.1f} 0 0 0 {-w:.1f} 0z" fill="{fill}" stroke="{stroke}" stroke-width="1.2"/>'
        )
        self.add(
            f'<ellipse cx="{cx:.1f}" cy="{y + ry:.1f}" rx="{rx:.1f}" ry="{ry:.1f}" '
            f'fill="{CARD}" stroke="{stroke}" stroke-width="1.2"/>'
        )
        self.text(cx, y + h / 2 + 6, label, size=11, fill=INK, weight="600", anchor="middle")

    def diamond(self, cx: float, cy: float, w: float, h: float, label: str, *, tone: str = "warn") -> None:
        fill, stroke, _ = TONES[tone]
        pts = f"{cx},{cy - h / 2} {cx + w / 2},{cy} {cx},{cy + h / 2} {cx - w / 2},{cy}"
        self.add(f'<polygon points="{pts}" fill="{fill}" stroke="{stroke}" stroke-width="1.2"/>')
        self.lines(cx, cy - 4, label.split("\n"), size=11, fill=INK, weight="600", anchor="middle", gap=13)

    def node(
        self,
        x: float,
        y: float,
        w: float,
        h: float,
        title: str,
        *body: str,
        tone: str = "neutral",
        title_size: float = 13,
    ) -> tuple[float, float, float, float]:
        self.card(x, y, w, h, tone=tone, title=title, body=list(body) if body else None, title_size=title_size)
        return x, y, w, h

    def mid(self, box: tuple[float, float, float, float], edge: str = "c") -> tuple[float, float]:
        x, y, w, h = box
        return {
            "c": (x + w / 2, y + h / 2),
            "n": (x + w / 2, y),
            "s": (x + w / 2, y + h),
            "e": (x + w, y + h / 2),
            "w": (x, y + h / 2),
        }[edge]

    def connect(
        self,
        a: tuple[float, float, float, float],
        b: tuple[float, float, float, float],
        *,
        frm: str = "e",
        to: str = "w",
        color: str = COPPER,
        dashed: bool = False,
        label: str = "",
        label_dy: float = -8,
    ) -> None:
        x1, y1 = self.mid(a, frm)
        x2, y2 = self.mid(b, to)
        # shorten so arrowheads do not sit under card strokes
        dx, dy = x2 - x1, y2 - y1
        length = math.hypot(dx, dy) or 1
        pad = 2
        x1 += dx / length * pad
        y1 += dy / length * pad
        x2 -= dx / length * 8
        y2 -= dy / length * 8
        marker = {
            COPPER: "arrowCopper",
            DESK: "arrowDesk",
            GOOD: "arrowGood",
            BAD: "arrowBad",
            INK_SOFT: "arrowSoft",
            WARN: "arrowWarn",
        }.get(color, "arrowCopper")
        self.arrow(x1, y1, x2, y2, color=color, dashed=dashed, marker=marker)
        if label:
            self.text(
                (x1 + x2) / 2,
                (y1 + y2) / 2 + label_dy,
                label,
                size=10.5,
                fill=INK_SOFT,
                weight="500",
                anchor="middle",
            )

    def footnote(self, text: str) -> None:
        self.text(28, self.h - 18, text, size=11, fill=INK_SOFT, italic=True)

    def render(self) -> str:
        title_id = "figtitle"
        body = "\n".join(self.parts)
        return f"""<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="{self.w}" height="{self.h}" viewBox="0 0 {self.w} {self.h}" role="img" aria-labelledby="{title_id}">
  <title id="{title_id}">{esc(self.title)}</title>
  <defs>
    <filter id="cardShadow" x="-12%" y="-12%" width="124%" height="132%">
      <feDropShadow dx="0" dy="5" stdDeviation="7" flood-color="{DESK_DEEP}" flood-opacity="0.12"/>
    </filter>
    <filter id="softShadow" x="-20%" y="-20%" width="140%" height="150%">
      <feDropShadow dx="0" dy="10" stdDeviation="14" flood-color="{DESK_DEEP}" flood-opacity="0.18"/>
    </filter>
    <marker id="arrowCopper" markerWidth="8" markerHeight="8" refX="6.2" refY="4" orient="auto">
      <path d="M1 1.2 L6.4 4 L1 6.8 Z" fill="{COPPER}"/>
    </marker>
    <marker id="arrowDesk" markerWidth="8" markerHeight="8" refX="6.2" refY="4" orient="auto">
      <path d="M1 1.2 L6.4 4 L1 6.8 Z" fill="{DESK}"/>
    </marker>
    <marker id="arrowGood" markerWidth="8" markerHeight="8" refX="6.2" refY="4" orient="auto">
      <path d="M1 1.2 L6.4 4 L1 6.8 Z" fill="{GOOD}"/>
    </marker>
    <marker id="arrowBad" markerWidth="8" markerHeight="8" refX="6.2" refY="4" orient="auto">
      <path d="M1 1.2 L6.4 4 L1 6.8 Z" fill="{BAD}"/>
    </marker>
    <marker id="arrowSoft" markerWidth="8" markerHeight="8" refX="6.2" refY="4" orient="auto">
      <path d="M1 1.2 L6.4 4 L1 6.8 Z" fill="{INK_SOFT}"/>
    </marker>
    <marker id="arrowWarn" markerWidth="8" markerHeight="8" refX="6.2" refY="4" orient="auto">
      <path d="M1 1.2 L6.4 4 L1 6.8 Z" fill="{WARN}"/>
    </marker>
    <linearGradient id="paperGrad" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="{CARD}"/>
      <stop offset="100%" stop-color="{PAPER}"/>
    </linearGradient>
  </defs>
  <rect width="100%" height="100%" fill="url(#paperGrad)"/>
  <rect x="10" y="10" width="{self.w - 20}" height="{self.h - 20}" rx="18" fill="none" stroke="{PAPER_EDGE}" stroke-width="1"/>
  <text id="visible-title" x="28" y="38" fill="{DESK}" font-size="20" font-weight="650" font-family="{FONT}">{esc(self.title)}</text>
  <path d="M28 48 h{min(self.w - 80, 360)}" stroke="{COPPER}" stroke-width="1.2" stroke-linecap="round"/>
  {f'<text x="28" y="66" fill="{INK_SOFT}" font-size="12" font-family="{FONT}">{esc(self.subtitle)}</text>' if self.subtitle else ""}
  {body}
</svg>
"""


def write_svg(path: Path, svg: Svg) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(svg.render(), encoding="utf-8")
    return path


def boxed(s: Svg, x: float, y: float, w: float, h: float, title: str, *body: str, tone: str = "neutral") -> tuple:
    return s.node(x, y, w, h, title, *body, tone=tone)


def flow_chain(s: Svg, items: list[tuple], y: float, w: float = 148, h: float = 86, gap: float = 28, x0: float = 28) -> list:
    boxes = []
    x = x0
    for item in items:
        title, *rest = item
        tone = "neutral"
        body: list[str] = []
        for part in rest:
            if part in TONES:
                tone = part
            else:
                body.append(part)
        box = boxed(s, x, y, w, h, title, *body, tone=tone)
        if boxes:
            s.connect(boxes[-1], box)
        boxes.append(box)
        x += w + gap
    return boxes


# ---------------------------------------------------------------------------
# Diagrams
# ---------------------------------------------------------------------------


def d_soa_vs_microservices() -> Svg:
    s = Svg(980, 560, "SOA vs microservices", "Smart pipes versus smart endpoints.")
    s.panel(28, 84, 450, 440, "Classic SOA: thin endpoints, smart pipes", tone="bad")
    esb = boxed(s, 148, 250, 210, 96, "Enterprise Service Bus", "routing · transform", "business rules in the pipe", tone="bad")
    a = boxed(s, 52, 130, 160, 72, "Checkout", "SOAP / XML", tone="paper")
    b = boxed(s, 248, 130, 160, 72, "Inventory", "SOAP / XML", tone="paper")
    c = boxed(s, 52, 400, 160, 72, "Billing", "SOAP / XML", tone="paper")
    d = boxed(s, 248, 400, 186, 72, "Shared schema", "legacy systems", tone="warn")
    s.connect(a, esb, frm="s", to="n", label="SOAP")
    s.connect(b, esb, frm="s", to="n")
    s.connect(c, esb, frm="n", to="s")
    s.connect(esb, d, frm="s", to="n", label="orchestration")

    s.panel(502, 84, 450, 440, "Microservices: smart endpoints, dumb pipes", tone="good")
    x = boxed(s, 536, 180, 180, 92, "Order service", "owns its rules", tone="good")
    y = boxed(s, 748, 180, 180, 92, "Payment service", "owns its rules", tone="good")
    z = boxed(s, 642, 360, 196, 92, "Inventory context", "owns its rules", tone="good")
    s.connect(x, y, label="HTTP / gRPC")
    s.connect(x, z, frm="s", to="n", dashed=True, label="domain event")
    s.connect(y, z, frm="s", to="n", dashed=True, label="domain event")
    return s


def d_granularity_spectrum() -> Svg:
    s = Svg(980, 420, "Granularity spectrum", "Value lives in the middle band that shifts with team, workload, and domain.")
    left = boxed(s, 40, 140, 250, 170, "Monolith zone", "entangled code", "slow builds", "too coarse", tone="bad")
    mid = boxed(s, 365, 120, 250, 210, "Bounded-context zone", "capability-aligned", "healthy band", "boundaries earn their keep", tone="good")
    right = boxed(s, 690, 140, 250, 170, "Nanoservice zone", "network tax", "distributed spaghetti", "too fine", tone="bad")
    s.connect(left, mid, label="decompose on seams")
    s.connect(mid, right, label="over-split")
    s.footnote("Too coarse is a monolith. Too fine is a distributed monolith. Neither extreme is the goal.")
    return s


def d_system_availability_chain() -> Svg:
    s = Svg(1040, 420, "System availability chain", "Combined success = (0.999)^n when each hop is independently 99.9%.")
    items = [
        ("Client request", "100%", "desk"),
        ("Hop 1", "99.9%", "warn"),
        ("Hop 10", "combined ≈ 99.0%", "warn"),
        ("Hop 25", "combined ≈ 97.5%", "bad"),
        ("Hop 50", "combined ≈ 95.1%", "bad"),
        ("Topology failure", "~1 in 20 requests", "fails by design", "bad"),
    ]
    flow_chain(s, items, 150, w=148, h=110, gap=18, x0=28)
    s.footnote("Independent failures, no retries. Correlated failures and retry storms make this worse.")
    return s


def d_temporal_coupling_analysis() -> Svg:
    s = Svg(980, 580, "Temporal coupling analysis", "Recipe 1.1 reads commits exploratorily. Chapter 11 publishes S from merged PRs.")
    s.panel(28, 88, 300, 200, "Git history, not the whiteboard")
    src = boxed(s, 48, 122, 260, 70, "git log --numstat", "who changed with whom", tone="desk")
    pairs = boxed(s, 48, 210, 260, 64, "Pair scoring", "Jaccard = together / either", tone="gilt")
    s.connect(src, pairs, frm="s", to="n")

    red = boxed(s, 360, 100, 280, 120, "Red · above ~0.7", "CartService ↔ PricingService", "keep in one context", tone="bad")
    amber = boxed(s, 360, 240, 280, 120, "Amber · 0.2 to 0.7", "investigate: real rule", "or a dependency magnet?", tone="warn")
    green = boxed(s, 360, 380, 280, 120, "Green · below ~0.2", "evolve independently", "safer to separate", tone="good")
    s.connect(pairs, red, frm="e", to="w")
    s.connect(pairs, amber, frm="e", to="w")
    s.connect(pairs, green, frm="e", to="w")

    boxed(s, 680, 110, 270, 100, "Do not split", "would create lock-step deploys", tone="bad")
    boxed(s, 680, 250, 270, 100, "Inspect first", "break up utils / constants", "before drawing a boundary", tone="warn")
    boxed(s, 680, 390, 270, 100, "Candidate seam", "still name an honest reason", tone="good")
    s.connect(red, (680, 110, 270, 100), frm="e", to="w")
    s.connect(amber, (680, 250, 270, 100), frm="e", to="w")
    s.connect(green, (680, 390, 270, 100), frm="e", to="w")
    s.footnote("Exploratory commit pairing here. Published S in Chapter 11 uses change sets (merged PRs), not raw commits.")
    return s


def d_conways_law() -> Svg:
    s = Svg(960, 480, "Conway's Law", "The architecture that ships is a copy of the communication structure.")
    s.panel(40, 96, 300, 330, "Organization")
    fe = boxed(s, 70, 140, 240, 70, "Frontend team", tone="warn")
    be = boxed(s, 70, 230, 240, 70, "Backend team", tone="warn")
    db = boxed(s, 70, 320, 240, 70, "Database team", tone="warn")
    s.panel(420, 96, 500, 330, "Architecture that results")
    bff = boxed(s, 460, 140, 200, 70, "BFF service", tone="desk")
    logic = boxed(s, 460, 230, 200, 70, "Business-logic service", tone="desk")
    data = boxed(s, 460, 320, 220, 70, "Data service", "shared schema", tone="bad")
    s.connect(fe, bff, label="mirrors")
    s.connect(be, logic, label="mirrors")
    s.connect(db, data, label="mirrors")
    s.connect(bff, logic, frm="s", to="n")
    s.connect(logic, data, frm="s", to="n")
    return s


def d_team_topologies() -> Svg:
    s = Svg(980, 520, "Team Topologies", "Stream-aligned teams, with platform, enabling, and complicated-subsystem support.")
    t1 = boxed(s, 80, 120, 200, 80, "Order team", "stream-aligned", tone="good")
    t2 = boxed(s, 390, 120, 200, 80, "Payment team", "stream-aligned", tone="good")
    t3 = boxed(s, 700, 120, 200, 80, "Shipping team", "stream-aligned", tone="good")
    plat = boxed(s, 80, 320, 240, 100, "Platform team", "paves the golden path", "X-as-a-Service", tone="desk")
    ena = boxed(s, 370, 320, 240, 100, "Enabling team", "spreads capability", "facilitating", tone="warn")
    hard = boxed(s, 660, 320, 250, 100, "Complicated-subsystem", "owns the hard parts", "time-boxed collaboration", tone="bad")
    s.connect(plat, t1, frm="n", to="s", label="X-as-a-Service")
    s.connect(plat, t2, frm="n", to="s")
    s.connect(plat, t3, frm="n", to="s")
    s.connect(ena, t1, frm="n", to="s", dashed=True, label="facilitating")
    s.connect(ena, t2, frm="n", to="s", dashed=True)
    s.connect(t2, hard, frm="s", to="n", label="collaborate")
    return s


def d_bounded_context_map() -> Svg:
    s = Svg(980, 520, "Bounded context map", "Relationships between contexts are designed, not accidental.")
    ident = boxed(s, 40, 200, 160, 90, "Identity", tone="desk")
    rec = boxed(s, 400, 200, 180, 100, "Recommendation", tone="good")
    main = boxed(s, 400, 40, 180, 90, "Legacy mainframe", tone="bad")
    sales = boxed(s, 760, 200, 170, 90, "Sales", tone="warn")
    cat = boxed(s, 760, 380, 170, 90, "Catalog", tone="bad")
    s.connect(ident, rec, label="Conformist: UserId only")
    s.connect(main, rec, frm="s", to="n", label="anti-corruption layer")
    s.connect(sales, rec, label="open host + published language")
    s.connect(cat, sales, frm="n", to="s", color=BAD, label="shared kernel, warning")
    return s


def d_anti_corruption_layer() -> Svg:
    s = Svg(980, 480, "Anti-corruption layer", "Keep the new model clean. Translate at the edge.")
    s.panel(36, 100, 280, 320, "New shipping service", tone="good")
    domain = boxed(s, 56, 150, 240, 90, "Clean domain model", tone="good")
    facade = boxed(s, 56, 280, 240, 90, "Facade", "CustomerProfilePort", tone="warn")
    s.connect(domain, facade, frm="s", to="n")

    s.panel(350, 100, 280, 320, "Anti-corruption layer", tone="warn")
    adapter = boxed(s, 370, 150, 240, 90, "Adapter", "talks to legacy", tone="warn")
    trans = boxed(s, 370, 280, 240, 90, "Translator", "K_12_ADDR → Address", tone="warn")
    s.connect(facade, adapter)
    s.connect(adapter, trans, frm="s", to="n")
    s.connect(trans, facade, frm="w", to="e", dashed=True)

    s.panel(664, 100, 280, 320, "Legacy ERP", tone="bad")
    ugly = boxed(s, 684, 210, 240, 100, "Legacy fields", "K_12_ADDR · STAT_ID", tone="bad")
    s.connect(adapter, ugly)
    s.connect(ugly, adapter, dashed=True)
    return s


def d_cap_theorem_triangle() -> Svg:
    s = Svg(980, 560, "CAP theorem", "Under a partition, P is not optional. You pick C or A.")
    cx, cy, r = 220, 300, 128
    pts = [
        (cx, cy - r, "C", "Consistency"),
        (cx - r * 0.92, cy + r * 0.62, "A", "Availability"),
        (cx + r * 0.92, cy + r * 0.62, "P", "Partition tolerance"),
    ]
    tri = " ".join(f"{x:.1f},{y:.1f}" for x, y, _, _ in pts)
    s.add(f'<polygon points="{tri}" fill="{GILT_WASH}" stroke="{COPPER}" stroke-width="1.6"/>')
    for x, y, letter, name in pts:
        s.add(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="22" fill="{CARD}" stroke="{DESK}" stroke-width="1.4"/>')
        s.text(x, y + 5, letter, size=16, fill=DESK, weight="700", anchor="middle")
        s.text(x, y + 42, name, size=12, fill=INK_SOFT, weight="500", anchor="middle")
    s.text(cx, cy + 8, "pick two", size=12, fill=COPPER, weight="600", anchor="middle", italic=True)

    cp = boxed(s, 460, 96, 230, 150, "CP", "refuse rather than guess", "etcd · ZooKeeper", "Regional DynamoDB writes", "Aurora storage quorum", tone="warn")
    ap = boxed(s, 720, 96, 230, 150, "AP", "answer rather than wait", "Cassandra", "2007 Dynamo paper", "Global Tables MREC", tone="good")
    ca = boxed(s, 590, 330, 250, 140, "Not a distributed third option", "CA is a single node", "single-node PostgreSQL", "no partition to tolerate", tone="paper")
    _ = (cp, ap, ca)
    s.footnote("When the network splits, you cannot keep both consistency and availability.")
    return s


def d_cap_theorem() -> Svg:
    s = Svg(960, 500, "CAP under a partition", "The same choice, drawn as a decision tree.")
    root = boxed(s, 340, 90, 280, 70, "CAP under a partition", tone="desk")
    cp = boxed(s, 40, 230, 270, 90, "CP", "consistency + partition tolerance", "refuse rather than guess", tone="warn")
    ap = boxed(s, 345, 230, 270, 90, "AP", "availability + partition tolerance", "answer rather than wait", tone="good")
    ca = boxed(s, 650, 230, 270, 90, "CA", "single node", "not a distributed choice", tone="paper")
    boxed(s, 40, 360, 270, 90, "etcd · ZooKeeper", "Regional DynamoDB writes", "Aurora", tone="warn")
    boxed(s, 345, 360, 270, 90, "Cassandra", "Dynamo 2007 paper", "Global Tables MREC", tone="good")
    boxed(s, 650, 360, 270, 90, "Single PostgreSQL", tone="paper")
    s.connect(root, cp, frm="s", to="n")
    s.connect(root, ap, frm="s", to="n")
    s.connect(root, ca, frm="s", to="n")
    s.connect(cp, (40, 360, 270, 90), frm="s", to="n")
    s.connect(ap, (345, 360, 270, 90), frm="s", to="n")
    s.connect(ca, (650, 360, 270, 90), frm="s", to="n")
    return s


def d_data_ownership_events() -> Svg:
    s = Svg(980, 480, "Data ownership through events", "Each service owns its store. Neighbors read a local projection.")
    s.panel(40, 100, 280, 300, "Customer service", tone="good")
    csvc = boxed(s, 60, 150, 240, 80, "Customer logic", tone="desk")
    s.cylinder(110, 270, 140, 90, "Private customer store", tone="good")
    s.panel(360, 140, 250, 220, "Local read model", tone="warn")
    proj = boxed(s, 380, 190, 210, 110, "Customer projection", "only the fields orders need", tone="warn")
    s.panel(660, 100, 280, 300, "Order service", tone="good")
    osvc = boxed(s, 680, 150, 240, 80, "Order logic", tone="desk")
    s.cylinder(730, 270, 140, 90, "Private order store", tone="good")
    s.connect(csvc, proj, label="CustomerUpdated")
    s.connect(proj, osvc)
    return s


def d_saga_vs() -> Svg:
    s = Svg(1000, 580, "Choreography versus orchestration", "No coordinator, or an explicit state machine.")
    s.panel(28, 88, 470, 450, "Choreography: no application coordinator", tone="good")
    o1 = boxed(s, 56, 130, 180, 70, "Order service", tone="desk")
    i1 = boxed(s, 280, 230, 180, 70, "Inventory service", tone="good")
    p1 = boxed(s, 56, 340, 180, 70, "Payment service", tone="bad")
    s.connect(o1, i1, label="OrderCreated")
    s.connect(i1, p1, label="InventoryReserved")
    s.connect(p1, o1, frm="n", to="s", label="PaymentProcessed")
    s.connect(p1, i1, dashed=True, color=BAD, label="PaymentFailed → release")

    s.panel(520, 88, 452, 450, "Orchestration: explicit state machine", tone="warn")
    orch = boxed(s, 610, 130, 260, 70, "Saga orchestrator", tone="warn")
    o2 = boxed(s, 548, 250, 170, 64, "Order service", tone="desk")
    i2 = boxed(s, 768, 250, 170, 64, "Inventory service", tone="good")
    p2 = boxed(s, 658, 370, 180, 64, "Payment service", "charge is the pivot", tone="bad")
    s.connect(orch, o2, frm="s", to="n", label="1. pending order")
    s.connect(orch, i2, frm="s", to="n", label="2. reserve")
    s.connect(orch, p2, frm="s", to="n", label="3. charge")
    s.connect(orch, i2, dashed=True, color=BAD)
    s.connect(orch, o2, dashed=True, color=BAD)
    s.footnote("Compensate in reverse after a completed step fails.")
    return s


def draw_sequence(s: Svg, participants: list[str], messages: list[tuple], y0: float = 100) -> None:
    n = len(participants)
    usable = s.w - 80
    step = usable / n
    xs = [40 + step / 2 + i * step for i in range(n)]
    heads = []
    for i, name in enumerate(participants):
        box = boxed(s, xs[i] - 88, y0, 176, 54, name, tone="desk")
        heads.append(box)
        s.add(
            f'<line x1="{xs[i]:.1f}" y1="{y0 + 54:.1f}" x2="{xs[i]:.1f}" y2="{s.h - 40:.1f}" '
            f'stroke="{PAPER_EDGE}" stroke-width="1.2"/>'
        )
    y = y0 + 90
    for msg in messages:
        if msg[0] == "note":
            _, i, j, text = msg
            x1, x2 = min(xs[i], xs[j]), max(xs[i], xs[j])
            s.rect(x1 - 10, y - 16, x2 - x1 + 20, 36, fill=WARN_WASH, stroke=WARN, rx=8, shadow=False)
            s.text((x1 + x2) / 2, y + 6, text, size=11, fill=INK, anchor="middle")
            y += 52
            continue
        frm, to, text, *rest = msg
        dashed = bool(rest and rest[0])
        color = BAD if dashed else COPPER
        x1, x2 = xs[frm], xs[to]
        if frm == to:
            s.add(
                f'<path d="M{x1:.1f} {y:.1f} c 36 0 36 28 0 28" fill="none" stroke="{color}" '
                f'stroke-width="1.3" marker-end="url(#arrowCopper)"/>'
            )
            s.text(x1 + 44, y + 12, text, size=11, fill=INK_SOFT)
        else:
            s.arrow(x1, y, x2, y, color=color, dashed=dashed, marker="arrowCopper" if not dashed else "arrowBad")
            s.text((x1 + x2) / 2, y - 8, text, size=11, fill=INK_SOFT, anchor="middle")
        y += 36


def d_saga_orchestration() -> Svg:
    s = Svg(1000, 620, "Orchestrated saga", "The orchestrator owns the state machine and compensates in reverse.")
    draw_sequence(
        s,
        ["Client", "Orchestrator", "Order", "Inventory", "Payment"],
        [
            (0, 1, "Place order"),
            (1, 2, "Create pending order"),
            (2, 1, "Order created"),
            (1, 3, "Reserve stock"),
            (3, 1, "Reserved"),
            (1, 4, "Charge card (pivot)"),
            (4, 1, "Charged"),
            (1, 2, "Mark approved"),
            (1, 0, "Order complete"),
            ("note", 1, 4, "On failure after a completed step, compensate in reverse order"),
        ],
    )
    return s


def d_saga_choreography() -> Svg:
    s = Svg(960, 520, "Choreographed saga", "Reversible reserve first, charge second. No application coordinator.")
    draw_sequence(
        s,
        ["Order", "Event bus", "Inventory", "Payment"],
        [
            (0, 1, "OrderCreated"),
            (1, 2, "OrderCreated"),
            (2, 1, "InventoryReserved"),
            (1, 3, "InventoryReserved"),
            (3, 1, "PaymentProcessed"),
            (1, 0, "PaymentProcessed"),
            ("note", 1, 3, "Reversible reserve first, charge second. No application coordinator."),
        ],
    )
    return s


def d_dual_write() -> Svg:
    s = Svg(980, 520, "Dual-write problem and outbox", "Two writes are two failure domains. One local transaction is not.")
    s.panel(28, 84, 924, 190, "Dual write: the gap", tone="bad")
    a1 = boxed(s, 56, 130, 140, 70, "App", "Save order", tone="desk")
    b1 = boxed(s, 280, 130, 180, 70, "Database", "Committed", tone="good")
    c1 = boxed(s, 540, 130, 180, 70, "Broker", "Timeout / crash", tone="bad")
    boxed(s, 760, 130, 160, 70, "Zombie", "order exists, no event", tone="bad")
    s.connect(a1, b1)
    s.connect(a1, c1, dashed=True, color=BAD, label="second write")
    s.panel(28, 300, 924, 180, "Outbox: one local transaction", tone="good")
    a = boxed(s, 56, 350, 140, 70, "App", "BEGIN", tone="desk")
    b = boxed(s, 250, 340, 220, 90, "Database", "INSERT order", "INSERT outbox event", "COMMIT", tone="good")
    c = boxed(s, 530, 350, 180, 70, "Relay", "publishes later", tone="warn")
    d = boxed(s, 770, 350, 150, 70, "Broker", "OrderCreated", tone="desk")
    s.connect(a, b)
    s.connect(b, c)
    s.connect(c, d)
    return s


def d_outbox_pattern() -> Svg:
    s = Svg(1000, 520, "Outbox pattern", "Atomic local write, then at-least-once relay. Consumers dedupe on event_id.")
    draw_sequence(
        s,
        ["App", "Database", "Streams", "Relay", "Event bus"],
        [
            (0, 1, "TransactWrite user + outbox"),
            (1, 0, "Atomic commit"),
            (1, 2, "INSERT outbox item"),
            (2, 3, "New image"),
            (3, 4, "put_events with event_id"),
            ("note", 3, 4, "At-least-once; consumers dedupe on event_id"),
        ],
    )
    return s


def d_backpressure() -> Svg:
    s = Svg(920, 380, "Backpressure flow control", "A bounded buffer slows the producer when the consumer falls behind.")
    p = boxed(s, 50, 150, 180, 90, "Producer", tone="desk")
    b = boxed(s, 360, 140, 200, 110, "Bounded buffer", tone="warn")
    c = boxed(s, 690, 150, 180, 90, "Consumer", tone="good")
    s.connect(p, b, label="work")
    s.connect(b, c, label="work")
    s.connect(b, p, frm="w", to="e", dashed=True, color=WARN, label="buffer full: slow down")
    s.connect(c, b, frm="w", to="e", dashed=True, label="I am behind")
    return s


def d_api_gateway_security() -> Svg:
    s = Svg(1000, 360, "API gateway as the security boundary", "Terminate at the edge. Re-verify at the resource.")
    items = [
        ("External client", "TLS", "desk"),
        ("API gateway", "TLS terminate", "warn"),
        ("Authenticate", "identity", "desk"),
        ("Rate limit · WAF", "gilt"),
        ("Internal service", "mTLS + token", "re-verify · authorize", "good"),
    ]
    flow_chain(s, items, 140, w=168, h=100, gap=20, x0=28)
    return s


def d_agentic_tool_gateway() -> Svg:
    s = Svg(1040, 640, "Agent tool gateway", "Probabilistic planning stays behind a deterministic, authorized execute path.")
    draw_sequence(
        s,
        ["User", "Planner", "Retrieved content", "Tool gateway", "Domain service", "Human"],
        [
            (0, 1, "Goal"),
            (1, 2, "Fetch context"),
            (2, 1, "Documents and tool results"),
            (1, 3, "Proposed tool call + idempotency key"),
            (3, 3, "Policy, schema, budget"),
            (3, 5, "Approval if high-risk"),
            (5, 3, "Approved or denied"),
            (3, 4, "Versioned, authorized execute"),
            (4, 3, "Receipt"),
            (3, 1, "Structured observation"),
            (1, 0, "Response"),
        ],
    )
    return s


def d_telemetry_pipeline() -> Svg:
    s = Svg(980, 500, "Telemetry pipeline", "One collector. Three signals. One operator view.")
    s.panel(36, 100, 220, 340, "Instrumented services", tone="desk")
    a = boxed(s, 56, 150, 180, 60, "Service A", tone="desk")
    b = boxed(s, 56, 240, 180, 60, "Service B", tone="desk")
    c = boxed(s, 56, 330, 180, 60, "Service C", tone="desk")
    col = boxed(s, 340, 220, 220, 100, "Collector", "receive · sample", "filter · export", tone="warn")
    m = boxed(s, 640, 120, 140, 70, "Metrics", tone="desk")
    t = boxed(s, 640, 230, 140, 70, "Traces", tone="desk")
    lg = boxed(s, 640, 340, 140, 70, "Structured logs", tone="desk")
    op = boxed(s, 830, 220, 120, 90, "Operator", tone="good")
    for box in (a, b, c):
        s.connect(box, col)
    s.connect(col, m, frm="n", to="w")
    s.connect(col, t)
    s.connect(col, lg, frm="s", to="w")
    s.connect(m, op, frm="e", to="n")
    s.connect(t, op)
    s.connect(lg, op, frm="e", to="s")
    return s


def d_sidecar_vs_ebpf() -> Svg:
    s = Svg(980, 460, "Sidecar versus eBPF collection", "A proxy in every pod, or observation from the kernel.")
    s.panel(36, 100, 440, 300, "Sidecar collection", tone="bad")
    a1 = boxed(s, 56, 160, 120, 64, "App", tone="desk")
    px = boxed(s, 210, 160, 150, 64, "Proxy in every pod", tone="bad")
    peer = boxed(s, 210, 280, 150, 64, "Peer proxy", tone="bad")
    a2 = boxed(s, 390, 280, 70, 64, "App", tone="desk")
    s.connect(a1, px)
    s.connect(px, peer, frm="s", to="n")
    s.connect(peer, a2)

    s.panel(504, 100, 440, 300, "Kernel-level collection", tone="good")
    a3 = boxed(s, 530, 180, 110, 64, "App", tone="desk")
    net = boxed(s, 680, 180, 130, 64, "Ordinary traffic", tone="warn")
    a4 = boxed(s, 840, 180, 80, 64, "App", tone="desk")
    kern = boxed(s, 650, 300, 180, 64, "eBPF in the kernel", "observes", tone="good")
    s.connect(a3, net)
    s.connect(net, a4)
    s.connect(kern, net, frm="n", to="s", dashed=True, label="observe")
    return s


def d_e2e_fragility() -> Svg:
    s = Svg(1000, 380, "End-to-end test fragility", "Independent 99% hops compound. One run in ten is the environment.")
    items = [
        ("End-to-end test", "desk"),
        ("Service A", "99 percent", "warn"),
        ("Service B", "99 percent", "warn"),
        ("Service C", "99 percent", "warn"),
        ("… ten services", "warn"),
        ("Combined pass ≈ 90%", "one run in ten", "is environment", "bad"),
    ]
    flow_chain(s, items, 150, w=140, h=110, gap=18, x0=24)
    return s


def d_testing_in_production() -> Svg:
    s = Svg(1000, 420, "Testing in production", "Expose a small slice, compare to control, widen or withdraw.")
    h = boxed(s, 30, 160, 140, 80, "Hypothesis", tone="desk")
    x = boxed(s, 200, 160, 150, 80, "Expose a small slice", tone="warn")
    o = boxed(s, 380, 160, 170, 80, "Observe SLIs", "vs control", tone="desk")
    s.diamond(640, 200, 150, 110, "Within\nbounds?")
    w = boxed(s, 760, 90, 200, 70, "Widen or keep", tone="good")
    r = boxed(s, 760, 260, 200, 70, "Withdraw immediately", tone="bad")
    learn = boxed(s, 400, 320, 140, 64, "Learn", tone="good")
    s.connect(h, x)
    s.connect(x, o)
    s.arrow(550, 200, 568, 200, color=COPPER, marker="arrowCopper")
    s.connect((565, 145, 150, 110), w, frm="n", to="w", label="yes")
    s.connect((565, 145, 150, 110), r, frm="s", to="w", label="no", color=BAD)
    s.connect(w, learn, frm="s", to="e")
    s.connect(r, learn, frm="w", to="e")
    s.connect(learn, h, frm="w", to="s", dashed=True)
    return s


def d_queue_backpressure() -> Svg:
    s = Svg(960, 380, "Queue backpressure", "A durable queue absorbs bursts. Depth and age tell the producer to slow down.")
    p = boxed(s, 40, 150, 170, 86, "Producer", tone="desk")
    q = boxed(s, 300, 140, 200, 110, "Durable queue", tone="warn")
    c = boxed(s, 590, 150, 170, 86, "Consumer", "pull at own rate", tone="good")
    d = boxed(s, 800, 150, 130, 86, "Downstream", "limit", tone="bad")
    s.connect(p, q, label="publish")
    s.connect(q, c, label="pull")
    s.connect(c, d)
    s.connect(q, p, frm="w", to="e", dashed=True, color=WARN, label="depth and age rise")
    return s


def d_claim_check() -> Svg:
    s = Svg(960, 520, "Claim-check pattern", "The queue carries a key. The payload lives in object storage.")
    draw_sequence(
        s,
        ["Producer", "Object store", "Queue", "Consumer"],
        [
            (0, 1, "1. Put payload under a generated key"),
            (1, 0, "2. Object is durable"),
            (0, 2, "3. Send claim check, key only"),
            (2, 3, "4. Deliver small message"),
            (3, 1, "5. Get object from the configured bucket"),
            (1, 3, "6. Payload"),
            ("note", 1, 1, "Lifecycle expires the object after queue plus DLQ retention"),
        ],
    )
    return s


def d_network_tax() -> Svg:
    s = Svg(980, 520, "Network tax and cognitive load", "Every boundary adds a runtime tax and a human tax. Both must be earned.")
    s.panel(36, 96, 430, 360, "In process", tone="good")
    boxed(s, 70, 160, 360, 90, "Monolithic application", "single deployable", "function call · nanoseconds", tone="desk")
    boxed(s, 70, 290, 360, 100, "Useful work dominates", "no serialization hop", "one team's cognitive surface", tone="good")
    s.panel(514, 96, 430, 360, "Across a badly drawn boundary", tone="bad")
    boxed(s, 548, 150, 170, 70, "Order", tone="desk")
    boxed(s, 748, 150, 170, 70, "Payment", tone="desk")
    boxed(s, 548, 250, 370, 80, "Network call", "milliseconds · RPC + serialization", "partial failures", tone="warn")
    boxed(s, 548, 360, 370, 70, "Network tax + split ownership", "latency, hops, two on-call rotations", tone="bad")
    s.footnote("Chapter 11 fuses E (traces), S (change sets / PRs), and L (static analysis + org capacity).")
    return s


def d_rvx_flow() -> Svg:
    s = Svg(1000, 460, "RVx calculation flow", "Three signals fuse, squash into a bounded score, then a band plus components.")
    e = boxed(s, 36, 110, 200, 90, "E from traces", "kinetic efficiency", tone="desk")
    sem = boxed(s, 36, 220, 200, 90, "S from change sets", "merged PRs, not commits", tone="warn")
    l = boxed(s, 36, 330, 200, 90, "L from static analysis", "plus org capacity", tone="gilt")
    fuse = boxed(s, 300, 210, 200, 110, "Fuse under a profile", "no invented exponents", "shown on this figure", tone="warn")
    raw = boxed(s, 560, 210, 200, 110, "RVx = raw / (1 + raw)", "bounded published score", tone="desk")
    band = boxed(s, 820, 120, 150, 90, "Band", "<0.4 coarse", "0.4–0.7 at-risk", ">0.7 healthy", tone="gilt")
    act = boxed(s, 820, 280, 150, 90, "Diagnose", "and act, or not", tone="good")
    s.connect(e, fuse)
    s.connect(sem, fuse)
    s.connect(l, fuse)
    s.connect(fuse, raw)
    s.connect(raw, band, frm="n", to="w")
    s.connect(raw, act, frm="s", to="w")
    s.footnote("High-load gate: if L > 0.7, treat as an ownership problem regardless of the composite.")
    return s


def d_khan_zones() -> Svg:
    s = Svg(980, 520, "Khan granularity matrix", "Read the components. The zone names the problem and the fix.")
    boxed(s, 40, 110, 440, 170, "Healthy microservice", "High E, high S, manageable L", "Leave it alone", tone="good")
    boxed(s, 500, 110, 440, 170, "Chatty boundary", "Low E, good S and L", "Cut hops or merge the chattiest edge", tone="warn")
    boxed(s, 40, 310, 440, 160, "Distributed-monolith fragment", "Good E, low S", "Merge, or find the missed seam", tone="bad")
    boxed(s, 500, 310, 440, 160, "Ownership problem", "High L, whatever else is true", "Shrink the surface or change the owner", tone="gilt")
    return s


def d_vaquarkhan_matrix() -> Svg:
    s = Svg(980, 540, "Khan granularity matrix (zones)", "Same four diagnoses as Chapter 11. Not a nano-service scoreboard.")
    boxed(s, 40, 100, 440, 180, "Healthy", "High E · high S · manageable L", "RVx > 0.7", "maintain", tone="good")
    boxed(s, 500, 100, 440, 180, "Chatty / too fine", "Low E with otherwise sound S and L", "cut hops or merge", tone="desk")
    boxed(s, 40, 310, 440, 170, "Distributed monolith", "Low S · RVx < 0.4", "wrong boundary · merge or re-cut", tone="bad")
    boxed(s, 500, 310, 440, 170, "Ownership / high load", "L > 0.7 gate", "organizational fix, not a split contest", tone="warn")
    s.footnote("Bands: <0.4 coarse/monolith · 0.4–0.7 at-risk · >0.7 healthy.")
    return s


def d_service_split() -> Svg:
    s = Svg(980, 500, "A split that earns the boundary", "Split when the two ends change on their own schedules and the edge is chatty.")
    s.panel(36, 96, 420, 350, "Before: one overloaded surface", tone="bad")
    boxed(s, 70, 160, 350, 230, "User service", "authentication", "profile", "preferences", "notifications", "activity · settings", "one store, many reasons to change", tone="bad")
    s.panel(524, 96, 420, 350, "After: seams that change apart", tone="good")
    boxed(s, 548, 150, 180, 90, "Auth", "own store", tone="good")
    boxed(s, 748, 150, 180, 90, "Profile", "own store", tone="good")
    boxed(s, 548, 280, 180, 90, "Preferences", "own store", tone="good")
    boxed(s, 748, 280, 180, 90, "Notifications", "own store", tone="good")
    s.footnote("No invented scores. The test is independence of change plus a quieter critical path.")
    return s


def d_service_merge() -> Svg:
    s = Svg(980, 500, "A merge that earns the contraction", "Merge when services always change together and the hop buys no independence.")
    s.panel(36, 96, 430, 340, "Before: over-split surfaces", tone="bad")
    boxed(s, 56, 150, 180, 80, "User", tone="desk")
    boxed(s, 256, 150, 180, 80, "Avatar", "always ships with User", tone="bad")
    boxed(s, 56, 270, 180, 80, "Status", "always ships with User", tone="bad")
    boxed(s, 256, 270, 180, 80, "Preferences", "lock-step deploys", tone="bad")
    s.panel(514, 96, 430, 340, "After: one profile context", tone="good")
    boxed(s, 574, 200, 310, 130, "User profile service", "one API", "one store", "no hop between things that co-change", tone="good")
    s.footnote("Not a nano-swarm scoreboard. Merge is a first-class remedy when S is the weak dimension.")
    return s


def km3_levels_row(s: Svg, y: float) -> list:
    labels = [
        ("1 Ad hoc", "intuition only", "paper"),
        ("2 Instrumented", "signals measured", "desk"),
        ("3 Governed", "metric gates changes", "warn"),
        ("4 Portfolio-managed", "estate investment", "gilt"),
        ("5 Self-correcting", "safety-gated loop", "good"),
    ]
    boxes = []
    x = 28
    for title, body, tone in labels:
        box = boxed(s, x, y, 176, 100, title, body, tone=tone)
        if boxes:
            s.connect(boxes[-1], box)
        boxes.append(box)
        x += 192
    return boxes


def d_km3_levels() -> Svg:
    s = Svg(1000, 320, "KM3 maturity levels", "Ad hoc → Instrumented → Governed → Portfolio-managed → Self-correcting")
    km3_levels_row(s, 130)
    return s


def d_km3_staircase() -> Svg:
    s = Svg(920, 560, "KM3 staircase", "Each step is gated by the one below it.")
    steps = [
        (40, 430, 200, "1 Ad hoc", "guessed boundaries", "paper"),
        (150, 350, 230, "2 Instrumented", "signals measured", "desk"),
        (270, 270, 250, "3 Governed", "metric gates changes", "warn"),
        (400, 190, 270, "4 Portfolio-managed", "estate investment", "gilt"),
        (540, 110, 300, "5 Self-correcting", "safety-gated loop", "good"),
    ]
    prev = None
    for x, y, w, title, body, tone in steps:
        box = boxed(s, x, y, w, 68, title, body, tone=tone)
        if prev:
            s.connect(prev, box, frm="n", to="s")
        prev = box
    s.footnote("A level cannot be claimed without the preconditions of the levels below it.")
    return s


def d_km3_capabilities() -> Svg:
    s = Svg(1000, 360, "KM3 capabilities", "Each level is defined by a capability whose absence lets a class of incident through.")
    items = [
        ("Ad hoc", "intuition only", "paper"),
        ("Instrumented", "signals measured", "desk"),
        ("Governed", "metric gates changes", "warn"),
        ("Portfolio-managed", "estate investment", "gilt"),
        ("Self-correcting", "safety-gated loop", "good"),
    ]
    flow_chain(s, [(t, b, tone) for t, b, tone in items], 140, w=176, h=100, gap=16, x0=24)
    return s


def d_shuffle_cells() -> Svg:
    s = Svg(960, 500, "Cells and shuffle sharding", "A request enters one cell. Inside the cell, a tenant uses a subset of shards.")
    req = boxed(s, 40, 200, 140, 80, "Request", tone="desk")
    pick = boxed(s, 230, 200, 180, 80, "Cell by region", "or cohort", tone="warn")
    c1 = boxed(s, 470, 130, 150, 80, "Active cell", tone="good")
    c2 = boxed(s, 470, 280, 150, 80, "Other cells", "stay dark", tone="paper")
    subset = boxed(s, 680, 130, 120, 80, "Tenant subset", "k shards", tone="warn")
    s1 = boxed(s, 840, 70, 90, 58, "Shard", tone="desk")
    s2 = boxed(s, 840, 140, 90, 58, "Shard", tone="desk")
    s3 = boxed(s, 840, 210, 90, 58, "Shard", tone="desk")
    s.connect(req, pick)
    s.connect(pick, c1)
    s.connect(pick, c2, dashed=True, color=INK_SOFT)
    s.connect(c1, subset)
    s.connect(subset, s1, frm="e", to="w")
    s.connect(subset, s2)
    s.connect(subset, s3, frm="e", to="w")
    return s


def d_shuffle_tenants() -> Svg:
    s = Svg(920, 420, "Shuffle sharding tenant assignment", "Tenants get overlapping subsets. One shared shard is not a shared fate.")
    s.panel(40, 110, 280, 230, "Tenant A", tone="desk")
    boxed(s, 70, 160, 80, 54, "3", tone="desk")
    a17 = boxed(s, 170, 160, 80, 54, "17", tone="warn")
    boxed(s, 120, 250, 80, 54, "40", tone="desk")
    s.panel(600, 110, 280, 230, "Tenant B", tone="desk")
    boxed(s, 630, 160, 80, 54, "8", tone="desk")
    b17 = boxed(s, 730, 160, 80, 54, "17", tone="warn")
    boxed(s, 680, 250, 80, 54, "52", tone="desk")
    shared = boxed(s, 380, 175, 160, 80, "Shared: 17", "overlap, not isolation fail", tone="bad")
    s.connect(a17, shared)
    s.connect(b17, shared)
    s.footnote("A noisy tenant on 17 does not take the rest of A or B with it.")
    return s


def d_chaos_loop() -> Svg:
    s = Svg(980, 400, "Chaos engineering loop", "Hypothesis, one bounded fault, measure, learn. Abort on customer harm.")
    h = boxed(s, 40, 160, 180, 80, "Write the hypothesis", tone="desk")
    i = boxed(s, 280, 160, 190, 80, "Inject one bounded fault", tone="warn")
    m = boxed(s, 530, 160, 200, 80, "Measure against it", tone="desk")
    l = boxed(s, 790, 160, 150, 80, "Learn", "fix or refine", tone="good")
    abort = boxed(s, 390, 300, 220, 64, "Abort on customer harm", tone="bad")
    s.connect(h, i)
    s.connect(i, m)
    s.connect(m, l)
    s.connect(l, h, frm="n", to="n", dashed=True)
    s.connect(abort, i, frm="n", to="s", dashed=True, color=BAD)
    s.connect(abort, m, frm="n", to="s", dashed=True, color=BAD)
    return s


def d_metastable() -> Svg:
    s = Svg(980, 400, "Metastable retry loop", "The trigger can be gone and the system still stays collapsed.")
    t = boxed(s, 40, 150, 150, 86, "Brief trigger", tone="warn")
    sl = boxed(s, 250, 150, 170, 86, "Dependency slows", tone="bad")
    w = boxed(s, 480, 150, 190, 86, "Callers wait", "and hold threads", tone="gilt")
    r = boxed(s, 730, 150, 190, 86, "Retries add load", tone="bad")
    x = boxed(s, 360, 300, 280, 64, "Trigger is gone · system stays collapsed", tone="bad")
    s.connect(t, sl)
    s.connect(sl, w)
    s.connect(w, r)
    s.connect(r, sl, frm="n", to="n", dashed=True, color=BAD)
    s.connect(t, x, frm="s", to="w", dashed=True)
    return s


def d_iac_pipeline() -> Svg:
    s = Svg(1000, 380, "IaC golden-path pipeline", "Plan, policy, human approval, then a governed apply.")
    pr = boxed(s, 30, 160, 140, 80, "Pull request", tone="desk")
    plan = boxed(s, 200, 160, 150, 80, "Automated plan", tone="warn")
    pol = boxed(s, 380, 160, 170, 80, "Policy against plan", tone="bad")
    app = boxed(s, 590, 160, 150, 80, "Human approval", tone="gilt")
    apply = boxed(s, 770, 90, 190, 70, "Governed apply", tone="good")
    cloud = boxed(s, 770, 250, 190, 70, "Cloud", tone="desk")
    s.connect(pr, plan)
    s.connect(plan, pol)
    s.connect(pol, pr, frm="n", to="n", dashed=True, color=BAD, label="fail")
    s.connect(pol, app, label="pass")
    s.connect(app, apply, frm="n", to="w")
    s.connect(apply, cloud, frm="s", to="n")
    return s


def d_accounts_blast() -> Svg:
    s = Svg(960, 420, "Accounts as blast-radius boundaries", "A fault or cost overrun stays inside the account that incurred it.")
    pipe = boxed(s, 40, 180, 200, 90, "Golden-path pipeline", tone="warn")
    a = boxed(s, 320, 80, 170, 80, "Account A", tone="good")
    b = boxed(s, 320, 190, 170, 80, "Account B", tone="good")
    c = boxed(s, 320, 300, 170, 80, "Account C", tone="good")
    x = boxed(s, 620, 80, 280, 80, "Fault or cost overrun", "contained", tone="bad")
    s.connect(pipe, a)
    s.connect(pipe, b)
    s.connect(pipe, c)
    s.connect(a, x, dashed=True, color=BAD, label="contained")
    return s


def d_obs2() -> Svg:
    s = Svg(1000, 500, "Observability 2.0 pipeline", "Metrics, traces, and wide events, cross-checked by a kernel graph.")
    s.panel(36, 110, 200, 320, "Services", tone="desk")
    s1 = boxed(s, 56, 160, 160, 56, "Checkout", tone="desk")
    s2 = boxed(s, 56, 240, 160, 56, "Inventory", tone="desk")
    s3 = boxed(s, 56, 320, 160, 56, "Payments", tone="desk")
    col = boxed(s, 300, 220, 190, 90, "OpenTelemetry", "collector", tone="warn")
    m = boxed(s, 560, 110, 140, 64, "Metrics", tone="desk")
    t = boxed(s, 560, 200, 140, 64, "Traces", tone="desk")
    w = boxed(s, 560, 290, 140, 64, "Wide events", tone="desk")
    bpf = boxed(s, 560, 380, 180, 64, "eBPF dependency graph", tone="gilt")
    x = boxed(s, 800, 230, 160, 80, "Cross-check", tone="good")
    for box in (s1, s2, s3):
        s.connect(box, col)
    s.connect(col, m, frm="n", to="w")
    s.connect(col, t)
    s.connect(col, w, frm="s", to="w")
    s.connect(t, x)
    s.connect(bpf, x, frm="e", to="s")
    return s


def d_ebpf_vs_trace() -> Svg:
    s = Svg(980, 440, "eBPF versus the trace graph", "The kernel sees edges the application never declared.")
    s.panel(40, 100, 360, 260, "Application traces", tone="desk")
    a1 = boxed(s, 70, 160, 140, 60, "Checkout", tone="desk")
    a2 = boxed(s, 240, 130, 140, 56, "Inventory", tone="desk")
    a3 = boxed(s, 240, 230, 140, 56, "Payments", tone="desk")
    s.connect(a1, a2)
    s.connect(a1, a3)
    s.panel(440, 100, 500, 260, "Kernel eBPF view", tone="warn")
    b1 = boxed(s, 470, 160, 130, 60, "Checkout", tone="desk")
    b2 = boxed(s, 650, 120, 120, 50, "Inventory", tone="desk")
    b3 = boxed(s, 650, 190, 120, 50, "Payments", tone="desk")
    b4 = boxed(s, 650, 270, 180, 56, "Hidden DNS / metadata", tone="bad")
    diff = boxed(s, 400, 380, 220, 40, "Edge only the kernel saw", tone="bad")
    s.connect(b1, b2)
    s.connect(b1, b3)
    s.connect(b1, b4)
    s.connect(b4, (400, 380, 220, 40), frm="s", to="e", dashed=True)
    return s


def d_multi_agent() -> Svg:
    s = Svg(980, 460, "Multi-agent coordination", "An orchestrating planner, or peers that talk to each other.")
    s.panel(40, 100, 430, 300, "Orchestrator", tone="warn")
    o = boxed(s, 150, 150, 200, 70, "Planner agent", tone="warn")
    boxed(s, 70, 280, 110, 64, "Specialist A", tone="desk")
    boxed(s, 200, 280, 110, 64, "Specialist B", tone="desk")
    boxed(s, 330, 280, 110, 64, "Specialist C", tone="desk")
    s.connect(o, (70, 280, 110, 64), frm="s", to="n")
    s.connect(o, (200, 280, 110, 64), frm="s", to="n")
    s.connect(o, (330, 280, 110, 64), frm="s", to="n")
    s.panel(510, 100, 430, 300, "Peers", tone="desk")
    p1 = boxed(s, 540, 180, 130, 70, "Agent A", tone="desk")
    p2 = boxed(s, 760, 180, 130, 70, "Agent B", tone="desk")
    p3 = boxed(s, 650, 300, 130, 70, "Agent C", tone="desk")
    s.connect(p1, p2)
    s.connect(p2, p3, frm="s", to="e")
    s.connect(p3, p1, frm="w", to="s")
    return s


def d_rag() -> Svg:
    s = Svg(720, 640, "RAG architecture", "Ingest into an index. Query with ACL prefilter, rerank, then cite.")
    s.panel(40, 90, 640, 220, "Ingestion", tone="desk")
    d = boxed(s, 60, 140, 130, 70, "Documents", tone="desk")
    c = boxed(s, 220, 140, 120, 70, "Chunks", tone="desk")
    e = boxed(s, 370, 140, 120, 70, "Embed", tone="desk")
    idx = boxed(s, 520, 140, 140, 70, "Vector index", tone="good")
    s.connect(d, c)
    s.connect(c, e)
    s.connect(e, idx)
    s.panel(40, 340, 640, 250, "Query", tone="warn")
    q = boxed(s, 60, 390, 110, 60, "Query", tone="desk")
    qe = boxed(s, 200, 390, 120, 60, "Embed query", tone="desk")
    r = boxed(s, 350, 390, 160, 60, "Retrieve + ACL", tone="warn")
    rr = boxed(s, 540, 390, 120, 60, "Rerank", tone="desk")
    g = boxed(s, 200, 490, 160, 60, "Generator", tone="desk")
    a = boxed(s, 400, 490, 160, 60, "Cited answer", tone="good")
    s.connect(q, qe)
    s.connect(qe, r)
    s.connect(r, rr)
    s.connect(idx, r, frm="s", to="n")
    s.connect(rr, g, frm="s", to="e")
    s.connect(g, a)
    return s


def d_hyde() -> Svg:
    s = Svg(1040, 360, "HyDE RAG pipeline", "Embed a hypothetical passage, then retrieve with the same ACL discipline.")
    items = [
        ("Query", "desk"),
        ("Hypothetical passage", "warn"),
        ("Embed hypothetical", "desk"),
        ("Index + ACL prefilter", "warn"),
        ("Rerank", "desk"),
        ("Generator + citations", "Cited, grounded answer", "good"),
    ]
    flow_chain(s, items, 140, w=150, h=100, gap=16, x0=24)
    return s


def d_vector_ownership() -> Svg:
    s = Svg(980, 460, "Vector store ownership", "A shared index couples writers. Service-owned indexes keep the blast radius local.")
    s.panel(36, 100, 440, 300, "Shared store", tone="bad")
    a = boxed(s, 56, 150, 130, 60, "Service A", tone="desk")
    b = boxed(s, 56, 230, 130, 60, "Service B", tone="desk")
    c = boxed(s, 56, 310, 130, 60, "Service C", tone="desk")
    v = boxed(s, 260, 210, 180, 90, "One index", tone="bad")
    s.connect(a, v)
    s.connect(b, v)
    s.connect(c, v)
    s.panel(504, 100, 440, 300, "Service-owned stores", tone="good")
    a1 = boxed(s, 524, 150, 130, 60, "Service A", tone="desk")
    b1 = boxed(s, 524, 230, 130, 60, "Service B", tone="desk")
    c1 = boxed(s, 524, 310, 130, 60, "Service C", tone="desk")
    va = boxed(s, 720, 150, 190, 60, "Index A", tone="good")
    vb = boxed(s, 720, 230, 190, 60, "Index B", tone="good")
    vc = boxed(s, 720, 310, 190, 60, "Index C", tone="good")
    s.connect(a1, va)
    s.connect(b1, vb)
    s.connect(c1, vc)
    return s


def d_shared_vector() -> Svg:
    s = Svg(860, 420, "Shared vector store", "Namespaces isolate keys. They do not isolate fate.")
    boxed(s, 60, 140, 180, 70, "Support service", tone="desk")
    boxed(s, 60, 230, 180, 70, "Sales service", tone="good")
    boxed(s, 60, 320, 180, 70, "Marketing service", tone="warn")
    store = boxed(
        s,
        400,
        180,
        380,
        160,
        "Shared vector store",
        "customer embeddings",
        "namespaces: support.* · sales.* · marketing.*",
        tone="gilt",
    )
    s.connect((60, 140, 180, 70), store)
    s.connect((60, 230, 180, 70), store)
    s.connect((60, 320, 180, 70), store)
    return s


def d_monolith_contraction() -> Svg:
    s = Svg(960, 400, "Monolith contraction", "Two chatty services become modules in one deployable.")
    s.panel(40, 110, 380, 220, "Two services", tone="bad")
    s1 = boxed(s, 70, 180, 140, 80, "Orders", tone="bad")
    s2 = boxed(s, 250, 180, 140, 80, "Inventory", tone="bad")
    s.connect(s1, s2, label="chatty sync")
    s.panel(540, 110, 380, 220, "One deployable", tone="good")
    m1 = boxed(s, 570, 180, 140, 80, "Orders module", tone="good")
    m2 = boxed(s, 750, 180, 140, 80, "Inventory module", tone="good")
    s.connect(m1, m2, label="in-process", color=GOOD)
    s.arrow(430, 220, 530, 220, color=COPPER, marker="arrowCopper")
    return s


def d_schema_per_module() -> Svg:
    s = Svg(860, 480, "Schema-per-module isolation", "One engine. Separate schemas. Blocked cross-module JOINs.")
    s.panel(60, 100, 320, 200, "One deployable", tone="desk")
    om = boxed(s, 90, 150, 260, 50, "Orders module", tone="desk")
    im = boxed(s, 90, 220, 260, 50, "Inventory module", tone="desk")
    s.panel(480, 100, 320, 200, "Shared engine", tone="good")
    os_ = boxed(s, 510, 150, 260, 50, "orders schema", tone="good")
    is_ = boxed(s, 510, 220, 260, 50, "inventory schema", tone="good")
    s.connect(om, os_, label="orders_app grants")
    s.connect(im, is_, label="inventory_app grants")
    s.connect(om, is_, frm="e", to="w", dashed=True, color=BAD, label="blocked JOIN")
    return s


def d_strangler_fig() -> Svg:
    s = Svg(920, 420, "Strangler fig", "A facade sits in front of legacy and the new services.")
    clients = boxed(s, 40, 180, 140, 80, "Clients", tone="desk")
    gw = boxed(s, 260, 170, 180, 100, "Gateway / facade", tone="warn")
    n1 = boxed(s, 540, 90, 170, 80, "New service A", "migrated paths", tone="good")
    n2 = boxed(s, 540, 190, 170, 80, "New service B", "migrated paths", tone="good")
    legacy = boxed(s, 540, 300, 200, 80, "Legacy", "default catch-all", tone="bad")
    s.connect(clients, gw)
    s.connect(gw, n1, frm="n", to="w", label="migrated")
    s.connect(gw, n2, label="migrated")
    s.connect(gw, legacy, frm="s", to="w", dashed=True, color=BAD, label="catch-all")
    return s


def d_strangler_data() -> Svg:
    s = Svg(860, 560, "Strangler data plane", "Route at the facade. Reconcile writes from both sides.")
    c = boxed(s, 340, 90, 160, 56, "Clients", tone="desk")
    g = boxed(s, 340, 180, 160, 64, "Gateway", tone="warn")
    n = boxed(s, 80, 300, 180, 70, "New system", tone="good")
    l = boxed(s, 580, 300, 180, 70, "Legacy", tone="bad")
    out = boxed(s, 80, 420, 180, 60, "Outbox", tone="desk")
    cdc = boxed(s, 580, 420, 180, 60, "CDC or outbox", tone="desk")
    sync = boxed(s, 330, 430, 180, 70, "Reconciliation", tone="desk")
    s.connect(c, g, frm="s", to="n")
    s.connect(g, n, frm="w", to="n", label="matched")
    s.connect(g, l, frm="e", to="n", dashed=True, label="catch-all")
    s.connect(n, out, frm="s", to="n")
    s.connect(l, cdc, frm="s", to="n")
    s.connect(out, sync)
    s.connect(cdc, sync)
    return s


def d_wasted_time() -> Svg:
    s = Svg(920, 460, "Where the money goes", "Wasted time is the shaded overhead on the critical path, times how often it runs.")
    s.panel(40, 110, 400, 280, "In process", tone="good")
    s.rect(80, 180, 320, 48, fill=GOOD, stroke=GOOD, rx=8, shadow=False)
    s.text(240, 210, "Useful work", size=14, fill=CARD, weight="600", anchor="middle")
    s.text(240, 260, "Efficiency near one", size=12, fill=INK_SOFT, anchor="middle")
    s.text(240, 280, "wasted time near zero", size=12, fill=INK_SOFT, anchor="middle")
    s.panel(480, 110, 400, 280, "Badly drawn boundary", tone="bad")
    s.rect(520, 180, 140, 48, fill=GOOD, stroke=GOOD, rx=8, shadow=False)
    s.text(590, 210, "Useful", size=13, fill=CARD, weight="600", anchor="middle")
    s.rect(668, 180, 176, 48, fill=BAD, stroke=BAD, rx=8, shadow=False)
    s.text(756, 210, "Network tax", size=13, fill=CARD, weight="600", anchor="middle")
    s.text(680, 260, "Serialization, transmission, waiting", size=12, fill=INK_SOFT, anchor="middle")
    s.text(680, 280, "W = N × t_total × (1 − E)", size=12, fill=INK, weight="600", anchor="middle", family=MONO)
    s.footnote("The picture is wall-clock on the path. Whether it is an invoice line depends on how you are billed.")
    return s


def d_cost_curve() -> Svg:
    s = Svg(960, 500, "Granularity cost curve", "A sketch of total cost, not a fitted chart from a production corpus.")
    ox, oy, w, h = 80, 400, 800, 240
    s.add(f'<line x1="{ox}" y1="{oy}" x2="{ox + w}" y2="{oy}" stroke="{INK_SOFT}" stroke-width="1.2"/>')
    s.add(f'<line x1="{ox}" y1="{oy}" x2="{ox}" y2="{oy - h}" stroke="{INK_SOFT}" stroke-width="1.2"/>')
    s.text(ox - 12, oy - h / 2, "Total cost", size=12, fill=INK_SOFT, anchor="end")
    s.text(ox + 40, oy + 24, "One coarse monolith", size=12, fill=INK_SOFT)
    s.text(ox + w / 2, oy + 24, "Calibrated middle", size=12, fill=GOOD, weight="600", anchor="middle")
    s.text(ox + w - 40, oy + 24, "Many fine services", size=12, fill=INK_SOFT, anchor="end")
    # U-shape sketch
    path = (
        f"M {ox + 20} {oy - 40} "
        f"C {ox + 160} {oy - 30}, {ox + 260} {oy - 210}, {ox + w / 2} {oy - 210} "
        f"S {ox + w - 160} {oy - 30}, {ox + w - 20} {oy - 36}"
    )
    s.add(f'<path d="{path}" fill="none" stroke="{COPPER}" stroke-width="2.2" stroke-linecap="round"/>')
    s.add(f'<circle cx="{ox + w / 2}" cy="{oy - 210}" r="6" fill="{GOOD}"/>')
    boxed(s, 70, 90, 200, 70, "Coarse end", "autonomy unavailable", tone="bad")
    boxed(s, 380, 70, 200, 70, "Calibrated middle", "lowest total cost", tone="good")
    boxed(s, 690, 90, 200, 70, "Fine end", "network + ops tax", tone="bad")
    s.footnote("Sketch of the shape the book argues for. Not a regression on an organic estate.")
    return s


def d_construct_validity() -> Svg:
    s = Svg(980, 500, "Construct validity: two streams", "The score never sees the outcome values it is asked to predict.")
    s.panel(36, 100, 430, 330, "Score path", tone="warn")
    e = boxed(s, 56, 150, 180, 56, "Traces to E", tone="desk")
    sem = boxed(s, 56, 230, 180, 56, "History to S", tone="warn")
    l = boxed(s, 56, 310, 180, 56, "Static analysis to L", tone="gilt")
    r = boxed(s, 280, 220, 160, 80, "Composite", tone="warn")
    s.connect(e, r)
    s.connect(sem, r)
    s.connect(l, r)
    s.panel(514, 100, 430, 330, "Outcome path", tone="desk")
    lat = boxed(s, 560, 150, 340, 56, "Tail latency", tone="desk")
    cost = boxed(s, 560, 230, 340, 56, "Cloud cost", tone="desk")
    err = boxed(s, 560, 310, 340, 56, "Error rate", tone="desk")
    s.connect(r, lat, dashed=True, label="predict, never compute")
    s.connect(r, cost, dashed=True)
    s.connect(r, err, dashed=True)
    s.footnote("No arrow from outcomes back into the score. Same-plane checks (E and p99) are weaker than cross-plane ones.")
    return s


def d_anti_gaming() -> Svg:
    s = Svg(980, 460, "Anti-gaming: three disjoint planes", "Faking the composite means faking all three planes at once.")
    e = boxed(s, 40, 140, 260, 130, "Observability traces", "kinetic efficiency", "collector-owned sampling", tone="desk")
    sem = boxed(s, 360, 140, 260, 130, "VCS history", "append-only change sets", "merged PRs", tone="warn")
    l = boxed(s, 680, 140, 260, 130, "Static analysis + org SoR", "complexity / capacity", "capacity not self-reported", tone="gilt")
    c = boxed(s, 340, 330, 300, 80, "Composite", "all three, or no published score", tone="good")
    s.connect(e, c, frm="s", to="w")
    s.connect(sem, c, frm="s", to="n")
    s.connect(l, c, frm="s", to="e")
    s.footnote("Disjoint means three systems with partially independent owners, not three vaults the team cannot touch.")
    return s


def d_cover() -> Svg:
    s = Svg(720, 1020, "Microservices Recipes")
    # Full-bleed editorial cover: replace default paper with desk.
    s.parts.insert(
        0,
        f'<rect width="100%" height="100%" fill="{DESK_DEEP}"/>'
        f'<rect x="28" y="28" width="664" height="964" rx="8" fill="{DESK}" stroke="{COPPER}" stroke-width="1.2"/>'
        f'<rect x="40" y="40" width="640" height="940" rx="4" fill="none" stroke="{GILT}" stroke-width="0.6" opacity="0.55"/>',
    )
    # Book-mark motif
    s.add(f'<rect x="300" y="92" width="72" height="80" rx="3" fill="{DESK_DEEP}"/>')
    s.add(f'<rect x="308" y="100" width="56" height="64" rx="2" fill="{PAPER}"/>')
    s.add(f'<path d="M316 116 h40 M316 128 h30 M316 140 h36 M316 152 h24" stroke="{COPPER}" stroke-width="1.6" stroke-linecap="round"/>')
    s.add(f'<path d="M372 100 v64 l14 -7 V107 l-14 -7z" fill="{GILT}"/>')
    s.add(
        f'<text x="360" y="240" fill="{PAPER}" font-size="42" font-weight="650" text-anchor="middle" '
        f'font-family="{DISPLAY}">Microservices</text>'
    )
    s.add(
        f'<text x="360" y="292" fill="{PAPER}" font-size="42" font-weight="650" text-anchor="middle" '
        f'font-family="{DISPLAY}">Recipes</text>'
    )
    s.add(f'<path d="M220 318 h280" stroke="{COPPER}" stroke-width="1.2" stroke-linecap="round"/>')
    s.add(
        f'<text x="360" y="360" fill="{GILT}" font-size="20" font-weight="500" text-anchor="middle" '
        f'font-family="{FONT}">The Architect\'s Field Guide</text>'
    )
    s.add(
        f'<text x="360" y="560" fill="{PAPER}" font-size="18" font-weight="500" text-anchor="middle" '
        f'font-family="{FONT}">Viquar Khan</text>'
    )
    s.add(
        f'<text x="360" y="900" fill="{GILT}" font-size="14" font-weight="500" text-anchor="middle" '
        f'font-family="{FONT}">Version 2.1 · 23 chapters · 2026</text>'
    )
    s.add(
        f'<text x="360" y="940" fill="{PAPER_EDGE}" font-size="12" text-anchor="middle" '
        f'font-family="{FONT}">Adaptive Granularity Governance</text>'
    )
    return s


def d_hero() -> Svg:
    s = Svg(1100, 560, "From a monolith to earned boundaries")
    s.panel(36, 100, 360, 390, "Monolith", tone="bad")
    s.rect(70, 150, 290, 300, fill=BAD_WASH, stroke=BAD, rx=12, shadow=True)
    # tangled modules
    for i, (x, y, w, h, label) in enumerate(
        [
            (90, 180, 120, 50, "Orders"),
            (200, 200, 130, 46, "Inventory"),
            (100, 250, 150, 48, "Billing"),
            (180, 310, 140, 44, "Users"),
            (90, 360, 160, 50, "Shared tables"),
        ]
    ):
        tone = "bad" if i == 4 else "paper"
        boxed(s, x, y, w, h, label, tone=tone)
    s.add(f'<path d="M 430 300 C 480 300, 500 300, 560 300" stroke="{COPPER}" stroke-width="1.8" fill="none" marker-end="url(#arrowCopper)"/>')
    s.text(500, 280, "contract", size=12, fill=COPPER, weight="600", anchor="middle")
    s.panel(580, 100, 490, 390, "Earned service boundaries", tone="good")
    boxed(s, 610, 150, 200, 90, "Orders", "own store · own pace", tone="good")
    boxed(s, 840, 150, 200, 90, "Payments", "own store · own pace", tone="good")
    boxed(s, 610, 280, 200, 90, "Inventory", "events, not a shared table", tone="good")
    boxed(s, 840, 280, 200, 90, "Identity", "conformist UserId only", tone="good")
    s.footnote("Boundaries are kept only when they earn efficiency, independence, and ownability.")
    return s


def d_logo() -> Svg:
    # Minimal mark; skip the default paper chrome by writing raw SVG.
    return Svg(128, 128, "Microservices Recipes mark")


def render_logo() -> str:
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="128" height="128" viewBox="0 0 128 128" role="img" aria-label="Microservices Recipes mark">
  <title>Microservices Recipes mark</title>
  <rect width="128" height="128" rx="20" fill="{DESK}"/>
  <rect x="28" y="26" width="58" height="76" rx="4" fill="{DESK_DEEP}"/>
  <rect x="34" y="32" width="46" height="64" rx="2" fill="{PAPER}"/>
  <path d="M40 46 h34 M40 56 h26 M40 66 h32 M40 76 h20" stroke="{COPPER}" stroke-width="2.2" stroke-linecap="round"/>
  <path d="M86 32 v64 l16 -8 V40 l-16 -8z" fill="{GILT}"/>
</svg>
"""


def render_cover_clean() -> str:
    """Editorial cover without the default diagram chrome."""
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="720" height="1020" viewBox="0 0 720 1020" role="img" aria-labelledby="cover-title">
  <title id="cover-title">Microservices Recipes</title>
  <defs>
    <linearGradient id="coverDesk" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="{DESK}"/>
      <stop offset="100%" stop-color="{DESK_DEEP}"/>
    </linearGradient>
  </defs>
  <rect width="720" height="1020" fill="url(#coverDesk)"/>
  <rect x="28" y="28" width="664" height="964" rx="10" fill="none" stroke="{COPPER}" stroke-width="1.25"/>
  <rect x="42" y="42" width="636" height="936" rx="4" fill="none" stroke="{GILT}" stroke-width="0.6" opacity="0.5"/>
  <rect x="312" y="108" width="64" height="72" rx="3" fill="{DESK_DEEP}"/>
  <rect x="320" y="116" width="48" height="56" rx="2" fill="{PAPER}"/>
  <path d="M328 130 h32 M328 140 h24 M328 150 h30 M328 160 h18" stroke="{COPPER}" stroke-width="1.5" stroke-linecap="round"/>
  <path d="M368 116 v56 l12 -6 V122 l-12 -6z" fill="{GILT}"/>
  <text x="360" y="268" fill="{PAPER}" font-size="44" font-weight="650" text-anchor="middle" font-family="{DISPLAY}">Microservices</text>
  <text x="360" y="324" fill="{PAPER}" font-size="44" font-weight="650" text-anchor="middle" font-family="{DISPLAY}">Recipes</text>
  <path d="M210 352 h300" stroke="{COPPER}" stroke-width="1.2" stroke-linecap="round"/>
  <text x="360" y="396" fill="{GILT}" font-size="20" font-weight="500" text-anchor="middle" font-family="{FONT}">The Architect's Field Guide</text>
  <text x="360" y="620" fill="{PAPER}" font-size="20" font-weight="500" text-anchor="middle" font-family="{FONT}">Viquar Khan</text>
  <path d="M250 780 h220" stroke="{COPPER}" stroke-width="1" stroke-linecap="round" opacity="0.7"/>
  <text x="360" y="860" fill="{GILT}" font-size="15" font-weight="500" text-anchor="middle" font-family="{FONT}">Version 2.1 · 23 chapters · 2026</text>
  <text x="360" y="896" fill="{PAPER_EDGE}" font-size="13" text-anchor="middle" font-family="{FONT}">Adaptive Granularity Governance</text>
</svg>
"""


DIAGRAMS = {
    "soa-vs-microservices": d_soa_vs_microservices,
    "granularity-spectrum": d_granularity_spectrum,
    "system-availability-chain": d_system_availability_chain,
    "temporal-coupling-analysis": d_temporal_coupling_analysis,
    "conways-law-visualization": d_conways_law,
    "team-topologies": d_team_topologies,
    "bounded-context-map": d_bounded_context_map,
    "anti-corruption-layer-pattern": d_anti_corruption_layer,
    "cap-theorem-triangle": d_cap_theorem_triangle,
    "data-ownership-events": d_data_ownership_events,
    "saga-choreography-vs-orchestration": d_saga_vs,
    "saga-orchestration": d_saga_orchestration,
    "dual-write-problem": d_dual_write,
    "backpressure-flow-control": d_backpressure,
    "api-gateway-security-boundary": d_api_gateway_security,
    "agentic-ai-tool-gateway": d_agentic_tool_gateway,
    "telemetry-pipeline": d_telemetry_pipeline,
    "sidecar-vs-ebpf-observability": d_sidecar_vs_ebpf,
    "e2e-test-fragility": d_e2e_fragility,
    "testing-in-production-loop": d_testing_in_production,
    "queue-backpressure": d_queue_backpressure,
    "claim-check-pattern": d_claim_check,
    "network-tax-cognitive-load": d_network_tax,
    "rvx-calculation-flow": d_rvx_flow,
    "khan-granularity-matrix-zones": d_khan_zones,
    "service-split-example": d_service_split,
    "service-merge-example": d_service_merge,
    "km3-maturity-levels": d_km3_levels,
    "shuffle-and-cells": d_shuffle_cells,
    "shuffle-sharding-tenant-assignment": d_shuffle_tenants,
    "chaos-engineering-loop": d_chaos_loop,
    "metastable-retry-loop": d_metastable,
    "iac-golden-path-pipeline": d_iac_pipeline,
    "accounts-as-blast-radius": d_accounts_blast,
    "observability-2-pipeline": d_obs2,
    "ebpf-vs-trace-graph": d_ebpf_vs_trace,
    "multi-agent-coordination": d_multi_agent,
    "rag-architecture": d_rag,
    "hyde-rag-pipeline": d_hyde,
    "vector-store-ownership": d_vector_ownership,
    "monolith-contraction": d_monolith_contraction,
    "schema-per-module": d_schema_per_module,
    "strangler-fig": d_strangler_fig,
    "strangler-data-plane": d_strangler_data,
    "km3-staircase": d_km3_staircase,
    "km3-capabilities": d_km3_capabilities,
    "wasted-time-network-tax": d_wasted_time,
    "granularity-cost-curve": d_cost_curve,
    "construct-validity-two-streams": d_construct_validity,
    "anti-gaming-three-planes": d_anti_gaming,
    # Extra mermaid sources
    "outbox-pattern": d_outbox_pattern,
    "saga-choreography": d_saga_choreography,
    "cap-theorem": d_cap_theorem,
    "vaquarkhan-granularity-matrix": d_vaquarkhan_matrix,
    "shared-vector-store": d_shared_vector,
}


SKIPPED_MERMAID = [
    "api-gateway-lambda-sync",
    "black-friday-crisis-timeline",
    "cell-based-architecture",
    "compute-spectrum",
    "ebpf-vs-sidecar",
    "eventbridge-lambda-async",
    "hybrid-architecture",
    "isolated-vector-stores",
    "km3-maturity-model",
    "protocol-selection-tree",
]


def main() -> None:
    created: list[Path] = []
    DIAG_DIR.mkdir(parents=True, exist_ok=True)
    IMAGE_DIR.mkdir(parents=True, exist_ok=True)

    for name, factory in DIAGRAMS.items():
        path = DIAG_DIR / f"{name}.svg"
        write_svg(path, factory())
        created.append(path)

    cover = IMAGE_DIR / "cover-image-1.svg"
    cover.write_text(render_cover_clean(), encoding="utf-8")
    created.append(cover)

    hero = IMAGE_DIR / "hero-transformation.svg"
    write_svg(hero, d_hero())
    created.append(hero)

    logo = IMAGE_DIR / "logo.svg"
    logo.write_text(render_logo(), encoding="utf-8")
    created.append(logo)

    print(f"Wrote {len(created)} SVG files")
    for path in created:
        print(path.relative_to(ROOT).as_posix())
    print("Skipped mermaid sources (not in the requested set):")
    for name in SKIPPED_MERMAID:
        print(f"  {name}")


if __name__ == "__main__":
    main()
