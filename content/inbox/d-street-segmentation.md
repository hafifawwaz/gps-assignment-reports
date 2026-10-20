---
source: report/inbox/d-street-segmentation.md
date: 16-10-2026
kind: inbox
comments: true
generated: 2026-10-20T16:29:09
---

# Street segmentation

<p class="doc-meta"><span class="chip chip-inbox">Inbox</span> <span class="chip chip-project">Doctoral</span> <span class="chip chip-date">16-10-2026</span></p>

!!! question "For discussion"
    Rough draft and open questions. Not yet reviewed.

Supporting work for [Sequence-aware assignment](d-sequence-aware.md).

A flaw found in the master's thesis: how streets are cut into segments affects the assignment. See [Limitations](../notes/m-limitations.md).

**Goal:** exploratory research to find the most robust way to segment streets for this kind of assignment work.

## What the street map is now

- Streets come from the MAPPLE pedestrian network: each link (a piece of path between two points of the network) is widened to its real width. There are 33,982 links. 68% of them are straight lines between two points, and only about 5% bend clearly.
- The road surface for cars is **not** a street in this map. It is open space on purpose, because it is not a place for walking. This is the main reason the segmentation needs to be rethought.
- Because of this, a person standing on a sidewalk is often recorded inside open space. For the stays labelled "Street", the GPS point closest to the stay's centre lies in open space 46% of the time, and inside a street piece only 28% of the time.
- Open space is what is left after buildings and streets are removed. Rivers are not part of it.

## Direction score bug

The direction score (`f_directional`) in the thesis never used the real direction of a street: every street was treated as pointing east (found 19-10-2026). The fixed code takes each street's direction from its centerline. So the thesis results say nothing yet about whether shorter or longer street pieces help the direction score.

First result with the real direction (experimental rerun, 19-10-2026): the small movements inside a stay follow the street direction about as much as random movement would. People standing on a street even move slightly less along the street than people near it (0.61 against 0.63, where 0.64 means random). In the refitted models, the direction score gets a clear weight when all three types share one weight (+3.43, t = 6.7). With one weight per type, the street weight is negative (about -5), so movement along a street counts against that street. A raw signal close to random and a street weight that points the wrong way make the direction score weak evidence at the moment, whatever the segmentation.


<div class="backlinks" markdown>

**Linked from** [Publications and doctoral plan](../progress/d-progress-20-10-2026.md) · [Sequence-aware assignment](d-sequence-aware.md) · [Thesis bug fixes and adopted rerun](thesis-bug-fix.md) · [d plan](d-plan.md)

</div>
