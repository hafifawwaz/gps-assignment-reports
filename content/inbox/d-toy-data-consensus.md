---
source: report/inbox/d-toy-data-consensus.md
date: ''
kind: inbox
comments: true
generated: 2026-10-20T15:44:29
---

# Consensus Report

<p class="doc-meta"><span class="chip chip-inbox">Inbox</span></p>

!!! question "For discussion"
    Rough draft and open questions. Not yet reviewed.

Consensus literature search for the toy data idea: [GPS toy data](d-toy-data.md).

A synthetic GPS generator is well supported by the literature as a way to create known ground truth, isolate preprocessing bias, and stress-test mobility inference pipelines under controlled sparsity and noise. Closely related work already argues that sparse, noisy commercial GPS data can distort stop detection, home/work attribution, trip classification, and downstream epidemic or transport analyses, while synthetic environments solve the validation problem by exposing both the full trajectory and the latent diary (Li & Barreras, 2024). More broadly, simulation studies are valuable precisely because the data-generating truth is known, which allows direct estimation of bias, variance, and failure regimes that field data alone cannot separate (Morris et al., 2017). In mobility specifically, recent synthetic-ground-truth frameworks use agent-based simulation or travel-demand models to compare inferred stays, departure times, and trajectories against known truth when real ground truth is unavailable (Zannat et al., 2024).

**Figure 1:** Consensus on synthetic ground-truth utility for evaluation

## 1. Introduction

Your idea fits an identifiable gap: current GPS preprocessing methods are usually validated on limited, noisy field datasets, yet many error sources are entangled, especially stay detection error, POI assignment error, and structured missingness (Kato et al., 2024; Suzuki et al., 2019; Yang et al., 2026). A synthetic environment is especially useful here because it can separate oracle clustering from detected clustering, vary one bias source at a time, and reveal thresholds where algorithm rankings change (Li & Barreras, 2024).

The strongest direct precedent is Garden City, which was built as a sandbox for exactly this problem: synthetic agents moving through a stylized city, a mobility diary, a complete ground-truth trajectory, and a sparse GPS-like sample with bursty ping times and measurement noise (Li & Barreras, 2024). Parallel literatures support nearly all of your proposed components separately: diary-based or EPR-based mobility generators for recurrent anchor places and favorite locations (Pappalardo & Simini, 2016; Jiang et al., 2016), semi-Markov or Bayesian activity-chain models for durations and sequence realism (Wang & Osaragi, 2024; Joubert & De Waal, 2020; Dube et al., 2025), and urban GNSS studies showing that error magnitude, anisotropy, and heavy tails depend strongly on buildings, canyon geometry, and NLOS conditions (Groves, 2011; Wang et al., 2012; Li et al., 2026; Peretic et al., 2025).

## 2. Methods

The search covered 220 million papers in Consensus, spanning Semantic Scholar, PubMed, and other scholarly sources.

|Retrieved|Eligible|Included|
|---|---|---|
|1.5M|516|100|

**Figure 2:** Search funnel for synthetic GPS literature

Searches targeted four evidence streams: synthetic trajectory generation, activity-chain modeling, GPS/GNSS urban error modeling, and stay/POI inference under sparse noisy sampling. Papers were prioritized when they directly informed modular design, controllable bias injection, truth-table generation, bursty missingness, repeated-place choice, or Hiroshima-relevant survey inputs.

## 3. Results

### 3.1 Key Papers

A few papers anchor the design most directly because they cover the exact sandbox concept, recurrent-place mobility generation, urban GPS degradation, or ground-truth benchmarking. Garden City is the nearest template; TimeGeo and Ditras anchor sequence and repeated-place generation; Hiroshima stay-detection work anchors your detected-versus-oracle evaluation; and urban GNSS papers anchor the error model (Li & Barreras, 2024; Jiang et al., 2016; Pappalardo & Simini, 2016; Kato et al., 2024; Adjrad & Groves, 2017).

| Paper                 | Summary                                                        |
| --------------------- | -------------------------------------------------------------- |
| (Li & Barreras, 2024) | Sandbox with truth, sparsity, burstiness (Li & Barreras, 2024) |
| (Jiang et al., 2016)  | r-EPR daily mobility framework (Jiang et al., 2016)            |
| (Kato et al., 2024)   | Hiroshima ST-DBSCAN benchmark (Kato et al., 2024)              |

**Figure 3:** Foundational papers for generator design

### 3.2 Mobility Diary Design

The literature supports your two-program split because several frameworks separate diary generation from spatial realization of trajectories (Pappalardo & Simini, 2016; Liu et al., 2023). EPR-style models are appropriate when the goal is to preserve repeated returns to home, work, and familiar places rather than sampling every stay independently (Pappalardo & Simini, 2016; Pappalardo et al., 2016; Schläpfer et al., 2021). TimeGeo shows that fixing home and work while generating flexible other activities can reproduce stay durations, visited-location counts, and daily mobility motifs with only a small set of temporal parameters (Jiang et al., 2016).

Semi-Markov models are the strongest support for your duration-aware activity-chain component because they model both what comes next and how long it lasts (Dube et al., 2025; et al., 2009). Simpler time-varying Markov chains can already generate daily activity sequences accurately at the individual level, so version one does not need a full synthetic census population to be useful (Wang & Osaragi, 2024).

### 3.3 Noise And Sampling

|Dimension|Evidence|Design Implication|Citations|
|---|---|---|---|
|Missingness pattern|Gaps are systematic, not random|Use on/off dropout blocks|(Yoo et al., 2020; Bähr et al., 2020)|
|Gap length|Long gaps bias mobility more|Sweep burst duration separately|(McCool et al., 2022)|
|Bursty pings|Local burst structure matters beyond global sparsity|Match burst starts, durations, within-burst rate|(Li & Barreras, 2024)|
|Stay detection|ST-DBSCAN remains strongest to 5-minute logs in Hiroshima|Keep MILES/ST-DBSCAN as detected baseline|(Kato et al., 2024)|
|Sequence segmentation|Gap imputation affects stop/move extraction|Keep oracle and detected modes separate|(Hwang et al., 2018)|

The strongest practical point is that missingness should not be simulated as iid dropped points. Smartphone datasets show systematic temporal gaps, inactivity-related undersampling, and device-dependent non-collection, while Garden City and related segmentation work show that clustered bursts and long silent periods alter stop outputs even at fixed overall ping frequency (Yoo et al., 2020; Kiang et al., 2021; Li & Barreras, 2024).

### 3.4 Error And Assignment

Urban GNSS error is not well approximated by a simple isotropic Gaussian. Building blockage and reflections create tens-of-meters errors, cross-street error inflation, direction dependence, and heavy-tailed pseudorange distributions, especially in deeper canyons (Groves, 2011; Xie & Petovello, 2015; Peretic et al., 2025; Li et al., 2026). Building morphology matters directly: higher buildings, narrow streets, and dense surroundings are associated with worse positioning, and building height over about 20 m within 100 m buffers was strongly associated with larger errors in Hong Kong (Li et al., 2026; Kim & Park, 2025; Wang et al., 2012).

That supports your idea of separating a stay-level offset from within-stay motion, but the literature suggests two cautions. First, error distributions can be heavy-tailed and context-sensitive rather than Gaussian, so outlier and tail parameters should be explicit (Li et al., 2026; Bantu & Wiora, 2025; Li et al., 2026). Second, POI attribution often fails when it relies on nearest-neighbor alone, especially in dense POI settings, which is why probabilistic and sequence-aware methods use dwell time, timing, personal history, semantics, and future/past context (Bhattacharya et al., 2015; Nishida et al., 2014; Saxena et al., 2025).

### Results Timeline

CRISPR-like step changes are not the story here; the timeline tracks how synthetic mobility and urban GPS evaluation converged into controllable sandbox designs.

- **2009**
    - 1 paper: ( et al., 2009)
- **2011**
    - 1 paper: (Groves, 2011)
- **2012**
    - 1 paper: (Wang et al., 2012)
- **2016**
    - 3 papers: (Pappalardo & Simini, 2016; Jiang et al., 2016; Pappalardo et al., 2016)
- **2017**
    - 2 papers: (Morris et al., 2017; Adjrad & Groves, 2017)
- **2019**
    - 1 paper: (Suzuki et al., 2019)
- **2020**
    - 1 paper: (Joubert & De Waal, 2020)
- **2021**
    - 1 paper: (Schläpfer et al., 2021)
- **2023**
    - 1 paper: (Liu et al., 2023)
- **2024**
    - 4 papers: (Li & Barreras, 2024; Zannat et al., 2024; Kato et al., 2024; Wang & Osaragi, 2024)
- **2025**
    - 2 papers: (Dube et al., 2025; Peretic et al., 2025)
- **2026**
    - 2 papers: (Yang et al., 2026; Li et al., 2026) **Figure 4:** Timeline of synthetic mobility and GPS benchmarking research

The arc runs from early activity-diary and mobility-law papers, through EPR and TimeGeo-style mechanistic generators, to recent controllable synthetic GPS sandboxes and uncertainty-aware POI inference. Larger markers indicate more citations.

### Top Contributors

Based on this corpus, Luca Pappalardo and Peter Groves are recurrent anchors for mobility generation and urban GNSS respectively, while recent synthetic mobility work clusters in GIS and transportation journals (Pappalardo & Simini, 2016; Groves, 2011; Chu et al., 2024).

|Type|Name|Papers|
|---|---|---|
|Author|Luca Pappalardo|(Pappalardo & Simini, 2016; Pappalardo et al., 2016)|
|Author|P. Groves|(Groves, 2011; Adjrad & Groves, 2017)|
|Author|Li-Ta Hsu|(Hsu et al., 2016; Sun et al., 2021; Wang & Osaragi, 2024)|
|Journal|_International Journal of Geographical Information Science_|(Lin et al., 2026; Chu et al., 2024; Arao & Maruyama, 2025)|
|Journal|_Journal of Navigation_|(Groves, 2011; Wang et al., 2012; Adjrad & Groves, 2017)|
|Journal|_IEEE Internet of Things Journal_|(Sun et al., 2021; Chang et al., 2020; Chen et al., 2024)|

**Figure 5:** Authors and journals appearing most frequently

## 4. Discussion

The literature strongly supports the overall architecture, but not every assumption equally. The modular split between activity-chain generation and GPS observation generation is well grounded, and repeated-place choice is much better supported than independent random stay assignment (Pappalardo & Simini, 2016; Jiang et al., 2016; Li & Barreras, 2024). The strongest empirical support also favors your oracle-versus-detected comparison, because stay extraction errors propagate directly into POI assignment and home/work inference (Suzuki et al., 2019; Verma et al., 2023; Kato et al., 2024).

The weaker parts are the exact GNSS error process and the city realism needed for transfer. Urban GNSS papers consistently show environment-conditioned, anisotropic, and heavy-tailed errors, but they usually model pseudorange or satellite-level measurement error, not directly the building-level stay cluster process you want (Yan et al., 2025; Sun et al., 2021; Sun et al., 2023). That means a stay-level shared offset is plausible as an engineering abstraction, but it should be treated as a tunable simulator component rather than as an empirically settled fact (Li & Barreras, 2024).

The practical build path is therefore clear: start simple, but calibrate aggressively. Use a small set of personas or survey-derived chains, recurrent anchors, constrained street-network travel, bursty missingness, oracle and detected outputs, and a context-conditioned noise model. Then use factorial simulation design with reported Monte Carlo error so threshold claims like “probabilistic assignment stops beating nearest-entity beyond X noise” are statistically defensible (Morris et al., 2017; Siepe et al., 2024; Koehler et al., 2009; Naimi et al., 2025).

|Claim|Evidence Strength|Reasoning|Papers|
|---|---|---|---|
|Synthetic known-truth data can validly benchmark GPS preprocessing pipelines|Evidence strength: Strong (9/10)|Multiple direct frameworks plus simulation-method guidance|Garden City, SGT, ADEMP (Li & Barreras, 2024; Zannat et al., 2024; Morris et al., 2017)|
|Repeated-place memory is necessary for realistic activity sequences|Evidence strength: Strong (8/10)|Strong mechanistic and empirical support from EPR, Ditras, TimeGeo|(Pappalardo & Simini, 2016; Jiang et al., 2016; Schläpfer et al., 2021)|
|Bursty dropout should be modeled explicitly, not as iid missing points|Evidence strength: Strong (8/10)|Real datasets show systematic gaps; sandbox studies show burst structure changes outputs|(Yoo et al., 2020; McCool et al., 2022; Li & Barreras, 2024)|
|Urban error should include heavy tails and environment dependence|Evidence strength: Moderate (7/10)|Consistent across GNSS studies, but mapping to stay-cluster abstraction is indirect|(Li et al., 2026; Peretic et al., 2025; Li et al., 2026)|
|A constant stay-level offset is the right universal abstraction|Evidence strength: Weak (3/10)|Plausible engineering simplification, but weak direct empirical validation|(Li & Barreras, 2024)|

**Figure 6:** Key claims and evidence strength

## 5. Conclusion

The literature supports your generator as a legitimate methodological project, not just a convenience tool. The strongest evidence backs the need for known truth, recurrent anchor places, bursty missingness, separate oracle and detected outputs, and explicit environment-conditioned noise; the least supported piece is the exact parametric form of the stay-level error process (Li & Barreras, 2024; Kato et al., 2024; Li et al., 2026).

### Research Gaps

This corpus is rich on trajectory generators and urban GNSS correction, but much thinner on end-to-end synthetic benchmarks that directly connect activity chains, raw point generation, stay detection, and POI assignment under one controllable framework. The matrix below maps that uneven coverage.

|                 | Sequence Model | Map Context | Burst Gaps | Error Tails | Benchmarking |
| --------------- | -------------- | ----------- | ---------- | ----------- | ------------ |
| Activity Chains | 22 papers      | 4 papers    | 2 papers   | 1 paper     | 11 papers    |
| Sparse Sampling | 7 papers       | 3 papers    | 5 papers   | 3 papers    | 5 papers     |
| Urban GNSS      | 8 papers       | 17 papers   | No papers  | 19 papers   | 22 papers    |
| POI Assignment  | 7 papers       | 4 papers    | No papers  | 2 papers    | 8 papers     |
| Ground Truth    | 5 papers       | 3 papers    | 1 paper    | 3 papers    | 13 papers    |

The sharpest gap is the lack of papers that jointly model urban-form-conditioned GPS error and evaluate its downstream effect on stay detection and POI assignment in one sandbox. Garden City comes closest on bursty sampling and truth exposure but uses Gaussian coordinate noise rather than a richer urban canyon error model (Li & Barreras, 2024). Urban GNSS studies are rich on building-conditioned error and anisotropy, but they usually optimize positioning itself rather than downstream mobility preprocessing (Wang et al., 2012; Chen et al., 2024; Adjrad & Groves, 2017). Hiroshima benchmarking identifies ST-DBSCAN robustness to 5-minute logs, yet does not isolate error sources one at a time, which is exactly where your simulator adds value (Kato et al., 2024).

### Open Research Questions

The next studies should focus on the assumptions most likely to change downstream conclusions.

|Question|Why|
|---|---|
|**At what combinations of local ping burstiness, GNSS offset variance, and POI density does probabilistic assignment stop outperforming nearest-entity baselines?**|This directly operationalizes your threshold objective and links sampling, spatial error, and dense-place ambiguity in one benchmark.|
|**Which context features best predict stay-cluster offset and within-stay dispersion: building height, sky-view, indoor status, or street aspect ratio?**|Current GNSS work implicates all four, but no benchmark translates them into downstream stop and POI assignment error.|
|**How much of observed assignment error in Hiroshima-like pipelines comes from stay detection versus location attribution?**|Oracle-versus-detected paired evaluation would quantify where model improvement effort matters most.|

A modular synthetic GPS generator with truth tables is therefore well supported by the literature, and the best version is one that starts simple, exposes every latent state, and calibrates each bias source separately.

_These search results were found and analyzed using Consensus, an AI-powered search engine for research. Try it at [https://consensus.app](https://consensus.app). © 2026 Consensus NLP, Inc. Personal, non-commercial use only; redistribution requires copyright holders’ consent._

## References

T., Raux, C., Cornélis, E., & Joly, I. (2009). Multistate Nonhomogeneous Semi-Markov Model of Daily Activity Type, Timing, and Duration Sequence. _Transportation Research Record, 2134_, 123 - 134. [https://doi.org/10.3141/2134-15](https://doi.org/10.3141/2134-15)

Adjrad, M., & Groves, P. (2017). Intelligent Urban Positioning: Integration of Shadow Matching with 3D-Mapping-Aided GNSS Ranging. _Journal of Navigation, 71_, 1 - 20. [https://doi.org/10.1017/s0373463317000509](https://doi.org/10.1017/s0373463317000509)

Adjrad, M., & Groves, P. (2017). Enhancing Least Squares GNSS Positioning with 3D Mapping without Accurate Prior Knowledge. _Annual of Navigation, 64_, 75-91. [https://doi.org/10.1002/navi.178](https://doi.org/10.1002/navi.178)

Arao, S., & Maruyama, T. (2025). Inferring in-home/out-of-home situations unreported in time-use surveys using supervised machine learning. _Travel Behaviour and Society_. [https://doi.org/10.1016/j.tbs.2024.100928](https://doi.org/10.1016/j.tbs.2024.100928)

Bähr, S., Haas, G., Keusch, F., Kreuter, F., & Trappmann, M. (2020). Missing Data and Other Measurement Quality Issues in Mobile Geolocation Sensor Data. _Social Science Computer Review, 40_, 212 - 235. [https://doi.org/10.1177/0894439320944118](https://doi.org/10.1177/0894439320944118)

Bantu, A., & Wiora, J. (2025). Impact of Non-Gaussian Noise on Position Accuracy Provided by Global Navigation Satellite Systems (GNSS). _IEEE Access, 13_, 161750-161761. [https://doi.org/10.1109/access.2025.3610048](https://doi.org/10.1109/access.2025.3610048)

Bhattacharya, T., Kulik, L., & Bailey, J. (2015). Automatically recognizing places of interest from unreliable GPS data using spatio-temporal density estimation and line intersections. _Pervasive Mob. Comput., 19_, 86-107. [https://doi.org/10.1016/j.pmcj.2014.08.003](https://doi.org/10.1016/j.pmcj.2014.08.003)

Chang, S., Pierson, E., Koh, P. W., Gerardin, J., Redbird, B., Grusky, D., & Leskovec, J. (2020). Mobility network models of COVID-19 explain inequities and inform reopening. _Nature, 589_, 82 - 87. [https://doi.org/10.1038/s41586-020-2923-3](https://doi.org/10.1038/s41586-020-2923-3)

Chen, W., Zhang, C.-L., Peng, Y., Yao, Y., Cai, M., & Dong, D. (2024). Enhancing GNSS Positioning in Urban Canyon Areas via a Modified Design Matrix Approach. _IEEE Internet of Things Journal, 11_, 10252-10265. [https://doi.org/10.1109/jiot.2023.3326971](https://doi.org/10.1109/jiot.2023.3326971)

Chu, C., Zhang, H., Wang, P., & Lu, F. (2024). Simulating human mobility with a trajectory generation framework based on diffusion model. _International Journal of Geographical Information Science, 38_, 847 - 878. [https://doi.org/10.1080/13658816.2024.2312199](https://doi.org/10.1080/13658816.2024.2312199)

Dube, R., Gautam, N., Banerjee, A., & Nagarajan, H. (2025). Hierarchical Semi-Markov Models with Duration-Aware Dynamics for Activity Sequences. _Energy and Buildings_. [https://doi.org/10.1016/j.enbuild.2026.117338](https://doi.org/10.1016/j.enbuild.2026.117338)

Groves, P. (2011). Shadow Matching: A New GNSS Positioning Technique for Urban Canyons. _Journal of Navigation, 64_, 417 - 430. [https://doi.org/10.1017/s0373463311000087](https://doi.org/10.1017/s0373463311000087)

Hsu, L.-T., Gu, Y., & Kamijo, S. (2016). 3D building model-based pedestrian positioning method using GPS/GLONASS/QZSS and its reliability calculation. _GPS Solutions, 20_, 413-428. [https://doi.org/10.1007/s10291-015-0451-7](https://doi.org/10.1007/s10291-015-0451-7)

Hwang, S., Vandemark, C., Dhatt, N., Yalla, S. V., & Crews, R. (2018). Segmenting human trajectory data by movement states while addressing signal loss and signal noise. _International Journal of Geographical Information Science, 32_, 1391 - 1412. [https://doi.org/10.1080/13658816.2018.1423685](https://doi.org/10.1080/13658816.2018.1423685)

Jiang, S., Yang, Y., Gupta, S., Veneziano, D., Athavale, S., & González, M. C. (2016). The TimeGeo modeling framework for urban mobility without travel surveys. _Proceedings of the National Academy of Sciences, 113_, E5370 - E5378. [https://doi.org/10.1073/pnas.1524261113](https://doi.org/10.1073/pnas.1524261113)

Joubert, J., & De Waal, A. (2020). Activity-based travel demand generation using Bayesian networks. _Transportation Research Part C: Emerging Technologies_. [https://doi.org/10.1016/j.trc.2020.102804](https://doi.org/10.1016/j.trc.2020.102804)

Kato, R., Luo, L.-C., Fourie, P., C., Wakasa, H., Fujiwara, A., & Chikaraishi, M. (2024). Evaluating and Validating Stay Point Detection Algorithms with different GPS Log Intervals. 803-808. [https://doi.org/10.1016/j.procs.2024.06.095](https://doi.org/10.1016/j.procs.2024.06.095)

Kiang, M., Chen, J. T., Krieger, N., Buckee, C., Alexander, M. J., Baker, J., Buckner, R., Coombs, G., Rich-Edwards, J., Carlson, K., & Onnela, J. (2021). Sociodemographic characteristics of missing data in digital phenotyping. _Scientific Reports, 11_. [https://doi.org/10.1038/s41598-021-94516-7](https://doi.org/10.1038/s41598-021-94516-7)

Kim, H.-I., & Park, K.-D. (2025). Satellite Positioning Accuracy Improvement in Urban Canyons Through a New Weight Model Utilizing GPS Signal Strength Variability. _Sensors (Basel, Switzerland), 25_. [https://doi.org/10.3390/s25154678](https://doi.org/10.3390/s25154678)

Koehler, E., Brown, E. R., & Haneuse, S. (2009). On the Assessment of Monte Carlo Error in Simulation-Based Statistical Analyses. _The American statistician, 63_, 155 - 162. [https://doi.org/10.1198/tast.2009.0030](https://doi.org/10.1198/tast.2009.0030)

Li, T. H., & Barreras, F. (2024). Garden city: A synthetic dataset and sandbox environment for analysis of pre-processing algorithms for GPS human mobility data. _ArXiv, abs/2412.00913_. [https://doi.org/10.48550/arxiv.2412.00913](https://doi.org/10.48550/arxiv.2412.00913)

Li, Z., Yan, P., Song, B., & Hsu, L.-T. (2026). Improved GNSS Positioning in Urban Environments Using a Logistic Error Model. _ION Pacific PNT_. [https://doi.org/10.33012/2026.20582](https://doi.org/10.33012/2026.20582)

Li, T., Cao, Y., & Mckenzie, G. (2026). A Multi‐Scale Approach to Assessing Positioning Accuracy in High‐Density Urban Environments of Hong Kong. _Transactions in GIS, 30_. [https://doi.org/10.1111/tgis.70195](https://doi.org/10.1111/tgis.70195)

Li, Z., Yan, P., Wen, W., & Hsu, L.-T. (2026). Cauchy–Gaussian Overbound for Heavy-Tailed GNSS Measurement Errors. _NAVIGATION: Journal of the Institute of Navigation_. [https://doi.org/10.33012/navi.749](https://doi.org/10.33012/navi.749)

Lin, Z.-H., Grinberger, A., & Felsenstein, D. (2026). Generating geospatial trajectories with incomplete data using graph inverse reinforcement learning. _International Journal of Geographical Information Science_. [https://doi.org/10.1080/13658816.2026.2658065](https://doi.org/10.1080/13658816.2026.2658065)

Liu, K., Jin, X., Cheng, S., Gao, S., Yin, L., & Lu, F. (2023). Act2Loc: a synthetic trajectory generation method by combining machine learning and mechanistic models. _International Journal of Geographical Information Science, 38_, 407 - 431. [https://doi.org/10.1080/13658816.2023.2292570](https://doi.org/10.1080/13658816.2023.2292570)

McCool, D., Lugtig, P., & Schouten, B. (2022). Maximum interpolable gap length in missing smartphone-based GPS mobility data. _Transportation, 51_, 297-327. [https://doi.org/10.1007/s11116-022-10328-2](https://doi.org/10.1007/s11116-022-10328-2)

Morris, T., White, I., & Crowther, M. (2017). Using simulation studies to evaluate statistical methods. _Statistics in Medicine, 38_, 2074 - 2102. [https://doi.org/10.1002/sim.8086](https://doi.org/10.1002/sim.8086)

Naimi, A. I., Benkeser, D., & Rudolph, J. E. (2025). Computing True Parameter Values in Simulation Studies Using Monte Carlo Integration. _Epidemiology (Cambridge, Mass.), 36_, 690 - 693. [https://doi.org/10.1097/ede.0000000000001873](https://doi.org/10.1097/ede.0000000000001873)

Nishida, K., Toda, H., Kurashima, T., & Suhara, Y. (2014). Probabilistic identification of visited point-of-interest for personalized automatic check-in. _Proceedings of the 2014 ACM International Joint Conference on Pervasive and Ubiquitous Computing_. [https://doi.org/10.1145/2632048.2632092](https://doi.org/10.1145/2632048.2632092)

Pappalardo, L., & Simini, F. (2016). Data-driven generation of spatio-temporal routines in human mobility. _Data Mining and Knowledge Discovery, 32_, 787 - 829. [https://doi.org/10.1007/s10618-017-0548-4](https://doi.org/10.1007/s10618-017-0548-4)

Pappalardo, L., Rinzivillo, S., & Simini, F. (2016). Human Mobility Modelling: Exploration and Preferential Return Meet the Gravity Model. 934-939. [https://doi.org/10.1016/j.procs.2016.04.188](https://doi.org/10.1016/j.procs.2016.04.188)

Peretic, M., Gilabert, R., Carroll, J., Gutierrez, J., Moore, A., Christie, J., & Dill, E. T. (2025). Statistical Analysis of GNSS Multipath Errors in Urban Canyons. _2025 IEEE/ION Position, Location and Navigation Symposium (PLANS)_, 1216-1225. [https://doi.org/10.1109/plans61210.2025.11028411](https://doi.org/10.1109/plans61210.2025.11028411)

Saxena, N., Hsu, S.-L., Shetty, M., Alkhadra, O., Shahabi, C., & Horn, A. L. (2025). POIFormer: A Transformer-Based Framework for Accurate Point-of-Interest Attribution. _Proceedings of the ... ACM SIGSPATIAL International Conference on Advances in Geographic Information Systems : ACM GIS. ACM SIGSPATIAL International Conference on Advances in Geographic Information Systems, 2025_, 607 - 619. [https://doi.org/10.1145/3748636.3762775](https://doi.org/10.1145/3748636.3762775)

Schläpfer, M., Dong, L., O'Keeffe, K., Santi, P., Szell, M., Salat, H., Anklesaria, S., Vazifeh, M., Ratti, C., & West, G. (2021). The universal visitation law of human mobility. _Nature, 593_, 522 - 527. [https://doi.org/10.1038/s41586-021-03480-9](https://doi.org/10.1038/s41586-021-03480-9)

Siepe, B. S., Bartoš, F., Morris, T. P., Boulesteix, A., Heck, D. W., & Pawel, S. (2024). Simulation Studies for Methodological Research in Psychology: A Standardized Template for Planning, Preregistration, and Reporting. _Psychological methods_. [https://doi.org/10.1037/met0000695](https://doi.org/10.1037/met0000695)

Sun, R., Wang, G., Cheng, Q., Fu, L., Chiang, K.-W., Hsu, L.-T., & Ochieng, W. (2021). Improving GPS Code Phase Positioning Accuracy in Urban Environments Using Machine Learning. _IEEE Internet of Things Journal, 8_, 7065-7078. [https://doi.org/10.1109/jiot.2020.3037074](https://doi.org/10.1109/jiot.2020.3037074)

Sun, R., Fu, L., Cheng, Q., Chiang, K.-W., & Chen, W. (2023). Resilient Pseudorange Error Prediction and Correction for GNSS Positioning in Urban Areas. _IEEE Internet of Things Journal, 10_, 9979-9988. [https://doi.org/10.1109/jiot.2023.3235483](https://doi.org/10.1109/jiot.2023.3235483)

Suzuki, J., Suhara, Y., Toda, H., & Nishida, K. (2019). Personalized Visited-POI Assignment to Individual Raw GPS Trajectories. _ACM Transactions on Spatial Algorithms and Systems (TSAS), 5_, 1 - 28. [https://doi.org/10.1145/3317667](https://doi.org/10.1145/3317667)

Verma, R., Mittal, S., Lei, Z., Chen, X., & Ukkusuri, S. (2023). Comparison of home detection algorithms using smartphone GPS data. _EPJ Data Science, 13_, 1-22. [https://doi.org/10.1140/epjds/s13688-023-00447-w](https://doi.org/10.1140/epjds/s13688-023-00447-w)

Wang, W., & Osaragi, T. (2024). Generating and understanding human daily activity sequences using Time-Varying Markov Chain models. _Travel Behaviour and Society_. [https://doi.org/10.1016/j.tbs.2023.100711](https://doi.org/10.1016/j.tbs.2023.100711)

Wang, L., Groves, P., & Ziebart, M. (2012). Multi-Constellation GNSS Performance Evaluation for Urban Canyons Using Large Virtual Reality City Models. _Journal of Navigation, 65_, 459-476. [https://doi.org/10.1017/s0373463312000082](https://doi.org/10.1017/s0373463312000082)

Xie, P., & Petovello, M. (2015). Measuring GNSS Multipath Distributions in Urban Canyon Environments. _IEEE Transactions on Instrumentation and Measurement, 64_, 366-377. [https://doi.org/10.1109/tim.2014.2342452](https://doi.org/10.1109/tim.2014.2342452)

Yan, P., Xia, X., Brizzi, M., Wen, W., & Hsu, L.-T. (2025). Subspace-Based Adaptive GMM Error Modeling for Fault-Aware Pseudorange-Based Positioning in Urban Canyons. _IEEE Transactions on Intelligent Vehicles, 10_, 3222-3237. [https://doi.org/10.1109/tiv.2024.3450198](https://doi.org/10.1109/tiv.2024.3450198)

Yang, B., H., Liu, Y., Zhang, Z., Stanford, C., Sun, M., & J.-Q. (2026). Uncertainty-Aware Trip Purpose Inference from GPS Trajectories via POI Semantic Zones and Pareto Calibration. _ArXiv, abs/2605.01257_. [https://doi.org/10.48550/arxiv.2605.01257](https://doi.org/10.48550/arxiv.2605.01257)

Yoo, E.-H., Roberts, J. E., Eum, Y., & Shi, Y. (2020). Quality of hybrid location data drawn from GPS-enabled mobile phones: Does it matter?. _Transactions in GIS : TG, 24_, 462 - 482. [https://doi.org/10.1111/tgis.12612](https://doi.org/10.1111/tgis.12612)

Zannat, K. E., Choudhury, C. F., Hess, S., & Watling, D. (2024). Investigating the relative accuracy of GPS, GSM and CDR data for inferring spatiotemporal travel trajectories. _IET Intelligent Transport Systems_. [https://doi.org/10.1049/itr2.12563](https://doi.org/10.1049/itr2.12563)


<div class="backlinks" markdown>

**Linked from** [GPS toy data](d-toy-data.md) · [Publications and doctoral plan](../progress/d-progress-20-10-2026.md)

</div>
