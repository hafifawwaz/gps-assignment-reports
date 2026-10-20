---
source: report/analysis/m-final-model.md
date: 21-07-2026
kind: analysis
comments: true
generated: 2026-10-20T15:44:29
---

# Final model

<p class="doc-meta"><span class="chip chip-analysis">Analysis</span> <span class="chip chip-project">Master</span> <span class="chip chip-date">21-07-2026</span></p>

The model the thesis ends with (Section 5.1.8). It has 11 parameters, uses α = 2.764 and a search distance (`R_buffer`) of 10 m.


$$V_t = w_{1,t} f_\text{distribution} + w_{2,t} f_\text{distance} + w_3 f_\text{directional} + w_{4,t}\,share_t + w_5\,\sigma$$


A small $t$ means the weight is different for each place type (building, street, open space). No $t$ means one weight shared by all types.

**How well it fits.** The most important line is CV accuracy: on data it did not learn from, the model picks the correct type for 71.9% of stays.

| | |
|---|---:|
| LL(0) / LL(C) / LL(b) | -1.0712 / -0.9359 / -0.6509 |
| ρ² vs LL(0) / LL(C) | 0.392 / 0.305 |
| Accuracy (in-sample) | 0.731 |
| **CV accuracy (grouped, 5-fold)** | **0.719 ± 0.032** |
| CV building / street / open space | 0.900 / 0.486 / 0.439 |
| Condition number | 1,681 |

**The weights.** w is the learned weight: positive raises the probability, negative lowers it. t shows how clearly the weight differs from zero (about 2 or more is significant). VIF shows overlap with other inputs (above 10 is the usual warning line; see [Multicollinearity is structural](../notes/m-multicollinearity-is-structural.md)).

| Term | w | t | VIF |
|---|---:|---:|---:|
| f_distribution, bldg | +2.066 | 4.12 | 1.78 |
| f_distribution, street | +2.648 | 5.32 | 1.98 |
| f_distribution, os | +6.520 | 10.93 | 2.13 |
| f_distance, bldg | -0.384 | -0.32 | 7.83 |
| f_distance, street | -3.042 | -2.86 | 22.36 |
| f_distance, os | -6.065 | -4.98 | 12.80 |
| f_directional | +3.429 | 6.68 | 10.03 |
| share, bldg | -1.014 | -1.98 | 6.35 |
| share, street | -5.163 | -7.05 | 10.77 |
| share, os | -0.798 | -0.72 | 9.10 |
| sigma | +1.016 | 7.36 | 3.34 |

How the model was built: [Model progression](m-model-progression-table.md). Overlap between inputs: [Final model correlation matrix](m-final-model-correlation-matrix.md). Where it makes mistakes: [Confusion matrix](m-confusion-matrix.md). It also holds up without downsampling the data: [Raw-density refit](m-raw-density-refit.md).

Part of [Calibration](../threads/m-calibration.md).


<div class="backlinks" markdown>

**Linked from** [Calibration](../threads/m-calibration.md) · [Candidate density bias toward building](m-candidate-density-bias.md) · [Confusion matrix](m-confusion-matrix.md) · [Contributions](../notes/m-contributions.md) · [Does downsampling matter?](../progress/m-progress-29-07-2026.md) · [Final model correlation matrix](m-final-model-correlation-matrix.md) · [Fold difficulty](m-fold-difficulty.md) · [ML ceiling check, row level](m-ml-ceiling-row-level.md) · [Model progression](m-model-progression-table.md) · [Positioning against deterministic assignment](../notes/m-positioning-vs-deterministic-assignment.md) · [Publications and doctoral plan](../progress/d-progress-20-10-2026.md) · [RQ1 rebuilt with grouped CV](../progress/m-progress-21-07-2026.md) · [RQ2 diagnostics and RQ3 ceiling check](../progress/m-progress-23-07-2026.md) · [Raw-density refit](m-raw-density-refit.md) · [Sigma in tree importance](m-sigma-tree-importance.md) · [Thesis bug fixes and adopted rerun](../inbox/thesis-bug-fix.md) · [Thesis summary](../threads/m-thesis-summary.md) · [f_directional: shared vs split](m-f-directional-shared-vs-split.md) · [f_distribution](../notes/m-f-distribution.md) · [share_type](../notes/m-share-type.md) · [sigma](../notes/m-sigma.md)

</div>
