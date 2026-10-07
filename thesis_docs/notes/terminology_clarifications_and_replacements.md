# Academic Terminology Clarification and Replacement Guide
## De-Jargoning Core Concepts for Thesis Defense & Committee Review

* **Author**: Leila Gleich  
* **Institution**: Embry-Riddle Aeronautical University  
* **Degree**: Master of Science in Aeronautics (MSAA)  
* **Date**: October 6, 2026  
* **Companion CSV File**: [`thesis_docs/notes/terminology_replacements.csv`](file:///Users/leilagleich/Library/CloudStorage/OneDrive-Embry-RiddleAeronauticalUniversity/final-thesis/thesis_docs/notes/terminology_replacements.csv) | [`results/tables/terminology_replacements.csv`](file:///Users/leilagleich/Library/CloudStorage/OneDrive-Embry-RiddleAeronauticalUniversity/final-thesis/results/tables/terminology_replacements.csv)
* **Document Purpose**: Synthesizes the terminology clarifications and de-jargoning policies requested during manuscript refinement. This guide translates proprietary-sounding formulas, machine-learning buzzwords, and engineering/physics metaphors into rigorous, publishable commercial aviation operations and transportation econometrics terminology for Chapters I through V, as well as oral defense preparation before Embry-Riddle committee members who emphasize qualitative research, human traveler behavior, and practical airport management credibility.

---

## Executive Summary & Quick-Reference Cheat Sheet

The following master replacement table maps all 26 identified jargon terms, physical metaphors, and coined phrases to their recommended academic replacements, plain-English operational meanings, and qualitative committee rationale.

| Category | Draft Jargon / Coined Term | Recommended Academic Replacement | Plain-English Operational Reality | Why It Risks Committee Scrutiny |
| :--- | :--- | :--- | :--- | :--- |
| **Queuing & Physics** | **Heavy-Traffic Queuing Physics** | **Heavy-Traffic Queuing Principles** (or **Queuing Dynamics / Queuing Theory**) | Checkpoint wait times and delays scale quadratically with passenger arrival variance ($C_a^2$) as checkpoint utilization approaches capacity ($\rho \to 1.0$). | Prompts qualitative committee members to ask where the physical conservation laws or Navier-Stokes equations are; passengers are human travelers making cognitive choices. |
| **Model Baselines** | **Deterministic Physical Baseline (Model 1)** | **Deterministic Operational Baseline** | Published airline flight schedules shifted forward in time across empirical ACRP Report 40 passenger arrival distributions ($t+1, t+2, t+3$). | "Physical baseline" implies physical sensor modeling or physics-informed neural networks rather than schedule-driven terminal planning. |
| **Model Baselines** | **Physical Ebb and Flow / Physical Rules** | **Operational Ebb and Flow / Deterministic Operational Rules** | Concentrated surges and valleys in security arrivals caused by hub-and-spoke airline flight departure banks. | Conflates airline bank scheduling and passenger habits with physical forces or mechanics. |
| **Model Baselines** | **True Physical Lead-Lag Relationship** | **True Empirical Lead-Lag Relationship** (or **Operational Lead-Lag Offset**) | The observed time gap between when passengers clear security (90–120 min prior) and when flights push back from gates. | It is an empirically observed behavioral timeline in aviation data, not a physical law of nature. |
| **Terminal Geometry** | **Idiosyncratic Physical Geometry** | **Idiosyncratic Terminal Layouts and Gate Configurations** | Unique concourse layout, pier shapes, checkpoint locations, and gate distributions at an individual airport. | "Physical geometry" sounds like CAD engineering or fluid domain meshing rather than airport terminal planning. |
| **Terminal Geometry** | **Facility Physical Features** | **Facility and Aircraft Features** (or **Terminal Operational Features**) | Screening lane counts, checkpoint configurations, aircraft seat gauge, route load factors, and connecting ratios. | Over-emphasizes "physics" when referring to operational and equipment characteristics of commercial aviation. |
| **Terminal Geometry** | **Carrier Isolation Physically Impossible** | **Carrier Isolation Structurally / Operationally Impossible** | Consolidated central checkpoint halls (such as Salt Lake City) where all airlines mix into a single passenger screening line. | It is an architectural and operational design choice of the terminal, not an impossibility under physical laws. |
| **Data Hygiene** | **Physical Checkpoint Closures vs. Missing Sensor Data** | **Scheduled Checkpoint Closures vs. Missing Sensor Data** (or **Nighttime Closures**) | Zero throughput recorded between 00:00 and 04:00 because checkpoints are closed overnight by TSA policy. | Conflates administrative operating schedules with physical phenomenon; "sensor dropouts" implies faulty hardware. |
| **Model Architecture** | **Cyber-Physical Hybrid Model / Architecture** | **Dynamic Two-Stage Hybrid Model** (or **Sequential Two-Stage Hybrid**) | A sequential model coupling recurring daily flight schedule cycles with live prior-hour error feedback ($e_{t-1}$) from checkpoint turnstiles. | "Cyber-physical" refers to robotics, industrial SCADA systems, or IoT embedded hardware; using it for a statistical model is buzzword inflation. |
| **Model Architecture** | **Cyber-Physical Stability Manifolds** | **Two-Stage Sequential Architecture / Closed-Loop Error Adaptation** | Updating forecasts dynamically using live floor feedback during severe flight delays to avoid demand collapse. | "Manifolds" is borrowed from differential geometry and topology, sounding like pseudo-mathematical obfuscation. |
| **Model Architecture** | **Regime-Switched Gated Inference Engine** | **Dual-Track Operational Decision Framework** (or **Disruption-Adaptive Checkpoint Forecasting Playbook / Regime-Adaptive Predictive Architecture**) | An automated operational decision rule routing predictions to Model 2 (Supervised ML) during calm conditions and switching to Model 3 (Dynamic Hybrid) during severe disruptions ($T(h) \ge 0.75$). | "Gated" and "inference engine" are computer science / AI runtime jargon; "gates" also conflicts with physical airport boarding gates. |
| **Proprietary Metrics** | **Coupled Volatility Index ($\text{CVI}$)** | **Landside–Airside Volatility Interaction Term** (or **Joint Volatility Interaction**) | Compounding operational stress when passenger arrival surges ($CV_{\text{TSA}}$) coincide with high flight departure delay dispersion ($\sigma_{\text{Delay}}$). | Coined, proprietary acronym not found in FAA/IATA literature; multiplies mixed units (dimensionless ratio $\times$ delay minutes). |
| **Proprietary Metrics** | **Coupled Volatility Matrix / Regimes** | **Bivariate Volatility Stratification** (or **Cross-System Volatility Regimes**) | Grouping operational days by both landside passenger variation ($CV_{\text{TSA}}$) and airside flight delay spread ($\sigma_{\text{Delay}}$). | Sounds like an invented mathematical artifact rather than standard bivariate statistical clustering. |
| **Intraday Regimes** | **Diurnal Non-Consecutive Dual Turbulence Peaks** | **Bimodal Intraday Operational Peaks: Morning Surges and Evening Delay Cascades** | Daily bimodal congestion curve: morning passenger arrival rush (05:00–08:00) and evening flight delay propagation (14:00–22:00). | "Diurnal" is ecology jargon; "non-consecutive" overcomplicates a standard bimodal curve; "turbulence" borrows fluid physics jargon. |
| **Intraday Regimes** | **Diurnal Operational Turbulence Shock Index ($T_{dow}(h)$)** | **Intraday Operational Congestion Index** (or **Operational Stress Index**) | Formula classifying hours of the day into Off-Peak, Mid-Peak, and Peak congestion blocks. | "Turbulence Shock Index" sounds like aeroelastic flutter or fluid mechanics rather than queuing congestion. |
| **Model Control** | **Live 1-Step Error Innovation Feedback ($e_{t-1}$)** | **Real-Time Prior-Hour Error Correction** (or **Live Prior-Hour Forecast Error Feedback**) | Raising this hour's forecast if the model underpredicted last hour because delayed passengers crowded the terminal. | "Innovation" sounds like corporate buzzwords; "1-step" is abstract algorithm speak for "prior-hour." |
| **Model Control** | **Zero Feedback Latency** | **Requires No Real-Time Checkpoint Data Feeds** (or **Advance Shift Scheduling Capability**) | Model 2 (Machine Learning) does not require live sensor feeds from turnstiles, enabling advance shift planning. | Misleading (Model 2 has no feedback loop at all); "latency" is IT jargon that obscures the practical planning benefit. |
| **Data Engineering** | **Zero Lookahead Leakage** | **Strict Information Causality** (or **Preserving Operational Information Availability**) | Models only ingest information knowable before the forecast hour, using prior-hour delays rather than same-hour delays. | "Lookahead leakage" is Kaggle data science competition jargon rather than formal econometric causality terminology. |
| **Carrier Isolation** | **Orthogonal Wiener-Hopf Deconvolution Operator** | **Carrier Checkpoint Isolation** (or **Carrier-Exclusive Terminal Pairing**) | In dedicated single-airline terminals, flight departure schedules map directly to security queues without multi-carrier overlap. | Extreme over-mathematization (Wiener-Hopf integral operators) for what is simply filtering data to dedicated single-airline terminals. |
| **Passenger Timing** | **Physics-Based Continuous Arrival Kernel Convolution** | **Empirical Passenger Show-Up Curve Convolution** (or **Lead-Lag Arrival Distribution**) | Spreading departing flight seats across 1, 2, and 3 hours prior to takeoff based on empirical ACRP Report 40 arrival timing. | Passengers do not follow continuous physics kernels; they follow empirical behavioral timing (90 to 120 minutes prior to departure). |
| **Network Accounting** | **DB1B Transfer Deflation Manifold** | **Connecting Passenger Deflator** (or **Local Originating Passenger Fraction**) | Multiplying flight seats by $(1 - \text{Connecting Ratio})$ to remove passengers who connect airside and never enter TSA security. | Calling a simple subtraction and multiplication a "manifold" is pretension that invites immediate committee challenge. |
| **Network Accounting** | **The Connecting Passenger Paradox** | **The Hub Disconnect** (or **Connecting vs. Local Originating Disconnect**) | The planning error of assuming every departing airline seat corresponds to a passenger entering landside security. | "Paradox" sounds melodramatic for a well-known airline hub transfer phenomenon. |
| **Terminal Geometry** | **Type I (Air-Gapped) vs. Type II (Airside Connected) Complexes** | **Physically Separate Terminals vs. Walkway-Connected Terminals** | Standalone terminal buildings (LGA, DTW) versus terminals connected airside by post-security pedestrian walkways (DFW, LAX). | "Type I/II" is idiosyncratic labeling; "air-gapped" is cybersecurity jargon borrowed from network engineering. |
| **Terminal Geometry** | **Inter-Terminal Airside Passenger Leakage / Cross-Contamination** | **Post-Security Terminal Cross-Over** | Passengers who clear TSA security at Terminal A and walk post-security to board a departure out of Terminal B. | "Leakage" and "cross-contamination" are chemical/microbiological terms that sound inappropriate in passenger transport. |
| **Operational Regimes** | **Quiescent / Sterile Control** | **Nominal On-Time Baseline** (or **Overnight Low-Demand Period**) | On-time flight operations (delay < 15 min, 0 cancellations) used as a control state, or overnight curfew hours. | "Quiescent" is biology/laboratory jargon; "sterile control" confuses medical sterilization with FAA sterile concourses. |
| **Performance Pillars** | **Continuous Static Stability (Hypothesis 1 & 2)** | **Routine Operational Accuracy (Robustness)** | How consistently and accurately a predictive model forecasts during normal, undisturbed commercial flight banks. | "Static stability" is flight dynamics terminology (longitudinal stability derivatives); confuses aerodynamics with forecast accuracy. |

---

## 1. The Coupled Volatility Index ($\text{CVI}$) & Coupled Volatility Matrix

### 1.1 Context and Original Question
* **Query**: *"Is the Coupled Volatility Index original to this paper? I don't want to have any made up things, or at least need to give it another name."*
* **Formula in Draft**:
  $$\text{CVI}_d = CV_{\text{TSA}, d} \times \sigma_{\text{Delay}, d}$$

### 1.2 Originality Analysis
* **Yes, the coined name and specific multiplicative equation are original to this thesis.** You will not find the term "Coupled Volatility Index" or the abbreviation "CVI" in standard FAA, TSA, ACRP, or transportation engineering literature.
* **The "Made-Up" Trap**: Reviewers and committee members naturally challenge self-coined indexes:
  1. *Dimensionality Critique*: $CV_{\text{TSA}}$ is a scale-free ratio (dimensionless), whereas $\sigma_{\text{Delay}}$ is measured in minutes. Multiplying them yields an unstandardized composite with units of "dimensionless-minutes."
  2. *Arbitrary Form Critique*: Reviewers may ask why multiplication was chosen over a standardized Euclidean distance, Mahalanobis distance, or standard econometric interaction.

### 1.3 The Underlying Scientific Reality
The underlying phenomenon is **100% legitimate and grounded in queuing theory**:
* Under **Kingman's Heavy-Traffic Approximation**:
  $$W_q \approx \left(\frac{\rho}{1-\rho}\right) \left(\frac{C_a^2 + C_s^2}{2}\right) \frac{1}{\mu}$$
  Checkpoint wait times ($W_q$) scale quadratically with arrival volatility ($C_a^2$) as traffic approaches capacity ($\rho \to 1.0$).
* Empirical correlation demonstrates that static flight volumes disconnect from landside demand ($r = 0.2019, R^2 = 4.08\%$), whereas **volatilities are strongly coupled** ($CV_{\text{TSA}}$ vs. $CV_{\text{Delay}}: r = 0.4375, p < 0.05$).
* Multiplying two explanatory features in statistics is simply an **interaction term** ($X_1 \cdot X_2$) designed to test compounding effects.

### 1.4 Recommended Framing and Text Replacements
Rather than declaring an invented index, frame it as a **statistical interaction term** and **bivariate clustering**:
* **Before (Proprietary / Jargon)**:  
  *"To address post-pandemic volatility, the methodology introduces a novel Coupled Volatility Index ($\text{CVI}_d = CV_{\text{TSA}, d} \times \sigma_{\text{Delay}, d}$) to quantify operational turbulence."*
* **After (Standard Aviation & Econometrics)**:  
  *"To capture the compounding operational stress when passenger arrival surges coincide with airside schedule instability, a cross-system volatility interaction term was evaluated ($CV_{\text{TSA}, d} \times \sigma_{\text{Delay}, d}$). Furthermore, bivariate clustering across standardized passenger arrival variation ($CV_{\text{TSA}}$) and flight departure delay dispersion ($\sigma_{\text{Delay}}$) was employed to empirically delineate annual seasonal regimes and day-of-week operational cycles."*

---

## 2. Diurnal Non-Consecutive Dual Turbulence Peaks & Turbulence Shock Index

### 2.1 Context and Analysis of Awkward Phrasing
1. **"Diurnal"**: Standard in ecology and zoology, but rarely used by airport directors or transportation economists. Established domain terms are **intraday**, **within-day**, or **daily**.
2. **"Non-Consecutive"**: Morning (05:00–08:00) and evening (14:00–22:00) peaks separated by a midday trough form a standard **bimodal distribution**. Stating "non-consecutive" makes a common time-series feature sound artificially exotic.
3. **"Turbulence"**: Borrowed from fluid dynamics. In terminal operations, the physical reality is **checkpoint demand surges** and **flight delay cascades**.
4. **"Turbulence Shock Index ($T(h)$)"**: Classifying hours into congestion regimes is standard cluster analysis; calling it a "Shock Index" sounds like aeroelastic flutter.

### 2.2 Recommended Framing and Text Replacements
* **Heading Replacement**: `Bimodal Intraday Operational Peaks: Morning Surges and Evening Delay Cascades` (or `Bimodal Intraday Congestion Regimes`)
* **Index Replacement**: `Intraday Operational Congestion Index` (or `Operational Stress Index`)
* **Before (Draft Text)**:  
  *"Diurnal Non-Consecutive Dual Turbulence Peaks. Rather than dividing the 24 hours of each operational day into arbitrary consecutive time blocks, diurnal hours were categorized by the Operational Turbulence Shock Index ($T(h)$)..."*
* **After (Publishable Manuscript Text)**:  
  *"Bimodal Intraday Operational Peaks: Morning Surges and Evening Delay Cascades. Rather than partitioning the operational day into arbitrary uniform time blocks, intraday hours were grouped into operational regimes reflecting the airport system's bimodal congestion profile:  
  1. **1_OFF_PEAK (Overnight Curfew Valley)**: Typically 00:00 to 03:59, when flight movements are sparse and checkpoint demand is minimal.  
  2. **2_MID_PEAK (Midday Steady Flow)**: Typically 08:00 to 13:59, characterized by steady passenger screening rates and scheduled turnarounds.  
  3. **3_PEAK (Bimodal Congestion Windows)**: Unifies the system's two operational stress windows into a single high-demand category:  
     * *Morning Bank Surge (05:00–07:59)*: Driven by concentrated passenger arrival waves ($\sigma_{\text{TSA}} > 11,380$ pax/hr) while airside flights operate largely on time.  
     * *Evening Delay Cascade (14:00–21:59)*: Driven by cumulative network-wide flight delay propagation ($\sigma_{\text{Delay}} > 63.4$ min)."*

---

## 3. Live 1-Step Error Innovation Feedback ($e_{t-1} = y_{t-1} - \hat{y}_{t-1}$)

### 3.1 Plain-English Operational Reality
* **The Scenario**: Severe convective storms delay 18:00 flight departures until 22:00.
* **The Problem with Open-Loop ML (The Empty Checkpoint Fallacy)**: A model that only watches delayed departure boards assumes the checkpoint will be empty at 16:30. In reality, passengers arrived on their original ticketed schedule and are stranded in the terminal lobby.
* **The Mechanism**: In the previous hour ($t-1$), the model predicted 500 passengers ($\hat{y}_{t-1}$), but turnstiles recorded 1,200 ($y_{t-1}$). The error is $+700$.
* **The Action**: Instead of repeating the mistake in the current hour ($t$), the model ingests that $+700$ passenger discrepancy and immediately raises its current forecast.

### 3.2 Academic Lineage vs. Jargon Perception
* In Kalman filtering and state-space econometrics (Kalman, 1960; Box & Jenkins, 1970), $y_t - \hat{y}_t$ is mathematically termed the **innovation** (representing "new information" unpredicted by historical states).
* However, in modern English, "innovation" denotes creative invention or corporate buzzwords. Stringing together *"live 1-step error innovation feedback"* sounds like robotics techno-babble. Operationally, "1-step" simply means **"prior-hour."**

### 3.3 Recommended Framing and Text Replacements
* **Before (Draft Text)**:  
  *"Combines daily and weekly flight schedule cycles with live 1-step error innovation feedback ($e_{t-1} = y_{t-1} - \hat{y}_{t-1}$) from actual checkpoint screening counts. When unexpected flight delays hold passengers landside, the dynamic error correction senses the accumulation and immediately adjusts the forecast upward."*
* **After (Publishable Manuscript Text)**:  
  *"Combines recurring flight schedule cycles with real-time prior-hour error correction ($e_{t-1} = y_{t-1} - \hat{y}_{t-1}$) from live checkpoint screening turnstiles. When unexpected flight delays cause passengers to dwell landside, this closed-loop correction detects passenger accumulation in real time and immediately adjusts the upcoming forecast upward."*

---

## 4. Zero Feedback Latency (Model 2 vs. Model 3)

### 4.1 Practical Operational Contrast: Model 2 vs. Model 3
* **Model 3 (Dynamic Two-Stage Hybrid)**: Requires live prior-hour throughput counts ($y_{t-1}$) to calculate its residual error correction. It cannot generate a forecast until the previous hour concludes and TSA sensor data is transmitted over the airport network. It is bound to a real-time data dependency.
* **Model 2 (Supervised Machine Learning)**: Depends only on published airline schedules, aircraft seat capacities, and historical weather/delay attributes. It requires **no live data feeds from the screening floor**.

### 4.2 Why the Term is Problematic
1. **Technically Misleading**: Saying "zero feedback latency" implies Model 2 possesses a feedback loop that executes in zero seconds. In reality, Model 2 has **no feedback loop at all** (it is a feed-forward, open-loop architecture).
2. **Abstract IT Jargon**: Airport managers do not evaluate models based on "microsecond latency"; they evaluate whether they can produce **TSO staffing schedules 24 to 72 hours in advance**.

### 4.3 Recommended Framing and Text Replacements
* **Before (Draft Text)**:  
  *"Both Model 2 and Model 3 achieve $\text{MASE} < 0.70$ under routine operations. However, Model 2 achieves this with near-zero computational overhead and zero feedback latency, making it the preferred operational choice for everyday routine staffing."*
* **After (Publishable Manuscript Text)**:  
  *"Both Model 2 and Model 3 achieve the academic target of $\text{MASE} < 0.70$ under routine operations. However, Model 2 operates with near-zero computational overhead and requires no real-time checkpoint data feeds, allowing airport operators to generate shift staffing plans days in advance without waiting for live hourly turnstile telemetry."*

---

## 5. Heavy-Traffic Queuing Physics vs. Queuing Principles & Dynamics (The "Physics" Trap)

### 5.1 Context and The Qualitative Research Rationale
At Embry-Riddle Aeronautical University, qualitative researchers in aviation management, human factors, and airline operations study human decision-making, organizational protocols, and passenger travel habits. Human passengers do not obey Newton's laws of motion, conservation of momentum, or thermodynamic fluid equations. 

When a thesis manuscript uses terms like **"heavy-traffic queuing physics"**, qualitative committee members are immediately prompted to ask:
> *"Where are the physical laws or Navier-Stokes equations? Passengers are thinking humans who arrive based on flight times, carry-on bags, and mobile notifications. Calling this 'physics' is a category error."*

### 5.2 The Mathematical and Theoretical Reality
The mathematical relationship referenced is **Kingman's Heavy-Traffic Approximation (1961)** and the **Allen-Cunneen Formula for $G/G/s$ Queues**:
$$W_q \approx \left(\frac{\rho^{\sqrt{2(s+1)}-1}}{s(1-\rho)}\right) \left(\frac{C_a^2 + C_s^2}{2}\right) \frac{1}{\mu}$$
This is a foundational theorem of **Applied Probability, Operations Research, and Queuing Theory**. It describes how random arrival intervals and service variances interact in multi-server service facilities. Referring to it as **"queuing principles"**, **"queuing theory"**, or **"queuing dynamics"** is 100% mathematically correct and completely immune to the "physics trap."

### 5.3 Recommended Framing and Text Replacements
* **Before (Physics Jargon)**:  
  *"In operational reality, heavy-traffic queuing physics (Kingman, 1961; Whitt, 1993) proves that expected queue wait times scale linearly with arrival variance ($C_a^2$)."*
* **After (Queuing Principles / Operations Research)**:  
  *"In operational reality, heavy-traffic queuing principles (Kingman, 1961; Whitt, 1993) demonstrate that expected queue wait times and backlogs in general $G/G/s$ screening facilities scale not with mean volume, but linearly with the squared coefficient of variation of arrival times ($C_a^2$) and service times ($C_s^2$) via the Allen-Cunneen approximation."*

---

## 6. Deterministic Physical Baseline (Model 1) vs. Deterministic Operational Baseline

### 6.1 Operational Meaning of Model 1
Model 1 uses published airline flight schedules, adjusted forward in time by multiplying scheduled seat departures by empirical passenger show-up curves from ACRP Report 40 ($t+1, t+2, t+3$). It represents a non-machine-learning, schedule-based planning benchmark.

### 6.2 Why "Physical Baseline" and "Physical Rules" Risk Scrutiny
Calling an airline flight schedule a "physical baseline" or referring to "physical schedule rules" implies:
* Physical sensor telemetry (e.g., optical turnstiles, lidar queue sensors, RFID tracking).
* Physics-Informed Neural Networks (PINNs) or mechanical modeling.
In reality, published schedules are **administrative operational plans** filed by airlines with the FAA and OAG. The rules governing them are **deterministic operational rules** (e.g., convolution across passenger arrival windows).

### 6.3 Recommended Framing and Text Replacements
* **Before (Draft Text)**:  
  *"Model 1: Deterministic Flight Schedule Model (Physical Baseline). Deterministic physical rules lose only 4.2% accuracy on spatial transfer."*
* **After (Publishable Manuscript Text)**:  
  *"Model 1: Deterministic Flight Schedule Model (Operational Baseline). Deterministic operational rules lose only 4.2% accuracy on spatial transfer because flight schedule convolution is invariant across terminal geometries."*

---

## 7. "True Physical Lead-Lag Relationship" vs. Empirical Behavioral Lead-Lag Offset

### 7.1 Operational Meaning
Commercial airline passengers arrive at security checkpoints 90 to 120 minutes prior to scheduled takeoff (ACRP Report 40). Thus, landside security throughput peaks 1.5 to 2 hours *before* flights depart. Conversely, airside departure delays accumulate *downstream* throughout the operational day.

### 7.2 Why "Physical" Is Inaccurate
This time difference is an **empirical behavioral offset** created by traveler risk aversion, airport dwell habits, and airline boarding closure cutoffs (e.g., doors closing 15 minutes prior to departure). It is not a physical constraint of mechanics.

### 7.3 Recommended Framing and Text Replacements
* **Before (Draft Text)**:  
  *"Isolating pure carrier-checkpoint pairs where single-carrier operations feed dedicated screening lanes is essential to unmask the true physical lead-lag relationship between flight schedules and landside arrivals."*
* **After (Publishable Manuscript Text)**:  
  *"Isolating pure carrier-checkpoint pairs where single-carrier operations feed dedicated screening lanes is essential to unmask the true empirical lead-lag relationship between flight schedules and landside arrivals."*

---

## 8. "Idiosyncratic Physical Geometry" vs. Terminal Layouts, Gate Geometry & Concourse Facilities

### 8.1 Operational Meaning
Different airports feature divergent terminal architectures: finger-pier concourses (BOS Terminal A), linear central halls (DTW McNamara), multi-terminal circular satellites (DFW), or perpendicular gate piers (LGA Terminal C). Machine learning models trained on one airport can memorize specific local gate walking distances and airline bank structures.

### 8.2 Why "Physical Geometry" Sounds Jargon-Heavy
"Physical geometry" sounds like computational fluid dynamics (CFD) mesh modeling or mechanical CAD drafting. Airport operators and transportation planners use standard industry terms: **terminal layouts**, **gate configurations**, and **concourse architecture**.

### 8.3 Recommended Framing and Text Replacements
* **Before (Draft Text)**:  
  *"Highly parameterized neural networks tend to memorize terminal-specific gate layouts and idiosyncratic physical geometry, causing transfer failure."*
* **After (Publishable Manuscript Text)**:  
  *"Highly parameterized neural networks tend to memorize terminal-specific gate layouts, unique local carrier flight banks, and idiosyncratic terminal layouts and gate configurations, causing forecast accuracy to degrade when transferred to unfamiliar airports."*

---

## 9. "Carrier Isolation Physically Impossible" vs. Structural / Architectural Single-Checkpoint Constraints

### 9.1 Operational Meaning (PHL vs. SLC Case Study)
In Chapter IV, Salt Lake City International (SLC) was excluded from the experimental cohort because all departing passengers from all airlines are funneled through a single, consolidated central screening checkpoint hall. Philadelphia International (PHL) was selected because American Airlines operates dedicated, exclusive checkpoints in Terminals B and C.

### 9.2 Committee Critique of "Physically Impossible"
Carrier isolation is not prevented by the laws of physics. It is prevented by the **architectural design and operational layout** of SLC's terminal complex, which deliberately consolidated security screening into a single hall to optimize TSA staffing lines.

### 9.3 Recommended Framing and Text Replacements
* **Before (Draft Text)**:  
  *"Salt Lake City International channels all airlines through a single consolidated central screening checkpoint, making carrier isolation physically impossible."*
* **After (Publishable Manuscript Text)**:  
  *"Salt Lake City International channels all airlines through a single consolidated central screening checkpoint, making carrier isolation structurally impossible within shared terminal geometry."*

---

## 10. "Physical Checkpoint Closures" vs. Scheduled Nighttime Closures & Operational Zeros

### 10.1 Operational Meaning
In raw TSA hourly logs, 2.31% of records report exactly zero screened passengers. Cross-referencing flight records proves that 98.6% of these zeros occur between 00:00 and 03:59 local time, when security checkpoints are closed for the night.

### 10.2 Why "Physical Closures vs. Sensor Dropouts" Risks Scrutiny
In data science literature, missing data is often called "sensor dropouts" or "hardware dropouts." Calling closed checkpoint doors a "physical closure" is overly clinical. Describing them as **scheduled nighttime checkpoint closures** or **true operational structural zeros** immediately communicates administrative reality.

### 10.3 Recommended Framing and Text Replacements
* **Before (Draft Text)**:  
  *"Physical Checkpoint Closures vs. Missing Sensor Data: Intervals were preserved as real physical zeros..."*
* **After (Publishable Manuscript Text)**:  
  *"Scheduled Checkpoint Closures vs. Missing Sensor Data: Rather than fabricating passenger demand during scheduled overnight lane closures, these intervals were preserved as true operational structural zeros..."*

---

## 11. "Cyber-Physical Hybrid" & "Stability Manifolds" vs. Dynamic Two-Stage Sequential Hybrid

### 11.1 Operational Meaning of Model 3
Model 3 operates in two sequential stages:
1. *Stage 1*: An open-loop schedule baseline estimating recurring daily/weekly passenger waves.
2. *Stage 2*: A decision-tree error correction model that ingests live prior-hour residuals ($e_{t-1} = y_{t-1} - \hat{y}_{t-1}$) to track real-time queue accumulation during flight delays.

### 11.2 The "Cyber-Physical" Buzzword Problem
"Cyber-physical systems" (CPS) formally describes physical mechanisms controlled by computer-based algorithms via feedback loops—such as autonomous drones, nuclear reactor cooling systems, or CNC milling machines. Applying this term to a **two-stage statistical time-series model** creates artificial complexity that journal reviewers and qualitative committee members reject as posturing.

### 11.3 Recommended Framing and Text Replacements
* **Before (Draft Text)**:  
  *"Rather than utilizing deep cyber-physical recurrent architectures, a sequential cyber-physical framework was formulated to maintain cyber-physical stability manifolds under shock states."*
* **After (Publishable Manuscript Text)**:  
  *"A Dynamic Two-Stage Hybrid Model was developed, coupling a baseline flight schedule foundation with live real-time error feedback ($e_{t-1}$) from the checkpoint floor to achieve decisive resilience during severe flight disruptions."*

---

## 12. "Zero Lookahead Leakage" vs. Strict Information Causality

### 12.1 Operational Meaning
A forecasting model designed to predict passenger volumes at 16:00 cannot use flight departure delays that occur at 18:00, because airport managers at 16:00 do not yet know the future delay. Models must use lagged covariates (such as departure delays at $t-1$).

### 12.2 Academic Lineage vs. Kaggle Jargon
"Lookahead leakage" is informal machine learning competition slang. In academic transportation econometrics and time-series forecasting, the formal principle is **strict information causality** or **operational information availability**.

### 12.3 Recommended Framing and Text Replacements
* **Before (Draft Text)**:  
  *"Strict ETL partitioning enforces zero lookahead leakage into downstream model training."*
* **After (Publishable Manuscript Text)**:  
  *"Strict information causality ensures that pre-departure forecasting models can only consume information that was knowable before the event, preserving real-world operational validity."*

---

## 13. "Orthogonal Wiener-Hopf Deconvolution Operator" vs. Carrier Checkpoint Isolation

### 13.1 Operational Meaning
In multi-carrier terminals, competing airlines schedule flight departure banks at the exact same times, making it impossible to separate which passengers belong to which airline. By isolating terminals that serve a single airline exclusively (e.g., Delta at LGA Terminal C), flight schedules map directly to security queues.

### 13.2 Committee Critique
Wiener-Hopf operators are complex integral equations used in mathematical physics and signal deconvolution. Calling dedicated single-airline terminal filtering an "orthogonal Wiener-Hopf deconvolution operator" is extreme over-mathematization that undermines credibility during defense questioning.

### 13.3 Recommended Framing and Text Replacements
* **Before (Draft Text)**:  
  *"This research formulates an orthogonal Wiener-Hopf deconvolution operator across dedicated carrier complexes to collapse collinear schedule cross-talk."*
* **After (Publishable Manuscript Text)**:  
  *"This research isolates carrier-exclusive terminal screening complexes, eliminating multi-carrier schedule collinearity and directly mapping an airline's departing flight banks to its dedicated security checkpoint queues."*

---

## 14. "Physics-Based Continuous Arrival Kernel Convolution" vs. Empirical Passenger Show-Up Curve Convolution

### 14.1 Operational Meaning
Taking published airline flight departures and distributing departing seats across lead hours ($t+1, t+2, t+3$) based on standard ACRP Report 40 arrival profiles (35% at $t-1$, 50% at $t-2$, 15% at $t-3$).

### 14.2 Reviewer Critique
Passengers do not follow a continuous physical kernel function. They follow **empirical passenger show-up curves** documented in transportation planning literature. Citing ACRP Report 40 grounds the method in authentic aviation planning standards.

### 14.3 Recommended Framing and Text Replacements
* **Before (Draft Text)**:  
  *"Departures are transformed via a physics-based continuous lognormal arrival kernel convolution pipeline."*
* **After (Publishable Manuscript Text)**:  
  *"Scheduled flight departures are convolved across empirical passenger show-up curves derived from ACRP Report 40 guidelines, distributing passenger arrivals across 1-, 2-, and 3-hour lead horizons prior to takeoff."*

---

## 15. "DB1B Transfer Deflation Manifold" & "The Connecting Passenger Paradox" vs. Connecting Passenger Deflator & The Hub Disconnect

### 15.1 Operational Meaning
At major fortress hubs (e.g., Charlotte at 76.0% connecting or Atlanta at 70.1%), over two-thirds of departing passengers transfer between gates airside and never enter the landside security queue. Treating total departing aircraft seats as security demand overestimates screening loads by 2.5- to 4-fold. Multiplying departing seats by $(1 - \text{Connecting Ratio})$ removes transfer travelers.

### 15.2 Why "Manifold" and "Paradox" Are Inappropriate
* A "manifold" in mathematics is a topological space that locally resembles Euclidean space. A simple subtraction and scalar multiplication $(1 - \text{Connecting Ratio})$ is not a manifold.
* "Paradox" sounds dramatic; it is simply an operational disconnect between total enplanements and landside security demand.

### 15.3 Recommended Framing and Text Replacements
* **Before (Draft Text)**:  
  *"To resolve the Connecting Passenger Paradox, a DB1B transfer deflation manifold was mapped across quarterly coupon surveys."*
* **After (Publishable Manuscript Text)**:  
  *"To resolve the hub disconnect, a connecting passenger deflator derived from quarterly BTS DB1B ticket coupon surveys was applied, scaling flight capacity down to isolate the true local originating passenger fraction."*

---

## 16. "Type I / II Air-Gapped Complexes" & "Passenger Leakage" vs. Physically Separate vs. Walkway-Connected Terminals & Cross-Over

### 16.1 Operational Meaning
* *Physically Separate Terminals*: Standalone buildings with no airside walkway connections (e.g., LGA Terminal C, DTW McNamara, BOS Terminal A).
* *Walkway-Connected Terminals*: Terminal concourses linked post-security behind TSA checkpoints via airside pedestrian bridges or walkways (e.g., DFW Terminals A–E, LAX Terminals 4–8).
* In Chapter IV, a two-sample Kolmogorov-Smirnov test proved that connected terminals behave identically to separate buildings ($D = 0.032, p = 0.28$) because airline baggage-check rules and CAT biometric ID scanners prevent travelers from screening at the wrong terminal.

### 16.2 Critique of Jargon
* "Type I" and "Type II" are arbitrary, non-standard designations.
* "Air-gapped" is a cybersecurity networking term (referring to computers disconnected from the internet).
* "Passenger leakage" and "cross-contamination" are chemical/medical terms.

### 16.3 Recommended Framing and Text Replacements
* **Before (Draft Text)**:  
  *"Evaluates Type I air-gapped versus Type II airside-connected complexes to test whether inter-terminal airside passenger leakage and cross-contamination distorts dedicated carrier signals."*
* **After (Publishable Manuscript Text)**:  
  *"Compares physically separate terminal buildings against walkway-connected terminals to evaluate whether post-security terminal cross-over distorts dedicated carrier screening demand."*

---

## 17. "Quiescent / Sterile Control" & "Continuous Static Stability" vs. Nominal On-Time Baseline & Routine Operational Accuracy

### 17.1 Operational Meaning
* *Nominal Baseline*: Days/hours where flights depart with less than 15 minutes of delay and zero cancellations (conforming to the FAA/DOT A14 regulatory on-time benchmark).
* *Routine Accuracy*: The model's day-in, day-out forecast precision during standard commercial operations (evaluated via $\text{RMSE}_{\text{routine}}$ and $\text{MASE}_{\text{routine}} < 0.700$).

### 17.2 Critique of Jargon
* "Quiescent" is biology and clinical laboratory jargon.
* "Sterile control" confuses medical laboratory sterilization with an FAA "sterile area" (the post-security airside concourse).
* "Static stability" is aircraft aerodynamics terminology (longitudinal stability derivatives $C_{m_\alpha}$). Using it for time-series forecasting causes immediate confusion among aeronautics faculty.

### 17.3 Recommended Framing and Text Replacements
* **Before (Draft Text)**:  
  *"Dimension 1 establishes a quiescent sterile control to evaluate continuous static stability across undisturbed flight regimes."*
* **After (Publishable Manuscript Text)**:  
  *"Dimension 1 establishes a nominal on-time baseline (conforming to FAA A14 on-time standards) to evaluate routine operational accuracy across undisturbed daily flight banks."*

---

## 18. "Regime-Switched Gated Inference Engine" vs. Dual-Track Operational Decision Framework

### 18.1 Operational Meaning
* The automated decision framework recommended for airport operations centers (AOCs) and TSA leadership to operationalize the thesis's empirical findings.
* Rather than deploying a single model 24/7, the system evaluates real-time flight network turbulence ($T(h)$ or delay dispersion) and dynamically switches between operational tracks:
  * **Track 1: Routine Flow ($T(h) < 0.75$)**: Uses **Model 2 (Supervised Machine Learning)** for low-overhead, advance shift scheduling ($\text{MASE} = 0.68\text{--}0.70$) without live checkpoint sensor dependencies.
  * **Track 2: Tactical Shock / IROPS ($T(h) \ge 0.75$)**: Engages **Model 3 (Dynamic Two-Stage Hybrid)** with closed-loop prior-hour error correction ($e_{t-1}$) to rapidly absorb convective disruptions and ground stop cascades ($\text{TTR} = 2.8\text{h}, R_{\text{MASE}} = 1.05$).

### 18.2 Critique of Jargon
* **"Gated"**: Borrowed from neural network / deep learning architectures (e.g., Mixture-of-Experts gating networks, LSTM recurrent gates). In commercial airport operations, "gates" refers to physical aircraft parking positions; using "gated" for model switching causes domain ambiguity and sounds like AI buzzwords.
* **"Inference Engine"**: Borrowed from expert systems and machine learning hardware runtimes (e.g., TensorRT inference engines). Airport operations centers and TSA command staff execute *operational decision frameworks*, *dispatch playbooks*, or *staffing protocols*, not software "inference engines."
* **"Regime-Switched"**: While "regime switching" is an established econometric concept (Hamilton, 1989), combining all three buzzwords (*regime-switched*, *gated*, *inference engine*) into a single compound phrase creates an impression of unnecessary technical complexity for an aviation management thesis committee.

### 18.3 Recommended Framing and Text Replacements
* **Option 1 (Operational & Applied Aviation - Recommended)**:  
  `Dual-Track Operational Decision Framework` (or `Dual-Track Decision Playbook`)
* **Option 2 (Disruption / Queuing Focused)**:  
  `Disruption-Adaptive Checkpoint Forecasting Framework` (or `Condition-Responsive Staffing Protocol`)
* **Option 3 (Econometrics & Operations Research)**:  
  `Regime-Adaptive Predictive Architecture` (or `Dual-Regime Operational Forecasting System`)
* **Option 4 (Conservative Polish Retaining "Regime-Switching")**:  
  `Regime-Switched Dual-Track Decision Engine`

#### Before vs. After Section Prose:
* **Before (Draft Text)**:  
  *"To operationalize these empirical findings, the Transportation Security Administration (TSA) and Airport Operations Centers (AOC) should deploy a **Regime-Switched Gated Inference Engine**—an automated decision playbook that monitors airport turbulence and automatically selects the most suitable forecasting model..."*
* **After (Publishable Manuscript Text)**:  
  *"To operationalize these empirical findings, the Transportation Security Administration (TSA) and Airport Operations Centers (AOC) should deploy a **Dual-Track Operational Decision Framework**—an automated operational playbook that monitors airport turbulence levels and dynamically routes checkpoint predictions to the most resilient forecasting model based on flight network stability..."*

---

## 19. Comprehensive Oral Defense Q&A Strategy: Anticipated Committee Questions & Qualitative Defense Scripts

The following scripted questions and responses prepare the candidate to address qualitative and operational questions during the thesis oral defense before Embry-Riddle aeronautics professors.

### Question 1: "Why did you shift the primary research target from predicting passenger volume to predicting passenger throughput volatility?"
* **Candidate Defense Script**:  
  *"In traditional airport master planning, terminal models focused exclusively on expected passenger volumes ($\mu$). However, as any airport terminal manager knows, security checkpoints do not fail because of average daily passenger volumes—they fail because of sudden arrival surges and queuing volatility. Under Kingman's heavy-traffic queuing formula ($W_q \propto C_a^2$), expected queue wait times scale quadratically with arrival volatility ($C_a^2$) as checkpoint lanes approach capacity. Predicting passenger throughput volatility ($\sigma_{\text{TSA}}$ and $CV_{\text{TSA}}$) is what allows airport security directors to establish dynamic lane staffing buffers ($c(t) = \lceil (\hat{\mu}_t + 1.036 \cdot \hat{\sigma}_t) / \mu_{\text{lane}} \rceil$), directly preventing runway queue backlogs during peak departure banks."*

### Question 2: "Your committee includes faculty who specialize in qualitative aviation research. How does your methodology account for human passenger behavior rather than treating travelers like automated particles?"
* **Candidate Defense Script**:  
  *"That is precisely why this research rejects mechanical 'physics' modeling in favor of empirical human behavioral dynamics. Human travelers make strategic decisions: they arrive at security 90 to 120 minutes prior to departure based on baggage check rules, boarding priorities, and risk aversion (ACRP Report 40). Furthermore, travelers behave differently depending on airline policies—which is why Southwest Airlines was excluded due to its bimodal arrival timing driven by open-seating boarding habits. Finally, our analysis of the 'Empty Checkpoint Fallacy' demonstrates that during flight delays, passengers do not disappear as automated algorithms predict; they arrive based on their original ticketed schedules and dwell in airport lobbies, proving that forecasting models must accommodate human traveler behavior."*

### Question 3: "Why did you select exactly three candidate models plus a baseline control rather than testing dozens of machine learning algorithms?"
* **Candidate Defense Script**:  
  *"Rather than conducting an unconstrained algorithmic horse race, the evaluation was designed around three distinct operational paradigms that represent real-world choices for airport operators:  
  1. **Baseline Control**: A daily persistence benchmark ($y_{t-24}$) establishing the non-parametric reference standard ($\text{MASE} \equiv 1.000$).  
  2. **Model 1 (Deterministic Operational Baseline)**: Uses only published airline schedules convolved across passenger show-up curves, representing a lightweight physical schedule baseline.  
  3. **Model 2 (Supervised Machine Learning)**: Incorporates 24 airside operational attributes from BTS OTP to test whether delay and cancellation data improves routine planning without requiring live sensors.  
  4. **Model 3 (Dynamic Two-Stage Hybrid)**: Couples schedule cycles with real-time prior-hour error correction ($e_{t-1}$) to absorb severe storm disruptions.  
  Testing these three paradigms allowed us to prove Hypothesis 1: that models exhibit asymmetric operational trade-offs, with Model 3 winning Resilience, Model 1 winning Generalizability, and Model 2 winning Routine Pareto Efficiency."*

### Question 4: "Why did you exclude non-tenant airlines and focus on dedicated carrier complexes?"
* **Candidate Defense Script**:  
  *"In shared terminal facilities (such as Salt Lake City or Phoenix), multiple airlines funnel passengers into shared security lines. Because competing airlines coordinate their departure banks around the same peak hours, their flight schedules are collinear ($\text{Corr} \ge 0.88$). In a shared checkpoint, it is impossible to separate which passengers in line belong to which airline. By isolating dedicated, single-carrier checkpoints—such as Delta at LGA Terminal C or United at Newark Terminal C—we eliminated multi-carrier schedule cross-talk ($\kappa < 25$), directly mapping airline flight departures to security throughput."*

### Question 5: "What is the practical takeaway for a TSA Federal Security Director (FSD) or Airport Operations Center (AOC)?"
* **Candidate Defense Script**:  
  *"The practical operational deliverable is the **Dual-Track Operational Decision Framework** (or Regime-Switched Decision Engine):  
  * During routine, clear-weather operations ($T(h) < 0.75$), the airport uses **Model 2 (Supervised Machine Learning)**. It requires no real-time sensor connections, produces shift staffing plans days in advance, and achieves superior accuracy ($\text{MASE} = 0.680\text{--}0.700$).  
  * When severe convective weather ground stops occur ($T(h) \ge 0.75$), the system automatically switches to **Model 3 (Dynamic Two-Stage Hybrid)**. Model 3 engages live prior-hour error correction ($e_{t-1}$), tracking stranded passengers dwelling landside and recovering normal error bounds in 2.8 hours.  
  This provides airport authorities with a practical, defensible decision tool that optimizes screening lane staffing without costly brick-and-mortar facility expansion."*
