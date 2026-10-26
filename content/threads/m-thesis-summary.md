---
source: report/threads/m-thesis-summary.md
date: 05-08-2026
kind: thread
comments: true
generated: 2026-10-26T20:41:14
---

# Thesis summary

<p class="doc-meta"><span class="chip chip-thread">Thread</span> <span class="chip chip-project">Master</span> <span class="chip chip-date">05-08-2026</span></p>

**Beyond the Building: A Probabilistic Framework for GPS Assignment Under Positional Uncertainty**

When a phone records GPS points while someone stays in one place, the points do not tell you exactly where the person was. In a city, the GPS error is often larger than the distance between a building, the street in front of it, and the open space next to it.

Most studies solve this by picking the nearest building. This thesis does something different. For each stay, it gives a **probability for building, street and open space**, so the uncertainty stays visible. The model learns how to do this from a field survey in Hiroshima, where participants recorded where they really were.

New to the terms? Start with the [Glossary](../concepts/glossary.md).

## Why and what

- Why "nearest building" is not good enough: [Motivation](../concepts/m-motivation.md)
- The three research questions: [Research questions](../concepts/m-research-questions.md)

## Threads

The notes are grouped by theme, not by thesis chapter:

1. [Problem and positioning](m-problem-and-positioning.md): the problem, the research questions, and how this work compares with earlier methods
2. [Ground truth data](m-ground-truth-data.md): the Hiroshima map layers and the 907 stays with known answers
3. [Assignment framework](m-assignment-framework.md): how the method works: candidates, four scores, and a model that turns scores into probabilities
4. [Calibration](m-calibration.md): research question 1, how the final 11-parameter model was built step by step
5. [Error analysis](m-error-analysis.md): research question 2, where the model makes mistakes and why streets are often mistaken for buildings
6. [Complexity and transfer](m-complexity-and-transfer.md): research question 3, whether more complex models help, and whether the model will work on new data
7. [Outlook](m-outlook.md): what the thesis contributes, its limits, and next steps

## Where it stands

- The final model has 11 parameters. On data it had not seen, it picks the correct type for **71.9% of stays (± 3.2%)**, written as grouped CV accuracy 0.719 ± 0.032 ([Final model](../analysis/m-final-model.md)).
- It finds 90.0% of building stays, but only 48.6% of street stays and 44.0% of open-space stays. When it gets streets or open spaces wrong, it usually says "building". For streets, the reason is how the street map is cut into pieces; for open space, the reason is still open ([Confusion matrix](../analysis/m-confusion-matrix.md), [Candidate density bias toward building](../analysis/m-candidate-density-bias.md)).
- Random Forest and XGBoost fit the training data better, but on unseen data this simpler model does better ([ML ceiling check, row level](../analysis/m-ml-ceiling-row-level.md)).
- The thesis is complete. The questions that were still open in these notes are answered in the final text ([Final model](../analysis/m-final-model.md), [Ground truth cleaning](../concepts/m-ground-truth-cleaning.md), [Tension with the street-space argument](../concepts/m-street-space-tension.md)).

## Dated updates

[MNL model development](../progress/m-progress-19-07-2026.md) · [ML baseline](../progress/m-progress-20-07-2026.md) · [RQ1 rebuilt with grouped CV](../progress/m-progress-21-07-2026.md) · [RQ2 diagnostics and RQ3 ceiling check](../progress/m-progress-23-07-2026.md) · [Does downsampling matter?](../progress/m-progress-29-07-2026.md)


<div class="backlinks" markdown>

**Linked from** [Assignment framework](m-assignment-framework.md) · [Calibration](m-calibration.md) · [Complexity and transfer](m-complexity-and-transfer.md) · [Doctoral plan](d-doctoral-plan.md) · [Error analysis](m-error-analysis.md) · [Glossary](../concepts/glossary.md) · [Ground truth data](m-ground-truth-data.md) · [Outlook](m-outlook.md) · [Problem and positioning](m-problem-and-positioning.md)

</div>
