---
source: report/analysis/m-confusion-matrix.md
date: 23-07-2026
kind: analysis
comments: true
generated: 2026-10-26T20:52:49
---

# Confusion matrix

<p class="doc-meta"><span class="chip chip-analysis">Analysis</span> <span class="chip chip-project">Master</span> <span class="chip chip-date">23-07-2026</span></p>

A table of the [Final model](m-final-model.md)'s answers against the correct answers. Each row is the correct type, each column is the model's answer. Every answer comes from a test where that stay was not used for learning (grouped cross-validation).

| actual \ predicted | building | street | open space | recall |
|---|---:|---:|---:|---:|
| building | 478 | 26 | 27 | **90.0%** |
| street | 76 | 90 | 19 | **48.6%** |
| open space | 97 | 10 | 84 | **44.0%** |

Recall is the share of stays of one type that the model found. For example, 90 of 185 street stays were called street: 48.6%.

- The model finds building stays about **twice** as often as the other two types.
- When it gets a street or open-space stay wrong, it mostly says **building** (41.1% and 50.8% of those stays). It rarely mixes up street and open space (10.3% and 5.2%).
- More open-space stays were called building (97) than open space (84).

On the training data the table looks much the same (building 90.8%, street 52.4%, open space 44.0%). So overfitting does not explain this pattern.

Why it happens for streets: [Candidate density bias toward building](m-candidate-density-bias.md). How it changes from test set to test set: [Fold difficulty](m-fold-difficulty.md). Answers RQ2 of [Research questions](../concepts/m-research-questions.md). Part of [Error analysis](../threads/m-error-analysis.md).


<div class="backlinks" markdown>

**Linked from** [Candidate density bias toward building](m-candidate-density-bias.md) · [Error analysis](../threads/m-error-analysis.md) · [Final model](m-final-model.md) · [Open space in the ground truth](../plans/d-gt-open-space.md) · [RQ2 diagnostics and RQ3 ceiling check](../progress/m-progress-23-07-2026.md) · [Research questions](../concepts/m-research-questions.md) · [Tension with the street-space argument](../concepts/m-street-space-tension.md) · [Thesis summary](../threads/m-thesis-summary.md)

</div>
