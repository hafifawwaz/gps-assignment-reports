---
hide:
  - navigation
  - toc
---

<div class="hero" markdown>

# Catch-up summary

The master's thesis is complete. Work now runs on three lines:

- **A paper for the journal *Computers, Environment and Urban Systems* (CEUS)**, in drafting. It presents the method from the thesis: for each GPS stay, it gives a probability that the person was in a building, on a street, or in an open space, instead of picking one place. The model learns from 907 stays with known answers from a field survey in Hiroshima. On data it has not seen, it picks the correct type for 71.9% of stays (grouped CV accuracy 0.719 ± 0.032), and it does better there than Random Forest and XGBoost. Its main weakness is mistaking streets and open spaces for buildings. For streets, this comes from how the street map is cut into many short pieces, not from the GPS data itself; for open space, the cause is still open. Start from [Thesis summary](threads/m-thesis-summary.md). After the meeting on 20-10-2026 the paper changes to one column and gets map examples: an outdoor and an indoor cluster, and one stay shown through every step ([CEUS paper](plans/m-ceus-paper.md)).
- **CSIS DAYS 2026**: a poster, approved by sensei on 20-10-2026, and slides for the talk. The QR code on the poster opens the slides ([CSIS DAYS 2026](plans/csisdays-2026.md)).
- **The doctoral plan** ([Doctoral plan](threads/d-doctoral-plan.md)). The goal is an assignment that also knows which stays came before ([Sequence-aware assignment](plans/d-sequence-aware.md)). The meeting on 20-10-2026 added three new items, now in the inbox: the indoor and outdoor split across the four seasons, a second level of probability that picks which building, street or open space, and real open spaces in the ground truth. A new review of the key literature, a test in another city and a better way to cut streets into pieces are on hold. The toy GPS data idea was dropped. Latest update: [Publications and doctoral plan](progress/d-progress-20-10-2026.md).

The board below shows every work item by status: **Inbox** (not started, or still to discuss with sensei), **On-going** and **On-hold**. A finished item moves to **Done** (shown on the Plans page), and its results move into the notes.

The thesis code was checked against the text on 19-10-2026, and every number on this site comes from the checked pipeline. The check is settled and its notes are archived.


</div>

<div class="home-board" markdown>

<div class="home-col" markdown>

## [Inbox](plans/index.md) { .home-section }

<p class="empty">Nothing yet.</p>

</div>

<div class="home-col" markdown>

## [On-going](plans/index.md) { .home-section }

- [CEUS paper](plans/m-ceus-paper.md)
- [Open space in the ground truth](plans/d-gt-open-space.md)

</div>

<div class="home-col" markdown>

## [On-hold](plans/index.md) { .home-section }

- [Comprehensive literature review](plans/d-comprehensive-litrev.md)
- [Transferability](plans/d-transferability.md)
- [Street segmentation](plans/d-street-segmentation.md)
- [Seasonal variance](plans/d-seasonal-variance.md)
- [Sequence-aware assignment](plans/d-sequence-aware.md)
- [Nested probabilities](plans/d-nested-probabilities.md)

</div>

</div>

<div class="home-columns" markdown>

<div class="home-col" markdown>

## [Threads](threads/index.md) { .home-section }

<p class="section-blurb">Hubs by theme: the thesis summary and the doctoral plan, then one list of notes per theme.</p>

- [Doctoral plan](threads/d-doctoral-plan.md)
- [Thesis summary](threads/m-thesis-summary.md)
- [Problem and positioning](threads/m-problem-and-positioning.md)
- [Outlook](threads/m-outlook.md)
- [Ground truth data](threads/m-ground-truth-data.md)

[All 9](threads/index.md){ .more }

</div>

<div class="home-col" markdown>

## [Progress](progress/index.md) { .home-section }

<p class="section-blurb">Dated updates for sensei, and slide exports.</p>

- [Publications and doctoral plan](progress/d-progress-20-10-2026.md)
- [PhD interview slides](progress/m-phd-interview-slides.md) <span class="chip chip-pdf">PDF</span>
- [Does downsampling matter?](progress/m-progress-29-07-2026.md)
- [RQ2 diagnostics and RQ3 ceiling check](progress/m-progress-23-07-2026.md)
- [RQ1 rebuilt with grouped CV](progress/m-progress-21-07-2026.md)

[All 7](progress/index.md){ .more }

</div>

<div class="home-col" markdown>

## [Concepts](concepts/index.md) { .home-section }

<p class="section-blurb">Settled pieces of the work: method, data, interpretation, discussion.</p>

- [Glossary](concepts/glossary.md)
- [Study area](concepts/m-study-area.md)
- [Spatial entity layers](concepts/m-spatial-entity-layers.md)
- [Research questions](concepts/m-research-questions.md)
- [Overfitting signature](concepts/m-overfitting-signature.md)

[All 34](concepts/index.md){ .more }

</div>

<div class="home-col" markdown>

## [Analysis](analysis/index.md) { .home-section }

<p class="section-blurb">Raw analysis output: tables, numbers and diagnostics.</p>

- [CSIS DAYS 2026 slides](analysis/m-csis-slide.md) <span class="chip chip-pdf">PDF</span>
- [CSIS DAYS 2026 poster](analysis/m-csis-poster.md) <span class="chip chip-pdf">PDF</span>
- [Raw-density refit](analysis/m-raw-density-refit.md)
- [Raw-density alpha profile](analysis/m-raw-density-alpha-profile.md)
- [Downsampling shrinks the candidate search area](analysis/m-candidate-search-area.md)

[All 27](analysis/index.md){ .more }

</div>

</div>

<div class="about" markdown>

## About this research

**Hafiyyan Hilmy Fawwaz** · Urban Transportation and Planning Lab, Hiroshima University

A GPS staypoint rarely tells you which place a person actually visited: positional error is often larger than the gap between a building, the street in front of it and the open space beside it. This research builds a probabilistic framework that assigns each staypoint to an urban spatial entity (building, street or open space) under explicit positional uncertainty, instead of snapping it to the nearest one.

Dates are written `DD-MM-YYYY`.

</div>
