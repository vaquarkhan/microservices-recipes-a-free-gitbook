<div class="title-page" markdown="1">

# Microservices Recipes

<span class="book-edition-kicker">The Architect's Field Guide</span>

![Book Cover](assets/images/cover-image-2.png){:.book-cover-img}

**Adaptive Granularity Governance: The Khan Microservice Pattern**

*by **Viquar Khan***

**Version 2.1** · 23 chapters · September 2026

<p class="title-actions">
<a href="{{ "/chapters/01-introduction-to-microservices.html" | relative_url }}" class="book-cta">Start reading</a>
<a href="{{ "/PREFACE.html" | relative_url }}">Preface</a>
<a href="{{ "/AUTHOR.html" | relative_url }}">Author</a>
</p>

A service boundary is worth deploying separately only when it earns its distributed cost. Chapter 11 is the measurement. [Fulcrum / RVx](https://vaquarkhan.github.io/fulcrum-rxy/) is the research.

</div>

---

## Start here

<div class="start-paths">
  <a class="start-path" href="{{ "/chapters/01-introduction-to-microservices.html" | relative_url }}">
    <em>I</em>
    <strong>New to the argument</strong>
    <span>Chapter 1, then the Preface. Read Parts I through X in order.</span>
  </a>
  <a class="start-path" href="{{ "/reference/quick-reference.html" | relative_url }}">
    <em>II</em>
    <strong>Already in the work</strong>
    <span>Use the contents below. Keep the quick reference open.</span>
  </a>
  <a class="start-path" href="{{ "/chapters/11-khan-pattern-deep-dive.html" | relative_url }}">
    <em>III</em>
    <strong>Governing a portfolio</strong>
    <span>Chapters 2, 3, and 7, then Chapter 11. The 2017–2026 record is on the author page.</span>
  </a>
</div>

---

## Contents

### Front matter

- [Preface](PREFACE.md) - why a boundary has to earn its keep
- [About the Author](AUTHOR.md) - Viquar Khan
- [Mentorship](MENTORSHIP.md) - 1:1 on ADPList
- [Academic use](FREE-ACCESS.md) - the full book is public; cite it
- [Licensing](LICENSING.md) - MIT for code; CC BY-NC-ND 4.0 for prose
- [Naming](NAMING.md) - methodology title and attribution
- [Citations](CITATIONS.md) - how to cite this work
- [Copyright](COPYRIGHT.md) - owner and dual license
- [Disclaimer](DISCLAIMER.md) - legal notice
- [Contributing](CONTRIBUTING.md)
- [Version history](VERSION-HISTORY.md)
- [Changelog](CHANGELOG.md)

### Part I - The sociotechnical substrate

*Align the shape of the organization with the shape of the architecture.*

| | | |
|---|---|---|
| 1 | [Earned Boundaries, Not Fashionable Ones](chapters/01-introduction-to-microservices.md) | 35 min |
| 2 | [The Distributed Monolith: Diagnosis and First Remedies](chapters/02-design-principles-and-patterns.md) | 40 min |
| 3 | [Decouple the Language Before You Decouple the Code](chapters/03-service-communication.md) | 40 min |
{:.contents-table}

### Part II - Data architecture

*Splitting a system splits its data.*

| | | |
|---|---|---|
| 4 | [The End of ACID](chapters/04-data-management.md) | 45 min |
| 5 | [The Consistency Tax of Spanning Services](chapters/05-deployment-and-operations.md) | 45 min |
| 6 | [Close the Dual Write, Then Survive Failure](chapters/06-resilience-and-reliability.md) | 45 min |
| 7 | [Every Hop Is a Door. Prove Who Is Knocking.](chapters/07-security.md) | 50 min |
{:.contents-table}

### Part III - Evidence between processes

*You cannot attach a debugger to the space between services.*

| | | |
|---|---|---|
| 8 | [You Cannot Attach a Debugger. Emit the Evidence First.](chapters/08-monitoring-and-observability.md) | 50 min |
| 9 | [There Is No Whole System to Test. Test the Agreements.](chapters/09-testing-strategies.md) | 50 min |
| 10 | [Publish What Happened. Do Not Wait.](chapters/10-asynchronous-messaging-patterns.md) | 50 min |
{:.contents-table}

### Part IV - Adaptive Granularity Governance

*The score. Chapter 11 is the only source of truth for the formula.*

| | | |
|---|---|---|
| 11 | [A Boundary Earns Its Keep Only When All Three Hold](chapters/11-khan-pattern-deep-dive.md) | 70 min |
{:.contents-table}

### Part V - Resilience and scale

| | | |
|---|---|---|
| 12 | [A Single Bad Shard Should Be a Footnote](chapters/12-shuffle-sharding.md) | 55 min |
| 13 | [Break It on Purpose. Watch. Then You Know.](chapters/13-chaos-engineering.md) | 55 min |
{:.contents-table}

### Part VI - Platform

| | | |
|---|---|---|
| 14 | [The Definition Is the Truth. Reality Is Reconciled Toward It.](chapters/14-infrastructure-as-code-at-scale.md) | 55 min |
| 15 | [Spend the Budget on Answers. Stay Sighted When It Counts.](chapters/15-observability-2.md) | 55 min |
{:.contents-table}

### Part VII - Agents and retrieval

| | | |
|---|---|---|
| 16 | [The Model Proposes. The Executor Disposes.](chapters/16-agentic-ai-architectures.md) | 55 min |
| 17 | [Retrieval as a Data-Plane Discipline, Not a Prompt Trick](chapters/17-rag-at-scale.md) | 55 min |
{:.contents-table}

### Part VIII - Migration

| | | |
|---|---|---|
| 18 | [The Right Number of Services Is Often One.](chapters/18-modular-monolith.md) | 55 min |
| 19 | [Replace It While It Is Still Running.](chapters/19-strangler-fig-pattern.md) | 55 min |
{:.contents-table}

### Part IX - Organizational maturity

| | | |
|---|---|---|
| 20 | [Has This Organization Earned the Right to Distribute?](chapters/20-km3-maturity-model.md) | 50 min |
{:.contents-table}

### Part X - The science behind the metric

| | | |
|---|---|---|
| 21 | [Price the Waste. Name the Rest. Do Not Invent a Total.](chapters/21-pricing-the-distributed-monolith.md) | 50 min |
| 22 | [A Formula Confers No Truth. Outcomes Do.](chapters/22-construct-validity.md) | 50 min |
| 23 | [Never Point the Number at the People.](chapters/23-gaming-and-goodhart.md) | 50 min |
{:.contents-table}

### Reference

- [Glossary](reference/glossary.md)
- [Quick reference](reference/quick-reference.md)
- [Bibliography](reference/bibliography.md)

---

## The method

A boundary is worth deploying separately only when it is efficient at runtime, independent in how it changes, and small enough for its team to own. Chapter 11 measures that. Chapter 23 is the rule that keeps the measurement honest: do not use the score to review people.

![A monolith on the left. Earned service boundaries on the right.](assets/images/microservices-animation.gif){:.book-hero-gif}

---

## The author

**[Viquar Khan](AUTHOR.md)** is a Senior Data Architect at AWS Professional Services. He has kept this book in print, in public, from the 2017 eight-chapter edition through Version 2.1. On [Stack Overflow](https://stackoverflow.com/users/4812170/vaquar-khan) his helpful posts have 7.5 million people reached.

[Mentorship on ADPList](https://adplist.org/mentors/vaquar-khan). [ORCID](https://orcid.org/0009-0008-3592-4162) · [LinkedIn](https://www.linkedin.com/in/vaquar-khan-b695577/) · [GitHub](https://github.com/vaquarkhan)

---

## Colophon

**Copyright © 2017–2026 by Viquar Khan.** Dual license: MIT for code; CC BY-NC-ND 4.0 for prose and figures. See [LICENSING.md](LICENSING.md).

First edition January 2017. Second edition January 2026. Version 2.1 September 6, 2026. [Citations](CITATIONS.md) · [Copyright](COPYRIGHT.md) · [Disclaimer](DISCLAIMER.md)

[Star the repo](https://github.com/vaquarkhan/microservices-recipes-a-free-gitbook) · [Cite it](CITATIONS.md) · [Contributing](CONTRIBUTING.md)
