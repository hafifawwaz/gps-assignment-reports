---
source: report/plans/m-ceus-paper.md
date: 26-10-2026
kind: plan
comments: true
generated: 2026-11-06T11:37:20
---

# CEUS paper

<p class="doc-meta"><span class="chip chip-plan">Plan</span> <span class="chip chip-lane">Done</span> <span class="chip chip-project">Master</span> <span class="chip chip-date">26-10-2026</span></p>

A methodological paper for the journal *Computers, Environment and Urban Systems* (CEUS), written from the content of the master's thesis ([Thesis summary](../threads/m-thesis-summary.md)). It presents how to assign GPS stays to buildings, streets and open spaces with probabilities, under GPS error. The model learns from the Hiroshima ground truth (GT), the stays with known correct answers from the field survey.

All the material already exists in the thesis. The paper uses the final numbers: 11 parameters, α = 2.979, grouped CV accuracy 0.718 ± 0.028 ([Final model](../analysis/m-final-model.md)).

## Revisions from the meeting on 20-10-2026
Revised [d-progress-05-11-2026](../progress/d-progress-05-11-2026.md)

1. **Show an outdoor and an indoor cluster on a map.** Take examples from the GT and show visually, on a map, how a stay outdoors and a stay indoors look. Add a light comparison with nearest-entity assignment: the place nearest the stay, picked with no probabilities.
2. **An example for every step.** Take one stay and illustrate how the framework works on it, step by step ([Framework overview](../concepts/m-framework-overview.md)).
3. **One column.** Change the format to a single column. Two columns is the old format.

Meeting: [Publications and doctoral plan](../progress/d-progress-20-10-2026.md).

Part of [Outlook](../threads/m-outlook.md).


<div class="backlinks" markdown>

**Linked from** [CEUS paper revisions](../progress/d-progress-05-11-2026.md) · [Doctoral plan](../threads/d-doctoral-plan.md) · [Publications and doctoral plan](../progress/d-progress-20-10-2026.md)

</div>
