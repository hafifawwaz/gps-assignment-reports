---
source: report/analysis/m-raw-density-refit.md
date: 29-07-2026
kind: analysis
comments: true
generated: 2026-11-06T11:37:20
---

# Raw-density refit

<p class="doc-meta"><span class="chip chip-analysis">Analysis</span> <span class="chip chip-project">Master</span> <span class="chip chip-date">29-07-2026</span></p>

Sensei asked whether downsampling the survey data ([Downsampling to MILES density](../concepts/m-downsampling-to-miles-density.md)) changes the result. To check, the [Final model](m-final-model.md) was fitted again on the same 907 stays, using the **full** data (152,602 points instead of 15,687). The search distance, the score formulas, the 11-parameter form and the test sets stayed the same. α and `sigma_scale` were tuned again for the full data.

| | Downsampled | Raw density |
|---|---:|---:|
| Calibrated α | 2.979 | 6.000 (search limit) |
| Candidate rows | 20,219 | 32,563 |
| Accuracy | 0.729 | 0.714 |
| **CV accuracy (grouped)** | **0.718 ± 0.028** | 0.709 ± 0.032 |
| Condition number | **1,869** | 4,735 |

**Downsampling does no harm.** The downsampled version is slightly more accurate on unseen data (0.718 against 0.709) and much more stable. All 11 weights keep the same sign (positive or negative). The f_distance weights are larger with the full data (street 2.3 times, open space 1.8 times; the building weight is small and not significant in the downsampled model). That follows from the larger α, because the distance score changes with α, so it does not mean the two models disagree.

More results from this test: [Raw-density alpha profile](m-raw-density-alpha-profile.md), [Downsampling shrinks the candidate search area](m-candidate-search-area.md). Part of [Complexity and transfer](../threads/m-complexity-and-transfer.md).


<div class="backlinks" markdown>

**Linked from** [Complexity and transfer](../threads/m-complexity-and-transfer.md) · [Does downsampling matter?](../progress/m-progress-29-07-2026.md) · [Downsampling shrinks the candidate search area](m-candidate-search-area.md) · [Downsampling to MILES density](../concepts/m-downsampling-to-miles-density.md) · [Final model](m-final-model.md) · [Raw-density alpha profile](m-raw-density-alpha-profile.md)

</div>
