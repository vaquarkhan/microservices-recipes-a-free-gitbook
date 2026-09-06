# Book Preview

<div align="center">
  <img src="assets/images/cover-image-1.png" alt="Microservices Recipes book cover" width="360"/>

  **Microservices Recipes: The Architect's Field Guide**  
  *By Viquar Khan · Version 2.1 · 23 chapters*
</div>

---

This page is a map of the book that is actually in the repository. It is not a teaser for a later paid edition. All **23 chapters** are here, on GitHub Pages and in the repo.

The spine is one argument: **a service boundary is worth deploying separately only when it earns its distributed cost.** Chapter 11 defines the measurement. Chapters 21–23 say what the measurement costs, whether it is valid, and how you keep it from being gamed.

## The method, without reprinting the formula

**Adaptive Granularity Governance: The Khan Microservice Pattern** is the author's method for deciding service granularity with evidence instead of fashion. The RVx Index is the score at its centre. Chapter 11 is the only source of truth for the equation, the defaults, the squash, the bands, and the evidence tiers.

Read a score as a check-engine light, not a high-score table:

| Band | Meaning |
|------|---------|
| **> 0.7** | Healthy on the declared profile; still publish the three components |
| **0.4–0.7** | At-risk; diagnose which signal is weak |
| **< 0.4** | The boundary is not earning its keep |

Older drafts and slides sometimes swapped a and ß, used bands at 0.3 / 0.6, or named a "Nano-Swarm zone." Discard those. If a preview page restates the formula, it is already out of date.

## What the book actually contains

### Part I — The sociotechnical substrate (Chapters 1–3)
- **Chapter 1.** Earned boundaries, not fashionable ones. SOA inverted. Temporal coupling from Git.
- **Chapter 2.** The distributed monolith: diagnosis, Conway, Team APIs, first remedies.
- **Chapter 3.** Strategic DDD: bounded contexts, context maps, Event Storming. The filename still says "service communication." The chapter is about language.

### Part II — Data architecture (Chapters 4–7)
- **Chapter 4.** The end of ACID. CAP/PACELC, ownership, listen-to-yourself.
- **Chapter 5.** Sagas and the consistency tax. The filename still says "deployment."
- **Chapter 6.** Close the dual write, then survive failure. Outbox, timeouts, breakers.
- **Chapter 7.** Security. Every hop is a door. Not Data Mesh. Recipe 7.1 is a gateway JWT authorizer.

### Part III — Evidence between processes (Chapters 8–10)
- **Chapter 8.** Observability as the evidence you emit first.
- **Chapter 9.** Test the agreements. Contracts, not a fictional whole-system suite.
- **Chapter 10.** Publish what happened. Backpressure, poison, claim check.

### Part IV — The Khan Microservice Pattern (Chapter 11)
Fulcrum, RVx, SCS, KM3 introduction, honesty tiers. This is the definition chapter.

### Part V — Resilience and scale (Chapters 12–13)
Shuffle sharding inside cells. Chaos with an abort outside the blast radius.

### Part VI — Platform engineering (Chapters 14–15)
IaC as desired state. Observability 2.0: wide events, tail sampling, eBPF as a cross-check.

### Part VII — The AI frontier (Chapters 16–17)
The model proposes; the executor disposes. RAG as a data-plane discipline with ACL prefilter.

### Part VIII — Migration (Chapters 18–19)
Modular monolith first. Strangler fig while the system is still running.

### Part IX — Organizational maturity (Chapter 20)
KM3 assessment: Ad hoc ? Instrumented ? Governed ? Portfolio-managed ? Self-correcting. Not a badge race.

### Part X — The science behind the metric (Chapters 21–23)
Price wasted time without inventing a dollar total. Construct validity and evidence tiers. Tamper-evidence and the rule that the metric never evaluates people.

## How to read it

- [Start at Chapter 1](chapters/01-introduction-to-microservices.md)
- [Preface](PREFACE.md)
- [Chapter 11, the formula](chapters/11-khan-pattern-deep-dive.md)
- [Quick reference](reference/quick-reference.md)
- [Glossary](reference/glossary.md)

**Connect:** [LinkedIn](https://www.linkedin.com/in/vaquar-khan-b695577/) · [GitHub](https://github.com/vaquarkhan) · [Mentorship](https://adplist.org/mentors/vaquar-khan)
