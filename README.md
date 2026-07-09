# 📖 Microservices Recipes: The Architect's Field Guide

<div align="center">

![Microservices Recipes Cover](assets/images/cover-image-1.png)

**A practical guide to building, scaling, and managing microservices architectures**

As defined by Sam Newman in his foundational text *Building Microservices*, microservices are "small, autonomous services that work together." This definition emphasizes the dual requirements of independence and interoperability.

*Featuring Adaptive Granularity Governance: The Khan Microservice Pattern*

[![GitHub Pages](https://img.shields.io/badge/GitHub%20Pages-Live-brightgreen)](https://vaquarkhan.github.io/microservices-recipes-a-free-gitbook/)
[![License: MIT](https://img.shields.io/badge/Code-MIT-yellow.svg)](LICENSE)
[![Prose: CC BY-NC-ND 4.0](https://img.shields.io/badge/Prose-CC%20BY--NC--ND%204.0-lightgrey.svg)](LICENSING.md)
[![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)](CONTRIBUTING.md)

---

*"Stop splitting, start governing."* - **Adaptive Granularity Governance: The Khan Microservice Pattern**

![Microservices Animation](assets/images/microservices-animation.gif)

</div>

## 📋 Table of Contents

### 📚 **Front Matter**
- [📖 **Preface**](PREFACE.md) - The Architect's Mandate
- [👨‍💻 **About the Author**](AUTHOR.md) - Viquar Khan and Adaptive Granularity Governance
- [🎓 **Free Mentorship**](MENTORSHIP.md) - 1:1 Sessions with Viquar Khan
- [⚖️ **Licensing**](LICENSING.md) - MIT for code; CC BY-NC-ND 4.0 for prose and figures
- [🏷️ **Naming**](NAMING.md) - Methodology title and attribution
- [📖 **Citations Guide**](CITATIONS.md) - How to Cite This Work Properly
- [📜 **Copyright Notice**](COPYRIGHT.md) - Copyright and dual license
- [⚖️ **Disclaimer**](DISCLAIMER.md) - Legal notice
- [🤝 **Contributing**](CONTRIBUTING.md) - How to Contribute
- [📜 **Version History**](VERSION-HISTORY.md) - Release lineage
- [📋 **Changelog**](CHANGELOG.md) - 2017 to present change log
- [🎓 **Free Academic Access**](FREE-ACCESS.md) - Academic edition notes
- [📄 **CITATION.cff**](CITATION.cff) - Machine-readable citation metadata

---

### 📖 **Part I: The Sociotechnical Substrate**
*Focus: Aligning organization and architecture to prevent the "Distributed Monolith"*

| Chapter | Title | Description | Read Time |
|---------|-------|-------------|-----------|
| **[1](chapters/01-introduction-to-microservices.md)** | **The Definition Wars & The Reality of SOA** | Understanding microservices lineage and avoiding SOA's mistakes | 15 min |
| **[2](chapters/02-design-principles-and-patterns.md)** | **The Distributed Monolith and Anti Patterns** | Identifying and preventing distributed monolith anti-patterns | 25 min |
| **[3](chapters/03-service-communication.md)** | **Strategic Decomposition: Domain Driven Design** | Applying DDD principles to determine service boundaries | 20 min |

---

### 🗄️ **Part II: Data Architecture**
*Focus: Managing data consistency and transactions in distributed systems*

| Chapter | Title | Description | Read Time |
|---------|-------|-------------|-----------|
| **[4](chapters/04-data-management.md)** | **The End of ACID** | Understanding distributed data consistency challenges | 30 min |
| **[5](chapters/05-deployment-and-operations.md)** | **Distributed Transactions (The Saga Pattern)** | Implementing reliable distributed transactions | 25 min |
| **[6](chapters/06-resilience-and-reliability.md)** | **The Dual Write Problem** | Solving data consistency across service boundaries | 20 min |
| **[7](chapters/07-security.md)** | **Data Mesh vs. Data Fabric** | Modern approaches to distributed data management | 18 min |

---

### 🌐 **Part III: Inter Process Communication**
*Focus: Moving bits between services without creating latency storms*

| Chapter | Title | Description | Read Time |
|---------|-------|-------------|-----------|
| **[8](chapters/08-monitoring-and-observability.md)** | **The Trinity of Protocols** | HTTP/REST, gRPC, and GraphQL communication patterns | 22 min |
| **[9](chapters/09-testing-strategies.md)** | **The Rise of eBPF Networking and the Post Sidecar Era** | Next-generation service mesh and networking | 28 min |
| **[10](chapters/10-asynchronous-messaging-patterns.md)** | **Asynchronous Messaging Patterns** | Event-driven architecture and messaging strategies | 30 min |

---

### 🎯 **Part IV: Adaptive Granularity Governance**
*Focus: Quantitative framework for microservices decomposition (The Khan Microservice Pattern)*

| Chapter | Title | Description | Read Time |
|---------|-------|-------------|-----------|
| **11** | **Adaptive Granularity Governance: The Khan Microservice Pattern** | Origin, RVx Index, and maturity model | 40 min |

---

### 🧱 **Part V: Resilience Engineering & Advanced Scaling**
*Focus: Blast-radius control and evidence-based failure injection*

| Chapter | Title | Description | Read Time |
|---------|-------|-------------|-----------|
| **12** | **Shuffle Sharding & Blast-Radius Minimization** | Probabilistic tenant-shard assignment and collision analysis | 55 min |
| **13** | **Chaos Engineering & Evidence-Based Resilience** | Hypotheses, game days, and AWS FIS guardrails | 60 min |

---

### 🏗️ **Part VI: The Platform Engineering Shift**
*Focus: Golden paths, policy-as-code, and telemetry economics*

| Chapter | Title | Description | Read Time |
|---------|-------|-------------|-----------|
| **14** | **Infrastructure as Code at Scale** | Modules, drift, Terraform/CDK/Pulumi trade-offs | 58 min |
| **15** | **Observability 2.0** | OpenTelemetry, X-Ray, wide events, sampling design | 62 min |

---

### 🤖 **Part VII: The AI Frontier (2026)**
*Focus: Probabilistic components inside deterministic architectures*

| Chapter | Title | Description | Read Time |
|---------|-------|-------------|-----------|
| **16** | **Agentic AI Architectures** | Tool gateways, Bedrock agents, safety cases | 58 min |
| **17** | **Retrieval-Augmented Generation at Scale** | HyDE, evaluation, ACL-aware corpora | 60 min |

---

### 🚀 **Part VIII: The Migration Playbook**
*Focus: Monolith-first discipline and incremental replacement*

| Chapter | Title | Description | Read Time |
|---------|-------|-------------|-----------|
| **18** | **The Modular Monolith** | Schema-per-module, ArchUnit, contraction economics | 55 min |
| **19** | **The Strangler Fig Pattern** | Edge routing, data strangler, parity proofs | 55 min |

---

### 📈 **Part IX: Organizational Maturity**
*Focus: KM3 operational assessment*

| Chapter | Title | Description | Read Time |
|---------|-------|-------------|-----------|
| **20** | **The Khan Microservices Maturity Model (KM3)** | Stages, instrumentation, X-Ray sampling | 50 min |

---

### 📚 **Reference Materials**

| Resource | Description |
|----------|-------------|
| **[📖 Glossary](reference/glossary.md)** | Comprehensive definitions of microservices terms |
| **[⚡ Quick Reference](reference/quick-reference.md)** | Handy reference cards for patterns and practices |
| **[📚 Bibliography](reference/bibliography.md)** | Curated list of books, articles, and resources |

---

## 🎯 **What Makes This Book Special**

### **Adaptive Granularity Governance: The Khan Microservice Pattern**

At the heart of this book is **Adaptive Granularity Governance: The Khan Microservice Pattern** (formerly the Adaptive Granularity Strategy): a systematic methodology for determining optimal microservice boundaries. This adaptive framework considers your specific:

**Field basis:** The methodology is an original synthesis by the author, refined through professional practice. Please cite when you reuse it ([CITATIONS.md](CITATIONS.md)).

- **Organizational maturity** and team structure
- **Business domain complexity** and change frequency  
- **Technical constraints** and operational capabilities
- **Evolutionary growth** and learning patterns

> *"The goal is not to build the perfect architecture, but to build an architecture that can evolve toward perfection."* - Viquar Khan

### **Key Features**

✅ **Practical, Not Theoretical** - Every pattern tested in production  
✅ **Context-Aware Guidance** - Solutions for different organizational contexts  
✅ **Evolution-Focused** - Architecture as a journey, not a destination  
✅ **Anti-Pattern Awareness** - Learn from real-world failures  
✅ **Complete Framework** - Design through operations coverage  

---

## 🚀 **Quick Start Guide**

### **For Beginners**
1. Start with [**Chapter 1: The Definition Wars**](chapters/01-introduction-to-microservices.md)
2. Read [**The Preface**](PREFACE.md) to understand the book's philosophy
3. Progress sequentially through Parts I → II → III

### **For Experienced Practitioners**
1. Review the [**Table of Contents**](#-table-of-contents) above
2. Jump to specific chapters addressing your current challenges
3. Use [**Quick Reference**](reference/quick-reference.md) for rapid pattern lookup

### **For Architects**
1. Focus on strategic chapters: [Ch 2](chapters/02-design-principles-and-patterns.md), [Ch 3](chapters/03-service-communication.md), [Ch 7](chapters/07-security.md)
2. Study [**Adaptive Granularity Governance: The Khan Microservice Pattern**](AUTHOR.md#adaptive-granularity-governance-the-khan-microservice-pattern) (formerly Adaptive Granularity Strategy)
3. Review [**Complete Book Preview**](BOOK-PREVIEW.md) for advanced topics

---

## 📊 **Book Statistics**

| Metric | Value |
|--------|-------|
| **Total Chapters** | 20 (chapters 1-10 linked in TOC; 11-20 listed without open links) |
| **Reading Time** | ~4.5 hours total |
| **Content Length** | 236,000+ characters |
| **Code Examples** | 50+ practical implementations |
| **Patterns Covered** | 25+ architectural patterns |
| **Case Studies** | Real-world examples from industry leaders |
| **GitHub Stars** | 606 developers |
| **Repository Forks** | 228 active forks |
| **Author Followers** | 1,400+ on [@vaquarkhan](https://github.com/vaquarkhan) |
| **Community Reach** | Global developer community |

---

## 🌟 **What You'll Master**

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

### **Credentials**
- 🏆 **JSR 368** Expert Group Member (Java Message Service 2.1)
- 📚 **Author** of "Data Engineering with AWS Cookbook" (Packt, 2026)
- 🌟 **7.5M+** developers reached on [Stack Overflow](https://stackoverflow.com/users/4812170/vaquar-khan)
- 👥 **1,400+** GitHub followers ([@vaquarkhan](https://github.com/vaquarkhan))
- 🔧 **50+** open-source microservices repositories

**Connect:** [LinkedIn](https://www.linkedin.com/in/vaquar-khan-b695577/) | [GitHub](https://github.com/vaquarkhan) | [Amazon Author](https://us.amazon.com/stores/Viquar-Khan/author/B0DMJCG9W6) | [🎓 Free Mentorship](https://adplist.org/mentors/vaquar-khan)

---

## 🌐 **Access This Book**

### **📖 Read Online**
- **GitHub Pages**: [https://vaquarkhan.github.io/microservices-recipes-a-free-gitbook/](https://vaquarkhan.github.io/microservices-recipes-a-free-gitbook/)
- **GitHub Repository**: [https://github.com/vaquarkhan/microservices-recipes-a-free-gitbook](https://github.com/vaquarkhan/microservices-recipes-a-free-gitbook)

### **🎓 Academic Access**
- **Complete 20-Chapter Edition**: [Request Free Access](FREE-ACCESS.md) for students, faculty, and researchers under my Official Academic License
- **Citation Guide**: [Proper Citation Formats](CITATIONS.md) for academic use
- **Version History**: [Release Lineage](VERSION-HISTORY.md) and evolution

### **💾 Download Options**
- **Clone Repository**: `git clone https://github.com/vaquarkhan/microservices-recipes-a-free-gitbook.git`
- **Download ZIP**: [Latest Release](https://github.com/vaquarkhan/microservices-recipes-a-free-gitbook/archive/main.zip)
- **PDF Version**: Available through [Academic Access Program](FREE-ACCESS.md)

---

## 🤝 **Community & Support**

### **🌟 Support This Open Knowledge Initiative**
If you find this resource valuable, please help me keep it free and accessible:

**⭐ [Star this repository](https://github.com/vaquarkhan/microservices-recipes-a-free-gitbook)** - Help others discover this work  
**🍴 [Fork the project](https://github.com/vaquarkhan/microservices-recipes-a-free-gitbook/fork)** - Build upon these methodologies  
**📖 [Cite properly](CITATIONS.md)** - Support academic recognition  

### **Get Involved**
- 🐛 **[Report Issues](https://github.com/vaquarkhan/microservices-recipes-a-free-gitbook/issues)** - Found an error or have suggestions?
- 💡 **Share Case Studies** - Connect with the author to share real-world implementation experiences
- 📊 **View Impact** - See global reach: 606 stars, 228 forks, 1,400+ followers on [@vaquarkhan](https://github.com/vaquarkhan)
- 🔄 **[See Guidelines](CONTRIBUTING.md)** - Learn about acceptable contributions
- ⭐ **Star this repo** if you find it valuable!

### **Professional Networks**
- 🔗 **LinkedIn**: [Microservices Architecture Practitioners Group](https://www.linkedin.com/groups/microservices-practitioners)
- � **ResearchGate**: [Academic Collaboration Hub](https://researchgate.net/profile/viquar-khan)

### **Stay Updated**
- 📢 **Watch** this repository for updates
- 🔔 **Follow** [@vaquarkhan](https://github.com/vaquarkhan) for announcements
- 📧 **Subscribe** to release notifications

---

## 📜 **License & Usage**

This book is released under the **[MIT License](LICENSE)** - free for personal and commercial use.

### **Citation**
```
Khan, V. (2026). Microservices Recipes: The Architect's Field Guide. 
GitHub. https://github.com/vaquarkhan/microservices-recipes-a-free-gitbook
```

---

## 🚀 **Ready to Begin Your Journey?**

<div align="center">

### **Choose Your Path**

[![Start Reading](https://img.shields.io/badge/📖_Start_Reading-Chapter_1-blue?style=for-the-badge)](chapters/01-introduction-to-microservices.md)
[![Read Preface](https://img.shields.io/badge/📜_Read_Preface-Philosophy-green?style=for-the-badge)](PREFACE.md)
[![Quick Reference](https://img.shields.io/badge/⚡_Quick_Reference-Patterns-orange?style=for-the-badge)](reference/quick-reference.md)

---

*"The journey of a thousand microservices begins with a single service boundary."*

**Build better, more scalable systems with proven methodologies.** 🚀

</div>

---

<div align="center">

## How to cite

Machine-readable metadata: [CITATION.cff](CITATION.cff). Full guide: [CITATIONS.md](CITATIONS.md).

**APA:**
```
Khan, V. (2026). Microservices recipes: The architect's field guide (Version 2.0)
[Featuring Adaptive Granularity Governance: The Khan Microservice Pattern]. GitHub.
https://github.com/vaquarkhan/microservices-recipes-a-free-gitbook
```

**IEEE:**
```
[1] V. Khan, Microservices Recipes: The Architect's Field Guide, ver. 2.0,
featuring Adaptive Granularity Governance: The Khan Microservice Pattern. GitHub, 2026.
[Online]. Available: https://github.com/vaquarkhan/microservices-recipes-a-free-gitbook
```

---

## Copyright and licensing

**Copyright © 2017-2026 by Vaquar Khan.**

**Adaptive Granularity Governance: The Khan Microservice Pattern**, the **Service Decomposition Workflow**, and the **Microservices Maturity Assessment (KM3)** are original methodologies by Vaquar Khan; please cite. No trademark is claimed at this time.

| Material | License |
|----------|---------|
| Source code | [MIT](LICENSE) |
| Book text, diagrams, figures | [CC BY-NC-ND 4.0](LICENSING.md) |

Details: [LICENSING.md](LICENSING.md) | [COPYRIGHT.md](COPYRIGHT.md) | [DISCLAIMER.md](DISCLAIMER.md) | [NAMING.md](NAMING.md)

<sub>Last Updated: July 9, 2026 | Original work by Vaquar Khan</sub>

</div>
