---
source: report/analysis/m-model-2-share-type-sigma.md
date: 21-07-2026
kind: analysis
comments: true
generated: 2026-11-06T11:37:20
---

# Model 2: share-type and sigma

<p class="doc-meta"><span class="chip chip-analysis">Analysis</span> <span class="chip chip-project">Master</span> <span class="chip chip-date">21-07-2026</span></p>

The second model removes [f_temporal](../concepts/m-f-temporal.md). It adds [share_type](../concepts/m-share-type.md), with a separate weight for each type, and one [sigma](../concepts/m-sigma.md) term:


$$V_k = w_1 f_\text{distribution} + w_2 f_\text{distance} + w_3 f_\text{directional} + w_4\,share_\text{bldg} + w_5\,share_\text{street} + w_6\,share_\text{os} + w_7\,\sigma$$


| | R=10 m | R=15 m |
|---|---:|---:|
| ρ² vs LL(C) | 0.216 | **0.219** |
| Accuracy | **0.663** | 0.639 |
| Building / street / open space | 0.838 / 0.438 / 0.393 | 0.838 / 0.405 / 0.314 |
| CV accuracy (grouped) | 0.655 ± 0.029 | 0.642 ± 0.031 |
| Condition number | 114 | 106 |

| Term (R=10 m) | w | t |
|---|---:|---:|
| f_distribution | +3.546 | 8.83 |
| f_distance | -1.072 | -2.36 |
| f_directional | +3.296 | 8.42 |
| share_bldg | +0.936 | 2.79 |
| share_street | **-7.292** | -16.35 |
| share_os | **-5.408** | -11.59 |
| sigma | +0.481 | 5.92 |

- The model now beats the simple baseline, and accuracy is 14 percentage points higher than [Model 1: base](m-model-1-base.md).
- **The gain is for buildings and streets.** Building accuracy rises from 0.57 to 0.84 and street from 0.10 to 0.44, but open space falls from 0.77 to 0.39. The large negative weights `share_street` and `share_os` push the probability toward buildings. This is an early sign of [Candidate density bias toward building](m-candidate-density-bias.md).
- [sigma](../concepts/m-sigma.md) has a clear positive effect. [f_directional](../concepts/m-f-directional.md) turns positive and strongly significant once `f_temporal` is removed.
- The weight of [f_distance](../concepts/m-f-distance.md) now changes sign between 10 m and 15 m (-1.07 and +1.06), and both values are significant.

Next: [Directional scope ablation (3a vs 3b)](m-directional-scope-ablation.md). Part of [Calibration](../threads/m-calibration.md).


<div class="backlinks" markdown>

**Linked from** [Calibration](../threads/m-calibration.md) · [Directional scope ablation (3a vs 3b)](m-directional-scope-ablation.md) · [MNL model development](../progress/m-progress-19-07-2026.md) · [Model 1: base](m-model-1-base.md) · [Model progression](m-model-progression-table.md) · [R_buffer: 10 m vs 15 m](m-r-buffer-10m-vs-15m.md) · [f_distance](../concepts/m-f-distance.md) · [share_type](../concepts/m-share-type.md) · [sigma](../concepts/m-sigma.md)

</div>
