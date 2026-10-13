---
source: report/analysis/f-distance-squared-artifact.md
date: 21-07-2026
kind: analysis
comments: true
generated: 2026-10-13T16:57:34
---

# The f_distance² artifact

<p class="doc-meta"><span class="chip chip-analysis">Analysis</span> <span class="chip chip-date">21-07-2026</span></p>

At α = 1, a squared distance term was clearly significant (t = 3.81) in the [Interaction term screen (α = 1)](interaction-term-screen.md). After [Alpha calibration](alpha-calibration.md) (α = 2.4297), the same screen re-run from scratch gives **t = 0.50**.

The squared term was compensating for a too-narrow decay, not capturing real nonlinearity. It also caused most of Model 6's conditioning problem.

| Screen term | t at α = 1 | t at α = 2.4297 |
|---|---:|---:|
| f_distance² | 3.81 | **0.50** |
| σ² | 2.23 | 2.47 |
| f_distribution × σ | -0.15 | 0.32 |
| f_distance × f_directional | 0.11 | 1.73 |
| f_distribution × share_type | 5.58 | 4.91 |

Lesson: re-derive the term selection at the calibrated α; bolting the new α onto old terms doubled VIFs instead (condition number 20,695 → 48,275).

One case of [Overfitting signature](../notes/overfitting-signature.md). Next: [Model 6, re-derived at calibrated alpha](model-6-rederived.md). Part of [Chapter 5: Results](../progress/ch5-results.md).


<div class="backlinks" markdown>

**Linked from** [Alpha calibration](alpha-calibration.md) · [Chapter 5: Results](../progress/ch5-results.md) · [Interaction term screen (α = 1)](interaction-term-screen.md) · [MNL model development](../progress/progress-19-07-2026.md) · [Overfitting signature](../notes/overfitting-signature.md) · [RQ1 rebuilt with grouped CV](../progress/progress-21-07-2026.md) · [f_distance](../notes/f-distance.md)

</div>
