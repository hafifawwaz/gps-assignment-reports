---
source: report/analysis/m-model-1-base.md
date: 21-07-2026
kind: analysis
comments: true
generated: 2026-10-14T14:44:07
---

# Model 1: base

<p class="doc-meta"><span class="chip chip-analysis">Analysis</span> <span class="chip chip-project">Master</span> <span class="chip chip-date">21-07-2026</span></p>

The first and simplest model: the four scores, each with one weight shared by all place types.


$$V_k = w_1 f_\text{distribution} + w_2 f_\text{distance} + w_3 f_\text{temporal} + w_4 f_\text{directional}$$


Tested with two search distances, 10 m and 15 m:

| | R=10 m | R=15 m |
|---|---:|---:|
| LL(C) / LL(b) | -0.9362 / -0.9745 | -0.9985 / -1.0360 |
| ρ² vs LL(C) | **-0.041** | **-0.038** |
| Accuracy | 0.518 | 0.509 |
| Building / street / open space | 0.576 / 0.378 / 0.492 | 0.589 / 0.346 / 0.445 |
| CV accuracy (grouped) | 0.514 ± 0.089 | 0.512 ± 0.098 |
| Condition number | 36 | 26 |

| Term (R=10 m) | w | t | VIF |
|---|---:|---:|---:|
| f_distribution | +3.331 | 5.34 | 7.14 |
| f_distance | -0.467 | -1.14 | 3.73 |
| f_temporal | +0.179 | 0.29 | 7.49 |
| f_directional | -0.080 | -0.41 | 2.78 |

- **Worse than a simple baseline.** ρ² is negative, so this model does worse than just knowing how common each type is. No value of α fixes this ([Alpha calibration](m-alpha-calibration.md)).
- Only [f_distribution](../notes/m-f-distribution.md) is significant at both distances. [f_temporal](../notes/m-f-temporal.md) moves almost the same way as f_distribution (r ≈ 0.88), so it was removed.
- [f_distance](../notes/m-f-distance.md) has a negative weight at 10 m (-0.47) and a positive one at 15 m (+0.95). This had to wait until α was tuned.
- The condition number is low, so the fit itself is stable. The problem is which inputs the model has, not the fitting.

Next: [Model 2: share-type and sigma](m-model-2-share-type-sigma.md). Part of [Calibration](../threads/m-calibration.md).


<div class="backlinks" markdown>

**Linked from** [Alpha calibration](m-alpha-calibration.md) · [Calibration](../threads/m-calibration.md) · [MNL model development](../progress/m-progress-19-07-2026.md) · [Model 2: share-type and sigma](m-model-2-share-type-sigma.md) · [Model progression](m-model-progression-table.md) · [R_buffer: 10 m vs 15 m](m-r-buffer-10m-vs-15m.md) · [f_distance](../notes/m-f-distance.md) · [f_distribution](../notes/m-f-distribution.md) · [f_temporal](../notes/m-f-temporal.md)

</div>
