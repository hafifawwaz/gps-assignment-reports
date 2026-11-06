---
source: report/analysis/m-ml-baseline-stay-level.md
date: 20-07-2026
kind: analysis
comments: true
generated: 2026-11-06T11:37:20
---

# ML baseline, stay level (superseded)

<p class="doc-meta"><span class="chip chip-analysis">Analysis</span> <span class="chip chip-project">Master</span> <span class="chip chip-date">20-07-2026</span></p>

Sensei asked whether Random Forest or XGBoost could show the best possible result, since these methods can find curved and combined effects by themselves. Both were trained to choose one of three types, using the same 13 inputs as Model 4a, one row per stay, with no combined terms added by hand. They were tested with normal (not grouped) cross-validation.

| Model | CV accuracy | Building | Street | Open space |
|---|---:|---:|---:|---:|
| Logit (final, 11 params) | 0.716 ± 0.016 | | | |
| RF | 0.734 ± 0.023 | 0.878 | 0.584 | 0.482 |
| RF, class-weighted | **0.745 ± 0.019** | 0.898 | 0.584 | 0.476 |
| XGBoost | 0.722 ± 0.027 | 0.846 | 0.589 | 0.508 |
| XGBoost, class-weighted | 0.717 ± 0.020 | 0.823 | 0.605 | 0.529 |

"Class-weighted" means the less common types (street, open space) were given more importance during training.

At the time, this looked like room for a small improvement (Random Forest about +2 percentage points; XGBoost about the same as the logit). Every tree model scored 1.000 on its own training data, which means it memorized the data.

**Replaced:** normal cross-validation lets recordings of the same stop from different phones end up in both training and testing ([Grouped cross-validation](../concepts/m-grouped-cross-validation.md)). The fair comparison turns the ranking around: [ML ceiling check, row level](m-ml-ceiling-row-level.md). The finding about σ still holds: [Sigma in tree importance](m-sigma-tree-importance.md).

Part of [Complexity and transfer](../threads/m-complexity-and-transfer.md).


<div class="backlinks" markdown>

**Linked from** [Complexity and transfer](../threads/m-complexity-and-transfer.md) · [Grouped cross-validation](../concepts/m-grouped-cross-validation.md) · [ML baseline](../progress/m-progress-20-07-2026.md) · [ML ceiling check, row level](m-ml-ceiling-row-level.md) · [Sigma in tree importance](m-sigma-tree-importance.md)

</div>
