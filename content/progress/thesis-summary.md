---
source: report/progress/thesis-summary.md
date: 13-10-2026
kind: progress
comments: true
generated: 2026-10-13T17:38:15
---

# Thesis summary

<p class="doc-meta"><span class="chip chip-progress">Progress</span> <span class="chip chip-date">13-10-2026</span></p>

**Beyond the Building: A Probabilistic Framework for GPS Assignment Under Positional Uncertainty**

A GPS stay cluster rarely tells us which place a person visited: positional error is often larger than the gap between a building, the street in front of it and the open space beside it. This thesis assigns each stay cluster a **probability over buildings, streets and open spaces** instead of snapping it to the nearest entity, and calibrates that assignment against a controlled field-survey ground truth.

## Why and what

- Why deterministic assignment falls short: [Motivation](../notes/motivation.md)
- What the thesis asks: [Research questions](../notes/research-questions.md)

## The thesis, chapter by chapter

1. [Introduction](ch1-introduction.md): motivation, objective, research questions
2. [Literature](ch2-literature.md): where the framework sits against prior work
3. [Data and ground truth](ch3-data.md): Hiroshima entity layers and the 907-stay ground truth
4. [Framework](ch4-framework.md): candidates, four scores, a type-level logit
5. [Results](ch5-results.md): calibration (RQ1), validation (RQ2), complexity (RQ3)
6. [Discussion and conclusion](ch6-discussion.md): positioning, tension, contributions, limits

## Where it stands

- Final model: 12 parameters, grouped 5-fold CV accuracy **0.716 ± 0.076** ([Final model](../analysis/final-model.md)).
- Building recall 89.6% vs. street 42.7% and open space 49.2%; both lose mostly to building ([Confusion matrix](../analysis/confusion-matrix.md), [Candidate density bias toward building](../analysis/candidate-density-bias.md)).
- The logit beats Random Forest and XGBoost under grouped CV despite losing to them in-sample ([ML ceiling check, row level](../analysis/ml-ceiling-row-level.md)).
- The thesis is complete; the questions that were open in the reports are settled in the final text ([Final model](../analysis/final-model.md), [Ground truth cleaning](../notes/ground-truth-cleaning.md), [Chapter 6: Discussion and conclusion](ch6-discussion.md)).

## Dated updates

[MNL model development](progress-19-07-2026.md) · [ML baseline](progress-20-07-2026.md) · [RQ1 rebuilt with grouped CV](progress-21-07-2026.md) · [RQ2 diagnostics and RQ3 ceiling check](progress-23-07-2026.md) · [Does downsampling matter?](progress-29-07-2026.md)


<div class="backlinks" markdown>

**Linked from** [Chapter 1: Introduction](ch1-introduction.md) · [Chapter 2: Literature](ch2-literature.md) · [Chapter 3: Data and ground truth](ch3-data.md) · [Chapter 4: Framework](ch4-framework.md) · [Chapter 5: Results](ch5-results.md) · [Chapter 6: Discussion and conclusion](ch6-discussion.md)

</div>
