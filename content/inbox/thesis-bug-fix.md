---
source: report/inbox/thesis-bug-fix.md
date: 19-10-2026
kind: inbox
comments: true
generated: 2026-10-20T15:44:29
---

# Thesis bug fixes and adopted rerun

<p class="doc-meta"><span class="chip chip-inbox">Inbox</span> <span class="chip chip-project">Master</span> <span class="chip chip-date">19-10-2026</span></p>

!!! question "For discussion"
    Rough draft and open questions. Not yet reviewed.

Found six bugs that change the thesis numbers: 
- two in the scores and 
- four in the ground truth (GT) cleaning. 
The GT is the set of stays with known correct answers from the field survey. Terms: [Glossary](../notes/glossary.md). Process log: `analysis/docs/19-10-2026.md`.

## Status

- **Adopted on 19-10-2026.** The analysis code runs the fixes by default, and the official pipeline gives the same results as run C.
- **Open:** sensei has not reviewed the change. The points for that meeting close this note.

## The six bugs

### Scores

**1. Direction score (`f_directional`).** This score checks whether a person's small movements during a stay follow the street ([f_directional](../notes/m-f-directional.md)). The code read each street's direction from its polygon outline. An outline starts and ends at the same point, so the code gave all 33,982 streets the direction "east", and the model learned nothing about real street directions. The fix reads each street's direction from its MAPPLE center line (`analysis/data/processed/centerline.parquet`), matched by map tile and link number. It takes the length-weighted mean direction of the line's pieces, where a direction and its reverse count as one. For the 68% of links that are straight lines between two points, this equals the direction from the first point to the last.

**2. Time-in-place score (`f_temporal`).** This score finds the longest unbroken stretch of a stay within 10 m of a place, as a share of the whole stay ([f_temporal](../notes/m-f-temporal.md)). A person may step outside for up to 5 minutes, and that time counts toward the stretch. The old code compared each gap between two neighbouring points with 5 minutes, so a long chain of short gaps could not break a stretch. The fixed code measures the time outside from the last point within 10 m. A stretch breaks at a GPS point outside that comes more than 5 minutes after that last point. A stretch of time with no GPS points cannot break it, because missing points give no sign that the person left. On the thesis GT, the fix changes 8.6% of the `f_temporal` values (mean 0.283 to 0.241).

Example: a 60-minute stay is within 10 m from minute 0 to 20, outside for 3 minutes, back from 23 to 40, outside for 10 minutes, and back from 50 to 60. The first stretch runs from 0 to 40 with the 3 minutes outside included, so `f_temporal` = 40/60 ≈ 0.67. `f_distribution` adds up all time within 10 m: 47/60 ≈ 0.78.

The thesis text said "within an entity boundary". The code counts every point within 10 m of the place (`R_buffer`), and Section 4.2.3 of the thesis says so after the fix.

A third score problem left the thesis numbers alone. Newer pandas versions read times in microseconds, while the code assumed nanoseconds and turned the 5-minute limit into 83 hours. The stored thesis data uses nanoseconds. The fixed code computes seconds in a way that works for both units.

### Ground truth cleaning

A stay-device entry is one phone's record of one stop. Each participant carried three phones (four or five in six sessions), so most stops give three entries ([Ground truth cleaning](../notes/m-ground-truth-cleaning.md)).

**3. Two-day session.** The code gave each session one date. Session P ran on 13 and 14 June, so the cleaning step searched stops 7, 12 and 16 on 13 June and found no GPS points. On 14 June the phones recorded 12 to 143 points per stop. The fix dates each stop by the day on which the session's GPS covers its time window. It brings back 9 entries.

**4. Wrong time correction (Session P stop 15).** The form says 9:12 to 21:25. A manual correction changed the end to 09:25, a time with no GPS data. The participant sent the form at 21:26 on 13 June, between stop 14 (ended 21:00) and stop 11 (started 21:29). The phones recorded 66 to 439 points between 21:12 and 21:25. The fix sets the start to 21:12 and brings back 3 entries.

**5. Automatic time swaps.** The code swapped start and end whenever the end came first. It swapped three rows, and each swap moved the window onto the next stop. Each row had a one-hour typo in one of its two times:

| Stop | Form | Old swap | Fixed | Evidence |
|---|---|---|---|---|
| Session S stop 11 | 17:51-17:09 | 17:09-17:51 | 16:51-17:09 | Form sent at 17:08. GPS stays in one spot from 16:51 to 17:09 (spread 9 m) and moves away after 17:09. |
| Session T stop 4 | 12:57-12:15 | 12:15-12:57 | 12:57-13:15 | Stop 3 ended 12:55, stop 5 started 13:16. |
| Session U stop 7 | 18:54-18:07 | 18:07-18:54 | 17:54-18:07 | Stop 8 started 18:08. |

The cleaning step stops at an end-before-start row that has no written correction.

**6. One label for several stops.** The code merged form rows that share the same start and end time, as floors of one building. Some participants filled several stops with one time block after the session, so one stay could cover stops of different types under one label:

| Stay       | Window  | Stops inside                                     | Label used |
| ---------- | ------- | ------------------------------------------------ | ---------- |
| Session Q stop 1 | 104 min | open space, street, building, terrace            | open space |
| Session Q stop 5 | 79 min  | open space, street, building                     | open space |
| Session Q stop 8 | 29 min  | street, building                                 | street     |
| Session R stop 1 | 218 min | 7 stops in SOGO, one on the rooftop (open space) | building   |

The fix keeps merges whose rows share one type, such as several floors of one building, and drops the four mixed ones (12 entries).

### Smaller problems found while adopting

These four left the thesis numbers unchanged, but each could spoil a later run.

- `score_gt.py` took α from the settings file for the first scoring pass, which the method runs at α = 1. The stored thesis tables came from a run at α = 1. The script passes α = 1 itself after the fix.
- Entity IDs repeated across map areas: `tatemon_id` repeats across the 8 ZTOWN area codes and `link_no` across the 4 MAPPLE tiles. The IDs include the area or tile code (`B_{area}_{tatemon_id}`, `S_{tile}_{link_no}`), and the code stops when two places share an ID. The score tables stay the same.
- Some open-space polygons had invalid shapes. The code repairs them (`make_valid`). One of them is a candidate for a GT stay, and its scores stay the same.
- The cleaning step swapped start and end times by default. It stops and asks for a written correction (`known_time_corrections`) instead.

## Ground truth before and after

|                                               |  Thesis |   Fixed |
| --------------------------------------------- | ------: | ------: |
| Stay-device entries                           |   1,029 |   1,017 |
| Entries with no GPS point in the window       |      54 |      42 |
| Entries with GPS points                       |     975 |     975 |
| Stays used, after the drop list               |     907 |     907 |
| Physical stops used                           |     280 |     280 |
| GPS points in the stays used, before downsampling | 167,615 | 152,602 |
| GPS points after downsampling                 |  17,010 |  15,687 |

The counts match, but the stays differ. Twelve entries came in (Session P stops 7, 12, 15 and 16), twelve went out (Session Q stops 1, 5 and 8, Session R stop 1), and three windows moved (Session S stop 11, Session T stop 4, Session U stop 7). The four dropped blocks were long, so the point counts fall.

Downsampling keeps a random part of each stay's GPS points, so that the survey data looks as sparse as MILES ([Downsampling to MILES density](../notes/m-downsampling-to-miles-density.md)). The fixed GT keeps the thesis's downsampled points for the 886 stays the fixes leave as they were.

## Results

### Final model

Recall is the share of stays of one type that the model finds. Here it is out-of-sample: each stay's answer comes from the CV fold that left that stay out. ρ² shows the gain over a baseline that knows how common each type is. The condition number measures stability: higher means less stable.

|                            |            Thesis |           Adopted |
| -------------------------- | ----------------: | ----------------: |
| Parameters                 |                12 |                11 |
| α                          |             2.430 |             2.764 |
| Accuracy, in-sample        |             0.721 |             0.731 |
| **Accuracy, CV (grouped)** | **0.716 ± 0.076** | **0.719 ± 0.032** |
| Recall, building           |             0.896 |             0.900 |
| Recall, street             |             0.427 |             0.486 |
| Recall, open space         |             0.492 |             0.440 |
| ρ² vs LL(C)                |             0.300 |             0.305 |
| Condition number           |             1,373 |             1,681 |

The adopted model is the thesis model without `f_distribution × share_type`: the core terms of Model 4a, with one direction weight shared by all three place types ([Final model](../analysis/m-final-model.md)).

### Size of the change

A paired comparison checks the same stays one by one, thesis against adopted. It uses the 895 stays that both versions contain; the other 12 exist in the fixed GT alone. Re-drawing whole physical stops 10,000 times (a bootstrap) gives the 95% range of each difference. A range that contains 0 means chance can explain the change. Differences are in percentage points (points).

| On the 895 shared stays | Change | 95% range |
|---|---:|---:|
| CV accuracy (0.715 → 0.721) | +0.6 points | -1.8 to +3.0 |
| Recall, building | +0.4 points | -2.1 to +2.9 |
| Recall, street | +6.0 points | -0.6 to +13.1 |
| Recall, open space | -4.3 points | -9.8 to +1.7 |

McNemar's test, a standard test for paired right-or-wrong answers, gives p = 0.67 for accuracy. Accuracy shows no significant change. Recall moves from open space to street, and both ranges include 0. The spread of CV accuracy across folds falls from ± 0.076 to ± 0.032. The new list of stays changes the make-up of the folds, so part of that fall comes from different folds.

### Thesis decisions after the fix

| Thesis decision                                                                    | After the fix                                                                                                                                                                                                                                                                                                   |
| ---------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `R_buffer` 10 m beats 15 m ([R_buffer: 10 m vs 15 m](../analysis/m-r-buffer-10m-vs-15m.md))                             | Holds for accuracy and fit in Models 1, 2, 4a, 5 and 6. The condition number is lower at 15 m for Models 1, 2 and 5, so stability no longer favours 10 m.                                                                                                                                                       |
| Drop `f_temporal` (Model 1: t = 0.29)                                              | Holds: t = -1.56, and its overlap with `f_distribution` grows (VIF 7.5 → 21.7, r 0.88 → 0.96).                                                                                                                                                                                                                  |
| Reject the ASC, a fixed bonus per type ([Model 5: alternative-specific constants (rejected)](../analysis/m-model-5-asc-rejected.md))                | Holds, on a narrower ground. The ASC raises CV accuracy by 1.9 points (0.700 → 0.719), less than one fold spread (± 0.033). `asc_street` copies the street direction score (r = 0.94, VIF 30.6) and flips its weight from +3.46 to -5.30. The condition number rises from 737 to 2,027 (thesis: 775 to 37,583). |
| Interaction screen at α = 1 ([Interaction term screen (α = 1)](../analysis/m-interaction-term-screen.md))                        | Holds: the same three terms pass.                                                                                                                                                                                                                                                                               |
| Keep `f_distribution × share_type`, VIF 9.8 ([Stepwise VIF elimination](../analysis/m-stepwise-vif-elimination.md))       | Changes: VIF 10.4, above the limit of 10, so the term drops out, although its t-value is 4.61. Dropping it and σ² raises CV accuracy from 0.703 to 0.712.                                                                                                                                                       |
| One shared `f_directional` weight, p = 0.067 ([f_directional: shared vs split](../analysis/m-f-directional-shared-vs-split.md)) | Holds, at the edge: p = 0.054.                                                                                                                                                                                                                                                                                  |
| α = 2.43 with a clear peak ([Alpha calibration](../analysis/m-alpha-calibration.md))                               | Changes: α\* = 2.764 inside a flat profile. Any α from 2.2 upward fits within 1.92 total log-likelihood units of the best (thesis: 1.8 to 3.8). Above α = 4 the fit climbs back and passes the inside best point near α = 5, by 1.0 unit at α = 6 (not significant).                                            |
| MNL beats Random Forest and XGBoost in CV ([ML ceiling check, row level](../analysis/m-ml-ceiling-row-level.md))             | Holds: 0.719 against 0.708 and 0.703.                                                                                                                                                                                                                                                                           |
| Downsampling does not hurt the fit ([Raw-density refit](../analysis/m-raw-density-refit.md))                       | Holds: 0.719 with and without downsampling. Without downsampling, α runs to the search limit (6.0) and the condition number reaches 4,849.                                                                                                                                                                      |
| Bias toward building ([Confusion matrix](../analysis/m-confusion-matrix.md))                                      | Holds: the model calls 41.1% of street stays and 50.8% of open-space stays building (thesis 46.5% and 45.0%).                                                                                                                                                                                                   |
| Crowded candidates explain the bias ([Candidate density bias toward building](../analysis/m-candidate-density-bias.md))                 | Holds for streets. `share_street` stays strong (-5.16, t = -7.05), with 13.1 street candidates per street stay against 7.0 building candidates per building stay. `share_os` shrinks to -0.80 and loses significance (thesis -5.87), so it no longer covers the open-space errors.                              |
| Hard folds are hard for every type ([Fold difficulty](../analysis/m-fold-difficulty.md))                         | Changes: street accuracy follows the fold (0.36 to 0.65). Open space stays low in every fold (0.38 to 0.49). Thesis: 0.16 to 0.67 and 0.33 to 0.72.                                                                                                                                                             |

### Final model weights

The number in brackets is the t-value. A t-value of 2 or more counts as significant.

| Term | Thesis | Adopted |
|---|---:|---:|
| f_distribution, building | +1.25 (2.2) | +2.07 (4.1) |
| f_distribution, street | +0.91 (1.6) | +2.65 (5.3) |
| f_distribution, open space | +5.28 (8.1) | +6.52 (10.9) |
| f_distance, building | -2.10 (-2.0) | -0.38 (-0.3) |
| f_distance, street | -2.29 (-2.5) | -3.04 (-2.9) |
| f_distance, open space | -6.55 (-6.1) | -6.06 (-5.0) |
| f_directional, shared | +0.98 (3.1) | +3.43 (6.7) |
| share, building | -3.15 (-4.6) | -1.01 (-2.0) |
| share, street | -8.09 (-9.6) | -5.16 (-7.1) |
| share, open space | -5.87 (-4.2) | -0.80 (-0.7) |
| sigma | +0.78 (5.9) | +1.02 (7.4) |
| f_distribution × share_type | +5.78 (5.7) | dropped |

The share penalties shrink, and the dropped interaction term carried part of them, since it multiplies `f_distribution` by the share of the candidate's own type. All three `f_distribution` weights pass the significance line.

### The direction score with real street directions

With real street directions, the shared direction weight grows from +0.98 (t = 3.1) to +3.43 (t = 6.7). The split version, with one weight per type, gives street -5.17 (t = -4.4), building +2.67 (t = 2.0) and open space +2.57 (t = 1.7). In that version, movement along a street counts against that street. The raw scores carry a weak signal. On street candidates, the mean alignment is 0.613 for street stays, 0.627 for building stays and 0.633 for open-space stays, and random directions give 0.637. The movement inside a stay looks like GPS noise. More in [Street segmentation](d-street-segmentation.md).

## Points for discussion

1. **α.** The profile is flat above α = 2.2 and climbs back above α = 4, where `f_distance` comes close to 1 for nearly every candidate and acts like a fixed bonus per type. The data bound α from below and leave the upper side open. The 1.92 limit treats stays as independent; with three phones per stop, the true range is wider. The adopted model uses the inside best point, 2.764.
2. **Two tests near their limits decide the model shape.** The interaction term has VIF 10.4 against the limit of 10, and the split direction test gives p = 0.054 against 0.05. A rule that compares the candidate shapes on grouped CV would not hinge on these cut-offs.
3. **The ASC.** It raises CV accuracy by 1.9 points, so overfitting does not describe it. The case against it rests on the copy of the street direction score (r = 0.94) and the sign flip of that score's weight.
4. **Open-space errors.** The model calls 97 of 191 open-space stays building and 84 open space. Crowded candidates explain the street errors and leave the open-space errors without a cause.
5. **Two thesis statements were wrong before the fix**, and the documents correct them: open space is not the smallest type (191 stays, street 185), and all 21 stops on the drop list were building stays.

## Open items

- Sensei's review of the adoption.
- Slide 9 of `M241098.pptx` shows an R_buffer coverage table with thesis-era values. Its definition is not on record, so the table waits for the author.
- `manuscript/master-thesis/main.txt`, a text export of the thesis PDF from July, is out of date.
- The public dashboard shows the old numbers until the next publish.


<div class="backlinks" markdown>

**Linked from** [Publications and doctoral plan](../progress/d-progress-20-10-2026.md)

</div>
