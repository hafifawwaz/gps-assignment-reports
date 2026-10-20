---
source: report/inbox/d-toy-data.md
date: 16-10-2026
kind: inbox
comments: true
generated: 2026-10-20T16:29:09
---

# GPS toy data

<p class="doc-meta"><span class="chip chip-inbox">Inbox</span> <span class="chip chip-project">Doctoral</span> <span class="chip chip-date">16-10-2026</span></p>

!!! question "For discussion"
    Rough draft and open questions. Not yet reviewed.

Supporting work for [Sequence-aware assignment](d-sequence-aware.md). No publication is planned. If a part turns out to be new, it can become one.

Consensus report: [Consensus Report](d-toy-data-consensus.md)
## The idea

The field-survey ground truth is small and biased. All tests so far ran on the same 907 stays, so a result mixes the model with the quirks of that dataset.

Toy data separates the two:
- The true place of every stay is known.
- Every source of noise is set on purpose, so a result can be traced to one cause.

The generator has four jobs:
- Test models against a known truth.
- Separate bias sources by switching them on and off one at a time.
- Find the limits of the framework, for example the noise and density where probabilistic assignment stops beating nearest-entity.
- Supply sequences for the sequence-aware work.

Two things are bonuses and do not shape the design: standing in for ground truth in other cities, and a paper.

## What it produces

- **Raw GPS points in the MILES format,** so the existing pipeline runs on them without changes.
- Two truth tables next to the points:
	- The stay table has the true entity (id and type), the true coordinate, and the true start and end time.
	- The point table labels each point with its stay, or with "transit".
- Size is a parameter (people and days). Small to debug, large for sweeps.
- One device per person at first.
	- The tables have a `device_id` column from the start, so several devices per stop can be added later.

## Two programs

The work splits in two. Each can be swapped without touching the other.

**Program 1: population and activity chains.** It needs no map.
- A set of people, each with an activity chain: order of activities, activity type, start and end.
- A full synthetic population (matched to the census) is probably too much. Tests 1 to 4 only need a few persona types, such as office worker, student, homemaker, retiree.
- It becomes useful if the work moves to other cities.
- The activity chain can come from persona rules, a semi-Markov model, or a real person trip survey. Whether a Hiroshima survey exists and may be used needs checking.

**Program 2: GPS generator.** It needs the map.
- It takes the chains from program 1 and turns them into GPS points.
- It has its own location choice step, because of the point below.

**Why location choice has memory.**
- A person who goes home must return to the same building. The same goes for work and for favourite shops.
- If every stay picked a new random entity, the sequences would lose their main structure, and sequence-aware tests would mean nothing.
- So each person gets anchor places (home, work) and favourite places. Each activity is then mapped to a concrete entity.
- Models like EPR (explore and return to favourite places) are built for this.
- Version one uses a trivial planner with independent random stays. Program 1 replaces it later.

## How a run flows

Six stages inside program 2.

#### Spatial world
- Either the real Hiroshima layers or a synthetic city.
- A synthetic city has density, street width and building size set by hand.
- Both use the same layer format.
- A synthetic city also needs land use, because an activity such as shopping must land on a building that can host it.

#### Move/transit segment
- Inside a stay, the person stays near one true point inside the entity:
	- in a building: the interior or the entrance,
	- on a street: a spot along the segment,
	- in an open space: a point inside it.
- Between stays, the person travels over the street network, on foot or by vehicle. This produces the transit points.

#### Sampling
- Interval and dropout are knobs. Defaults come from MILES.
- **Dropout** means missing GPS points: the device should log one point per interval, but sometimes logs none.
- Dropout runs as an on/off process, not as random single points, because real signal loss comes in blocks (for example 5 minutes inside a shop with no points).
- Long gaps matter for the model. They test `f_temporal` (bridging), and they can split one stay into two in ST-DBSCAN.

#### Detection
Two modes, run on the same points.
- **Oracle mode:** clusters are built straight from the true labels. Only assignment error is left.
- **Detected mode:** run ST-DBSCAN with the MILES parameters, then match the clusters it finds to the true stays.
- The accuracy gap between the two modes is the bias that ST-DBSCAN adds. The field data cannot show this.

#### GPS error
Described below.

## The error model

> **An observed point is the true position plus a cluster offset plus motion inside the cluster.**

**Cluster offset**
- One 2D vector per stay, shared by all its points.
- It moves the whole cluster away from the truth.
- It is the main cause of wrong assignments.

**Motion inside the cluster**
- Follows an **AR(1) or Ornstein-Uhlenbeck process**: each point depends on the previous one, with a correlation time and a spread.
- The jumps can have heavy tails, and a separate outlier rate covers multipath jumps.

**What the surroundings change**
- A denser or taller neighbourhood widens the spread and pushes the offset away from tall buildings.
- A stay inside a building gets a larger spread and longer dropouts.
- Inputs for this:
	- building density in a radius,
	- building height (for a sky-view estimate),
	- the inside/outside flag,
	- street width or height-to-width ratio.
- Each effect has its own switch and strength, so each bias can run alone.

**A later, heavier level** would simulate satellites and ray-trace against a 3D city model such as PLATEAU. That gives physical line-of-sight and non-line-of-sight errors. It is parked. It could be a result of its own.

## Calibration and validation

**What is fitted to MILES.** Only things that can be seen without a truth:
- spread per stay,
- points per stay,
- gap length and dropout pattern,
- dwell time.

**What is not fitted.**
- Offset size and direction need a truth, and the only truth is the biased field data.
- So they are knobs with a wide range.
- Results are read as sensitivity ("the model breaks from this offset up"), not as a prediction of the real value.

**The confusion pattern of the field data is not a target.**
- Building recall 90.0%, street 48.6%, open space 44.0%.
- The pattern comes from how the survey ran: which stops were chosen, how they were reported, how dense the candidates were.
- Fitting the toy data to it would bring that bias into the generator.

**What is done instead.**
- The mix of stay types is a knob.
- Recall per type is reported as an output for each setting.
- One check on the field data, without tuning:
	- Run the generator on the real Hiroshima layers with a plausible error.
	- See whether the same order appears: building easiest, street hardest.
	- If it appears, geometry and density explain it.
	- If it does not, the generator or the field data needs an explanation.
- The numbers themselves are not matched.

## Experiments it enables

- Bias ablation: switch each noise source on alone, then in pairs. Record which model loses accuracy and by how much.
- A sweep over noise and entity density, to draw where probabilistic beats nearest-entity.
- Oracle versus detected: the cost of detection before assignment starts.
- Parameter recovery: generate from the MNL, refit, check that the coefficients come back.
- Sequences: test the sequence-aware model once program 1 exists.

## Risks

- **Circularity.**
	- A toy set generated from the model's own assumptions only confirms the model.
	- The generator uses a different mechanism from the MNL.
	- Parameter recovery runs as a separate sanity check.
- **Sequence circularity.**
	- The sequence model can learn the structure of the planner.
	- It also needs a check on MILES.
- **Matching rule for detected clusters.**
	- Split, merged and missed stays each need a stated rule before any number is reported.
- **Transit path.**
	- It depends on the street network and on the walking or vehicle choice.

## Open questions

- Matching rule for detected clusters.
- Land use for the synthetic city.
- How transit points should look for walking versus vehicles.
- Which of EPR and TimeGeo (below) fits the location choice and the chains.
- Is a Hiroshima person trip survey available, and may it be used.

## Search keywords

**GPS error structure**
- "GNSS multipath urban canyon error model", "non-line-of-sight NLOS pseudorange error"
- "GPS positioning error autocorrelation", "Gauss-Markov process GNSS error"
- "smartphone GNSS accuracy urban", "Android raw GNSS measurements"
- "sky view factor GNSS", "HDOP dilution of precision urban"
- "3D-mapping-aided GNSS", "shadow matching", "GNSS ray tracing simulation"

**Trajectory simulation with known truth**
- "synthetic GPS trajectory generation noise", "GPS trajectory simulator ground truth"
- "map matching synthetic noise" (Newson and Krumm 2009 added Gaussian noise to test their HMM)
- "SUMO trajectory simulation", "benchmark trajectory dataset known ground truth"

**Human mobility and activity chains**
- "exploration and preferential return" (EPR, Song et al. 2010), "TimeGeo" (Jiang et al. 2016)
- "DITRAS" (Pappalardo and Simini), "scikit-mobility"
- "activity-based model", "ActivitySim", "semi-Markov activity chain"
- "synthetic population", "iterative proportional fitting synthetic population", "person trip survey"
- "daily activity schedule generation", "time geography"

**Stay detection and stay-to-place**
- "stay point detection", "ST-DBSCAN" (Birant and Kut 2007), "Trackintel"
- "stop detection sensitivity to parameters", "stop-move trajectory"
- "semantic enrichment of trajectories", "POI assignment GPS uncertainty", "visit attribution"
- "indoor outdoor detection smartphone"

**Simulator validation and experiment design**
- "simulation-based inference", "approximate Bayesian computation"
- "pattern-oriented modelling", "sim-to-real gap", "synthetic data fidelity"
- "Monte Carlo experiment design", "Sobol sensitivity analysis"


<div class="backlinks" markdown>

**Linked from** [Consensus Report](d-toy-data-consensus.md) · [Publications and doctoral plan](../progress/d-progress-20-10-2026.md) · [Sequence-aware assignment](d-sequence-aware.md) · [d plan](d-plan.md)

</div>
