---
source: report/progress/m-progress-21-07-2026.md
date: 21-07-2026
kind: progress
comments: true
generated: 2026-10-26T20:41:14
---

# RQ1 rebuilt with grouped CV

<p class="doc-meta"><span class="chip chip-progress">Progress</span> <span class="chip chip-project">Master</span> <span class="chip chip-date">21-07-2026</span></p>

All models were tested again with a fairer method.

- **The problem.** Three phones recorded each stop at the same time. In the old cross-validation (CV), one phone's recording of a stop could be in the training data and another phone's recording of the same stop in the test data. That made results look better than they really are. All models were fitted again with [Grouped cross-validation](../concepts/m-grouped-cross-validation.md), which keeps all recordings of one stop together ([Model progression](../analysis/m-model-progression-table.md)).
- **What changed.** The best model kept the same form and the same accuracy on its training data (0.733). On unseen data it scored **0.712 ± 0.038**. This is the fairer number.
- **What stayed the same.** [Alpha calibration](../analysis/m-alpha-calibration.md) found α = 2.764 again. The model with ASC terms was rejected again ([Model 5: alternative-specific constants (rejected)](../analysis/m-model-5-asc-rejected.md)), and f_distance² was again shown to be a side effect of the wrong α ([The f_distance² artifact](../analysis/m-f-distance-squared-artifact.md)). Removing weak terms ([Stepwise VIF elimination](../analysis/m-stepwise-vif-elimination.md)) gave the 13-parameter model, the core of Model 4a.
- **Follow-up.** `f_directional` does not need a separate weight for each place type (p = 0.054, not significant). The **11-parameter version with one shared weight** does better on unseen data (0.719 ± 0.032) and is more stable: [f_directional: shared vs split](../analysis/m-f-directional-shared-vs-split.md) → [Final model](../analysis/m-final-model.md).

The 11-parameter model is the final model of the thesis (Section 5.1.8).


<div class="backlinks" markdown>

**Linked from** [Assignment framework](../threads/m-assignment-framework.md) · [Calibration](../threads/m-calibration.md) · [MNL model development](m-progress-19-07-2026.md) · [Thesis summary](../threads/m-thesis-summary.md)

</div>
