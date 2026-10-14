---
source: report/analysis/m-raw-density-refit.md
date: 29-07-2026
kind: analysis
comments: true
generated: 2026-10-14T14:44:07
---

# Raw-density refit

<p class="doc-meta"><span class="chip chip-analysis">Analysis</span> <span class="chip chip-project">Master</span> <span class="chip chip-date">29-07-2026</span></p>

Sensei asked whether thinning the survey data ([Downsampling to MILES density](../notes/m-downsampling-to-miles-density.md)) changes the result. To check, the [Final model](m-final-model.md) was fitted again on the same 907 stays, using the **full** data (167,615 points instead of 17,010). The search distance, the score formulas, the 12-parameter form and the test sets stayed the same. α and `sigma_scale` were tuned again for the full data.

| | Downsampled | Raw density |
|---|---:|---:|
| Calibrated α | 2.4297 | 4.6159 |
| Candidate rows | 22,484 | 36,110 |
| Accuracy | 0.721 | 0.705 |
| **CV accuracy (grouped)** | **0.716 ± 0.076** | 0.697 ± 0.062 |
| Condition number | **1,373** | 2,865 |

**Thinning does no harm. The thinned model is even a little better**, in accuracy and in stability. All 12 weights keep the same sign (positive or negative). The f_distance weights are about 2.5 times larger with the full data. That follows from the larger α, because the distance score changes with α, so it does not mean the two models disagree.

More results from this test: [Raw-density alpha profile](m-raw-density-alpha-profile.md), [Downsampling shrinks the candidate search area](m-candidate-search-area.md). Part of [Complexity and transfer](../threads/m-complexity-and-transfer.md).


<div class="backlinks" markdown>

**Linked from** [Complexity and transfer](../threads/m-complexity-and-transfer.md) · [Does downsampling matter?](../progress/m-progress-29-07-2026.md) · [Downsampling shrinks the candidate search area](m-candidate-search-area.md) · [Downsampling to MILES density](../notes/m-downsampling-to-miles-density.md) · [Final model](m-final-model.md) · [Raw-density alpha profile](m-raw-density-alpha-profile.md)

</div>
