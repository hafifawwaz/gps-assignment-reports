---
source: report/analysis/stepwise-vif-elimination.md
date: 21-07-2026
kind: analysis
comments: true
generated: 2026-10-13T16:57:34
---

# Stepwise VIF elimination

<p class="doc-meta"><span class="chip chip-analysis">Analysis</span> <span class="chip chip-date">21-07-2026</span></p>

Backward elimination on [Model 6, re-derived at calibrated alpha](model-6-rederived.md): drop the highest-VIF **non-core** term, refit, stop when every droppable term has VIF ≤ 10. The 13 Model 4a terms are protected ([Multicollinearity is structural](../notes/multicollinearity-is-structural.md)).

| Step | Worst droppable | VIF | Action |
|---:|---|---:|---|
| 0 | σ² | 18.38 | drop |
| 1 | f_distribution × share_type | 9.82 | stop |

Dropping σ² costs nothing (LR = 1.18, df = 1, **p = 0.278**) and cuts the condition number about 6× (14,851 → 2,430).

**Result, the 14-parameter model:** Model 4a + f_distribution × share_type. Accuracy 0.724, grouped CV **0.709 ± 0.075**, condition number 2,430. Same shape as reported on 19-07-2026, now re-derived from scratch.

It was then simplified to 12 parameters: [f_directional: shared vs split](f-directional-shared-vs-split.md). Part of [Chapter 5: Results](../progress/ch5-results.md).


<div class="backlinks" markdown>

**Linked from** [Chapter 5: Results](../progress/ch5-results.md) · [Model 6, re-derived at calibrated alpha](model-6-rederived.md) · [Model progression](model-progression-table.md) · [Multicollinearity is structural](../notes/multicollinearity-is-structural.md) · [RQ1 rebuilt with grouped CV](../progress/progress-21-07-2026.md) · [Sigma in tree importance](sigma-tree-importance.md)

</div>
