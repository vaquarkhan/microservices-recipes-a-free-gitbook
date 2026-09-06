# Preface

I wrote this book because I kept seeing the same failure. A team splits a working system into services, calls the result modern, and then spends the next two years paying for a distributed monolith: lock-step deploys, a shared database, and a request path that dies because every hop can time out.

The question that actually matters is not “how many services.” It is whether a boundary earns the cost of being remote. That is the spine of the book.

**Adaptive Granularity Governance** (the Khan Microservice Pattern) is how I make that question answerable. The RVx Index is the score. Chapter 11 is the only place the formula, the defaults, and the evidence tiers are written down. I am not reprinting the equation here. If an old slide has the exponents swapped, throw the slide away.

Read a score as a warning light, not a trophy:

- **Above 0.7** — healthy on the declared profile. Still show the three components.
- **0.4 to 0.7** — at risk. Find the weak signal before you split or merge.
- **Below 0.4** — the boundary is not earning its keep.

The whole book is here. Twenty-three chapters. There is no later paid half, and there is no ten-chapter teaser. Parts I–III are the substrate: organization, data, evidence. Chapter 11 is the measurement. Parts V–IX are isolation, platform, agents, migration, and maturity. Part X is cost, validity, and Goodhart.

I work on AWS. The examples lean that way. The arguments are not AWS-specific.

If you use the method, cite it. Formats are in [CITATIONS.md](CITATIONS.md).

**Viquar Khan**  
September 6, 2026

---

**Copyright © 2017–2026 by Viquar Khan.**

Original methods, please cite:

- Adaptive Granularity Governance: The Khan Microservice Pattern
- Service Decomposition Workflow
- Microservices Maturity Assessment (KM3)

First edition: January 2017. Second edition: January 2026. Version 2.1: September 2026.

Repository: https://github.com/vaquarkhan/microservices-recipes-a-free-gitbook

See [CITATIONS.md](CITATIONS.md), [LICENSING.md](LICENSING.md), and [DISCLAIMER.md](DISCLAIMER.md).
