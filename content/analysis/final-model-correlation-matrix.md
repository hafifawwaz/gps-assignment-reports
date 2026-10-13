---
source: report/analysis/final-model-correlation-matrix.md
date: 21-07-2026
kind: analysis
comments: true
generated: 2026-10-13T20:05:33
---

# Final model correlation matrix

<p class="doc-meta"><span class="chip chip-analysis">Analysis</span> <span class="chip chip-date">21-07-2026</span></p>

Pairwise correlations of the [Final model](final-model.md)'s 12 features.

| | dist_b | dist_s | dist_o | dec_b | dec_s | dec_o | dir | shr_b | shr_s | shr_o | σ | dist×shr |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| f_distribution, bldg | 1 | -.16 | -.13 | .59 | -.32 | -.22 | -.20 | .50 | -.31 | -.21 | -.31 | .54 |
| f_distribution, street | -.16 | 1 | -.15 | -.29 | .53 | -.24 | .34 | -.26 | .41 | -.23 | -.01 | .45 |
| f_distribution, os | -.13 | -.15 | 1 | -.23 | -.30 | .64 | -.19 | -.21 | -.28 | .58 | -.01 | .24 |
| f_distance, bldg | .59 | -.29 | -.23 | 1 | -.57 | -.39 | -.45 | .87 | -.54 | -.37 | -.55 | .13 |
| f_distance, street | -.32 | .53 | -.30 | -.57 | 1 | -.49 | .71 | -.52 | .91 | -.46 | .35 | .00 |
| f_distance, os | -.22 | -.24 | .64 | -.39 | -.49 | 1 | -.34 | -.35 | -.46 | .92 | .24 | -.05 |
| f_directional | -.20 | .34 | -.19 | -.45 | .71 | -.34 | 1 | -.43 | .66 | -.30 | .27 | .01 |
| share, bldg | .50 | -.26 | -.21 | .87 | -.52 | -.35 | -.43 | 1 | -.49 | -.33 | -.50 | .20 |
| share, street | -.31 | .41 | -.28 | -.54 | .91 | -.46 | .66 | -.49 | 1 | -.44 | .27 | .00 |
| share, os | -.21 | -.23 | .58 | -.37 | -.46 | .92 | -.30 | -.33 | -.44 | 1 | .18 | -.01 |
| sigma | -.31 | -.01 | -.01 | -.55 | .35 | .24 | .27 | -.50 | .27 | .18 | 1 | -.24 |
| f_distribution × share_type | .54 | .45 | .24 | .13 | .00 | -.05 | .01 | .20 | .00 | -.01 | -.24 | 1 |

(dist = f_distribution, dec = f_distance, dir = f_directional, shr = share; _b/_s/_o = building/street/open space.)

The strongest pairs are all same-type: f_distance ↔ share for open space (.92), street (.91) and building (.87). See [Multicollinearity is structural](../notes/multicollinearity-is-structural.md). Even shared, f_directional tracks street distance and share (.71, .66), consistent with it being most meaningful for streets.

Part of [Calibration](../threads/calibration.md).


<div class="backlinks" markdown>

**Linked from** [Calibration](../threads/calibration.md) · [Final model](final-model.md) · [Multicollinearity is structural](../notes/multicollinearity-is-structural.md) · [RQ2 diagnostics and RQ3 ceiling check](../progress/progress-23-07-2026.md)

</div>
