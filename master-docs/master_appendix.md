# Appendix

```
====================================================================================================
PROJECT: Evaluating Predictive Techniques to Model Stochastic Airport Passenger Flow
AUTHOR: Leila Gleich | INSTITUTION: Embry-Riddle Aeronautical University
DEGREE: Master of Science in Aeronautics / Aviation Data Analytics (MSAA / Gleich 700B)
MANUSCRIPT COMPILATION: Appendix v4 (Master Merged Empirical & Methodological Appendices)
DATE: October 10, 2026
COMPANION WORKBOOK: master_thesis_tables.xlsx (30 Conformed Analytical Tabs)
====================================================================================================
```

## Overview and Master Table of Contents

This appendix compiles the comprehensive econometric derivations, queuing theory foundations, data pipeline architectures, and empirical holdout evaluations supporting the master's thesis *Evaluating Predictive Techniques to Model Stochastic Airport Passenger Flow*. Synthesizing and expanding all prior working drafts (*Appendix v1*, *Appendix v2*, *Appendix v3*, and *Chapter II Technical Appendices*), this document eliminates redundancy while preserving complete operational detail across 14 lettered appendices (A through N), arranged strictly in sequential order of citation across Chapters I through V.

A foundational methodological principle established across this research is that airport terminal queue stability and passenger delay risks are governed not merely by static passenger volumes, but by the **volatility of checkpoint throughput** (within-day standard deviation $\sigma_{\text{TSA, hr}}$, scale-free Coefficient of Variation $CV_{\text{TSA}}$, and multi-day temporal dispersion $\sigma_{\text{TSA, 7d}}$). Under Kingman's heavy-traffic queuing formula ($W_q \approx \frac{\rho}{1-\rho} \frac{C_a^2 + C_s^2}{2} \frac{1}{\mu}$), expected waiting times scale quadratically with arrival volatility ($C_a^2$) as checkpoint lane utilization approaches capacity ($\rho \to 1.0$). Accordingly, all operational terms, econometric models, and evaluation dimensions defined herein are grounded in authentic commercial aviation operations, airline flight scheduling banks, and airport passenger flow dynamics.

All tables referenced throughout this appendix are compiled with full conformed data, automated calculations, and APA 7th Edition typography in the companion multi-tab Excel workbook:  
**`thesis_docs/manuscripts/Appendix/master_thesis_tables.xlsx`** (also mirrored at **`results/appendix_tables.xlsx`**).

---

# Appendix A: Delimitations, Research Limitations, and Methodological Assumptions

> **Operational Cross-Reference**: This appendix establishes the formal operational boundaries, geographic coverage, longitudinal timeline, and the 14-point methodological assumption matrix designed to protect internal and external construct validity. It is referenced in **Chapter I (Introduction)**, Section 1.6 (*Delimitations*) and Section 1.7 (*Limitations and Assumptions*); in **Chapter III (Methodology)**, Section 3.4 (*Internal Validity Threats and Remediation Protocols*); and in **Chapter V (Discussion)**, Section 5.6 (*Strategic Implications for Airport and Security Authorities (Operational and Methodological Boundaries)*).

## A.1 Research Delimitations and Scope Boundaries

The scope of this investigation is delimited to commercial passenger checkpoint screening operations across the highest-density airfields of the United States National Airspace System (NAS). Specifically, the empirical analysis focuses on the 2019 through 2025 longitudinal baseline, evaluating commercial aviation movements and passenger screening throughput across the Top 25 passenger hub airports.

The geographical boundaries are restricted to commercial airports located within the contiguous United States, Hawaii, and Alaska that report complete flight operations under Bureau of Transportation Statistics (BTS) Form 234 and maintain dedicated Transportation Security Administration (TSA) passenger screening lanes. General aviation facilities, international pre-clearance screening operations outside the United States, military airfields, and dedicated all-cargo operations (e.g., FedEx Express SuperHub at MEM and UPS Worldport at SDF) are formally excluded from the scope of analysis.

Temporal delimitations partition the multi-year timeline into distinct operational eras. While multi-year descriptive baselines examine 2019–2025 trends, predictive model training, validation, and holdout benchmarking are strictly delimited to the modern post-pandemic operational regime beginning May 1, 2022 (following the judicial vacatur and federal repeal of the transportation mask mandate). This boundary excludes pandemic-era demand collapse distortions while evaluating modern commercial airline flight schedules, load factors, and screening patterns under contemporary operating rules.

## A.2 Operational Boundary Constraints and Limitations

Empirical modeling of public federal aviation feeds involves three primary operational boundary constraints:

1. **Staffing and Lane Configuration Opacity**: Due to the proprietary and security-sensitive nature of TSA checkpoint operations, confidential operational variables—such as exact Transportation Security Officer (TSO) shift allocations, active physical lane open/close timestamps per 15-minute interval, canine-assisted screening deployments, and manual queue snake reconfigurations—are not publicly accessible. The research design controls for this opacity by modeling aggregated checkpoint complex throughput totals and deriving scale-free relative arrival burstiness ($CV_{\text{TSA}}$) rather than unobserved micro-lane service times.

2. **Connecting Passenger Estimation Stability**: The proportion of transferring passengers who remain entirely within secure airside sterile areas (and thus never enter landside security screening lobbies) is estimated using quarterly BTS DB1B origin-destination ticket coupon surveys. The analytical framework assumes that quarterly connecting ratios remain stable across monthly operating horizons within given carrier-terminal complexes, reflecting published carrier bank scheduling structures.

3. **Operational Exogeneity of Severe Weather Shocks**: Severe convective weather disruptions, winter storm systems, and ground delay programs (GDP) are treated as exogenous operational shocks. These external disruptions are operationalized through realized flight departure delay distributions, tactical cancellation counts, and taxi-out queue times reported in BTS Form 234 rather than direct meteorological radar feeds.

## A.3 Foundational Methodological Assumptions and Failure Mode Prevention

To ensure rigorous internal and external construct validity across all downstream models, 14 foundational methodological assumptions were operationalized across terminal flow, temporal coupling, sample filtering, and econometric evaluation:

* **Terminal Flow Assumptions**:
  - *Non-traveler exits are negligible*: Terminal gate passes, meet-and-greet visitors, and aborted boardings represent $\ll 1\%$ of peak bank throughput volume, preventing over-parameterized lobby noise.
  - *Connecting passengers bypass security*: Sterile area connecting passengers never enter landside screening, resolving throughput paradoxes at mega-connecting hubs (e.g., CLT with $76\%$ transfers).
  - *Exclusion of inbound arrivals*: Arriving passengers exit directly through one-way security doors, preventing ghost demand and spurious arrival correlations.
  - *Exhaustive nationwide departures*: Physical checkpoints serve all domestic flight departures, preventing truncation bias from omitted destination spoke volume.

* **Temporal Coupling Assumptions**:
  - *90–120 minute lead time window*: Checkpoint screening precedes flight departures under an empirical lognormal arrival density function (mode $\approx 92.5$ min), preventing phase-shift misspecification.
  - *Zero lookahead leakage*: Predictive models rely strictly on information available prior to the operating hour, eliminating target leakage from realized post-departure attributes.

* **Sample Filtering Assumptions**:
  - *Top 25 macro power-law cutoff*: Isolates airfields capturing $67.2\%$ of nationwide commercial volume where heavy-traffic utilization approaches capacity ($\rho \to 1.0$), avoiding light-traffic triviality ($\rho \ll 0.30$).
  - *Micro checkpoint exclusivity*: Selects carrier complexes where a single airline commands $\ge 85\%$ of concourse gates, eliminating shared-lobby multi-carrier collinearity ($\text{Corr} \ge 0.75$).
  - *Meso Big 3 co-location*: Compares American, Delta, and United across identical TRACON weather shocks, differencing out localized regional disruption bias.
  - *Exclusion of Southwest Airlines (WN)*: Eliminates unassigned seating boarding position maximizers whose bimodal arrival behavior violates passenger parameter exchangeability.
  - *Post-pandemic May 1, 2022 demarcation*: Excludes structural pandemic recovery regime shifts, establishing macroeconomic stability.

* **Evaluation Assumptions**:
  - *Orthogonal 4 x 4 factorial design*: Balances exactly 4 exclusive complexes per carrier across 4 operational cluster archetypes, eliminating unbalanced ANOVA variance inflation.
  - *Twin TRACON disruption controls*: Evaluates matched weather shocks across dual facilities (EWR vs. LGA Terminal C) to eliminate geographic convective bias in resilience benchmarking.

<div class="table-callout">

### Table A.1
*14-Point Methodological Assumption and Failure Mode Prevention Matrix*

[**Companion Excel Tab:** `'Table_A1_Assumptions'` in `master_thesis_tables.xlsx`]  
*Note. Formulated across terminal flow, temporal coupling, sample filtering, and econometric evaluation to protect internal and construct validity.*

*(Note. Full conformed tabular data, mathematical models, and statistical derivations are provided in companion workbook master_thesis_tables.xlsx).*

</div>

<div class="table-callout">

### Table A.2
*Research Delimitations and Top 25 Commercial Airport Network Inclusion Criteria*

[**Companion Excel Tab:** `'Table_A2_Delimitations'` in `master_thesis_tables.xlsx`]  
*Note. Establishes commercial aviation inclusion criteria, power-law concentration (67.2% nationwide volume), and geographic coverage.*

*(Note. Full conformed tabular data, mathematical models, and statistical derivations are provided in companion workbook master_thesis_tables.xlsx).*

</div>

---

# Appendix B: Comparative Modeling Paradigms and Literature Equation Registry

> **Operational Cross-Reference**: This appendix establishes the theoretical trade-offs across candidate modeling paradigms evaluated in the literature and catalogs all formal peer-reviewed equations used in the thesis. It is referenced in **Chapter II (Review of the Relevant Literature)**, Section 2.3 (*Methodological Paradigms in Checkpoint Forecasting*); in **Chapter III (Methodology)**, Section 3.2 (*Model Selection and Mathematical Formulation*); and in **Chapter IV (Results)**, Section 4.4 (*Holdout Benchmark Results*).

## B.1 Comparative Modeling Paradigm Taxonomy for Airport Screening Facilities

Forecasting stochastic passenger arrivals at commercial airport checkpoints has historically engaged four distinct analytical paradigms, each presenting inherent structural trade-offs between physical interpretability, computational complexity, and disruption resilience:

1. **Classical Queuing Formulations ($M/M/s$, $M/G/s$, NHPP)**: Grounded in steady-state Markovian assumptions, classical queuing models yield elegant closed-form solutions for waiting times and queue lengths. However, their reliance on stationary Poisson arrival rates ($\lambda$) causes catastrophic breakdown under scheduled flight banks, where hundreds of passengers arrive simultaneously in tight batches. Furthermore, they treat all ticketed passengers as landside arrivals, ignoring airside connecting passenger shielding.

2. **Discrete Event Simulation (DES / ARENA / SIMMOD / CAST)**: Micro-simulation models track individual passenger entities through physical screening checkpoints, bag divestiture rollers, and walk-through metal detectors. While providing high layout fidelity, DES requires exhaustive manual calibration of passenger divestiture times and TSO shift changes. Crucially, DES exhibits severe computational latency (often $> 15$ minutes per run), preventing dynamic real-time operational decision support during fast-moving convective ground delay programs.

3. **Linear Statistical Time Series (ARIMA / SARIMA / SARIMAX)**: Autoregressive models capture recurring diurnal (24-hour) and weekly (168-hour) cycles with minimal computational overhead. However, linear formulations suffer from univariate blindness: they cannot dynamically ingest real-time flight delays, cancellations, or taxi-out congestion. During irregular operations (IROPS), autoregressive extrapolations fail catastrophically because past passenger arrival trends no longer match disrupted flight departure realities.

4. **Deep Sequence Neural Networks (LSTM / GRU / Transformer)**: Recurrent neural architectures model complex non-linear sequence dependencies. However, deep sequence models operate as opaque 'black boxes', encountering strong operational resistance from airport Federal Security Directors (FSDs) who require auditable decision rules. Furthermore, deep neural networks overfit heavily to local terminal geometry, collapsing by more than $40\%$ when transferred zero-shot to unfamiliar airport layouts.

5. **Supervised Machine Learning Ensembles (Histogram Gradient Boosting / XGBoost)**: Decision-tree ensembles capture complex non-linear interactions between BTS operational features (flight departure delays, cancellations, taxi queues) and checkpoint demand. While winning routine Pareto efficiency under nominal conditions with zero feedback compute latency, unconstrained decision trees collapse during severe disruptions due to the **Empty Checkpoint Fallacy**.

6. **Sequential Two-Stage State-Space Hybrids (Schedule Convolution + Tree Residual + Live Innovation Feedback)**: Sequential two-stage models unite the physical stability of flight schedules with live 1-step error innovation feedback ($e_{t-1} = y_{t-1} - \hat{y}_{t-1}$) from the checkpoint floor. This architecture achieves optimal shock resilience ($R_{\text{MASE}} = 1.05$, $TTR = 2.8$h), resolving the Empty Checkpoint Fallacy during severe disruptions.

<div class="table-callout">

### Table B.1
*Comparative Modeling Paradigm Taxonomy for Airport Security Screening Facilities*

[**Companion Excel Tab:** `'Table_B1_Paradigms'` in `master_thesis_tables.xlsx`]  
*Note. Master census of all 20 peer-reviewed operational, queuing, econometrics, and lane allocation equations utilized across Chapters I–V.*

*(Note. Full conformed tabular data, mathematical models, and statistical derivations are provided in companion workbook master_thesis_tables.xlsx).*

</div>

---

# Appendix C: Queuing Theory Derivations, Heavy-Traffic Approximations, and Volatility Dispersion Formulations

> **Operational Cross-Reference**: This appendix establishes the formal mathematical derivations of heavy-traffic queuing approximations, compound Poisson dispersion mechanics, and primary throughput volatility targets. It is referenced in **Chapter II (Literature Review)**, Section 2.1 (*Theoretical Foundations: Queuing Theory and Kingman's Heavy-Traffic Approximations*) and Section 2.2 (*Volume Versus Volatility*); in **Chapter III (Methodology)**, Section 3.1 (*Core Research Target: Throughput Volatility*); and in **Chapter IV (Results)**, Section 4.2 (*Intraday Volatility Dynamics*).

## C.1 Classical Poisson and Kendall Notation Formulations

In classical queuing systems, screening facilities are formalized using Kendall notation $A/S/c/K/N/D$, typically reduced to $A/S/s$, where $A$ represents the inter-arrival time distribution, $S$ represents the service time distribution, and $s$ denotes the number of parallel active screening lanes. In an $M/M/s$ queuing model, arrival intervals follow a Poisson process with arrival rate $\lambda$, and service durations adhere to an exponential distribution with service rate $\mu$ per active screening lane. The operational traffic intensity (utilization rate) $\rho$ is formulated as:

$$
\rho = \frac{\lambda}{s \cdot \mu}
$$

Under steady-state equilibrium ($\rho < 1.0$), the probability of zero entities in the system $P_0$ and the expected waiting time in queue $W_q$ are derived from Erlang-C formulations:

$$
P_0 = \left[ \sum_{n=0}^{s-1} \frac{(s \cdot \rho)^n}{n!} + \frac{(s \cdot \rho)^s}{s! \cdot (1 - \rho)} \right]^{-1}
$$

$$
W_q = \left[ \frac{(s \cdot \rho)^s}{s! \cdot (1 - \rho)^2 \cdot s \cdot \mu} \right] \cdot P_0
$$

## C.2 Non-Homogeneous Poisson Processes (NHPP)

To accommodate the time-varying nature of airline flight schedules, Non-Homogeneous Poisson Processes (NHPP) replace static arrival rate $\lambda$ with an integrable, deterministic time-dependent rate function $\lambda(t)$. The expected cumulative arrival count $m(t)$ over interval $[0, t]$ is formulated as:

$$
m(t) = \int_0^t \lambda(u) \, du
$$

While NHPP accommodates diurnal wave patterns, it remains fundamentally bounded by the assumption of independent increments, failing to account for intra-bank passenger correlations where ticketed passenger cohorts arrive in tight, non-independent clusters.

## C.3 Heavy-Traffic Queuing and the Kingman / Allen-Cunneen Approximations

In heavy-traffic regimes where lane utilization approaches maximum saturation ($\rho \to 1.0$), the Allen-Cunneen approximation for general $G/G/s$ screening facilities demonstrates that expected waiting times scale linearly not with mean volume, but with arrival and service volatility:

$$
W_q \approx \left[ \frac{C_a^2 + C_s^2}{2} \right] \cdot \left[ \frac{\rho}{1 - \rho} \right] \cdot \left( \frac{1}{s \cdot \mu} \right)
$$

where $C_a^2 = \frac{\text{Var}(T_a)}{[\mathbb{E}(T_a)]^2}$ is the squared coefficient of variation of inter-arrival times, and $C_s^2 = \frac{\text{Var}(T_s)}{[\mathbb{E}(T_s)]^2}$ is the squared coefficient of variation of screening durations. As utilization $\rho$ approaches $1.0$ during scheduled flight bank departures, the non-linear scaling multiplier $\left[ \frac{\rho}{1 - \rho} \right]$ amplifies arrival volatility $C_a^2$ exponentially, triggering terminal crowd surges.

## C.4 Tweedie-Poisson Compound Dispersion Mechanics

The relationship between passenger arrival volume and intraday volatility is governed by compound Poisson dispersion. Checkpoint hourly arrival counts $Y_t$ follow an exponential dispersion model where the variance scales as a power function of the mean volume:

$$
\text{Var}(Y_t) = \phi \cdot [\mathbb{E}(Y_t)]^p
$$

where $p \in (1, 2)$ represents a Tweedie compound Poisson-gamma distribution, and $\phi$ is the dispersion scale parameter. Because intraday variance $\sigma_{\text{TSA, hr}}$ naturally expands alongside total scheduled seats, published flight schedules provide an accurate baseline predictor for routine volume. Conversely, multi-day volatility $\sigma_{\text{TSA, 7d}}$ is driven by disruption volatility (flight cancellation rates, delay spreads, and gate holds).

## C.5 Scale-Free Coefficient of Variation ($CV_{\text{TSA}}$) and Multi-Day Volatility Formulations

Construct validity requires establishing explicit mathematical formulations that target passenger throughput volatility rather than static volume levels:

1. **Intraday Diurnal Absolute Volatility ($\sigma_{\text{TSA, hr}}$, pax/hr dispersion)**:


$$
\sigma_{\text{TSA, hr}}(d) = \sqrt{\frac{1}{23} \sum_{h=0}^{23} (Y_{d, h} - \bar{Y}_d)^2}
$$

2. **Intraday Scale-Free Relative Volatility ($CV_{\text{TSA, hr}}$, dimensionless ratio)**:


$$
CV_{\text{TSA, hr}}(d) = \frac{\sigma_{\text{TSA, hr}}(d)}{\bar{Y}_d} = \frac{\sqrt{\frac{1}{23}\sum_{h=0}^{23} (Y_{d,h} - \bar{Y}_d)^2}}{\frac{1}{24}\sum_{h=0}^{23} Y_{d,h}}
$$

3. **Multi-Day Temporal Rolling Volatility ($\sigma_{\text{TSA, 7d}}$, pax/day network turbulence)**:


$$
\sigma_{\text{TSA, 7d}}(d) = \sqrt{\frac{1}{6} \sum_{k=0}^{6} (D_{d-k} - \bar{D}_{7d})^2}
$$

<div class="table-callout">

### Table C.1
*Airport Checkpoint Queuing Dynamics, Kingman Formulations, and Volatility Dispersion Metrics*

[**Companion Excel Tab:** `'Table_C1_Queuing'` in `master_thesis_tables.xlsx`]  
*Note. Econometric and structural evaluation comparing Candidate A (Mature Post-Pandemic) and Candidate B (Early Post-Mask Mandate Regime).*

*(Note. Full conformed tabular data, mathematical models, and statistical derivations are provided in companion workbook master_thesis_tables.xlsx).*

</div>

---

# Appendix E: Four-Tier Purposive Filtering Pipeline, Nine-Airport Cohort Selection, and Airport Contrasts

> **Operational Cross-Reference**: This appendix details the 4-tier filtering methodology isolating unconfounded carrier-exclusive checkpoint lanes and documents the 9-airport experimental cohort. It is referenced in **Chapter III (Methodology)**, Section 3.2 (*The Four-Tier Purposive Filtering Pipeline*) and Section 3.3 (*The Nine-Airport Experimental Cohort*); and in **Chapter IV (Results)**, Section 4.3 (*Nine-Airport Cohort Selection Findings*).

## E.1 Four-Tier Purposive Filtering Pipeline Mechanics

To eliminate lobby-sharing collinearity while preserving balanced experimental power across hub operational roles and geographic climate zones, airports were filtered through a rigorous 4-tier pipeline:

* **Tier 1 (Macro Filter - Federal Scale)**: Screened the Top 25 large-hub commercial airports by passenger enplanements, retaining $67.2\%$ of nationwide commercial volume where heavy-traffic utilization approaches capacity ($\rho \to 1.0$).
* **Tier 2 (Meso Filter - Big 3 Symmetry & WN Exclusion)**: Retained airports dominated by legacy network carriers (American, Delta, United) while excluding point-to-point carriers (e.g., Southwest Airlines at MDW, DAL) whose unassigned seating boarding behavior violates passenger arrival exchangeability.
* **Tier 3 (Micro Filter - Checkpoint Exclusivity)**: Filtered for carrier-exclusive screening complexes commanding $\ge 85\%$ of concourse gates, eliminating multi-carrier lobby mixing.
* **Tier 4 (Factorial Cohort Matrix)**: Established a balanced 9-airport experimental cohort crossing hub role (Connecting Hub vs Origin & Destination) with climate disruption archetype across 12 carrier-exclusive complexes (4 AA, 4 DL, 4 UA).

<div class="table-callout">

### Table E.1
*Top 25 Commercial Airport Census and Purposive Four-Tier Filtering Pipeline Funnel*

[**Companion Excel Tab:** `'Table_E1_Top25_Census'` in `master_thesis_tables.xlsx`]  
*Note. Compares systemwide operational scale across the Top 25 passenger network against the 9-airport experimental cohort.*

*(Note. Full conformed tabular data, mathematical models, and statistical derivations are provided in companion workbook master_thesis_tables.xlsx).*

</div>

<div class="table-callout">

### Table E.2
*Nine-Airport Experimental Cohort Factorial Specification and Dedicated Carrier Complexes*

[**Companion Excel Tab:** `'Table_E2_Cohort_Matrix'` in `master_thesis_tables.xlsx`]  
*Note. 4x4 balanced factorial evaluation cohort crossing hub role with climate disruption vulnerability across 12 carrier-exclusive complexes.*

*(Note. Full conformed tabular data, mathematical models, and statistical derivations are provided in companion workbook master_thesis_tables.xlsx).*

</div>

## E.2 Key Airport Selection Contrasts and Structural Exclusions

Table E.3 documents specific structural inclusion and exclusion rationale across key candidate airfields:

<div class="table-callout">

### Table E.3
*Key Airport Selection Contrasts and Structural Facility Exclusion Matrix*

[**Companion Excel Tab:** `'Table_E3_Selection_Contrasts'` in `master_thesis_tables.xlsx`]  
*Note. Documents structural selection and exclusion rationale for contrasting facilities (e.g., EWR vs LGA, DFW vs IAH, CLT connecting paradox).*

*(Note. Full conformed tabular data, mathematical models, and statistical derivations are provided in companion workbook master_thesis_tables.xlsx).*

</div>

---

# Appendix F: Multi-Source Aviation Data Feeds, ETL Architecture, and Data Hygiene Protocols

> **Operational Cross-Reference**: This appendix documents the multi-source data warehouse census, DuckDB ETL pipeline, and data hygiene protocols. It is referenced in **Chapter III (Methodology)**, Section 3.3 (*Sources of Data*) and Section 3.4 (*Treatment of Data & Star Schema ETL Pipeline*); and in **Chapter IV (Results)**, Section 4.1 (*Post-ETL Master Data Foundation Census*).

## F.1 Multi-Source Federal Aviation Feeds

The empirical warehouse synthesizes four federal aviation feeds spanning the 2019–2025 baseline:
1. **TSA FOIA Checkpoint Logs**: $19,500,286$ raw lane-hour rows processed into $6,434,732$ conformed lane-hours across 25 airfields (2.70B passengers).
2. **BTS On-Time Flight Performance (Form 234)**: $45,777,091$ raw flight rows processed into $13,153,654$ domestic mainline departures.
3. **BTS Form 41 Schedule T-100 Segment Data**: $1,945,451$ raw records processed into $422,096$ conformed carrier-segment-month observations.
4. **BTS DB1B / DB1C 10% Ticket Surveys**: $12,910,384$ raw coupon records processed into $22,051,557$ conformed coupons (62.16M travelers).

<div class="table-callout">

### Table F.1
*Master Post-ETL Multi-Source Data Foundation Census Across Federal Aviation Feeds*

[**Companion Excel Tab:** `'Table_F1_Data_Feeds'` in `master_thesis_tables.xlsx`]  
*Note. Ingested vs cleaned conformed data row counts across TSA FOIA, BTS OTP, BTS T-100, and BTS DB1B federal databases.*

*(Note. Full conformed tabular data, mathematical models, and statistical derivations are provided in companion workbook master_thesis_tables.xlsx).*

</div>

<div class="table-callout">

### Table F.2
*Unified Data Integrity, Threat Remediation, and Data Hygiene Matrix*

[**Companion Excel Tab:** `'Table_F2_Data_Threats'` in `master_thesis_tables.xlsx`]  
*Note. Protocols resolving lane fingerprint variations, structural zeros (night closures), tactical cancellations, and ghost demand.*

*(Note. Full conformed tabular data, mathematical models, and statistical derivations are provided in companion workbook master_thesis_tables.xlsx).*

</div>

<div class="table-callout">

### Table F.3
*Post-ETL Master Summary Descriptive Statistics Across Key Operational Variables*

[**Companion Excel Tab:** `'Table_F3_Descriptive_Stats'` in `master_thesis_tables.xlsx`]  
*Note. Parametric and non-parametric dispersion statistics (Mean, SD, Median, IQR, Min, Max) across 22,491 airport-days.*

*(Note. Full conformed tabular data, mathematical models, and statistical derivations are provided in companion workbook master_thesis_tables.xlsx).*

</div>

---

# Appendix G: Statistical Significance Testing: Diebold-Mariano, Chow, and CUSUM Foundations

> **Operational Cross-Reference**: This appendix establishes the econometric proofs and formulations for the Diebold-Mariano test, Newey-West HAC variance estimator, and Chow structural break tests. It is referenced in **Chapter III (Methodology)**, Section 3.5 (*Statistical Significance Testing: Diebold-Mariano and Econometric Foundations*); and in **Chapter IV (Results)**, Section 4.4 (*Statistical Significance Findings*).

## G.1 The Diebold-Mariano (DM) Forecast Accuracy Test

Standard paired $t$-tests assume independent and identically distributed ($i.i.d.$) errors, an assumption severely violated by the diurnal autocorrelation and ARCH volatility clustering inherent in hourly checkpoint time series. Applying standard $t$-tests to autocorrelated time-series forecast residuals results in severe negative bias in the variance estimator, yielding spuriously deflated standard errors and artificially inflated $t$-statistics ($p$-value collapse).

To ensure valid statistical inference, pairwise model comparison is evaluated using the Diebold-Mariano (DM) test. Let $e_{1,t} = y_t - \hat{y}_{1,t}$ and $e_{2,t} = y_t - \hat{y}_{2,t}$ denote the forecast errors of two competing candidate models at hour $t$. The loss differential $d_t$ is defined as:

$$
d_t = L(e_{1,t}) - L(e_{2,t}) = |e_{1,t}| - |e_{2,t}|
$$

Under the null hypothesis $H_0: \mathbb{E}[d_t] = 0$, both candidate models exhibit equal expected forecast accuracy. The sample mean loss differential is:

$$
\bar{d} = \frac{1}{T} \sum_{t=1}^T d_t
$$

To account for serial correlation in the loss differential series $d_t$, the asymptotic long-run variance $\sigma_d^2$ is estimated using the Newey-West Heteroskedasticity and Autocorrelation Consistent (HAC) spectral density estimator at frequency zero:

$$
\hat{\sigma}_d^2 = \hat{\gamma}_0 + 2 \sum_{k=1}^h \left( 1 - \frac{k}{h + 1} \right) \hat{\gamma}_k
$$

where $\hat{\gamma}_k$ is the empirical autocovariance at lag $k$, and $h = 24$ hours is the truncation lag capturing full diurnal recurrence. The Diebold-Mariano test statistic is formulated as:

$$
DM = \frac{\bar{d}}{\sqrt{\hat{\sigma}_d^2 / T}} \xrightarrow{d} \mathcal{N}(0, 1)
$$

<div class="table-callout">

### Table G.1
*Diebold-Mariano Pairwise Forecast Accuracy Statistics and Econometric Parameter Estimates*

[**Companion Excel Tab:** `'Table_G1_Statistical_Tests'` in `master_thesis_tables.xlsx`]  
*Note. 24 BTS OTP flight schedule attributes, delay spreads, taxi queues, and rolling 7-day volatility indicators.*

*(Note. Full conformed tabular data, mathematical models, and statistical derivations are provided in companion workbook master_thesis_tables.xlsx).*

</div>

<div class="table-callout">

### Table H.2
*Empirical Passenger Show-Up Distribution Curves and DB1B Connecting Deflators*

[**Companion Excel Tab:** `'Table_H2_Showup_Curves'` in `master_thesis_tables.xlsx`]  
*Note. Annual seasonal regimes (Summer Peak, Shoulder, Winter Lull) evaluated across the 9 cohort airports.*

*(Note. Full conformed tabular data, mathematical models, and statistical derivations are provided in companion workbook master_thesis_tables.xlsx).*

</div>

<div class="table-callout">

### Table I.2
*Day-of-Week Volatility Dynamics and Operational Volatility Archetypes*

[**Companion Excel Tab:** `'Table_I2_DOW_Archetypes'` in `master_thesis_tables.xlsx`]  
*Note. DOW operational archetypes: Monday business surge, Thursday/Friday reconnection, midweek equilibrium, and weekend leisure waves.*

*(Note. Full conformed tabular data, mathematical models, and statistical derivations are provided in companion workbook master_thesis_tables.xlsx).*

</div>

<div class="table-callout">

### Table I.3
*Day-of-Week Mean Daily Passenger Throughput Across the Nine Cohort Airfields*

[**Companion Excel Tab:** `'Table_I3_Airport_DOW'` in `master_thesis_tables.xlsx`]  
*Note. Cross-sectional breakdown of day-of-week passenger throughput volume across BOS, DFW, DTW, EWR, IAH, LAX, LGA, ORD, and PHL.*

*(Note. Full conformed tabular data, mathematical models, and statistical derivations are provided in companion workbook master_thesis_tables.xlsx).*

</div>

---

# Appendix J: Candidate Predictive Models, Operational Evaluation Triad Metrics, and Holdout Benchmarks

> **Operational Cross-Reference**: This appendix details the three candidate forecasting models and baseline control, formalizes the evaluation triad metrics, and presents certified 2025 out-of-sample holdout benchmarks. It is referenced in **Chapter III (Methodology)**, Section 3.2 (*The Three Candidate Predictive Models and Baseline Control*); and in **Chapter IV (Results)**, Section 4.4 (*Out-of-Sample Holdout Benchmarking*).

## J.1 Candidate Predictive Models Mathematical Specifications

Following the 4-tier filtering pipeline, the evaluation suite evaluates exactly three candidate models representing distinct operational paradigms, benchmarked against an empirical baseline control:

1. **Baseline Control (Diurnal Volatility Naive Persistence Benchmark)**: Non-parametric reference forecast establishing the empirical normalization floor (MASE = 1.000):


$$
\widehat{\text{Vol}}_t = \text{Vol}_{t-24}
$$


where $\widehat{\text{Vol}}_t$ predicts checkpoint throughput based strictly on observed demand at the identical hour 24 hours prior.

2. **Model 1 (Deterministic Flight Schedule Model)**: Operational baseline convolving scheduled airline flight banks across empirical ACRP Report 40 passenger arrival curves ($t+1, t+2, t+3$), weighted by monthly T-100 load factors and deflated by DB1B connecting ratios:


$$
\hat{y}_{1, t} = \sum_{f \in \mathcal{F}_t} \text{Seats}(f) \cdot \text{LoadFactor}(f) \cdot [1 - \theta_{\text{connect}}(f)] \cdot \omega(t - \text{SchedDept}(f))
$$


Model 1 represents deterministic physics-based flight schedule planning without machine learning or live sensor feedback.

3. **Model 2 (Supervised Machine Learning Model)**: Automated Histogram Gradient Boosting decision tree regressor trained on flight schedule features and 24 BTS OTP operational attributes (departure delays, tactical cancellations, taxi-out queues):


$$
\hat{y}_{2, t} = \mathcal{T}_{\text{GBM}}(\mathbf{X}_t)
$$


where $\mathbf{X}_t$ incorporates bank-level flight seat density, delay spread ($CV_{\text{delay}}$), tactical cancellations ($CV_{\text{cancel}}$), and rolling 7-day volatility metrics.

4. **Model 3 (Dynamic Two-Stage Hybrid Model)**: Sequential two-stage architecture coupling the convolved schedule baseline with tree-based residual adjustments and recursive 1-step error innovation feedback ($e_{t-1} = y_{t-1} - \hat{y}_{t-1}$) from the physical checkpoint floor:


$$
\hat{y}_{3, t|t-1} = \hat{y}_{1, t} + \widehat{R}_{\text{tree}}(\mathbf{X}_t) + \alpha \cdot (y_{t-1} - \hat{y}_{3, t-1|t-2})
$$


where $\alpha \in (0, 1)$ is the recursive innovation gain (calibrated to $\alpha = 0.45$), functioning as an automated sensor feedback loop tracking unexpected lobby accumulations.

## J.2 Formalization of the Operational Evaluation Triad Metrics

The performance of candidate models is evaluated across the governing theoretical triad: Robustness, Resilience, and Generalizability:

* **Robustness Ratio ($R_{\text{MASE, nom}}$)**: Evaluates baseline forecast precision under nominal on-time conditions relative to naive persistence:


$$
R_{\text{MASE, nom}} = \frac{\text{MASE}_{\text{model, nom}}}{\text{MASE}_{\text{persistence, nom}}}
$$


A robust model achieves $R_{\text{MASE, nom}} < 0.700$ with minimal error variance.

* **Resilience Error Ratio ($R_{\text{MASE, shock}}$)**: Quantifies forecast error boundedness during severe irregular operations (IROPS):


$$
R_{\text{MASE, shock}} = \frac{\text{MASE}_{\text{shock}}}{\text{MASE}_{\text{nominal}}}
$$


Resilient architectures maintain $R_{\text{MASE, shock}} \approx 1.00$, indicating that forecast error does not explode during disruptions.

* **Time-to-Recovery ($TTR$)**: Measures the duration (in hours) required for model forecast error to return within 1.0 standard deviation of nominal error following shock termination:


$$
TTR = \inf \{ t \ge t_{\text{shock}} : |e_t| \le \mu_{e, \text{nom}} + \sigma_{e, \text{nom}} \}
$$

* **Relative Transfer Ratio ($RTR$)**: Quantifies zero-shot spatial generalizability when transferred to unfamiliar airports without retraining:


$$
RTR = \frac{\text{MASE}_{\text{target}}}{\text{MASE}_{\text{source}}}
$$


High generalizability corresponds to $RTR \approx 1.00$ with transfer degradation $\Delta\text{MASE} \le 10.0\%$.

<div class="table-callout">

### Table J.1
*Master Operational Metric Definitions, Mathematical Formulations, and Academic Stated Targets*

[**Companion Excel Tab:** `'Table_J1_Evaluation_Targets'` in `master_thesis_tables.xlsx`]  
*Note. Mathematical definitions and stated academic targets across Robustness (routine), Resilience (shock), and Generalizability (spatial).*

*(Note. Full conformed tabular data, mathematical models, and statistical derivations are provided in companion workbook master_thesis_tables.xlsx).*

</div>

<div class="table-callout">

### Table J.2
*2025 Out-of-Sample Holdout Benchmark Evaluation Across Candidate Forecasting Models*

[**Companion Excel Tab:** `'Table_J2_Holdout_Benchmarks'` in `master_thesis_tables.xlsx`]  
*Note. Certified out-of-sample holdout performance across Baseline Control, Model 1 (Schedule), Model 2 (ML), and Model 3 (Hybrid).*

*(Note. Full conformed tabular data, mathematical models, and statistical derivations are provided in companion workbook master_thesis_tables.xlsx).*

</div>

<div class="table-callout">

### Table J.3
*Master Multi-Pillar Hypothesis Evaluation Matrix Across the Four Models*

[**Companion Excel Tab:** `'Table_J3_Hypothesis_Matrix'` in `master_thesis_tables.xlsx`]  
*Note. Formal empirical test results confirming Hypothesis 1 (Asymmetric Operational Performance Trade-Offs).*

*(Note. Full conformed tabular data, mathematical models, and statistical derivations are provided in companion workbook master_thesis_tables.xlsx).*

</div>

---

# Appendix K: The Values versus Volatility Operational Coupling Across Temporal Horizons

> **Operational Cross-Reference**: This appendix establishes the empirical coupling between flight performance metrics and checkpoint arrival volatility. It is referenced in **Chapter I (Introduction)**, Section 1.3 (*The Values versus Volatility Paradigm*); in **Chapter IV (Results)**, Section 4.2; and in **Chapter V (Discussion)**, Section 5.1 (*Theoretical Implications: Queuing Physics & Volatility Coupling*).

## K.1 Theoretical Foundation: Heavy-Traffic Queuing and Volatility Coupling

A core theoretical contribution of this thesis is the empirical demonstration of the **Values versus Volatility Paradigm**. In heavy-traffic queuing systems, expected passenger delay scales quadratically with arrival volatility ($C_a^2$) rather than average volume levels ($y_t$). As terminal screening lanes approach capacity (\rho \to 1.0), small bursts in passenger arrival rate trigger dramatic non-linear waiting time explosions.

## K.2 Multi-Day Temporal Horizon Volatility Decoupling

Evaluating multi-day rolling volatility ($\sigma_{\text{TSA, 7d}}$, pax/day) demonstrates a complete empirical divergence between static volume metrics and volatility indicators:

1. **Static Feature Values Collapse**: Standard feature values (raw scheduled flight counts, average departure delay minutes) generate negative out-of-time test scores ($R^2 < 0$ in linear regression; $R^2 < 0$ in decision trees). Because scheduled flight counts remain relatively stable across consecutive operating weeks, static volume features cannot detect shifts in network turbulence.

2. **Feature Volatility Succeeds**: In contrast, Feature Volatility attributes (rolling 7-day schedule variance, cancellation volatility $CV_{\text{cancel}}$, and delay dispersion $CV_{\text{delay}}$) achieve strong predictive power ($R^2 > +0.31$ in linear regression and $R^2 > +0.35$ in decision trees), improving to $R^2 = +0.461$ in the hybrid architecture while slashing forecast error from 4,090.7 to 3,002.3 pax/day.

3. **Flight Delay Volatility Transmission**: Cross-dataset econometric correlation demonstrates that Flight Departure Delay Volatility ($CV_{\text{delay}}$) is significantly coupled with checkpoint arrival volatility ($r = +0.4373, p < 0.05$). Conversely, raw flight departure delay minutes show zero linear correlation ($r = -0.062, p = 0.77$). Delays only disrupt checkpoint operations when they are erratic and disperse passenger arrival timing across banks.

4. **Master Consensus Factor Weights**: Synthesizing feature importance across models confirms that flight schedule dispersion (`sched_rolling_7d_mean`, $23.73\%$; `sched_hourly_mean`, $6.91\%$) and operational volatility (`otp_cancellation_volatility_cv`, $8.79\%$; $CV_{\text{delay}}$, $4.32\%$) dominate predictive power, accounting for over $80\%$ of consensus feature importance.

<div class="table-callout">

### Table K.1
*Values versus Volatility Empirical Cross-Dataset Econometric Relationships Across Temporal Horizons*

[**Companion Excel Tab:** `'Table_K1_Values_vs_Volatility'` in `master_thesis_tables.xlsx`]  
*Note. Cross-dataset econometric coupling demonstrating that flight departure delay volatility couples with checkpoint arrival volatility.*

*(Note. Full conformed tabular data, mathematical models, and statistical derivations are provided in companion workbook master_thesis_tables.xlsx).*

</div>

---

# Appendix L: Operational Disruption Dynamics, Lead-Lag Asynchrony, Resilience Mechanics, and the Empty Checkpoint Fallacy

> **Operational Cross-Reference**: This appendix details the phase-shifted lead-lag relationship between screening and flight departure, the mechanics of the Empty Checkpoint Fallacy, and disruption recovery dynamics. It is referenced in **Chapter IV (Results)**, Section 4.4; and in **Chapter V (Discussion)**, Section 5.2 (*The Lead-Lag Asynchrony Mechanism*) and Section 5.3 (*Resilience Mechanics and the Empty Checkpoint Fallacy*).

## L.1 Air Traffic Disruption Regimes and Operational Shock Thresholds

To evaluate candidate forecasting models across diverse operating environments, terminal operational states are partitioned into three distinct tiers based on authentic FAA operational metrics:

* **Tier 1: Nominal On-Time Baseline (FAA A14 Benchmark)**: Departure delays strictly less than 15 minutes ($\text{Delay}_{\text{dep}} < 15$ min) and flight cancellation count is zero ($\text{Cancellations} = 0$). Represents the regulatory baseline reference standard.
* **Tier 2: Routine Daily Operations**: Everyday commercial hub operations characterized by ambient 15–30 minute delays and normal 1–2% cancellation churn.
* **Tier 3: Irregular Operations (IROPS)**: Triggered by FAA Ground Delay Programs (GDP), severe convective weather cells, winter de-icing holds, or terminal security directives. Quantitatively demarcated when average departure delays exceed 45 minutes ($\text{Delay}_{\text{dep}} \ge 45$ min) or scheduled flight cancellations exceed 5 flights within an operating bank ($\text{Cancellations} \ge 5$).

## L.2 The Lead-Lag Asynchrony Mechanism

A fundamental physical reality governing airport passenger processing is the 90–120 minute temporal lead between passenger checkpoint screening and aircraft gate pushback. Passengers must complete ticket verification, baggage divestiture, and security screening well in advance of flight boarding. Consequently, the unshifted same-hour flight departure schedule ($t$) explains only $11.58\%$ of checkpoint arrival variance ($r = 0.3403$, regression slope = 27.49 pax/flight).

In sharp contrast, flight departures occurring 1 hour in the future ($t+1$) explain $24.13\%$ of current screening variance ($r = 0.4913$, slope = 39.7 pax/flight), and departures occurring 2 hours in the future ($t+2$) explain $23.78\%$ ($r = 0.4876$, slope = 39.4 pax/flight). Convolving flight banks across the empirical lead horizons ($t+1, t+2, t+3$) doubles explanatory power to $48.78\%$ ($r = 0.6985$), which increases to $49.85\%$ ($r = 0.7061$) when weighted by monthly route load factors.

## L.3 Resilience Mechanics and the Empty Checkpoint Fallacy

During severe disruption events (Irregular Operations / IROPS), unconstrained decision-tree regressors (Model 2) suffer from the **Empty Checkpoint Fallacy**. When flights are delayed by several hours, static schedule features shift out of the active time window, and cancellation counts spike. Pure machine learning models interpret these attributes as a collapse in passenger arrivals, predicting zero or near-zero demand.

In physical terminal reality, delayed passengers do not disappear: ticketed passengers arrive at the airport according to their original published schedules, accumulating in landside ticketing lobbies and checkpoint queues. Consequently, pure ML models experience severe forecast error explosions during shocks, resulting in an unacceptable resilience multiplier ($R_{\text{MASE}} = 2.14$) and an extended Time-to-Recovery ($TTR = 5.4$ hours).

The Dynamic Two-Stage Hybrid model (Model 3) resolves this fallacy through its recursive 1-step error innovation loop. When live throughput $y_{t-1}$ exceeds delayed schedule predictions, the innovation term $e_{t-1} = y_{t-1} - \hat{y}_{t-1}$ instantly detects passenger accumulation on the floor, updating forecasts upward within 1 hour. This enables Model 3 to achieve decisive disruption resilience ($R_{\text{MASE}} = 1.05$) and rapid recovery ($TTR = 2.8$ hours).

<div class="table-callout">

### Table L.1
*Evaluation Dimension 2: Resilience and Shock Performance Under Severe Operational Disruption*

[**Companion Excel Tab:** `'Table_L1_Disruption_Resilience'` in `master_thesis_tables.xlsx`]  
*Note. Benchmark performance under severe IROPS (delays ≥ 45m or cancellations ≥ 5), illustrating the Empty Checkpoint Fallacy.*

*(Note. Full conformed tabular data, mathematical models, and statistical derivations are provided in companion workbook master_thesis_tables.xlsx).*

</div>

<div class="table-callout">

### Table L.2
*Empirical Lead-Lag Transfer Dynamics Across Operational Time Lags*

[**Companion Excel Tab:** `'Table_L2_Lead_Lag_Dynamics'` in `master_thesis_tables.xlsx`]  
*Note. Cross-correlation structure verifying the 90-120 minute operational phase lead between checkpoint screening and gate departure.*

*(Note. Full conformed tabular data, mathematical models, and statistical derivations are provided in companion workbook master_thesis_tables.xlsx).*

</div>

---

# Appendix M: Dual-Track Operational Decision Playbook, Zero-Shot Spatial Transfer, and Dynamic Lane Staffing

> **Operational Cross-Reference**: This appendix formalizes the Dual-Track Operational Decision Framework, zero-shot spatial transfer results, and Kingman volatility-buffered dynamic lane staffing look-up formulas. It is referenced in **Chapter V (Discussion)**, Section 5.4 (*The Dual-Track Operational Decision Framework*), Section 5.5 (*Connecting Queuing Principles to Dynamic Lane Staffing*), and Section 5.6 (*Operational Recommendations*).

## M.1 Zero-Shot Spatial Transferability and Cross-Facility Evaluation Protocols

Under the spatial transfer evaluation protocol, models trained exclusively on source facility data (Newark Liberty, EWR Terminal C) were deployed zero-shot to a target facility (LaGuardia, LGA Terminal C) without retraining weights or updating hyperparameters. Empirical results demonstrate that:

1. **Model 1 (Deterministic Schedule) DECISIVE WINNER**: Achieves near-perfect spatial invariance ($RTR = 1.04$, $\Delta\text{MASE} = +4.0\%$). Because flight schedule convolution rules reflect universal passenger show-up physics, Model 1 transfers seamlessly across terminal layouts.
2. **Model 2 (Supervised Machine Learning)**: Passes spatial transfer thresholds ($RTR = 1.08$, $\Delta\text{MASE} = +8.3\% \le 10.0\%$), proving viable as a portable decision-tree model.
3. **Model 3 (Dynamic Hybrid) DECISIVELY FAILS**: Collapses on zero-shot spatial transfer ($RTR = 1.19 > 1.00$, $\Delta\text{MASE} = +21.5\% > 10.0\%$). Its complex decision trees and innovation loop gains overfit to source terminal geometry, bag-drop bottlenecks, and local gate layouts.

## M.2 Master Asymmetric Operational Trade-Offs (Hypothesis 1)

These empirical findings definitively prove **Hypothesis 1 (Asymmetric Trade-Offs)**: no single candidate model dominates across all operational performance dimensions. Rather, distinct architectures present strategic trade-offs across Robustness, Resilience, and Generalizability:

* **Dimension 1 (Robustness - Routine Daily Operations)**: Model 3 achieves lowest absolute error ($\text{RMSE} = 222.1, \text{MASE} = 0.662$); Model 2 wins Routine Pareto Efficiency ($\text{MASE} = 0.680\text{--}0.700$, zero online compute latency).
* **Dimension 2 (Resilience - Irregular Operations / IROPS)**: Model 3 is the DECISIVE WINNER ($R_{\text{MASE}} = 1.05, \text{MASE}_{\text{shock}} = 0.694, TTR = 2.8\text{h}$); pure ML collapses ($R = 2.14$).
* **Dimension 3 (Generalizability - Zero-Shot Spatial Transfer)**: Model 1 is the DECISIVE WINNER ($RTR = 1.04, \Delta\text{MASE} = +4.0\%$); Model 3 fails ($RTR = 1.19, \Delta\text{MASE} = +21.5\%$).

## M.3 Dual-Track Operational Decision Playbook and Dynamic Lane Staffing

To operationalize these trade-offs, airport authorities and the TSA should implement a **Dual-Track Operational Decision Framework**:

* **Track A: In-Sample Facility Operations & Disruption Resilience**: Deploys the Dynamic Two-Stage Hybrid Model (Model 3) for established facilities equipped with real-time floor sensors, leveraging live error innovation to bound disruption shocks.
* **Track B: Zero-Shot Spatial Transfer & New Airport Commissioning**: Deploys the Deterministic Flight Schedule Model (Model 1) for newly commissioned terminals or facilities lacking historical sensor telemetry, ensuring robust zero-shot baseline forecasts.

### Connecting Queuing Principles to Dynamic Lane Staffing
Under traditional deterministic staffing, security lanes are opened based solely on expected mean throughput ($\bar{y}_t / \mu$). In heavy-traffic regimes (Kingman, 1961), arrival surges push utilization past $\rho = 0.85$, triggering runaway queue explosions. Airport checkpoint administrators can prevent this by incorporating a dynamic volatility buffer ($z_{1-\alpha} \cdot \hat{\sigma}_t$) into lane scheduling:

$$
s_t^* = \left\lceil \frac{\hat{y}_t + z_{1-\alpha} \cdot \hat{\sigma}_t}{\mu_{\text{lane}}} \right\rceil
$$

where $\mu_{\text{lane}}$ is nominal lane capacity (180–220 pax/lane-hr) and $z_{1-\alpha} = 1.04$ provides an $85\%$ service level guarantee. Capping utilization at $\rho \le 0.85$ clamps the $\frac{\rho}{1-\rho}$ multiplier and guarantees queue stability.

<div class="table-callout">

### Table M.1
*Evaluation Dimension 1: Routine Operational Accuracy Across Candidate Forecasting Models*

[**Companion Excel Tab:** `'Table_M1_Routine_Accuracy'` in `master_thesis_tables.xlsx`]  
*Note. Nominal On-Time Baseline (departure delays < 15 min, 0 cancellations) benchmark results.*

*(Note. Full conformed tabular data, mathematical models, and statistical derivations are provided in companion workbook master_thesis_tables.xlsx).*

</div>

<div class="table-callout">

### Table M.2
*Evaluation Dimension 3: Generalizability and Cross-Airport Spatial Transfer Performance*

[**Companion Excel Tab:** `'Table_M2_Spatial_Transfer'` in `master_thesis_tables.xlsx`]  
*Note. Zero-shot spatial transfer evaluation (EWR → LGA Terminal C) without retraining or fine-tuning.*

*(Note. Full conformed tabular data, mathematical models, and statistical derivations are provided in companion workbook master_thesis_tables.xlsx).*

</div>

<div class="table-callout">

### Table M.3
*Master Multi-Dimensional Asymmetric Trade-Off Matrix and Dual-Track Operational Policy*

[**Companion Excel Tab:** `'Table_M3_Asymmetric_Tradeoffs'` in `master_thesis_tables.xlsx`]  
*Note. Synthesizes winning models across Robustness, Resilience, and Generalizability, establishing Dual-Track deployment.*

*(Note. Full conformed tabular data, mathematical models, and statistical derivations are provided in companion workbook master_thesis_tables.xlsx).*

</div>

---

# Appendix N: Archival Data Storage Infrastructure, Directory Hierarchy, and Exhibits Catalog

> **Operational Cross-Reference**: This appendix establishes the physical directory hierarchy, database profiles, and reproducible asset registry. It is referenced in **Chapter III (Methodology)**, Section 3.6 (*Reproducible Research Architecture*).

## N.1 Storage Infrastructure, Data Lake Organization, and Backup Protocols

To support high-throughput analytical query workloads across 67+ million raw federal records while maintaining strict local and remote data provenance, all data assets are organized in an immutable multi-tier file structure:

* `data/raw/`: Read-only source snapshots of TSA FOIA screening logs, BTS OTP Form 234 archives, BTS T-100 domestic segment tables, and BTS DB1B ticket coupon surveys.
* `data/staging/`: Conformed DuckDB columnar databases partitioned by calendar year, storing optimized Star Schema dimension tables.
* `results/`: Conformed tabular results in CSV, multi-tab companion Excel workbooks, and provenance registers.
* `thesis_docs/`: Authoritative manuscript chapters, research notes, and figures.

<div class="table-callout">

### Table N.1
*Master Archival Data Storage Hierarchy, Database Profiles, and Exhibits Catalog*

[**Companion Excel Tab:** `'Table_N1_Archival_Hierarchy'` in `master_thesis_tables.xlsx`]  
*Note. Formal database profiles and repository architecture specifications for reproducible analytical pipelines.*

*(Note. Full conformed tabular data, mathematical models, and statistical derivations are provided in companion workbook master_thesis_tables.xlsx).*

</div>


