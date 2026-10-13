---
source: report/analysis/raw-density-refit.md
date: 29-07-2026
kind: analysis
comments: true
generated: 2026-10-13T20:05:33
---

# Raw-density refit

<p class="doc-meta"><span class="chip chip-analysis">Analysis</span> <span class="chip chip-date">29-07-2026</span></p>

Sensei asked whether [Downsampling to MILES density](../notes/downsampling-to-miles-density.md) changes calibration. The [Final model](final-model.md) specification was refit on the same 907 stays scored from the **raw** points (167,615 instead of 17,010); `R_buffer`, formulas, 12-parameter spec and CV folds held fixed, α and `sigma_scale` recalibrated on the raw data.

| | Downsampled | Raw density |
|---|---:|---:|
| Calibrated α | 2.4297 | 4.6159 |
| Candidate rows | 22,484 | 36,110 |
| Accuracy | 0.721 | 0.705 |
| **CV accuracy (grouped)** | **0.716 ± 0.076** | 0.697 ± 0.062 |
| Condition number | **1,373** | 2,865 |

**Downsampling does not hurt; the downsampled model is slightly better** on accuracy and conditioning. All 12 coefficients keep their sign. `f_distance` weights are about 2.5× larger on raw data, which tracks the doubled α (the feature is a power transform of α), not a real disagreement.

Side findings: [Raw-density alpha profile](raw-density-alpha-profile.md), [Downsampling shrinks the candidate search area](candidate-search-area.md). Part of [Complexity and transfer](../threads/complexity-and-transfer.md).


<div class="backlinks" markdown>

**Linked from** [Complexity and transfer](../threads/complexity-and-transfer.md) · [Does downsampling matter?](../progress/progress-29-07-2026.md) · [Downsampling shrinks the candidate search area](candidate-search-area.md) · [Downsampling to MILES density](../notes/downsampling-to-miles-density.md) · [Final model](final-model.md) · [Raw-density alpha profile](raw-density-alpha-profile.md)

</div>
