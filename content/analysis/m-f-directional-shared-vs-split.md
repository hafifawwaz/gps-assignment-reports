---
source: report/analysis/m-f-directional-shared-vs-split.md
date: 21-07-2026
kind: analysis
comments: true
generated: 2026-10-14T14:44:07
---

# f_directional: shared vs split

<p class="doc-meta"><span class="chip chip-analysis">Analysis</span> <span class="chip chip-project">Master</span> <span class="chip chip-date">21-07-2026</span></p>

Does [f_directional](../notes/m-f-directional.md) need a separate weight for each place type ("split", the 14-parameter model, $w_{3,t} f_\text{directional}$)? Or is one weight for all types enough ("shared", 12 parameters, $w_3 f_\text{directional}$)? Everything else stayed the same.

| | Shared (12) | Split (14) | Street only (12) |
|---|---:|---:|---:|
| Accuracy | 0.721 | 0.724 | 0.723 |
| CV accuracy (grouped) | **0.716 ± 0.076** | 0.709 ± 0.075 | **0.716 ± 0.069** |
| Condition number | **1,373** | 2,430 | 1,431 |

**Split vs shared: LR = 5.41, df = 2, p = 0.067.** This is not significant: the two extra weights do not improve the fit enough. They raise training accuracy by 0.3 percentage points, but *lower* accuracy on unseen data and double the condition number. That is overfitting ([Overfitting signature](../notes/m-overfitting-signature.md)).

The shared weight is clearly significant (t = +3.12). In the split version, only the building weight passes 1.96. "Street only" performs about the same as shared at this size, and never better. In the 7-parameter models, shared wins on every measure (CV 0.666 against 0.656), the same result as in [Directional scope ablation (3a vs 3b)](m-directional-scope-ablation.md).

**Decision: shared, 12 parameters** → [Final model](m-final-model.md), the final model of the thesis (Section 5.1.8). Part of [Calibration](../threads/m-calibration.md).


<div class="backlinks" markdown>

**Linked from** [Calibration](../threads/m-calibration.md) · [Directional scope ablation (3a vs 3b)](m-directional-scope-ablation.md) · [Overfitting signature](../notes/m-overfitting-signature.md) · [RQ1 rebuilt with grouped CV](../progress/m-progress-21-07-2026.md) · [Stepwise VIF elimination](m-stepwise-vif-elimination.md) · [f_directional](../notes/m-f-directional.md)

</div>
