---
source: report/concepts/m-positioning-vs-deterministic-assignment.md
date: 23-07-2026
kind: concept
comments: true
generated: 2026-10-26T20:41:14
---

# Positioning against deterministic assignment

<p class="doc-meta"><span class="chip chip-concept">Concept</span> <span class="chip chip-project">Master</span> <span class="chip chip-date">23-07-2026</span></p>

How this method differs from methods that give one fixed answer (deterministic methods).

Chapter 2 describes two of them. SMoT checks whether part of a GPS track stays inside a place's outline for a minimum time (Alvares et al., 2007). Wu et al. (2026) give each GPS point to its nearest place. Both choose one place and say nothing about how sure they are.

Wu et al. do calculate the chance of a wrong answer. That chance depends on the GPS error and on how close the point is to the edge of a place. But they only use it afterwards, to report accuracy. This method builds the same idea into the answer itself: it gives a probability for each type. Its accuracy on unseen data is 0.719 ± 0.032 ([Final model](../analysis/m-final-model.md)).

Would a more flexible model do better? Research question 3 says no. Random Forest and XGBoost fit the training data better (0.750 and 0.829, against 0.731), but they do worse on unseen data (0.708 and 0.703, against 0.719) ([ML ceiling check, row level](../analysis/m-ml-ceiling-row-level.md)). The simple model has the right amount of complexity for this data. And anyone can read it: it is just eleven weights, each with a clear sign.

A subsection of the Discussion in the thesis. Part of [Problem and positioning](../threads/m-problem-and-positioning.md).


<div class="backlinks" markdown>

**Linked from** [Problem and positioning](../threads/m-problem-and-positioning.md)

</div>
