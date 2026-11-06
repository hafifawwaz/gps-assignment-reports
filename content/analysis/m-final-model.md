---
source: report/analysis/m-final-model.md
date: 21-07-2026
kind: analysis
comments: true
generated: 2026-11-06T11:37:20
---

# Final model

<p class="doc-meta"><span class="chip chip-analysis">Analysis</span> <span class="chip chip-project">Master</span> <span class="chip chip-date">21-07-2026</span></p>

The model the thesis ends with (Section 5.1.8). It has 11 parameters, uses α = 2.979 and a search distance (`R_buffer`) of 10 m.


$$V_t = w_{1,t} f_\text{distribution} + w_{2,t} f_\text{distance} + w_3 f_\text{directional} + w_{4,t}\,share_t + w_5\,\sigma$$


A small $t$ means the weight is different for each place type (building, street, open space). No $t$ means one weight shared by all types.

**How well it fits.** The most important line is CV accuracy: on data it did not learn from, the model picks the correct type for 71.8% of stays.

| | |
|---|---:|
| LL(0) / LL(C) / LL(b) | -1.1318 / -0.9507 / -0.6477 |
| ρ² vs LL(0) / LL(C) | 0.428 / 0.319 |
| Accuracy (in-sample) | 0.729 |
| **CV accuracy (grouped, 5-fold)** | **0.718 ± 0.028** |
| CV building / street / open space | 0.893 / 0.491 / 0.450 |
| Condition number | 1,869 |

**The weights.** w is the learned weight: positive raises the probability, negative lowers it. t shows how clearly the weight differs from zero (about 2 or more is significant). VIF shows overlap with other inputs (above 10 is the usual warning line; see [Multicollinearity is structural](../concepts/m-multicollinearity-is-structural.md)).

| Term | w | t | VIF |
|---|---:|---:|---:|
| f_distribution, bldg | +1.960 | 4.06 | 1.75 |
| f_distribution, street | +2.659 | 5.36 | 1.97 |
| f_distribution, os | +6.410 | 11.01 | 2.11 |
| f_distance, bldg | -0.465 | -0.37 | 7.87 |
| f_distance, street | -3.350 | -2.92 | 23.79 |
| f_distance, os | -6.665 | -5.16 | 13.64 |
| f_directional | +3.488 | 6.82 | 10.35 |
| share, bldg | -1.182 | -2.38 | 6.32 |
| share, street | -5.156 | -7.27 | 11.33 |
| share, os | +0.246 | 0.23 | 9.93 |
| sigma | +1.045 | 7.63 | 3.36 |

How the model was built: [Model progression](m-model-progression-table.md). Overlap between inputs: [Final model correlation matrix](m-final-model-correlation-matrix.md). Where it makes mistakes: [Confusion matrix](m-confusion-matrix.md). It also holds up without downsampling the data: [Raw-density refit](m-raw-density-refit.md).

Part of [Calibration](../threads/m-calibration.md).


<div class="backlinks" markdown>

**Linked from** [CEUS paper](../plans/m-ceus-paper.md) · [CEUS paper revisions](../progress/d-progress-05-11-2026.md) · [CSIS DAYS 2026](../plans/csisdays-2026.md) · [CSIS DAYS 2026 poster](m-csis-poster.md) · [CSIS DAYS 2026 slides](m-csis-slide.md) · [Calibration](../threads/m-calibration.md) · [Candidate density bias toward building](m-candidate-density-bias.md) · [Confusion matrix](m-confusion-matrix.md) · [Contributions](../concepts/m-contributions.md) · [Does downsampling matter?](../progress/m-progress-29-07-2026.md) · [Final model correlation matrix](m-final-model-correlation-matrix.md) · [Fold difficulty](m-fold-difficulty.md) · [ML ceiling check, row level](m-ml-ceiling-row-level.md) · [Model progression](m-model-progression-table.md) · [Positioning against deterministic assignment](../concepts/m-positioning-vs-deterministic-assignment.md) · [Publications and doctoral plan](../progress/d-progress-20-10-2026.md) · [RQ1 rebuilt with grouped CV](../progress/m-progress-21-07-2026.md) · [RQ2 diagnostics and RQ3 ceiling check](../progress/m-progress-23-07-2026.md) · [Raw-density refit](m-raw-density-refit.md) · [Seasonal variance](../plans/d-seasonal-variance.md) · [Sigma in tree importance](m-sigma-tree-importance.md) · [Thesis summary](../threads/m-thesis-summary.md) · [f_directional: shared vs split](m-f-directional-shared-vs-split.md) · [f_distribution](../concepts/m-f-distribution.md) · [share_type](../concepts/m-share-type.md) · [sigma](../concepts/m-sigma.md)

</div>
