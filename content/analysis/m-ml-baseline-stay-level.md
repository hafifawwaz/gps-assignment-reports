---
source: report/analysis/m-ml-baseline-stay-level.md
date: 20-07-2026
kind: analysis
comments: true
generated: 2026-10-14T14:44:07
---

# ML baseline, stay level (superseded)

<p class="doc-meta"><span class="chip chip-analysis">Analysis</span> <span class="chip chip-project">Master</span> <span class="chip chip-date">20-07-2026</span></p>

Sensei asked whether Random Forest or XGBoost could show the best possible result, since these methods can find curved and combined effects by themselves. Both were trained to choose one of three types, using the same 13 inputs as the simple model, one row per stay, with no combined terms added by hand. They were tested with normal (not grouped) cross-validation.

| Model | CV accuracy | Building | Street | Open space |
|---|---:|---:|---:|---:|
| Logit (14 params) | 0.716 ± 0.035 | | | |
| RF | **0.754 ± 0.023** | 0.913 | 0.573 | 0.487 |
| RF, class-weighted | 0.753 ± 0.017 | 0.917 | 0.562 | 0.482 |
| XGBoost | 0.723 ± 0.015 | 0.855 | 0.557 | 0.518 |
| XGBoost, class-weighted | 0.725 ± 0.012 | 0.838 | 0.600 | 0.534 |

"Class-weighted" means the less common types (street, open space) were given more importance during training.

At the time, this looked like room for a small improvement (Random Forest +3.8 percentage points). Every tree model scored 1.000 on its own training data, which means it memorized the data.

**Replaced:** normal cross-validation lets recordings of the same stop from different phones end up in both training and testing ([Grouped cross-validation](../notes/m-grouped-cross-validation.md)). The fair comparison turns the ranking around: [ML ceiling check, row level](m-ml-ceiling-row-level.md). The finding about σ still holds: [Sigma in tree importance](m-sigma-tree-importance.md).

Part of [Complexity and transfer](../threads/m-complexity-and-transfer.md).


<div class="backlinks" markdown>

**Linked from** [Complexity and transfer](../threads/m-complexity-and-transfer.md) · [Grouped cross-validation](../notes/m-grouped-cross-validation.md) · [ML baseline](../progress/m-progress-20-07-2026.md) · [ML ceiling check, row level](m-ml-ceiling-row-level.md) · [Sigma in tree importance](m-sigma-tree-importance.md)

</div>
