---
source: report/analysis/m-final-model.md
date: 21-07-2026
kind: analysis
comments: true
generated: 2026-10-14T14:44:07
---

# Final model

<p class="doc-meta"><span class="chip chip-analysis">Analysis</span> <span class="chip chip-project">Master</span> <span class="chip chip-date">21-07-2026</span></p>

The model the thesis ends with (Section 5.1.8). It has 12 parameters, uses α = 2.4297 and a search distance (`R_buffer`) of 10 m.


$$V_t = w_{1,t} f_\text{distribution} + w_{2,t} f_\text{distance} + w_3 f_\text{directional} + w_{4,t}\,share_t + w_5\,\sigma + w_6\,(f_\text{distribution}\times share_\text{type})$$


A small $t$ means the weight is different for each place type (building, street, open space). No $t$ means one weight shared by all types.

**How well it fits.** The most important line is CV accuracy: on data it did not learn from, the model picks the correct type for 71.6% of stays.

| | |
|---|---:|
| LL(0) / LL(C) / LL(b) | -1.0799 / -0.9362 / -0.6557 |
| ρ² vs LL(0) / LL(C) | 0.393 / 0.300 |
| Accuracy (in-sample) | 0.721 |
| **CV accuracy (grouped, 5-fold)** | **0.716 ± 0.076** |
| CV building / street / open space | 0.896 / 0.429 / 0.491 |
| Condition number | 1,373 |

**The weights.** w is the learned weight: positive raises the probability, negative lowers it. t shows how clearly the weight differs from zero (about 2 or more is significant). VIF shows overlap with other inputs (above 10 is the usual warning line; see [Multicollinearity is structural](../notes/m-multicollinearity-is-structural.md)).

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

How the model was built: [Model progression](m-model-progression-table.md). Overlap between inputs: [Final model correlation matrix](m-final-model-correlation-matrix.md). Where it makes mistakes: [Confusion matrix](m-confusion-matrix.md). It also holds up without thinning the data: [Raw-density refit](m-raw-density-refit.md).

Part of [Calibration](../threads/m-calibration.md).


<div class="backlinks" markdown>

**Linked from** [Calibration](../threads/m-calibration.md) · [Candidate density bias toward building](m-candidate-density-bias.md) · [Confusion matrix](m-confusion-matrix.md) · [Contributions](../notes/m-contributions.md) · [Does downsampling matter?](../progress/m-progress-29-07-2026.md) · [Final model correlation matrix](m-final-model-correlation-matrix.md) · [Fold difficulty](m-fold-difficulty.md) · [ML ceiling check, row level](m-ml-ceiling-row-level.md) · [Model progression](m-model-progression-table.md) · [Positioning against deterministic assignment](../notes/m-positioning-vs-deterministic-assignment.md) · [RQ1 rebuilt with grouped CV](../progress/m-progress-21-07-2026.md) · [RQ2 diagnostics and RQ3 ceiling check](../progress/m-progress-23-07-2026.md) · [Raw-density refit](m-raw-density-refit.md) · [Sigma in tree importance](m-sigma-tree-importance.md) · [Thesis summary](../threads/m-thesis-summary.md) · [f_directional: shared vs split](m-f-directional-shared-vs-split.md) · [f_distribution](../notes/m-f-distribution.md) · [sigma](../notes/m-sigma.md)

</div>
