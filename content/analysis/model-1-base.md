---
source: report/analysis/model-1-base.md
date: 21-07-2026
kind: analysis
comments: true
generated: 2026-10-13T16:57:34
---

# Model 1: base

<p class="doc-meta"><span class="chip chip-analysis">Analysis</span> <span class="chip chip-date">21-07-2026</span></p>


$$V_k = w_1 f_\text{distribution} + w_2 f_\text{distance} + w_3 f_\text{temporal} + w_4 f_\text{directional}$$


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

- **Worse than the type-share baseline** (negative ρ² vs LL(C)); no alpha value fixes this ([Alpha calibration](alpha-calibration.md)).
- Only [f_distribution](../notes/f-distribution.md) is significant at both radii. [f_temporal](../notes/f-temporal.md) is collinear with it (r ≈ 0.88) and gets dropped.
- [f_distance](../notes/f-distance.md) changes sign between radii (-0.47 at 10 m, +0.95 at 15 m), blocked on alpha calibration.
- Healthy conditioning: the problems are specification, not identification.

Next: [Model 2: share-type and sigma](model-2-share-type-sigma.md). Part of [Chapter 5: Results](../progress/ch5-results.md).


<div class="backlinks" markdown>

**Linked from** [Alpha calibration](alpha-calibration.md) · [Chapter 5: Results](../progress/ch5-results.md) · [MNL model development](../progress/progress-19-07-2026.md) · [Model 2: share-type and sigma](model-2-share-type-sigma.md) · [Model progression](model-progression-table.md) · [R_buffer: 10 m vs 15 m](r-buffer-10m-vs-15m.md) · [f_distance](../notes/f-distance.md) · [f_distribution](../notes/f-distribution.md) · [f_temporal](../notes/f-temporal.md)

</div>
