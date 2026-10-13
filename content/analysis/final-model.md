---
source: report/analysis/final-model.md
date: 21-07-2026
kind: analysis
comments: true
generated: 2026-10-13T16:57:34
---

# Final model

<p class="doc-meta"><span class="chip chip-analysis">Analysis</span> <span class="chip chip-date">21-07-2026</span></p>


$$V_t = w_{1,t} f_\text{distribution} + w_{2,t} f_\text{distance} + w_3 f_\text{directional} + w_{4,t}\,share_t + w_5\,\sigma + w_6\,(f_\text{distribution}\times share_\text{type})$$


12 parameters, α = 2.4297, `R_buffer` = 10 m. This is the final model of the thesis (Section 5.1.8).

| | |
|---|---:|
| LL(0) / LL(C) / LL(b) | -1.0799 / -0.9362 / -0.6557 |
| ρ² vs LL(0) / LL(C) | 0.393 / 0.300 |
| Accuracy (in-sample) | 0.721 |
| **CV accuracy (grouped, 5-fold)** | **0.716 ± 0.076** |
| CV building / street / open space | 0.896 / 0.429 / 0.491 |
| Condition number | 1,373 |

| Term | w | t | VIF |
|---|---:|---:|---:|
| f_distribution, bldg | +1.253 | 2.19 | 5.62 |
| f_distribution, street | +0.913 | 1.57 | 5.37 |
| f_distribution, os | +5.277 | 8.10 | 3.61 |
| f_distance, bldg | -2.102 | -2.04 | 9.37 |
| f_distance, street | -2.293 | -2.51 | 21.42 |
| f_distance, os | -6.554 | -6.14 | 13.05 |
| f_directional | +0.980 | 3.12 | 10.28 |
| share, bldg | -3.152 | -4.64 | 7.90 |
| share, street | -8.088 | -9.57 | 11.95 |
| share, os | -5.873 | -4.17 | 10.13 |
| sigma | +0.778 | 5.89 | 3.14 |
| f_distribution × share_type | +5.779 | 5.66 | 9.81 |

How it was reached: [Model progression](model-progression-table.md). Correlations: [Final model correlation matrix](final-model-correlation-matrix.md). How it fails: [Confusion matrix](confusion-matrix.md). Robust to downsampling: [Raw-density refit](raw-density-refit.md).

Part of [Chapter 5: Results](../progress/ch5-results.md).


<div class="backlinks" markdown>

**Linked from** [Candidate density bias toward building](candidate-density-bias.md) · [Chapter 5: Results](../progress/ch5-results.md) · [Confusion matrix](confusion-matrix.md) · [Contributions](../notes/contributions.md) · [Does downsampling matter?](../progress/progress-29-07-2026.md) · [Final model correlation matrix](final-model-correlation-matrix.md) · [Fold difficulty](fold-difficulty.md) · [ML ceiling check, row level](ml-ceiling-row-level.md) · [Model progression](model-progression-table.md) · [Positioning against deterministic assignment](../notes/positioning-vs-deterministic-assignment.md) · [RQ1 rebuilt with grouped CV](../progress/progress-21-07-2026.md) · [RQ2 diagnostics and RQ3 ceiling check](../progress/progress-23-07-2026.md) · [Raw-density refit](raw-density-refit.md) · [Sigma in tree importance](sigma-tree-importance.md) · [Thesis summary](../progress/thesis-summary.md) · [f_directional: shared vs split](f-directional-shared-vs-split.md) · [f_distribution](../notes/f-distribution.md) · [sigma](../notes/sigma.md)

</div>
