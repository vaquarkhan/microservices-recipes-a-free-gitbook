ï»¿# Book Preview

<div align="center">
  <img src="assets/images/cover-image-1.png" alt="Microservices Recipes book cover" width="360"/>
  <p>
    <img src="assets/images/cover-image-2.png" alt="Front cover" width="160"/>
    <img src="assets/images/cover-image-3.png" alt="Front cover" width="160"/>
    <img src="assets/images/cover-image-4.png" alt="Book on desk" width="160"/>
  </p>

  **Microservices Recipes: The Architect's Field Guide**  
  *By Viquar Khan Â· Version 2.1 Â· 23 chapters*
</div>

---

All 23 chapters are in this repository. There is no later paid half.

The argument is one sentence: a service boundary is worth deploying separately only when it earns its distributed cost. Chapter 11 is the measurement. Chapters 21â23 cover cost, whether the measurement is valid, and how you keep it from being gamed.

## The method

**Adaptive Granularity Governance** (the Khan Microservice Pattern) is the author's method. The RVx Index is the score. Chapter 11 is the only source of truth for the formula.

| Band | Meaning |
|------|---------|
| **> 0.7** | Healthy on the declared profile; still publish the three components |
| **0.4â0.7** | At-risk; diagnose which signal is weak |
| **< 0.4** | The boundary is not earning its keep |

## Contents

### Part I â Chapters 1â3
Organization and architecture. Distributed monolith. Strategic DDD (the file is still named `03-service-communication.md`).

### Part II â Chapters 4â7
Data, sagas, outbox, security. Chapter 7 is security, not Data Mesh.

### Part III â Chapters 8â10
Observability, testing agreements, messaging.

### Part IV â Chapter 11
Fulcrum, RVx, SCS, KM3 introduction, evidence tiers.

### Part V â Chapters 12â13
Shuffle sharding. Chaos with an abort outside the blast radius.

### Part VI â Chapters 14â15
Infrastructure as code. Observability 2.0.

### Part VII â Chapters 16â17
Agents. Retrieval with an ACL prefilter.

### Part VIII â Chapters 18â19
Modular monolith. Strangler fig.

### Part IX â Chapter 20
KM3 assessment.

### Part X â Chapters 21â23
Wasted time, construct validity, Goodhart.

## Read

- [Chapter 1](chapters/01-introduction-to-microservices.md)
- [Preface](PREFACE.md)
- [Chapter 11](chapters/11-khan-pattern-deep-dive.md)
- [Citations](CITATIONS.md)

**Connect:** [LinkedIn](https://www.linkedin.com/in/vaquar-khan-b695577/) Â· [GitHub](https://github.com/vaquarkhan) Â· [Mentorship](https://adplist.org/mentors/vaquar-khan)
