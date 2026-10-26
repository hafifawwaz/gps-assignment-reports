---
source: report/analysis/m-interaction-term-screen.md
date: 21-07-2026
kind: analysis
comments: true
generated: 2026-10-26T20:52:49
---

# Interaction term screen (α = 1)

<p class="doc-meta"><span class="chip chip-analysis">Analysis</span> <span class="chip chip-project">Master</span> <span class="chip chip-date">21-07-2026</span></p>

Could combined or squared terms help the model? Five such terms were tested together, on top of the 7-parameter model with shared weights. An interaction term multiplies two inputs, for example f_distribution × σ. A term with a t-value above about 2 counts as significant.

| Term | w | t | |
|---|---:|---:|---|
| f_distance² | +4.702 | 3.78 | significant |
| σ² | +0.407 | 4.31 | significant |
| f_distribution × σ | +0.557 | 1.55 | |
| f_distance × f_directional | +1.133 | 0.88 | |
| **f_distribution × share_type** | **+4.422** | **4.12** | significant |

The three significant terms were added to [Model 4a: alternative-specific parameters](m-model-4a-alternative-specific.md). This gives Model 6, with 16 parameters:


$$V_t = w_{1,t} f_\text{distribution} + w_{2,t} f_\text{distance} + w_{3,t} f_\text{directional} + w_{4,t}\,share_t + w_5\,\sigma + w_6\,f_\text{distance}^2 + w_7\,\sigma^2 + w_8\,(f_\text{distribution}\times share_\text{type})$$


| | 4a | Model 6 (α = 1) |
|---|---:|---:|
| Accuracy | 0.722 | 0.728 |
| Building / street / open space | 0.889 / 0.519 / 0.455 | 0.883 / 0.519 / **0.497** |
| CV accuracy (grouped) | 0.700 ± 0.036 | 0.710 ± 0.031 |
| Condition number | 737 | 13,198 |

Model 6 raises **open space** further (to 0.497), keeps street the same, and lowers building a little. Inside the larger model, σ² is no longer significant (t falls to 1.56). And f_distance² turns out to make up for an α that was not yet tuned: [The f_distance² artifact](m-f-distance-squared-artifact.md).

The two terms that were not significant are built from inputs that overlap strongly (VIF up to 71). So "not significant" is weak evidence for them.

The same test with the tuned α: [Model 6, re-derived at calibrated alpha](m-model-6-rederived.md). Part of [Calibration](../threads/m-calibration.md).


<div class="backlinks" markdown>

**Linked from** [Calibration](../threads/m-calibration.md) · [MNL model development](../progress/m-progress-19-07-2026.md) · [Model 4a: alternative-specific parameters](m-model-4a-alternative-specific.md) · [Model progression](m-model-progression-table.md) · [The f_distance² artifact](m-f-distance-squared-artifact.md) · [f_distribution](../concepts/m-f-distribution.md)

</div>
