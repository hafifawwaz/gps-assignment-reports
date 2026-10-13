---
source: report/analysis/alpha-calibration.md
date: 21-07-2026
kind: analysis
comments: true
generated: 2026-10-13T20:30:42
---

# Alpha calibration

<p class="doc-meta"><span class="chip chip-analysis">Analysis</span> <span class="chip chip-date">21-07-2026</span></p>

$\alpha$ sets the width of [f_distance](../notes/f-distance.md)'s decay. It is calibrated by **profile likelihood on Model 4a**: for each α the other weights are refit, and LL(b) scores that α. Since $f_\text{distance}(\alpha) = f_\text{distance}(1)^{1/\alpha^2}$, no rescoring is needed during the search.

| α | LL(b) | Accuracy |
|---:|---:|---:|
| 1.0 | -0.6881 | 0.717 |
| 2.0 | -0.6708 | 0.726 |
| **2.4** | **-0.6701** | 0.723 |
| 3.0 | -0.6707 | 0.720 |
| 4.0 | -0.6725 | 0.720 |

Single peak; optimizer gives **α\* = 2.4297**. Real rescoring at that value matches the shortcut to 2e-16.

- Model 2's own optimum (2.106) transfers to 4a at almost no cost, and vice versa: the models agree on the decay width.
- **Calibrate once on 4a and re-derive downstream models**, rather than recalibrating inside richer ones: for Models 5 and 6 that marginally raised LL, lowered accuracy and roughly doubled VIFs.
- Model 1's surface is not single-peaked and no α fixes its core problem ([Model 1: base](model-1-base.md)).

Main payoff: [The f_distance² artifact](f-distance-squared-artifact.md). On raw-density data the optimum moves: [Raw-density alpha profile](raw-density-alpha-profile.md). Part of [Calibration](../threads/calibration.md).


<div class="backlinks" markdown>

**Linked from** [Calibration](../threads/calibration.md) · [MNL model development](../progress/progress-19-07-2026.md) · [Model 1: base](model-1-base.md) · [Model 4a: alternative-specific parameters](model-4a-alternative-specific.md) · [RQ1 rebuilt with grouped CV](../progress/progress-21-07-2026.md) · [Raw-density alpha profile](raw-density-alpha-profile.md) · [The f_distance² artifact](f-distance-squared-artifact.md) · [f_distance](../notes/f-distance.md)

</div>
