---
source: report/plans/d-seasonal-variance.md
date: 26-10-2026
kind: plan
comments: true
generated: 2026-11-10T14:29:37
---

# Seasonal variance

<p class="doc-meta"><span class="chip chip-plan">Plan</span> <span class="chip chip-lane">On-going</span> <span class="chip chip-project">Doctoral</span> <span class="chip chip-date">26-10-2026</span></p>

New work from the meeting on 20-10-2026 ([Publications and doctoral plan](../progress/d-progress-20-10-2026.md)).

**Goal:** see how the split between indoor and outdoor activity changes with the season in Hiroshima.

Take the framework as it is for now, as if it were final ([Final model](../analysis/m-final-model.md)), and apply it to MILES on one week per season:

| Season | Week |
|---|---|
| Spring | 15–21 April 2024 |
| Summer | 8–14 July 2024 |
| Autumn | 21–27 October 2024 |
| Winter | 15–21 January 2024 |

A small area is enough.

## Progress (10-11-2026)

The data is prepared (steps 1–3), and the framework has been applied to every stay (step 4, first results below).

1. **Clip.** Keep only the GPS points inside the study area. The area is the same as the ground truth (GT) area: the rectangle covered by the street map, about 12 km × 9.5 km of central Hiroshima. All data uses one map projection (EPSG:32653, distances in metres). Unlike the GT, the points are not thinned (no downsampling, [Downsampling to MILES density](../concepts/m-downsampling-to-miles-density.md)).
2. **Overview.** Look at how often the phones record a point and how far apart the points are, before choosing the stay detection settings.
3. **Stay detection.** Find the stays with ST-DBSCAN, a method that groups GPS points that are close in space and in time. It has three settings: the largest distance between points of one stay (eps1), the largest time gap (eps2), and the smallest number of points that makes a stay (min_samples). The settings come from Kato et al. (2024), who tuned them on GPS data from Hiroshima for different recording intervals.
4. **Framework.** Give every stay its probabilities of building, street and open space, then compare indoor and outdoor time across the seasons.

| Season                  | Clip | Overview | Stay detection      | Framework |
| ----------------------- | ---- | -------- | ------------------- | --------- |
| Winter (15–21 Jan 2024) | done | done     | done                | done      |
| Spring (15–21 Apr 2024) | done | done     | done                | done      |
| Summer (8–14 Jul 2024)  | done | done     | done                | done      |
| Autumn (21–27 Oct 2023) | done | done     | done                | done      |
| Autumn (21–27 Oct 2024) | done | done     | on hold (anomaly 4) |           |

Autumn 2023 (21–27 October 2023) was added to check whether autumn 2024 differs because of the season or because of the way the data was collected. **For now, autumn 2023 stands for autumn** (decision of 10-11-2026), because autumn 2024 is not comparable (anomaly 4).

**Decisions of 10-11-2026** for stay detection:

- **No trip-label filter.** Every GPS point goes into ST-DBSCAN, whatever its trip label. Before, points with a trip label (walk, car, train, ...) were removed first. The labels are not reliable in every week (anomaly 4), so stay detection no longer depends on them.
- **Stays cut at midnight are joined**, but only when they are certainly the same stay (anomaly 2).
- **Split visits are not joined** for now (anomaly 3).

## The data

|                                        |    Winter |    Spring |    Summer | Autumn 2024 | Autumn 2023 |
| -------------------------------------- | --------: | --------: | --------: | ----------: | ----------: |
| GPS points in the area                 | 2,821,778 | 2,349,164 | 2,088,422 |   1,406,182 |   3,696,829 |
| People                                 |     6,006 |     5,146 |     4,536 |       3,090 |       8,693 |
| Time between two points (median)       |      41 s |      41 s |      41 s |        40 s |        41 s |
| Points with accuracy of 100 m or worse |     14.7% |     15.3% |     17.6% |       14.3% |       15.5% |

The phones record about one point every 40 seconds, in every week and at every hour of the day. The number of people changes a lot: autumn 2024 has about a third of the people of autumn 2023.

**Checks on the single points** (before any stays are built):

- Every week has the year it should (four weeks of 2024, one of 2023): every clipped point, and every row of five sampled hours of the raw files (all of Japan). Every time stamp falls inside its hour folder.
- No two points of one person share the same time. No person sends points unusually fast (no one above one point per 10 seconds for an hour).
- The same people appear in several weeks: for example 2,984 people are in both winter and spring, 2,275–2,496 in summer and winter or spring, about 1,550–1,800 in autumn 2024 and one of the other 2024 weeks, and 1,612 in both autumns. The person IDs are coded the same way in every week, so the same people can be followed from season to season.
- Gender and age group are missing for about three in four people.

![](../figures/seasons_data.png)

The left chart shows the trip label that MILES gives each point (walk, car, train, ...). A point without a label counts as not travelling. Winter, spring and autumn 2023 look the same. Summer and autumn 2024 have far fewer walk labels (anomaly 4).

## Choosing the ST-DBSCAN settings

Kato et al. (2024) give settings for a 30-second interval and for a 1-minute interval. MILES records about every 40 seconds, so three options were compared on spring:

|                                    |        Kato 30 s | Between the two (~40 s) |     Kato 1 min |
| ---------------------------------- | ---------------: | ----------------------: | -------------: |
| Settings (eps1, eps2, min_samples) | 70 m, 1100 s, 18 |         63 m, 920 s, 14 | 50 m, 610 s, 6 |
| Stays found (one week)             |            7,966 |                  11,012 |         44,051 |
| Typical stay length (median)       |           44 min |                  32 min |          5 min |
| Stays shorter than 10 minutes      |             0.6% |                    5.3% |            64% |

![](../figures/summary.png)

- The 30 s settings and the in-between settings find almost the same stays (94% of the stay points are shared). The in-between settings add about 3,000 shorter stays of 10–18 minutes.
- The 1 min settings find four times as many stays. Most are stops of about 5 minutes, and long visits break into many small pieces. They do not fit MILES.
- **Chosen: the 30 s settings** (70 m, 1100 s, 18). With one point every 41 seconds, a stay must last at least about 12 minutes.

## Stays in the four seasons

|                                            | Winter | Spring | Summer | Autumn (2023) |
| ------------------------------------------ | -----: | -----: | -----: | ------------: |
| Stays                                      | 10,222 |  8,695 |  7,497 |        13,767 |
| People with at least one stay              |  1,649 |  1,369 |  1,180 |         2,050 |
| Share of people with at least one stay     |    27% |    27% |    26% |           24% |
| Stays per person (people with a stay)      |    6.2 |    6.4 |    6.4 |           6.7 |
| Typical stay length (median)               | 40 min | 41 min | 42 min |        41 min |
| Stays joined over midnight                 |    260 |    185 |    201 |           349 |
| Spread of the points in a stay (σ, median) | 19.7 m | 19.8 m | 19.8 m |        20.1 m |

![](../figures/seasons_stays.png)

The stays of the four seasons have almost the same length, size and start times. Any seasonal difference should therefore show up in where the stays are (indoor or outdoor), which is the next step. The peak at midnight in the start-hour chart is gone since the midnight join.

**What dropping the trip-label filter changed** (winter and spring, same settings otherwise):

![](../figures/filter_effect.png)

|                                                 | Winter         | Spring        |
| ----------------------------------------------- | -------------- | ------------- |
| Stays with the filter → without                 | 9,410 → 10,222 | 7,966 → 8,695 |
| Earlier stays lost                              | 0              | 0             |
| New stays (none of their points was in a stay)  | 1,133          | 975           |
| New stays mostly made of labelled travel points | 48             | 74            |
| Shared stay points (overlap)                    | 96%            | 96%           |

- Every earlier stay is still there. About 1,000 new stays appear per season. They are shorter (median 20 minutes, against 45) and mostly made of unlabelled points; only about 5–7% of them are mostly labelled travel.
- Most new stays contain a few labelled points, typically at their edges (anomaly 9).

## Indoor vs outdoor: first results

The framework ([Final model](../analysis/m-final-model.md)) was applied to every stay exactly as it was fitted on the GT, with no refit. For each stay it gives three probabilities: building, street and open space. **Indoor** means building; **outdoor** means street or open space.

**Main measure** (decision of 10-11-2026): the share of stay time spent indoors, using the probabilities. Each stay counts with its length times its probability of being in a building. A 2-hour stay with P(building) = 0.7 adds 1.4 indoor hours and 0.6 outdoor hours.

|                                                      |       Winter |       Spring |       Summer | Autumn (2023) |
| ---------------------------------------------------- | -----------: | -----------: | -----------: | ------------: |
| Stays                                                |       10,165 |        8,654 |        7,459 |        13,691 |
| People                                               |        1,647 |        1,367 |        1,178 |         2,047 |
| **Indoor share of stay time**                        |    **69.8%** |    **69.0%** |    **69.0%** |     **69.8%** |
| 95% interval                                         |   68.1–71.3% |   67.7–70.2% |   67.4–70.4% |    68.4–71.2% |
| Street / open space                                  | 14.4 / 15.9% | 14.3 / 16.7% | 13.6 / 17.5% |  14.7 / 15.6% |
| Indoor share if each stay takes its most likely type |        94.2% |        94.2% |        93.7% |         93.8% |

![](../figures/indoor_outdoor_seasons.png)

- **No season differs from another.** All differences are below 1 percentage point, and every 95% interval includes zero. The interval comes from a bootstrap over people: the people of a season are drawn again at random 1,000 times, and the share is recomputed each time.
- **The same people tell the same story.** 370 people have stays in all four seasons; their indoor share is 68–70% in every season, with no significant difference. Pairs of seasons with 493–824 shared people give the same result.
- **Most likely type vs probability.** Building is the most likely type for 93–95% of stays, but the probabilities put about 69–70% of the time indoors. Many stays are uncertain, and the probabilistic measure keeps that uncertainty instead of rounding it away.

![](../figures/indoor_outdoor_hourly.png)

- **By hour:** about 71–72% indoors around midday, but only 63–67% at night (00:00–06:00). This is probably not real outdoor time. Long stays (8 hours or more, mostly nights at home) get a lower P(building), 0.63 on average. Their positions are often rough: stays whose typical accuracy is exactly 100 m get 0.68, and 500 m or worse 0.58, against 0.74–0.76 for 10–50 m. A rough position can fall on the street or open space next to the home.
- **Weekday and weekend** are almost the same in every season.

![](../figures/indoor_outdoor_differences.png)

**Sensitivity** (indoor share of stay time):

|                                                        | Winter | Spring | Summer | Autumn (2023) |
| ------------------------------------------------------ | -----: | -----: | -----: | ------------: |
| Main                                                   |  69.8% |  69.0% |  69.0% |         69.8% |
| Without stays with typical accuracy of 500 m or worse  |  69.8% |  69.1% |  69.0% |         69.9% |
| Without stays with typical accuracy of 100 m or worse  |  71.7% |  69.7% |  70.1% |         71.7% |
| Travel points at stay edges removed (anomaly 9)        |  71.7% |  70.8% |  70.1% |         71.2% |

Both corrections raise the indoor share by about 1–2 points in every season, and the seasons stay as close as before. Without the 100 m stays the night dip becomes smaller but does not disappear.

**Most likely type, one stay = one count.** A second way to compare the seasons: each stay counts once, with the type that has the highest probability.

|                     | Winter        | Spring        | Summer        | Autumn (2023)  |
| ------------------- | ------------: | ------------: | ------------: | -------------: |
| Stays               |        10,165 |         8,654 |         7,459 |         13,691 |
| Building            | 95.0% (9,661) | 93.5% (8,095) | 93.2% (6,953) | 94.8% (12,982) |
| Street              |    1.2% (122) |    1.2% (103) |     0.8% (61) |     1.2% (169) |
| Open space          |    3.8% (382) |    5.3% (456) |    6.0% (445) |     3.9% (540) |
| Open space, 95% interval | 3.1–4.6% | 4.4–6.3% | 4.9–7.1% | 3.4–4.6% |

![](../figures/indoor_outdoor_argmax.png)

- **This measure shows a seasonal pattern.** More stays are in open space in spring and summer (5.3% and 6.0%) than in winter and autumn (3.8% and 3.9%). The differences between these two groups are significant (their 95% intervals do not include zero).
- **The same 370 people:** summer has more open-space stays than each of the other three seasons (5.9% against 3.5–4.1%). Spring is not higher than winter or autumn for these people.
- **Why the time share does not show it.** Open-space stays are not shorter (about 40 minutes, like the others). But the time share is dominated by long stays at home and at work, and the open-space probability is spread thinly over many uncertain stays. Counting each stay once makes the confident open-space stays stand out.
- **Caution.** Outdoor stays are few (street 61–169, open space 382–540 per season), and taking the most likely type hides the uncertainty: a stay labelled open space has, on average, a 71% probability of being in open space.

**Limits of this first result.** The model learned from GT stops of about 10 minutes in the daytime. MILES stays are longer, and include whole nights at home, which the GT never had. Autumn is the 2023 week. Split visits are not joined (anomaly 3), and the travel points at stay edges make stays wider in the main run (anomaly 9).

## Anomalies

1. **Times are in UTC, not Japan time.** The downloaded files follow UTC (9 hours behind Japan). Each week therefore runs from 09:00 on the first day to 08:59 on the day after the last day (Japan time). The first and the last day are not complete and are marked as partial. About 100 stays per season are cut where the week starts or ends.
2. **Stays are cut at midnight** (now joined). Stays are searched day by day, so a stay over midnight becomes two stays. Before the fix, about 3% of stays started between 00:00 and 00:05 or ended between 23:55 and 24:00. Two parts are now joined only when all of these hold: the first part ends at most 5 minutes before midnight, the second starts at most 5 minutes after it, their centre points are at most 70 m apart (eps1), and the person never goes farther than 70 m away in between. Almost every candidate pair passes (winter 260 of 264, spring 185 of 187, summer 201 of 201, autumn 349 of 351). About 30–70 stays per season still start or end within 5 minutes of midnight; they did not pass these checks.
3. **One visit split into several stays** (not joined for now). About 23% of stays in every season start at the same place as the person's previous stay that day. For each such pair, the points between the two stays were checked (the "same place" chart above):
    - **The person stayed** (11% of all stays). The person did not go more than 200 m away, but the phone recorded only about 2 points per 15 minutes instead of about 22. ST-DBSCAN needs 18 points close in time, so this time counts as no stay at all. Phones record less often when they are not moving.
    - **No points at all** (7–8% of all stays). The phone recorded nothing between the two stays, typically for 15–17 minutes.
    - **A real return** (4–5% of all stays). The person went more than 200 m away and came back, typically after about 2 hours.

   So about 4 in 5 of these pairs are one visit cut in two. Joining them would reduce the stays by about 18–19% in every season (winter 10,222 → 8,309, spring 8,695 → 7,072, summer 7,497 → 6,107, autumn 13,767 → 11,277). The time lost in the gaps is mostly long, still periods, probably indoors, so without a fix indoor time is underestimated.
4. **Fewer walk labels in summer and autumn 2024.** Walking is labelled much less often in these two weeks:

|                                       | Winter | Spring | Summer | Autumn 2024 | Autumn 2023 |
| ------------------------------------- | ------ | ------ | ------ | ----------- | ----------- |
| Points labelled walk                  | 6.5%   | 7.1%   | 1.7%   | 0.9%        | 7.0%        |
| Labelled trips that are walking trips | 29%    | 30%    | 10%    | 9%          | 30%         |
| Unlabelled points faster than 1 m/s   | 14%    | 14%    | 15%    | 27%         | 14%         |

   - **Not the season.** Autumn 2023 looks exactly like winter and spring in every check (labels, distance between points, missing values). So autumn 2024 differs because of the way the data was collected or processed, as sensei suggested. The autumn 2024 files also have another format (other column names, extra ID columns, another folder structure, a missing speed written as −2.24 instead of left empty; the speed is still in metres per second).
   - **Autumn 2024:** many people who are walking count as not travelling (27% of the unlabelled points move at walking pace or faster, against 14%). Stay detection would use these walking points, so autumn 2024 stays would not be comparable with the other weeks.
   - **Summer:** the files have the usual format, and the unlabelled points move as in winter and spring (15%). The walk labels drop on every day of the week (1.2–2.1%), while the share of points moving at walking speed stays the same (about 8%). So summer looks like a change in how walking is labelled, not in how much people walk. Summer and autumn 2024 are both later than April 2024, so the labelling may have changed between April and July 2024. The effect on stay detection looks small in summer.
5. **Many points report exactly 100 m accuracy.** 12% of all points and 20% of points that are not travelling report an accuracy of exactly 100 m, 97% of them from Android phones. This looks like a fixed value for a rough position, not a measured error. They are much more common in long stays (28% of the points) than in short stops (5%).
6. **Most people only pass through.** Three in four person-days have no stay in the area. A person-day has a median of about 67 points, roughly 45 minutes of recording inside the area.
7. **Some positions are very rough.** About 0.6% of points report an accuracy of 1,000 m or worse. Some of them sit at exactly the same position for many people (up to 35 people at one spot, with an accuracy of 1,500 m in winter and 2,200 m in autumn): probably a position taken from the phone network, not from GPS. 152 winter, 143 spring, 84 summer and 240 autumn stays (about 1–2%) have a median accuracy of 500 m or worse.
8. **Small items.** 26–67 stays per season have fewer than 18 points (a known side effect of how the method shares border points between nearby stays); they are kept. Two map layers (centerline and open space) were stored in another projection (EPSG:6691) and are now EPSG:32653; the shapes did not change, so no earlier result changes.
9. **Stays are wider without the trip-label filter.** Points labelled as travel now join a stay when they are close enough in space and time: mostly the arrival and departure at its edges. They are only 2.4% of the stay points, but they sit far from the centre (median 43 m, against 2 m for the other points), and 61% of stays contain at least one. The spread of a stay (σ, the standard deviation of its points) grows from 15.3 m to 19.8 m in spring, and the largest distance from the centre point from 54 m to 71 m. σ is one of the inputs of the model ([sigma](../concepts/m-sigma.md)), so this will matter when the model is applied.

## Questions for sensei

1. **Join split visits later?** Not joined for now. The rule would join two stays at the same place when the person did not go more than 200 m away in between (anomaly 3); it is a new rule, added after the Kato et al. method.
2. **Walk labels.** Ask the data provider whether the trip labelling changed between April and July 2024, and whether autumn 2024 can be processed like the other weeks (anomaly 4). Autumn 2023 is used until then.
3. **Travel points at the edges of stays.** Keep them, or remove the labelled travel points at the edges of each stay after ST-DBSCAN, so that σ is not inflated (anomaly 9)?
4. **The 100 m points.** Keep them (as now), or treat them separately (anomaly 5)? Leaving out the stays they dominate raises the indoor share by up to 2 points.
5. **Night stays.** The framework was fitted on daytime stops. Should long night stays at home be checked separately (for example with a few labelled nights), since they get a lower P(building)?
6. **What to report as the result.** The time share shows no seasonal difference (about 69–72% indoors in every season, every correction). Counting each stay once with its most likely type shows more open-space stays in spring and summer (5.3–6.0% against 3.8–3.9%). Which measure answers the research question, or should both be reported?



Part of [Doctoral plan](../threads/d-doctoral-plan.md).


<div class="backlinks" markdown>

**Linked from** [Doctoral plan](../threads/d-doctoral-plan.md) · [Publications and doctoral plan](../progress/d-progress-20-10-2026.md)

</div>
