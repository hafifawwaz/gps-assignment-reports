---
source: report/analysis/m-final-model-correlation-matrix.md
date: 21-07-2026
kind: analysis
comments: true
generated: 2026-10-26T20:41:14
---

# Final model correlation matrix

<p class="doc-meta"><span class="chip chip-analysis">Analysis</span> <span class="chip chip-project">Master</span> <span class="chip chip-date">21-07-2026</span></p>

How closely each pair of the [Final model](m-final-model.md)'s 11 inputs move together. A correlation near 1 or -1 means two inputs carry almost the same information. Near 0 means they are unrelated.

| | dist_b | dist_s | dist_o | dec_b | dec_s | dec_o | dir | shr_b | shr_s | shr_o | σ |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| f_distribution, bldg | 1 | -.17 | -.14 | .59 | -.33 | -.23 | -.25 | .50 | -.31 | -.21 | -.32 |
| f_distribution, street | -.17 | 1 | -.16 | -.31 | .55 | -.25 | .44 | -.28 | .44 | -.24 | .03 |
| f_distribution, os | -.14 | -.16 | 1 | -.25 | -.30 | .65 | -.26 | -.23 | -.28 | .61 | .02 |
| f_distance, bldg | .59 | -.31 | -.25 | 1 | -.58 | -.40 | -.48 | .88 | -.55 | -.38 | -.57 |
| f_distance, street | -.33 | .55 | -.30 | -.58 | 1 | -.47 | .82 | -.53 | .91 | -.45 | .36 |
| f_distance, os | -.23 | -.25 | .65 | -.40 | -.47 | 1 | -.41 | -.36 | -.45 | .92 | .26 |
| f_directional | -.25 | .44 | -.26 | -.48 | .82 | -.41 | 1 | -.43 | .77 | -.39 | .24 |
| share, bldg | .50 | -.28 | -.23 | .88 | -.53 | -.36 | -.43 | 1 | -.49 | -.34 | -.52 |
| share, street | -.31 | .44 | -.28 | -.55 | .91 | -.45 | .77 | -.49 | 1 | -.42 | .24 |
| share, os | -.21 | -.24 | .61 | -.38 | -.45 | .92 | -.39 | -.34 | -.42 | 1 | .19 |
| sigma | -.32 | .03 | .02 | -.57 | .36 | .26 | .24 | -.52 | .24 | .19 | 1 |

(dist = f_distribution, dec = f_distance, dir = f_directional, shr = share; _b/_s/_o = building/street/open space.)

The strongest pairs are always inputs of the same type: f_distance and share for open space (.92), street (.91) and building (.88). [Multicollinearity is structural](../concepts/m-multicollinearity-is-structural.md) explains why. f_directional has one shared weight, but it still moves with the street distance score and the street share (.82, .77). This fits the idea that the direction score matters most for streets.

Part of [Calibration](../threads/m-calibration.md).


<div class="backlinks" markdown>

**Linked from** [Calibration](../threads/m-calibration.md) · [Final model](m-final-model.md) · [Multicollinearity is structural](../concepts/m-multicollinearity-is-structural.md) · [RQ2 diagnostics and RQ3 ceiling check](../progress/m-progress-23-07-2026.md)

</div>
