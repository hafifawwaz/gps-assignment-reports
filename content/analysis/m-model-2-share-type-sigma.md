---
source: report/analysis/m-model-2-share-type-sigma.md
date: 21-07-2026
kind: analysis
comments: true
generated: 2026-10-14T14:44:07
---

# Model 2: share-type and sigma

<p class="doc-meta"><span class="chip chip-analysis">Analysis</span> <span class="chip chip-project">Master</span> <span class="chip chip-date">21-07-2026</span></p>

The second model removes [f_temporal](../notes/m-f-temporal.md). It adds [share_type](../notes/m-share-type.md), with a separate weight for each type, and one [sigma](../notes/m-sigma.md) term:


$$V_k = w_1 f_\text{distribution} + w_2 f_\text{distance} + w_3 f_\text{directional} + w_4\,share_\text{bldg} + w_5\,share_\text{street} + w_6\,share_\text{os} + w_7\,\sigma$$


| | R=10 m | R=15 m |
|---|---:|---:|
| ρ² vs LL(C) | **0.198** | 0.199 |
| Accuracy | **0.668** | 0.654 |
| Building / street / open space | 0.872 / 0.362 / 0.398 | 0.881 / 0.308 / 0.356 |
| CV accuracy (grouped) | 0.664 ± 0.046 | 0.647 ± 0.042 |
| Condition number | 117 | 98 |

| Term (R=10 m) | w | t |
|---|---:|---:|
| f_distribution | +3.542 | 8.40 |
| f_distance | -1.209 | -2.60 |
| f_directional | +1.708 | 5.89 |
| share_bldg | +0.219 | 0.76 |
| share_street | **-5.552** | -15.68 |
| share_os | **-5.887** | -12.79 |
| sigma | +0.475 | 5.87 |

- The model now beats the simple baseline, and accuracy is 15 percentage points higher than [Model 1: base](m-model-1-base.md).
- **Almost all of the gain is for buildings.** Building accuracy jumps from about 0.58 to about 0.87. Street stays the same or gets worse, and open space gets worse. The large negative weights `share_street` and `share_os` push the probability toward buildings. This is an early sign of [Candidate density bias toward building](m-candidate-density-bias.md).
- [sigma](../notes/m-sigma.md) has a clear positive effect. [f_directional](../notes/m-f-directional.md) becomes significant once `f_temporal` is removed.
- The weight of [f_distance](../notes/m-f-distance.md) now changes sign between 10 m and 15 m, and both values are significant.

Next: [Directional scope ablation (3a vs 3b)](m-directional-scope-ablation.md). Part of [Calibration](../threads/m-calibration.md).


<div class="backlinks" markdown>

**Linked from** [Calibration](../threads/m-calibration.md) · [Directional scope ablation (3a vs 3b)](m-directional-scope-ablation.md) · [MNL model development](../progress/m-progress-19-07-2026.md) · [Model 1: base](m-model-1-base.md) · [Model progression](m-model-progression-table.md) · [f_distance](../notes/m-f-distance.md) · [share_type](../notes/m-share-type.md) · [sigma](../notes/m-sigma.md)

</div>
