---
source: report/notes/m-boundary-matching-analogy.md
date: 23-07-2026
kind: note
comments: true
generated: 2026-10-14T14:44:07
---

# Candidate density as boundary-matching difficulty

<p class="doc-meta"><span class="chip chip-note">Note</span> <span class="chip chip-project">Master</span> <span class="chip chip-date">23-07-2026</span></p>

GPS research on roads and sidewalks knows a similar problem. Weng et al. (2025) need a special sidewalk-matching method, because a sidewalk is only about 2 m wide, while GPS error between tall buildings reaches 18.4 m (RMS) when standing and up to 32 m across the street when walking. Quddus et al. (2007) report three related problems: point-to-line matching becomes unstable when roads are close together, one matching method gets worse on parallel streets, and at a Y-shaped junction both roads can be almost equally close.

[Candidate density bias toward building](../analysis/m-candidate-density-bias.md) is a similar problem at a larger scale. When many candidates of the same type are packed close together, a small GPS error has more chances to land on a wrong one.

The comparison has a limit. Those papers choose between places of the same kind, for example two roads. Here, the problem is a competition **between types**: streets lose to buildings. The two problems share one cause, candidates packed close together, but they work in different ways.

A subsection of the Discussion in the thesis. Part of [Error analysis](../threads/m-error-analysis.md).


<div class="backlinks" markdown>

**Linked from** [Candidate density bias toward building](../analysis/m-candidate-density-bias.md) · [Discussion citation checks](m-discussion-citation-checks.md) · [Error analysis](../threads/m-error-analysis.md)

</div>
