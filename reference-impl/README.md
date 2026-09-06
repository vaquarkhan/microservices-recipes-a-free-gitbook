# RVx reference implementation (MVP)

**Status:** Stub / MVP. Not production-ready.  
**Purpose:** Demonstrate how to assemble RVx inputs from static analysis, git history, and runtime traces.  
**Spec:** [docs/RVX-SPEC.md](../docs/RVX-SPEC.md)  
**License:** MIT (this directory). Methodology prose remains under the book dual license; see [LICENSING.md](../LICENSING.md).

## What this MVP does

1. Accepts **static** complexity signals (LOC, complexity score).  
2. Mines **temporal coupling** from git log co-change (semantic distinctness proxy).  
3. Accepts **runtime** kinetic efficiency from a simple JSON trace summary.  
4. Computes published RVx using the Chapter 11 power form, then squash: \(\mathrm{RVx}=\mathrm{raw}/(1+\mathrm{raw})\), defaults \(\beta=1.2\), \(\alpha=0.8\), \(\varepsilon=0.1\). Chapter 22 is the validity chapter. Do not treat this stub as a production study.

## What this MVP does not do

- Full OpenTelemetry ingestion  
- Automatic SonarQube integration  
- Validated calibration against a labeled dataset (see [validation/](../validation/))  

## Quick start

```bash
cd reference-impl
python rvx_scorer.py --help
python rvx_scorer.py \
  --loc 12000 --complexity 85 \
  --git-repo .. --service-path chapters \
  --trace-file examples/trace_summary.json
```

## Attribution

When you publish scores derived from this tool, cite **Adaptive Granularity Governance: The Khan Microservice Pattern** and the RVx Index ([CITATIONS.md](../CITATIONS.md)).
