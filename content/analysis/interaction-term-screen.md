---
source: report/analysis/interaction-term-screen.md
date: 21-07-2026
kind: analysis
comments: true
generated: 2026-10-13T20:30:42
---

# Interaction term screen (α = 1)

<p class="doc-meta"><span class="chip chip-analysis">Analysis</span> <span class="chip chip-date">21-07-2026</span></p>

Five candidate terms screened jointly on the generic 7-parameter base:

| Term | w | t | |
|---|---:|---:|---|
| f_distance² | +4.588 | 3.81 | significant |
| σ² | +0.165 | 2.22 | significant |
| f_distribution × σ | -0.058 | -0.15 | |
| f_distance × f_directional | +0.150 | 0.11 | |
| **f_distribution × share_type** | **+5.264** | **5.57** | significant, largest |

The three significant terms were added to [Model 4a: alternative-specific parameters](model-4a-alternative-specific.md) (Model 6, 16 parameters):

| | 4a | Model 6 (α = 1) |
|---|---:|---:|
| Accuracy | 0.717 | 0.724 |
| Building / street / open space | 0.902 / 0.443 / 0.466 | 0.876 / **0.497** / **0.524** |
| CV accuracy (grouped) | 0.707 ± 0.069 | 0.711 ± 0.077 |
| Condition number | 775 | 20,695 |

The first model to move **open space** (to 0.524), at a cost to building. But σ² dies inside the richer model (t → -0.27), and f_distance² turns out to be compensating for uncalibrated alpha: [The f_distance² artifact](f-distance-squared-artifact.md).

The screen's two non-significant terms sit on badly collinear ingredients (VIF up to 73), so "not significant" is weak evidence here.

Re-run at calibrated alpha: [Model 6, re-derived at calibrated alpha](model-6-rederived.md). Part of [Calibration](../threads/calibration.md).


<div class="backlinks" markdown>

**Linked from** [Calibration](../threads/calibration.md) · [MNL model development](../progress/progress-19-07-2026.md) · [Model 4a: alternative-specific parameters](model-4a-alternative-specific.md) · [Model progression](model-progression-table.md) · [The f_distance² artifact](f-distance-squared-artifact.md) · [f_distribution](../notes/f-distribution.md)

</div>
