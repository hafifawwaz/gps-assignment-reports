---
source: report/plans/d-nested-probabilities.md
date: 26-10-2026
kind: plan
comments: true
generated: 2026-11-06T11:37:20
---

# Nested probabilities

<p class="doc-meta"><span class="chip chip-plan">Plan</span> <span class="chip chip-lane">On-going</span> <span class="chip chip-project">Doctoral</span> <span class="chip chip-date">26-10-2026</span></p>

New work from the meeting on 20-10-2026 ([Publications and doctoral plan](../progress/d-progress-20-10-2026.md)). Builds on [Assignment framework](../threads/m-assignment-framework.md).

**Goal:** two levels of probability for each stay.

1. **Which type?** How likely the person is in a building, on a street, or in an open space. The master's model gives this level.
2. **Which one?** Which building, which street, which open space. This level is computed separately for each type, so within one type the probabilities add up to 100%.

Example: a stay has three candidate buildings, and level 1 gives building 70%. Level 2 then shares 100% among those three buildings.

This is the first extension named at the group meeting on 26-10-2026: identify which building, which street, or which open space.

## Steps

All three types are tried together first. If that is too hard, one type at a time, to see which works best.

1. **Labels for level 2.** The ground truth (GT) only says the type of each stay, not the exact building, street or open space. A script suggests one entity for each physical stop (one place, recorded by up to five phones). For buildings it compares the place name in the survey form with the building names in the map. Otherwise it takes the entity closest to the stay. Each suggestion is then checked by hand on a map. One stop can have more than one correct entity, for example a mall made of several building outlines, or a street cut into several pieces.
2. **Level 2 from the current model.** The master's model already gives every candidate a score. Inside one type, these scores already split 100% among that type's candidates, so level 2 needs no new model at first. The check: how often the true entity gets the highest share, and whether that beats simply taking the nearest entity.
3. **A new fit, only if step 2 is weak.** Train the model on the exact entities as well, or use a nested logit (a model that first picks the type, then the entity inside it). The type accuracy (0.718) must not drop.

Part of [Doctoral plan](../threads/d-doctoral-plan.md).


<div class="backlinks" markdown>

**Linked from** [Doctoral plan](../threads/d-doctoral-plan.md) · [Publications and doctoral plan](../progress/d-progress-20-10-2026.md)

</div>
