---
source: report/analysis/ml-baseline-stay-level.md
date: 20-07-2026
kind: analysis
comments: true
generated: 2026-10-13T16:57:34
---

# ML baseline, stay level (superseded)

<p class="doc-meta"><span class="chip chip-analysis">Analysis</span> <span class="chip chip-date">20-07-2026</span></p>

Sensei asked whether Random Forest or XGBoost would show the ceiling once nonlinearity is free. Both were fit as 3-class classifiers on the logit's 13 raw ingredients, one row per stay, no hand-built interactions, with **stay-level** CV.

| Model | CV accuracy | Building | Street | Open space |
|---|---:|---:|---:|---:|
| Logit (14 params) | 0.716 ± 0.035 | | | |
| RF | **0.754 ± 0.023** | 0.913 | 0.573 | 0.487 |
| RF, class-weighted | 0.753 ± 0.017 | 0.917 | 0.562 | 0.482 |
| XGBoost | 0.723 ± 0.015 | 0.855 | 0.557 | 0.518 |
| XGBoost, class-weighted | 0.725 ± 0.012 | 0.838 | 0.600 | 0.534 |

At the time this read as modest headroom (RF +3.8 pp). Every tree variant scored 1.000 in-sample: pure memorization.

**Superseded:** stay-level CV leaks sibling recordings ([Grouped cross-validation](../notes/grouped-cross-validation.md)). The corrected comparison reverses the ranking: [ML ceiling check, row level](ml-ceiling-row-level.md). The σ importance flag carried over: [Sigma in tree importance](sigma-tree-importance.md).

Part of [Chapter 5: Results](../progress/ch5-results.md).


<div class="backlinks" markdown>

**Linked from** [Chapter 5: Results](../progress/ch5-results.md) · [Grouped cross-validation](../notes/grouped-cross-validation.md) · [ML baseline](../progress/progress-20-07-2026.md) · [ML ceiling check, row level](ml-ceiling-row-level.md) · [Sigma in tree importance](sigma-tree-importance.md)

</div>
