# RVx Index: Formal Specification

**Status:** Normative for this repository (v3.0, aligned with Chapter 11 rewrite of 2026-09-06).  
**Methodology:** Adaptive Granularity Governance: The Khan Microservice Pattern.  
**Copyright:** © 2017-2026 Viquar Khan. Prose under CC BY-NC-ND 4.0; see [LICENSING.md](../LICENSING.md).  
**Scope:** Chapter 11 is the source of truth for formulas, bands, and honesty tiers. This file restates them so implementations do not drift.

## 1. Purpose

The **RVx Index** scores whether a service boundary is earning its keep: runtime efficiency, evolutionary independence, and cognitive ownability, together.

## 2. Published formula (power form, then squash)

\[
\mathrm{RVx}_{raw} = \frac{E^{\beta} \times S}{L^{\alpha} + \varepsilon}, \qquad
\mathrm{RVx} = \frac{\mathrm{RVx}_{raw}}{1 + \mathrm{RVx}_{raw}}
\]

| Symbol | Name | Range | Meaning |
|--------|------|-------|---------|
| \(E\) | Kinetic Efficiency | \([0,1]\) | Share of critical-path time spent in useful local work |
| \(S\) | Semantic Distinctness | \([0,1]\) | \(1 - \) co-change fraction across the boundary |
| \(L\) | Cognitive Load (Capacity-Normalized Complexity) | \([0,1]\) | Static complexity / team capacity |
| \(\beta\) | Efficiency exponent | default \(1.2\) | Emphasizes kinetic efficiency |
| \(\alpha\) | Load exponent | default \(0.8\) | Softens the load penalty |
| \(\varepsilon\) | Stability constant | default \(0.1\) | Avoids division by zero; caps reward for near-zero load |

**Published range:** \(0 < \mathrm{RVx} < 1\). Implementations that emit only \(\mathrm{RVx}_{raw}\) must not compare that number to the bands below. Report \(E\), \(S\), \(L\), raw, published score, profile id, and composition form.

When \(\alpha = \beta = 1\), the raw form reduces to \((E \times S) / (L + \varepsilon)\).

## 3. Illustrative bands (calibrate per profile)

| Band | Published RVx | Reading |
|------|----------------|---------|
| Distributed monolith | \(\mathrm{RVx} < 0.4\) | Boundary is not earning its keep |
| At risk | \(0.4 \le \mathrm{RVx} \le 0.7\) | Diagnose from components |
| Healthy | \(\mathrm{RVx} > 0.7\) | Clearly earning its keep (high bar after squash) |

**High-load gate:** if \(L > 0.7\), treat as an ownership problem regardless of the composite.

At defaults, \(E = S = L = 1\) floors the published score at \(\approx 0.476\), just above the monolith band. That is why the gate exists.

## 4. Composition rule

- No signal degenerate: multiplicative raw form, then squash.
- Exactly one signal degenerate (confidence or floor-bound): additive mean over trustworthy signals, degenerate one down-weighted; log the form.
- Two or more degenerate: do not publish a composite.

Thresholds are fixed in the profile *before* scoring.

## 5. Variable definitions

### 5.1 Kinetic Efficiency \(E\)

\[
E = t_{\mathrm{useful}} / t_{\mathrm{total}}
\]

\(t_{\mathrm{total}}\) is root-span wall-clock (critical path). \(t_{\mathrm{useful}}\) is the union of local compute intervals on that path, not the sum of overlapping spans. Asynchronous fire-and-forget that does not sit on the caller critical path keeps \(E\) high. Workload must be declared and representative; do not score from a tail-biased debug sample without reweighting.

**Source:** distributed traces (OpenTelemetry). Not static.

### 5.2 Semantic Distinctness \(S\)

\[
S = 1 - \frac{\text{change sets that touch this service and another across the boundary}}{\text{change sets that touch this service}}
\]

Change set = merged pull request or linked work item, not a raw commit. Exclude bot-only changes. Attribute shared libraries via an explicit map.

In a monorepo or shared-schema estate, \(S\) is often floor-bound. Annotate low confidence and apply the composition rule. Do not pretend.

**Source:** version history. Chapter 1 Recipe 1.1 is the manual form.

### 5.3 Cognitive Load \(L\)

\[
L = \mathrm{clamp}(\mathrm{complexity} / \mathrm{capacity},\ 0,\ 1)
\]

Complexity combination is profile-declared. Capacity comes from an organizational system of record, not self-report. This is Capacity-Normalized Complexity, not NASA-TLX.

## 6. Saga Complexity Score (SCS)

Defined in Chapter 11, used by Chapter 5. Do not reuse \(S\) for a saga step count.

\[
\mathrm{SCS} = w_c C + w_r R + w_x \varphi(X), \qquad
\varphi(X) = 1 - e^{-X / X_0}
\]

| Symbol | Meaning |
|--------|---------|
| \(C\) | Transaction complexity (normalized ordinal: steps, branches, waits, approval) |
| \(R\) | Business risk (normalized ordinal: money, compliance, irreversibility) |
| \(X\) | Cross-service interaction count |
| \(X_0\) | Profile reference count |
| \(w_c, w_r, w_x\) | Profile weights |

Low SCS favours choreography. High SCS favours orchestration. Design-time score, not mined from git.

## 7. Per-context calibration

Defaults are starting points. Calibrate \(\alpha\), \(\beta\), \(\varepsilon\), bands, and SCS weights as **profiles**. Publish the profile id with every score. See [validation/README.md](../validation/README.md).

## 8. Honesty tiers (Chapter 11)

- **Proven:** boundedness, monotonicity, weakest-link numerator, ranking depends on \(\beta/\alpha\).
- **Demonstrated:** simulation and a 36-boundary AWS construct-validity benchmark. Not organic production.
- **Hypothesised:** separation of healthy vs distributed-monolith boundaries on organically grown estates.

## 9. Normative references in this repo

- Chapter 11: practitioner treatment (source of truth)
- Chapter 1: manual co-change recipe (S)
- Chapter 5: saga topology; points here for SCS
- Chapter 8: traces that feed E
- Chapter 20: KM3 assessment instrumentation
- [reference-impl/](../reference-impl/) MVP scorer (must emit the squashed score)
- [validation/README.md](../validation/README.md) study plan
