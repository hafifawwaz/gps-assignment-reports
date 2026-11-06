---
source: report/analysis/m-model-1-base.md
date: 21-07-2026
kind: analysis
comments: true
generated: 2026-11-06T11:37:20
---

# Model 1: base

<p class="doc-meta"><span class="chip chip-analysis">Analysis</span> <span class="chip chip-project">Master</span> <span class="chip chip-date">21-07-2026</span></p>

The first and simplest model: the four scores, each with one weight shared by all place types.


$$V_k = w_1 f_\text{distribution} + w_2 f_\text{distance} + w_3 f_\text{temporal} + w_4 f_\text{directional}$$


Tested with two search distances, 10 m and 15 m:

| | R=10 m | R=15 m |
|---|---:|---:|
| LL(C) / LL(b) | -0.9507 / -0.9998 | -1.0212 / -1.0590 |
| ρ² vs LL(C) | **-0.052** | **-0.037** |
| Accuracy | 0.519 | 0.512 |
| Building / street / open space | 0.573 / 0.103 / 0.775 | 0.578 / 0.049 / 0.775 |
| CV accuracy (grouped) | 0.522 ± 0.055 | 0.505 ± 0.065 |
| Condition number | 86 | 78 |

| Term (R=10 m) | w | t | VIF |
|---|---:|---:|---:|
| f_distribution | +4.261 | 4.88 | 21.65 |
| f_distance | -0.518 | -1.31 | 3.19 |
| f_temporal | -1.281 | -1.53 | 21.43 |
| f_directional | -1.391 | -4.91 | 2.21 |

- **Worse than a simple baseline.** ρ² is negative, so this model does worse than just knowing how common each type is. No value of α fixes this: for every α from 0.2 to 6, LL(b) stays between -1.001 and -0.996, below LL(C) ([Alpha calibration](m-alpha-calibration.md)).
- [f_distribution](../concepts/m-f-distribution.md) is significant at both distances. [f_temporal](../concepts/m-f-temporal.md) is not, and it moves almost the same way as f_distribution (r ≈ 0.96), so it was removed.
- [f_directional](../concepts/m-f-directional.md) is significant at both distances, but with a negative weight. It turns positive once share_type and σ are added ([Model 2: share-type and sigma](m-model-2-share-type-sigma.md)).
- [f_distance](../concepts/m-f-distance.md) has a negative weight at 10 m (-0.52) and a positive one at 15 m (+0.72). This had to wait until α was tuned.
- The condition number is low, so the fit itself is stable. The problem is which inputs the model has, not the fitting.

Next: [Model 2: share-type and sigma](m-model-2-share-type-sigma.md). Part of [Calibration](../threads/m-calibration.md).


<div class="backlinks" markdown>

**Linked from** [Alpha calibration](m-alpha-calibration.md) · [Calibration](../threads/m-calibration.md) · [MNL model development](../progress/m-progress-19-07-2026.md) · [Model 2: share-type and sigma](m-model-2-share-type-sigma.md) · [Model progression](m-model-progression-table.md) · [R_buffer: 10 m vs 15 m](m-r-buffer-10m-vs-15m.md) · [f_distance](../concepts/m-f-distance.md) · [f_distribution](../concepts/m-f-distribution.md) · [f_temporal](../concepts/m-f-temporal.md)

</div>
