---
source: report/concepts/glossary.md
date: 05-08-2026
kind: concept
comments: true
generated: 2026-10-26T20:52:49
---

# Glossary

<p class="doc-meta"><span class="chip chip-concept">Concept</span> <span class="chip chip-date">05-08-2026</span></p>

Plain explanations of the words that come back in many notes. Each note also explains its own terms the first time it uses them.

## Places and data

**Stay cluster (stay).** A group of GPS points recorded while a person stayed in one place, for example sitting in a cafe for 20 minutes.

**Entity.** One place on the map: a building, a street, or an open space (a park, a plaza).

**Entity type.** Building, street or open space. The model predicts the type of place, not the exact building.

**Candidate.** An entity close enough to a stay to be a possible answer. Each stay has a list of candidates.

**Ground truth (GT).** The correct answers. In this study, participants wrote down where they really were, so each stay has a known correct type.

**MILES.** A large GPS dataset from a smartphone app. The model is meant to be used on MILES later.

## Model terms

**Model.** A formula that turns the scores of each candidate into a probability for building, street and open space.

**MNL / logit / conditional logit.** The type of model used here. It gives each candidate a value, and turns those values into probabilities that add up to 1.

**Weight (coefficient, w).** How much one score counts in the model. The model learns the weights from the ground truth.

**Parameter.** A number the model learns. "11 parameters" means the model learns 11 weights.

**Generic vs alternative-specific.** A generic weight is the same for all three types. An alternative-specific weight is different for building, street and open space.

**ASC (alternative-specific constant).** A fixed extra value for each type, used to see if one type is preferred in general.

**Calibration.** Finding the best weights and settings by fitting the model to the ground truth.

**α (alpha).** A setting that controls how fast the distance score drops as a candidate gets farther away.

**σ (sigma).** How spread out the GPS points of a stay are. A large σ means the GPS position was uncertain.

**R_buffer.** The search distance around each GPS point. Entities inside this distance become candidates. The study uses 10 m.

## How results are measured

**Accuracy.** The share of stays where the model's top answer is the correct type. 0.719 means 71.9% correct.

**Recall (per type).** Of all stays that really were, for example, street, the share the model called street.

**In-sample.** Accuracy measured on the same data the model learned from. It is usually too optimistic.

**Cross-validation (CV).** The data is split into 5 parts (folds). The model learns from 4 parts and is tested on the 5th, five times. This shows how well the model works on data it has not seen.

**Grouped CV.** CV where all recordings of the same stop stay in the same part. This study needs it because several phones (three for most stops) recorded each stop at the same time.

**± value.** How much the result changes from fold to fold (one standard deviation). In 0.719 ± 0.032, the 0.032 shows that some folds are easier than others.

**Log-likelihood (LL).** A number that shows how well the model's probabilities fit the correct answers. Closer to 0 is better.

**ρ² (rho-squared).** How much better the model is than a simple baseline. Negative means worse than the baseline.

**t-value.** How clearly a weight differs from zero. Above about 2 (or below -2) usually counts as significant.

**p-value.** The chance of seeing a result this strong if there were no real effect. Below 0.05 usually counts as significant.

**LR test (likelihood-ratio test).** A test that checks whether extra parameters improve the fit enough to be worth keeping.

**Overfitting.** When a model learns the training data too closely, including noise, and then does worse on new data.

## Warning signs in a model

**Correlation (r).** How closely two numbers move together, from -1 to 1. Near 1 means they almost always rise and fall together.

**Multicollinearity.** When several scores in a model are strongly correlated, so the model cannot tell their effects apart well.

**VIF (variance inflation factor).** A number for each score that shows multicollinearity. Above 10 is the usual warning line.

**Condition number.** One number for the whole model that shows how stable the fit is. Large values (thousands) mean the individual weights are unreliable.

**Random Forest, XGBoost.** Two machine-learning methods built from many decision trees. They are flexible but hard to interpret.

Part of [Thesis summary](../threads/m-thesis-summary.md).


<div class="backlinks" markdown>

**Linked from** [MNL model development](../progress/m-progress-19-07-2026.md) · [Model evaluation metrics](m-model-evaluation-metrics.md) · [Thesis summary](../threads/m-thesis-summary.md)

</div>
