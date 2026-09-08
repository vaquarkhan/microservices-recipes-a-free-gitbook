# 📖 Microservices Recipes: The Architect's Field Guide

<div align="center">

![Microservices Recipes Cover](assets/images/cover-image-2.png)

**A practical guide to building, scaling, and managing microservices architectures**

As defined by Sam Newman in his foundational text *Building Microservices*, microservices are "small, autonomous services that work together." This definition emphasizes the dual requirements of independence and interoperability.

*Featuring Adaptive Granularity Governance: The Khan Microservice Pattern*

[![GitHub Pages](https://img.shields.io/badge/GitHub%20Pages-Live-brightgreen)](https://vaquarkhan.github.io/microservices-recipes-a-free-gitbook/)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.22654421.svg)](https://doi.org/10.5281/zenodo.22654421)
[![License: MIT](https://img.shields.io/badge/Code-MIT-yellow.svg)](LICENSE)
[![Prose: CC BY-NC-ND 4.0](https://img.shields.io/badge/Prose-CC%20BY--NC--ND%204.0-lightgrey.svg)](LICENSING.md)
[![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)](CONTRIBUTING.md)

---

*"Stop splitting, start governing."* - **Adaptive Granularity Governance: The Khan Microservice Pattern**

![Microservices Animation](assets/images/microservices-animation.gif)

</div>

## 📋 Table of Contents

### 📚 **Front Matter**
- [Preface](PREFACE.md) - why a boundary has to earn its keep
- [About the Author](AUTHOR.md) - Viquar Khan
- [Mentorship](MENTORSHIP.md) - free 1:1 on ADPList
- [Licensing](LICENSING.md) - MIT for code; CC BY-NC-ND 4.0 for prose and figures
- [Naming](NAMING.md) - methodology title and attribution
- [Citations](CITATIONS.md) - how to cite this work
- [Copyright](COPYRIGHT.md) - owner and dual license
- [Disclaimer](DISCLAIMER.md) - legal notice
- [Contributing](CONTRIBUTING.md)
- [Version history](VERSION-HISTORY.md)
- [Changelog](CHANGELOG.md)
- [Academic use](FREE-ACCESS.md) - the full book is public; cite it
- [CITATION.cff](CITATION.cff) - machine-readable citation metadata

---

### 📖 **Part I: The Sociotechnical Substrate**
*Focus: Aligning organization and architecture to prevent the "Distributed Monolith"*

| Chapter | Title | Description | Read Time |
|---------|-------|-------------|-----------|
| **[1](chapters/01-introduction-to-microservices.md)** | **Earned Boundaries, Not Fashionable Ones** | SOA done right, replaceability over size, and finding seams in Git history | 35 min |
| **[2](chapters/02-design-principles-and-patterns.md)** | **The Distributed Monolith: Diagnosis and First Remedies** | Connascence, Conway's Law, contracts, and the first resilience gate | 40 min |
| **[3](chapters/03-service-communication.md)** | **Decouple the Language Before You Decouple the Code** | Bounded contexts, context maps, Event Storming, and aggregates | 40 min |

---

### 🗄️ **Part II: Data Architecture**
*Focus: Managing data consistency and transactions in distributed systems*

| Chapter | Title | Description | Read Time |
|---------|-------|-------------|-----------|
| **[4](chapters/04-data-management.md)** | **The End of ACID** | Consistency dial, CRDTs, cloud internals, and data ownership | 45 min |
| **[5](chapters/05-deployment-and-operations.md)** | **The Consistency Tax of Spanning Services** | Sagas, compensation, choreography vs orchestration, isolation | 45 min |
| **[6](chapters/06-resilience-and-reliability.md)** | **Close the Dual Write, Then Survive Failure** | Outbox, timeouts, breakers, backpressure, and error budgets | 45 min |
| **[7](chapters/07-security.md)** | **Every Hop Is a Door. Prove Who Is Knocking.** | Zero trust, tokens, secrets, and agent capability limits | 50 min |

---

### 🌐 **Part III: Inter Process Communication**
*Focus: Moving bits between services without creating latency storms*

| Chapter | Title | Description | Read Time |
|---------|-------|-------------|-----------|
| **[8](chapters/08-monitoring-and-observability.md)** | **You Cannot Attach a Debugger. Emit the Evidence First.** | Metrics, structured logs, traces, OpenTelemetry, and burn-rate alerts | 50 min |
| **[9](chapters/09-testing-strategies.md)** | **There Is No Whole System to Test. Test the Agreements.** | Pyramid, contracts, async tests, and testing in production | 50 min |
| **[10](chapters/10-asynchronous-messaging-patterns.md)** | **Publish What Happened. Do Not Wait.** | Backpressure, poison messages, idempotency, and claim check | 50 min |

---

### 🎯 **Part IV: Adaptive Granularity Governance**
*Focus: Quantitative framework for microservices decomposition (The Khan Microservice Pattern)*

| Chapter | Title | Description | Read Time |
|---------|-------|-------------|-----------|
| **[11](chapters/11-khan-pattern-deep-dive.md)** | **A Boundary Earns Its Keep Only When All Three Hold** | Fulcrum, RVx, SCS, and KM3, with honesty tiers | 70 min |

---

### 🧱 **Part V: Resilience Engineering & Advanced Scaling**
*Focus: Blast-radius control and evidence-based failure injection*

| Chapter | Title | Description | Read Time |
|---------|-------|-------------|-----------|
| **[12](chapters/12-shuffle-sharding.md)** | **A Single Bad Shard Should Be a Footnote** | Shuffle sharding inside cells, with measured blast radius | 55 min |
| **[13](chapters/13-chaos-engineering.md)** | **Break It on Purpose. Watch. Then You Know.** | Game days, FIS abort alarms, and metastable retries | 55 min |

---

### 🏗️ **Part VI: The Platform Engineering Shift**
*Focus: Golden paths, policy-as-code, and telemetry economics*

| Chapter | Title | Description | Read Time |
|---------|-------|-------------|-----------|
| **[14](chapters/14-infrastructure-as-code-at-scale.md)** | **The Definition Is the Truth. Reality Is Reconciled Toward It.** | Desired state, locked state, three-layer policy, and version-pinned golden paths | 55 min |
| **[15](chapters/15-observability-2.md)** | **Spend the Budget on Answers. Stay Sighted When It Counts.** | Wide events, tail sampling, eBPF cross-check, and retention tiers | 55 min |

---

### Part VII: Agents and retrieval
*Focus: Probabilistic components inside deterministic architectures*

| Chapter | Title | Description | Read Time |
|---------|-------|-------------|-----------|
| **[16](chapters/16-agentic-ai-architectures.md)** | **The Model Proposes. The Executor Disposes.** | Planner versus executor, tool gateway, and bounded multi-agent design | 55 min |
| **[17](chapters/17-rag-at-scale.md)** | **Retrieval as a Data-Plane Discipline, Not a Prompt Trick** | ACL prefilter, hybrid retrieval, pinned embeddings, and shadow eval | 55 min |

---

### Part VIII: Migration
*Focus: Monolith-first discipline and incremental replacement*

| Chapter | Title | Description | Read Time |
|---------|-------|-------------|-----------|
| **[18](chapters/18-modular-monolith.md)** | **The Right Number of Services Is Often One.** | Enforced modules, schema-per-module grants, and extraction on evidence | 55 min |
| **[19](chapters/19-strangler-fig-pattern.md)** | **Replace It While It Is Still Running.** | Facade first, data ownership, shadow that does not persist twice | 55 min |

---

### 📈 **Part IX: Organizational Maturity**
*Focus: KM3 operational assessment*

| Chapter | Title | Description | Read Time |
|---------|-------|-------------|-----------|
| **[20](chapters/20-km3-maturity-model.md)** | **Has This Organization Earned the Right to Distribute?** | Evidence-based KM3 assessment, not a badge race | 50 min |

---

### 📐 **Part X: The Science Behind the Metric**
*Focus: Cost, construct validity, and anti-Goodhart discipline*

| Chapter | Title | Description | Read Time |
|---------|-------|-------------|-----------|
| **[21](chapters/21-pricing-the-distributed-monolith.md)** | **Price the Waste. Name the Rest. Do Not Invent a Total.** | Wasted time as an identity, payback on hypothesized savings | 50 min |
| **[22](chapters/22-construct-validity.md)** | **A Formula Confers No Truth. Outcomes Do.** | Construct validity, reliability, and evidence tiers | 50 min |
| **[23](chapters/23-gaming-and-goodhart.md)** | **Never Point the Number at the People.** | Tamper-evidence, named attacks, and no score in reviews | 50 min |

---

### 📚 **Reference Materials**

| Resource | Description |
|----------|-------------|
| **[📖 Glossary](reference/glossary.md)** | Comprehensive definitions of microservices terms |
| **[⚡ Quick Reference](reference/quick-reference.md)** | Handy reference cards for patterns and practices |
| **[📚 Bibliography](reference/bibliography.md)** | Curated list of books, articles, and resources |

---

## The method

**Adaptive Granularity Governance: The Khan Microservice Pattern** (formerly the Adaptive Granularity Strategy) is how I decide whether a boundary earns a remote hop. Chapter 11 is the score. Chapters 21–23 cover cost, whether the measurement is valid, and how you keep it from being gamed.

The method is an original synthesis from practice. Cite it if you reuse it ([CITATIONS.md](CITATIONS.md)).

The job is not a perfect target architecture. It is to keep the boundaries honest as the system and the team change.

---

## Start here

### **For Beginners**
1. Start with [**Chapter 1: Earned Boundaries**](chapters/01-introduction-to-microservices.md)
2. Read [**The Preface**](PREFACE.md) to understand the book's philosophy
3. Progress through Parts I → X. All 23 chapters are in this repo.

### **For Experienced Practitioners**
1. Review the [**Table of Contents**](#-table-of-contents) above
2. Jump to specific chapters addressing your current challenges
3. Use [**Quick Reference**](reference/quick-reference.md) for rapid pattern lookup

### **For Architects**
1. Focus on strategic chapters: [Ch 2](chapters/02-design-principles-and-patterns.md), [Ch 3](chapters/03-service-communication.md), [Ch 7](chapters/07-security.md)
2. Study [**Adaptive Granularity Governance: The Khan Microservice Pattern**](AUTHOR.md#adaptive-granularity-governance-the-khan-microservice-pattern) (formerly Adaptive Granularity Strategy)
3. Review [**Complete Book Preview**](BOOK-PREVIEW.md) for advanced topics

---

## Scope

| Metric | Value |
|--------|-------|
| **Total Chapters** | 23 (Parts I–X; all linked in the TOC) |
| **Reading Time** | ~19 hours across the full book |
| **Code Examples** | Recipes in every practitioner chapter |
| **Patterns Covered** | Decomposition, data, resilience, platform, AI, migration |
| **Evidence stance** | Proved / demonstrated / hypothesized - Chapter 11 and 22 |
---

## Topics covered

<details>
<summary><strong>🏗️ Architectural Patterns</strong></summary>

- **Adaptive Granularity Governance: The Khan Microservice Pattern** for adaptive service granularity
- **Distributed Monolith** identification and prevention
- **Domain-Driven Design** for service boundaries
- **Saga Pattern** for distributed transactions
- **Event Sourcing** and **CQRS** patterns
- **API Gateway** and **Service Mesh** architectures

</details>

<details>
<summary><strong>🔧 Technical Implementation</strong></summary>

- **Microservices Communication** (REST, gRPC, GraphQL)
- **Data Management** strategies and consistency patterns
- **Deployment & Operations** with containers and orchestration
- **Monitoring & Observability** with distributed tracing
- **Security** patterns and zero-trust architectures
- **Testing Strategies** for distributed systems

</details>

<details>
<summary><strong>🎯 Real-World Skills</strong></summary>

- **Conway's Law** and organizational design
- **Failure Mode Analysis** and resilience engineering
- **Performance Optimization** and scalability patterns
- **Migration Strategies** from monolith to microservices
- **Team Topologies** and cognitive load management
- **Platform Engineering** and developer experience

</details>

---

## 👨‍💻 **About the Author**

**[Viquar Khan](AUTHOR.md)** is a Senior Data Architect at AWS Professional Services with 20+ years of expertise in distributed systems. Creator of **Adaptive Granularity Governance: The Khan Microservice Pattern**, the **Service Decomposition Workflow**, and the **Microservices Maturity Assessment (KM3)**. Original methodologies by the author; please cite.

JSR 368 expert group (Java Message Service 2.1). Also author of *Data Engineering with AWS Cookbook* (Packt, 2026). On [Stack Overflow](https://stackoverflow.com/users/4812170/vaquar-khan) his helpful posts have 7.5 million people reached (Stack Overflow’s estimate). 2024–2025 research: [Fulcrum / RVx](https://vaquarkhan.github.io/fulcrum-rxy/). Book history, 2019 to 2026: [AUTHOR.md](AUTHOR.md).

**Connect:** [ORCID](https://orcid.org/0009-0008-3592-4162) | [LinkedIn](https://www.linkedin.com/in/vaquar-khan-b695577/) | [GitHub](https://github.com/vaquarkhan) | [Amazon](https://us.amazon.com/stores/Viquar-Khan/author/B0DMJCG9W6) | [Mentorship](https://adplist.org/mentors/vaquar-khan)

---

## 🌐 **Access This Book**

### **📖 Read Online**
- **GitHub Pages**: [https://vaquarkhan.github.io/microservices-recipes-a-free-gitbook/](https://vaquarkhan.github.io/microservices-recipes-a-free-gitbook/)
- **GitHub Repository**: [https://github.com/vaquarkhan/microservices-recipes-a-free-gitbook](https://github.com/vaquarkhan/microservices-recipes-a-free-gitbook)

### Academic use
The 23 chapters are in this repository. There is no separate academic edition. Cite it ([CITATIONS.md](CITATIONS.md)). Lineage: [VERSION-HISTORY.md](VERSION-HISTORY.md). Notes: [FREE-ACCESS.md](FREE-ACCESS.md).

### Download
```
git clone https://github.com/vaquarkhan/microservices-recipes-a-free-gitbook.git
```
ZIP of the default branch: [archive](https://github.com/vaquarkhan/microservices-recipes-a-free-gitbook/archive/master.zip). GitHub Pages deploys from `master`. DOI: [10.5281/zenodo.22654421](https://doi.org/10.5281/zenodo.22654421).

---

## Community

[Star the repo](https://github.com/vaquarkhan/microservices-recipes-a-free-gitbook) if it is useful. [Cite it](CITATIONS.md) if you use the method. [Open an issue](https://github.com/vaquarkhan/microservices-recipes-a-free-gitbook/issues) for errors. Case studies: see [CONTRIBUTING.md](CONTRIBUTING.md). Watch the repository for releases.

---

## 📜 **License & Usage**

Dual license. **Code** is [MIT](LICENSE). **Prose and figures** are [CC BY-NC-ND 4.0](LICENSING.md).

### **Citation**
```
Khan, V. (2026). Microservices Recipes: The Architect's Field Guide (Version 2.1).
Zenodo. https://doi.org/10.5281/zenodo.22654421
```

---

## Read

[Chapter 1](chapters/01-introduction-to-microservices.md) · [Preface](PREFACE.md) · [Quick reference](reference/quick-reference.md)

---

<div align="center">

## How to cite

Machine-readable metadata: [CITATION.cff](CITATION.cff). Full guide: [CITATIONS.md](CITATIONS.md).

**APA:**
```
Khan, V. (2026). Microservices recipes: The architect's field guide (Version 2.1)
[Featuring Adaptive Granularity Governance: The Khan Microservice Pattern]. Zenodo.
https://doi.org/10.5281/zenodo.22654421
```

**IEEE:**
```
[1] V. Khan, Microservices Recipes: The Architect's Field Guide, ver. 2.1,
featuring Adaptive Granularity Governance: The Khan Microservice Pattern. Zenodo, 2026.
doi: 10.5281/zenodo.22654421.
```

---

## Copyright and licensing

**Copyright © 2019-2026 by Viquar Khan.**

**Adaptive Granularity Governance: The Khan Microservice Pattern**, the **Service Decomposition Workflow**, and the **Microservices Maturity Assessment (KM3)** are original methodologies by Viquar Khan; please cite. No trademark is claimed at this time.

| Material | License |
|----------|---------|
| Source code | [MIT](LICENSE) |
| Book text, diagrams, figures | [CC BY-NC-ND 4.0](LICENSING.md) |

Details: [LICENSING.md](LICENSING.md) | [COPYRIGHT.md](COPYRIGHT.md) | [DISCLAIMER.md](DISCLAIMER.md) | [NAMING.md](NAMING.md)

<sub>Last Updated: September 6, 2026 | Version 2.1 | Original work by Viquar Khan</sub>

</div>
