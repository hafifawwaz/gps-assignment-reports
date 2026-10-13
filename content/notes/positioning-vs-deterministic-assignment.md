---
source: report/notes/positioning-vs-deterministic-assignment.md
date: 23-07-2026
kind: note
comments: true
generated: 2026-10-13T16:57:34
---

# Positioning against deterministic assignment

<p class="doc-meta"><span class="chip chip-note">Note</span> <span class="chip chip-date">23-07-2026</span></p>

Two deterministic mechanisms from Chapter 2: SMoT tests whether a trajectory segment stays inside a candidate-stop polygon for a minimum time (Alvares et al., 2007), and Wu et al. (2026) assign each GPS point to its nearest entity. Both commit to one entity and carry no confidence.

Wu et al. do define a misclassification probability that depends on GPS error and on closeness to an entity's boundary, but only as an after-the-fact accuracy bound. This framework builds that boundary-and-error logic **into** the assignment and returns a distribution, at grouped CV accuracy 0.716 ± 0.076 ([Final model](../analysis/final-model.md)).

Would a more flexible model do better? RQ3 says no: Random Forest and XGBoost fit closer in-sample (0.762, 0.849 vs 0.721) but generalize worse (0.699, 0.695 vs 0.716) ([ML ceiling check, row level](../analysis/ml-ceiling-row-level.md)). The advantage is complexity matched to what generalizes, while staying interpretable as twelve signed coefficients.

Part of [Chapter 6: Discussion and conclusion](../progress/ch6-discussion.md) (a subsection of the thesis's Discussion). Literature: [Chapter 2: Literature](../progress/ch2-literature.md).


<div class="backlinks" markdown>

**Linked from** [Chapter 2: Literature](../progress/ch2-literature.md) · [Chapter 6: Discussion and conclusion](../progress/ch6-discussion.md) · [Discussion citation checks](discussion-citation-checks.md)

</div>
