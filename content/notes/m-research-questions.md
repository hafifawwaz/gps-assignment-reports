---
source: report/notes/m-research-questions.md
date: 25-07-2026
kind: note
comments: true
generated: 2026-10-14T14:44:07
---

# Research questions

<p class="doc-meta"><span class="chip chip-note">Note</span> <span class="chip chip-project">Master</span> <span class="chip chip-date">25-07-2026</span></p>

**Goal:** a method that gives each GPS stay a probability for building, street and open space. The method takes GPS error into account by measuring each stay itself: how spread out its points are, and how they move over time.

- **RQ1:** How can GPS error be built into a method that gives probabilities for several types of place? → [Framework overview](m-framework-overview.md), and how the model was built step by step: [Calibration](../threads/m-calibration.md)
- **RQ2:** How well do the method's answers match the correct answers from the field survey? → [Confusion matrix](../analysis/m-confusion-matrix.md)
- **RQ3:** Does a more complex model fit better? And does that extra complexity make it worse on new data, where the mix of place types may be different? → [Overfitting signature](m-overfitting-signature.md), [ML ceiling check, row level](../analysis/m-ml-ceiling-row-level.md)

Part of [Problem and positioning](../threads/m-problem-and-positioning.md).


<div class="backlinks" markdown>

**Linked from** [Confusion matrix](../analysis/m-confusion-matrix.md) · [Framework overview](m-framework-overview.md) · [Motivation](m-motivation.md) · [Overfitting signature](m-overfitting-signature.md) · [Problem and positioning](../threads/m-problem-and-positioning.md) · [Thesis summary](../threads/m-thesis-summary.md)

</div>
