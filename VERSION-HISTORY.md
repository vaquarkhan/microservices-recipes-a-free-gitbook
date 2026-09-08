# 📚 Version History & Release Lineage

**Microservices Recipes: The Architect's Field Guide**  
*by Viquar Khan*

---

## 🏷️ **Current Version: 2.1**

### **Version 2.1** — *Science edition, 23 chapters* (September 6, 2026)

- Chapters 21–23 added: pricing wasted time, construct validity, Goodhart and tamper-evidence.
- Practitioner chapters 1–20 aligned to one spine. Chapter 11 remains the only source of truth for the RVx formula (β=1.2, α=0.8, ε=0.1; bands &lt;0.4 / 0.4–0.7 / &gt;0.7).
- Editorial SVGs replace chapter figures. Original book covers from `assets/images` are used on Home, Preface, Author, and Copyright.
- Preface, book preview, glossary, and quick reference no longer restate a swapped-exponent formula or a 20-chapter teaser.
- Recipes corrected: Kinesis idempotency JMESPath, human-approval Step Functions (no heartbeat without `SendTaskHeartbeat`), gateway authorizer response shape, Collector Contrib for tail sampling.

### **Version 2.0** - *Adaptive Granularity Governance edition* (January 2026)
**Major revision**

**Disclosure (historical name):** v2.0 (January 2026): Adaptive Granularity Strategy and RVx Index introduced.

#### **🎯 New Features & Enhancements:**
- **Adaptive Granularity Governance: The Khan Microservice Pattern** (formerly Adaptive Granularity Strategy) - Systematic approach to microservice boundaries
- **RVx Index** - Quantitative service-boundary effectiveness score
- **Service Decomposition Workflow** - Systematic methodology for service decomposition
- **Microservices Maturity Assessment (KM3)** - Assessment framework for organizational readiness
- **Chapter headers** — reading time and difficulty
- **GitHub Pages layout**
- **Updated case material** from 2020–2026 practice
- **eBPF Networking Coverage** - Post-sidecar era networking patterns
- **Cloud-Native Focus** - AWS, Kubernetes, and modern container orchestration

#### **📖 Content Updates:**
- RVx Index and KM3 introduced
- Security, data, and observability chapters rewritten for current practice

#### Site and markup
- Markdown that builds on GitHub Pages
- Book CSS and navigation for the Pages site

---

### **Version 2.0.1** - *Naming and licensing clarity* (July 9, 2026)

- Renamed the methodology to **Adaptive Granularity Governance: The Khan Microservice Pattern** (RVx Index unchanged).
- Dual license documented: MIT for code; CC BY-NC-ND 4.0 for book prose, diagrams, and figures ([LICENSING.md](LICENSING.md)).
- Added [NAMING.md](NAMING.md), [CITATION.cff](CITATION.cff), [docs/RVX-SPEC.md](docs/RVX-SPEC.md), [docs/PATTERN-HISTORY.md](docs/PATTERN-HISTORY.md), reference-impl MVP, and validation plan.
- Removed contradictory "All rights reserved" / "proprietary" language next to the MIT grant; no trademark symbols claimed.

## 📜 **Legacy Versions**

### **Version 1.0** - *Foundational Edition* (2017)
**Initial public edition**

#### **📖 Original Content:**
- **8 Core Chapters** covering fundamental microservices concepts
- **SOA vs Microservices** - Historical context and evolution
- **Domain-Driven Design** - Strategic decomposition principles  
- **Data Management Patterns** - ACID to eventual consistency
- **Communication Protocols** - REST, messaging, and RPC patterns
- **Deployment Strategies** - Container orchestration basics
- **Monitoring & Observability** - Distributed tracing foundations
- **Security Fundamentals** - Authentication and authorization patterns
- **Testing Approaches** - Unit, integration, and contract testing

#### What 1.0 covered
- Foundational field guide to implementation
- Anti-patterns and common failure modes
- Conway's Law and team structure
- Principles over a specific tool stack

---

## 🔄 **Evolution Timeline**

### **2017 - Genesis**
- **Initial concept** developed as version one when microservices started
- **First draft** based on real-world enterprise transformations
- **Community feedback** incorporated from early adopters

### **2018-2019 - Refinement**
- **Case study additions** from successful implementations
- **Anti-pattern documentation** from failed transformations
- **Tool ecosystem updates** reflecting market evolution

### **2020-2021 - Pandemic Adaptations**
- **Remote team considerations** added to organizational patterns
- **Cloud-first approaches** emphasized due to digital acceleration
- **Resilience patterns** enhanced for distributed workforce support

### **2022-2023 - Modern Patterns**
- **Kubernetes-native patterns** integrated throughout
- **Service mesh evolution** documented with real implementations
- **Observability** updated for OpenTelemetry-era practice

### **2024-2025 - Original research (Fulcrum / RVx)**
- The field still had no operational formula that said a given boundary *is* a distributed monolith. The concepts were in the book. The score was not.
- Research years for **Fulcrum** and the **RVx Index**: Khan's Law, three-signal fusion (E, S, L), SCS, KM3, wasted-time cost. Companion site: [fulcrum-rxy](https://vaquarkhan.github.io/fulcrum-rxy/). Paper in 2026; arXiv forthcoming.
- Math properties proved. 36-boundary AWS estate demonstrated (directional). Organic production still hypothesized.

### **2026 - Adaptive Granularity Governance**
- **Systematic methodology** introduced (January 2026) under the historical name Adaptive Granularity Strategy, with the **RVx Index**
- **July 2026:** renamed to **Adaptive Granularity Governance: The Khan Microservice Pattern** (RVx unchanged); dual license and citation scaffolding published
- Methodology and score added to the existing field guide

---

## 📈 **Version Comparison Matrix**

| Feature | Version 1.0 (2017) | Version 2.1 (2026) |
|---------|-------------------|-------------------|
| **Chapters** | 8 foundational | 23 (Parts I–X) |
| **Methodologies** | General principles | Adaptive Granularity Governance: The Khan Microservice Pattern (formerly Adaptive Granularity Strategy) |
| **Technology Focus** | Docker, basic K8s | Modern cloud-native |
| **Networking** | Traditional service mesh | eBPF and post-sidecar |
| **Data Patterns** | Basic CQRS/ES | Advanced distributed patterns |
| **Security** | Traditional auth | Zero-trust architectures |
| **Case Studies** | 2015-2017 examples | 2020-2026 implementations |
| **Assessment Tools** | Informal checklists | Microservices Maturity Assessment |
| **Reading** | Markdown in the repo | GitHub Pages plus chapter figures |

---

## 🎯 **Future Roadmap**

### **After 2.1**
Version 2.1 shipped on September 6, 2026: 23 chapters, editorial SVGs, and the science arc (cost, construct validity, Goodhart). Further work is empirical validation of organic-production separation, not a new formula. See `validation/` and Chapter 22. The old "planned Q2 2026" 2.1 teaser on this page is retired.

There is no “coming soon” half of the book. Version 2.1 is the public edition.

---

## 📚 **Citation & Academic Use**

### **Recommended Citation (APA Style):**
```
Khan, V. (2026). Microservices Recipes: The Architect's Field Guide (Version 2.1). 
GitHub. https://github.com/vaquarkhan/microservices-recipes-a-free-gitbook
https://orcid.org/0009-0008-3592-4162
```

### **Recommended Citation (IEEE Style):**
```
V. Khan, "Microservices Recipes: The Architect's Field Guide," ver. 2.1, 
GitHub Repository, 2026. [Online]. Available: 
https://github.com/vaquarkhan/microservices-recipes-a-free-gitbook
```

### **Recommended Citation (Chicago Style):**
```
Khan, Viquar. Microservices Recipes: The Architect's Field Guide. Version 2.1. 
GitHub, 2026. https://github.com/vaquarkhan/microservices-recipes-a-free-gitbook.
```


## 📞 **Version Support**

### **Current Support:**
- **Version 2.1** - ✅ Current public edition (23 chapters, September 2026)
- **Version 1.0** - 📚 Archived, available for historical reference

### **Community Channels:**
- **GitHub Issues** - Bug reports and feature requests
- **GitHub Discussions** - Community Q&A and best practices
- **LinkedIn** - Professional networking and updates

---

See [CHANGELOG.md](CHANGELOG.md) for the 2017-to-present record. Do not drop older entries when you add a new version. The author’s own account of how the book grew is on [AUTHOR.md](AUTHOR.md).
