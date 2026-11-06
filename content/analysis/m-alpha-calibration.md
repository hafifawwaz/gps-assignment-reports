---
source: report/analysis/m-alpha-calibration.md
date: 21-07-2026
kind: analysis
comments: true
generated: 2026-11-06T11:37:20
---

# Alpha calibration

<p class="doc-meta"><span class="chip chip-analysis">Analysis</span> <span class="chip chip-project">Master</span> <span class="chip chip-date">21-07-2026</span></p>

How the setting α was chosen. α controls how fast the [f_distance](../concepts/m-f-distance.md) score falls as a candidate gets farther from the stay.

The method is called profile likelihood, and it uses Model 4a. Take one value of α, fit all the other weights again, and record how well the model fits (LL(b), closer to 0 is better). Repeat for many values of α and keep the best one. Because $f_\text{distance}(\alpha) = f_\text{distance}(1)^{1/\alpha^2}$, the scores do not need to be computed again for each α.

| α | LL(b) | Accuracy |
|---:|---:|---:|
| 1.0 | -0.6731 | 0.714 |
| 2.0 | -0.6494 | 0.722 |
| 2.4 | -0.6463 | 0.721 |
| **2.979** | **-0.6453** | 0.727 |
| 3.0 | -0.6453 | 0.725 |
| 4.0 | -0.6461 | 0.724 |
| 5.0 | -0.6447 | 0.728 |
| 6.0 | -0.6437 | 0.729 |

The fit rises quickly up to about α = 2 and is almost flat after that. The optimizer finds an inside best point at **α\* = 2.979**. Every α from about 2.4 upward fits nearly as well (within 1.92 total log-likelihood units, the usual 95% limit), so the data rule out small values of α but do not pin down large ones. Above α ≈ 4 the fit rises slowly again and passes the inside best point near α = 4.6 (by 1.4 total log-likelihood units at α = 6, which is not significant). At such large α, f_distance is close to 1 for almost every candidate, so the per-type f_distance columns act like the type constants rejected in [Model 5: alternative-specific constants (rejected)](m-model-5-asc-rejected.md). So the inside best point is used. Computing the scores again from scratch at this value gives the same result as the shortcut, to within 2e-16.

- Model 2 has its own best α (2.275). Using that value in Model 4a costs little (1.5 total log-likelihood units, below the 1.92 that would count as significant), and using Model 4a's α in Model 2 costs almost nothing (0.1). So the two models agree on how fast the score should fall.
- **Tune α once on Model 4a, then build the later models with that value.** Tuning α again inside Model 5 gives 2.28 and improves the fit by only 0.3 total log-likelihood units (accuracy +0.4 percentage points). Inside Model 6 with its α = 1 terms it gives 2.45 and improves the fit by 3.0 units (accuracy +0.8 points), but that model is not used: its terms were chosen at α = 1, and it is very unstable at any α (condition number above 140,000). So tuning once loses almost nothing for the models that matter.
- Model 1 has no inside best point. Its fit is best at the smallest α tried (0.2) and hardly changes over the whole range, and no value of α fixes its main problem ([Model 1: base](m-model-1-base.md)).

The main result of this step: [The f_distance² artifact](m-f-distance-squared-artifact.md). With the full data, before downsampling, the best α moves: [Raw-density alpha profile](m-raw-density-alpha-profile.md). Part of [Calibration](../threads/m-calibration.md).


<div class="backlinks" markdown>

**Linked from** [Calibration](../threads/m-calibration.md) · [MNL model development](../progress/m-progress-19-07-2026.md) · [Model 1: base](m-model-1-base.md) · [Model 4a: alternative-specific parameters](m-model-4a-alternative-specific.md) · [RQ1 rebuilt with grouped CV](../progress/m-progress-21-07-2026.md) · [Raw-density alpha profile](m-raw-density-alpha-profile.md) · [The f_distance² artifact](m-f-distance-squared-artifact.md) · [f_distance](../concepts/m-f-distance.md)

</div>
