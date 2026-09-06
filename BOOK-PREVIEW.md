ï»¿Ã¯Â»Â¿# Book Preview

<div align="center">
  <img src="assets/images/cover-image-2.png" alt="Microservices Recipes book cover" width="360"/>

  **Microservices Recipes: The Architect's Field Guide**  
  *By Viquar Khan ÃÂ· Version 2.1 ÃÂ· 23 chapters*
</div>

---

All 23 chapters are in this repository. There is no later paid half.

The argument is one sentence: a service boundary is worth deploying separately only when it earns its distributed cost. Chapter 11 is the measurement. Chapters 21Ã¢ÂÂ23 cover cost, whether the measurement is valid, and how you keep it from being gamed.

## The method

**Adaptive Granularity Governance** (the Khan Microservice Pattern) is the author's method. The RVx Index is the score. Chapter 11 is the only source of truth for the formula.

| Band | Meaning |
|------|---------|
| **> 0.7** | Healthy on the declared profile; still publish the three components |
| **0.4Ã¢ÂÂ0.7** | At-risk; diagnose which signal is weak |
| **< 0.4** | The boundary is not earning its keep |

## Contents

### Part I Ã¢ÂÂ Chapters 1Ã¢ÂÂ3
Organization and architecture. Distributed monolith. Strategic DDD (the file is still named `03-service-communication.md`).

### Part II Ã¢ÂÂ Chapters 4Ã¢ÂÂ7
Data, sagas, outbox, security. Chapter 7 is security, not Data Mesh.

### Part III Ã¢ÂÂ Chapters 8Ã¢ÂÂ10
Observability, testing agreements, messaging.

### Part IV Ã¢ÂÂ Chapter 11
Fulcrum, RVx, SCS, KM3 introduction, evidence tiers.

### Part V Ã¢ÂÂ Chapters 12Ã¢ÂÂ13
Shuffle sharding. Chaos with an abort outside the blast radius.

### Part VI Ã¢ÂÂ Chapters 14Ã¢ÂÂ15
Infrastructure as code. Observability 2.0.

### Part VII Ã¢ÂÂ Chapters 16Ã¢ÂÂ17
Agents. Retrieval with an ACL prefilter.

### Part VIII Ã¢ÂÂ Chapters 18Ã¢ÂÂ19
Modular monolith. Strangler fig.

### Part IX Ã¢ÂÂ Chapter 20
KM3 assessment.

### Part X Ã¢ÂÂ Chapters 21Ã¢ÂÂ23
Wasted time, construct validity, Goodhart.

## Read

- [Chapter 1](chapters/01-introduction-to-microservices.md)
- [Preface](PREFACE.md)
- [Chapter 11](chapters/11-khan-pattern-deep-dive.md)
- [Citations](CITATIONS.md)

**Connect:** [LinkedIn](https://www.linkedin.com/in/vaquar-khan-b695577/) ÃÂ· [GitHub](https://github.com/vaquarkhan) ÃÂ· [Mentorship](https://adplist.org/mentors/vaquar-khan)
