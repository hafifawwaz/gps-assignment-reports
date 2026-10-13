---
source: report/analysis/confusion-matrix.md
date: 23-07-2026
kind: analysis
comments: true
generated: 2026-10-13T16:57:34
---

# Confusion matrix

<p class="doc-meta"><span class="chip chip-analysis">Analysis</span> <span class="chip chip-date">23-07-2026</span></p>

[Final model](final-model.md), out-of-sample: each stay's prediction comes from the grouped-CV fold where it was held out.

| actual \ predicted | building | street | open space | recall |
|---|---:|---:|---:|---:|
| building | 476 | 22 | 33 | **89.6%** |
| street | 86 | 79 | 20 | **42.7%** |
| open space | 86 | 11 | 94 | **49.2%** |

- Building recall is about **double** the other two.
- Both street and open space are misclassified **as building** (46.5%, 45.0%) far more than as each other (10.8%, 5.8%).
- More street stays go to building (86) than are classified as street (79).

The in-sample matrix is nearly identical (building 89.8%, street 44.3%, open space 49.7%), so this is not an overfitting effect.

Why: [Candidate density bias toward building](candidate-density-bias.md). Fold-to-fold behaviour: [Fold difficulty](fold-difficulty.md). Answers RQ2 of [Research questions](../notes/research-questions.md). Part of [Chapter 5: Results](../progress/ch5-results.md).


<div class="backlinks" markdown>

**Linked from** [Candidate density bias toward building](candidate-density-bias.md) · [Chapter 5: Results](../progress/ch5-results.md) · [Final model](final-model.md) · [RQ2 diagnostics and RQ3 ceiling check](../progress/progress-23-07-2026.md) · [Research questions](../notes/research-questions.md) · [Tension with the street-space argument](../notes/street-space-tension.md) · [Thesis summary](../progress/thesis-summary.md)

</div>
