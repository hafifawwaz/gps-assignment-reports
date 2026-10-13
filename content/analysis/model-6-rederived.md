---
source: report/analysis/model-6-rederived.md
date: 21-07-2026
kind: analysis
comments: true
generated: 2026-10-13T16:57:34
---

# Model 6, re-derived at calibrated alpha

<p class="doc-meta"><span class="chip chip-analysis">Analysis</span> <span class="chip chip-date">21-07-2026</span></p>

[Model 4a: alternative-specific parameters](model-4a-alternative-specific.md) at α = 2.4297 plus the two terms that survived the re-run screen (σ² and f_distribution × share_type): 15 parameters.

| | 4a at α\* | Model 6 re-derived |
|---|---:|---:|
| LL(b) | -0.6701 | -0.6520 |
| LR vs 4a at α\* (df=2) | | 32.72, p < 1e-7 |
| Accuracy | 0.723 | 0.723 |
| CV accuracy (grouped) | 0.717 ± 0.065 | 0.710 ± 0.075 |
| Condition number | 2,338 | 14,851 |
| Max VIF | | 18.38 (σ²) |

Significant fit gain, but a real conditioning cost, and σ² again carries little. Next: [Stepwise VIF elimination](stepwise-vif-elimination.md). Part of [Chapter 5: Results](../progress/ch5-results.md).


<div class="backlinks" markdown>

**Linked from** [Chapter 5: Results](../progress/ch5-results.md) · [Interaction term screen (α = 1)](interaction-term-screen.md) · [Model progression](model-progression-table.md) · [Stepwise VIF elimination](stepwise-vif-elimination.md) · [The f_distance² artifact](f-distance-squared-artifact.md)

</div>
