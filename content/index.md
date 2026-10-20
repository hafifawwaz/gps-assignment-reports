---
hide:
  - navigation
  - toc
---

<div class="hero" markdown>

# Catch-up summary

The master's thesis is complete. Work now runs on three lines:

- **A paper for the journal *Computers, Environment and Urban Systems* (CEUS)**, in drafting. It presents the method from the thesis: for each GPS stay, it gives a probability that the person was in a building, on a street, or in an open space, instead of picking one place. The model learns from 907 stays with known answers from a field survey in Hiroshima. On data it has not seen, it picks the correct type for 71.9% of stays (grouped CV accuracy 0.719 ± 0.032), and it does better there than Random Forest and XGBoost. Its main weakness is mistaking streets and open spaces for buildings. For streets, this comes from how the street map is cut into many short pieces, not from the GPS data itself; for open space, the cause is still open. Start from [Thesis summary](threads/m-thesis-summary.md).
- **A poster for CSIS DAYS 2026**, fairly complete.
- **The doctoral plan.** The goal is an assignment that also knows which stays came before ([Sequence-aware assignment](inbox/d-sequence-aware.md)). The steps: a new review of the key literature, a test in another city, a better way to cut streets into pieces, and toy GPS data with a known true place for every stay. Latest update: [Publications and doctoral plan](progress/d-progress-20-10-2026.md).

The thesis code was checked against the text on 19-10-2026, and every number on this site comes from the checked pipeline ([Thesis bug fixes and adopted rerun](inbox/thesis-bug-fix.md)).


</div>

<div class="home-columns" markdown>

<div class="home-col" markdown>

## [Threads](threads/index.md) { .home-section }

<p class="section-blurb">Hubs by theme: the thesis summary, then one list of notes per theme.</p>

- [Thesis summary](threads/m-thesis-summary.md)
- [Problem and positioning](threads/m-problem-and-positioning.md)
- [Outlook](threads/m-outlook.md)
- [Ground truth data](threads/m-ground-truth-data.md)
- [Error analysis](threads/m-error-analysis.md)

[All 8](threads/index.md){ .more }

</div>

<div class="home-col" markdown>

## [Progress](progress/index.md) { .home-section }

<p class="section-blurb">Dated updates for sensei, and slide exports.</p>

- [Publications and doctoral plan](progress/d-progress-20-10-2026.md)
- [PhD interview slides](progress/m-phd-interview-slides.md) <span class="chip chip-pdf">PDF</span>
- [Does downsampling matter?](progress/m-progress-29-07-2026.md)
- [RQ2 diagnostics and RQ3 ceiling check](progress/m-progress-23-07-2026.md)
- [RQ1 rebuilt with grouped CV](progress/m-progress-21-07-2026.md)

[All 8](progress/index.md){ .more }

</div>

<div class="home-col" markdown>

## [Notes](notes/index.md) { .home-section }

<p class="section-blurb">Small pieces of progress: method, data, interpretation, discussion.</p>

- [Glossary](notes/glossary.md)
- [Study area](notes/m-study-area.md)
- [Spatial entity layers](notes/m-spatial-entity-layers.md)
- [Research questions](notes/m-research-questions.md)
- [Overfitting signature](notes/m-overfitting-signature.md)

[All 34](notes/index.md){ .more }

</div>

<div class="home-col" markdown>

## [Analysis](analysis/index.md) { .home-section }

<p class="section-blurb">Raw analysis output: tables, numbers and diagnostics.</p>

- [Raw-density refit](analysis/m-raw-density-refit.md)
- [Raw-density alpha profile](analysis/m-raw-density-alpha-profile.md)
- [Downsampling shrinks the candidate search area](analysis/m-candidate-search-area.md)
- [Sigma in tree importance](analysis/m-sigma-tree-importance.md)
- [ML ceiling check, row level](analysis/m-ml-ceiling-row-level.md)

[All 25](analysis/index.md){ .more }

</div>

</div>

<div class="home-col home-below" markdown>

## [Inbox](inbox/index.md) { .home-section }

<p class="section-blurb">Open items not yet settled with sensei.</p>

- [Thesis bug fixes and adopted rerun](inbox/thesis-bug-fix.md)
- [Transferability](inbox/d-transferability.md)
- [GPS toy data](inbox/d-toy-data.md)
- [Street segmentation](inbox/d-street-segmentation.md)
- [Sequence-aware assignment](inbox/d-sequence-aware.md)

[All 9](inbox/index.md){ .more }

</div>

<div class="about" markdown>

## About this research

**Hafiyyan Hilmy Fawwaz** · Urban Transportation and Planning Lab, Hiroshima University

A GPS staypoint rarely tells you which place a person actually visited: positional error is often larger than the gap between a building, the street in front of it and the open space beside it. This research builds a probabilistic framework that assigns each staypoint to an urban spatial entity (building, street or open space) under explicit positional uncertainty, instead of snapping it to the nearest one.

Dates are written `DD-MM-YYYY`.

</div>
