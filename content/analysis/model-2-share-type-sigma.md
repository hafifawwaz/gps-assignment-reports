---
source: report/analysis/model-2-share-type-sigma.md
date: 21-07-2026
kind: analysis
comments: true
generated: 2026-10-13T20:41:00
---

# Model 2: share-type and sigma

<p class="doc-meta"><span class="chip chip-analysis">Analysis</span> <span class="chip chip-date">21-07-2026</span></p>

Drops [f_temporal](../notes/f-temporal.md), adds [share_type](../notes/share-type.md) per type and one [sigma](../notes/sigma.md) term:


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

- Now beats the type-share baseline; accuracy +15 pp over [Model 1: base](model-1-base.md).
- **The gain is a building story:** building jumps from ~0.58 to ~0.87, street is flat to worse, open space worse. `share_street`/`share_os` dominate and pull probability toward buildings, an early sign of [Candidate density bias toward building](candidate-density-bias.md).
- [sigma](../notes/sigma.md) is a clean positive effect; [f_directional](../notes/f-directional.md) becomes significant once `f_temporal` is gone.
- [f_distance](../notes/f-distance.md) now flips sign *significantly* between radii.

Next: [Directional scope ablation (3a vs 3b)](directional-scope-ablation.md). Part of [Calibration](../threads/calibration.md).


<div class="backlinks" markdown>

**Linked from** [Calibration](../threads/calibration.md) · [Directional scope ablation (3a vs 3b)](directional-scope-ablation.md) · [MNL model development](../progress/progress-19-07-2026.md) · [Model 1: base](model-1-base.md) · [Model progression](model-progression-table.md) · [f_distance](../notes/f-distance.md) · [share_type](../notes/share-type.md) · [sigma](../notes/sigma.md)

</div>
