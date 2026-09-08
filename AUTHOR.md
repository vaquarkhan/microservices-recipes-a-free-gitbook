# About the Author

## Viquar Khan

![The Architect's Field Guide](assets/images/cover-image-1.png){:.book-scene}

**Viquar Khan** is a Senior Data Architect at AWS Professional Services. He has spent more than twenty years on distributed systems and data architecture, mostly with financial institutions on AWS.

He works in Java, Scala, and Python. He was an expert-group member of JSR 368 (Java Message Service 2.1) and contributes to open-source work including Apache Spark and Terraform.

On [Stack Overflow](https://stackoverflow.com/users/4812170/vaquar-khan) his helpful posts have **7.5 million people reached**. That is Stack Overflow’s own estimate: views of questions, and of questions where he wrote a highly ranked answer. It is not a profile-view count.

ORCID: [0009-0008-3592-4162](https://orcid.org/0009-0008-3592-4162)

## How this book grew, 2017 to 2026

I started this book in 2017 because the same failure kept showing up in the field. A team split a working system, called the result modern, and then paid for a distributed monolith: lock-step deploys, a shared database, and a request path that died because every hop could time out. Version 1.0 was eight chapters. SOA versus services. Domain language. Data. Communication. Deploy. Observe. Secure. Test. The argument was already there, even if I did not yet have a score for it: a boundary is worth deploying separately only when it earns its cost.

I did not treat 1.0 as finished. The public edition stayed rooted in that 2017 guide while the work around it changed.

**2018–2019.** Cases from implementations that held. Anti-patterns from ones that did not. Tool notes as containers and cloud practice moved.

**2020–2021.** Remote teams and cloud-first delivery. Resilience for systems that had to stay up while the people who ran them were no longer in one room.

**2022–2023.** Kubernetes as the default runtime. Service mesh as it actually shipped. Observability as OpenTelemetry became the common language.

**2024–2025.** I kept the repo open and took the feedback. The next edition was not a new slogan. It was a way to measure the question the first edition had only asked.

**January 2026 — Version 2.0.** I published Adaptive Granularity Strategy and the RVx Index. The field guide became a scored argument. Service Decomposition Workflow and KM3 came with it. Chapters were rewritten for current practice. That January name is historical. Keep it in citations.

**July 2026 — Version 2.0.1.** I renamed the method to **Adaptive Granularity Governance: The Khan Microservice Pattern**. The RVx formula did not change. Dual license, naming, and citation files went in so the work could be cited without guessing.

**September 6, 2026 — Version 2.1.** Twenty-three chapters. Parts I–IX are the practitioner book. Part X is the science the metric has to survive: cost, construct validity, and Goodhart. Chapter 11 is still the only place the formula is written down. Further work is empirical validation, not a new equation.

The edition history is in [VERSION-HISTORY.md](VERSION-HISTORY.md). The dated change log is in [CHANGELOG.md](CHANGELOG.md). Those files are the record. Do not drop a year when a new version ships.

## The method

I am the author of **Adaptive Granularity Governance: The Khan Microservice Pattern** (formerly the Adaptive Granularity Strategy), the **Service Decomposition Workflow**, and the **Microservices Maturity Assessment (KM3)**. Cite them. See [LICENSING.md](LICENSING.md) and [NAMING.md](NAMING.md). No trademark is claimed.

They stand on work I did not invent:

- Cognitive load, from Team Topologies by Matthew Skelton and Manuel Pais
- Cell-based architecture, from the Amazon Builders' Library
- Forensic code analysis, from Adam Tornhill
- DynamoDB patterns, from Rick Houlihan and Alex DeBrie

## Publications

- **Microservices Recipes: The Architect's Field Guide** (2017, 2026; Version 2.1, 23 chapters)
- **Data Engineering with AWS Cookbook** (Packt Publishing, 2026)

## Philosophy

> "Stop splitting, start governing." — Viquar Khan

The job is not to draw a perfect target architecture. It is to keep the boundaries honest as the system and the team change.

## Connect

- **ORCID**: [0009-0008-3592-4162](https://orcid.org/0009-0008-3592-4162)
- **Stack Overflow**: [7.5m people reached](https://stackoverflow.com/users/4812170/vaquar-khan)
- **LinkedIn**: [www.linkedin.com/in/vaquar-khan-b695577/](https://www.linkedin.com/in/vaquar-khan-b695577/)
- **GitHub**: [github.com/vaquarkhan](https://github.com/vaquarkhan)
- **Amazon Author**: [Viquar Khan on Amazon](https://us.amazon.com/stores/Viquar-Khan/author/B0DMJCG9W6)
- **Mentorship**: [1:1 on ADPList](https://adplist.org/mentors/vaquar-khan)

## Dedication

*To the engineers who have been woken up at 3:00 AM by a PagerDuty alert caused by a distributed transaction that wasn't.*

*And to the architects who understand that the most important lines on a diagram are not the boxes, but the empty spaces between them where the network lives.*
