---
source: report/threads/thesis-summary.md
date: 13-10-2026
kind: thread
comments: true
generated: 2026-10-13T20:06:43
---

# Thesis summary

<p class="doc-meta"><span class="chip chip-thread">Thread</span> <span class="chip chip-date">13-10-2026</span></p>

**Beyond the Building: A Probabilistic Framework for GPS Assignment Under Positional Uncertainty**

A GPS stay cluster rarely shows which place a person visited: positional error is often larger than the gap between a building, the street in front of it and the open space beside it. This thesis assigns each stay cluster a **probability over buildings, streets and open spaces** instead of snapping it to the nearest entity, and calibrates that assignment against a controlled field-survey ground truth.

## Why and what

- Why deterministic assignment falls short: [Motivation](../notes/motivation.md)
- What the thesis asks: [Research questions](../notes/research-questions.md)

## Threads

The notes are grouped by theme rather than by chapter:

1. [Problem and positioning](problem-and-positioning.md): motivation, research questions, where the framework sits against prior work
2. [Ground truth data](ground-truth-data.md): Hiroshima entity layers and the 907-stay ground truth
3. [Assignment framework](assignment-framework.md): candidates, four scores, a type-level logit
4. [Calibration](calibration.md): RQ1, from the base model to the final 12-parameter model
5. [Error analysis](error-analysis.md): RQ2, where the model fails and why street loses to building
6. [Complexity and transfer](complexity-and-transfer.md): RQ3, tree models, overfitting, downsampling
7. [Outlook](outlook.md): contributions, limitations, future work

## Where it stands

- Final model: 12 parameters, grouped 5-fold CV accuracy **0.716 ± 0.076** ([Final model](../analysis/final-model.md)).
- Building recall 89.6% vs. street 42.7% and open space 49.2%; both lose mostly to building ([Confusion matrix](../analysis/confusion-matrix.md), [Candidate density bias toward building](../analysis/candidate-density-bias.md)).
- The logit beats Random Forest and XGBoost under grouped CV despite losing to them in-sample ([ML ceiling check, row level](../analysis/ml-ceiling-row-level.md)).
- The thesis is complete; the questions that were open in the reports are settled in the final text ([Final model](../analysis/final-model.md), [Ground truth cleaning](../notes/ground-truth-cleaning.md), [Tension with the street-space argument](../notes/street-space-tension.md)).

## Dated updates

[MNL model development](../progress/progress-19-07-2026.md) · [ML baseline](../progress/progress-20-07-2026.md) · [RQ1 rebuilt with grouped CV](../progress/progress-21-07-2026.md) · [RQ2 diagnostics and RQ3 ceiling check](../progress/progress-23-07-2026.md) · [Does downsampling matter?](../progress/progress-29-07-2026.md)


<div class="backlinks" markdown>

**Linked from** [Assignment framework](assignment-framework.md) · [Calibration](calibration.md) · [Complexity and transfer](complexity-and-transfer.md) · [Error analysis](error-analysis.md) · [Ground truth data](ground-truth-data.md) · [Outlook](outlook.md) · [Problem and positioning](problem-and-positioning.md)

</div>
