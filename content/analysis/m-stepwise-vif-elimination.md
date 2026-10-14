---
source: report/analysis/m-stepwise-vif-elimination.md
date: 21-07-2026
kind: analysis
comments: true
generated: 2026-10-14T14:44:07
---

# Stepwise VIF elimination

<p class="doc-meta"><span class="chip chip-analysis">Analysis</span> <span class="chip chip-project">Master</span> <span class="chip chip-date">21-07-2026</span></p>

Removing weak terms one at a time from [Model 6, re-derived at calibrated alpha](m-model-6-rederived.md). At each step, find the extra term (not one of the core terms) with the highest VIF, remove it, and fit the model again. Stop when every extra term has a VIF of 10 or less. The 13 core terms from Model 4a are never removed ([Multicollinearity is structural](../notes/m-multicollinearity-is-structural.md)).

| Step | Worst droppable | VIF | Action |
|---:|---|---:|---|
| 0 | σ² | 18.38 | drop |
| 1 | f_distribution × share_type | 9.82 | stop |

Removing σ² costs nothing: the fit does not get significantly worse (LR = 1.18, df = 1, **p = 0.278**). The condition number drops about 6 times (14,851 → 2,430), so the model becomes much more stable.

**Result, the 14-parameter model:**


$$V_t = w_{1,t} f_\text{distribution} + w_{2,t} f_\text{distance} + w_{3,t} f_\text{directional} + w_{4,t}\,share_t + w_5\,\sigma + w_6\,(f_\text{distribution}\times share_\text{type})$$


This is Model 4a plus f_distribution × share_type. Accuracy 0.724, accuracy on unseen data **0.709 ± 0.075**, condition number 2,430. It has the same form as the model reported on 19-07-2026, now built again from the start.

Later it was made smaller, to 12 parameters: [f_directional: shared vs split](m-f-directional-shared-vs-split.md). Part of [Calibration](../threads/m-calibration.md).


<div class="backlinks" markdown>

**Linked from** [Calibration](../threads/m-calibration.md) · [Model 6, re-derived at calibrated alpha](m-model-6-rederived.md) · [Model progression](m-model-progression-table.md) · [Multicollinearity is structural](../notes/m-multicollinearity-is-structural.md) · [RQ1 rebuilt with grouped CV](../progress/m-progress-21-07-2026.md) · [Sigma in tree importance](m-sigma-tree-importance.md)

</div>
