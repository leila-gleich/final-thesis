# Academic & Operational Guide: Replacing Jargon and Buzzwords with Defensible Aviation Terminology

**Author**: Leila Gleich  
**Institution**: Embry-Riddle Aeronautical University  
**Degree**: Master of Science in Aeronautics / Aviation Data Analytics  
**Document Purpose**: Reference guide for translating overcomplicated mathematical, machine learning, and engineer-speak jargon into standard, publishable transportation operations terminology across Chapters IV, V, and journal manuscripts.

---

## 1. Executive Rationale & Motivation

In aviation and transportation research, human passengers do not follow the laws of physics or classical mechanics; they follow **human behavioral patterns and airport queueing dynamics**. 

Over-mathematizing or using machine learning buzzwords creates three significant risks during your thesis defense and peer review:
1. **The 'Physics' Trap**: Calling passenger arrival behavior 'physics-based' or 'physics-informed' prompts committee members and journal reviewers to ask, *"Where are the physical laws, Navier-Stokes equations, or conservation of momentum?"*
2. **Reviewer Skepticism**: Reviewers at premier aviation journals (e.g., *Journal of Air Transport Management*, *Transportation Research Part C/E*, *Transportation Research Board*) strongly favor simple, intuitive, and practically useful solutions over artificial algorithmic complexity.
3. **Loss of Operational Credibility**: Airport Federal Security Directors (FSDs), airline hub managers, and FAA planners reject black-box buzzwords. Grounding your methodology in standard aviation literature (such as **ACRP Report 40: Airport Passenger Terminal Planning and Design**) immediately establishes domain mastery.

By stripping out pseudo-mathematical buzzwords and adopting clean transportation terms, **your methodology becomes clearer, more credible, and significantly easier to publish**.

---

## 2. Master Thematic Replacement Tables

### Category A: Model Mechanics & Feature Engineering

| Overcomplicated Jargon / Buzzword (Do NOT Use) | Clean Aviation Term (Recommended for Thesis & Publication) | Plain-English Operational Meaning |
| :--- | :--- | :--- |
| **Physics-based continuous arrival kernel convolution** | **Empirical Passenger Show-Up Curve** or **Lead-Lag Passenger Arrival Distribution** | Passengers arrive at security 1.5 to 3 hours before their scheduled flight departure (standard ACRP Report 40 terminology). |
| **Orthogonal Wiener-Hopf deconvolution operator** | **Carrier Checkpoint Isolation** | In dedicated single-airline terminals, flight schedules map directly to security lines without confusion from other airlines. |
| **Cyber-physical hybrid architecture** | **Two-Stage Hybrid Model** | A sequential model that combines a baseline flight schedule with a decision tree to catch real-time flight delays. |
| **Parameter exchangeability across carrier kernels** | **Consistent Passenger Arrival Timing** | Legacy carrier passengers follow similar arrival timing, whereas Southwest passengers arrive on a different schedule due to open seating and two free checked bags. |
| **DB1B transfer deflation manifold** | **Connecting Passenger Deflator** or **Local Originating Passenger Fraction** | Multiplying flight seats by $(1 - \text{Connecting Ratio})$ to subtract the 50% to 75% of hub passengers who merely transfer airside and never enter TSA security. |

---

### Category B: Airport Geometry & Terminal Filtering

| Overcomplicated Jargon / Buzzword (Do NOT Use) | Clean Aviation Term (Recommended for Thesis & Publication) | Plain-English Operational Meaning |
| :--- | :--- | :--- |
| **Type I (air-gapped) vs. Type II (airside connected) complexes** | **Physically Separate Terminals vs. Walkway-Connected Terminals** | Some terminals are completely separate buildings (e.g., LGA, DTW); others connect post-security behind TSA (e.g., DFW, LAX). |
| **Inter-terminal airside passenger leakage / cross-contamination** | **Post-Security Terminal Cross-Over** | Passengers clearing checkpoint Terminal A to board a flight out of gate Terminal B. |
| **Heavy-traffic asymptotics and boundary saturation ($\rho \to 1.0$)** | **Peak-Hour Checkpoint Congestion** | High-volume flight banks where passenger arrival rates approach screening lane capacity, causing queues to form. |
| **The Connecting Passenger Paradox** | **The Hub Disconnect** or **Connecting vs. Local Originating Disconnect** | The common planning mistake of assuming every departing airline seat represents a person entering landside airport security. |

---

### Category C: Performance Dimensions & Evaluation Metrics

| Overcomplicated Jargon / Buzzword (Do NOT Use) | Clean Aviation Term (Recommended for Thesis & Publication) | Plain-English Operational Meaning |
| :--- | :--- | :--- |
| **Continuous Static Stability (Hypothesis 1 & 2)** | **Routine Operational Accuracy** | How accurately the model forecasts on normal, sunny days with on-time flights. |
| **System Shock Absorption & Disruption Dynamics (Hypothesis 3)** | **Resilience Under Disruption** | How well the model maintains accuracy during severe weather, cascading flight delays, and cancellations. |
| **Spatial Layout Transferability** | **Cross-Airport Transferability** | Can a model calibrated on one airport be deployed to an unfamiliar airport without site-specific retraining? |
| **Resilience Multiplier ($R_{\text{MASE}}$)** | **Disruption Error Multiplier** | The ratio of storm error to normal error; shows whether errors double during disruptions or remain stable. |
| **Relative Transfer Ratio (RTR)** | **Transfer Error Penalty** | The percentage increase in forecast error when deploying the model zero-shot to a new airport. |
| **Diebold-Mariano test of superior predictive ability** | **Statistical Test for Forecast Improvement** | Formal hypothesis test proving that the hybrid model's 14% error reduction wasn't due to random chance ($p < 0.0001$). |

---

### Category D: Data Engineering & Pre-Processing

| Overcomplicated Jargon / Buzzword (Do NOT Use) | Clean Aviation Term (Recommended for Thesis & Publication) | Plain-English Operational Meaning |
| :--- | :--- | :--- |
| **Temporal Demarcation Regime** | **Post-COVID Study Period** or **Training Window Start Date** | Explaining why training begins on May 1, 2022 (after federal transportation mask mandates were lifted). |
| **Sensor dropouts vs. structural zeros** | **Nighttime Checkpoint Closures vs. Missing Data** | Checkpoints close between midnight and 4:00 AM; these are real physical zeros, not broken sensors. |
| **Phantom composite mega-airport aggregation** | **Unidentified Airport Records** | Blank airport codes in raw TSA logs that were quarantined so they wouldn't distort national totals. |
| **Zero lookahead leakage** | **Strict Information Causality** | Only feeding the model information that airport managers actually know in advance (yesterday's schedule, prior-hour delay). |
| **Heteroskedastic Tweedie deviance minimization ($p = 1.3$)** | **Zero-Bounded Count Regression** | Ensuring predicted passenger counts can never be negative and accounting for wider variance during peak hours. |

---

## 3. Concrete 'Before & After' Manuscript Examples

### Example 1: Describing the Core Methodology (Abstract & Methodology)
* **Before (Overcomplicated Jargon)**:  
  *"This research formulates an orthogonal Wiener-Hopf deconvolution pipeline utilizing continuous physics-based lognormal arrival kernels and DB1B transfer deflation manifolds to map scheduled departures to TSA security throughput."*
* **After (Clean & Publishable)**:  
  *"This research develops a data-driven forecasting framework that shifts scheduled flight departures into empirical passenger show-up curves (peaking 90 to 120 minutes prior to takeoff) and deflates seat capacity by hub connecting ratios to isolate true landside security demand."*

### Example 2: Justifying Gradient-Boosted Decision Trees Over Neural Networks
* **Before (Overcomplicated Jargon)**:  
  *"Rather than utilizing deep cyber-physical recurrent architectures, a multi-quantile gradient boosting regressor was implemented to resolve non-linear manifold transitions and preserve zero boundary asymptotics without gradient explosion on severe weather delay outliers."*
* **After (Clean & Publishable)**:  
  *"Rather than deploying opaque deep neural networks, Gradient-Boosted Decision Trees were selected. Decision trees naturally handle non-linear operational dynamics—such as cascading flight delays—while respecting zero-throughput nighttime closures and providing transparent feature attribution for airport operational planning."*

### Example 3: Discussing Performance Under Disruption (Chapter V Analysis)
* **Before (Overcomplicated Jargon)**:  
  *"Under acute stochastic perturbation regimes ($T_{shock}$), the sequential cyber-physical framework exhibited superior shock absorption, restricting the resilience error multiplier to $R_{\text{MASE}} = 0.88$."*
* **After (Clean & Publishable)**:  
  *"During severe operational disruptions (hours with 45+ minute flight delays or multiple cancellations), the two-stage hybrid model proved highly resilient, maintaining a disruption error multiplier of $0.88$ and avoiding the severe underprediction typical of status-quo flight schedules."*

---

## 4. Where the Previous Findings Outline Files Are Stored

For full transparency, the previous outline files were archived during workspace reorganization:
* **Current Location**: `Gleich-Thesis/archive/early_walkthroughs_and_notes/findings_outline_staging/`
* **Contents Preserved**: All 6 text outline documents (`00_Findings_Outline_Master_Overview.txt`, `Section_1` through `Section_5`) and all 16 companion CSV files (`Section_1A` through `Section_5B`).

---

## 5. Summary Recommendation for Your Committee & Publishing

1. **Keep the Math Rigorous in Equations & Appendices**: Your lognormal formulas, SARIMA formulations, and Diebold-Mariano test equations should remain mathematically precise.
2. **Use Clear Aviation English in the Prose**: In your chapter narrative, talk about **flights, delays, passenger show-up curves, and connecting passengers**.
3. **The Core Contribution is Clear & Simple**: Current airport planning ignores passenger arrival timing and counts connecting passengers who never enter security. Simply fixing those two factors cuts checkpoint forecast error by **14.2%** and explains **62.7% of all throughput variance**.
