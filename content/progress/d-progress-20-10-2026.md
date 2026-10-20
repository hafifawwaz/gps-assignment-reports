---
source: report/progress/d-progress-20-10-2026.md
date: 20-10-2026
kind: progress
comments: true
generated: 2026-10-20T15:44:29
---

# Publications and doctoral plan

<p class="doc-meta"><span class="chip chip-progress">Progress</span> <span class="chip chip-project">Doctoral</span> <span class="chip chip-date">20-10-2026</span></p>

The update for the meeting with sensei on 20-10-2026. It gathers the open items in the inbox, listed in [plan](../inbox/plan.md): the two outputs from the master's thesis, a code check of the thesis, and the steps toward the doctoral goal.

## Outputs from the master's thesis

[thesis publication](../inbox/thesis-publication.md). Both outputs use only the thesis content, so all the material already exists.

- **CSIS Days 2026 poster.** Fairly complete. Sensei has not seen it yet.
- **CEUS paper** (*Computers, Environment and Urban Systems*). A methodological paper, written from the thesis content.
- Both use the final numbers: 11 parameters, α = 2.764, grouped CV accuracy 0.719 ± 0.032 ([Final model](../analysis/m-final-model.md)).

## Code check and adopted rerun

[Thesis bug fixes and adopted rerun](../inbox/thesis-bug-fix.md). A check of the code against the thesis on 19-10-2026 found six problems: two in the scores and four in the ground truth cleaning. The fixed pipeline (run C) is now the official one, and the thesis, paper, poster, abstract and slides use its numbers. The old versions are archived.

- Accuracy on unseen data does not change significantly (0.716 → 0.719; McNemar p = 0.67 on the 895 shared stays).
- Recall moves from open space (0.492 → 0.440) to street (0.427 → 0.486). Building barely moves (0.896 → 0.900).
- The final model loses the `f_distribution × share_type` term (VIF 10.4, just above the limit of 10) and has 11 parameters instead of 12.
- Most thesis decisions hold: 10 m search distance, no ASC, one shared direction weight, the simple model beats Random Forest and XGBoost, downsampling does no harm.

Points for sensei:

1. α is bounded from below only. The fit is almost flat above 2.2, and the model uses the inside best point, 2.764.
2. Two tests close to their limits decide the model shape: VIF 10.4 against 10, and p = 0.054 against 0.05.
3. The ASC raises accuracy on unseen data, so the case against it rests on its copy of the street direction score (r = 0.94) and the sign flip that follows ([Model 5: alternative-specific constants (rejected)](../analysis/m-model-5-asc-rejected.md)).
4. Crowded street candidates explain the street errors. The open-space errors still have no cause.
5. Sensei's review of the adoption itself.

## Doctoral direction

The end goal is [Sequence-aware assignment](../inbox/d-sequence-aware.md): an assignment that knows which stays came before.

**Milestones**

- [Comprehensive literature review](../inbox/d-comprehensive-litrev.md). Re-read the key papers the research is built on, some of them old, and search for newer work on the same ideas.
- [Transferability](../inbox/d-transferability.md). Show that the framework works on other data. Sensei prefers another city before MILES. The open question is ground truth for that city; the most likely source is data from the University of Tokyo.

**Supporting work**

- [Street segmentation](../inbox/d-street-segmentation.md). Find the most robust way to cut streets into pieces. In the current map the road surface for cars counts as open space, so a person on a sidewalk often lands in open space: for street stays, the GPS point closest to the stay's centre lies in open space 46% of the time and in a street piece 28% of the time. With real street directions, movement inside a stay follows the street about as much as random movement would.
- [GPS toy data](../inbox/d-toy-data.md). A GPS generator with a known true place for every stay, so each source of error can be switched on alone. Two programs: one makes people and their activity chains, the other turns them into GPS points in the MILES format. The literature search ([Consensus Report](../inbox/d-toy-data-consensus.md)) supports the design. Its weakest part is the stay-level offset in the error model, so the offset stays a setting with a wide range.

## Other topics

- Group meeting proposal.
- Seat arrangement.
