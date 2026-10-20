---
source: report/analysis/m-r-buffer-10m-vs-15m.md
date: 19-07-2026
kind: analysis
comments: true
generated: 2026-10-20T15:22:17
---

# R_buffer: 10 m vs 15 m

<p class="doc-meta"><span class="chip chip-analysis">Analysis</span> <span class="chip chip-project">Master</span> <span class="chip chip-date">19-07-2026</span></p>

Which search distance (`R_buffer`) is better for finding candidates around a stay? **10 m beats 15 m for every model tested**, in accuracy and in fit (log-likelihood). Stability does not decide it: the condition number is lower at 15 m for some models and at 10 m for others.

| Model | Accuracy R=10 m | Accuracy R=15 m | Δ |
|---|---:|---:|---:|
| 1 Base | 0.540 | 0.538 | +0.2 pp |
| 2 Share-type + σ | 0.673 | 0.649 | +2.3 pp |
| 4a Alternative-specific | 0.722 | 0.703 | +1.9 pp |
| 5 + ASC | 0.728 | 0.727 | +0.1 pp |
| 6 + interactions | 0.728 | 0.700 | +2.8 pp |

(pp = percentage points.) The result held again with [Grouped cross-validation](../notes/m-grouped-cross-validation.md) on 21-07-2026. From the directional test onward, only 10 m was used.

One caution: ρ² cannot be compared between the two distances, because its baseline changes when the candidates change ([Model evaluation metrics](../notes/m-model-evaluation-metrics.md)).

A wider search distance brings in more street pieces that are not really relevant. Street accuracy suffers at 15 m ([Model 1: base](m-model-1-base.md), [Model 2: share-type and sigma](m-model-2-share-type-sigma.md)).

Part of [Calibration](../threads/m-calibration.md). How candidates are found: [Candidate selection](../notes/m-candidate-selection.md).


<div class="backlinks" markdown>

**Linked from** [Calibration](../threads/m-calibration.md) · [Candidate selection](../notes/m-candidate-selection.md) · [Downsampling shrinks the candidate search area](m-candidate-search-area.md) · [MNL model development](../progress/m-progress-19-07-2026.md) · [Model evaluation metrics](../notes/m-model-evaluation-metrics.md) · [Thesis bug fixes and adopted rerun](../inbox/thesis-bug-fix.md)

</div>
