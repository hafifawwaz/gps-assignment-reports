---
source: report/analysis/m-model-1-base.md
date: 21-07-2026
kind: analysis
comments: true
generated: 2026-10-26T20:41:14
---

# Model 1: base

<p class="doc-meta"><span class="chip chip-analysis">Analysis</span> <span class="chip chip-project">Master</span> <span class="chip chip-date">21-07-2026</span></p>

The first and simplest model: the four scores, each with one weight shared by all place types.


$$V_k = w_1 f_\text{distribution} + w_2 f_\text{distance} + w_3 f_\text{temporal} + w_4 f_\text{directional}$$


Tested with two search distances, 10 m and 15 m:

| | R=10 m | R=15 m |
|---|---:|---:|
| LL(C) / LL(b) | -0.9359 / -0.9513 | -0.9992 / -1.0078 |
| ρ² vs LL(C) | **-0.016** | **-0.009** |
| Accuracy | 0.540 | 0.538 |
| Building / street / open space | 0.631 / 0.130 / 0.686 | 0.638 / 0.076 / 0.707 |
| CV accuracy (grouped) | 0.539 ± 0.051 | 0.533 ± 0.033 |
| Condition number | 84 | 76 |

| Term (R=10 m) | w | t | VIF |
|---|---:|---:|---:|
| f_distribution | +4.258 | 4.90 | 21.92 |
| f_distance | -0.491 | -1.24 | 3.22 |
| f_temporal | -1.303 | -1.56 | 21.72 |
| f_directional | -1.176 | -4.29 | 2.20 |

- **Worse than a simple baseline.** ρ² is negative, so this model does worse than just knowing how common each type is. No value of α fixes this: for every α from 0.2 to 6, LL(b) stays between -0.952 and -0.948, below LL(C) ([Alpha calibration](m-alpha-calibration.md)).
- [f_distribution](../concepts/m-f-distribution.md) is significant at both distances. [f_temporal](../concepts/m-f-temporal.md) is not, and it moves almost the same way as f_distribution (r ≈ 0.96), so it was removed.
- [f_directional](../concepts/m-f-directional.md) is significant at both distances, but with a negative weight. It turns positive once share_type and σ are added ([Model 2: share-type and sigma](m-model-2-share-type-sigma.md)).
- [f_distance](../concepts/m-f-distance.md) has a negative weight at 10 m (-0.49) and a positive one at 15 m (+0.73). This had to wait until α was tuned.
- The condition number is low, so the fit itself is stable. The problem is which inputs the model has, not the fitting.

Next: [Model 2: share-type and sigma](m-model-2-share-type-sigma.md). Part of [Calibration](../threads/m-calibration.md).


<div class="backlinks" markdown>

**Linked from** [Alpha calibration](m-alpha-calibration.md) · [Calibration](../threads/m-calibration.md) · [MNL model development](../progress/m-progress-19-07-2026.md) · [Model 2: share-type and sigma](m-model-2-share-type-sigma.md) · [Model progression](m-model-progression-table.md) · [R_buffer: 10 m vs 15 m](m-r-buffer-10m-vs-15m.md) · [f_distance](../concepts/m-f-distance.md) · [f_distribution](../concepts/m-f-distribution.md) · [f_temporal](../concepts/m-f-temporal.md)

</div>
