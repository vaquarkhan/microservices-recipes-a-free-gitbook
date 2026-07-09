---
title: "Chaos Engineering & Evidence-Based Resilience"
chapter: 13
author: "Viquar Khan"
date: "2026-05-07"
tags:
  - chaos-engineering
  - experimentation
  - aws-fis
  - slo
difficulty: "expert"
readingTime: "60 minutes"
---

# Chapter 13: Chaos Engineering & Evidence-Based Resilience

<div class="chapter-header">
  <h2 class="chapter-subtitle">From Hope to Hypothesis: Controlled Fault Injection at Scale</h2>
  <div class="chapter-meta">
    <span class="reading-time">📖 60 min read</span>
    <span class="difficulty">🎯 Expert</span>
  </div>
</div>

## Abstract

**Chaos engineering** treats resilience as an **empirical claim**: a system “handles failure well” only if demonstrated under **controlled perturbations** whose design follows scientific method: **steady-state hypothesis**, **control**, **measurement**, and **safeguards**. This chapter frames chaos as **online experimentation** on sociotechnical systems: we connect to **SLO/SLI** theory (error budgets), formalize **game-day** governance, and operationalize **AWS Fault Injection Service (FIS)** experiments with explicit **abort conditions** (automatic rollbacks when customer impact violates hypotheses).

Unlike ad hoc “restart random instances in prod,” professional chaos links hypotheses to **observability signals** (Chapter 15) and **organizational learning**: postmortems without shame, but with **reproducible experiment IDs**.

![Chaos engineering loop - hypothesis, experiment, measure, abort, learn](../assets/images/diagrams/chaos-engineering-loop.png)

*Figure 13.1: The chaos engineering cycle with explicit abort conditions tied to SLO burn alarms.*

---

## 13.1 Epistemology: what chaos can and cannot prove

**Can:** refute brittle design assumptions (“circuit breaker never opens”) within **scope** of faults modeled.  
**Cannot:** prove correctness under *all* failures (undecidable in full generality); **combinatorial explosion** of failure modes implies **risk-based sampling**, not exhaustive simulation.

**Principle 13.1 (Falsifiability).** A resilience claim must be **testable by an experiment** that could fail; otherwise it is rhetoric.

---

## 13.2 Steady-state hypotheses and stopping conditions

Let \(y(t)\) be an SLI-vector (latency p99, error rate, queue depth). **Steady state** under load test \(L\) satisfies \(y(t) \in \mathcal{R}\) (feasible region) for duration \(T\).

A chaos run introduces fault \(\phi\). **Hypothesis:** \(\forall t \in [t_0, t_1],\, y_{\phi}(t) \in \mathcal{R}'\) where \(\mathcal{R}'\) may relax non-critical dimensions but **never** customer SLOs without explicit approval.

**Automatic abort:** if **SLO burn** alarm fires or **canary** error rate exceeds threshold, terminate \(\phi\) and **capture** telemetry snapshot for causal analysis.

---

## 13.3 Game-day operating model

| Role | Responsibility |
|------|------------------|
| **Experiment owner** | Writes hypothesis, blast radius, rollback |
| **Observer** | Tracks metrics; sole authority to call abort |
| **Comms** | Customer messaging if external degradation possible |
| **Incident commander (on-call)** | Activated if abort escalates |

**Artifacts:** pre-read (30 min), runbook links, **Jira/CM ticket** with ID propagated to traces.

---

## Recipe 13.1: AWS FIS experiment template (YAML sketch)

> **Note:** validate action IDs against current AWS regional catalogs; this is structural guidance only.

```yaml
# Pseudocode CloudFormation / CDK-equivalent intent
ExperimentTemplate:
  Description: AZ power-interrupt resilience for checkout read path
  Targets:
    - Name: AZ1a-subnets
      ResourceType: aws:ec2:subnet
      SelectionMode: FILTER
      Filters:
        - Path: AvailabilityZone
          Values: ["us-east-1a"]
  Actions:
    - Name: aws:ssm:send-command  # illustrative; use approved FIS actions
      TargetName: AZ1a-subnets
  StopConditions:
    - Type: aws:cloudwatch:alarm
      AlarmArn: arn:aws:cloudwatch:us-east-1:ACCOUNT:alarm:checkout-p99-burn
  RoleArn: arn:aws:iam::ACCOUNT:role/FISExperimentRole
```

Pair with **post-experiment review**: did \(y_{\phi}\) violate \(\mathcal{R}'\)? If yes-**not** a failure of chaos, but **success of learning**.

---

## 13.4 Statistical cautions

- **Peeking:** repeatedly glancing at metrics inflates false positives-pre-register success criteria.  
- **Multiplicity:** many teams running chaos concurrently **couples** experiments; coordinate calendars.  
- **Non-stationarity:** deployments change baseline \(y\); re-baseline after releases.

---

## 13.5 Ethics and compliance

Chaos in regulated industries may **not** touch systems of record without audit trails. Prefer **shadow environments** with **production-like load cloning** when law or policy forbids direct prod fault injection.

---

## 13.6 Synthesis

Chaos engineering operationalizes **Popperian falsification** for distributed systems. Integrate with shuffle sharding (Chapter 12) and KM3 maturity controls (Chapter 20) so resilience becomes **governed capability**, not heroism.

---

**Navigation:**
- [Previous: Chapter 12](12-shuffle-sharding.md)
- [Next: Chapter 14](14-infrastructure-as-code-at-scale.md)
