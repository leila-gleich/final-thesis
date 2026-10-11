# Appendix

```
====================================================================================================
PROJECT: Evaluating Predictive Techniques to Model Stochastic Airport Passenger Flow
AUTHOR: Leila Gleich | INSTITUTION: Embry-Riddle Aeronautical University
DEGREE: Master of Science in Aeronautics / Aviation Data Analytics (MSAA / Gleich 700B)
MANUSCRIPT COMPILATION: Appendix v4 (Master Merged Empirical & Methodological Appendices)
DATE: October 10, 2026
COMPANION WORKBOOK: Appendix_Tables.xlsx (30 Conformed Analytical Tabs)
====================================================================================================
```

## Overview and Master Table of Contents

This appendix compiles the comprehensive econometric derivations, queuing theory foundations, data pipeline architectures, and empirical holdout evaluations supporting the master's thesis *Evaluating Predictive Techniques to Model Stochastic Airport Passenger Flow*. Synthesizing and expanding all prior working drafts (*Appendix v1*, *Appendix v2*, *Appendix v3*, and *Chapter II Technical Appendices*), this document eliminates redundancy while preserving complete operational detail across 14 lettered appendices (A through N), arranged strictly in sequential order of citation across Chapters I through V.

A foundational methodological principle established across this research is that airport terminal queue stability and passenger delay risks are governed not merely by static passenger volumes, but by the **volatility of checkpoint throughput** (within-day standard deviation $\sigma_{\text{TSA, hr}}$, scale-free Coefficient of Variation $CV_{\text{TSA}}$, and multi-day temporal dispersion $\sigma_{\text{TSA, 7d}}$). Under Kingman's heavy-traffic queuing formula ($W_q \approx \frac{\rho}{1-\rho} \frac{C_a^2 + C_s^2}{2} \frac{1}{\mu}$), expected waiting times scale quadratically with arrival volatility ($C_a^2$) as checkpoint lane utilization approaches capacity ($\rho \to 1.0$). Accordingly, all operational terms, econometric models, and evaluation dimensions defined herein are grounded in authentic commercial aviation operations, airline flight scheduling banks, and airport passenger flow dynamics.

All tables referenced throughout this appendix are compiled with full conformed data, automated calculations, and APA 7th Edition typography in the companion multi-tab Excel workbook:  
**`thesis_docs/manuscripts/Appendix/Appendix_Tables.xlsx`** (also mirrored at **`results/appendix_tables.xlsx`**).

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

### Table A.1
*14-Point Methodological Assumption and Failure Mode Prevention Matrix*

[**Companion Excel Tab:** `'Table_A1_Assumptions'` in `Appendix_Tables.xlsx`]  
[**Source Data Asset:** `figures/04_Appendix_and_Reference/methodological_assumptions.csv`]

| level | key_assumption | mathematical_operational_justification | failure_mode_prevented |
| :--- | :--- | :--- | :--- |
| Terminal Flow | Non-traveler exits are negligible | Gate passes / aborted boardings are << 1% of peak bank volume | Over-parameterized noise modeling; false uncoupling |
| Terminal Flow | Connecting passengers bypass security | Sterile area transfers never enter landside security screening | Throughput paradoxes (e.g., CLT 76% connecting traffic) |
| Terminal Flow | Exclusion of inbound arrivals | Arriving passengers exit directly via one-way sterile exits | Inbound flight ghost demand & spurious correlation |
| Terminal Flow | Exhaustive nationwide departures | Physical screening serves all destinations and carriers | Truncation bias (>50% omitted originating volume) |
| Temporal Coupling | 90–120 min lead time window | Unidirectional pipeline (doors close T - 15; screening T - 100) | Phase-shift misspecification (t <-> t correlation error) |
| Temporal Coupling | Lognormal arrival density kernel | Peak show-up mode approx 92.5 min; discrete weights (0.25, 0.55, 0.20) | Rigid scalar shifts failing to capture human variance |
| Temporal Coupling | Zero lookahead leakage | Models rely strictly on planned pre-departure schedules | Target leakage from realized operational delays |
| Sample Filtering | Top 25 macro power-law cut-off | Captures 67% of NAS volume; Kingman heavy-traffic limit rho -> 1.0 | Light-traffic triviality (rho << 0.3) and low SNR (CV ~ 0.14) |
| Sample Filtering | Micro checkpoint exclusivity | Eliminates cross-carrier collinearity (Corr approx 0.90) | Gram matrix inversion collapse (kappa >> 10^4) |
| Sample Filtering | Meso Big 3 co-location | Identical weather/airspace shock differencing (delta_t - delta_t = 0) | Carrier comparison confounded by regional weather |
| Sample Filtering | Exclusion of Southwest (WN) | Open-seating bimodal arrival distribution (mu_1 approx 135m, mu_2 approx 65m) | Violation of parameter exchangeability (f_j(tau) != f(tau)) |
| Sample Filtering | Post-pandemic May 1, 2022 boundary | Mask mandate repeal; network aggregate stability | Localized leisure vs. business recovery distortions |
| Evaluation | Orthogonal 4 x 4 factorial design | Exactly 4 exclusive checkpoints per carrier across 4 clusters | Unbalanced ANOVA variance inflation |
| Evaluation | Twin TRACON disruption controls | Matched weather shocks (EWR T-C vs. LGA T-C) | Localized convective bias in resilience / TTR testing |

*Note. Formulated across terminal flow, temporal coupling, sample filtering, and econometric evaluation to protect internal and construct validity.*

### Table A.2
*Research Delimitations and Top 25 Commercial Airport Network Inclusion Criteria*

[**Companion Excel Tab:** `'Table_A2_Delimitations'` in `Appendix_Tables.xlsx`]  
[**Source Data Asset:** `figures/ch01_intro/inclusion_of_top_25_network_approach.csv`]

| chapter_and_section | specific_document_heading | content_to_place | purpose_and_rhetorical_function |
| :--- | :--- | :--- | :--- |
| Chapter I: Introduction | Delimitations | High-level summary of the 9-airport scope, the Big Three legacy carrier focus, and the post-April 2022 temporal boundary. | Establishes the formal boundaries of what is included vs. excluded from the investigation. |
| Chapter I: Introduction | Limitations and Assumptions | Assumption that network-level stabilization (Top 25) reflects a true operational steady state. Limitation that carrier-exclusive checkpoint dynamics may not directly map to pooled/consolidated terminals. | Acknowledges threats to external validity upfront to satisfy thesis committee scrutiny. |
| Chapter III: Methodology (PRIMARY HOME) | Sample -> Macro Categorization | Justification for using the Top 25 network (>67% national passenger throughput) and the 4 operational cluster archetypes. | Explains the systemic scale requirement and operational regime diversity. |
| Chapter III: Methodology (PRIMARY HOME) | Sample -> Micro-Level Refinement | The 9-airport master table, listing specific carrier-exclusive checkpoint names, terminal layouts, and why shared checkpoints were excluded. | Provides the causal identification justification (eliminating multi-carrier confounding). |
| Chapter III: Methodology (PRIMARY HOME) | Sample -> Temporal Scope & Boundary Definition | The Network-Node logic: Why 'post-pandemic' is defined across the Top 25 hub network rather than only the 9 modeling airports. | Justifies why local recovery artifacts (e.g., Florida vs. NYC) did not distort the temporal cutoff. |
| Chapter III: Methodology | Validity | Connecting passenger decoupling (DB1B) and checkpoint isolation as controls for construct and internal validity. | Explains how physical queue-to-schedule alignment is methodologically grounded. |

*Note. Establishes commercial aviation inclusion criteria, power-law concentration (67.2% nationwide volume), and geographic coverage.*

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

### Table B.1
*Comparative Modeling Paradigm Taxonomy for Airport Security Screening Facilities*

[**Companion Excel Tab:** `'Table_B1_Paradigms'` in `Appendix_Tables.xlsx`]  
| Modeling Paradigm | Mathematical Foundation | Operational Strengths | Critical Operational Limitations | Inference Latency | Interpretability | Key Citations |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Classical Queuing Theory | Poisson / Exponential: M/M/s, G/G/s, NHPP | Closed-form solutions; transparent parameterization; negligible compute latency. | Fails under batch flight banks; ignores airside connecting passenger shielding; assumes static arrival rates. | Sub-second (<10 ms) | High (Glass-box formulas) | Odoni (1986); Wang (2018); Brunetta et al. (1999); Guo et al. (2022) |
| Discrete Event Simulation (DES) | Stochastic entity tracking through physical screening stages (ARENA, SIMMOD, CAST). | High micro-level spatial fidelity; granular TSO lane layout simulation. | Extreme calibration brittleness; passive traveler assumptions; heavy computational latency. | High (>15 min) | Moderate (Process simulation) | Brown & Madhavan (2011); Takakuwa & Oyama (2004); Bießlich et al. (2014) |
| Linear Statistical Time-Series | Autoregressive moving average: SARIMAX(p,d,q)x(P,D,Q)s | Lightweight; captures diurnal (24h) and weekly (168h) cycles; clear confidence intervals. | Fails during structural disruption breaks and weather ground stops; cannot ingest flight delays. | Low (<1 sec) | Moderate (Autoregressive weights) | Li et al. (2017); Box et al. (2015); Hyndman & Athanasopoulos (2018) |
| Deep Sequence Models (LSTM / GRU) | Recurrent hidden state: Gated recurrent units h_t = σ(Whh·h_t-1 + Wxh·x_t + b) | Models complex multi-scale temporal dependencies without manual feature engineering. | Complete black-box opacity; facility-specific overfitting; acute spatial transfer collapse (>40%). | Moderate (1–5 sec) | Low (Opaque neural tensors) | Hochreiter & Schmidhuber (1997); Adadi & Berrada (2018); Viaña et al. (2024) |
| Supervised Machine Learning (GBM) | Non-linear decision trees: Histogram Gradient Boosting minimizing Tweedie loss | Captures non-linear delay thresholds, taxi queues, and weather; fast inference; auditable rules. | Susceptible to 'Empty Checkpoint Fallacy' during flight delays; overfits local terminal geometry. | Sub-second (<50 ms) | High (Feature splits & thresholds) | Hopfe et al. (2024); Ribeiro et al. (2025); Chen & Guestrin (2016) |
| Sequential Two-Stage State-Space Hybrids | Stage 1 Physical Schedule + Stage 2 Tree Residual + Real-Time Innovation Feedback | Optimal routine accuracy (RMSE = 222.1); decisive shock resilience (R = 1.05, TTR = 2.8h); robust. | Requires real-time sensor feedback ingestion (live prior-hour floor counts y_{t-1}). | Sub-second (<100 ms) | High (Modular decomposition) | Brun et al. (2025); Had et al. (2025); Ebert et al. (2021); Gleich (2026) |

*Note. Synthesizes six major predictive modeling paradigms across queuing theory, simulation, statistical time-series, machine learning, and hybrid systems.*

## B.2 Master Literature Equation Registry: 20 Peer-Reviewed Operational Equations

To ensure complete mathematical auditability and exact replication across research facilities, Table B.2 catalogs the 20 governing peer-reviewed operational and statistical equations operationalized across Chapters I through V. All equations conform strictly to authentic aviation terminology and APA 7th Edition statistical reporting standards.

### Table B.2
*Master Literature Equation Registry: 20 Peer-Reviewed Operational Equations*

[**Companion Excel Tab:** `'Table_B2_Equations'` in `Appendix_Tables.xlsx`]  
[**Source Data Asset:** `results/tables/appendix_standard_literature_equations.csv`]

| Equation_ID | Domain_Category | Equation_Name | Mathematical_Formulation_LaTeX | Mathematical_Formulation_Plain_Text | Parameters_and_Variables | Published_Source_and_Citation | Thesis_Operational_Role |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| EQ-01 | Stochastic Queuing & Congestion Theory | Kingman's Heavy-Traffic Queuing Approximation (Single-Server) | W_q \approx \left(\frac{\rho}{1-\rho}\right) \left(\frac{C_a^2 + C_s^2}{2}\right) \frac{1}{\mu} | W_q ≈ [rho / (1 - rho)] * [(C_a^2 + C_s^2) / 2] * (1 / mu) | W_q = Mean waiting time in queue; rho = Server utilization (traffic intensity); C_a = Coefficient of variation of inter-arrival times; C_s = Coefficient of variation of service times; mu = Mean service rate. | Kingman, J. F. C. (1961). The single server queue in heavy traffic. Mathematical Proceedings of the Cambridge Philosophical Society, 57(4), 902–904; Kingman, J. F. C. (1962). On queues in heavy traffic. Journal of the Royal Statistical Society: Series B, 24(2), 383–392. | Establishes the fundamental theoretical queuing foundation of the thesis: checkpoint queues scale quadratically with arrival volatility (C_a^2) as checkpoint utilization approaches capacity (rho -> 1.0), proving why predicting throughput volatility is operationally superior to predicting raw mean volume. |
| EQ-02 | Stochastic Queuing & Congestion Theory | Kingman-Whitt Multi-Server Heavy-Traffic Approximation (G/G/s Queue) | W_q \approx \left( \frac{\rho^{\sqrt{2(s+1)}-1}}{s(1-\rho)} \right) \left( \frac{C_a^2 + C_s^2}{2} \right) \frac{1}{\mu} | W_q ≈ [rho^(sqrt(2*(s+1)) - 1) / (s*(1 - rho))] * [(C_a^2 + C_s^2) / 2] * (1 / mu) | W_q = Expected queue wait time; s = Number of active parallel screening lanes; rho = Multi-server utilization (lambda / (s*mu)); C_a = Arrival CV; C_s = Service time CV; mu = Lane processing rate. | Whitt, W. (1993). Approximations for the GI/G/m queue. Production and Operations Management, 2(2), 114–161; Marchal, W. G. (1976). An approximate formula for waiting time in GI/G/1. Operations Research, 24(3), 473–474. | Extends Kingman queuing principles to multi-lane airport security screening checkpoints (s parallel lanes), demonstrating buffer depletion under high lane utilization across Top 25 commercial airfields. |
| EQ-03 | Stochastic Queuing & Congestion Theory | Traffic Intensity / Checkpoint Utilization Ratio | \rho(t) = \frac{\lambda(t)}{c(t) \cdot \mu} | rho(t) = lambda(t) / (c(t) * mu) | rho(t) = Instantaneous traffic intensity at hour t; lambda(t) = Hourly passenger arrival demand rate; c(t) = Number of open screening lanes at hour t; mu = Nominal screening throughput rate per lane (pax/lane-hr). | Kendall, D. G. (1953). Stochastic processes occurring in the theory of queues and their analysis by the method of the imbedded Markov chain. The Annals of Mathematical Statistics, 24(3), 338–354; Erlang, A. K. (1909). | Operationalized in Chapter III Macro Filtering (§3.4): small regional airfields operate at rho << 0.30 (preventing queue formation), whereas Top 25 hubs routinely hit rho -> 1.0 during bank surges (05:00–08:30 and 16:00–18:30). |
| EQ-04 | Passenger Lead-Time & Arrival Curves | Lognormal Passenger Show-Up Lead-Time Distribution | \tau \sim \text{Lognormal}(\mu, \sigma^2), \quad E[\tau] \approx 105 \text{ min} | tau ~ Lognormal(mu, sigma^2), with E[tau] ≈ 105 minutes | tau = Lead time (minutes before scheduled departure) that ticketed passengers present at security; mu = Log-scale mean; sigma = Log-scale dispersion; E[tau] = Expected show-up lead time (~105 minutes for domestic legacy flights). | Airport Cooperative Research Program (ACRP). (2010). ACRP Report 40: Airport Curbside and Terminal Area Planning. Transportation Research Board, National Academies of Sciences, Engineering, and Medicine. | Governs the empirical lead-lag passenger arrival distribution convolving scheduled flight banks into landside security arrival curves across American Airlines, Delta Air Lines, and United Airlines. |
| EQ-05 | Passenger Lead-Time & Arrival Curves | Gaussian Mixture Bimodal Boarding Arrival Distribution | \tau_{\text{WN}} \sim w_1 \mathcal{N}(\mu_1, \sigma_1^2) + (1 - w_1) \mathcal{N}(\mu_2, \sigma_2^2) | tau_WN ~ w1 * N(mu1, sigma1^2) + (1 - w1) * N(mu2, sigma2^2) | tau_WN = Southwest passenger arrival lead time; w1 = Weight of boarding position maximizers (~135 min lead time); (1-w1) = Weight of carry-on business travelers (~65 min lead time). | ACRP Report 40 (TRB, 2010); Pearson, K. (1894). Contributions to the mathematical theory of evolution. Philosophical Transactions of the Royal Society of London, 185, 71–110. | Empirically demonstrates that unassigned boarding produces bimodal arrival distributions, justifying Southwest Airlines exclusion under Meso Filtering to prevent passenger show-up heterogeneity. |
| EQ-06 | Operational Accounting & Filtering | Local Originating Passenger Demand Accounting Identity | \text{Demand}_{\text{orig}, t} = \sum_{f \in \mathcal{F}_t} \text{Seats}_f \cdot \text{LoadFactor}_f \cdot (1 - \text{ConnectingRatio}_{\text{airport}}) | Demand_orig(t) = sum_{f in F_t} [ Seats_f * LoadFactor_f * (1 - ConnectingRatio_airport) ] | Demand_orig,t = True originating passenger demand entering landside screening at hour t; Seats_f = Aircraft seat capacity for flight f; LoadFactor_f = Route-level passenger load factor; ConnectingRatio = Quarterly airport connecting percentage from DB1B. | Bureau of Transportation Statistics (BTS). (2024). Form 41 Schedule T-100 Segment Data and DB1B Airline Origin and Destination Survey. U.S. Department of Transportation. | Resolves the Hub Disconnect: subtracts transferring passengers who never enter landside security queues, increasing explained schedule-to-checkpoint variance from 20.9% to 44.9% across the Top 25 airfields. |
| EQ-07 | Passenger Lead-Time & Arrival Curves | Discrete Empirical Lead-Time Convolution (Finite Impulse Response) | \text{Demand}_{\text{convolved}, t} = \sum_{h=1}^{3} w_h \cdot \left[ \sum_{f \in \mathcal{F}_{t+h}} \text{Seats}_f \cdot \text{LoadFactor}_f \cdot (1 - \text{ConnectingRatio}) \right] | Demand_convolved(t) = sum_{h=1..3} [ w_h * Demand_orig(t+h) ] | w_h = Empirical ACRP arrival weights: w_1 (t+1 hr lead) = 0.52, w_2 (t+2 hr lead) = 0.38, w_3 (t+3 hr lead) = 0.10, where sum(w_h) = 1.0; F_{t+h} = Set of scheduled departures at hours t+1, t+2, t+3. | ACRP Report 40 (TRB, 2010); Oppenheim, A. V., & Schafer, R. W. (2009). Discrete-Time Signal Processing (3rd ed.). Prentice Hall. | The physical operational engine of Model 1 (Deterministic Flight Schedule Model), convolving scheduled departure banks into landside arrival hours to forecast baseline passenger demand. |
| EQ-08 | Statistical Moments & Volatility Targets | Intraday Diurnal Absolute Volume Volatility (Dispersion) | \sigma_{\text{TSA, hr}}(d) = \sqrt{\frac{1}{23} \sum_{h=0}^{23} (y_{d, h} - \bar{y}_d)^2} | sigma_TSA_hr(d) = sqrt( (1 / 23) * sum_{h=0..23} (y_{d,h} - y_bar_d)^2 ) | sigma_TSA,hr(d) = Diurnal standard deviation of hourly passenger screening throughput on day d (pax/hr); y_{d,h} = Hourly TSA throughput at hour h; y_bar_d = Daily mean hourly throughput. | Pearson, K. (1894). Contributions to the mathematical theory of evolution. Philosophical Transactions of the Royal Society of London, 185, 71–110. | Primary dependent modeling target 1: captures within-day absolute demand dispersion across the 24 hours of each day (in pax/hr), isolating bank surge amplitudes. |
| EQ-09 | Statistical Moments & Volatility Targets | Intraday Scale-Free Relative Arrival Volatility (Coefficient of Variation) | CV_{\text{TSA, hr}}(d) = \frac{\sigma_{\text{TSA, hr}}(d)}{\bar{y}_d} = \frac{\sqrt{\frac{1}{23}\sum_{h=0}^{23} (y_{d,h} - \bar{y}_d)^2}}{\frac{1}{24}\sum_{h=0}^{23} y_{d,h}} | CV_TSA_hr(d) = sigma_TSA_hr(d) / y_bar_d | CV_TSA,hr = Dimensionless ratio of hourly standard deviation to daily mean throughput. | Pearson, K. (1895). Notes on regression and inheritance in the case of two parents. Proceedings of the Royal Society of London, 58, 240–242. | Primary dependent modeling target 2: removes facility baseline scale to quantify pure arrival burstiness and queue surge spikiness across different checkpoint geometries. |
| EQ-10 | Statistical Moments & Volatility Targets | Multi-Day Temporal Rolling Volatility | \sigma_{\text{TSA, 7d}}(d) = \sqrt{\frac{1}{6} \sum_{k=0}^{6} (Y_{d-k} - \bar{Y}_{7d})^2} | sigma_TSA_7d(d) = sqrt( (1 / 6) * sum_{k=0..6} (Y_{d-k} - Y_bar_7d)^2 ) | sigma_TSA,7d(d) = Rolling 7-day standard deviation of daily passenger volume (pax/day); Y_{d-k} = Total daily throughput on day d-k; Y_bar_7d = 7-day rolling mean daily throughput. | Box, G. E., Jenkins, G. M., Reinsel, G. C., & Ljung, G. M. (2015). Time Series Analysis: Forecasting and Control (5th ed.). John Wiley & Sons. | Primary dependent modeling target 3: captures medium-term multi-day network turbulence caused by severe winter storm systems, convective ground delay programs, and cancellation cascades. |
| EQ-11 | Statistical Moments & Volatility Targets | Daily Flight Departure Delay Dispersion | \sigma_{\text{Delay}, d} = \sqrt{\frac{1}{N_d - 1}\sum_{i=1}^{N_d} (\text{DepDelay}_{d,i} - \bar{\text{DepDelay}}_d)^2} | sigma_Delay(d) = sqrt( (1 / (N_d - 1)) * sum_{i=1..N_d} (DepDelay_{d,i} - DepDelay_bar_d)^2 ) | sigma_Delay,d = Sample standard deviation of flight departure delays across all uncancelled domestic departures on day d (minutes); DepDelay_i = Actual minus scheduled departure time for flight i; N_d = Total domestic departures. | Standard sample variance; Bureau of Transportation Statistics (BTS). (2024). Airline On-Time Performance Data Technical Reporting Directives. | Primary airside explanatory volatility metric: exhibits strong operational coupling with landside checkpoint arrival volatility (r = +0.4373, p < 0.05), while raw delay minutes show zero correlation (r = -0.062). |
| EQ-12 | Time-Series Forecasting & Error Metrics | Root Mean Squared Error (RMSE) | \text{RMSE} = \sqrt{\frac{1}{N}\sum_{t=1}^N (y_t - \hat{y}_t)^2} | RMSE = sqrt( (1 / N) * sum_{t=1..N} (y_t - y_hat_t)^2 ) | RMSE = Quadratic loss forecast error (pax/hr); y_t = Actual observed volatility; y_hat_t = Model-predicted volatility; N = Sample evaluation hours. | Standard quadratic loss metric in statistical estimation and econometric forecasting. | Governing absolute error metric for Dimension 1 (Robustness): Model 3 achieves lowest RMSE (222.1 pax/hr) on the 2025 holdout dataset (-91.3 pax/hr vs Model 1). |
| EQ-13 | Time-Series Forecasting & Error Metrics | Mean Absolute Error (MAE) | \text{MAE} = \frac{1}{N} \sum_{t=1}^N \|y_t - \hat{y}_t\| | MAE = (1 / N) * sum_{t=1..N} \|y_t - y_hat_t\| | MAE = Linear loss forecast error (pax/hr); absolute difference between observed and predicted values. | Standard linear loss metric in time-series forecasting and regression. | Measures typical magnitude of point forecast errors without quadratic penalty for outliers; Model 3 achieves 142.8 pax/hr across dedicated screening complexes. |
| EQ-14 | Time-Series Forecasting & Error Metrics | Mean Forecast Bias (Directional Systematic Error) | \text{Bias} = \frac{1}{N} \sum_{t=1}^N (\hat{y}_t - y_t) | Bias = (1 / N) * sum_{t=1..N} (y_hat_t - y_t) | Bias = Mean directional error (pax/hr); negative values indicate systematic under-prediction; positive values indicate over-prediction. | Standard forecast bias metric in operations research and inventory management. | Evaluates systematic under-prediction during bank surges: Model 1 displays -42.1 pax/hr bias; Model 2 exhibits -18.4 pax/hr; Model 3 maintains near-zero bias (-8.5 pax/hr). |
| EQ-15 | Time-Series Forecasting & Error Metrics | Mean Absolute Scaled Error (MASE) | \text{MASE} = \frac{\frac{1}{N}\sum_{t=1}^N \|y_t - \hat{y}_t\|}{\frac{1}{N-24}\sum_{t=25}^N \|y_t - y_{t-24}\|} | MASE = MAE_model / MAE_naive_24h_persistence | MASE = Scale-free relative forecast accuracy metric; numerator is candidate model MAE; denominator is in-sample mean absolute error of 24-hour diurnal naive persistence control. | Hyndman, R. J., & Koehler, A. B. (2006). Another look at measures of forecast accuracy. International Journal of Forecasting, 22(4), 679–688. | Primary scale-free benchmark metric across all models and regimes: Baseline Control is calibrated at MASE = 1.000; Model 2 achieves MASE = 0.779; Model 3 achieves champion MASE = 0.662. |
| EQ-16 | Hypothesis & Significance Testing | Diebold-Mariano Test Statistic for Equal Predictive Accuracy | DM = \frac{\bar{d}}{\sqrt{\hat{V}(\bar{d}) / N}} \sim \mathcal{N}(0, 1) | DM = d_bar / sqrt(Var_hat(d_bar) / N) ~ N(0, 1) | d_t = e_{1,t}^2 - e_{2,t}^2 (Loss differential at time t); d_bar = Sample mean loss differential; Var_hat(d_bar) = Asymptotic long-run variance of loss differential. | Diebold, F. X., & Mariano, R. S. (1995). Comparing predictive accuracy. Journal of Business & Economic Statistics, 13(3), 253–263. | Formally proves that Model 2 (DM = 42.15, p < 0.0001) and Model 3 (DM = 48.72, p < 0.0001) error reductions over Model 1 are genuine statistical improvements rather than random chance. |
| EQ-17 | Hypothesis & Significance Testing | Chow Test Statistic for Structural Breaks in Linear Regressions | F = \frac{(RSS_C - (RSS_1 + RSS_2)) / k}{(RSS_1 + RSS_2) / (N_1 + N_2 - 2k)} \sim F(k, N_1 + N_2 - 2k) | F = [ (RSS_C - (RSS_1 + RSS_2)) / k ] / [ (RSS_1 + RSS_2) / (N_1 + N_2 - 2k) ] | RSS_C = Residual sum of squares of pooled model; RSS_1, RSS_2 = Residual sums of squares of pre- and post-break sub-periods; k = Number of parameters; N_1, N_2 = Sample sizes. | Chow, G. C. (1960). Tests of equality between sets of coefficients in two linear regressions. Econometrica, 28(3), 591–605. | Statistically justified the Candidate B temporal demarcation point (May 1, 2022 post-mask mandate): Chow test confirms structural stability (p >= 0.15) for the post-mandate modern operational regime. |
| EQ-18 | Hypothesis & Significance Testing | CUSUM Test for Structural Parameter Stability | W_t = \sum_{r=k+1}^t \frac{w_r}{\hat{\sigma}_w} | W_t = sum_{r=k+1..t} [ w_r / sigma_hat_w ] | W_t = Cumulative sum of standardized recursive residuals w_r; sigma_hat_w = Sample standard deviation of recursive residuals; k = Number of regression regressors. | Brown, R. L., Durbin, J., & Evans, J. M. (1975). Techniques for testing the constancy of regression relationships over time. Journal of the Royal Statistical Society: Series B, 37(2), 149–163. | Demonstrates that cumulative recursive residuals stay strictly within the 95% confidence bands from May 2022 through Dec 2025, validating model training data integrity. |
| EQ-19 | Statistical Moments & Volatility Targets | Peak-to-Average Ratio (PAR / Crest Factor) | \text{PAR}_d = \frac{\max_{h \in [0,23]} y_{d,h}}{\frac{1}{24}\sum_{h=0}^{23} y_{d,h}} | PAR_d = max(y_{d,h}) / mean(y_{d,h}) | PAR_d = Ratio of maximum hourly throughput on day d to that day's average hourly volume; measures acute demand concentration into a single peak hour. | Standard engineering and operational metrics (Crest Factor / Peak-to-Average Ratio); Oppenheim & Schafer (2009). | Standard literature replacement for S_TSA: identifies days where checkpoint queues experience extreme surge concentration into an acute morning or evening rush hour. |
| EQ-20 | Operational Dimensioning & Staffing | Volatility-Buffered Safety Capacity Lane Dimensioning Rule | c(t) = \left\lceil \frac{\hat{\mu}_t + z_q \cdot \hat{\sigma}_{\text{TSA}, t}}{\mu_{\text{lane}}} \right\rceil | c(t) = ceil( (mu_hat_t + z_q * sigma_hat_t) / mu_lane ) | c(t) = Recommended integer number of open screening lanes at hour t; mu_hat_t = Expected hourly passenger arrivals; sigma_hat_t = Forecasted arrival volatility; z_q = Normal service quantile (e.g., 1.645 for 95% service level); mu_lane = Lane throughput capacity (pax/lane-hr). | Erlang, A. K. (1917); Kolesar, P., & Green, L. (1998). Insights on capacity planning using a queuing model. Management Science; Whitt, W. (1992). Understanding the efficiency of multi-server service systems. Management Science, 38(5), 708–723. | Translates volatility forecasts into actionable security checkpoint lane dimensioning in Chapter V (§5.2), proving that buffering for volatility (sigma) prevents heavy-traffic queue collapse under Kingman's formula. |

*Note. Master census of all 20 peer-reviewed operational, queuing, econometrics, and lane allocation equations utilized across Chapters I–V.*

---

# Appendix C: Queuing Theory Derivations, Heavy-Traffic Approximations, and Volatility Dispersion Formulations

> **Operational Cross-Reference**: This appendix establishes the formal mathematical derivations of heavy-traffic queuing approximations, compound Poisson dispersion mechanics, and primary throughput volatility targets. It is referenced in **Chapter II (Literature Review)**, Section 2.1 (*Theoretical Foundations: Queuing Theory and Kingman's Heavy-Traffic Approximations*) and Section 2.2 (*Volume Versus Volatility*); in **Chapter III (Methodology)**, Section 3.1 (*Core Research Target: Throughput Volatility*); and in **Chapter IV (Results)**, Section 4.2 (*Intraday Volatility Dynamics*).

## C.1 Classical Poisson and Kendall Notation Formulations

In classical queuing systems, screening facilities are formalized using Kendall notation $A/S/c/K/N/D$, typically reduced to $A/S/s$, where $A$ represents the inter-arrival time distribution, $S$ represents the service time distribution, and $s$ denotes the number of parallel active screening lanes. In an $M/M/s$ queuing model, arrival intervals follow a Poisson process with arrival rate $\lambda$, and service durations adhere to an exponential distribution with service rate $\mu$ per active screening lane. The operational traffic intensity (utilization rate) $\rho$ is formulated as:

$$\rho = \frac{\lambda}{s \cdot \mu}$$

Under steady-state equilibrium ($\rho < 1.0$), the probability of zero entities in the system $P_0$ and the expected waiting time in queue $W_q$ are derived from Erlang-C formulations:

$$P_0 = \left[ \sum_{n=0}^{s-1} \frac{(s \cdot \rho)^n}{n!} + \frac{(s \cdot \rho)^s}{s! \cdot (1 - \rho)} \right]^{-1}$$

$$W_q = \left[ \frac{(s \cdot \rho)^s}{s! \cdot (1 - \rho)^2 \cdot s \cdot \mu} \right] \cdot P_0$$

## C.2 Non-Homogeneous Poisson Processes (NHPP)

To accommodate the time-varying nature of airline flight schedules, Non-Homogeneous Poisson Processes (NHPP) replace static arrival rate $\lambda$ with an integrable, deterministic time-dependent rate function $\lambda(t)$. The expected cumulative arrival count $m(t)$ over interval $[0, t]$ is formulated as:

$$m(t) = \int_0^t \lambda(u) \, du$$

While NHPP accommodates diurnal wave patterns, it remains fundamentally bounded by the assumption of independent increments, failing to account for intra-bank passenger correlations where ticketed passenger cohorts arrive in tight, non-independent clusters.

## C.3 Heavy-Traffic Queuing and the Kingman / Allen-Cunneen Approximations

In heavy-traffic regimes where lane utilization approaches maximum saturation ($\rho \to 1.0$), the Allen-Cunneen approximation for general $G/G/s$ screening facilities demonstrates that expected waiting times scale linearly not with mean volume, but with arrival and service volatility:

$$W_q \approx \left[ \frac{C_a^2 + C_s^2}{2} \right] \cdot \left[ \frac{\rho}{1 - \rho} \right] \cdot \left( \frac{1}{s \cdot \mu} \right)$$

where $C_a^2 = \frac{\text{Var}(T_a)}{[\mathbb{E}(T_a)]^2}$ is the squared coefficient of variation of inter-arrival times, and $C_s^2 = \frac{\text{Var}(T_s)}{[\mathbb{E}(T_s)]^2}$ is the squared coefficient of variation of screening durations. As utilization $\rho$ approaches $1.0$ during scheduled flight bank departures, the non-linear scaling multiplier $\left[ \frac{\rho}{1 - \rho} \right]$ amplifies arrival volatility $C_a^2$ exponentially, triggering terminal crowd surges.

## C.4 Tweedie-Poisson Compound Dispersion Mechanics

The relationship between passenger arrival volume and intraday volatility is governed by compound Poisson dispersion. Checkpoint hourly arrival counts $Y_t$ follow an exponential dispersion model where the variance scales as a power function of the mean volume:

$$\text{Var}(Y_t) = \phi \cdot [\mathbb{E}(Y_t)]^p$$

where $p \in (1, 2)$ represents a Tweedie compound Poisson-gamma distribution, and $\phi$ is the dispersion scale parameter. Because intraday variance $\sigma_{\text{TSA, hr}}$ naturally expands alongside total scheduled seats, published flight schedules provide an accurate baseline predictor for routine volume. Conversely, multi-day volatility $\sigma_{\text{TSA, 7d}}$ is driven by disruption volatility (flight cancellation rates, delay spreads, and gate holds).

## C.5 Scale-Free Coefficient of Variation ($CV_{\text{TSA}}$) and Multi-Day Volatility Formulations

Construct validity requires establishing explicit mathematical formulations that target passenger throughput volatility rather than static volume levels:

1. **Intraday Diurnal Absolute Volatility ($\sigma_{\text{TSA, hr}}$, pax/hr dispersion)**:
$$\sigma_{\text{TSA, hr}}(d) = \sqrt{\frac{1}{23} \sum_{h=0}^{23} (Y_{d, h} - \bar{Y}_d)^2}$$

2. **Intraday Scale-Free Relative Volatility ($CV_{\text{TSA, hr}}$, dimensionless ratio)**:
$$CV_{\text{TSA, hr}}(d) = \frac{\sigma_{\text{TSA, hr}}(d)}{\bar{Y}_d} = \frac{\sqrt{\frac{1}{23}\sum_{h=0}^{23} (Y_{d,h} - \bar{Y}_d)^2}}{\frac{1}{24}\sum_{h=0}^{23} Y_{d,h}}$$

3. **Multi-Day Temporal Rolling Volatility ($\sigma_{\text{TSA, 7d}}$, pax/day network turbulence)**:
$$\sigma_{\text{TSA, 7d}}(d) = \sqrt{\frac{1}{6} \sum_{k=0}^{6} (D_{d-k} - \bar{D}_{7d})^2}$$

### Table C.1
*Airport Checkpoint Queuing Dynamics, Kingman Formulations, and Volatility Dispersion Metrics*

[**Companion Excel Tab:** `'Table_C1_Queuing'` in `Appendix_Tables.xlsx`]  
| Queuing / Volatility Dimension | Mathematical Formulation | Operational Meaning in Airport Terminals | Theoretical Parameter Constraints | Empirical Baseline Benchmark |
| :--- | :--- | :--- | :--- | :--- |
| Traffic Intensity / Utilization (ρ) | ρ = λ / (s · μ) | Proportion of active screening lane capacity occupied by arriving passenger flow. | 0.0 ≤ ρ < 1.0 for steady-state equilibrium; ρ → 1.0 during flight banks. | Peak bank mean: ρ = 0.842 across 9 cohort complexes. |
| Kingman Heavy-Traffic Approximation (W_q) | W_q ≈ [(C_a^2 + C_s^2)/2] · [ρ / (1 - ρ)] · (1 / (s · μ)) | Expected passenger queue waiting time scales quadratically with arrival volatility C_a^2 under saturation. | Approximation asymptotically exact as ρ → 1.0 in G/G/s queues. | Queue delay multiplier expands 4.8x when ρ shifts from 0.70 to 0.90. |
| Arrival Volatility Dispersion (C_a^2) | C_a^2 = Var(T_a) / [E(T_a)]^2 | Squared coefficient of variation of passenger checkpoint inter-arrival intervals. | C_a^2 = 1.0 for exponential arrivals; C_a^2 > 1.0 for clustered flight banks. | Commercial terminal flight banks: C_a^2 = 1.64 to 2.85. |
| Service Duration Volatility (C_s^2) | C_s^2 = Var(T_s) / [E(T_s)]^2 | Squared coefficient of variation of TSO divestiture, scanning, and bag inspection times. | C_s^2 < 1.0 under standardized automated screening lanes (ASL). | Standard lanes: C_s^2 = 0.42; TSA PreCheck: C_s^2 = 0.18. |
| Tweedie Compound Poisson Variance | Var(Y_t) = ϕ · [E(Y_t)]^p | Non-linear variance expansion of hourly checkpoint throughput counts with mean volume. | Tweedie index p ∈ (1, 2) indicates compound Poisson-gamma arrivals. | Empirical calibrate: p = 1.482, ϕ = 2.14 across Top 25 airfields. |
| Intraday Throughput Volatility (σ_{TSA, hr}) | σ_{TSA, hr} = sqrt( (1/23) · ∑_{h=0}^{23} (Y_{d,h} - μ_{d})^2 ) | Standard deviation of 24 hourly passenger counts across operating day d. | Non-negative dispersion metric; sensitive to diurnal peak-to-trough amplitude. | Cohort mean: 892.4 passengers/hr (nominal) to 1,482.1 pax/hr (peak). |
| Scale-Free Relative Volatility (CV_{TSA}) | CV_{TSA} = σ_{TSA, hr} / μ_{TSA, hr} | Dimensionless arrival burstiness normalized across small vs mega terminal complexes. | Scale-free ratio enabling direct cross-airport comparisons. | Cohort mean: 0.384 (Summer Peak) vs 0.281 (Winter Lull). |
| Multi-Day Rolling Volatility (σ_{TSA, 7d}) | σ_{TSA, 7d} = sqrt( (1/6) · ∑_{k=0}^{6} (D_{d-k} - μ_{7d})^2 ) | Rolling 7-day standard deviation of daily passenger volume capturing network turbulence. | Reflects macroeconomic shocks, holiday demand surges, and convective storm waves. | Cohort mean: 4,821 passengers/day across 9-airport complexes. |

*Note. Details heavy-traffic queuing formulations, Tweedie compound Poisson dispersion mechanics, and scale-free throughput volatility targets.*

---

# Appendix D: Temporal Scope, Post-Pandemic Demarcation, and Dataset Partitioning

> **Operational Cross-Reference**: This appendix establishes the empirical justification for excluding pandemic-period volatility, documents the post-pandemic demarcation point, and formalizes the 44-month longitudinal dataset partitioning design. It is referenced in **Chapter III (Methodology)**, Section 3.1 (*Dataset Partitioning and Validation Protocol*) and Section 3.2 (*Temporal Scope and Boundary Definition*); and in **Chapter IV (Results)**, Section 4.1 (*Post-Pandemic Temporal Demarcation Evaluation*).

## D.1 Post-Pandemic Temporal Demarcation and Structural Regime Shift

To ensure structural modeling integrity, the temporal boundaries of this sample exclude the systemic disruptions of the COVID-19 pandemic (2020 through early 2022). While passenger volume collapsed by more than $95\%$ during March–April 2020, commercial flight schedules were maintained at artificially inflated levels to protect airline airport slot rights and comply with federal CARES Act minimum service guarantees. This created a complete structural decoupling between flight schedules and passenger arrivals.

The empirical demarcation point is established on **May 1, 2022**, following the nationwide judicial vacatur and federal repeal of the commercial transportation mask mandate in late April 2022. This date marks the restoration of normal commercial travel behaviors and stable airline schedule-to-demand coupling across legacy carriers.

Econometric stability across the demarcation point was evaluated through two formal tests:
1. **Chow Structural Break Test**: Compares linear regression parameters pre- and post-May 1, 2022, confirming structural parameter stability ($F = 1.42, p = 0.18 > 0.05$).
2. **Cumulative Sum of Recursive Residuals (CUSUM)**: Confirms that recursive residuals remain bounded within $95\%$ confidence bands throughout the post-demarcation window (May 2022 through December 2025).

### Table D.1
*Dataset Partitioning Design: Development vs Holdout Windows and Temporal Embargoes*

[**Companion Excel Tab:** `'Table_D1_Partitioning'` in `Appendix_Tables.xlsx`]  
| Partition Designation | Operational Horizon | Calendar Date Range | Duration | Airport-Days (N) | Hourly Records (n) | Screening Complexes | Methodological Function & Validation Role |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Training Window | Model Training & Parameter Calibration | May 1, 2022 – Dec 31, 2023 | 20.0 Months | 15,976 | 122,847 | 9 Airports / 12 Complexes | Calibrate flight schedule convolution baseline; train decision-tree regressors on BTS OTP features; establish initial hybrid Stage 1 cycles. |
| Validation Window | Hyperparameter Tuning & Optimization | Jan 8, 2024 – Dec 24, 2024 | 11.8 Months | 3,293 | 72,723 | 9 Airports / 12 Complexes | Strictly reserved for hyperparameter tuning (tree depth, leaf size, learning rate), cross-validation, and error innovation loop gain calibration. |
| Out-of-Time Holdout Window | Blind Empirical Holdout Evaluation | Jan 1, 2025 – Dec 31, 2025 | 12.0 Months | 3,222 | 72,053 | 9 Airports / 12 Complexes | Certified out-of-time evaluation suite benchmarking Robustness (routine operations), Resilience (severe IROPS), and Generalizability (zero-shot transfer). |
| Total Longitudinal Dataset | Full Continuous Study Sequence | May 1, 2022 – Dec 31, 2025 | 44.0 Months | 22,491 | 267,623 | 9 Airports / 12 Complexes | Comprehensive longitudinal empirical foundation tracking carrier-exclusive terminal screening complexes across all four structural airport archetypes. |

*Note. Formal longitudinal partitioning structure across 44 continuous post-mask mandate months (May 1, 2022 to December 31, 2025).*

### Table D.2
*Post-Pandemic Temporal Demarcation Evaluation Across Candidate Longitudinal Horizons*

[**Companion Excel Tab:** `'Table_D2_Demarcation'` in `Appendix_Tables.xlsx`]  
[**Source Data Asset:** `results/tables/table_4_3a_post_pandemic_temporal_demarcation_evaluation.csv`]

| Evaluation Criteria | Candidate A: Mature Post-Pandemic | Candidate B: Early Post-Mask Regime (Selected) |
| :--- | :--- | :--- |
| Start Date | January 1, 2023 | May 1, 2022 (RECOMMENDED) |
| Statistical Demarcation Rationale | Rolling Welch's t-test variance convergence | CUSUM structural break stabilization; Mask Mandate Repeal |
| Training Span | 24 Months (2023-01 to 2024-12) | 32 Months (2022-05 to 2024-12; 20 mo train / 12 mo val) |
| Holdout Test Span | 12 Months (2025 Full-Year Holdout) | 12 Months (2025 Full-Year Holdout) |
| Robustness Impact | Excellent baseline stability; limited historical depth | Superior: Captures two complete annual seasonal cycles |
| Resilience Impact | Misses Winter Storm Elliott (Dec 2022) | Superior: Encapsulates severe winter freeze and summer storms |
| Generalizability Impact | Narrower training variance across spoke airfields | Superior: 404,324 candidate multi-facility hourly records |
| Coupling Rebound (R^2) | R^2 = 0.323 (Macro scheduled-to-TSA daily) | R^2 rebounds from 0.368 (COVID) to 0.306–0.323 (Equilibrium) |

*Note. Econometric and structural evaluation comparing Candidate A (Mature Post-Pandemic) and Candidate B (Early Post-Mask Mandate Regime).*

---

# Appendix E: Four-Tier Purposive Filtering Pipeline, Nine-Airport Cohort Selection, and Airport Contrasts

> **Operational Cross-Reference**: This appendix details the 4-tier filtering methodology isolating unconfounded carrier-exclusive checkpoint lanes and documents the 9-airport experimental cohort. It is referenced in **Chapter III (Methodology)**, Section 3.2 (*The Four-Tier Purposive Filtering Pipeline*) and Section 3.3 (*The Nine-Airport Experimental Cohort*); and in **Chapter IV (Results)**, Section 4.3 (*Nine-Airport Cohort Selection Findings*).

## E.1 Four-Tier Purposive Filtering Pipeline Mechanics

To eliminate lobby-sharing collinearity while preserving balanced experimental power across hub operational roles and geographic climate zones, airports were filtered through a rigorous 4-tier pipeline:

* **Tier 1 (Macro Filter - Federal Scale)**: Screened the Top 25 large-hub commercial airports by passenger enplanements, retaining $67.2\%$ of nationwide commercial volume where heavy-traffic utilization approaches capacity ($\rho \to 1.0$).
* **Tier 2 (Meso Filter - Big 3 Symmetry & WN Exclusion)**: Retained airports dominated by legacy network carriers (American, Delta, United) while excluding point-to-point carriers (e.g., Southwest Airlines at MDW, DAL) whose unassigned seating boarding behavior violates passenger arrival exchangeability.
* **Tier 3 (Micro Filter - Checkpoint Exclusivity)**: Filtered for carrier-exclusive screening complexes commanding $\ge 85\%$ of concourse gates, eliminating multi-carrier lobby mixing.
* **Tier 4 (Factorial Cohort Matrix)**: Established a balanced 9-airport experimental cohort crossing hub role (Connecting Hub vs Origin & Destination) with climate disruption archetype across 12 carrier-exclusive complexes (4 AA, 4 DL, 4 UA).

### Table E.1
*Top 25 Commercial Airport Census and Purposive Four-Tier Filtering Pipeline Funnel*

[**Companion Excel Tab:** `'Table_E1_Top25_Census'` in `Appendix_Tables.xlsx`]  
[**Source Data Asset:** `results/tables/table_4_7_summary_descriptive_statistics_nine_airport_vs_top25.csv`]

| Metric Category | Operational Metric | Unit | 9-Airport Mean | 9-Airport Std Dev | 9-Airport Median | 9-Airport Min (Airport) | 9-Airport Max (Airport) | Top 25 Mean | Delta (%) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| BTS OTP Operations | Scheduled Domestic Flights | flights | 224,576 | 78,441 | 206,024 | 138,372 (PHL) | 360,571 (ORD) | 192,160 | +16.9% |
| BTS OTP Operations | Cancelled Flights | flights | 3,623 | 1,599 | 2,920 | 1,777 (DTW) | 6,515 (DFW) | 2,738 | +32.3% |
| BTS OTP Operations | Flight Cancellation Rate | % | 1.63% | 0.50% | 1.47% | 0.99% (LAX) | 2.46% (LGA) | 1.43% | +14.1% |
| BTS OTP Delays | Average Departure Delay | min | 15.23 | 2.75 | 15.65 | 11.55 (DTW) | 19.85 (DFW) | 14.21 | +7.2% |
| BTS OTP Delays | Significant Delay Rate (>= 15m) | % | 21.42% | 3.30% | 20.14% | 17.93% (LAX) | 28.07% (DFW) | 20.31% | +5.5% |
| BTS OTP Delays | Runway Taxi-Out Queue Time | min | 20.59 | 2.58 | 20.35 | 16.96 (DTW) | 24.67 (EWR) | 19.69 | +4.5% |
| TSA Checkpoint | Total Passenger Throughput | pax | 71,145,628 | 27,465,238 | 63,720,916 | 40,429,531 (PHL) | 129,069,341 (LAX) | 68,495,531 | +3.9% |
| TSA Checkpoint | Average Daily Passenger Count | pax/day | 53,075 | 20,473 | 47,553 | 30,171 (PHL) | 96,249 (LAX) | 51,138 | +3.8% |
| TSA Checkpoint | Average Hourly Passenger Count | pax/hr | 418.53 | 157.02 | 388.40 | 239.60 (ORD) | 662.40 (LGA) | 540.34 | -22.5% |
| TSA Checkpoint | Peak Single-Hour Checkpoint Rush | pax/hr | 2,673 | 881 | 2,654 | 1,385 (DTW) | 4,020 (EWR) | 2,784 | -4.0% |
| TSA Checkpoint | Demand Volatility (CV_TSA) | ratio | 0.8728 | 0.2000 | 0.9064 | 0.6488 (BOS) | 1.1240 (LGA) | 0.8250 | +5.8% |
| BTS DB1B Surveys | Connecting Passenger Share | % | 47.45% | 10.98% | 44.41% | 33.58% (EWR) | 66.32% (DFW) | 51.39% | -7.7% |
| BTS DB1B Surveys | Local Originating Passenger Share | % | 52.55% | 10.98% | 55.59% | 33.68% (DFW) | 66.42% (EWR) | 48.61% | +8.1% |
| BTS DB1B Surveys | True Local Originating TSA Demand | pax | 16,376,561 | 5,167,458 | 15,995,278 | 10,555,299 (DTW) | 26,293,897 (LAX) | 13,103,484 | +25.0% |
| T-100 Aircraft Gauge | Seating Capacity per Flight | seats | 168.42 | 7.49 | 168.00 | 154.20 (LGA) | 182.30 (LAX) | 171.10 | -1.6% |
| T-100 Load Factor | Route Passenger Load Factor | % | 85.08% | 0.82% | 85.26% | 83.85% (DTW) | 86.12% (EWR) | 84.73% | +0.4% |

*Note. Compares systemwide operational scale across the Top 25 passenger network against the 9-airport experimental cohort.*

### Table E.2
*Nine-Airport Experimental Cohort Factorial Specification and Dedicated Carrier Complexes*

[**Companion Excel Tab:** `'Table_E2_Cohort_Matrix'` in `Appendix_Tables.xlsx`]  
[**Source Data Asset:** `results/tables/table_4_6_nine_airport_experimental_cohort_factorial_specification.csv`]

| Airport Code | Airport Name | Dominant Legacy Carrier | Carrier Hub Role | Dedicated Terminal Screening Complex | Cluster Archetype | Strategic Justification & Selection Rationale |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| BOS | Boston Logan | DL / AA | Dual Focus Station | Terminal A (DL) & Terminal B (AA) | Cluster 1: High-Density O&D Focus | Unconfounded Northeast high-yield O&D demand; physically separate terminal finger piers. |
| DFW | Dallas/Fort Worth | AA | Primary Fortress Hub | Terminal D Screening Complex | Cluster 0: Mega-Connecting Gateway | American Airlines primary mega-connecting fortress hub; high gauge international operations. |
| DTW | Detroit Metro | DL | Primary Fortress Hub | McNamara Terminal Complex | Cluster 2: High-Reliability Fortress | Delta primary Midwest fortress hub; world-class operational fluidity and high connecting ratio. |
| EWR | Newark Liberty | UA | Primary Fortress Hub | Terminal C Screening Complex | Cluster 3: Congested Coastal Originator | United primary East Coast fortress hub; severe New York airspace slot congestion. |
| IAH | Houston Bush | UA | Primary Fortress Hub | Terminal C Screening Complex | Cluster 1: High-Density O&D Focus | United southern hub; balanced energy sector business O&D travel and Latin American connecting banks. |
| LAX | Los Angeles World | DL / AA / UA | Tri-Carrier Parity Hub | Terminals 2/3 (DL), 4 (AA), 7 (UA) | Cluster 0: Mega-Connecting Gateway | Massive transpacific and transcontinental origin-destination demand across all three legacy carriers. |
| LGA | New York LaGuardia | DL | Primary Fortress Hub | Terminal C Screening Complex | Cluster 3: Congested Coastal Originator | Consolidated Delta Terminal C (opened June 2022); perimeter rule market and pure O&D flows. |
| ORD | Chicago O'Hare | UA / AA | Dual Fortress Hub | Terminal 1 (UA) & Terminal 3 (AA) | Cluster 0: Mega-Connecting Gateway | Intense head-to-head legacy carrier competition; dual hub bank synchronization. |
| PHL | Philadelphia Intl | AA | Primary Fortress Hub | Terminals B & C Complexes | Cluster 2: High-Reliability Fortress | American Mid-Atlantic transatlantic hub; counterpart to Delta's Midwestern fortress at DTW. |

*Note. 4x4 balanced factorial evaluation cohort crossing hub role with climate disruption vulnerability across 12 carrier-exclusive complexes.*

## E.2 Key Airport Selection Contrasts and Structural Exclusions

Table E.3 documents specific structural inclusion and exclusion rationale across key candidate airfields:

### Table E.3
*Key Airport Selection Contrasts and Structural Facility Exclusion Matrix*

[**Companion Excel Tab:** `'Table_E3_Selection_Contrasts'` in `Appendix_Tables.xlsx`]  
[**Source Data Asset:** `figures/ch03_methodology/airport_selection_strategy_document.csv`]

| component | focus_area | implementation_details | methodological_rationale |
| :--- | :--- | :--- | :--- |
| Purposive Sampling Funnel | The 4-Tiered Purposive Filtering Pipeline | Macro volume (Top 25) -> Meso Big 3 co-location & Southwest exclusion -> Micro causal identification via checkpoint exclusivity -> 4x3 experimental transfer grid | Eliminates multi-carrier schedule crosstalk and isolates single-carrier passenger demand. |
| Candidate Justification | LGA Selection Over JFK | LGA selected; JFK excluded | United vacated JFK in October 2022 while LGA opened Delta's $4B consolidated Terminal C in June 2022. |
| Candidate Justification | PHL Selection Over SLC/MSP/SEA/PHX | PHL selected; SLC/MSP/SEA/PHX excluded | SLC channels 100% of passengers through one shared checkpoint; PHL Terminals B and C are 100% dedicated to American Airlines. |
| Temporal Boundary | Network-Level Temporal Demarcation | May 1, 2022 onwards across Top 25 hub network (~67% national volume) | Prevents localized recovery distortions across coupled nodes in the National Airspace System. |

*Note. Documents structural selection and exclusion rationale for contrasting facilities (e.g., EWR vs LGA, DFW vs IAH, CLT connecting paradox).*

---

# Appendix F: Multi-Source Aviation Data Feeds, ETL Architecture, and Data Hygiene Protocols

> **Operational Cross-Reference**: This appendix documents the multi-source data warehouse census, DuckDB ETL pipeline, and data hygiene protocols. It is referenced in **Chapter III (Methodology)**, Section 3.3 (*Sources of Data*) and Section 3.4 (*Treatment of Data & Star Schema ETL Pipeline*); and in **Chapter IV (Results)**, Section 4.1 (*Post-ETL Master Data Foundation Census*).

## F.1 Multi-Source Federal Aviation Feeds

The empirical warehouse synthesizes four federal aviation feeds spanning the 2019–2025 baseline:
1. **TSA FOIA Checkpoint Logs**: $19,500,286$ raw lane-hour rows processed into $6,434,732$ conformed lane-hours across 25 airfields (2.70B passengers).
2. **BTS On-Time Flight Performance (Form 234)**: $45,777,091$ raw flight rows processed into $13,153,654$ domestic mainline departures.
3. **BTS Form 41 Schedule T-100 Segment Data**: $1,945,451$ raw records processed into $422,096$ conformed carrier-segment-month observations.
4. **BTS DB1B / DB1C 10% Ticket Surveys**: $12,910,384$ raw coupon records processed into $22,051,557$ conformed coupons (62.16M travelers).

### Table F.1
*Master Post-ETL Multi-Source Data Foundation Census Across Federal Aviation Feeds*

[**Companion Excel Tab:** `'Table_F1_Data_Feeds'` in `Appendix_Tables.xlsx`]  
[**Source Data Asset:** `results/tables/table_4_1_master_post_etl_multi_source_data_foundation_census.csv`]

| Primary Data Feed | Entity Grain | Raw Ingested Rows | Post-ETL Cleaned Rows | Network & Facility Coverage | Conformance & Data Health Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| TSA FOIA Checkpoint Logs | Checkpoint-Lane-Hour | 19,500,286 | 6,434,732 | 25 Airfields, 955 Screening Lanes | 100% Non-Null; Zero Orphans; 2.70 Billion Passengers Screened |
| BTS On-Time Performance (OTP) | Flight Departure | 45,777,091 | 13,153,654 | 25 Airfields, 17 Reporting Carriers | 100% Non-Null Dimensions; 13.15 Million Domestic Departures Tracking Delays & Cancels |
| BTS Form 41 Schedule T-100 | Carrier-Route-Month | 1,945,451 | 422,096 | 25 Airfields, 18 Operating Carriers | 100% Non-Null Dimensions; 2.09 Billion Departing Seats, 1.70 Billion Passengers |
| BTS DB1B / DB1C Ticket Surveys | Ticket Coupon Itinerary | 12,910,384 | 22,051,557 | Closed 25-Airport City Pairs | 100% Non-Null Dimensions; 22.05 Million Coupon Records (62.16 Million Ticketed Travelers) |
| Combined Analytical Warehouse | Multi-Source Fact Records | 67,222,828 | 42,062,039 | Full 25-Airfield Candidate Network | Comprehensive conformed relational warehouse; 100% referential integrity |

*Note. Ingested vs cleaned conformed data row counts across TSA FOIA, BTS OTP, BTS T-100, and BTS DB1B federal databases.*

### Table F.2
*Unified Data Integrity, Threat Remediation, and Data Hygiene Matrix*

[**Companion Excel Tab:** `'Table_F2_Data_Threats'` in `Appendix_Tables.xlsx`]  
[**Source Data Asset:** `figures/ch03_methodology/combined_data_threats_and_remediation_matrix.csv`]

| severity | integrity_threat | data_source | prevalence_and_metric_symptom | failure_mode_theoretical_risk | methodological_cleansing_and_ml_action |
| :--- | :--- | :--- | :--- | :--- | :--- |
| CRITICAL | Lookahead Target Leakage (Contemporaneous delays) | BTS OTP (otpv0 / cloudv2) | Delay causes & actual gate times (depDel, depTime) contemporaneous with departures. | Produces illusory 99% training accuracy (R^2 > 0.98) that collapses completely in operational deployment. | Restricted Pre-Flight Features: Train models strictly on planned attributes (crsDepTime, scheduled seats); isolate realized delay metrics strictly to prior lagged windows (t-1) as airside congestion indicators. |
| CRITICAL | Unresolved Spatial Key (Phantom mega-airport) | TSA FOIA (tsav0 / cloudv2) | 35,809 blank rows in raw FOIA; 22,190 mapped to airportId = 0 (9.71M passengers). | Creates a synthetic nationwide 'phantom hub' that corrupts baseline parameters, cluster assignments, and spatial transferability. | Strict Dimension Key Enforcement: Enforce SQL filter WHERE airportMissing = 0 AND airportId > 0 in all modeling tables. Recover fingerprintable rows via canonical checkpoint lookup; discard residual unmapped keys. |
| CRITICAL | Load Factor Domain Exceedance (Math domain boundary) | BTS T-100 (t100v0 / cloudv2) | 23 route segment records reporting loadFactor > 1.00 (max: 1.0145) due to overbooking/infants. | Triggers NaN loss gradients, undefined numerical states, and fatal crashes in Beta distributions and sigmoid activation layers. | Hard Upfront Clamping: Apply loadFactor = LEAST(1.0, GREATEST(0.0, loadFactor)) during ETL transformation before computing passenger demand features. |
| HIGH | Target Zero-Inflation & Skewness (Overnight physical shutdowns) | TSA Fact (tsav0 / v1) | 450,973 zero rows (2.31% of data) during 00:00-03:59; skewness = 2.72. | Gaussian loss models produce nonsensical negative passenger predictions and underestimate daytime peak queue surges. | Hurdle & Tweedie Formulations: Do NOT discard zeros (they reflect true lane closures). Add is_night_closure = 1. Train with Tweedie deviance loss (p = 1.3) or a Two-Stage Hurdle model (Binary Classifier -> Count Regressor). |
| HIGH | Lead-Lag Temporal Asynchrony (Arrival show-up distribution) | TSA <-> BTS OTP (Cross-Source) | 60-180 min lead time between security screening entry and scheduled wheel-off (t_TSA << t_OTP). | Phase-shift misspecification (t <-> t error); treats departing flights as instantaneous security demand. | Empirical Demand Convolution: Convolve flight seats into forward horizons (t+1, t+2, t+3) via Lognormal arrival density kernel (mode approx 92.5 min) with discrete weights (0.25, 0.55, 0.20). |
| HIGH | Airside Connecting Passenger Bypass (Fortress hub transfer bias) | BTS DB1B <-> OTP (Market Survey) | 40% to 76% of passengers at fortress hubs (CLT: 76%, DFW: 55%, ATL: 64%) are connecting transfers who never clear landside TSA. | Massive structural overestimation of landside checkpoint volume at hub airfields, causing throughput paradoxes. | O&D Scale Factor Deflation: Deflate scheduled seats by airport-specific origin-and-destination ratio: Demand = Seats * LF * gamma_OD, where gamma_OD in [0.24, 0.95] is calibrated from DB1B ticket coupon data. |
| HIGH | Extreme Class Imbalance & Cancellations (Acute disruption shocks) | BTS OTP (Flight Status) | 988,155 cancellations (2.16%); 271,543 unassigned tails (0.59%); diversions 0.24%. | Standard loss functions ignore rare shock events, causing severe queue blowout during ground delay programs (GDPs). | Advance vs. Tactical Decoupling: If cancelled > 24h ahead, exclude from demand. If cancelled tactically (< 2h), retain passengers in queue (they already passed TSA). Evaluate shocks via PR-AUC and Resilience Multiplier R_MASE. |
| HIGH | Structural Regime Drift (Pandemic recovery non-stationarity) | Multi-Dataset (Temporal) | Pre-2020 vs. 2020-2021 shock vs. post-2022 recovery dynamics; federal mask mandate repeal April 2022. | Violates statistical parameter exchangeability (f_t(tau) != f(tau)); overfits to localized recovery artifacts. | Demarcation & Walk-Forward CV: Establish May 1, 2022 boundary (providing 36 mo training + 12 mo 2025 testing); apply purged walk-forward CV with a 7-day embargo buffer and exponential sample decay W_i = exp(-lambda(T_max - t_i)). |
| MODERATE | Feature Multicollinearity (Redundant flight delay terms) | BTS OTP (otpv0 / cloudv2) | Correlation r = 0.9975 between depDel and depDelMin; zero-variance features. | Inflates parameter coefficient variance, destabilizes gradient descent, and creates uninterpretable regression weights. | Parsimonious Feature Selection: Drop depDelMin, depDelGroups, and zero-variance columns; retain single canonical departure delay indicator. |
| MODERATE | High-Cardinality Entity Sparsity (Lanes and aircraft tails) | TSA & BTS OTP (Dimensions) | 7,617 unique aircraft tail numbers; 7,370 physical checkpoint lanes across the nation. | Extreme one-hot encoding sparsity (>10,000 columns); causes tree overfitting and Gram matrix inversion failure. | Hierarchical Dimension Aggregation: Map tail numbers to 40 conformed BTS aircraft models and 3 seating tiers (Regional, Narrowbody, Widebody); aggregate adjacent screening lanes into unified terminal complexes. |
| MODERATE | Ingestion Shifting & Lineage Audit (FOIA schema evolution) | TSA FOIA (tsav0 / cloudv2) | 154 records in late 2025/2026 with lane acronyms shifted into airport code columns; lane string variants (e.g. SBP01 vs BP01). | Silent data corruption, record drops, and unexplainable step-downs in longitudinal throughput trendlines. | Audit Lineage Metadata: Append non-destructive tracking columns: is_imputed (BOOL), imputation_method (VARCHAR), and imputation_confidence (FLOAT [0,1]). |

*Note. Protocols resolving lane fingerprint variations, structural zeros (night closures), tactical cancellations, and ghost demand.*

### Table F.3
*Post-ETL Master Summary Descriptive Statistics Across Key Operational Variables*

[**Companion Excel Tab:** `'Table_F3_Descriptive_Stats'` in `Appendix_Tables.xlsx`]  
[**Source Data Asset:** `results/tables/table_4_2_post_etl_master_summary_descriptive_statistics.csv`]

| Operational Domain | Variable Name | Sample Size (N) | Mean | Median | Std Dev | IQR | Min | Max | 5th Pct | 95th Pct |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| TSA Throughput | Hourly Lane Throughput (pax/hr) | 6,434,732 | 420.17 | 293.00 | 444.84 | 447.00 | 0.00 | 5,336.00 | 10.00 | 1,316.00 |
| Flight Delays | Flight Departure Delay (minutes) | 13,153,654 | 12.70 | -2.00 | 52.75 | 14.00 | -105.00 | 3,695.00 | -10.00 | 83.00 |
| Flight Delays | Significant Delay Rate (>= 15 min) | 13,153,654 | 20.12% | 0.00% | 40.09% | 0.00% | 0.00% | 100.00% | 0.00% | 100.00% |
| Flight Operations | Flight Cancellation Rate | 13,153,654 | 2.03% | 0.00% | 14.09% | 0.00% | 0.00% | 100.00% | 0.00% | 100.00% |
| Flight Operations | Runway Taxi-Out Queue Time (min) | 13,153,654 | 18.84 | 16.00 | 10.03 | 9.00 | 1.00 | 180.00 | 8.00 | 39.00 |
| Flight Operations | Airborne Flight Duration (min) | 13,153,654 | 141.50 | 126.00 | 75.40 | 92.00 | 15.00 | 720.00 | 45.00 | 310.00 |
| Flight Operations | Scheduled Flight Distance (miles) | 13,153,654 | 1,052.12 | 867.00 | 624.80 | 820.00 | 67.00 | 5,095.00 | 230.00 | 2,550.00 |
| Route Capacity | Available Seats per Route-Month | 422,096 | 4,962.40 | 2,512.00 | 7,019.66 | 5,480.00 | 1.00 | 145,200.00 | 120.00 | 19,200.00 |
| Route Capacity | Transported Pax per Route-Month | 422,096 | 4,030.05 | 1,927.00 | 5,938.42 | 4,380.00 | 0.00 | 128,500.00 | 85.00 | 15,800.00 |
| Route Capacity | Route Load Factor (%) | 422,096 | 81.21% | 83.40% | 11.80% | 12.50% | 0.00% | 100.00% | 58.40% | 94.20% |
| Passenger Surveys | Connecting Passenger Fraction (%) | 22,051,557 | 51.39% | 50.73% | 11.74% | 16.20% | 33.58% | 76.04% | 35.69% | 70.09% |

*Note. Parametric and non-parametric dispersion statistics (Mean, SD, Median, IQR, Min, Max) across 22,491 airport-days.*

---

# Appendix G: Statistical Significance Testing: Diebold-Mariano, Chow, and CUSUM Foundations

> **Operational Cross-Reference**: This appendix establishes the econometric proofs and formulations for the Diebold-Mariano test, Newey-West HAC variance estimator, and Chow structural break tests. It is referenced in **Chapter III (Methodology)**, Section 3.5 (*Statistical Significance Testing: Diebold-Mariano and Econometric Foundations*); and in **Chapter IV (Results)**, Section 4.4 (*Statistical Significance Findings*).

## G.1 The Diebold-Mariano (DM) Forecast Accuracy Test

Standard paired $t$-tests assume independent and identically distributed ($i.i.d.$) errors, an assumption severely violated by the diurnal autocorrelation and ARCH volatility clustering inherent in hourly checkpoint time series. Applying standard $t$-tests to autocorrelated time-series forecast residuals results in severe negative bias in the variance estimator, yielding spuriously deflated standard errors and artificially inflated $t$-statistics ($p$-value collapse).

To ensure valid statistical inference, pairwise model comparison is evaluated using the Diebold-Mariano (DM) test. Let $e_{1,t} = y_t - \hat{y}_{1,t}$ and $e_{2,t} = y_t - \hat{y}_{2,t}$ denote the forecast errors of two competing candidate models at hour $t$. The loss differential $d_t$ is defined as:

$$d_t = L(e_{1,t}) - L(e_{2,t}) = |e_{1,t}| - |e_{2,t}|$$

Under the null hypothesis $H_0: \mathbb{E}[d_t] = 0$, both candidate models exhibit equal expected forecast accuracy. The sample mean loss differential is:

$$\bar{d} = \frac{1}{T} \sum_{t=1}^T d_t$$

To account for serial correlation in the loss differential series $d_t$, the asymptotic long-run variance $\sigma_d^2$ is estimated using the Newey-West Heteroskedasticity and Autocorrelation Consistent (HAC) spectral density estimator at frequency zero:

$$\hat{\sigma}_d^2 = \hat{\gamma}_0 + 2 \sum_{k=1}^h \left( 1 - \frac{k}{h + 1} \right) \hat{\gamma}_k$$

where $\hat{\gamma}_k$ is the empirical autocovariance at lag $k$, and $h = 24$ hours is the truncation lag capturing full diurnal recurrence. The Diebold-Mariano test statistic is formulated as:

$$DM = \frac{\bar{d}}{\sqrt{\hat{\sigma}_d^2 / T}} \xrightarrow{d} \mathcal{N}(0, 1)$$

### Table G.1
*Diebold-Mariano Pairwise Forecast Accuracy Statistics and Econometric Parameter Estimates*

[**Companion Excel Tab:** `'Table_G1_Statistical_Tests'` in `Appendix_Tables.xlsx`]  
| Model Comparison Pair | Diebold-Mariano Stat (DM) | p-value (HAC) | Loss Differential Mean (d̄) | Newey-West Truncation Lag (h) | Statistical Significance | Econometric Interpretation |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Model 2 vs. Model 1 (Schedule) | +42.15 | < 0.001 | -28.4 pax/hr | 24 Hours (Diurnal) | Statistically Significant | Machine learning regressor significantly outperforms deterministic schedule baseline under routine operations. |
| Model 3 vs. Model 1 (Schedule) | +48.72 | < 0.001 | -36.2 pax/hr | 24 Hours (Diurnal) | Statistically Significant | Dynamic two-stage hybrid model decisively outperforms deterministic schedule baseline with lowest aggregate error. |
| Model 3 vs. Model 2 (Machine Learning) | +14.88 | < 0.001 | -7.8 pax/hr | 24 Hours (Diurnal) | Statistically Significant | Live error innovation feedback significantly reduces residual error variance beyond static decision trees. |
| Model 1 vs. Baseline Control | +18.34 | < 0.001 | -8.1 pax/hr | 24 Hours (Diurnal) | Statistically Significant | Flight schedule convolution baseline significantly outperforms 24-hour diurnal naive persistence. |

*Note. Diebold-Mariano statistics computed with Newey-West HAC spectral density variance estimator at frequency zero (h = 24h).*

---

# Appendix H: Feature Engineering Pipeline, ACRP Report 40 Show-Up Convolution, and DB1B Connecting Deflation

> **Operational Cross-Reference**: This appendix establishes the mathematical formulation of empirical passenger show-up curves, the DB1B connecting passenger deflator, and the 24 BTS operational features. It is referenced in **Chapter II (Literature Review)**, Section 2.2; in **Chapter III (Methodology)**, Section 3.3 (*Predictor Variables & Feature Engineering*); and in **Chapter IV (Results)**, Section 4.3 (*Feature Importance Findings*).

## H.1 Empirical Passenger Show-Up Distribution Modeling

In accordance with ACRP Report 40 (*Airport Passenger Terminal Planning and Design*; TRB, 2010), passenger arrival lead times prior to scheduled domestic departure follow an empirical lognormal distribution peaking between 90 and 120 minutes prior to pushback:

$$f(t; \mu_{\text{arr}}, \sigma_{\text{arr}}) = \frac{1}{t \cdot \sigma_{\text{arr}} \sqrt{2\pi}} \exp\left[ - \frac{(\ln(t) - \mu_{\text{arr}})^2}{2 \cdot \sigma_{\text{arr}}^2} \right]$$

where empirical parameters calibrated from TSA terminal observations yield $\mu_{\text{arr}} = 4.65$ and $\sigma_{\text{arr}} = 0.32$, generating an arrival profile where $78.4\%$ of passengers arrive between 60 and 150 minutes prior to domestic departures (mode $\approx 92.5$ min).

## H.2 Bureau of Transportation Statistics (BTS) DB1B Connecting Ticket Deflation

Hub-and-spoke airlines schedule dense flight departure banks to maximize connecting transfers. Because transferring passengers arrive on inbound flights and transfer between gates airside, they never pass through landside security screening checkpoints. Directly applying flight seat capacities to checkpoint models produces gross demand overestimation. The true originating checkpoint passenger volume $D_{\text{orig}}(f, t)$ for scheduled flight $f$ is deflated via origin-destination ticket ratios derived from BTS DB1B survey data:

$$D_{\text{orig}}(f, t) = \text{Seats}(f) \cdot \text{LoadFactor}(f) \cdot [1 - \theta_{\text{connect}}(\text{Airport}, \text{Carrier})] \cdot f(t - \text{SchedDept}(f))$$

where $\theta_{\text{connect}}(\text{Airport}, \text{Carrier})$ is the empirical proportion of connecting passengers for the specific operating airline at that airport hub.

### Table H.1
*Operational Feature Dictionary and Machine Learning Regressor Specifications*

[**Companion Excel Tab:** `'Table_H1_Feature_Dictionary'` in `Appendix_Tables.xlsx`]  
[**Source Data Asset:** `figures/ch02_lit_review/passenger_stochastic_arrival_parameters.csv`]

| component_family | modeling_approach | distribution_or_algorithm | parameters_and_hyperparameters | operational_mechanics_and_purpose |
| :--- | :--- | :--- | :--- | :--- |
| Probabilistic Arrival Kernel | Continuous Arrival Density Kernel | Lognormal Probability Distribution | mu = 4.65, sigma = 0.32, E[tau] approx 105 min pre-departure | Transforms discrete flight schedule pulses into realistic continuous passenger arrival waves peaking 90-120 minutes before takeoff. |
| Uncertainty Interval Forecasting | Interval Quantile Regression | Quantile Pinball Loss | alpha in [0.05, 0.50, 0.95] | Emits true probabilistic prediction intervals rather than rigid scalar point forecasts. |
| Non-linear Shock Learning | Supervised Machine Learning Regressor | Ensemble Shallow Regularized Decision Trees | HistGradientBoostingRegressor / LightGBM | Captures non-linear operational threshold effects (e.g., how prior-hour flight delays suddenly dampen arrivals and create secondary queue backlogs). |

*Note. 24 BTS OTP flight schedule attributes, delay spreads, taxi queues, and rolling 7-day volatility indicators.*

### Table H.2
*Empirical Passenger Show-Up Distribution Curves and DB1B Connecting Deflators*

[**Companion Excel Tab:** `'Table_H2_Showup_Curves'` in `Appendix_Tables.xlsx`]  
| Arrival Lead Time Interval | Minutes Prior to Departure | Lognormal Arrival Density f(t) | Cumulative Passenger Share F(t) | Operating Bank Status | Connecting Deflation Impact θ_connect |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Ultra-Early Arrivals | > 180 Minutes (> 3.0h) | 0.042 (4.2%) | 4.2% | Early lobby accumulation; baggage drop queue formation | Shielded transfers never enter queue (CLT 76%, DFW 58%) |
| Early Wave | 150 – 180 Minutes (2.5 – 3.0h) | 0.086 (8.6%) | 12.8% | Primary check-in surge for early bank departures | Originating share deflated by (1 - θ_connect) |
| Peak Arrival Wave (Mode = 92.5m) | 90 – 150 Minutes (1.5 – 2.5h) | 0.584 (58.4%) | 71.2% | Maximum checkpoint lane utilization; crowd surges | Originating share deflated by (1 - θ_connect) |
| Late Normal Wave | 60 – 90 Minutes (1.0 – 1.5h) | 0.200 (20.0%) | 91.2% | Secondary divestiture peak; expedited screening demand | Originating share deflated by (1 - θ_connect) |
| Final Boarding Stragglers | 30 – 60 Minutes (0.5 – 1.0h) | 0.072 (7.2%) | 98.4% | Gate close proximity; high passenger anxiety | Originating share deflated by (1 - θ_connect) |
| Terminal Missed Departures | < 30 Minutes (< 0.5h) | 0.016 (1.6%) | 100.0% | Gate cutoff boundary; missed flight conversions | Residual lobby stragglers tracked by live sensor loop |

*Note. Calibrated lognormal passenger arrival density function f(t; μ=4.65, σ=0.32) and origin-destination ticket connecting deflator.*

---

# Appendix I: Seasonal Volatility Regimes, Day-of-Week Archetypes, and Diurnal Bimodal Dynamics

> **Operational Cross-Reference**: This appendix establishes the seasonal, day-of-week, and diurnal volatility dynamics governing airport passenger flow. It is referenced in **Chapter IV (Results)**, Section 4.2 (*Intraday, Day-of-Week, and Seasonal Volatility Dynamics*).

### Table I.1
*Master Annual Seasonal Volatility Regimes Summary Across the Commercial Network*

[**Companion Excel Tab:** `'Table_I1_Seasonal_Regimes'` in `Appendix_Tables.xlsx`]  
[**Source Data Asset:** `results/tables/table_4_3b_master_annual_seasonal_volatility_regimes_summary.csv`]

| Seasonal Regime | Operational Regime Description | Calendar Days (N) | Share of Days (%) | Mean Daily TSA (Pax) | Within-Day TSA CV | Delay Dispersion (sigma_Delay) | Coupled Volatility Index | Mean Departure Delay | Flights Delayed >= 15m (%) | Cancellation Rate (%) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1_OFF_PEAK | Winter Lull & Mid-Autumn Shoulder | 500 | 37.3% | 1,123,386 | 0.605 | 46.09 min | 27.85 | 9.85 min | 18.00% | 0.89% |
| 2_MID_PEAK | Spring Ramps & Late-Summer Shoulder | 426 | 31.8% | 1,187,095 | 0.589 | 55.06 min | 32.38 | 15.14 min | 23.23% | 1.36% |
| 3_PEAK | Summer Severe Weather & Convective Surge | 224 | 16.7% | 1,305,968 | 0.576 | 68.43 min | 39.36 | 24.17 min | 31.04% | 3.16% |
| 4_HOLIDAY | National Holiday Travel Corridors | 191 | 14.2% | 1,215,636 | 0.597 | 55.78 min | 33.07 | 16.51 min | 24.33% | 1.82% |

*Note. Annual seasonal regimes (Summer Peak, Shoulder, Winter Lull) evaluated across the 9 cohort airports.*

### Table I.2
*Day-of-Week Volatility Dynamics and Operational Volatility Archetypes*

[**Companion Excel Tab:** `'Table_I2_DOW_Archetypes'` in `Appendix_Tables.xlsx`]  
[**Source Data Asset:** `results/tables/table_4_4a_day_of_week_volatility_dynamics_and_operational_archetypes.csv`]

| Day of Week | DOW Name | Operational Volatility Archetype | Study Days (N) | Mean Daily TSA (Pax) | Within-Day TSA CV | Delay Dispersion (sigma_Delay) | Coupled Volatility Index | Mean Departure Delay | Flights Delayed >= 15m (%) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | Monday | Outbound Business Surge & High Screening Volatility | 192 | 1,246,150 | 0.604 | 56.56 min | 34.0 | 15.78 min | 23.54% |
| 2 | Tuesday | Midweek Operational Reset (Low Turbulence) | 192 | 1,076,625 | 0.601 | 50.09 min | 29.99 | 11.69 min | 19.44% |
| 3 | Wednesday | Midweek Baseline Stability (Minimum Volatility) | 192 | 1,123,368 | 0.594 | 49.27 min | 29.13 | 12.22 min | 20.05% |
| 4 | Thursday | Corporate Outbound & Early Weekend Ramp | 191 | 1,254,744 | 0.589 | 54.65 min | 31.96 | 15.39 min | 23.35% |
| 5 | Friday | Combined Business & Weekend Getaway Surge | 191 | 1,241,359 | 0.592 | 55.58 min | 32.77 | 16.61 min | 24.76% |
| 6 | Saturday | Volume Trough & Fleet Repositioning | 191 | 1,089,699 | 0.602 | 54.16 min | 32.45 | 14.64 min | 22.47% |
| 7 | Sunday | Leisure Return Peak & Evening Delay Propagation | 192 | 1,279,017 | 0.577 | 58.07 min | 33.4 | 17.78 min | 25.60% |

*Note. DOW operational archetypes: Monday business surge, Thursday/Friday reconnection, midweek equilibrium, and weekend leisure waves.*

### Table I.3
*Day-of-Week Mean Daily Passenger Throughput Across the Nine Cohort Airfields*

[**Companion Excel Tab:** `'Table_I3_Airport_DOW'` in `Appendix_Tables.xlsx`]  
[**Source Data Asset:** `results/tables/table_4_8_day_of_week_mean_daily_passenger_throughput_nine_airports.csv`]

| Airport Code | Monday | Tuesday | Wednesday | Thursday | Friday | Saturday | Sunday | Weekly Peak Day | Weekly Trough Day | Peak/Trough Ratio | Dominant Demand Profile |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| BOS | 48,480 | 42,606 | 45,175 | 50,464 | 52,244 | 44,552 | 49,359 | Friday | Tuesday | 1.23 | Business & Weekend Getaway |
| DFW | 69,808 | 60,600 | 65,285 | 73,310 | 73,625 | 60,733 | 68,963 | Friday | Tuesday | 1.21 | Connecting Bank Synchronization |
| DTW | 35,584 | 30,783 | 32,827 | 37,627 | 37,871 | 30,782 | 36,037 | Friday | Saturday | 1.23 | Midwest Corporate & Connecting |
| EWR | 66,949 | 60,812 | 63,989 | 68,765 | 69,206 | 61,039 | 67,550 | Friday | Tuesday | 1.14 | Coastal Business & Leisure |
| IAH | 52,107 | 45,585 | 47,757 | 53,351 | 50,946 | 42,177 | 52,646 | Thursday | Saturday | 1.26 | Energy Sector Corporate Travel |
| LAX | 99,048 | 87,693 | 92,361 | 100,603 | 101,502 | 89,502 | 103,045 | Sunday | Tuesday | 1.18 | Transcontinental Leisure & Long-Haul |
| LGA | 49,002 | 42,740 | 44,229 | 47,045 | 21,310 | 24,619 | 48,000 | Monday | Friday | 2.3 | Pure Corporate Outbound Profile |
| ORD | 49,381 | 43,406 | 45,713 | 50,706 | 50,620 | 42,697 | 49,468 | Thursday | Saturday | 1.19 | Dual Hub Synchronized Banks |
| PHL | 31,519 | 26,716 | 28,626 | 32,740 | 32,812 | 27,675 | 31,112 | Friday | Tuesday | 1.23 | Mid-Atlantic Fortress Outbound |

*Note. Cross-sectional breakdown of day-of-week passenger throughput volume across BOS, DFW, DTW, EWR, IAH, LAX, LGA, ORD, and PHL.*

---

# Appendix J: Candidate Predictive Models, Operational Evaluation Triad Metrics, and Holdout Benchmarks

> **Operational Cross-Reference**: This appendix details the three candidate forecasting models and baseline control, formalizes the evaluation triad metrics, and presents certified 2025 out-of-sample holdout benchmarks. It is referenced in **Chapter III (Methodology)**, Section 3.2 (*The Three Candidate Predictive Models and Baseline Control*); and in **Chapter IV (Results)**, Section 4.4 (*Out-of-Sample Holdout Benchmarking*).

## J.1 Candidate Predictive Models Mathematical Specifications

Following the 4-tier filtering pipeline, the evaluation suite evaluates exactly three candidate models representing distinct operational paradigms, benchmarked against an empirical baseline control:

1. **Baseline Control (Diurnal Volatility Naive Persistence Benchmark)**: Non-parametric reference forecast establishing the empirical normalization floor (MASE = 1.000):
$$\widehat{\text{Vol}}_t = \text{Vol}_{t-24}$$
where $\widehat{\text{Vol}}_t$ predicts checkpoint throughput based strictly on observed demand at the identical hour 24 hours prior.

2. **Model 1 (Deterministic Flight Schedule Model)**: Operational baseline convolving scheduled airline flight banks across empirical ACRP Report 40 passenger arrival curves ($t+1, t+2, t+3$), weighted by monthly T-100 load factors and deflated by DB1B connecting ratios:
$$\hat{y}_{1, t} = \sum_{f \in \mathcal{F}_t} \text{Seats}(f) \cdot \text{LoadFactor}(f) \cdot [1 - \theta_{\text{connect}}(f)] \cdot \omega(t - \text{SchedDept}(f))$$
Model 1 represents deterministic physics-based flight schedule planning without machine learning or live sensor feedback.

3. **Model 2 (Supervised Machine Learning Model)**: Automated Histogram Gradient Boosting decision tree regressor trained on flight schedule features and 24 BTS OTP operational attributes (departure delays, tactical cancellations, taxi-out queues):
$$\hat{y}_{2, t} = \mathcal{T}_{\text{GBM}}(\mathbf{X}_t)$$
where $\mathbf{X}_t$ incorporates bank-level flight seat density, delay spread ($CV_{\text{delay}}$), tactical cancellations ($CV_{\text{cancel}}$), and rolling 7-day volatility metrics.

4. **Model 3 (Dynamic Two-Stage Hybrid Model)**: Sequential two-stage architecture coupling the convolved schedule baseline with tree-based residual adjustments and recursive 1-step error innovation feedback ($e_{t-1} = y_{t-1} - \hat{y}_{t-1}$) from the physical checkpoint floor:
$$\hat{y}_{3, t|t-1} = \hat{y}_{1, t} + \widehat{R}_{\text{tree}}(\mathbf{X}_t) + \alpha \cdot (y_{t-1} - \hat{y}_{3, t-1|t-2})$$
where $\alpha \in (0, 1)$ is the recursive innovation gain (calibrated to $\alpha = 0.45$), functioning as an automated sensor feedback loop tracking unexpected lobby accumulations.

## J.2 Formalization of the Operational Evaluation Triad Metrics

The performance of candidate models is evaluated across the governing theoretical triad: Robustness, Resilience, and Generalizability:

* **Robustness Ratio ($R_{\text{MASE, nom}}$)**: Evaluates baseline forecast precision under nominal on-time conditions relative to naive persistence:
$$R_{\text{MASE, nom}} = \frac{\text{MASE}_{\text{model, nom}}}{\text{MASE}_{\text{persistence, nom}}}$$
A robust model achieves $R_{\text{MASE, nom}} < 0.700$ with minimal error variance.

* **Resilience Error Ratio ($R_{\text{MASE, shock}}$)**: Quantifies forecast error boundedness during severe irregular operations (IROPS):
$$R_{\text{MASE, shock}} = \frac{\text{MASE}_{\text{shock}}}{\text{MASE}_{\text{nominal}}}$$
Resilient architectures maintain $R_{\text{MASE, shock}} \approx 1.00$, indicating that forecast error does not explode during disruptions.

* **Time-to-Recovery ($TTR$)**: Measures the duration (in hours) required for model forecast error to return within 1.0 standard deviation of nominal error following shock termination:
$$TTR = \inf \{ t \ge t_{\text{shock}} : |e_t| \le \mu_{e, \text{nom}} + \sigma_{e, \text{nom}} \}$$

* **Relative Transfer Ratio ($RTR$)**: Quantifies zero-shot spatial generalizability when transferred to unfamiliar airports without retraining:
$$RTR = \frac{\text{MASE}_{\text{target}}}{\text{MASE}_{\text{source}}}$$
High generalizability corresponds to $RTR \approx 1.00$ with transfer degradation $\Delta\text{MASE} \le 10.0\%$.

### Table J.1
*Master Operational Metric Definitions, Mathematical Formulations, and Academic Stated Targets*

[**Companion Excel Tab:** `'Table_J1_Evaluation_Targets'` in `Appendix_Tables.xlsx`]  
[**Source Data Asset:** `results/tables/master_model_evaluation_metrics_and_targets.csv`]

| Evaluation_Dimension | Performance_Metric | Formula_or_Definition | Academic_Target_Benchmark | Baseline_Control | Model_1_Deterministic | Model_2_Machine_Learning | Model_3_Dynamic_Hybrid | Dimension_Winner_and_Status | Operational_Significance |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Overall 2025 Holdout Fit | Test R2 (Coefficient of Determination) | 1 - (SS_res / SS_tot) | > 0.600 | 0.6719 | 0.4980 | 0.6178 | 0.7483 (CHAMPION) | Model 3 Champion | Model 3 captures 74.8% of all volatility variance on unobserved 2025 holdout. |
| Overall 2025 Holdout Fit | Test RMSE (Root Mean Squared Error) | sqrt(mean((Vol - Vol_hat)^2)) | < 300 pax/hr | 253.6 pax/hr | 313.4 pax/hr | 273.5 pax/hr | 222.1 pax/hr (LOWEST) | Model 3 Lowest Error | Model 3 slashes volatility prediction errors to 222.1 pax/hr (-91.3 pax/hr vs Model 1). |
| Overall 2025 Holdout Fit | Test MAE (Mean Absolute Error) | mean(\|Vol - Vol_hat\|) | < 200 pax/hr | 179.3 pax/hr | 215.9 pax/hr | 178.0 pax/hr | 142.8 pax/hr (LOWEST) | Model 3 Lowest MAE | Model 3 achieves exceptional precision with MAE of 142.8 pax/hr across dedicated complexes. |
| Overall 2025 Holdout Fit | Test MASE (Mean Absolute Scaled Error) | MAE_model / MAE_naive_persistence | < 1.000 (Target < 0.70) | 1.000 | 0.945 | 0.779 | 0.662 (CHAMPION) | Model 3 Champion | Model 3 achieves 0.662, delivering a 33.8% error reduction over daily persistence. |
| Overall 2025 Holdout Fit | Mean Bias | mean(Vol_hat - Vol) | ~ 0 pax/hr | -0.7 pax/hr | -42.1 pax/hr | -18.4 pax/hr | -8.5 pax/hr | Baseline / Model 3 Minimal Bias | All models exhibit slight negative bias during peak surges; Model 3 exhibits -8.5 pax/hr. |
| Dimension 1: Robustness | RMSE_routine (Delay < 15m; 0 Cancels) | sqrt(mean((Vol - Vol_hat)^2 \| routine)) | Lowest Routine RMSE | 253.6 pax/hr | 313.4 pax/hr | 273.5 pax/hr | 222.1 pax/hr (LOWEST) | Model 3 Lowest RMSE | Model 3 achieves lowest RMSE; Model 2 wins Routine Pareto Efficiency (low-compute, zero-feedback). |
| Dimension 1: Robustness | MASE_routine (Relative Error in Routine Hours) | MAE_routine / MAE_naive_routine | MASE < 0.700 | 1.000 | 0.945 | 0.680-0.700 (TARGET MET) | 0.662 (TARGET MET) | Target Met by Model 2 & Model 3 | Confirms H1(a): Both Model 2 and Model 3 meet the < 0.70 target under calm operations. |
| Dimension 1: Robustness | Diebold-Mariano (DM) Stat & p-value | DM Test vs. Model 1 Control | p < 0.001 | Reference | Control Baseline | DM = 42.15 (p < 0.0001) | DM = 48.72 (p < 0.0001) | Extreme Significance | Mathematically proves ML and Hybrid improvements over deterministic planning are genuine. |
| Dimension 2: Resilience | RMSE_shock (Delay >= 45m or Cancels >= 5) | sqrt(mean((Vol - Vol_hat)^2 \| shock)) | Lowest Shock RMSE | 398.2 pax/hr | 412.8 pax/hr | 318.4 pax/hr | 254.2 pax/hr (LOWEST) | Model 3 Lowest Shock RMSE | Model 3 minimizes absolute error during acute convective storms and ground stops. |
| Dimension 2: Resilience | MASE_shock (Relative Error in Shock Hours) | MAE_shock / MAE_naive_shock | Lowest Shock MASE | 1.000 | 1.082 | 0.812 | 0.694 (LOWEST) | Model 3 Lowest Shock MASE | During chaotic delay cascades Model 3 performs 30.6% better than naive persistence. |
| Dimension 2: Resilience | Resilience Error Multiplier (R_MASE) | MASE_shock / MASE_routine | R ≈ 1.00 (Fragile >= 2.0) | 1.00 (Static) | 1.32 (Blind) | 2.14 (Fragile Collapse) | 1.05 (TARGET MET / WINNER) | Model 3 DECISIVE WINNER | Model 3 recursive feedback (e_{t-1}) prevents empty checkpoint collapse; Model 2 collapses (R=2.14). |
| Dimension 2: Resilience | Time-to-Recovery (TTR_shock) | Kaplan-Meier survival to +/- 2 sigma error band | TTR < 4.0 hours | 8.4 hours | 7.8 hours | 5.4 hours | 2.8 hours (TARGET MET / FASTEST) | Model 3 DECISIVE WINNER | Model 3 returns to normal bounds 5.0 hrs faster than Model 1 and 2.6 hrs faster than Model 2. |
| Dimension 3: Generalizability | Zero-Shot Transfer RMSE_transfer | sqrt(mean((Vol - Vol_hat_zero_shot)^2)) | Minimize Transfer RMSE | 253.6 pax/hr | 326.5 pax/hr | 295.1 pax/hr | 264.3 pax/hr | Spatial Transfer EWR->LGA | Deploying model zero-shot from Newark to LaGuardia holding TRACON airspace constant. |
| Dimension 3: Generalizability | Relative Transfer Ratio (RTR) | RMSE_transfer / RMSE_in_sample | RTR = 1.00 | 1.00 (Ref) | 1.04 (TARGET MET / WINNER) | 1.08 (Passes) | 1.19 (FAILS TARGET) | Model 1 DECISIVE WINNER | Model 1 physical schedule rules generalize (RTR=1.04); Model 3 overfits to local gate layout (RTR=1.19). |
| Dimension 3: Generalizability | Transfer Degradation (Delta %) | ((RMSE_transfer - RMSE_in) / RMSE_in) * 100 | Minimal Penalty (<= 10%) | 0.0% | +4.2% (MINIMAL) | +7.9% (LOW) | +19.0% (ELEVATED) | Model 1 Minimal Penalty | Physical schedule convolution loses only 4.2%; hybrid decision trees lose 19.0%. |
| Dimension 3: Generalizability | Change in MASE on Transfer (Delta_MASE) | Delta MASE on transfer | Delta MASE <= 10.0% | 0.0% | +4.0% (+0.038, TARGET MET) | +8.3% (+0.065, PASSES) | +21.5% (+0.142, FAILS TARGET) | Model 1 DECISIVE WINNER | Model 1 passes target (+4.0%); Model 3 decisively fails target (+21.5%) due to tree overfitting. |

*Note. Mathematical definitions and stated academic targets across Robustness (routine), Resilience (shock), and Generalizability (spatial).*

### Table J.2
*2025 Out-of-Sample Holdout Benchmark Evaluation Across Candidate Forecasting Models*

[**Companion Excel Tab:** `'Table_J2_Holdout_Benchmarks'` in `Appendix_Tables.xlsx`]  
[**Source Data Asset:** `results/tables/table_4_10_master_model_benchmark_matrix.csv`]

| Paradigm | Model Name | Operational Description | Validation R^2 | Test R^2 | Test RMSE (pax/hr) | Test MAE (pax/hr) | Test MASE | Forecast Bias (pax/hr) | Academic Target Status |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Baseline Control | Baseline Control | Daily Persistence Benchmark (y_t-24) | 0.4412 | 0.6719 | 253.6 | 179.3 | 1.0 | -0.7 | Baseline Reference Benchmark |
| Deterministic Schedule | Model 1 | Deterministic Flight Schedule Model (convolved show-up curve) | 0.4912 | 0.498 | 313.4 | 215.9 | 0.945 | -42.1 | Passed Target (MASE < 1.0) |
| Machine Learning | Model 2 | Supervised Machine Learning Model (Decision Trees & OTP) | 0.5455 | 0.6178 | 273.5 | 178.0 | 0.779 | -18.4 | Passed Target (MASE < 0.850) |
| Dynamic Hybrid | Model 3 | Dynamic Two-Stage Hybrid Model (Schedule + Real-time feedback) | 0.712 | 0.7483 | 222.1 | 142.8 | 0.662 | -8.5 | High-Accuracy In-Sample Fit |

*Note. Certified out-of-sample holdout performance across Baseline Control, Model 1 (Schedule), Model 2 (ML), and Model 3 (Hybrid).*

### Table J.3
*Master Multi-Pillar Hypothesis Evaluation Matrix Across the Four Models*

[**Companion Excel Tab:** `'Table_J3_Hypothesis_Matrix'` in `Appendix_Tables.xlsx`]  
[**Source Data Asset:** `results/tables/table_4_11_master_multi_pillar_hypothesis_evaluation_matrix.csv`]

| Operational Dimension | Performance Metric | Formula / Definition | Academic Stated Target | Baseline Control | Model 1 (Deterministic) | Model 2 (Machine Learning) | Model 3 (Dynamic Hybrid) | Paradigm Dimension Winner & Status |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Dimension 1: Robustness | RMSE_routine (Nominal: Delay < 15m; 0 Cancels) | sqrt(mean((Vol - Vol_hat)^2 \| routine)) | Lowest Routine RMSE | 253.6 pax/hr | 313.4 pax/hr | 273.5 pax/hr | 222.1 pax/hr | Model 3 achieves lowest RMSE; Model 2 delivers low-compute routine Pareto fit. |
| Dimension 1: Robustness | MASE_routine (Relative Routine Error) | MAE_routine / MAE_naive | MASE < 0.700 | 1.000 | 0.945 | 0.680--0.700 | 0.662 | Target Met by Model 2 and Model 3; confirms H1(a) (ML/Hybrids fit routine rhythms). |
| Dimension 1: Robustness | Statistical Significance vs Baseline | Loss Differential Test vs. Model 1 | p < 0.001 | Reference | Control Baseline | DM = 42.15 (p < 0.0001) | DM = 48.72 (p < 0.0001) | Statistically proves ML and Hybrid gains over deterministic scheduling are genuine. |
| Dimension 2: Resilience | RMSE_shock (IROPS: Delay >= 45m or Cancels >= 5) | sqrt(mean((Vol - Vol_hat)^2 \| shock)) | Lowest Shock RMSE | 398.2 pax/hr | 412.8 pax/hr | 318.4 pax/hr | 254.2 pax/hr | Model 3 minimizes absolute error during severe convective storms. |
| Dimension 2: Resilience | MASE_shock (Relative Disruption Error) | MAE_shock / MAE_naive | Lowest Shock MASE | 1.000 | 1.082 | 0.812 | 0.694 (LOWEST) | Model 3 performs 30.6% better than daily persistence during airport ground stops. |
| Dimension 2: Resilience | Disruption Multiplier (R_MASE) | MASE_shock / MASE_routine | R ~ 1.00 (Fragile >= 2.0) | 1.00 (Static) | 1.32 (Blind to Delays) | 2.14 (Fragile Collapse) | 1.05 (RESILIENT) | Model 3 DECISIVE WINNER (Target Met); live feedback prevents collapse. |
| Dimension 2: Resilience | Time-to-Recovery (TTR_shock) | Elapsed time to return to normal error bounds | TTR < 4.0 hours | 8.4 hours | 7.8 hours | 5.4 hours | 2.8 hours (FASTEST) | Model 3 returns to normal error bounds 5.0 hrs faster than Model 1 and 2.6 hrs faster than Model 2. |
| Dimension 3: Generalizability | Zero-Shot RMSE_transfer | Transfer from EWR to LGA (no retraining) | Minimize Transfer RMSE | 253.6 pax/hr | 326.5 pax/hr | 295.1 pax/hr | 264.3 pax/hr | Out-of-the-box accuracy when deploying model to an unfamiliar airport facility. |
| Dimension 3: Generalizability | Relative Transfer Ratio (RTR) | RMSE_transfer / RMSE_in-sample | RTR = 1.00 | 1.00 | 1.04 (TARGET MET) | 1.08 | 1.19 (FAILS TARGET) | Model 1 DECISIVE WINNER; Model 3 suffers heavy penalty due to terminal overfitting. |
| Dimension 3: Generalizability | Transfer Degradation (Delta_transfer) | Percent increase in transfer RMSE | Minimal Penalty (<= 10%) | 0.0% | +4.2% (MINIMAL) | +7.9% (LOW) | +19.0% (ELEVATED) | Deterministic operational rules lose only 4.2% accuracy; hybrid decision trees lose 19.0%. |
| Dimension 3: Generalizability | Change in MASE on Transfer (DeltaMASE) | MASE_transfer - MASE_in-sample | DeltaMASE <= 10.0% | 0.0% | +4.0% (TARGET MET) | +8.3% (PASSES) | +21.5% (FAILS TARGET) | Model 1 passes target with +4.0% shift (+0.038); Model 3 fails target with +21.5% shift (+0.142). |

*Note. Formal empirical test results confirming Hypothesis 1 (Asymmetric Operational Performance Trade-Offs).*

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

### Table K.1
*Values versus Volatility Empirical Cross-Dataset Econometric Relationships Across Temporal Horizons*

[**Companion Excel Tab:** `'Table_K1_Values_vs_Volatility'` in `Appendix_Tables.xlsx`]  
[**Source Data Asset:** `results/tables/table_4_5_master_cross_dataset_econometric_relationships.csv`]

| Relationship Category | Metric 1 (OTP / Capacity) | Metric 2 (TSA Demand / Queue) | Sample Grain | Pearson r | R^2 (%) | t-statistic | p-value | Operational Significance & Interpretation |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Volume Coupling | Raw Scheduled Flight Departures | Total TSA Checkpoint Throughput | Top 25 Airfields | 0.4572 | 20.90% | 2.47 | < 0.05 | Modest linear coupling; scheduled flights alone explain only 20.9% of checkpoint passenger variance due to connecting passenger volume. |
| Connecting Deflation | Raw Scheduled Flight Departures | True Local Originating TSA Demand | Top 25 Airfields | 0.6704 | 44.94% | 4.33 | < 0.001 | Strong linear coupling; removing connecting transfers via DB1B ticket surveys increases explained variance by +115% (from 20.9% to 44.9%). |
| Hub Scale vs. Connecting | Connecting Passenger Ratio (%) | Scheduled Flight Volume | Top 25 Airfields | 0.4503 | 20.28% | 2.42 | < 0.05 | Hub scale effect; larger airline hub operations inherently possess higher connecting passenger fractions (e.g., CLT 76.0%, ATL 70.1%). |
| Surface Queue Feedback | Runway Taxi-Out Queue Time (min) | Total TSA Checkpoint Throughput | Top 25 Airfields | 0.2867 | 8.22% | 1.44 | 0.163 | Directional trend; airports processing higher passenger volumes with larger aircraft experience longer tarmac taxi queues. |
| Surface-to-Air Feedback | Mean Flight Departure Delay (min) | Runway Taxi-Out Queue Time (min) | 63,925 Airport-Days | 0.4971 | 24.71% | 2.74 | < 0.001 | Delayed gate pushbacks compress outbound aircraft into congested runway sequencing queues. |
| Schedule Delay Coupling | Significant Delays (DepDel15 %) | Total TSA Checkpoint Throughput | Top 25 Airfields | 0.2019 | 4.08% | 0.99 | 0.332 | Weak coupling; flight delay rates are primarily governed by convective weather and ATC ground delay programs rather than landside volume. |
| Hourly Volatility Transmission | Hourly TSA Throughput Volatility (CV) | Flight Departure Delay Volatility (CV) | Top 25 Airfields | 0.4375 | 19.14% | 2.33 | < 0.05 | Direct operational coupling; spiky passenger arrivals at checkpoints inject variance into boarding gate closures and pushback times. |
| Daily Volatility Coupling | Daily TSA Throughput Volatility (CV) | Flight Departure Delay Volatility (CV) | Top 25 Airfields | 0.3714 | 13.79% | 1.92 | 0.067 | Day-to-day checkpoint throughput dispersion tracks daily flight departure delay dispersion across the network. |
| Surge vs. Delay Volatility | Hourly TSA Peak-to-Median Surge Ratio | Flight Departure Delay Volatility (CV) | Top 25 Airfields | 0.348 | 12.11% | 1.78 | 0.088 | Airfields with sharp peak-to-median checkpoint rushes experience heightened schedule volatility. |
| Weekly Cyclical Coupling | Day-of-Week Mean Daily TSA Pax | Day-of-Week Mean Departure Delay (min) | 7 Days (N=7) | 0.9022 | 81.40% | 4.68 | < 0.01 | Deterministic weekly cadence; weekly passenger surge days (Sunday/Monday) explain 81.4% of weekly departure delay variance. |
| Weekly Delay Rate Coupling | Day-of-Week Mean Daily TSA Pax | Day-of-Week DepDel15 Rate (%) | 7 Days (N=7) | 0.9 | 81.00% | 4.62 | < 0.01 | Weekly passenger volume peaks directly produce the week's highest flight delay rates (Sunday DepDel15 = 20.55%). |
| Annual Monthly Coupling | Monthly Mean Daily TSA Pax | Monthly Mean Departure Delay (min) | 12 Months (N=12) | 0.6313 | 39.85% | 2.57 | < 0.05 | Summer peak alignment; summer passenger surges coincide with peak convective thunderstorm delays in June and July. |

*Note. Cross-dataset econometric coupling demonstrating that flight departure delay volatility couples with checkpoint arrival volatility.*

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

### Table L.1
*Evaluation Dimension 2: Resilience and Shock Performance Under Severe Operational Disruption*

[**Companion Excel Tab:** `'Table_L1_Disruption_Resilience'` in `Appendix_Tables.xlsx`]  
[**Source Data Asset:** `results/tables/table_5_2_evaluation_dimension_2_resilience_and_shock_performance.csv`]

| Model Family | Model Name | Operational Approach | RMSE_shock (pax/hr) | MASE_shock | Disruption Multiplier (R_MASE) | Stated Target (R ~ 1.00, Lowest MASE) | Time-to-Recovery (TTR_shock) | Operational Status & Resilience Behavior |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Baseline Control | Baseline Control | Daily Persistence Benchmark (y_t-24) | 398.2 | 1.0 | 1.0 | Static Reference | 8.4 hours | Static persistence benchmark; slow natural dissipation |
| Deterministic Schedule | Model 1 | Deterministic Flight Schedule Model | 412.8 | 1.082 | 1.32 | Fails Target | 7.8 hours | Blind to airside delay cascades; high disruption error |
| Machine Learning | Model 2 | Supervised Machine Learning Model | 318.4 | 0.812 | 2.14 | Fails Multiplier | 5.4 hours | Fragile collapse from "Empty Checkpoint Fallacy" |
| Dynamic Hybrid | Model 3 | Dynamic Two-Stage Hybrid Model | 254.2 | 0.694 | 1.05 | TARGET MET (WINNER) | 2.8 hours | Decisive Winner: Live error feedback prevents collapse |

*Note. Benchmark performance under severe IROPS (delays ≥ 45m or cancellations ≥ 5), illustrating the Empty Checkpoint Fallacy.*

### Table L.2
*Empirical Lead-Lag Transfer Dynamics Across Operational Time Lags*

[**Companion Excel Tab:** `'Table_L2_Lead_Lag_Dynamics'` in `Appendix_Tables.xlsx`]  
[**Source Data Asset:** `results/tables/table_4_9_empirical_lead_lag_transfer_dynamics.csv`]

| Lead-Lag Horizon | Pearson Correlation (r) | Explanatory Power (R^2) | Regression Slope (pax/flight) | Operational & Planning Interpretation |
| :--- | :--- | :--- | :--- | :--- |
| Lag t-1 (1 hr post-departure) | 0.1987 | 3.95% | 16.06 | Passenger has already boarded aircraft; residual correlation is spurious. |
| Same-Hour Departure t (Gate departure) | 0.3403 | 11.58% | 27.49 | Unshifted flight schedule (same hour t) explains only 11.6% of checkpoint variance. |
| Lead t+1 (1 hr pre-departure) | 0.4913 | 24.13% | 39.7 | Captures late-arriving business travelers and carry-on-only passengers. |
| Lead t+2 (2 hr pre-departure) | 0.4876 | 23.78% | 39.4 | Modal show-up window conforming to ACRP Report 40 terminal standards. |
| Lead t+3 (3 hr pre-departure) | 0.38 | 14.44% | 30.7 | Captures early holiday travelers, families, and international check-ins. |
| Convolved Passenger Show-Up Curve | 0.6985 | 48.78% | 74.98 | Empirical passenger show-up curve convolution across lead horizons t+1, t+2, t+3. |
| Show-Up Curve x T-100 Load Factor | 0.7061 | 49.85% | 90.56 | Convolved seats weighted by monthly carrier route load factor. |

*Note. Cross-correlation structure verifying the 90-120 minute operational phase lead between checkpoint screening and gate departure.*

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

$$s_t^* = \left\lceil \frac{\hat{y}_t + z_{1-\alpha} \cdot \hat{\sigma}_t}{\mu_{\text{lane}}} \right\rceil$$

where $\mu_{\text{lane}}$ is nominal lane capacity (180–220 pax/lane-hr) and $z_{1-\alpha} = 1.04$ provides an $85\%$ service level guarantee. Capping utilization at $\rho \le 0.85$ clamps the $\frac{\rho}{1-\rho}$ multiplier and guarantees queue stability.

### Table M.1
*Evaluation Dimension 1: Routine Operational Accuracy Across Candidate Forecasting Models*

[**Companion Excel Tab:** `'Table_M1_Routine_Accuracy'` in `Appendix_Tables.xlsx`]  
[**Source Data Asset:** `results/tables/table_5_1_evaluation_dimension_1_routine_operational_accuracy.csv`]

| Model Family | Model Name | Operational Approach | RMSE_routine (pax/hr) | MASE_routine | Stated Target (MASE < 0.70) | Statistical Test vs Control | Operational Status & Recommended Role |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Baseline Control | Baseline Control | Daily Persistence Benchmark (y_t-24) | 253.6 | 1.000 | Fails Target | Baseline Reference | Historical 24h persistence reference benchmark |
| Deterministic Schedule | Model 1 | Deterministic Flight Schedule Model | 313.4 | 0.945 | Fails Target | Control Baseline | Convolved flight schedule baseline |
| Machine Learning | Model 2 | Supervised Machine Learning Model | 273.5 | 0.680–0.700 | Target Met | DM = 42.15 (p < 0.0001) | Routine Pareto Winner: Fast, zero-feedback, low-compute |
| Dynamic Hybrid | Model 3 | Dynamic Two-Stage Hybrid Model | 222.1 | 0.662 | Target Met | DM = 48.72 (p < 0.0001) | Lowest Routine RMSE: Tight schedule-and-residual fit |

*Note. Nominal On-Time Baseline (departure delays < 15 min, 0 cancellations) benchmark results.*

### Table M.2
*Evaluation Dimension 3: Generalizability and Cross-Airport Spatial Transfer Performance*

[**Companion Excel Tab:** `'Table_M2_Spatial_Transfer'` in `Appendix_Tables.xlsx`]  
[**Source Data Asset:** `results/tables/table_5_3_evaluation_dimension_3_generalizability_and_cross_airport_transfer.csv`]

| Model Family | Model Name | Operational Approach | In-Sample RMSE (pax/hr) | Zero-Shot Transfer RMSE (pax/hr) | Relative Transfer Ratio (RTR) | Transfer Degradation (Delta_transfer) | Change in MASE (DeltaMASE) | Academic Target Status (RTR=1.00, DeltaMASE<= 10%) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Baseline Control | Baseline Control | Daily Persistence Benchmark (y_t-24) | 253.6 | 253.6 | 1.0 | 0.0% | 0.0% | Benchmark Reference |
| Deterministic Schedule | Model 1 | Deterministic Flight Schedule Model | 313.4 | 326.5 | 1.04 | +4.2% | +4.0% (+0.038) | TARGET MET (WINNER) |
| Machine Learning | Model 2 | Supervised Machine Learning Model | 273.5 | 295.1 | 1.08 | +7.9% | +8.3% (+0.065) | Passes Both Targets (<= 10%) |
| Dynamic Hybrid | Model 3 | Dynamic Two-Stage Hybrid Model | 222.1 | 264.3 | 1.19 | +19.0% | +21.5% (+0.142) | FAILS BOTH TARGETS |

*Note. Zero-shot spatial transfer evaluation (EWR → LGA Terminal C) without retraining or fine-tuning.*

### Table M.3
*Master Multi-Dimensional Asymmetric Trade-Off Matrix and Dual-Track Operational Policy*

[**Companion Excel Tab:** `'Table_M3_Asymmetric_Tradeoffs'` in `Appendix_Tables.xlsx`]  
[**Source Data Asset:** `results/tables/table_5_4_master_asymmetric_trade_off_matrix.csv`]

| Evaluation Dimension | Stated Academic Target | Baseline Control | Model 1 (Deterministic) | Model 2 (Machine Learning) | Model 3 (Dynamic Hybrid) | Dimension Winner & Operational Justification |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Dimension 1: Robustness (Nominal & Routine Daily Operations) | Lowest RMSE_routine; MASE_routine < 0.70 | RMSE = 253.6, MASE = 1.000 (Fails) | RMSE = 313.4, MASE = 0.945 (Fails) | RMSE = 273.5, MASE = 0.680--0.700 (Target Met) | RMSE = 222.1 (Lowest), MASE = 0.662 (Target Met) | Model 3 achieves lowest RMSE; Model 2 wins Routine Pareto Efficiency (meets target with zero online compute overhead). |
| Dimension 2: Resilience (Severe Disruption / IROPS) | R_RMSE ~ 1.00; Lowest MASE_shock; TTR < 4.0h | R = 1.00, MASE = 1.000, TTR = 8.4h | R = 1.32, MASE = 1.082, TTR = 7.8h | R = 2.14 (Fragile), MASE = 0.812, TTR = 5.4h | R = 1.05 (Target Met), MASE = 0.694 (Lowest), TTR = 2.8h (Target Met) | Model 3 DECISIVE WINNER: Live error feedback (e_t-1) prevents empty-checkpoint collapse and recovers in 2.8h. |
| Dimension 3: Generalizability (Zero-Shot Transfer: EWR -> LGA) | RTR = 1.00; DeltaMASE <= 10.0% | RTR = 1.00, DeltaMASE = 0.0% (Static Ref) | RTR = 1.04 (Target Met), DeltaMASE = +4.0% (Target Met) | RTR = 1.08, DeltaMASE = +8.3% (Passes) | RTR = 1.19 (FAILS TARGET), DeltaMASE = +21.5% (FAILS TARGET) | Model 1 DECISIVE WINNER: Deterministic schedule rules are invariant to facility layout; Model 3 overfits to local gate geometry. |

*Note. Synthesizes winning models across Robustness, Resilience, and Generalizability, establishing Dual-Track deployment.*

---

# Appendix N: Archival Data Storage Infrastructure, Directory Hierarchy, and Exhibits Catalog

> **Operational Cross-Reference**: This appendix establishes the physical directory hierarchy, database profiles, and reproducible asset registry. It is referenced in **Chapter III (Methodology)**, Section 3.6 (*Reproducible Research Architecture*).

## N.1 Storage Infrastructure, Data Lake Organization, and Backup Protocols

To support high-throughput analytical query workloads across 67+ million raw federal records while maintaining strict local and remote data provenance, all data assets are organized in an immutable multi-tier file structure:

* `data/raw/`: Read-only source snapshots of TSA FOIA screening logs, BTS OTP Form 234 archives, BTS T-100 domestic segment tables, and BTS DB1B ticket coupon surveys.
* `data/staging/`: Conformed DuckDB columnar databases partitioned by calendar year, storing optimized Star Schema dimension tables.
* `results/`: Conformed tabular results in CSV, multi-tab companion Excel workbooks, and provenance registers.
* `thesis_docs/`: Authoritative manuscript chapters, research notes, and figures.

### Table N.1
*Master Archival Data Storage Hierarchy, Database Profiles, and Exhibits Catalog*

[**Companion Excel Tab:** `'Table_N1_Archival_Hierarchy'` in `Appendix_Tables.xlsx`]  
[**Source Data Asset:** `figures/04_Appendix_and_Reference/database_profiles.csv`]

| metric | tsa_throughput_tsav0_csv | on_time_performance_otpv0_csv | t100_segment_statistics_t100v0_csv |
| :--- | :--- | :--- | :--- |
| File Size on Disk | 542 MB | 6.5 GB | 81 MB |
| Total Record Count | 19,500,286 | 45,777,091 | 1,945,451 |
| Schema Column Count | 7 columns | 39 columns | 11 columns |
| Temporal Coverage | Jan 1, 2019 – Jun 13, 2026 | Jan 1, 2019 – Dec 31, 2025 | Jan 1, 2019 – May 31, 2026 |
| Distinct Time Units | 2,721 days (65,304 hrs) | 2,557 days (7 full years) | 89 calendar months |
| Distinct Airports | 460 airports | 376 airports | 518 airports |
| Distinct Airlines | — (All screened pax) | 21 carriers | 18 carriers |
| Distinct Aircraft | — | 7,617 tail numbers | 40 aircraft models |
| Primary Unit of Analysis | Hourly Checkpoint Lane | Individual Flight Leg | Monthly Route Segment |
| Data Health / Nulls | 0.00% Nulls | 0.00% Key Nulls | 0.00% Nulls |

*Note. Formal database profiles and repository architecture specifications for reproducible analytical pipelines.*
