---
source: report/notes/m-map-matching-extension.md
date: 23-07-2026
kind: note
comments: true
generated: 2026-10-14T14:44:07
---

# Extending map matching to stationary stays

<p class="doc-meta"><span class="chip chip-note">Note</span> <span class="chip chip-project">Master</span> <span class="chip chip-date">23-07-2026</span></p>

Map matching finds which road a moving person is on. Bierlaire et al. (2013), Chen and Bierlaire (2015) and Kempinska et al. (2016) all give probabilities, and they all build them from a **chain** of points: each point depends on the point before it, or the method steps forward through time (a Markov chain or a particle filter). A person standing still has no chain. There is no earlier point on a route, no previous step and no next road piece.

One idea still works: keep several possible places, each with a probability. The way of computing those probabilities has to change. This method uses only what one stay shows by itself: how its points spread, how long they stay, and how they move ([Framework overview](m-framework-overview.md)).

Quddus et al. (2007) support this change. They note that matching point by point, without the track history, often picks the wrong road. They also name places off the road network, such as car parks, as a problem that map matching has not solved.

A subsection of the Discussion in the thesis. Part of [Problem and positioning](../threads/m-problem-and-positioning.md). The starting point: [Motivation](m-motivation.md).


<div class="backlinks" markdown>

**Linked from** [Discussion citation checks](m-discussion-citation-checks.md) · [Motivation](m-motivation.md) · [Problem and positioning](../threads/m-problem-and-positioning.md)

</div>
