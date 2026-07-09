# RVx Index: Formal Specification

**Status:** Normative for this repository (v2.0).  
**Methodology:** Adaptive Granularity Governance: The Khan Microservice Pattern (formerly Adaptive Granularity Strategy).  
**Copyright:** © 2017-2026 Vaquar Khan. Prose under CC BY-NC-ND 4.0; see [LICENSING.md](../LICENSING.md).  
**Scope:** Naming and packaging may change; **this document does not change** published formulas or default thresholds from the book chapters.

## 1. Purpose

The **RVx Index** (Revised VaquarKhan Index) scores whether a service boundary is earning its keep: benefits of separation versus cost of separation.

## 2. Core formula (product form)

As stated in Chapter 11:

\[
\mathrm{RVx} = \frac{\hat{E} \times \hat{S}}{\hat{L} + \varepsilon}
\]

| Symbol | Name | Range | Meaning |
|--------|------|-------|---------|
| \(\hat{E}\) | Kinetic Efficiency | \([0,1]\) | Share of end-to-end time spent in useful compute |
| \(\hat{S}\) | Semantic Distinctness | \([0,1]\) | Independence of change and meaning from other services |
| \(\hat{L}\) | Cognitive Load | \([0,1]\) | Normalized complexity / ownership burden |
| \(\varepsilon\) | Stability constant | default \(0.1\) | Avoids division by zero; soft floor on cost |

**Output range:** With inputs in \([0,1]\) and \(\varepsilon = 0.1\), RVx lies in roughly \([0, 1/0.1] = [0, 10]\) in theory, and typically about **0 to ~3** in practice. Higher is better.

### 2.1 Why 0.7 and 0.4 are meaningful

Because \(\hat{E}\), \(\hat{S}\), and \(\hat{L}\) are **normalized to \([0,1]\)**, RVx is a dimensionless ratio of benefit to cost:

- An RVx near **0.4** means benefits barely cover (or fail to cover) cognitive and operational cost.  
- An RVx near **0.7** or above (with healthy \(\hat{S}\) and moderate \(\hat{L}\)) means the boundary is usually justified.  

Exact zone rules used in the book (do not change without a versioned amendment):

| Zone | Condition (from Chapter 11) | Action |
|------|-----------------------------|--------|
| Nano-swarm / merge | \(\mathrm{RVx} \le 0.3\) and \(\hat{E} < 0.3\) | Merge |
| Cognitive overload / split | \(\hat{L} > 0.7\) (regardless of RVx) | Split |
| Healthy | \(\mathrm{RVx} > 0.6\) and \(\hat{S} > 0.6\) and \(\hat{L} < 0.7\) | Keep |

## 3. Power-law form (Chapter 3 measurement protocol)

Chapter 3 documents a calibrated power form used in measurement recipes:

\[
\mathrm{RVx} = \frac{\hat{E}^{\beta} \times \hat{S}}{\hat{L}^{\alpha} + \varepsilon}
\]

**Default parameters (do not change casually):**

| Parameter | Default | Role |
|-----------|---------|------|
| \(\beta\) | **1.2** | Emphasizes kinetic efficiency |
| \(\alpha\) | **0.8** | Softens cognitive-load penalty relative to linear |
| \(\varepsilon\) | **0.1** | Stability constant |

When \(\alpha = \beta = 1\), this reduces to the product form in Section 2. Implementations should **document which form** they use and keep parameters versioned.

## 4. Variable definitions

### 4.1 Kinetic Efficiency \(\hat{E}\)

\[
\hat{E} = \frac{T_{\mathrm{compute}}}{T_{\mathrm{compute}} + T_{\mathrm{network}} + T_{\mathrm{serialize}} + T_{\mathrm{mesh}}}
\]

**Source:** runtime traces (OpenTelemetry, X-Ray, Jaeger).  
**Static?** No. Measured from production or load-test traces.

### 4.2 Semantic Distinctness \(\hat{S}\)

Measures whether the service changes independently of others (temporal coupling, shared commits, domain cohesion). Chapter 3 recipe:

\[
\hat{S} \approx 1 - \frac{\text{multi-service commits}}{\text{total commits}}
\]

(over a window such as 90 days), optionally combined with static domain checks.  
**Source:** git history (+ optional static analysis).  
**Static?** Partially: git-derived; may include static module graphs.

### 4.3 Cognitive Load \(\hat{L}\)

Normalized complexity / size / ownership burden. Chapter 3 example:

\[
\hat{L} = \frac{\mathrm{complexity} + \mathrm{LOC}/1000}{200}
\]

clamped to \([0,1]\).  
**Source:** static analysis (e.g. SonarQube) and team topology signals.  
**Static?** Mostly static; may include on-call / ownership metadata.

## 5. Input classes

| Input | Class |
|-------|--------|
| Complexity, LOC, module graph | **Static** |
| Co-change / multi-service commits | **Git history** |
| Latency breakdown, error rates | **Runtime traces** |

## 6. Per-context calibration profiles

Defaults above are starting points. Calibrate \(\alpha\), \(\beta\), and zone thresholds as **profiles**, not one global law:

| Profile | Intent | Typical adjustment |
|---------|--------|--------------------|
| **BFSI** | Strong consistency, audit, lower change rate | Slightly higher \(\hat{L}\) weight (raise \(\alpha\)); stricter merge on low \(\hat{E}\) |
| **Streaming** | High fan-out, latency sensitive | Emphasize \(\hat{E}\) (raise \(\beta\)); watch network tax |
| **Batch** | Throughput over p99 | Soften latency-driven \(\hat{E}\) penalties; focus \(\hat{S}\) and ops cost |

Publish profile IDs with every score. Thresholds and parameters are **calibrated**; see [validation/README.md](../validation/README.md).

## 7. Saga Complexity Score (SCS)

From Chapter 5 (unchanged):

\[
\mathrm{SCS} = (C \times 2) + (R \times 3) + (S \times 1)
\]

| Symbol | Meaning |
|--------|---------|
| \(C\) | Number of **compensatable** steps |
| \(R\) | Number of **pivot / hard-to-reverse** steps (weighted higher) |
| \(S\) | Number of **supporting / side-effect** steps (e.g. notifications) |

**Decision bands (unchanged):**

- \(\mathrm{SCS} \le 8\): choreography is viable  
- \(\mathrm{SCS}\) 9–15: orchestration recommended  
- \(\mathrm{SCS} > 15\): orchestration required  

SCS is **static design-time** (from the saga design), not from git or traces.

## 8. Normative references in this repo

- Chapter 11: RVx narrative and zones  
- Chapter 3: measurement protocol with \(\alpha,\beta,\varepsilon\)  
- Chapter 5: SCS formula  
- [NAMING.md](../NAMING.md), [LICENSING.md](../LICENSING.md)  
- [reference-impl/](../reference-impl/) MVP scorer  
- [validation/README.md](../validation/README.md) study plan  
