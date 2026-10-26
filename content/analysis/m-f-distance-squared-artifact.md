---
source: report/analysis/m-f-distance-squared-artifact.md
date: 21-07-2026
kind: analysis
comments: true
generated: 2026-10-26T20:41:14
---

# The f_distance² artifact

<p class="doc-meta"><span class="chip chip-analysis">Analysis</span> <span class="chip chip-project">Master</span> <span class="chip chip-date">21-07-2026</span></p>

With α = 1, a squared distance term (f_distance²) looked clearly significant (t = 3.78) in the [Interaction term screen (α = 1)](m-interaction-term-screen.md). After [Alpha calibration](m-alpha-calibration.md) set α to 2.764, the same test, run again from the start, gives only **t = 0.11**.

So the squared term was not finding a real curve in the data. It was making up for a distance score that fell too fast because α was too small. It also caused much of the instability of Model 6, where it had the highest VIF (44.7).

| Screen term | t at α = 1 | t at α = 2.764 |
|---|---:|---:|
| f_distance² | 3.78 | **0.11** |
| σ² | 4.31 | 4.49 |
| f_distribution × σ | 1.55 | 1.67 |
| f_distance × f_directional | 0.88 | 1.88 |
| f_distribution × share_type | 4.12 | 3.71 |

Lesson: after changing α, choose the extra terms again from the start. Keeping the old terms and only changing α made the model far less stable (condition number from 13,198 to 142,550; highest VIF from 45 to 180, on f_distance²).

One case of [Overfitting signature](../concepts/m-overfitting-signature.md). Next: [Model 6, re-derived at calibrated alpha](m-model-6-rederived.md). Part of [Calibration](../threads/m-calibration.md).


<div class="backlinks" markdown>

**Linked from** [Alpha calibration](m-alpha-calibration.md) · [Calibration](../threads/m-calibration.md) · [Interaction term screen (α = 1)](m-interaction-term-screen.md) · [MNL model development](../progress/m-progress-19-07-2026.md) · [Overfitting signature](../concepts/m-overfitting-signature.md) · [RQ1 rebuilt with grouped CV](../progress/m-progress-21-07-2026.md) · [f_distance](../concepts/m-f-distance.md)

</div>
