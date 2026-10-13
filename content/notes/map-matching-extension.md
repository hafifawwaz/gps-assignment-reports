---
source: report/notes/map-matching-extension.md
date: 23-07-2026
kind: note
comments: true
generated: 2026-10-13T20:30:42
---

# Extending map matching to stationary stays

<p class="doc-meta"><span class="chip chip-note">Note</span> <span class="chip chip-date">23-07-2026</span></p>

Bierlaire et al. (2013), Chen and Bierlaire (2015) and Kempinska et al. (2016) all generate probabilities from a **chain**: dependency between adjacent GPS points, a first-order Markov structure, or a particle filter stepping through time. A single stationary cluster has no upstream point, previous timestep or adjacent segment.

What carries over is the commitment to several plausible entities with likelihoods. What does not is the mechanism: this framework scores properties **intrinsic to one static cluster** ([Framework overview](framework-overview.md)). Quddus et al. (2007) support that this substitution is necessary: fix-by-fix matching without trajectory history risks selecting the wrong link, and off-network cases such as car parks are named as an unresolved limitation.

Part of [Problem and positioning](../threads/problem-and-positioning.md) (a subsection of the thesis's Discussion). Motivated in [Motivation](motivation.md).


<div class="backlinks" markdown>

**Linked from** [Discussion citation checks](discussion-citation-checks.md) · [Motivation](motivation.md) · [Problem and positioning](../threads/problem-and-positioning.md)

</div>
