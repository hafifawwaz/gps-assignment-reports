---
source: report/notes/street-space-tension.md
date: 23-07-2026
kind: note
comments: true
generated: 2026-10-13T20:05:33
---

# Tension with the street-space argument

<p class="doc-meta"><span class="chip chip-note">Note</span> <span class="chip chip-date">23-07-2026</span></p>

The framework gives streets and open spaces equal standing because Jacobs, Gehl and Whyte treat them as real sites of activity. RQ2 complicates that: building recall 89.6% vs street 42.7% and open space 49.2%, with both losing mostly to building ([Confusion matrix](../analysis/confusion-matrix.md)).

The cause is a calibration artifact, not weaker GPS evidence: `share_type` penalizes candidates with many same-type neighbours, and street candidates are about 1.9× denser than buildings' (mean 13.17 vs 7.09) because streets are drawn as many short segments ([Candidate density bias toward building](../analysis/candidate-density-bias.md)).

Two readings stay open: an artifact of this street layer (fewer, longer segments would narrow it), or a general disadvantage of elongated, repeated entity types under any density-based mechanism. No reviewed source settles it ([Discussion citation checks](discussion-citation-checks.md)); testing other segmentation schemes would ([Future work](future-work.md)).

Part of [Error analysis](../threads/error-analysis.md) (a subsection of the thesis's Discussion).


<div class="backlinks" markdown>

**Linked from** [Candidate density bias toward building](../analysis/candidate-density-bias.md) · [Discussion citation checks](discussion-citation-checks.md) · [Error analysis](../threads/error-analysis.md) · [Future work](future-work.md) · [Motivation](motivation.md) · [Thesis summary](../threads/thesis-summary.md)

</div>
