---
source: report/notes/overfitting-signature.md
date: 25-07-2026
kind: note
comments: true
generated: 2026-10-13T20:05:33
---

# Overfitting signature

<p class="doc-meta"><span class="chip chip-note">Note</span> <span class="chip chip-date">25-07-2026</span></p>

Across the calibration, extra complexity repeatedly bought **in-sample gains without matching CV gains**:

1. Adding an ASC: [Model 5: alternative-specific constants (rejected)](../analysis/model-5-asc-rejected.md)
2. Splitting `f_directional` by type: [f_directional: shared vs split](../analysis/f-directional-shared-vs-split.md)
3. The squared distance term at uncalibrated alpha: [The f_distance² artifact](../analysis/f-distance-squared-artifact.md)

Tree models show it at larger scale: both beat the logit in-sample and lose to it under grouped CV ([ML ceiling check, row level](../analysis/ml-ceiling-row-level.md)).

Why it matters for MILES: the ground truth's 59/20/21 type split is a design artifact ([Ground truth dataset](ground-truth-dataset.md)), and `share_type` weights fit sample-specific patterns, so transfer to MILES's unknown type mix is an untested risk ([Limitations](limitations.md)).

Answers [Research questions](research-questions.md) RQ3. Part of [Complexity and transfer](../threads/complexity-and-transfer.md).


<div class="backlinks" markdown>

**Linked from** [Complexity and transfer](../threads/complexity-and-transfer.md) · [Future work](future-work.md) · [Ground truth dataset](ground-truth-dataset.md) · [Limitations](limitations.md) · [ML ceiling check, row level](../analysis/ml-ceiling-row-level.md) · [Model 5: alternative-specific constants (rejected)](../analysis/model-5-asc-rejected.md) · [Research questions](research-questions.md) · [The f_distance² artifact](../analysis/f-distance-squared-artifact.md) · [f_directional: shared vs split](../analysis/f-directional-shared-vs-split.md)

</div>
