---
source: report/analysis/m-final-model-correlation-matrix.md
date: 21-07-2026
kind: analysis
comments: true
generated: 2026-11-06T11:37:20
---

# Final model correlation matrix

<p class="doc-meta"><span class="chip chip-analysis">Analysis</span> <span class="chip chip-project">Master</span> <span class="chip chip-date">21-07-2026</span></p>

How closely each pair of the [Final model](m-final-model.md)'s 11 inputs move together. A correlation near 1 or -1 means two inputs carry almost the same information. Near 0 means they are unrelated.

| | dist_b | dist_s | dist_o | dec_b | dec_s | dec_o | dir | shr_b | shr_s | shr_o | σ |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| f_distribution, bldg | 1 | -.17 | -.14 | .59 | -.32 | -.22 | -.24 | .50 | -.30 | -.21 | -.31 |
| f_distribution, street | -.17 | 1 | -.16 | -.30 | .54 | -.26 | .44 | -.27 | .43 | -.25 | .01 |
| f_distribution, os | -.14 | -.16 | 1 | -.24 | -.32 | .65 | -.27 | -.22 | -.30 | .61 | .01 |
| f_distance, bldg | .59 | -.30 | -.24 | 1 | -.57 | -.39 | -.48 | .89 | -.53 | -.37 | -.56 |
| f_distance, street | -.32 | .54 | -.32 | -.57 | 1 | -.51 | .82 | -.51 | .91 | -.48 | .34 |
| f_distance, os | -.22 | -.26 | .65 | -.39 | -.51 | 1 | -.43 | -.35 | -.48 | .93 | .24 |
| f_directional | -.24 | .44 | -.27 | -.48 | .82 | -.43 | 1 | -.43 | .77 | -.41 | .23 |
| share, bldg | .50 | -.27 | -.22 | .89 | -.51 | -.35 | -.43 | 1 | -.48 | -.33 | -.50 |
| share, street | -.30 | .43 | -.30 | -.53 | .91 | -.48 | .77 | -.48 | 1 | -.45 | .22 |
| share, os | -.21 | -.25 | .61 | -.37 | -.48 | .93 | -.41 | -.33 | -.45 | 1 | .17 |
| sigma | -.31 | .01 | .01 | -.56 | .34 | .24 | .23 | -.50 | .22 | .17 | 1 |

(dist = f_distribution, dec = f_distance, dir = f_directional, shr = share; _b/_s/_o = building/street/open space.)

The strongest pairs are always inputs of the same type: f_distance and share for open space (.93), street (.91) and building (.89). [Multicollinearity is structural](../concepts/m-multicollinearity-is-structural.md) explains why. f_directional has one shared weight, but it still moves with the street distance score and the street share (.82, .77). This fits the idea that the direction score matters most for streets.

Part of [Calibration](../threads/m-calibration.md).


<div class="backlinks" markdown>

**Linked from** [Calibration](../threads/m-calibration.md) · [Final model](m-final-model.md) · [Multicollinearity is structural](../concepts/m-multicollinearity-is-structural.md) · [RQ2 diagnostics and RQ3 ceiling check](../progress/m-progress-23-07-2026.md)

</div>
