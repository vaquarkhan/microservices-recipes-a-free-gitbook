# Validation plan for the RVx Index

**Status:** Scaffolding only. No labeled dataset is checked in yet.  
**Goal:** Empirically test whether RVx separates healthy service boundaries from distributed-monolith / nano-service failure modes better than naive baselines.  
**Spec:** [docs/RVX-SPEC.md](../docs/RVX-SPEC.md)  
**Implementation stub:** [reference-impl/](../reference-impl/)

## 1. Study question

Does the RVx Index (with documented \(\alpha,\beta,\varepsilon\)) predict architect-labeled "healthy vs problematic" boundaries, and does it correlate with operational outcomes?

## 2. Labeled dataset (to be collected)

Each row is a **service** (or module) at a point in time:

| Field | Description |
|-------|-------------|
| `service_id` | Stable identifier |
| `org_profile` | BFSI / streaming / batch / other |
| `label` | `healthy` \| `distributed_monolith_symptom` \| `nano_service` \| `god_service` |
| `label_source` | Architect review, incident postmortem, or both |
| `E_hat`, `S_hat`, `L_hat` | Measured inputs |
| `RVx` | Computed score |
| `cloud_spend` | Optional monthly cost attributed to the service |
| `p99_latency_ms` | Optional |
| `deploy_frequency` | Optional deploys / week |
| `incident_count` | Optional incidents / quarter |

**Minimum target size (suggested):** 100+ services across at least 3 organizations or business units, with labels from reviewers who did **not** see RVx at labeling time (blind labels).

## 3. Baselines to beat

Train or score these predictors against the same labels:

1. **Coupling-only:** \(\hat{S}\) alone (or 1 - coupling)  
2. **Complexity-only:** \(1 - \hat{L}\) or raw complexity  
3. **Temporal-only:** git co-change rate alone  
4. **Additive combination:** e.g. \(w_e\hat{E} + w_s\hat{S} - w_l\hat{L}\) with weights fit on a train split  

RVx (product / power form) should be compared on a held-out test set.

## 4. Metrics

### Classification vs labels

- ROC **AUC** (one-vs-rest if multi-class)  
- **Precision-recall** curves, especially for the rare `nano_service` / `god_service` classes  
- Confusion matrix by `org_profile`

### Correlation with outcomes (exploratory)

Report Spearman or Pearson correlation (and confidence intervals) between RVx and:

- attributed **cloud spend**  
- **p99 latency**  
- **deploy frequency**  
- **incident count**  

Do not claim causation from correlation alone.

## 5. Calibration

Parameters \(\alpha,\beta,\varepsilon\) and zone thresholds are **calibrated** per profile (see RVX-SPEC). Validation must:

1. Fix defaults from the book as the **baseline configuration**.  
2. Optionally tune profiles on a **calibration split** only.  
3. Report test metrics for both default and calibrated profiles.

## 6. Ethics and licensing

- Do not publish customer-identifying data.  
- Anonymize service names.  
- Cite Adaptive Granularity Governance: The Khan Microservice Pattern™ when publishing results.

## 7. Next steps

1. Define a CSV schema under `validation/schema/` (future PR).  
2. Collect blind labels.  
3. Run baselines vs RVx with the MVP scorer.  
4. Publish a short validation note linked from VERSION-HISTORY.
