---
source: report/analysis/r-buffer-10m-vs-15m.md
date: 19-07-2026
kind: analysis
comments: true
generated: 2026-10-13T20:30:42
---

# R_buffer: 10 m vs 15 m

<p class="doc-meta"><span class="chip chip-analysis">Analysis</span> <span class="chip chip-date">19-07-2026</span></p>

**10 m wins for every model tested**, on accuracy, log-likelihood and conditioning, and the gap widens as models grow:

| Model | Accuracy R=10 m | Accuracy R=15 m | Δ |
|---|---:|---:|---:|
| 1 Base | 0.518 | 0.509 | +0.9 pp |
| 2 Share-type + σ | 0.668 | 0.654 | +1.4 pp |
| 4a Alternative-specific | 0.717 | 0.698 | +1.9 pp |
| 5 + ASC | 0.728 | 0.709 | +1.9 pp |
| 6 + interactions | 0.724 | 0.699 | +2.5 pp |

Reconfirmed under [Grouped cross-validation](../notes/grouped-cross-validation.md) on 21-07-2026. From the directional ablation onward only 10 m was fit.

Two cautions: ρ² vs LL(C) is not comparable across radii ([Model evaluation metrics](../notes/model-evaluation-metrics.md)); and at 15 m the ASC model's CV fits diverged outright ([Model 5: alternative-specific constants (rejected)](model-5-asc-rejected.md)).

Wider buffers pull in more low-quality street candidates; street accuracy suffers most at 15 m ([Model 1: base](model-1-base.md)).

Part of [Calibration](../threads/calibration.md). Mechanism: [Candidate selection](../notes/candidate-selection.md).


<div class="backlinks" markdown>

**Linked from** [Calibration](../threads/calibration.md) · [Candidate selection](../notes/candidate-selection.md) · [Downsampling shrinks the candidate search area](candidate-search-area.md) · [MNL model development](../progress/progress-19-07-2026.md) · [Model evaluation metrics](../notes/model-evaluation-metrics.md)

</div>
