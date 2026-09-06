# Changelog

All notable changes to **Microservices Recipes: The Architect's Field Guide** are recorded here.

Format inspired by [Keep a Changelog](https://keepachangelog.com/). Dates use ISO style where known. Edition history also lives in [VERSION-HISTORY.md](VERSION-HISTORY.md).

**Methodology name today:** Adaptive Granularity Governance: The Khan Microservice Pattern  
**Former name (keep in citations):** Adaptive Granularity Strategy  
**Metric (unchanged):** RVx Index

---

## [2.1.0] - 2026-09-06

### Added
- Chapters 21–23 (cost, construct validity, Goodhart).
- Editorial SVG figures, cover, and hero art for GitHub Pages.
- `tools/render_book_svgs.py` to regenerate diagrams in the atelier palette.

### Changed
- Front matter, preview, glossary, and quick reference aligned to 23 chapters and Chapter 11 as formula source of truth.
- Recipe corrections: Kinesis Base64 JMESPath, Step Functions human-approval timeouts, API Gateway authorizer helpers, OTel Contrib note, Recipe 1.1 commit-vs-PR caveat.

### Removed
- Invented preview structure (Khan Protocol in Chapter 8, Nano-Swarm 0.3/0.6 bands, 20-chapter teaser, placeholder ISBN).

---

## [2.0.1] - 2026-07-09

### Changed
- Renamed the methodology to **Adaptive Granularity Governance: The Khan Microservice Pattern** (RVx Index formulas and thresholds unchanged).
- Dual license documented: **MIT** for source code; **CC BY-NC-ND 4.0** for book prose, diagrams, and figures ([LICENSING.md](LICENSING.md)).
- Copyright and disclaimer wording clarified: original methodology by the author; please cite; **no trademark claimed** (no registered or trademark symbols for the methodology names).

### Added
- [NAMING.md](NAMING.md), [CITATION.cff](CITATION.cff), [docs/RVX-SPEC.md](docs/RVX-SPEC.md), [docs/PATTERN-HISTORY.md](docs/PATTERN-HISTORY.md)
- `reference-impl/` MVP RVx scorer and `validation/` study scaffold
- README "How to cite" (APA and IEEE)

---

## [2.0.0] - 2026-01

### Added
- **Adaptive Granularity Strategy** and **RVx Index** introduced (historical name for the methodology).
- Service Decomposition Workflow and Microservices Maturity Assessment (KM3) framing.
- Expanded chapter set (foundational Parts I to III plus Adaptive Granularity deep dive).
- eBPF / post-sidecar networking coverage; cloud-native AWS and Kubernetes focus.
- Professional chapter headers, diagrams, and GitHub Pages presentation.

### Changed
- Major architectural overhaul from the 2017 foundational edition.
- Case studies and patterns updated for 2020 to 2026 practice.

**Disclosure line (provenance):** v2.0 (January 2026): Adaptive Granularity Strategy and RVx Index introduced.

---

## [1.x] - 2018 to 2025 (evolutionary updates)

Public edition remained rooted in the 2017 foundational guide while content and practice evolved. Highlights by period:

### 2024 to 2025
- Community forks, stars, and feedback continued on GitHub.
- Preparation for the January 2026 Adaptive Granularity / RVx edition.

### 2022 to 2023
- Kubernetes-native patterns emphasized.
- Service mesh evolution documented.
- Observability aligned with OpenTelemetry-era practice.

### 2020 to 2021
- Remote-team and cloud-first considerations strengthened.
- Resilience patterns updated for distributed delivery under pandemic-era constraints.

### 2018 to 2019
- Case studies from successful implementations added.
- Anti-pattern documentation from failed transformations expanded.
- Tooling notes updated as the container and cloud ecosystem matured.

---

## [1.0.0] - 2017-01

### Added
- First edition: **Microservices Recipes** foundational field guide.
- Eight core chapters covering SOA vs microservices, DDD, data consistency, communication, deployment, monitoring, security, and testing.
- Anti-pattern identification and Conway's Law / organizational notes.
- Technology-agnostic principles over tool fashion.

**Copyright notice begins:** Copyright 2017 by Viquar Khan (continued through later editions).

---

## Version comparison (summary)

| Year / version | What shipped |
|----------------|--------------|
| **2017 (1.0)** | Foundational 8-chapter microservices guide |
| **2018 to 2019** | Refinement, cases, anti-patterns |
| **2020 to 2021** | Cloud-first and resilience updates |
| **2022 to 2023** | K8s, mesh, observability modernization |
| **2026-01 (2.0)** | Adaptive Granularity Strategy + RVx Index (historical name) |
| **2026-07-09 (2.0.1)** | Rename to Adaptive Granularity Governance: The Khan Microservice Pattern; dual license; citation and RVx spec scaffolding |

---

## Notes on trademarks and copyright

- **Copyright** protects the book text, diagrams, and written expression of the pattern. That is already asserted (2017 to 2026).
- **Trademark symbols** (registered mark or trademark mark) are **not** used for methodology names in this repo because **no trademark registration is claimed** for those names at this time. See [NAMING.md](NAMING.md) and [LICENSING.md](LICENSING.md).
- Reuse: cite the work; follow MIT for code and CC BY-NC-ND 4.0 for prose and figures.

---

## Links

- [VERSION-HISTORY.md](VERSION-HISTORY.md) (narrative edition lineage)
- [docs/PATTERN-HISTORY.md](docs/PATTERN-HISTORY.md) (git provenance for RVx / SCS / KM3)
- [CITATIONS.md](CITATIONS.md) | [CITATION.cff](CITATION.cff)
