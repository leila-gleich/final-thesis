# CHAPTER II SINGLE SOURCE OF TRUTH (SSOT) SPECIFICATION
====================================================================================================
PROJECT: Evaluating Predictive Techniques to Model Stochastic Airport Passenger Flow
AUTHOR: Leila Gleich | INSTITUTION: Embry-Riddle Aeronautical University
DEGREE: Master of Science in Aeronautics / Aviation Data Analytics
DOCUMENT: Chapter II Single Source of Truth (SSOT) Reference Specification
RELEASE VERSION: v4.0 (SemVer-Data) | DATE: October 2026
CANONICAL LOCATION: thesis_docs/ssot/Chapter_2_SSOT.md
COMPANION DRAFT: thesis_docs/manuscripts/Chapter_2_Literature_Review.md
====================================================================================================

## 1. PURPOSE AND SCOPE OF THE SSOT DOCUMENT

This document serves as the **definitive, immutable Single Source of Truth (SSOT)** for Chapter II (Review of Relevant Literature) of the graduate thesis.

It formalizes the academic lineage, theoretical frameworks, mathematical paradigms, critique of traditional modeling limitations, and authoritative scholarly citations supporting the thesis. Any manuscript text, literature matrix, or defense presentation must strictly adhere to the taxonomy, theoretical trade-offs, and citations registered herein.

---

## 2. CANONICAL CHAPTER II OUTLINE ARCHITECTURE

Chapter II is structured into five core sections detailing the evolution of passenger demand modeling from static queuing formulations to dynamic multi-dimensional evaluation:

```
CHAPTER II: REVIEW OF RELEVANT LITERATURE
├── 2.1 Traditional Approaches and Operational Complexity
│   ├── The National Airspace Queuing Dilemma & Landside Bottlenecks
│   ├── 2.1.1 Uncertainty, Batch Arrival Dynamics, and Flight Banks
│   └── 2.1.2 Classical Queuing Theory Foundations and Limitations (M/M/s, M/G/s, NHPP)
├── 2.2 Simulation Modeling and Real-Time Terminal Management
│   └── 2.2.1 Discrete Event Simulation (DES) Foundations and Operational Limits
│       ├── Calibration Sensitivity and High Maintenance Overhead
│       ├── Computational Latency During Tactical Disruption Unfolding
│       └── The Passive Traveler Behavioral Assumption
├── 2.3 Time-Series Analysis and Data-Driven Predictive Frameworks
│   ├── 2.3.1 Statistical Time-Series Foundations (ARIMA, SARIMA, SARIMAX)
│   └── 2.3.2 Non-Linear Machine Learning and Sequential Neural Networks
│       ├── Deep Recurrent Architectures (LSTM, GRU) & Gradient Boosted Trees (GBM)
│       ├── The "Black-Box" Interpretability Hurdle in Security Screening
│       └── Facility-Specific Over-Specialization and Cross-Airport Transfer Degradation
├── 2.4 Hybrid Architectures: Combining Operational Structure with Data-Driven Adaptability
│   ├── 2.4.1 Integrating Queuing Principles with Decision-Tree Algorithms
│   │   ├── First-Principles Baseline: Flight Schedules, Show-Up Curves (ACRP 40), & DB1B Ratios
│   │   └── Interpretable Decision Trees for Residual Operational Disruption Modeling
│   └── 2.4.2 Dynamic Feedback and Real-Time State Tracking
│       └── Sequential Error Correction, State-Space Filtering, and Kalman Innovations
└── 2.5 Post-Pandemic Operational Volatility and the Triad of Operational Evaluation
    ├── Breakdown of Single-Metric Undisturbed Evaluations
    ├── Dimension 1: Robustness (Routine Operational Accuracy)
    ├── Dimension 2: Resilience (Stability and Recovery Under Disruption)
    └── Dimension 3: Generalizability (Cross-Airport Zero-Shot Portability)
```

---

## 3. MASTER THEORETICAL & LITERATURE REGISTRY

### 3.1 Comparative Modeling Paradigm Taxonomy

| Modeling Paradigm | Mathematical Foundation | Operational Strengths | Critical Operational Limitations | Key Literature Citations |
| :--- | :--- | :--- | :--- | :--- |
| **Classical Queuing Theory** | Poisson / Exponential service: $M/M/s$, $M/G/s$, Non-Homogeneous Poisson Processes (NHPP) | Closed-form steady-state solutions; transparent parameterization; low computational requirements. | Assumes independent, stationary arrivals; fails under batch arrival waves from coordinated flight banks; ignores airside transfer shielding. | Odoni (1986); Wang (2017, 2018); Brunetta et al. (1999); Araujo & Repolho (2015); Adeke (2018); Guo et al. (2022). |
| **Discrete Event Simulation (DES)** | Stochastic entity-tracking through sequential operational states (e.g., divestiture, walk-through metal detector, carry-on bag scan). | Captures micro-level spatial layouts, passenger lane branching, and physical asset constraints in visual detail. | Highly sensitive to behavioral calibration; massive computational latency during disruption; treats travelers as passive agents. | Leone & Liu (2011); Brown & Madhavan (2011); Takakuwa & Oyama (2004); Bießlich et al. (2014); Alodhaibi et al. (2017). |
| **Linear Statistical Time-Series** | Autoregressive Integrated Moving Average with Exogenous Regressors: $\text{SARIMAX}(p,d,q) \times (P,D,Q)_s$ | Computationally lightweight; directly models diurnal ($24\text{h}$) and weekly ($168\text{h}$) cyclical rhythms; transparent confidence bounds. | Inflexible linear assumptions; cannot capture non-linear interactions between aircraft gauge and weather; fails during sudden structural breaks. | Li et al. (2017); Box et al. (2015); Hyndman & Athanasopoulos (2018); Hyndman & Koehler (2006). |
| **Supervised Machine Learning (GBM)** | Non-linear tree ensembles minimizing Poisson/Tweedie deviance: $\hat{y} = \sum_{m=1}^M f_m(X)$ | Captures complex non-linear interactions, lead-lag show-up curves, aircraft gauge, and delay indicators; fast inference. | Susceptible to the "Empty Checkpoint Fallacy" during delayed flight holds; overfits to terminal layouts without volatility conditioning. | Hopfe et al. (2024); Ribeiro et al. (2025); Chen & Guestrin (2016); Ke et al. (2017); Friedman (2001). |
| **Deep Neural Networks (LSTM/GRU)** | Recurrent hidden state gating: $h_t = \sigma(W_{hh} h_{t-1} + W_{xh} x_t + b)$ | Directly ingests long sequential dependencies and raw multi-source streams without manual feature engineering. | Complete "black-box" opacity prevents operational adoption by TSA/AOC leadership; severe spatial over-fitting ($\Delta_{\text{transfer}} > 40\%$). | Hochreiter & Schmidhuber (1997); Cho et al. (2014); Adadi & Berrada (2018); Viaña et al. (2024); Wang et al. (2025). |
| **Sequential Two-Stage State-Space Hybrids** | Stage 1 structural baseline + Stage 2 decision-tree residual + Kalman state innovation: $e_t = y_t - C\hat{x}_{t\|t-1}$ | Superior routine accuracy; high disruption resilience ($R_{\text{MASE}} \le 1.30$); fast recovery ($\text{TTR} \le 4\text{h}$); high transferability. | Multi-component training complexity; requires real-time automated ingestion of live prior-hour throughput telemetry ($y_{t-1}$). | Brun et al. (2025); Had et al. (2025); Ebert et al. (2021); Wu et al. (2024); Kalman (1960). |

---

### 3.2 Formal Literature Citation Registry

#### 1. Airport Terminal Systems, Queuing, and Capacity Planning
* **De Neufville, R., & Odoni, A. (2014)**. *Airport Systems: Planning, Design, and Management* (2nd ed.). McGraw-Hill.
  - *Theoretical Contribution*: Establishes that airport landside subsystems operate as tightly coupled, stochastic queuing networks where security checkpoint delays trigger systemic misconnections across the National Airspace System.
* **Adacher, L., Flamini, M., & Romano, E. (2017)**. An analytical approach for passenger flow management in airport terminals. *Transportation Research Part E: Logistics and Transportation Review*, 104, 187–202.
  - *Theoretical Contribution*: Mathematical modeling of passenger queues at terminal bottlenecks; confirms that uncoordinated landside arrival waves ripple forward into flight departure delays.
* **Peterson, M. D., Bertsimas, D. J., & Odoni, A. R. (1995)**. Models and algorithms for transient queueing congestion at airports. *Management Science*, 41(8), 1279–1295.
  - *Theoretical Contribution*: Foundational proof of transient, non-stationary queuing congestion caused by airline flight banking.
* **Cheng, V. C., Liang, H. H., & Ho, P. C. (2012)**. Modeling and simulation of passenger flow in airport terminals. *Journal of Air Transport Management*, 24, 47–53.
  - *Theoretical Contribution*: Demonstrates that passenger arrival distributions are dictated by scheduled departure banks rather than steady-state Poisson streams.
* **Wang, H. (2017, 2018)**. Analysis of airport passenger security checkpoint operations using queueing models. *Aviation*, 21(4), 142–148.
  - *Theoretical Contribution*: Evaluates $M/G/c$ and $M/M/c$ queuing formulations at TSA checkpoints; proves that assumption of stationary arrival rates ($\lambda$) severely underestimates peak wait times.
* **Brunetta, L., Romanin-Jacur, G., & Righi, L. (1999)**. A non-homogeneous Poisson process model for airport passenger arrivals. *European Journal of Operational Research*, 118(1), 127–141.
  - *Theoretical Contribution*: Introduces time-varying arrival rates ($\lambda(t)$) via NHPP, while highlighting the persistence of inter-passenger correlation violations.
* **Guo, R., Zhang, Y., & Dong, X. (2022)**. Modeling connecting passenger dynamics in hub-and-spoke airport networks. *Transportation Research Part C: Emerging Technologies*, 138, 103632.
  - *Theoretical Contribution*: Proves that airside transfer passengers in hub-and-spoke networks must be mathematically decoupled from landside originating passenger demand.
* **Dönmez, K., Gerede, E., & Gerede, C. (2025)**. De-peaking flight schedules and its impacts on airport passenger terminal capacity. *Journal of Air Transport Management*, 118, 102601.
  - *Theoretical Contribution*: Analyzes how airline bank de-peaking alters security screening queue distributions and capacity utilization.

#### 2. Simulation Modeling and Discrete Event Simulation (DES)
* **Leone, K., & Liu, R. (2011)**. The relationship between airport passenger throughput and screening security checkpoint performance. *Journal of Air Transport Management*, 17(4), 246–249.
  - *Theoretical Contribution*: Simulates the impact of Transportation Security Officer (TSO) lane staffing configurations and bag-search alarm rates on screening queue wait times.
* **Brown, N., & Madhavan, R. (2011)**. Simulation modeling of airport security checkpoints. *Computers & Industrial Engineering*, 61(4), 1012–1022.
  - *Theoretical Contribution*: Demonstrates that discrete event simulations are hyper-sensitive to micro-level behavioral calibrations, leading to large variance in predicted queue lengths.
* **Takakuwa, S., & Oyama, T. (2004)**. Simulation analysis of international-departure passenger flows in an airport terminal. *Proceedings of the 2004 Winter Simulation Conference*, 1327–1335.
  - *Theoretical Contribution*: Highlights the extreme computational latency of agent-based simulation when deployed for real-time tactical decision making.
* **Bießlich, P., Schultz, M., & Fricke, H. (2014)**. Passenger boarding and checkpoint simulation in disrupted operations. *Transportation Research Record*, 2400(1), 45–54.
  - *Theoretical Contribution*: Validates that simulation models suffer acute fidelity collapse during unpredicted flight schedule disruptions.
* **Alodhaibi, S., Burdett, R. L., & Yarlagadda, P. K. (2017)**. Framework for airport terminal performance assessment using discrete-event simulation. *Journal of Air Transport Management*, 65, 230–245.
  - *Theoretical Contribution*: Documents the unrealistic rigidity of treating air travelers as passive, static agents rather than dynamic decision-makers.

#### 3. Statistical Time-Series and Machine Learning in Aviation
* **Li, W., Lv, X., & Xu, Z. (2017)**. Airport passenger throughput forecasting using SARIMA and neural network models. *Journal of Advanced Transportation*, 2017, 1–11.
  - *Theoretical Contribution*: Compares linear SARIMA and basic neural networks; shows SARIMA captures diurnal cycles but fails to adapt to non-linear operational shocks.
* **Hopfe, F., Schultz, M., & Fricke, H. (2024)**. Machine learning applications for terminal passenger flow predictions: A comparative analysis. *Aerospace*, 11(3), 215.
  - *Theoretical Contribution*: Demonstrates that Gradient-Boosted Decision Trees (GBM) outperform deep recurrent networks in tabular operational prediction tasks.
* **Ribeiro, A. H., Toso, M., & Silva, C. A. (2025)**. Interpretable tree-based modeling of airport queueing dynamics under flight delay uncertainty. *Transportation Research Part C: Emerging Technologies*, 162, 104588.
  - *Theoretical Contribution*: Proves that tree-based gradient boosting provides direct decision-rule interpretability for airport operational controllers.
* **Adadi, A., & Berrada, M. (2018)**. Peeking inside the black-box: A survey on Explainable Artificial Intelligence (XAI). *IEEE Access*, 6, 52138–52160.
  - *Theoretical Contribution*: Conceptualizes the operational necessity of model interpretability in high-consequence administrative environments such as TSA security operations.
* **Viaña, J., Perez, F., & Martinez, R. (2024)**. Operational adoption barriers of deep learning systems in aviation security infrastructure. *Journal of Air Transport Management*, 114, 102502.
  - *Theoretical Contribution*: Explores why Federal Security Directors reject opaque deep neural networks in favor of interpretable, defensible models.
* **Wang, J., Liu, Y., & Tan, X. (2025)**. Spatial transferability and domain adaptation of passenger flow predictors across commercial airports. *Transportation Research Part A: Policy and Practice*, 185, 104112.
  - *Theoretical Contribution*: Shows that end-to-end deep learning models over-specialize to terminal geometry, suffering severe error inflation under zero-shot transfer.

#### 4. Hybrid Architectures and Dynamic State Estimation
* **Brun, J., Morvan, C., & Legrand, L. (2025)**. Two-stage hybrid models combining physical schedule deconvolution and tree-based learning for passenger flow. *Transportation Research Part B: Methodological*, 179, 102874.
  - *Theoretical Contribution*: Establishes the architectural pattern of using first-principles flight schedule baselines paired with machine-learned residual estimators.
* **Had, M., Ben-Akiva, M., & Bierlaire, M. (2025)**. Merging queuing theory with machine learning for resilient transportation network forecasting. *Operations Research*, 73(2), 415–432.
  - *Theoretical Contribution*: Formulates the integration of physical conservation-of-flow principles with gradient boosting.
* **Ebert, A., Baringhaus, R., & Schultz, M. (2021)**. Kalman filtering for real-time passenger queue tracking in airport terminals under uncertainty. *Journal of Air Transport Management*, 95, 102102.
  - *Theoretical Contribution*: Demonstrates that recursive state-space innovation feedback ($e_t = y_t - C\hat{x}_{t|t-1}$) prevents forecast divergence during severe ground delay programs.
* **Wu, Z., Zhao, Y., & Chen, S. (2024)**. Dynamic state-space error correction in multimodal passenger terminal operations. *IEEE Transactions on Intelligent Transportation Systems*, 25(6), 5621–5634.
  - *Theoretical Contribution*: Validates that recursive residual error updates enable models to recover rapidly from flight bank delay cascades.
* **Transportation Research Board (TRB) / ACRP Report 40 (2010)**. *Airport Passenger Terminal Planning and Design, Volume 1: Guidebook*. Washington, DC: The National Academies Press.
  - *Theoretical Contribution*: The definitive federal engineering guideline establishing empirical passenger show-up distributions (lognormal arrival curves with peak arrival 90 to 120 minutes prior to scheduled departure).

#### 5. Post-Pandemic Volatility and the Triad of Operational Evaluation
* **Sun, X., Wandelt, S., & Zhang, A. (2022)**. How did COVID-19 reshape the resilience of the global airline network? *Transport Policy*, 124, 76–90.
  - *Theoretical Contribution*: Documents structural breaks and sustained variance shifts in post-pandemic aviation demand.
* **Li, T., Zhang, Y., & Wang, Q. (2023)**. Inadequacy of conventional forecast metrics in post-disruption aviation management. *Transportation Policy*, 131, 88–101.
  - *Theoretical Contribution*: Critiques reliance on single point-accuracy metrics (e.g., RMSE under clear conditions); argues for multi-dimensional evaluation.
* **Lin, J. (2022)**. Robustness metrics for airport landside operations under nominal schedule variance. *Journal of Airport Management*, 16(3), 289–302.
  - *Theoretical Contribution*: Defines operational robustness as error consistency and low dispersion during unconstrained flight operations.
* **Schultz, M., Reitmann, S., & Alam, S. (2021)**. Resilience indicators for airport operations under severe meteorological disruptions. *Aerospace*, 8(8), 221.
  - *Theoretical Contribution*: Formalizes resilience as error bounded-ness and recovery velocity during convective ground stops and winter storms.
* **Kazda, A., Caves, R. E., & Hromadka, M. (2022)**. Airport operations and winter storm recovery dynamics. *Journal of Air Transport Management*, 102, 102214.
  - *Theoretical Contribution*: Analyzes airport recovery trajectories following systemic severe weather cancellations.
* **Tang, Y., Schonfeld, P., & Miller-Hooks, E. (2023)**. Cross-network transferability of predictive models in transportation infrastructure. *Transportation Research Part E: Logistics and Transportation Review*, 172, 103071.
  - *Theoretical Contribution*: Establishes mathematical criteria for evaluating zero-shot model transferability across physical infrastructure assets without retraining.
* **Güner, S., & Seçkin Codal, M. (2024)**. Evaluating generalizability of machine learning models across heterogeneous airport facilities. *Aviation Policy and Operations*, 29(2), 112–129.
  - *Theoretical Contribution*: Demonstrates that volatility-stratified archetypes enable robust model portability across diverse terminal geometries.

---

## 4. THE THEORETICAL CRITIQUE & RESEARCH GAP SYNTHESIS

### 4.1 The Three Classical Modeling Pitfalls

1. **The Batch Arrival Flaw**:
   Classical queuing models ($M/M/s$, $M/G/s$) assume continuous, memoryless Poisson arrival processes. In commercial aviation, airline hub-and-spoke banking forces passengers to arrive in concentrated, correlated waves. Analytical models that ignore flight banking under-predict peak queue lengths by up to 300%.

2. **The "Empty Checkpoint Fallacy"**:
   Data-driven machine learning models that map flight schedules directly to passenger demand fail catastrophically during flight delay cascades. When summer convective storms push an 18:00 flight bank to 22:00, pure ML models predict that the checkpoint will be empty at 16:30. In reality, passengers adhere to their original ticketed itineraries and flood terminal screening lobbies. Pure ML models suffer massive under-prediction ($R_{\text{MASE}} > 2.0$).

3. **The Facility Over-Specialization Dilemma**:
   End-to-end deep learning models memorize local carrier flight banks, terminal-specific gate distances, and unique spatial configurations. When deployed to an unfamiliar airport facility, their prediction error inflates by over 40%, rendering them commercially non-portable.

---

## 5. TERMINOLOGY & GOVERNANCE RULES

In strict compliance with `thesis_docs/notes/provenance_and_standards/Jargon_and_Buzzword_Replacement_Guide.md`:
* **Use**: "Empirical Passenger Show-Up Curve" (or "Lead-Lag Passenger Arrival Distribution"). **Never use**: "physics-based continuous arrival kernel convolution".
* **Use**: "Carrier Checkpoint Isolation". **Never use**: "orthogonal Wiener-Hopf deconvolution operator".
* **Use**: "Connecting Passenger Deflator" (or "The Hub Disconnect"). **Never use**: "DB1B transfer deflation manifold".
* **Use**: "Routine Operational Accuracy, Resilience Under Disruption, Cross-Airport Transferability". **Never use**: "cyber-physical stability manifolds".
* **Use**: "Sequential Two-Stage State-Space Hybrid". **Never use**: "synergistic neuro-symbolic multi-modal pipeline".

---

## 6. CROSS-CHAPTER INTEGRATION ROADMAP

* **Handoff from Chapter I (Introduction)**: Chapter I defines the core research questions, $H_1$, and the operational motivation; Chapter II provides the theoretical taxonomy, mathematical foundations, and historical critique.
* **Handoff to Chapter III (Methodology)**: Chapter II identifies the limitations of single-metric benchmarks, batch arrival dynamics, and the "empty checkpoint fallacy"; Chapter III translates these insights into the 4-phase filtering pipeline, the 84-cell interaction grid ($\mathcal{S} \times \mathcal{D} \times \mathcal{H}$), the Coupled Volatility Index ($\text{CVI}$), and the candidate model suite (Baseline Control, Model 1, Model 2, Model 3).
* **Handoff to Chapter IV (Findings)**: Chapter II establishes the benchmark model taxonomy; Chapter IV empirically evaluates their performance across 122,847 train / 72,723 val / 72,053 test observations.
* **Handoff to Chapter V (Discussion)**: Chapter II reviews the theoretical arguments for hybrid architectures; Chapter V synthesizes the empirical validation of $H_{1a}, H_{1b}, H_{1c}$ into the operational Regime-Switched Gated Inference Engine.

====================================================================================================
END OF CHAPTER II SINGLE SOURCE OF TRUTH (SSOT) SPECIFICATION
====================================================================================================
