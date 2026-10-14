---
source: report/analysis/m-alpha-calibration.md
date: 21-07-2026
kind: analysis
comments: true
generated: 2026-10-14T14:44:07
---

# Alpha calibration

<p class="doc-meta"><span class="chip chip-analysis">Analysis</span> <span class="chip chip-project">Master</span> <span class="chip chip-date">21-07-2026</span></p>

How the setting α was chosen. α controls how fast the [f_distance](../notes/m-f-distance.md) score falls as a candidate gets farther from the stay.

The method is called profile likelihood, and it uses Model 4a. Take one value of α, fit all the other weights again, and record how well the model fits (LL(b), closer to 0 is better). Repeat for many values of α and keep the best one. Because $f_\text{distance}(\alpha) = f_\text{distance}(1)^{1/\alpha^2}$, the scores do not need to be computed again for each α.

| α | LL(b) | Accuracy |
|---:|---:|---:|
| 1.0 | -0.6881 | 0.717 |
| 2.0 | -0.6708 | 0.726 |
| **2.4** | **-0.6701** | 0.723 |
| 3.0 | -0.6707 | 0.720 |
| 4.0 | -0.6725 | 0.720 |

The fit has one clear best point. The optimizer finds **α\* = 2.4297**. Computing the scores again from scratch at this value gives the same result as the shortcut, to within 2e-16.

- Model 2 has its own best α (2.106). Using that value in Model 4a costs almost nothing, and the reverse is also true. So the two models agree on how fast the score should fall.
- **Tune α once on Model 4a, then build the later models with that value.** Tuning α again inside the larger Models 5 and 6 improved the fit only a little, lowered accuracy, and about doubled the VIF warning values.
- Model 1 has no single best α, and no value of α fixes its main problem ([Model 1: base](m-model-1-base.md)).

The main result of this step: [The f_distance² artifact](m-f-distance-squared-artifact.md). With the full, unthinned data, the best α moves: [Raw-density alpha profile](m-raw-density-alpha-profile.md). Part of [Calibration](../threads/m-calibration.md).


<div class="backlinks" markdown>

**Linked from** [Calibration](../threads/m-calibration.md) · [MNL model development](../progress/m-progress-19-07-2026.md) · [Model 1: base](m-model-1-base.md) · [Model 4a: alternative-specific parameters](m-model-4a-alternative-specific.md) · [RQ1 rebuilt with grouped CV](../progress/m-progress-21-07-2026.md) · [Raw-density alpha profile](m-raw-density-alpha-profile.md) · [The f_distance² artifact](m-f-distance-squared-artifact.md) · [f_distance](../notes/m-f-distance.md)

</div>
