# Master Defense Presentation Script: 25-Minute Oral Examination
**Candidate**: Leila Gleich  
**Degree**: Master of Science in Aeronautics (MSAA / Gleich 700B)  
**Institution**: Embry-Riddle Aeronautical University  
**Thesis Title**: *Evaluating Predictive Techniques to Model Stochastic Airport Passenger Flow*  
**Duration**: Exactly 25 Minutes (Paced at ~130–140 words per minute; ~3,400 words total)  
**Companion Slide Deck**: `Thesis-Defense.pptx` (32 Slides)

---

## Pacing & Timing Blueprint (25-Minute Breakdown)

| Segment | Slides | Topic / Focus | Target Time Window | Cumulative Elapsed |
| :--- | :--- | :--- | :--- | :--- |
| **I. Introduction & Theoretical Foundation** | Slides 1–7 | Problem, Purpose, Research Question, Hypotheses, 3 Dimensions | 0:00 – 4:30 | 4 min 30 sec |
| **II. Literature Review & Theoretical Evolution** | Slides 8–15 | Literature Gaps, Micro-simulation, ML, Hybrid, Volatility Need | 4:30 – 8:30 | 8 min 30 sec |
| **III. Methodology & Econometric Data Pipeline** | Slides 16–20 | 4-Phase Pipeline, 4-Tier Funnel, Hub Disconnect, Carrier Isolation | 8:30 – 13:00 | 13 min 00 sec |
| **IV. Empirical Findings & Data Explorations** | Slides 21–24 | Top 25 vs 9-Airport Cohort, Seasonal Regimes, Diurnal Dual-Peaks | 13:00 – 16:30 | 16 min 30 sec |
| **V. Model Execution & Multi-Pillar Hypothesis Testing** | Slides 25–28 | 4 Paradigms, Robustness, Resilience (IROPS), Generalizability | 16:30 – 21:00 | 21 min 00 sec |
| **VI. Operational Synthesis, Real-World Application & Conclusion** | Slides 29–32 | Conformal Buffers, Dynamic Rostering, Future Work, Final Takeaway | 21:00 – 25:00 | 25 min 00 sec |

---

## Segment I: Introduction, Research Problem & Hypothesis (Slides 1–7 | 0:00 – 4:30)

### Slide 1: Title Slide
* **Time**: 0:00 – 0:45 (Elapsed: 0:45)
* **Visual**: *Title, Author (Leila Gleich), Committee, Embry-Riddle Aeronautical University logo.*

> "Good morning, esteemed committee members, faculty, and colleagues. Welcome to my graduate thesis defense. 
> 
> My research is entitled: *Evaluating Predictive Techniques to Model Stochastic Airport Passenger Flow*. 
> 
> In this study, we bridge a critical gap between commercial airline airside operations and terminal landside security screening. Specifically, we investigate how predictive modeling paradigms—spanning deterministic airline flight schedules, supervised machine learning, and dynamic hybrid architectures—perform when forecasting the volatility of TSA passenger screening throughput across complex commercial hub airports."

---

### Slide 2: Outline
* **Time**: 0:45 – 1:15 (Elapsed: 1:15)
* **Visual**: *Six core sections: Problem & Purpose, Literature, Methodology, Data Findings, Model Evaluation, and Operational Recommendations.*

> "Our presentation today is organized into six core sections. We will establish the operational queuing problem in terminal screening; trace the theoretical evolution from deterministic curves to hybrid models; detail our rigorous four-tier data filtering pipeline across federal data assets; explore empirical volatility dynamics; evaluate the models across a three-pillar performance framework; and conclude with actionable policy recommendations for airport operators and the Transportation Security Administration."

---

### Slide 3: The Research Problem
* **Time**: 1:15 – 2:00 (Elapsed: 2:00)
* **Visual**: *Airport passenger flow stochasticity, Kingman's formula diagram, queue buildup.*

> "Commercial airport passenger flow is inherently stochastic. While flight schedules are published months in advance, passenger arrivals at security checkpoints exhibit heavy tail volatility driven by connecting itineraries, surface traffic, and flight delays. 
> 
> Under Kingman’s heavy-traffic approximation from queueing theory, checkpoint waiting times do not scale linearly with passenger volume—they scale quadratically with the coefficient of variation of arrivals ($C_a^2$) as checkpoint lane utilization approaches capacity ($\rho \to 1.0$). 
> 
> Historically, the TSA and airport operators have staffed screening checkpoints using static historical passenger volume tables. When sudden flight delay cascades or weather shocks hit, physical screening capacity cannot expand in real time. The result is terminal queuing fragility: catastrophic wait times, missed departures, and severe security lane misallocations."

---

### Slide 4: Research Purpose
* **Time**: 2:00 – 2:45 (Elapsed: 2:45)
* **Visual**: *Modeling Throughput Volatility vs. Volume; Evaluative Contexts.*

> "The core purpose of this thesis is twofold:
> 
> First, to shift the modeling paradigm away from predicting raw static passenger headcounts, and instead model and forecast **throughput volatility**—captured by the hourly standard deviation ($\sigma_{\text{TSA}}$) and the scale-free coefficient of variation ($CV_{\text{TSA}}$). 
> 
> Second, to establish an empirical framework that evaluates *which* predictive modeling architecture is best suited for specific operational circumstances, demonstrating that model selection must be conditioned on distinct operational priorities rather than a single global error metric."

---

### Slide 5: Research Question
* **Time**: 2:45 – 3:30 (Elapsed: 3:30)
* **Visual**: *The overarching research question broken down across the 3 dimensions.*

> "This leads directly to our central research question:
> 
> *Which predictive modeling frameworks—spanning deterministic persistence controls, deterministic schedule baselines, supervised machine learning, and dynamic two-stage hybrids—are most effective for forecasting airport passenger security screening throughput volatility when prioritizing:*
> 1. *Robustness (routine operational accuracy under nominal conditions),*
> 2. *Resilience (stability under irregular operations and severe convective weather disruptions), or*
> 3. *Generalizability (zero-shot spatial portability across unfamiliar airport terminal geometries) as the primary operational evaluation metric?*"

---

### Slide 6: Master Hypothesis ($H_1$) & Sub-Hypotheses
* **Time**: 3:30 – 4:15 (Elapsed: 4:15)
* **Visual**: *The Asymmetric Trade-Off ($H_1$) and $H_{1a}, H_{1b}, H_{1c}$.*

> "We formulate our primary hypothesis as **The Asymmetric Trade-Off ($H_1$)**:
> *Across the candidate modeling paradigms evaluated, no individual approach will prove universally superior across all three performance measures.*
> 
> Specifically:
> * Under $H_{1a}$ for **Robustness**, Supervised Machine Learning (Model 2) and Dynamic Hybrids (Model 3) will satisfy the routine accuracy target ($\text{MASE} < 0.700$), outperforming deterministic schedules.
> * Under $H_{1b}$ for **Resilience**, the Dynamic Two-Stage Hybrid (Model 3) will be the sole architecture to maintain stability during severe convective disruptions ($R_{\text{MASE}} \approx 1.00$), while pure machine learning will suffer severe performance degradation.
> * Under $H_{1c}$ for **Generalizability**, the Deterministic Flight Schedule Model (Model 1) will achieve the spatial transferability target ($\Delta\text{MASE} \le 10\%$), whereas complex models will fail due to terminal layout overfitting."

---

### Slide 7: Dynamic Performance Measures Framework
* **Time**: 4:15 – 4:30 (Elapsed: 4:30)
* **Visual**: *Trio diagram: Robustness, Resilience, Generalizability.*

> "To test these hypotheses rigorously, we establish this three-dimensional evaluation trio: Robustness measures routine baseline fit; Resilience measures recovery under shock states; and Generalizability measures spatial transportability without retraining."

---

## Segment II: Literature Review & Theoretical Foundations (Slides 8–15 | 4:30 – 8:30)

### Slide 8: Literature Overview
* **Time**: 4:30 – 5:00 (Elapsed: 5:00)
* **Visual**: *Literature review domain map.*

> "Our review of existing literature synthesized six distinct operational domains: traditional deterministic models, discrete-event simulation, advanced machine learning, hybrid cyber-physical architectures, post-pandemic demand shifts, and multi-dimensional performance evaluation."

---

### Slide 9: Literature Gap: The Volatility Problem
* **Time**: 5:00 – 5:30 (Elapsed: 5:30)
* **Visual**: *Comparison of static volume vs. variance clustering in literature.*

> "Existing airport throughput studies have overwhelmingly treated passenger arrivals as static, deterministic aggregates. While econometric gravity models and flight schedule convolutions capture baseline volume, they systematically overlook arrival variance. In heavy-traffic queues, variance—not volume—causes congestion."

---

### Slide 10: Traditional Models: Deterministic Schedules & Classic Queueing
* **Time**: 5:30 – 6:00 (Elapsed: 6:00)
* **Visual**: *ACRP Report 40 curves and classic M/M/s models.*

> "Early terminal planning relied on ACRP Report 40 passenger show-up curves convolved against scheduled flight banks. While computationally trivial and transparent, deterministic models make a fatal assumption: that flights depart exactly on time and passengers adhere to static show-up profiles. When operational delay propagation occurs, deterministic schedules collapse."

---

### Slide 11: The Shift to Micro-Simulation
* **Time**: 6:00 – 6:30 (Elapsed: 6:30)
* **Visual**: *Agent-based simulation strengths vs. real-time computational barriers.*

> "To capture stochasticity, researchers turned to discrete-event and agent-based micro-simulation (such as Simio or CAST). While simulation excels at granular terminal geometry modeling, it suffers from two decisive operational shortcomings: high calibration overhead and extreme computational latency. Airport operations centers cannot re-run micro-simulations dynamically during fast-moving convective ground stops."

---

### Slide 12: Advanced Predictive Machine Learning
* **Time**: 6:30 – 7:00 (Elapsed: 7:00)
* **Visual**: *Supervised regression trees, gradient boosting, and black-box limitations.*

> "The advent of machine learning introduced decision trees and gradient boosting, capturing nonlinear airside interactions like taxi-out delays and weather metrics. However, pure supervised machine learning suffers from historical bias and regime brittleness. Under severe irregular operations (IROPS), ML models often misinterpret cancelled or delayed flights, leading to extreme forecast breakdowns."

---

### Slide 13: Hybrid Predictive Architectures
* **Time**: 7:00 – 7:30 (Elapsed: 7:30)
* **Visual**: *Sequential two-stage architecture: Base schedule model + dynamic error innovation.*

> "To combine the stability of physics-based domain schedules with machine learning flexibility, recent literature proposed hybrid architectures. In our framework, we implement a sequential two-stage hybrid: Stage 1 establishes the recurring flight-schedule baseline, while Stage 2 injects live, 1-step error innovation feedback ($e_{t-1} = y_{t-1} - \hat{y}_{t-1}$) from the physical checkpoint floor."

---

### Slide 14: Post-Pandemic Volatility & Structural Demarcation
* **Time**: 7:30 – 8:00 (Elapsed: 8:00)
* **Visual**: *2022–2025 timeline; macro demand recovery shifts.*

> "The post-pandemic recovery fundamentally restructured commercial aviation passenger behavior. Business travel patterns shifted, remote check-in expanded, and airline scheduling practices evolved. Consequently, training models across 2020–2021 data contaminates algorithms with artificial structural shocks. Our research enforces a strict post-pandemic boundary, calibrating models exclusively across 2022 through 2025."

---

### Slide 15: The Imperative for Dynamic Multi-Pillar Measures
* **Time**: 8:00 – 8:30 (Elapsed: 8:30)
* **Visual**: *Single metric pitfalls (RMSE) vs. Multi-Pillar trade-offs.*

> "Finally, the literature revealed an evaluative deficiency: researchers traditionally rely on a single global error metric like $R^2$ or RMSE. In airport operations, an algorithm with the lowest annual RMSE may completely fail during a severe convective ground stop. We require dynamic performance measures that evaluate models across distinct operational regimes."

---

## Segment III: Methodology & Econometric Data Pipeline (Slides 16–20 | 8:30 – 13:00)

### Slide 16: Methodology Overview
* **Time**: 8:30 – 9:00 (Elapsed: 9:00)
* **Visual**: *Methodological pillars: Data, Filtering, Modeling, and Evaluation.*

> "Moving into Chapter III: our methodology is structured into four sequential phases: multi-source federal data ingestion and ETL; four-tier econometric filtering; candidate model execution; and multi-dimensional hypothesis evaluation."

---

### Slide 17: Modeling Paradigms & The Evaluative Trio
* **Time**: 9:00 – 9:45 (Elapsed: 9:45)
* **Visual**: *The 4 Model Candidates benchmarked across Robustness, Resilience, Generalizability.*

> "We evaluate exactly three candidate models representing fundamentally distinct paradigms, benchmarked against an empirical control:
> 1. **Baseline Control**: The naive persistence benchmark ($\hat{y}_t = y_{t-24}$, fixed at $\text{MASE} \equiv 1.000$).
> 2. **Model 1 (Deterministic)**: Flight schedule convolution using empirical show-up curves across $t+1, t+2,$ and $t+3$ lead hours.
> 3. **Model 2 (Supervised Machine Learning)**: Decision-tree regressor incorporating flight bank schedules and 24 BTS OTP operational attributes.
> 4. **Model 3 (Dynamic Two-Stage Hybrid)**: Coupling deterministic schedule baselines with real-time prior-hour error feedback from the checkpoint floor."

---

### Slide 18: Design and Procedures: The Four-Phase Architecture
* **Time**: 9:45 – 10:30 (Elapsed: 10:30)
* **Visual**: *Table 3.1: Phase 1 (ETL), Phase 2 (Filtering), Phase 3 (Modeling), Phase 4 (Evaluation).*

> "Our data foundation unifies 67.2 million raw records down to 42.1 million conformed records across three authoritative federal databases: TSA hourly throughput telemetry, Bureau of Transportation Statistics On-Time Performance (BTS OTP), and BTS DB1B origin-and-destination passenger surveys.
> 
> To prevent data leakage, we enforce a strict 7-day, 168-hour purge buffer between training (2022–2024) and our 2025 out-of-time holdout set, completely eliminating autoregressive contamination."

---

### Slide 19: Methodological Milestones: The Hub Disconnect & Carrier Isolation
* **Time**: 10:30 – 11:45 (Elapsed: 11:45)
* **Visual**: *BTS DB1B Connecting Passenger Deflator formula & Carrier Checkpoint Isolation diagram.*

> "Our methodology resolves two fundamental domain challenges that have compromised prior literature:
> 
> First, **The Hub Disconnect**: At mega connecting hubs, up to 66% of passengers on departing aircraft never pass through TSA checkpoints—they arrive airside from inbound connecting flights. If you predict checkpoint demand directly from flight seat capacity, you massively over-predict. We introduce the **Connecting Passenger Deflator** using quarterly BTS DB1B coupon data, scaling flight capacity by true local originating proportions ($S_{\text{local}} = 1 - S_{\text{connecting}}$).
> 
> Second, **Carrier Checkpoint Isolation**: Standard multi-user terminals mix passengers from numerous airlines across shared security lanes, creating an unidentifiable econometric bottleneck. To solve this, our filtering algorithm isolates carrier-exclusive terminals where an individual carrier operates a dedicated checkpoint complex."

---

### Slide 20: The Four-Tier Filtering Funnel
* **Time**: 11:45 – 13:00 (Elapsed: 13:00)
* **Visual**: *Table 3.2 Funnel: Macro (450+ -> Top 25), Meso (25 -> 14), Micro (14 -> 10), Final Cohort (9 airfields, 12 complexes).*

> "To create an unconfounded experimental cohort, we developed a 4-tier purposive filtering funnel:
> * **Macro Tier**: Filtered 450+ US airfields down to the Top 25 large hubs representing 68% of commercial traffic.
> * **Meso Tier**: Screened for continuous operational presence across the Big Three legacy carriers (American, Delta, United). This eliminated JFK due to United’s permanent withdrawal in October 2022.
> * **Micro Tier**: Enforced strict physical checkpoint isolation, eliminating airports with consolidated central checkpoints where carrier flows mix (such as Salt Lake City).
> * **Cohort Tier**: Isolated a balanced 9-airport experimental cohort representing 12 carrier-exclusive screening complexes: Atlanta, Boston, Dallas/Fort Worth, Detroit, Newark, Los Angeles, LaGuardia, Chicago O'Hare, and Philadelphia."

---

## Segment IV: Empirical Findings & Data Explorations (Slides 21–24 | 13:00 – 16:30)

### Slide 21: Descriptive Statistics: 9-Airport Cohort vs. Top 25
* **Time**: 13:00 – 14:00 (Elapsed: 14:00)
* **Visual**: *Table 4.7 comparison table highlighting deltas.*

> "Examining our conformed data in Table 4.7 reveals why the 9-airport cohort represents an ideal stress test. 
> 
> Compared to the Top 25 national average, our 9-airport cohort exhibits:
> * 16.9% higher scheduled flight movements (224,576 annual flights),
> * 14.1% higher flight cancellation rates (1.63% vs. 1.43%),
> * 25.0% higher true local originating passenger volume (16.4 million vs. 13.1 million passengers), and
> * A 5.8% higher checkpoint demand volatility ($CV_{\text{TSA}} = 0.8728$ vs. $0.8250$).
> 
> This confirms that our experimental cohort represents highly congested, delay-prone operational environments governed by landside show-up dynamics rather than passive connecting transfers."

---

### Slide 22: Coupled Volatility: The Values vs. Volatility Discovery
* **Time**: 14:00 – 14:45 (Elapsed: 14:45)
* **Visual**: *Figure 1 Coupled Volatility Phase Space ($CV_{\text{TSA}}$ vs. $\sigma_{\text{delay}}$).*

> "Slide 22 presents one of the most critical econometric discoveries of this thesis: **The Values versus Volatility Coupling**.
> 
> When you perform regression between static passenger volumes and raw flight departure delays, the correlation is virtually non-existent ($r = -0.062, p = 0.77; R^2 = 2.5\%$). This explains why historical static models fail!
> 
> However, when we evaluate **volatility metrics**, checkpoint arrival volatility is tightly coupled with flight departure delay dispersion ($CV_{\text{delay}}: r = +0.4373, p < 0.05; R^2 = 19.1\%$). During peak summer convective periods, this Coupled Volatility Index surges by 41%, driving delay standard deviations up to 68.4 minutes. Congestion is driven by variance mismatch, not static levels."

---

### Slide 23: Macro Seasonal Regimes & Day-of-Week Cycles
* **Time**: 14:45 – 15:30 (Elapsed: 15:30)
* **Visual**: *Table 4.3b (4 Macro Seasons) and Figure 2 (Day-of-Week cycles).*

> "By clustering ISO weekly volatility profiles, we identified four distinct annual regimes: Off-Peak Winter, Mid-Peak Spring, Summer Convective Peak, and Holiday Peak. 
> 
> Day-of-week analysis reveals two contrasting operational archetypes: Monday exhibits an **outbound business surge** with massive early-morning TSA screening volume and minimal delays, whereas Sunday exhibits an **inbound leisure return surge**, where screening volumes remain high while downline flight delay standard deviations expand by over 35%."

---

### Slide 24: Diurnal Non-Consecutive Dual Peaks & Lead-Lag Dynamics
* **Time**: 15:30 – 16:30 (Elapsed: 16:30)
* **Visual**: *Diurnal Heatmap and Lead-Lag Transfer Table ($t+1, t+2, t+3$).*

> "At the hourly level, our data uncovered a **non-consecutive dual-peak phenomenon**:
> In the early morning (05:00–08:00), TSA screening volatility peaks at over 11,380 passengers per hour while flights depart with near-zero delays. Conversely, in the late afternoon and evening (14:00–22:00), screening volumes moderate, but departure delay dispersion spikes beyond 63 minutes due to network-wide aircraft turnaround erosion.
> 
> Modeling lead-lag cross-correlations proved that contemporaneous flight schedules fail to capture arrivals ($R^2 = 0.198$). Instead, passenger show-up curves peak precisely at a two-hour lead ($t+2$), where correlation surges to $R^2 = 0.498$."

---

## Segment V: Model Execution & Multi-Pillar Hypothesis Testing (Slides 25–28 | 16:30 – 21:00)

### Slide 25: Model Execution & Baseline Benchmarks
* **Time**: 16:30 – 17:15 (Elapsed: 17:15)
* **Visual**: *Table 4.10 Master Benchmark Matrix (2025 Holdout).*

> "Turning to model execution: all models were evaluated on the 2025 out-of-time holdout dataset across our 12 carrier-exclusive screening complexes.
> 
> As displayed in Table 4.10:
> * **Baseline Control** (naive persistence) produced a test RMSE of 253.6 pax/hr and MASE of 1.000.
> * **Model 1 (Deterministic Schedule)** achieved an RMSE of 313.4 pax/hr and MASE of 0.945, showing a persistent negative forecast bias (-42.1 pax/hr) because static curves fail during delay ripples.
> * **Model 2 (Machine Learning)** reduced RMSE to 273.5 pax/hr and achieved a MASE of 0.779.
> * **Model 3 (Dynamic Hybrid)** delivered the lowest overall test error: RMSE of 222.1 pax/hr, MAE of 142.8 pax/hr, and a MASE of 0.662."

---

### Slide 26: Dimension 1 (Robustness): Routine Operational Accuracy
* **Time**: 17:15 – 18:15 (Elapsed: 18:15)
* **Visual**: *Table 4.11 / Table 5.1 Robustness metrics under nominal conditions.*

> "Now we evaluate our primary hypothesis across the three operational pillars.
> 
> Under **Dimension 1: Robustness**, evaluated under nominal operations (delays $< 15$ minutes, zero cancellations):
> * Model 3 achieved the lowest absolute error ($\text{RMSE}_{\text{routine}} = 222.1$ pax/hr, $\text{MASE}_{\text{routine}} = 0.662$), comfortably beating the academic threshold of $\text{MASE} < 0.700$.
> * Model 2 achieved $\text{MASE} = 0.680\text{--}0.700$, also passing the target.
> * Diebold-Mariano tests confirm that both ML and Hybrid gains over deterministic baselines are highly statistically significant ($DM = 42.15$ and $48.72, p < 0.0001$).
> 
> This fully confirms **$H_{1a}$**: in routine daily flow, advanced predictive models successfully capture nominal passenger rhythms, with Model 2 delivering routine Pareto efficiency due to zero feedback compute latency."

---

### Slide 27: Dimension 2 (Resilience): Irregular Operations (IROPS) & The Empty Checkpoint Fallacy
* **Time**: 18:15 – 19:45 (Elapsed: 19:45)
* **Visual**: *Table 5.2 Resilience metrics: Shock RMSE, Disruption Multiplier ($R_{\text{MASE}}$), Time-to-Recovery (TTR).*

> "Under **Dimension 2: Resilience**, evaluated during severe irregular operations (delays $\ge 45$ minutes or cancellations $\ge 5$):
> 
> Here, pure machine learning experienced a catastrophic collapse. Model 2's Disruption Multiplier skyrocketed to **$R_{\text{MASE}} = 2.14$**—more than doubling its forecast error!
> 
> We identified the physical mechanism behind this failure as the **Empty Checkpoint Fallacy**:
> When convective storms ground flights, scheduled departures vanish from the electronic airline feed. The decision-tree regressor observes zero scheduled flights and predicts that the security checkpoint will be completely empty. In reality, thousands of passengers are already physically stranded inside terminal lobbies waiting for rescheduled flights.
> 
> In contrast, **Model 3 (Dynamic Two-Stage Hybrid) was the decisive winner**:
> It maintained a near-perfect Disruption Multiplier of **$R_{\text{MASE}} = 1.05$**, achieved the lowest shock error ($\text{MASE}_{\text{shock}} = 0.694$), and demonstrated a Time-to-Recovery of just **2.8 hours**, compared to 5.4 hours for Model 2 and 7.8 hours for Model 1. Live error feedback ($t-1$) allows Model 3 to observe stranded lobby volume, overriding stale schedules. This conclusively confirms **$H_{1b}$**."

---

### Slide 28: Dimension 3 (Generalizability): Zero-Shot Spatial Portability
* **Time**: 19:45 – 21:00 (Elapsed: 21:00)
* **Visual**: *Table 5.3 Generalizability metrics: EWR to LGA zero-shot transfer.*

> "Under **Dimension 3: Generalizability**, we tested zero-shot spatial portability: deploying models calibrated on United's hub at Newark (EWR Terminal C) directly to Delta's terminal at LaGuardia (LGA Terminal C) without local retraining.
> 
> Here, the hierarchy completely inverted:
> * **Model 1 (Deterministic Schedule) was the decisive winner**: Its Relative Transfer Ratio was **$\text{RTR} = 1.04$**, with a MASE degradation of only **$+4.0\%$**, easily satisfying our academic threshold ($\Delta\text{MASE} \le 10\%$). Deterministic show-up physics generalize across airports because passenger psychology remains invariant.
> * In contrast, **Model 3 decisively failed the generalizability target**: Its Relative Transfer Ratio degraded to **$\text{RTR} = 1.19$**, and its error increased by **$+21.5\%$** ($\Delta\text{MASE} = +0.142$). 
> 
> Why? The supervised decision trees overfit to Newark's specific terminal geometry, taxi-way configurations, and flight bank banking structures. This conclusively confirms **$H_{1c}$** and proves our overarching hypothesis **$H_1$**: *there is no universally dominant model*."

---

## Segment VI: Operational Synthesis, Real-World Application & Conclusion (Slides 29–32 | 21:00 – 25:00)

### Slide 29: Discussion & Operational Synthesis
* **Time**: 21:00 – 22:00 (Elapsed: 22:00)
* **Visual**: *Synthesis matrix showing trade-offs across layouts and operations.*

> "Synthesizing our empirical results: terminal spatial architecture dictates model efficacy.
> Connecting passenger shielding cushions security checkpoints from airside flight delays at fortress hubs like Atlanta and Dallas. Conversely, at high-originating facilities like LaGuardia and Newark, checkpoint throughput is acutely coupled with local landside access. 
> Model selection cannot follow a 'one-size-fits-all' mandate. Instead, airport operators must match modeling architectures to their terminal's connecting ratio and operational regime."

---

### Slide 30: Real-World Aviation Applications
* **Time**: 22:00 – 23:15 (Elapsed: 23:15)
* **Visual**: *Three implementation pillars: Dynamic Rostering, Connecting Ratio Deflation, Regime-Switched Engine.*

> "We translate these findings into three actionable operational recommendations:
> 
> 1. **Dynamic Checkpoint Rostering**: TSA federal security directors should abandon static time-of-day tables in favor of dynamic staffing schedules driven by empirical two-hour lead ($t+2$) flight bank schedules convolved with conformal staffing buffers.
> 2. **Connecting Ratio Integration**: Centralized security dispatchers must scale flight bank capacity by airline O&D survey ratios to eliminate chronic over-staffing at connecting fortress hubs.
> 3. **The Regime-Switched Gated Inference Engine**: Airport operations centers should implement a regime-switched architecture. During nominal, on-time conditions, deploy pure supervised machine learning (Model 2) for zero-latency, interpretable staffing. The instant convective ground stops or severe delays exceed 45 minutes, automatically switch to the Dynamic Two-Stage Hybrid (Model 3) to leverage live checkpoint floor feedback and prevent terminal gridlock."

---

### Slide 31: Recommendations for Future Research
* **Time**: 23:15 – 24:00 (Elapsed: 24:00)
* **Visual**: *Bullet points: Lane-level telemetry, TSA PreCheck vs. Standard, surface transit integration.*

> "For future aviation operations research, we propose three extensions:
> First, disaggregating throughput down to physical lane types—specifically evaluating split queue dynamics between TSA PreCheck, standard screening, and CLEAR lanes.
> Second, integrating real-time ground transportation telemetry, such as highway congestion indexes and parking shuttle sensor feeds, to capture landside transit delays.
> Third, evaluating multi-step ahead recursive forecasting architectures for rolling 4-to-6 hour operational horizons."

---

### Slide 32: Conclusion & Final Remarks
* **Time**: 24:00 – 25:00 (Elapsed: 25:00)
* **Visual**: *Core concluding takeaway: Transforming airport security from reactive queueing to proactive stochastic synchronization.*

> "In conclusion: this thesis demonstrates that airport passenger flow cannot be treated as a static volume exercise. Checkpoint congestion is governed by throughput volatility and arrival burstiness. 
> 
> By formalizing the Asymmetric Trade-Off ($H_1$), we proved that while deterministic physics generalize best across airports, and machine learning optimizes routine operations, dynamic two-stage hybrid models are indispensable for surviving convective disruptions and overcoming the Empty Checkpoint Fallacy.
> 
> By synchronizing airside flight schedules, connecting passenger deflators, and real-time floor telemetry, airports can transition security screening from reactive firefighting to resilient, proactive operational control.
> 
> Thank you for your time and guidance throughout this research. I now conclude my formal presentation."
