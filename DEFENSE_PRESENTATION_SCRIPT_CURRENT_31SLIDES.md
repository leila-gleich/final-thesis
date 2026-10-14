# 25-Minute Master Thesis Defense Oral Examination Script
## Matching Current 31-Slide Presentation Deck: `Thesis-Defense-outline.pptx`
### Evaluating Predictive Techniques to Model Stochastic Airport Passenger Flow (MSAA / Gleich 700B)
**Candidate**: Leila Gleich | **Institution**: Embry-Riddle Aeronautical University  
**Degree**: Master of Science in Aeronautics / Aviation Data Analytics  
**Defense Presentation Target Duration**: Exactly 25:00 Minutes (No Questions Included)  
**Total Word Count**: ~3,480 Words | **Speaking Rate**: ~138–140 Words Per Minute (Deliberate Academic Cadence)  
**Synchronized Slide Deck**: [`thesis_final_package/defense/Thesis-Defense-outline.pptx`](file:///Users/leilagleich/Library/CloudStorage/OneDrive-Embry-RiddleAeronauticalUniversity/final-thesis/thesis_final_package/defense/Thesis-Defense-outline.pptx) (31 Slides)

---

## Presentation Timing & Slide Navigation Map (31 Slides | 25:00 Minutes)

| Phase | Slide Range | Title / Topic Focus | Segment Duration | Cumulative Elapsed Time |
| :--- | :--- | :--- | :--- | :--- |
| **Phase I: Introduction & Problem Formulation** | Slides 1–5 | Title, Agenda, Research Problem, Research Question, Master Hypothesis ($H_1$) | 3:45 | 0:00 – 3:45 |
| **Phase II: Literature Review & Foundations** | Slides 6–10 | Literature Foundations, Traditional PCA Models, Volatility vs. Volume Gap, Micro-Simulation Latency, Advanced ML | 4:45 | 3:45 – 8:30 |
| **Phase III: Methodology & Filtering Funnel** | Slides 11–13 | Architecture Overview, Design & Procedures (4 Phases), Four-Tier Filtering Funnel | 2:45 | 8:30 – 11:15 |
| **Phase IV: Data Foundation & Cohort Baseline** | Slides 14–19 | Findings Transition, Initial Dataset, Pipeline Results, Top 9 Descriptive Statistics (Table), Macro Archetypes & Lead-Lag, Model Implications | 5:30 | 11:15 – 16:45 |
| **Phase V: Model Execution & Hypothesis Testing** | Slides 20–25 | Development & Execution, Four Paradigms, Holdout Benchmarks (Table 4.10), Multi-Pillar Matrix (Table 4.11), Radar Chart ($H_1$), Hypothesis Confirmation | 5:30 | 16:45 – 22:15 |
| **Phase VI: Discussion, Application & Conclusion** | Slides 26–31 | Theoretical Mechanisms, Real-World Application (Playbook), Future Research, Conclusions, Data Overview, Closing & Q&A Transition | 2:45 | 22:15 – 25:00 |

---

## Phase I: Introduction & Problem Formulation (Slides 1–5 | 0:00 – 3:45)

### Slide 1: Title Slide
* **Slide Title**: AN EVALUATION OF PERFORMANCE MEASURES FOR PREDICTIVE APPROACHES TO MODEL TSA THROUGHPUT VOLATILITY
* **Visual**: *Title slide with candidate name (Leila Gleich), institutional affiliation (Embry-Riddle Aeronautical University), degree program, and date (October 2026).*
* **Pacing**: 0:00 – 0:30 (Duration: 30s | Running Total: 0:30)

> "Good morning, members of the committee, faculty, and colleagues. 
> 
> My name is Leila Gleich, and today I am defending my Master of Science in Aeronautics thesis titled: *An Evaluation of Performance Measures for Predictive Approaches to Model TSA Throughput Volatility*.
> 
> This research investigates the operational and mathematical coupling between commercial airline flight operations and landside Transportation Security Administration checkpoint screening demand. By evaluating predictive paradigms across 44 continuous post-pandemic months, we demonstrate why airport security checkpoints must be managed through the lens of passenger throughput volatility rather than static headcounts, and we formalize the asymmetric trade-offs governing operational model selection."

---

### Slide 2: Agenda
* **Slide Title**: Agenda
* **Visual**: *Structured presentation roadmap outlining the 6 phases of the oral defense.*
* **Pacing**: 0:30 – 1:00 (Duration: 30s | Running Total: 1:00)

> "Our presentation is structured into six sequential phases over the next 24 minutes:
> 
> First, we define the terminal queuing problem and our core research question. Second, we examine existing literature and the fundamental gap between passenger volume and arrival volatility. Third, we establish our scientific methodology and four-tier filtering pipeline. Fourth, we review the empirical data foundation across our nine-airport experimental cohort. Fifth, we evaluate prospective holdout benchmarks across three operational dimensions. Finally, we translate our empirical findings into an operational decision playbook for airport operators and TSA leadership."

---

### Slide 3: Research Problem
* **Slide Title**: Research Problem
* **Visual**: *Key operational constraints bulleted alongside terminal crowding photo (`figures/terminal_queuing_friction.jpg`): Inflexible physical capacity, quadratic delay scaling under Kingman's formula, static staffing fragility, and core objective.*
* **Pacing**: 1:00 – 2:00 (Duration: 60s | Running Total: 2:00)

> "Airport security screening checkpoints represent the most rigid physical bottleneck in commercial aviation. 
> 
> Once certified Transportation Security Officers are rostered and Advanced Imaging Technology lanes are open, capacity cannot expand dynamically in real time. Under Kingman's heavy-traffic queuing formula, passenger wait times do not increase linearly as terminal demand grows; rather, waiting times scale quadratically with arrival volatility ($C_a^2$) as checkpoint lane utilization ($\rho$) approaches capacity saturation:
> 
> $$W_q \approx \left[ \frac{\rho}{c(1-\rho)} \right] \cdot \left[ \frac{C_a^2 + C_s^2}{2} \right] \cdot \frac{1}{\mu}$$
> 
> For decades, commercial aviation planners have relied on published airline schedules and static historical headcount tables to roster security checkpoint lanes. When flight departure delays cascade or severe convective storms halt outbound traffic, these static volume tables fail catastrophically. Checkpoint lobbies experience sudden, chaotic arrival surges that trigger exponential passenger delays, terminal crowding, and missed flight departures. 
> 
> The core operational objective of this thesis is to move beyond static headcount averages and establish volatility-aware stochastic forecasting models for airport checkpoint management."

---

### Slide 4: Research Question
* **Slide Title**: Research Question
* **Visual**: *The primary research inquiry displayed prominently with the three core evaluative pillars: Robustness (routine accuracy), Resilience (disruption stability), and Generalizability (cross-airport portability).*
* **Pacing**: 2:00 – 2:45 (Duration: 45s | Running Total: 2:45)

> "To resolve this challenge, this thesis addresses one overarching research question:
> 
> *Which predictive modeling frameworks are most effective for forecasting airport passenger security screening throughput volatility when prioritizing three competing operational performance measures?*
> 
> Specifically, we evaluate candidate models across:
> 1. **Robustness**: Predictive consistency and low dispersion under routine, nominal daily operations.
> 2. **Resilience**: Error boundedness, stability, and speed of recovery during severe convective weather delays and ground stops.
> 3. **Generalizability**: Portability and out-of-the-box accuracy when transferred zero-shot to an unfamiliar airport terminal layout without local retraining."

---

### Slide 5: Hypothesis
* **Slide Title**: Hypothesis
* **Visual**: *Master Hypothesis $H_1$ (The Asymmetric Trade-Off) displayed with explicit mathematical performance targets across Robustness, Resilience, and Generalizability.*
* **Pacing**: 2:45 – 3:45 (Duration: 60s | Running Total: 3:45)

> "Our investigation is guided by **Master Hypothesis 1 ($H_1$)**: *The Asymmetric Trade-Off Hypothesis*.
> 
> We hypothesize that across distinct modeling paradigms—deterministic flight schedules, supervised machine learning, and dynamic two-stage hybrids—no single predictive approach will prove universally superior across all operational regimes. Rather, each modeling family exhibits stark, asymmetric performance trade-offs:
> 
> * In **Dimension 1 (Robustness)**, under nominal conditions with departure delays under 15 minutes, machine learning and dynamic hybrids will meet our stated target ($\text{MASE} < 0.700$), with pure machine learning winning routine Pareto efficiency due to zero feedback compute latency.
> * In **Dimension 2 (Resilience)**, during severe irregular operations with delays exceeding 45 minutes or cancellations, the dynamic hybrid model will prove decisively superior ($R_{\text{MASE}} \approx 1.00$, $\text{TTR} < 4.0\text{h}$), while pure machine learning collapses due to the Empty Checkpoint Fallacy.
> * In **Dimension 3 (Generalizability)**, under zero-shot transfer without local recalibration, the deterministic schedule model will prove decisively superior ($\text{RTR} \approx 1.00$, $\Delta\text{MASE} \le 10.0\%$), while complex hybrid models suffer transfer penalties from terminal geometry overfitting."

---

## Phase II: Literature Review & Theoretical Foundations (Slides 6–10 | 3:45 – 8:30)

### Slide 6: Literature Review & Theoretical Foundations
* **Slide Title**: Literature Review & Theoretical Foundations
* **Visual**: *Evolutionary progression of terminal planning literature: Traditional queuing, micro-simulation, advanced ML, hybrid frameworks, and post-pandemic structural shifts.*
* **Pacing**: 3:45 – 4:30 (Duration: 45s | Running Total: 4:30)

> "Chapter II synthesizes over four decades of airport terminal planning and transportation econometrics literature. 
> 
> Historically, research in checkpoint management evolved across four distinct analytical eras: starting with classical Markovian queuing equations in the 1980s; transitioning to discrete-event simulation in the 2000s; expanding into data-driven machine learning over the last decade; and culminating in emerging two-stage hybrid architectures. 
> 
> Across this literature, however, passenger terminal demand has almost universally been treated as an unvarying function of published flight timetables. Our review identifies three critical vulnerabilities in historical literature: the decoupling of volume from volatility, the computational latency of micro-simulation, and the fragility of unconstrained machine learning during irregular operations."

---

### Slide 7: Traditional Models
* **Slide Title**: Traditional Models
* **Visual**: *Classical queuing formulations ($M/M/s, \text{NHPP}$), static airline flight bank convolutions, and Principal Component Analysis capturing 77.0% of system variance across 3 operational vectors.*
* **Pacing**: 4:30 – 5:30 (Duration: 60s | Running Total: 5:30)

> "The earliest predictive frameworks relied on classical queuing theory—specifically $M/M/s$ and Non-Homogeneous Poisson Processes (NHPP; Odoni, 1986; Wang, 2018). 
> 
> While closed-form queuing formulas offer transparent parameters and negligible compute latency, they suffer from two fatal operational flaws:
> First, they assume passenger arrivals are independent, stationary Poisson streams. In reality, commercial airports operate on synchronized flight banks, where dozens of aircraft depart simultaneously, generating massive, correlated arrival waves.
> Second, classical models assume all ticketed passengers cross landside screening checkpoints, ignoring airside connecting passengers.
> 
> Furthermore, linear time-series models (such as SARIMA; Box et al., 2015; Li et al., 2017) capture diurnal 24-hour cycles but remain completely blind to flight delay propagation. When departure delays cascade, past passenger arrival trends no longer match disrupted flight departure realities."

---

### Slide 8: The Gap: Volatility vs Volume
* **Slide Title**: The Gap: Volatility vs Volume
* **Visual**: *The Values versus Volatility empirical decoupling: Headcount vs. Delays ($r = -0.062, p = 0.77, R^2 = 2.5\%$) versus Volatility Couplings ($r = +0.4373, p < 0.05, R^2 = 19.1\%$). Rendered KaTeX formula for $CV_{\text{TSA}}$ and Kingman heavy-traffic scaling.*
* **Pacing**: 5:30 – 6:30 (Duration: 60s | Running Total: 6:30)

> "This brings us to the foundational empirical gap identified in our thesis: **The Values versus Volatility Paradigm**.
> 
> When we examine empirical federal data across the Top 25 U.S. airfields, static passenger volume headcounts show absolutely zero statistically significant correlation with flight departure delays ($r = -0.062, p = 0.77$). An airport experiencing 20,000 delayed passengers on a stormy afternoon may report the exact same aggregate 24-hour headcount as an undisturbed sunny Tuesday.
> 
> However, when we evaluate **Throughput Volatility**—measured by the scale-free Coefficient of Variation ($CV_{\text{TSA}} = \sigma / \mu$)—a powerful, statistically significant operational coupling emerges ($r = +0.4373, p < 0.05, R^2 = 19.1\%$). Checkpoint arrival volatility is tightly synchronized with flight departure delay volatility ($CV_{\text{delay}}$). 
> 
> Grounded in Kingman's queuing theorem, it is arrival variance ($C_a^2$) that triggers exponential queue wait times, not static daily headcount levels."

---

### Slide 9: Shift to Micro-Simulation Modeling
* **Slide Title**: Shift to Micro-Simulation Modeling
* **Visual**: *Side-by-side comparison: Spatial Fidelity Advantages (granular physical paths, concourse sizing, capital planning) vs. Operational Dispatch Latency Bottlenecks (20–45 minute compute runtimes, heavy calibration overhead, unsuited for live tactical control).*
* **Pacing**: 6:30 – 7:30 (Duration: 60s | Running Total: 7:30)

> "To overcome the rigid mathematical assumptions of analytical queuing equations, terminal planners adopted micro-simulation—primarily Discrete Event Simulation platforms like ARENA, CAST, and Simio (Brown & Madhavan, 2011; Leone & Liu, 2011).
> 
> **What are the advantages of micro-simulation?**  
> Micro-simulation provides exceptional spatial fidelity. It models individual traveler trajectories through ticket verification, baggage divestiture, and body scanners, making it the global standard for multi-year airport terminal capital planning.
> 
> **What are its critical operational shortfalls?**  
> First, **Computational Latency**: Simulating thousands of individual stochastic passenger agents requires 20 to 45 minutes of compute runtime. When summer thunderstorms roll in and flight departure gates change dynamically, a 45-minute simulation run is obsolete before execution finishes.
> Second, **Calibration Brittleness**: Micro-simulations require hundreds of manual behavioral parameters that fail under unexpected disruption."

---

### Slide 10: Advanced Predictive Models
* **Slide Title**: Advanced Predictive Models
* **Visual**: *Machine learning architectures (Gradient Boosted Trees / HistGBM): 24 BTS OTP attributes, millisecond inference, routine Pareto efficiency vs. The Empty Checkpoint Fallacy diagram (`Picture 7`).*
* **Pacing**: 7:30 – 8:30 (Duration: 60s | Running Total: 8:30)

> "In response to simulation latency, modern transportation literature turned to **Supervised Machine Learning**, specifically Gradient-Boosted Decision Trees (Chen & Guestrin, 2016; Hopfe et al., 2024; Ribeiro et al., 2025).
> 
> **Why is machine learning superior under routine conditions?**  
> Decision-tree ensembles eliminate the computational latency barrier entirely, generating 24-hour tactical forecasts in milliseconds. Furthermore, they ingest high-dimensional operational telemetry. In our framework, Model 2 ingests 24 Bureau of Transportation Statistics features—including departure delays, taxi-out queues, aircraft seat gauge, and tactical cancellations—achieving outstanding routine accuracy ($\text{MASE} = 0.680\text{--}0.700$).
> 
> **What are its critical operational failure modes?**  
> 1. **The Empty Checkpoint Fallacy**: When severe thunderstorms trigger ground stops, automated airline feeds record dozens of cancelled departures. Decision trees observe cancelled flights and infer that passenger demand has vanished, forecasting near-zero checkpoint throughput. In reality, thousands of stranded passengers flood terminal lobbies seeking rebooking. Pure ML predicts empty checkpoints right when terminal crowding is at its worst ($R_{\text{MASE}} = 2.14$, acute collapse).
> 2. **Black-Box Opacity**: Uninterpretable neural weights cannot be justified administratively by Federal Security Directors during audits."

---

## Phase III: Methodology & Filtering Funnel (Slides 11–13 | 8:30 – 11:15)

### Slide 11: Architecture Overview
* **Slide Title**: Architecture Overview
* **Visual**: *The Sequential Two-Stage Hybrid formulation ($\widehat{Y}_t = M_{\text{base}} + \alpha \cdot (Y_{t-1} - \widehat{Y}_{t-1})$): Stage 1 physical schedule convolution with DB1B connecting deflator coupled with Stage 2 real-time floor error feedback.*
* **Pacing**: 8:30 – 9:30 (Duration: 60s | Running Total: 9:30)

> "To resolve the fragility of pure machine learning, emerging literature—including Brun et al. (2025), Had et al. (2025), and Ebert et al. (2021)—proposes **Sequential Two-Stage Hybrid Architectures**.
> 
> In our Model 3 architecture, we couple physical operational structure with dynamic real-time learning:
> 
> $$\widehat{Y}_t = M_{\text{base}}(\text{Schedule}_t, \mathbf{X}_t) + \alpha \cdot (Y_{t-1} - \widehat{Y}_{t-1})$$
> 
> * **Stage 1 (Operational Schedule Base)**: We convolve scheduled airline flight banks across empirical ACRP Report 40 passenger show-up curves and deflate by BTS DB1B connecting ratios ($1 - S_{\text{connect}}$). This anchors the diurnal heartbeat of the terminal.
> * **Stage 2 (Real-Time Floor Feedback)**: Grounded in Kalman state-space estimation, the model ingests the live prior-hour screening floor innovation ($e_{t-1} = Y_{t-1} - \widehat{Y}_{t-1}$).
> 
> When convective storms ground flights, live screening sensors detect stranded travelers still clearing security. The positive innovation overrides the stale schedule, restoring forecast accuracy within 2.8 hours ($R_{\text{MASE}} = 1.05$)."

---

### Slide 12: Design and Procedures: 4 Phases
* **Slide Title**: Design and Procedures: 4 Phases
* **Visual**: *Four-phase research execution lifecycle: Phase 1 (Ingestion & ETL), Phase 2 (Four-Tier Filtering), Phase 3 (Feature Engineering & 84-Cell Matrix), Phase 4 (Out-of-Time Holdout Benchmarking).*
* **Pacing**: 9:30 – 10:15 (Duration: 45s | Running Total: 10:15)

> "Our empirical research lifecycle follows a four-phase quantitative experimental design:
> 
> * **Phase 1 (Data Foundation & ETL)**: Conformed 67.2 million raw federal records from TSA FOIA, BTS Form 234 On-Time Performance, Form 41 T-100 Segment Capacity, and DB1B Ticket Surveys into a DuckDB Star Schema.
> * **Phase 2 (Econometric Filtering)**: Executed our four-tier purposive filtering funnel to eliminate inter-airline passenger mixing and common-use checkpoint contamination.
> * **Phase 3 (Calibration & Engineering)**: Engineered 24 operational features across an 84-cell interaction grid, verifying sample sufficiency ($N_{\text{train}} \ge 50$ in 98.8% of cells).
> * **Phase 4 (Multi-Pillar Testing)**: Executed out-of-time prospective holdout testing on full-year 2025 data across Robustness, Resilience, and Generalizability."

---

### Slide 13: The Four-Tier Filtering Funnel
* **Slide Title**: The Four-Tier Filtering Funnel
* **Visual**: *Funnel diagram (`Picture 6`): Macro Tier (450+ airports -> Top 25), Meso Tier (Top 25 -> 14), Micro Tier (14 -> 10), Final Cohort Tier (9 airfields, 12 carrier-exclusive terminal complexes).*
* **Pacing**: 10:15 – 11:15 (Duration: 60s | Running Total: 11:15)

> "Commercial airports are highly heterogeneous environments. To ensure valid causal inferences between flight delays and checkpoint queues, we engineered a **Four-Tier Purposive Filtering Pipeline**:
> 
> 1. **Macro Tier (Top 25 Airfields)**: Screened over 450 commercial airports down to the Top 25 large hubs representing 68.4% of national passenger enplanements.
> 2. **Meso Tier (Connecting Shielding Filter)**: Filtered out mega connecting transfer hubs where connecting ratios exceed 65% (such as Atlanta and Charlotte), eliminating unobserved airside transfer confounding.
> 3. **Micro Tier (Multi-Carrier De-Contamination)**: Filtered out common-use shared terminals where passenger flows from competing airlines intermix before screening lanes.
> 4. **Final Cohort Tier (9 Airfields, 12 Complexes)**: Isolated nine commercial airfields representing 12 carrier-exclusive screening complexes (BOS, DFW, DTW, EWR, IAH, LAX, LGA, ORD, and PHL) providing pure orthogonal carrier isolation across American, Delta, and United."

---

## Phase IV: Data Foundation & Cohort Baseline (Slides 14–19 | 11:15 – 16:45)

### Slide 14: Findings and Discussion Transition
* **Slide Title**: Findings and discussion
* **Visual**: *Divider slide marking the transition from methodology to Chapter IV empirical findings and Chapter V operational discussion.*
* **Pacing**: 11:15 – 11:45 (Duration: 30s | Running Total: 11:45)

> "This brings us to Phase IV: Empirical Findings and Operational Discussion. 
> 
> We now examine the post-ETL data foundations, the structural characteristics of our nine-airport cohort, the lead-lag transfer dynamics between flight banks and security queues, and the prospective out-of-time holdout benchmarks across our candidate models."

---

### Slide 15: Initial Dataset
* **Slide Title**: Initial Dataset
* **Visual**: *Temporal Boundaries (May 1, 2022 to Dec 31, 2025), Chow break test ($F = 1.42, p = 0.18$), Seasonality regimes (Table 4.3b), TSA & OTP warehouse integration, and data hygiene rules.*
* **Pacing**: 11:45 – 12:45 (Duration: 60s | Running Total: 12:45)

> "Our empirical analysis spans 44 continuous months from May 1, 2022 to December 31, 2025. 
> 
> To ensure time-series stationarity, we established May 1, 2022—the federal dissolution of the transit mask mandate—as our post-pandemic demarcation baseline. A formal Chow structural break test yielded $F = 1.42, p = 0.18$, failing to reject the null hypothesis and confirming econometric stability across our development window.
> 
> Two data hygiene rules were essential:
> 1. **Quarantining Null Spatial Keys**: We isolated 22,190 unresolvable TSA checkpoint records to a null surrogate key, preventing the creation of a fictitious 9.7-million passenger phantom airport.
> 2. **Structural Zeros Preservation**: 64,743 zero-throughput lane hours occurred during overnight curfew hours (00:00–03:59). Rather than naively imputing these with moving averages, we preserved them as true physical lane closures using zero-bounded hurdle and Tweedie count models ($p = 1.3$)."

---

### Slide 16: Pipeline Results
* **Slide Title**: Pipeline Results
* **Visual**: *Key cohort behavioral characteristics: 9 airports, 12 carrier-exclusive screening complexes, high movement density, heightened operational disruption, and dominant local originating passenger share.*
* **Pacing**: 12:45 – 13:45 (Duration: 60s | Running Total: 13:45)

> "The filtering pipeline successfully isolated nine commercial airfields representing 12 carrier-exclusive screening environments, achieving complete factorial balance across legacy airlines and terminal archetypes.
> 
> As detailed on Slide 16, this cohort exhibits three distinct operational characteristics:
> First, **Flight Movement Density**: The cohort accounts for 4.21 million commercial flight movements, capturing high-density hub-and-spoke operations.
> Second, **Heightened Operational Turbulence**: Checkpoint complexes in this cohort experience 28.4% greater delay variance than secondary spoke airfields, providing an ideal stress environment for resilience testing.
> Third, **Local Originating Dominance**: Across these 12 complexes, true local originating passenger traffic averages 48.6%, mathematically confirming that screening lanes are governed by landside passenger show-up curves rather than airside transfers."

---

### Slide 17: Top 9 Descriptive Statistics (PAX Throughput)
* **Slide Title**: Top 9 Descriptive Statistics (PAX Throughput)
* **Visual**: *Table of 9 airfields across $N = 269,764$ hourly complex observations: BOS, DFW, DTW, EWR, IAH, LAX, LGA, ORD, PHL detailing Observation count, Mean throughput, Standard Deviation, Median, Maximum, and Terminal Complex.*
* **Pacing**: 13:45 – 14:45 (Duration: 60s | Running Total: 14:45)

> "Slide 17 displays the descriptive summary statistics across our nine-airport experimental cohort, spanning 269,764 hourly complex observations:
> 
> Notice the substantial operational diversity across these hubs:
> * Mean hourly passenger throughput ranges from 1,443 passengers per hour at Detroit's McNamara Terminal to 4,165 passengers per hour across Terminals 2, 3, and 7 at Los Angeles (LAX).
> * Peak throughput reaches as high as 9,569 passengers per hour at LAX and 9,380 at Chicago O'Hare (ORD).
> * Crucially, hourly throughput standard deviation ($\sigma$) exceeds 1,000 passengers per hour across all facilities, reaching 2,127 pax/hr at LAX and 1,774 pax/hr at Newark Terminal C. 
> 
> This intense dispersion reinforces why models designed for average headcounts fail; staffing rosters must be buffered against these multi-thousand passenger volatility swings."

---

### Slide 18: Macro Archetypes & Lead-Lag Dynamics
* **Slide Title**: Macro Archetypes & Lead-Lag Dynamics
* **Visual**: *Day-of-week archetypes (Midweek Business, Mon/Fri Transition, Weekend Leisure) and empirical passenger arrival distribution curve (`Picture 5` / Figure 4.5) peaking at $t-2$ hours prior to scheduled flight departures.*
* **Pacing**: 14:45 – 15:45 (Duration: 60s | Running Total: 15:45)

> "Slide 18 details the temporal mechanics connecting flight schedules to checkpoint queues.
> 
> First, **Weekly Archetypes**: Operational demand follows three distinct structural profiles: Midweek Business Peaks (Tuesday/Wednesday high-frequency corporate travel), Weekend Leisure Surges (Sunday afternoon returns), and Mon/Fri Transition Banks.
> 
> Second, **The Lead-Lag Transfer Timeline**: A foundational premise of our research is that passengers arrive at screening checkpoints well in advance of departure. As illustrated in the convolution curve, convolving scheduled flight banks across an empirical ACRP Report 40 lognormal distribution reveals that passenger arrivals at security checkpoints peak precisely **two hours prior to scheduled departure ($t-2$)**. 
> 
> Convolving this $t-2$ arrival probability density curve raised explained variance from 19.88% under contemporaneous scheduling to 48.78%—a 145% explanatory gain."

---

### Slide 19: Implications for Model Development
* **Slide Title**: Implications for Model Development
* **Visual**: *Four core methodological principles: Single carrier complex isolation, connecting passenger deflation, strict prior-hour information availability, and zero-bounded hurdle/Tweedie formulations.*
* **Pacing**: 15:45 – 16:45 (Duration: 60s | Running Total: 16:45)

> "These empirical findings establish four mandatory constraints for valid predictive modeling:
> 
> 1. **Carrier Checkpoint Isolation**: Restricting analysis to dedicated single-carrier complexes isolates the causal link between airline flight disruptions and checkpoint queues, eliminating multi-carrier contamination.
> 2. **Connecting Passenger Deflator**: Multiplying scheduled airline seat capacity by $(1 - S_{\text{connect}})$ from DB1B ticket data deflates airside transfers, aligning flight seats with true landside arrivals.
> 3. **Strict Information Availability**: To prevent feature lookahead leakage, all operational delay covariates at forecast hour $t$ are strictly restricted to realized prior-hour data available at $t-1$.
> 4. **Zero-Bounded Hurdle Formulation**: Checkpoint volume cannot be negative; Tweedie compound Poisson modeling ($p = 1.3$) accurately handles overnight terminal closures."

---

## Phase V: Model Execution & Hypothesis Testing (Slides 20–25 | 16:45 – 22:15)

### Slide 20: Model Development & Execution
* **Slide Title**: Model Development & Execution
* **Visual**: *Feature engineering (24 BTS attributes across 84-cell grid), training window (May 2022 to Dec 2024), prospective holdout (full-year 2025; 72,053 complex-hours), and MASE volatility standard.*
* **Pacing**: 16:45 – 17:30 (Duration: 45s | Running Total: 17:30)

> "Slide 20 outlines our model execution pipeline. 
> 
> We engineered 24 operational features across our 84-cell interaction grid, spanning departure delays, taxi-out times, tactical cancellations, and seat gauge.
> 
> All models were calibrated strictly on our development partition (May 1, 2022 to December 31, 2024) with a 7-day operational purge embargo. Models were then benchmarked against the untouched, full-year 2025 prospective holdout dataset comprising 3,222 test airport-days and 72,053 hourly complex observations.
> 
> Mean Absolute Scaled Error (MASE) serves as our primary scale-free benchmark, normalizing error against the non-parametric Baseline Control ($\text{MASE} \equiv 1.000$)."

---

### Slide 21: Model Development (Four Candidate Paradigms)
* **Slide Title**: Model Development
* **Visual**: *The 3-Model Candidate Evaluation Suite plus Baseline Control: Baseline Control (Daily Persistence $y_{t-24}$), Model 1 (Deterministic Flight Schedule), Model 2 (Supervised Machine Learning / HistGBM), Model 3 (Dynamic Two-Stage Hybrid).*
* **Pacing**: 17:30 – 18:30 (Duration: 60s | Running Total: 18:30)

> "Slide 21 illustrates the four modeling paradigms evaluated in our prospective holdout:
> 
> 1. **Baseline Control (Daily Persistence Benchmark)**: Forecasts checkpoint volume using the identical hour from the previous day ($\widehat{Y}_t = Y_{t-24}$). It requires zero operational features and serves as our non-parametric benchmark ($\text{MASE} \equiv 1.000$).
> 2. **Model 1 (Deterministic Flight Schedule Model)**: Convolves published airline schedules across empirical ACRP Report 40 lognormal show-up curves with DB1B connecting deflation.
> 3. **Model 2 (Supervised Machine Learning Model)**: Automated Histogram Gradient-Boosted Decision Trees ingesting all 24 BTS OTP operational attributes to capture non-linear delay thresholds.
> 4. **Model 3 (Dynamic Two-Stage Hybrid Model)**: Sequential model coupling Stage 1 schedule convolutions with live 1-step prior-hour error innovation feedback ($e_{t-1} = Y_{t-1} - \widehat{Y}_{t-1}$) from the checkpoint floor."

---

### Slide 22: Model Performance: Holdout Benchmarks (Table 4.10)
* **Slide Title**: Model Performance
* **Visual**: *Master Model Benchmark Matrix (Table 4.10): Baseline Control ($R^2 = 0.6719, \text{RMSE} = 253.6, \text{MASE} = 1.000$), Model 1 ($R^2 = 0.4980, \text{RMSE} = 313.4, \text{MASE} = 0.945$), Model 2 ($R^2 = 0.6178, \text{RMSE} = 273.5, \text{MASE} = 0.779, DM = 42.15$), Model 3 ($R^2 = 0.7483, \text{RMSE} = 222.1, \text{MASE} = 0.662, DM = 48.72$).*
* **Pacing**: 18:30 – 19:30 (Duration: 60s | Running Total: 19:30)

> "Slide 22 presents Table 4.10: the certified out-of-time evaluation benchmarks on the 2025 prospective holdout across 72,053 hourly complex observations:
> 
> * **Model 1 (Deterministic Schedule)** achieves $\text{Test } R^2 = 0.4980$ and $\text{MASE} = 0.945$, outperforming simple persistence by 5.5% without requiring real-time IT feeds.
> * **Model 2 (Supervised Machine Learning)** elevates explained variance to **$R^2 = 0.6178$**, cutting RMSE to 273.5 pax/hr and holdout MASE to 0.779. Pairwise Diebold-Mariano tests confirm that Model 2's error reductions over deterministic scheduling are statistically decisive ($DM = 42.15, p < 0.0001$).
> * **Model 3 (Dynamic Hybrid)** is the overall holdout leader, explaining **74.83% of total passenger throughput volatility variance** ($R^2 = 0.7483$), achieving an RMSE of **222.1 pax/hr** and a holdout MASE of **0.662** ($DM = 48.72, p < 0.0001$)."

---

### Slide 23: Model Performance: Multi-Pillar Hypothesis Matrix (Table 4.11)
* **Slide Title**: Model Performance
* **Visual**: *Master Multi-Pillar Hypothesis Evaluation Matrix (Table 4.11 / Table 4.7): Dimension 1 Robustness (RMSE/MASE), Dimension 2 Resilience ($R_{\text{MASE}}$, $\text{RMSE}_{\text{shock}}$, TTR), and Dimension 3 Generalizability (RTR, $\Delta\text{MASE}$). Bold highlights indicating dimension winners.*
* **Pacing**: 19:30 – 20:45 (Duration: 75s | Running Total: 20:45)

> "Now, examine Slide 23—Table 4.11—which represents the central empirical core of this thesis. 
> 
> While Model 3 achieved the highest aggregate holdout fit, **Model 3 is NOT the universal winner across all performance measures**:
> 
> * **Dimension 1: Robustness (Nominal Routine Operations)**: Under calm conditions ($\text{Delay} < 15\text{m}$, 0 cancellations), Model 3 achieves lowest RMSE (222.1 pax/hr, $\text{MASE} = 0.662$). However, **Model 2 wins Routine Pareto Efficiency**: it meets the academic target ($\text{MASE} = 0.680\text{--}0.700$) with near-zero compute latency and requires zero live feedback feeds.
> * **Dimension 2: Resilience (Severe Disruption / IROPS)**: During severe thunderstorms and ground stops ($\text{Delay} \ge 45\text{m}$ or Cancels $\ge 5$), **Model 3 is the DECISIVE CHAMPION**. It maintains a resilient shock multiplier ($R_{\text{MASE}} = 1.05 \approx 1.00$), achieves lowest shock error ($\text{RMSE}_{\text{shock}} = 254.2\text{ pax/hr}$), and recovers normal error bounds in **2.8 hours** ($\text{TTR} < 4.0\text{h}$). Conversely, pure machine learning (Model 2) collapses ($R_{\text{MASE}} = 2.14$) due to the Empty Checkpoint Fallacy.
> * **Dimension 3: Generalizability (Zero-Shot Portability)**: Under zero-shot transfer from Newark (EWR) to LaGuardia (LGA) without local retraining, **Model 1 is the DECISIVE CHAMPION** ($\text{RTR} = 1.04 \approx 1.00, \Delta\text{MASE} = +4.0\%$). **Model 3 decisively fails generalizability** ($\text{RTR} = 1.19 > 1.00, \Delta\text{MASE} = +21.5\%$) because its decision trees overfit to Newark's specific terminal geometry and bank timings."

---

### Slide 24: Importance of Dynamic Performance Measures (Radar Chart)
* **Slide Title**: Importance of Dynamic Performance Measures
* **Visual**: *The Asymmetric Trade-Off Evaluation Triangle (Figure 5.1 Radar Chart / `Picture 4`): Robustness, Resilience, and Generalizability axes proving non-dominance across candidate paradigms.*
* **Pacing**: 20:45 – 21:30 (Duration: 45s | Running Total: 21:30)

> "Slide 24 visually synthesizes this trade-off space through the **Asymmetric Trade-Off Evaluation Triangle** (Figure 5.1).
> 
> As you can see, no single polygon encompasses all three operational vertices:
> * Model 3 (the blue polygon) stretches deeply into the **Resilience** vertex, absorbing severe convective disruption, but contracts sharply on the **Generalizability** axis.
> * Model 1 (the green polygon) anchors the **Generalizability** vertex, maintaining layout invariance across airports, but lacks disruption resilience.
> * Model 2 (the orange polygon) balances the interior, winning **Routine Pareto Efficiency** under clear skies.
> 
> This empirical geometry disproves universal model superiority and confirms that forecasting algorithms must be selected dynamically based on the prevailing operational regime."

---

### Slide 25: Model Results Evaluation - Hypothesis Confirmation
* **Slide Title**: Model Results Evaluation - Hypothesis
* **Visual**: *Summary scorecards confirming Master Hypothesis $H_1$: Robustness target ($\text{MASE} < 0.700$ met by Model 2 & 3), Resilience target ($R \approx 1.00, \text{TTR} < 4.0\text{h}$ met exclusively by Model 3), Generalizability target ($\text{RTR} \approx 1.00, \Delta\text{MASE} \le 10\%$ met exclusively by Model 1).*
* **Pacing**: 21:30 – 22:15 (Duration: 45s | Running Total: 22:15)

> "Slide 25 formalizes the verification of our research hypotheses:
> 
> * **Hypothesis 1(a) (Robustness)** is **CONFIRMED**: Both Model 2 and Model 3 successfully satisfy the stated target ($\text{MASE}_{\text{routine}} < 0.700$), achieving 0.680 and 0.662 respectively.
> * **Hypothesis 1(b) (Resilience)** is **CONFIRMED**: Model 3 exclusively satisfies the resilience threshold ($R_{\text{MASE}} = 1.05 \le 1.15$ and $\text{TTR} = 2.8\text{h} < 4.0\text{h}$), while unassisted machine learning experiences fragile collapse ($R = 2.14$).
> * **Hypothesis 1(c) (Generalizability)** is **CONFIRMED**: Model 1 exclusively satisfies the spatial transfer thresholds ($\text{RTR} = 1.04 \le 1.05$ and $\Delta\text{MASE} = +4.0\% \le 10.0\%$), while the hybrid architecture incurs a prohibitive 21.5% transfer penalty.
> 
> Master Hypothesis $H_1$ is thus fully substantiated: model superiority is strictly context-dependent."

---

## Phase VI: Discussion, Application & Conclusion (Slides 26–31 | 22:15 – 25:00)

### Slide 26: Discussion and Analysis of Results
* **Slide Title**: Discussion and Analysis of Results
* **Visual**: *Underlying causal mechanisms: Spatial architecture and passenger dynamics, connecting passenger shielding, terminal complex aggregation, and Type I vs. Type II layout invariance ($D = 0.032, p = 0.28$).*
* **Pacing**: 22:15 – 23:00 (Duration: 45s | Running Total: 23:00)

> "Chapter V investigates the underlying operational and behavioral mechanisms driving these empirical results:
> 
> 1. **Connecting Passenger Shielding**: Airside transfers deplane and board connections without crossing security checkpoints. Failure to apply DB1B ticket deflation distorts landside arrival curves by over 50%.
> 2. **Layout Invariance**: A two-sample Kolmogorov-Smirnov test between physically separate concourses (Type I) and airside-connected concourses (Type II) yielded $D = 0.032, p = 0.28$, mathematically proving that terminal screening queues are governed by carrier flight bank timing rather than physical concourse connectors.
> 3. **The Empty Checkpoint Fallacy Mechanism**: Decision trees overfit to negative correlation between flight cancellations and scheduled gate departures, producing catastrophic demand under-predictions during severe convective ground stops unless corrected by live floor error feedback."

---

### Slide 27: Real World Application
* **Slide Title**: Real World Application
* **Visual**: *The Disruption-Adaptive Checkpoint Forecasting Playbook (Dual-Track Policy): Track A (Disruption Resilience / Model 3) vs. Track B (Zero-Shot Portability / Model 1). Dynamic Staffing Safety Cushion under Kingman's formula.*
* **Pacing**: 23:00 – 23:45 (Duration: 45s | Running Total: 23:45)

> "To bridge the gap between academic econometrics and terminal operations, we translate our findings into **The Airport Operator's Playbook: A Dual-Track Policy**:
> 
> * **Track A (Resilience & Tactical Disruption Control)**: Deployed at mature, sensorized hub checkpoints equipped with automated wait-time sensors. During convective storm ground stops, the framework executes **Model 3 (Dynamic Hybrid)**, utilizing live floor error feedback ($e_{t-1}$) to track stranded passengers and maintain error bounds ($R_{\text{MASE}} = 1.05$).
> * **Track B (Zero-Shot Portability & Rapid Rollouts)**: Deployed at non-sensorized regional spoke airports or newly commissioned terminal concourses. The framework executes **Model 1 (Deterministic Flight Schedule)**, providing out-of-the-box accuracy without requiring historical retraining or sensor feeds ($\text{RTR} = 1.04$).
> 
> Furthermore, we translate volatility forecasts directly into required screening lanes using the **Volatility-Buffered Dynamic Lane Dimensioning Rule**:
> 
> $$c^* = \left\lceil \frac{\lambda}{\mu} + z_{1-\alpha} \sqrt{\frac{\lambda (C_a^2 + C_s^2)}{2}} \right\rceil$$
> 
> Under Kingman's law, dynamic safety buffers scale directly with arrival burstiness ($C_a$), preventing exponential queue wait-time escalation during flight delay cascades."

---

### Slide 28: Recommendations for Future Research
* **Slide Title**: Recommendations for future research
* **Visual**: *Four forward-looking research avenues: Airline-specific show-up curves, live external telemetry (rideshare / online search), lane-level granularity (PreCheck vs. Standard), and multi-horizon hybrid deep learning.*
* **Pacing**: 23:45 – 24:15 (Duration: 30s | Running Total: 24:15)

> "We recommend four high-priority avenues for future research:
> 
> 1. **Carrier-Specific Show-Up Curves**: Developing airline-specific passenger arrival distributions to account for loyalty tier differences between low-cost carriers and legacy network airlines.
> 2. **High-Frequency External Telemetry**: Integrating real-time municipal highway traffic, rideshare dispatch volumes, and mobile search queries to capture passenger lead-time adjustments prior to airport arrival.
> 3. **Sub-Lane Granularity**: Disaggregating checkpoint throughput by lane designation, explicitly modeling flow differences across TSA PreCheck, Standard screening, and CLEAR lanes.
> 4. **Multi-Horizon Neural Hybrids**: Exploring graph neural networks coupled with state-space filters across rolling multi-hour prediction horizons."

---

### Slide 29: Conclusion & Final Remarks
* **Slide Title**: Conclusion & Final Remarks
* **Visual**: *The Four Core Thesis Contributions: Volatility Paradigm Pivot, 4-Tier Filtering Pipeline, Proof of Asymmetric Trade-Offs ($H_1$), and The Operator's Decision Playbook.*
* **Pacing**: 24:15 – 24:45 (Duration: 30s | Running Total: 24:45)

> "In conclusion, this thesis delivers four foundational contributions to commercial aviation analytics:
> 
> 1. **The Volatility Paradigm Shift**: We proved that airport checkpoint queuing delays are governed by passenger arrival volatility ($CV_{\text{TSA}}$), not static volume headcounts, aligning terminal forecasting with heavy-traffic queuing theory.
> 2. **Methodological Cohort Isolation**: Our four-tier filtering pipeline successfully isolated 12 carrier-exclusive screening complexes, overcoming the Hub Disconnect and multi-carrier passenger mixing.
> 3. **Proof of Asymmetric Trade-Offs**: We empirically confirmed Master Hypothesis $H_1$, proving that while Model 3 wins Disruption Resilience, Model 1 wins Zero-Shot Generalizability, and Model 2 wins Routine Pareto Efficiency.
> 4. **Actionable Operations**: We provided airport operators with a dual-track decision playbook and a volatility-buffered lane dimensioning rule, transforming airport checkpoint management from reactive firefighting to resilient operational synchronization."

---

### Slide 30: Tables: Data Overview
* **Slide Title**: Tables: Data Overview
* **Visual**: *Master Data Warehouse Overview (`Picture 4`): 67.2M raw records conformed into Star Schema; Top 25 airfields; 9-airport experimental cohort; 16 standardized APA 7 tables synchronized across CSV and Excel workbooks.*
* **Pacing**: 24:45 – 25:00 (Duration: 15s | Running Total: 25:00)

> "Slide 30 provides the master data overview of our research repository: synthesizing 67.2 million raw federal records across TSA, BTS OTP, T-100, and DB1B into conformed analytical dimensions, fully documented across 16 synchronized APA 7th Edition tables and companion Excel workbooks."

---

### Slide 31: Closing Slide / Q&A Opening
* **Slide Title**: Slide 31
* **Visual**: *Closing acknowledgments, research repository citations, and formal invitation for Committee Oral Examination questions.*
* **Pacing**: 25:00 (Presentation Concludes | Transition to Oral Examination)

> "Thank you to my committee chair, committee members, and the faculty of Embry-Riddle Aeronautical University for your guidance and support throughout this research. 
> 
> That concludes my formal 25-minute presentation, and I am now ready for your questions."

---

## Defense Q&A Strategy & Anticipated Committee Questions (Pro-Tips)

### Question 1: "Why evaluate throughput volatility rather than raw passenger volume?"
* **Candidate Defense Script**:  
  > *"Under Kingman's heavy-traffic queuing formula, queue wait times scale quadratically with arrival volatility ($C_a^2$) as utilization approaches capacity ($\rho \to 1.0$). In our empirical data across the Top 25 airfields, static 24-hour headcounts show zero correlation with flight delays ($r = -0.062, p = 0.77$). Conversely, throughput volatility ($CV_{\text{TSA}}$) is tightly coupled with departure delay volatility ($r = +0.4373, p < 0.05$). Focusing on volatility directly addresses what causes checkpoint queue collapses."*

### Question 2: "Why does unconstrained Machine Learning collapse during severe flight disruptions?"
* **Candidate Defense Script**:  
  > *"This is the **Empty Checkpoint Fallacy**. When summer thunderstorms trigger severe ground stops, airline feeds report cancelled departures. Decision trees observe cancelled flights and infer that passenger demand has vanished, predicting near-zero throughput. In reality, thousands of stranded passengers remain in terminal lobbies seeking rebooking. Pure ML predicts empty checkpoints right when crowding is at its worst ($R_{\text{MASE}} = 2.14$). In Model 3, live 1-step error innovation feedback ($e_{t-1}$) detects stranded passengers on the floor, immediately overriding stale schedules."*

### Question 3: "Why does the Deterministic Schedule model outperform the Hybrid model on Generalizability?"
* **Candidate Defense Script**:  
  > *"Model 1 relies strictly on scheduled flight banks convolved across empirical show-up curves deflated by DB1B ticket ratios. These physical operational relationships are invariant across airport facilities ($\text{RTR} = 1.04, \Delta\text{MASE} = +4.0\%$). Conversely, Model 3's decision trees overfit to local taxiway geometry, gate layouts, and carrier banking structures at Newark, incurring an elevated 21.5% transfer penalty when deployed zero-shot to LaGuardia without local retraining."*

### Question 4: "Why exclude COVID-19 pandemic data (2020–2021) from model training?"
* **Candidate Defense Script**:  
  > *"COVID-19 induced severe, non-stationary structural breaks in passenger arrival lead times and screening lane procedures. A formal Chow structural break test on our demarcation cutoff (May 1, 2022) yielded $F = 1.42, p = 0.18$, confirming time-series stability across our 44-month post-pandemic window. Including 2020–2021 data introduces severe non-stationary bias that distorts modern operational staffing models."*
