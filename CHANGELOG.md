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
- Editorial pass: EventBridge PutEvents 256 KB/entry, Recipe 19.1 `method.request.path.proxy`, Chapter 14 Fulcrum cross-ref, Chapter 8 Contrib caveat for tail sampling, Chapter 4 causal-broadcast wording and Powertools accessor, Chapter 12 combinatorics wording, Chapter 18 `ALTER DEFAULT PRIVILEGES`, Chapter 20 modular-monolith in the 12–19 list. Redrew saga choreography-vs-orchestration and RAG architecture figures. Compressed the four original cover PNGs for Pages.
- Copyright and first-edition dates aligned to the GitHub record: public from January 2019, not 2017.
- Em dashes replaced with ASCII hyphens in front matter. GitHub release `v2.1.0` prepared for Zenodo.

### Removed
- Invented preview structure (Khan Protocol in Chapter 8, Nano-Swarm 0.3/0.6 bands, 20-chapter teaser, placeholder ISBN).
- Ten leftover mermaid PNGs that were never regenerated (odd sizes, unused, some with retired formulas or invented outage numbers).
- Marketing phrasing on README, Author, and Version History. The 2019–2.1 lineage entries stay.

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
- Major revision of the 2019 public gitbook. The 1.0 record stays in this file.
- Case studies and patterns updated for 2020 to 2026 practice.

**Disclosure line (provenance):** v2.0 (January 2026): Adaptive Granularity Strategy and RVx Index introduced.

---

## [1.x] - 2019 to 2025 (evolutionary updates)

Public notes remained under this title on GitHub. Git history shows 2019 and 2021 README work; numbered chapters arrive in Version 2.0. Highlights by period:

### 2024 to 2025
- Research years for Fulcrum and the RVx Index. Microservice writing was still mostly theoretical: no published formula that scored a boundary as a distributed monolith.
- Original work: Khan's Law, E × S / L fusion, Fulcrum loop, SCS, KM3, wasted-time cost. Site: https://vaquarkhan.github.io/fulcrum-rxy/
- Community forks, stars, and feedback continued on GitHub.
- That research became Version 2.0 (January 2026) and the 2026 paper (arXiv forthcoming).

### 2021
- README updates on GitHub (March–April).

### 2019
- Repository created 10 January 2019.
- Notes, patterns, anti-patterns, and tool links under the title Microservices Recipes.

---

## [1.0.0] - 2019-01-10

### Added
- First public edition: **Microservices Recipes** as a free GitHub gitbook of notes and recipes.
- Coverage of SOA vs microservices, DDD, data consistency, communication, deployment, monitoring, security, and testing.
- Anti-pattern identification and Conway's Law / organizational notes.
- Technology-agnostic principles over tool fashion.

**Copyright notice begins:** Copyright 2019 by Viquar Khan (continued through later editions). GitHub repository created 10 January 2019.

---

## Version comparison (summary)

| Year / version | What shipped |
|----------------|--------------|
| **2019-01-10 (1.0)** | Public GitHub gitbook of notes and recipes under this title |
| **2021** | README updates on GitHub |
| **2024 to 2025** | Fulcrum / RVx original research; no prior operational formula for a distributed monolith |
| **2026-01 (2.0)** | Adaptive Granularity Strategy + RVx Index (historical name); numbered Field Guide chapters |
| **2026-07-09 (2.0.1)** | Rename to Adaptive Granularity Governance: The Khan Microservice Pattern; dual license; citation and RVx spec scaffolding |
| **2026-09-06 (2.1)** | 23-chapter science edition; editorial SVGs; Chapters 21–23 |

---

## Notes on trademarks and copyright

- **Copyright** protects the book text, diagrams, and written expression of the pattern. That is already asserted (2019 to 2026).
- **Trademark symbols** (registered mark or trademark mark) are **not** used for methodology names in this repo because **no trademark registration is claimed** for those names at this time. See [NAMING.md](NAMING.md) and [LICENSING.md](LICENSING.md).
- Reuse: cite the work; follow MIT for code and CC BY-NC-ND 4.0 for prose and figures.

---

## Links

- [VERSION-HISTORY.md](VERSION-HISTORY.md) (narrative edition lineage)
- [docs/PATTERN-HISTORY.md](docs/PATTERN-HISTORY.md) (git provenance for RVx / SCS / KM3)
- [CITATIONS.md](CITATIONS.md) | [CITATION.cff](CITATION.cff)
