---
source: report/concepts/m-overfitting-signature.md
date: 25-07-2026
kind: concept
comments: true
generated: 2026-10-26T20:41:14
---

# Overfitting signature

<p class="doc-meta"><span class="chip chip-concept">Concept</span> <span class="chip chip-project">Master</span> <span class="chip chip-date">25-07-2026</span></p>

Again and again, a more complex model fit the training data better **without doing better on unseen data**. That is the sign of overfitting: the model learns details of this sample that do not carry over. Three cases:

1. Adding σ² and f_distribution × share_type at the tuned α: [Stepwise VIF elimination](../analysis/m-stepwise-vif-elimination.md)
2. Giving `f_directional` a separate weight per type: [f_directional: shared vs split](../analysis/m-f-directional-shared-vs-split.md)
3. The squared distance term, before α was tuned: [The f_distance² artifact](../analysis/m-f-distance-squared-artifact.md)

One step does not fit this pattern. The ASC terms (a fixed extra value per type) also raised accuracy on unseen data. They were rejected because they copy another input, not because of overfitting ([Model 5: alternative-specific constants (rejected)](../analysis/m-model-5-asc-rejected.md)).

The tree models show the same thing on a bigger scale. Both beat the simple model on the training data and lose to it on unseen data ([ML ceiling check, row level](../analysis/m-ml-ceiling-row-level.md)).

Why this matters for MILES: the survey's mix of 59% building, 20% street and 21% open space was set by the survey plan ([Ground truth dataset](m-ground-truth-dataset.md)). The `share_type` weights learned patterns of this sample. MILES may have a different mix, so it is not yet known how well the model will work there ([Limitations](m-limitations.md)).

Answers [Research questions](m-research-questions.md) RQ3. Part of [Complexity and transfer](../threads/m-complexity-and-transfer.md).


<div class="backlinks" markdown>

**Linked from** [Complexity and transfer](../threads/m-complexity-and-transfer.md) · [Future work](m-future-work.md) · [Ground truth dataset](m-ground-truth-dataset.md) · [Limitations](m-limitations.md) · [ML ceiling check, row level](../analysis/m-ml-ceiling-row-level.md) · [Model 5: alternative-specific constants (rejected)](../analysis/m-model-5-asc-rejected.md) · [Research questions](m-research-questions.md) · [The f_distance² artifact](../analysis/m-f-distance-squared-artifact.md) · [f_directional: shared vs split](../analysis/m-f-directional-shared-vs-split.md)

</div>
