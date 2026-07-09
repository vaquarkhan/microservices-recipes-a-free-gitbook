---
title: "Observability 2.0 - Telemetry, Causality, and Cost"
chapter: 15
author: "Viquar Khan"
date: "2026-05-07"
tags:
  - opentelemetry
  - tracing
  - x-ray
  - wide-events
difficulty: "expert"
readingTime: "62 minutes"
---

# Chapter 15: Observability 2.0 - Telemetry, Causality, and Cost

<div class="chapter-header">
  <h2 class="chapter-subtitle">From Signal Collection to Causal Inference Under Budget Constraints</h2>
  <div class="chapter-meta">
    <span class="reading-time">📖 62 min read</span>
    <span class="difficulty">🎯 Expert</span>
  </div>
</div>

## Abstract

**Observability** (in the control-theoretic sense popularized for software) is the property that internal states can be **inferred** from **external outputs** (traces, metrics, logs), subject to **observation cost**. Chapters 8-10 established *what* to measure at the protocol and messaging layers; here we formalize **how** to compose signals into **actionable causal hypotheses** without bankrupting the observability budget.

We unify **OpenTelemetry**-compatible pipelines with **AWS X-Ray** / **CloudWatch** practices: **tail sampling**, **wide events**, linkage to **continuous profiling**, and **eBPF-derived** ground truth for L4 dependency graphs (Chapter 9). The goal is not 100% tracing; it is **maximal information per dollar** under SLO constraints.

![Observability 2.0 pipeline - OTel collector, metrics, traces, logs, eBPF cross-check](../assets/images/diagrams/observability-2-pipeline.png)

*Figure 15.1: Unified telemetry plane with eBPF-derived dependency graphs cross-checking trace DAGs.*

---

## 15.1 Causality vs correlation: architectural stance

Distributed traces encode **partial orders** of spans (**happens-before** at service boundaries). They **do not** prove root causes, only **candidate DAGs** for human or automated diagnosis.

**Principle 15.1 (Trace as evidence, not verdict).** Post-incident reviews must cross-validate traces with **change records**, **deploy diffs**, and **hardware SMART** data when applicable.

---

## 15.2 Wide events: semantic compression

Instead of exploding logs, emit **one structured record per request** with **high-cardinality** fields (user cohort, tenant, feature flags, `saga_id`, `cell_id`):

```json
{
  "ts": "2026-05-07T18:00:00.123Z",
  "trace_id": "4bf92f3577b34da6a3ce929d0e0e4736",
  "service": "checkout",
  "tenant_id": "t-8821",
  "saga_id": "a9182736-...",
  "duration_ms": 87,
  "outcome": "success"
}
```

Pair with columnar stores (Athena / managed OLAP) for **ad hoc** cohort queries.

---

## Recipe 15.1: OpenTelemetry → AWS X-Ray (collector excerpt)

```yaml
receivers:
  otlp:
    protocols:
      grpc:
      http:
processors:
  batch: {}
  tail_sampling:  # policy omitted - tune to SLO
    policies: []
exporters:
  awsxray:
    region: us-east-1
service:
  pipelines:
    traces:
      receivers: [otlp]
      processors: [batch, tail_sampling]
      exporters: [awsxray]
```

Enforce **W3C Trace Context** on every synchronous hop; propagate baggage **minimally** (bloat risk).

---

## 15.3 Sampling as a statistical design problem

Let **trace mass** \(M\) be stored bytes. Tail sampling strives for:

\[
\mathbb{E}[M] \le B \quad\text{s.t.}\quad \Pr[\text{miss rare failure}] \le \epsilon
\]

Adaptive rules: **always retain** traces where `http.status >= 500` or `latency > τ`.

---

## 15.4 Continuous profiling and eBPF cross-check

**Profiles** reveal CPU hotspots orthogonal to spans; **eBPF** edges reveal **surprise dependencies**. **Disagreement** between trace DAG and eBPF graph flags **hidden synchronous calls** (library defaults, DNS).

---

## 15.5 Data protection

High-cardinality telemetry risks **PII concentration**. Apply **field-level classification**, **hashing tenant IDs** in external vendors, and **regional residency** routing.

---

## 15.6 Synthesis

Observability 2.0 is **economics** applied to evidence: design telemetry where **marginal information** per gigabyte is maximized. Link to **KM3** governance (Chapter 20) so observability maturity is **audited**, not assumed.

---

**Navigation:**
- [Previous: Chapter 14](14-infrastructure-as-code-at-scale.md)
- [Next: Chapter 16](16-agentic-ai-architectures.md)
