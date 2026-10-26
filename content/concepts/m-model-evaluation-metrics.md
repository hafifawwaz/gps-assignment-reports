---
source: report/concepts/m-model-evaluation-metrics.md
date: 19-07-2026
kind: concept
comments: true
generated: 2026-10-26T20:41:14
---

# Model evaluation metrics

<p class="doc-meta"><span class="chip chip-concept">Concept</span> <span class="chip chip-project">Master</span> <span class="chip chip-date">19-07-2026</span></p>

The numbers used to compare models. Longer explanations are in the [Glossary](glossary.md).

| Metric | Meaning |
|---|---|
| LL(0) | Log-likelihood (how well the probabilities fit the correct answers) when every candidate gets the same probability |
| LL(C) | Log-likelihood of a simple baseline: one constant per type, which only knows how common each type is |
| LL(b) | Log-likelihood of the fitted model. Closer to 0 is better |
| ρ² vs LL(C) | How much better the model is than the simple baseline. Negative means worse than the baseline |
| Accuracy | The share of stays where the most likely type is the correct one |
| Condition number | How stable the fit is. Large values mean the single weights cannot be trusted |
| VIF | For each input, how much it overlaps with the other inputs. Above 10 is the usual warning line |

ρ² vs LL(C) cannot compare different search distances (`R_buffer`), because the baseline LL(C) itself changes when the list of candidates changes ([R_buffer: 10 m vs 15 m](../analysis/m-r-buffer-10m-vs-15m.md)). All cross-validation numbers use [Grouped cross-validation](m-grouped-cross-validation.md).

Part of [Calibration](../threads/m-calibration.md).


<div class="backlinks" markdown>

**Linked from** [Calibration](../threads/m-calibration.md) · [R_buffer: 10 m vs 15 m](../analysis/m-r-buffer-10m-vs-15m.md)

</div>
