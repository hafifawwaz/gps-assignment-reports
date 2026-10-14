---
source: report/notes/m-grouped-cross-validation.md
date: 21-07-2026
kind: note
comments: true
generated: 2026-10-14T14:44:07
---

# Grouped cross-validation

<p class="doc-meta"><span class="chip chip-note">Note</span> <span class="chip chip-project">Master</span> <span class="chip chip-date">21-07-2026</span></p>

Cross-validation (CV) tests a model on data it did not learn from. The data is split into 5 parts. The model learns from 4 parts and is tested on the 5th, and this repeats five times.

In this survey, up to **3 phones** recorded each stop at the same time ([Experiment design](m-experiment-design.md)). So up to 3 records share the same correct answer and the same situation. In normal CV, one phone's record can land in the training part and another phone's record of the same stop in the test part. The model then sees almost the same stop during learning and testing, and the result looks better than it should.

Since 21-07-2026, every CV number uses `StratifiedGroupKFold` with 5 parts, **grouped by real stop** (participant and stop number). All records of one stop always stay in the same part. All models were tested again this way ([Model progression](../analysis/m-model-progression-table.md)).

The effect: accuracy on the training data did not change (about 0.724). But the CV result for the 14-parameter model became **0.709 ± 0.075**, instead of the earlier 0.716 ± 0.035. The wider range is the honest one. Earlier results from normal CV, such as [ML baseline, stay level (superseded)](../analysis/m-ml-baseline-stay-level.md), are replaced.

Part of [Calibration](../threads/m-calibration.md).


<div class="backlinks" markdown>

**Linked from** [Calibration](../threads/m-calibration.md) · [Experiment design](m-experiment-design.md) · [Limitations](m-limitations.md) · [ML baseline, stay level (superseded)](../analysis/m-ml-baseline-stay-level.md) · [Model evaluation metrics](m-model-evaluation-metrics.md) · [Model progression](../analysis/m-model-progression-table.md) · [RQ1 rebuilt with grouped CV](../progress/m-progress-21-07-2026.md) · [R_buffer: 10 m vs 15 m](../analysis/m-r-buffer-10m-vs-15m.md)

</div>
