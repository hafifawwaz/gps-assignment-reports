---
source: report/analysis/m-f-distance-squared-artifact.md
date: 21-07-2026
kind: analysis
comments: true
generated: 2026-10-14T14:44:07
---

# The f_distance² artifact

<p class="doc-meta"><span class="chip chip-analysis">Analysis</span> <span class="chip chip-project">Master</span> <span class="chip chip-date">21-07-2026</span></p>

With α = 1, a squared distance term (f_distance²) looked clearly significant (t = 3.81) in the [Interaction term screen (α = 1)](m-interaction-term-screen.md). After [Alpha calibration](m-alpha-calibration.md) set α to 2.4297, the same test, run again from the start, gives only **t = 0.50**.

So the squared term was not finding a real curve in the data. It was making up for a distance score that fell too fast because α was too small. It also caused most of the instability of Model 6.

| Screen term | t at α = 1 | t at α = 2.4297 |
|---|---:|---:|
| f_distance² | 3.81 | **0.50** |
| σ² | 2.23 | 2.47 |
| f_distribution × σ | -0.15 | 0.32 |
| f_distance × f_directional | 0.11 | 1.73 |
| f_distribution × share_type | 5.58 | 4.91 |

Lesson: after changing α, choose the extra terms again from the start. Keeping the old terms and only changing α doubled the VIF warning values (condition number from 20,695 to 48,275).

One case of [Overfitting signature](../notes/m-overfitting-signature.md). Next: [Model 6, re-derived at calibrated alpha](m-model-6-rederived.md). Part of [Calibration](../threads/m-calibration.md).


<div class="backlinks" markdown>

**Linked from** [Alpha calibration](m-alpha-calibration.md) · [Calibration](../threads/m-calibration.md) · [Interaction term screen (α = 1)](m-interaction-term-screen.md) · [MNL model development](../progress/m-progress-19-07-2026.md) · [Overfitting signature](../notes/m-overfitting-signature.md) · [RQ1 rebuilt with grouped CV](../progress/m-progress-21-07-2026.md) · [f_distance](../notes/m-f-distance.md)

</div>
