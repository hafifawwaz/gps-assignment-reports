---
source: report/analysis/ml-ceiling-row-level.md
date: 23-07-2026
kind: analysis
comments: true
generated: 2026-10-13T16:57:34
---

# ML ceiling check, row level

<p class="doc-meta"><span class="chip chip-analysis">Analysis</span> <span class="chip chip-date">23-07-2026</span></p>

Random Forest and XGBoost on the **same row-level task** as the logit (one row per stay-candidate pair), raw unsplit features plus a one-hot type, on the **identical grouped-CV folds**.

| Model | In-sample | **CV (grouped)** | CV building | CV street | CV open space |
|---|---:|---:|---:|---:|---:|
| Logit, [Final model](final-model.md) | 0.721 | **0.716 ± 0.076** | 0.896 | 0.429 | **0.491** |
| Random Forest | 0.762 | 0.699 ± 0.063 | 0.942 | 0.439 | 0.277 |
| XGBoost | **0.849** | 0.695 ± 0.071 | 0.893 | 0.461 | 0.371 |

Both trees win in-sample, and **both lose under grouped CV**. The gap is almost all open space; building and street are comparable. No headroom once evaluated honestly, reversing [ML baseline, stay level (superseded)](ml-baseline-stay-level.md).

Settings: RF 400 trees, depth 8, min leaf 5; XGBoost 300 rounds, depth 4, learning rate 0.1; not tuned. All three models rank the folds the same way ([Fold difficulty](fold-difficulty.md)).

The clearest case of [Overfitting signature](../notes/overfitting-signature.md). Importance: [Sigma in tree importance](sigma-tree-importance.md). Part of [Chapter 5: Results](../progress/ch5-results.md).


<div class="backlinks" markdown>

**Linked from** [Chapter 5: Results](../progress/ch5-results.md) · [Fold difficulty](fold-difficulty.md) · [ML baseline, stay level (superseded)](ml-baseline-stay-level.md) · [Overfitting signature](../notes/overfitting-signature.md) · [Positioning against deterministic assignment](../notes/positioning-vs-deterministic-assignment.md) · [RQ2 diagnostics and RQ3 ceiling check](../progress/progress-23-07-2026.md) · [Research questions](../notes/research-questions.md) · [Sigma in tree importance](sigma-tree-importance.md) · [Thesis summary](../progress/thesis-summary.md)

</div>
