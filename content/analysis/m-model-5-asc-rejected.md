---
source: report/analysis/m-model-5-asc-rejected.md
date: 21-07-2026
kind: analysis
comments: true
generated: 2026-10-14T14:44:07
---

# Model 5: alternative-specific constants (rejected)

<p class="doc-meta"><span class="chip chip-analysis">Analysis</span> <span class="chip chip-project">Master</span> <span class="chip chip-date">21-07-2026</span></p>

[Model 4a: alternative-specific parameters](m-model-4a-alternative-specific.md) plus two constants, `asc_street` and `asc_os`. A constant (ASC) is a fixed extra value for each type, which shows whether a type is preferred in general. Building is the reference ($ASC_\text{bldg} = 0$). In total, 15 parameters:


$$V_t = w_{1,t} f_\text{distribution} + w_{2,t} f_\text{distance} + w_{3,t} f_\text{directional} + w_{4,t}\,share_t + w_5\,\sigma + ASC_t$$


| | 4a | 5 (+ ASC) |
|---|---:|---:|
| Accuracy | 0.717 | 0.728 |
| CV accuracy (grouped) | 0.707 ± 0.069 | 0.717 ± 0.068 |
| LR vs 4a (df=2) | | 29.6, p < 0.0001 |
| Max VIF | 10.69 | **39.76** |
| Condition number | 775 | **37,583** |

On paper, the constants are significant. But the gain on unseen data is smaller than the normal spread between test sets. And **`asc_street` and `f_directional_street` move almost together (r = 0.96)**. The reason: [f_directional](../notes/m-f-directional.md) hardly changes between street candidates, so it acts almost like a constant for streets. The model is asked to measure the same "street-ness" twice. As a result, the direction weights and `asc_street` get standard errors of about 4.5 and are no longer significant, and their values change by 60-65% between test sets.

With a 15 m search distance it gets worse: the condition number reaches 92,891, and in some test sets the weights run off to values in the thousands. Tuning α adds two more pairs that move almost together (`asc_t` and `f_distance_t`, r = 0.98).

**Rejected, because its weights cannot be trusted.** One case of [Overfitting signature](../notes/m-overfitting-signature.md). Part of [Calibration](../threads/m-calibration.md).


<div class="backlinks" markdown>

**Linked from** [Calibration](../threads/m-calibration.md) · [MNL model development](../progress/m-progress-19-07-2026.md) · [Model 4a: alternative-specific parameters](m-model-4a-alternative-specific.md) · [Model progression](m-model-progression-table.md) · [Multicollinearity is structural](../notes/m-multicollinearity-is-structural.md) · [Overfitting signature](../notes/m-overfitting-signature.md) · [RQ1 rebuilt with grouped CV](../progress/m-progress-21-07-2026.md) · [R_buffer: 10 m vs 15 m](m-r-buffer-10m-vs-15m.md) · [f_directional](../notes/m-f-directional.md)

</div>
