---
source: report/analysis/model-5-asc-rejected.md
date: 21-07-2026
kind: analysis
comments: true
generated: 2026-10-13T20:30:42
---

# Model 5: alternative-specific constants (rejected)

<p class="doc-meta"><span class="chip chip-analysis">Analysis</span> <span class="chip chip-date">21-07-2026</span></p>

[Model 4a: alternative-specific parameters](model-4a-alternative-specific.md) plus `asc_street`, `asc_os` (building = reference), 15 parameters.

| | 4a | 5 (+ ASC) |
|---|---:|---:|
| Accuracy | 0.717 | 0.728 |
| CV accuracy (grouped) | 0.707 ± 0.069 | 0.717 ± 0.068 |
| LR vs 4a (df=2) | | 29.6, p < 0.0001 |
| Max VIF | 10.69 | **39.76** |
| Condition number | 775 | **37,583** |

Formally significant, but the CV gain is within one standard deviation, and **`asc_street` ↔ `f_directional_street` r = 0.96**: [f_directional](../notes/f-directional.md) is nearly constant within street candidates, so the model is asked to estimate the same "street-ness" twice. The directional terms and `asc_street` get standard errors around 4.5 and lose significance; CV estimates swing by 60-65% of their mean.

At 15 m it gets worse (condition number 92,891) and some CV folds diverge to coefficients in the thousands. Calibrating alpha adds two more near-duplicate pairs (`asc_t` ↔ `f_distance_t`, r = 0.98).

**Rejected on reliability grounds.** One case of [Overfitting signature](../notes/overfitting-signature.md). Part of [Calibration](../threads/calibration.md).


<div class="backlinks" markdown>

**Linked from** [Calibration](../threads/calibration.md) · [MNL model development](../progress/progress-19-07-2026.md) · [Model 4a: alternative-specific parameters](model-4a-alternative-specific.md) · [Model progression](model-progression-table.md) · [Multicollinearity is structural](../notes/multicollinearity-is-structural.md) · [Overfitting signature](../notes/overfitting-signature.md) · [RQ1 rebuilt with grouped CV](../progress/progress-21-07-2026.md) · [R_buffer: 10 m vs 15 m](r-buffer-10m-vs-15m.md) · [f_directional](../notes/f-directional.md)

</div>
