# Pattern history (provenance)

This file records **first introduction in this Git repository** for key artifacts. It does **not** rewrite git history. Hashes come from `git log` on the current clone.

**Repository note:** A shallow or single-commit upload history may collapse earlier private drafts into one public commit. Treat the dates below as **first appearance in this public tree**, not necessarily the first private invention date.

## Summary table

| Artifact | First public commit in this repo | Date | Subject |
|----------|----------------------------------|------|---------|
| **RVx Index** (and Adaptive Granularity Strategy / Chapter 11) | `93d1d0c647da82ff746fbc7c9fa107a9fe426c77` | 2026-03-21 | Add files via upload |
| **Saga Complexity Score (SCS)** | `93d1d0c647da82ff746fbc7c9fa107a9fe426c77` | 2026-03-21 | Add files via upload (see Chapter 5) |
| **KM3** (Microservices Maturity Assessment) | `93d1d0c647da82ff746fbc7c9fa107a9fe426c77` | 2026-03-21 | Add files via upload (see Chapter 11 / Chapter 20) |

## How these were found

```bash
git log -S "RVx" --oneline --all
git log -S "Saga_Complexity_Score\|SCS =" --oneline --all
git log -S "KM3" --oneline --all
git log --follow --format="%H %ad %s" --date=short -- chapters/11-khan-pattern-deep-dive.md
```

On the clone used for this document, those searches all resolve to the same root upload commit above.

## Editorial disclosure (book edition)

Independent of git upload timing, the book edition history states:

- **v2.0 (January 2026):** Adaptive Granularity Strategy and RVx Index introduced (historical name).

See [VERSION-HISTORY.md](../VERSION-HISTORY.md).

## Rename (naming only)

Later commits rename the methodology to **Adaptive Granularity Governance: The Khan Microservice Pattern™**. The **RVx Index** formulas and thresholds are unchanged. See [NAMING.md](../NAMING.md).
