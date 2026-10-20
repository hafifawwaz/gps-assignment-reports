---
source: report/analysis/m-ml-ceiling-row-level.md
date: 23-07-2026
kind: analysis
comments: true
generated: 2026-10-20T15:22:17
---

# ML ceiling check, row level

<p class="doc-meta"><span class="chip chip-analysis">Analysis</span> <span class="chip chip-project">Master</span> <span class="chip chip-date">23-07-2026</span></p>

A fair comparison between the simple model and two machine-learning models. Random Forest and XGBoost got **exactly the same task** as the simple model (one row per stay and candidate), the raw inputs plus the place type, and **exactly the same grouped test sets**.

| Model | In-sample | **CV (grouped)** | CV building | CV street | CV open space |
|---|---:|---:|---:|---:|---:|
| Logit, [Final model](m-final-model.md) | 0.731 | **0.719 ± 0.032** | 0.900 | 0.486 | **0.439** |
| Random Forest | 0.750 | 0.708 ± 0.027 | 0.947 | 0.459 | 0.282 |
| XGBoost | **0.829** | 0.703 ± 0.049 | 0.913 | 0.486 | 0.329 |

Both tree models win on the training data (in-sample), and **both lose on unseen data** (CV). Almost the whole difference comes from open space. For street the three models are close, and for building the trees do a little better. So with a fair test, the machine-learning models offer no improvement. This reverses the earlier result in [ML baseline, stay level (superseded)](m-ml-baseline-stay-level.md).

Settings: Random Forest with 400 trees, depth 8, at least 5 rows per leaf. XGBoost with 300 rounds, depth 4, learning rate 0.1. Neither was tuned. The three models agree only in part on which test sets are hard: fold 1 is the hardest for all three ([Fold difficulty](m-fold-difficulty.md)).

The clearest case of [Overfitting signature](../notes/m-overfitting-signature.md). Which inputs the trees use: [Sigma in tree importance](m-sigma-tree-importance.md). Part of [Complexity and transfer](../threads/m-complexity-and-transfer.md).


<div class="backlinks" markdown>

**Linked from** [Complexity and transfer](../threads/m-complexity-and-transfer.md) · [Fold difficulty](m-fold-difficulty.md) · [ML baseline, stay level (superseded)](m-ml-baseline-stay-level.md) · [Overfitting signature](../notes/m-overfitting-signature.md) · [Positioning against deterministic assignment](../notes/m-positioning-vs-deterministic-assignment.md) · [RQ2 diagnostics and RQ3 ceiling check](../progress/m-progress-23-07-2026.md) · [Research questions](../notes/m-research-questions.md) · [Sigma in tree importance](m-sigma-tree-importance.md) · [Thesis bug fixes and adopted rerun](../inbox/thesis-bug-fix.md) · [Thesis summary](../threads/m-thesis-summary.md)

</div>
