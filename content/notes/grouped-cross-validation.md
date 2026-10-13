---
source: report/notes/grouped-cross-validation.md
date: 21-07-2026
kind: note
comments: true
generated: 2026-10-13T16:57:34
---

# Grouped cross-validation

<p class="doc-meta"><span class="chip chip-note">Note</span> <span class="chip chip-date">21-07-2026</span></p>

Each physical stop was recorded by up to **3 devices** at once ([Experiment design](experiment-design.md)), so up to 3 stay records share one label and context. Plain stratified CV can put siblings in both train and test, which leaks and inflates accuracy.

Since 21-07-2026 every CV number uses `StratifiedGroupKFold` (5 folds) **grouped by physical stop** (participant and stop sequence), so siblings always share a fold. The whole progression was refit under it ([Model progression](../analysis/model-progression-table.md)).

Effect on the headline: in-sample accuracy unchanged (~0.724), but CV became **0.709 ± 0.075** for the 14-parameter model instead of the earlier 0.716 ± 0.035. The wider band is the honest one. Earlier stay-level CV results, such as [ML baseline, stay level (superseded)](../analysis/ml-baseline-stay-level.md), are superseded.

Part of [Chapter 4: Framework](../progress/ch4-framework.md).


<div class="backlinks" markdown>

**Linked from** [Chapter 4: Framework](../progress/ch4-framework.md) · [Experiment design](experiment-design.md) · [Limitations](limitations.md) · [ML baseline, stay level (superseded)](../analysis/ml-baseline-stay-level.md) · [Model evaluation metrics](model-evaluation-metrics.md) · [Model progression](../analysis/model-progression-table.md) · [RQ1 rebuilt with grouped CV](../progress/progress-21-07-2026.md) · [R_buffer: 10 m vs 15 m](../analysis/r-buffer-10m-vs-15m.md)

</div>
