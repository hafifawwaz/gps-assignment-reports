---
source: report/analysis/m-confusion-matrix.md
date: 23-07-2026
kind: analysis
comments: true
generated: 2026-10-14T14:44:07
---

# Confusion matrix

<p class="doc-meta"><span class="chip chip-analysis">Analysis</span> <span class="chip chip-project">Master</span> <span class="chip chip-date">23-07-2026</span></p>

A table of the [Final model](m-final-model.md)'s answers against the correct answers. Each row is the correct type, each column is the model's answer. Every answer comes from a test where that stay was not used for learning (grouped cross-validation).

| actual \ predicted | building | street | open space | recall |
|---|---:|---:|---:|---:|
| building | 476 | 22 | 33 | **89.6%** |
| street | 86 | 79 | 20 | **42.7%** |
| open space | 86 | 11 | 94 | **49.2%** |

Recall is the share of stays of one type that the model found. For example, 79 of 185 street stays were called street: 42.7%.

- The model finds building stays about **twice** as often as the other two types.
- When it gets a street or open-space stay wrong, it mostly says **building** (46.5% and 45.0% of those stays). It rarely mixes up street and open space (10.8% and 5.8%).
- More street stays were called building (86) than street (79).

On the training data the table looks almost the same (building 89.8%, street 44.3%, open space 49.7%). So overfitting does not explain this pattern.

Why it happens: [Candidate density bias toward building](m-candidate-density-bias.md). How it changes from test set to test set: [Fold difficulty](m-fold-difficulty.md). Answers RQ2 of [Research questions](../notes/m-research-questions.md). Part of [Error analysis](../threads/m-error-analysis.md).


<div class="backlinks" markdown>

**Linked from** [Candidate density bias toward building](m-candidate-density-bias.md) · [Error analysis](../threads/m-error-analysis.md) · [Final model](m-final-model.md) · [RQ2 diagnostics and RQ3 ceiling check](../progress/m-progress-23-07-2026.md) · [Research questions](../notes/m-research-questions.md) · [Tension with the street-space argument](../notes/m-street-space-tension.md) · [Thesis summary](../threads/m-thesis-summary.md)

</div>
