# Academic Terminology Clarification and Replacement Guide
## De-Jargoning Core Concepts for Thesis Defense & Committee Review

* **Author**: Leila Gleich  
* **Institution**: Embry-Riddle Aeronautical University  
* **Degree**: Master of Science in Aeronautics (MSAA)  
* **Date**: October 6, 2026  
* **Document Purpose**: Synthesizes the terminology clarifications requested during manuscript refinement. This guide translates proprietary-sounding formulas and computer-science/physics jargon into rigorous, publishable aviation operations and transportation econometrics terminology for Chapters III, IV, and V, as well as oral defense preparation.

---

## Executive Summary & Quick-Reference Cheat Sheet

| Draft Terminology / Jargon | Underlying Operational Reality | Why It Risks Committee Scrutiny | Recommended Academic Replacement |
| :--- | :--- | :--- | :--- |
| **Coupled Volatility Index ($\text{CVI}$)** | The compounding effect when passenger screening surges coincide with high flight departure delay dispersion. | Coined, proprietary name not found in FAA/IATA literature; multiplies mixed units ($CV$ [dimensionless] $\times$ $\sigma$ [minutes]). | **Landside–Airside Volatility Interaction Term** (or **Joint Volatility Interaction**) |
| **Coupled Volatility Matrix / Regimes** | Grouping days or weeks by both passenger arrival variation ($CV_{\text{TSA}}$) and flight delay standard deviation ($\sigma_{\text{Delay}}$). | Sounds like an invented mathematical artifact rather than standard clustering. | **Bivariate Volatility Stratification** (or **Cross-System Volatility Regimes**) |
| **Diurnal Non-Consecutive Dual Turbulence Peaks** | The daily bimodal congestion curve: morning passenger arrival rush (05:00–08:00) and evening flight delay propagation (14:00–22:00). | "Diurnal" sounds like biology/ecology; "non-consecutive" overcomplicates a standard bimodal curve; "turbulence" is borrowed physics jargon. | **Bimodal Intraday Operational Peaks: Morning Surges and Evening Delay Cascades** (or **Bimodal Intraday Congestion Regimes**) |
| **Live 1-Step Error Innovation Feedback ($e_{t-1}$)** | If the model underpredicted checkpoint demand last hour because delayed passengers crowded the lobby, it raises this hour's forecast. | "Innovation" sounds like corporate tech buzzwords; "1-step" is abstract algorithm speak for "prior-hour." | **Real-Time Prior-Hour Error Correction** (or **Live Prior-Hour Forecast Error Feedback**) |
| **Zero Feedback Latency** | Model 2 (Machine Learning) does not require live sensor feeds from the checkpoint floor, allowing advance shift scheduling. | Misleading (Model 2 has *no* feedback loop, it is feed-forward); "latency" is IT jargon that obscures the practical planning benefit. | **Requires No Real-Time Checkpoint Data Feeds** (or **Advance Scheduling Capability**) |

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

## 2. Diurnal Non-Consecutive Dual Turbulence Peaks

### 2.1 Context and Original Question
* **Query**: Section heading refinement for `Diurnal Non-Consecutive Dual Turbulence Peaks`.

### 2.2 Analysis of Awkward Phrasing
1. **"Diurnal"**: Standard in ecology/zoology, but rarely used by airport directors or transportation economists. The established domain terms are **intraday**, **within-day**, or **daily**.
2. **"Non-Consecutive"**: Morning (05:00–08:00) and evening (14:00–22:00) peaks separated by a midday trough form a standard **bimodal distribution**. Stating "non-consecutive" makes a common time-series feature sound artificially exotic.
3. **"Turbulence"**: Borrowed from fluid dynamics. In terminal operations, the physical reality is **checkpoint demand surges** and **flight delay cascades**.

### 2.3 Recommended Framing and Text Replacements

#### Recommended Heading Options:
* **Option 1 (Operational & Informative - Recommended)**:  
  `Bimodal Intraday Operational Peaks: Morning Surges and Evening Delay Cascades`
* **Option 2 (Concise & Formal)**:  
  `Bimodal Intraday Congestion Regimes`
* **Option 3 (Queuing & Variance Focused)**:  
  `Bimodal Daily Volatility Regimes: Arrival Surges vs. Delay Propagation`

#### Before vs. After Section Prose:
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

### 3.1 Context and Original Question
* **Query**: *"What is the 1 step error innovation feedback? this feels like jargon: Combines daily and weekly flight schedule cycles with live 1-step error innovation feedback ($e_{t-1}=y_{t-1}-\hat{y}_{t-1}$) from actual checkpoint screening counts. When unexpected flight delays hold passengers landside, the dynamic error correction senses the accumulation and immediately adjusts the forecast upward."*

### 3.2 Plain-English Operational Reality
* **The Scenario**: Severe convective storms delay 18:00 flight departures until 22:00.
* **The Problem with Open-Loop ML (The Empty Checkpoint Fallacy)**: A model that only watches the delayed flight board assumes the security checkpoint will be empty at 16:30. In reality, passengers arrived on their original ticketed schedule and are stranded in the terminal lobby.
* **The Mechanism**: In the previous hour ($t-1$), the model predicted 500 passengers ($\hat{y}_{t-1}$), but turnstiles recorded 1,200 ($y_{t-1}$). The error is $+700$.
* **The Action**: Instead of repeating the mistake in the current hour ($t$), the model ingests that $+700$ passenger discrepancy and immediately raises its current forecast.

### 3.3 Academic Lineage vs. Jargon Perception
* In Kalman filtering and state-space econometrics (Kalman, 1960; Box & Jenkins, 1970), $y_t - \hat{y}_t$ is mathematically termed the **innovation** (representing the "new information" unpredicted by historical states).
* However, in modern English, "innovation" denotes creative invention or corporate buzzwords. Stringing together *"live 1-step error innovation feedback"* sounds like robotics techno-babble.
* Operationally, "1-step" simply means **"prior-hour."**

### 3.4 Recommended Framing and Text Replacements
* **Before (Draft Text)**:  
  *"Combines daily and weekly flight schedule cycles with live 1-step error innovation feedback ($e_{t-1} = y_{t-1} - \hat{y}_{t-1}$) from actual checkpoint screening counts. When unexpected flight delays hold passengers landside, the dynamic error correction senses the accumulation and immediately adjusts the forecast upward."*
* **After (Publishable Manuscript Text)**:  
  *"Combines recurring flight schedule cycles with real-time prior-hour error correction ($e_{t-1} = y_{t-1} - \hat{y}_{t-1}$) from live checkpoint screening turnstiles. When unexpected flight delays cause passengers to dwell landside, this closed-loop correction loop detects passenger accumulation in real time and immediately adjusts the upcoming forecast upward."*

---

## 4. Zero Feedback Latency

### 4.1 Context and Original Question
* **Query**: *"What is zero feedback latency"*

### 4.2 Practical Operational Contrast: Model 2 vs. Model 3
* **Model 3 (Dynamic Hybrid)**: Requires live prior-hour throughput counts ($y_{t-1}$) to calculate its residual error correction. It cannot generate a forecast until the previous hour concludes and TSA sensor data is transmitted over the airport network. It is bound to a real-time data dependency (pipeline latency).
* **Model 2 (Supervised Machine Learning)**: Depends only on published airline schedules, aircraft seat capacities, and historical weather/delay attributes. It requires **no live data feeds from the screening floor**.

### 4.3 Why the Term is Problematic
1. **Technically Misleading**: Saying "zero feedback latency" implies Model 2 possesses a feedback loop that executes in zero seconds. In reality, Model 2 has **no feedback loop at all** (it is a feed-forward, open-loop architecture).
2. **Abstract IT Jargon**: Airport managers do not evaluate models based on "microsecond latency"; they evaluate whether they can produce **TSO staffing schedules 24 to 72 hours in advance**.

### 4.4 Recommended Framing and Text Replacements
* **Before (Draft Text)**:  
  *"Both Model 2 and Model 3 achieve $\text{MASE} < 0.70$ under routine operations. However, Model 2 achieves this with near-zero computational overhead and zero feedback latency, making it the preferred operational choice for everyday routine staffing."*
* **After (Publishable Manuscript Text)**:  
  *"Both Model 2 and Model 3 achieve the academic target of $\text{MASE} < 0.70$ under routine operations. However, Model 2 operates with near-zero computational overhead and requires no real-time checkpoint data feeds, allowing airport operators to generate shift staffing plans days in advance without waiting for live hourly turnstile telemetry."*

---

## 5. Defense Q&A Strategy: Anticipated Committee Questions

### Q1: "Why didn't you just use an established index like the FAA Delay Index?"
* **Response**: *"The FAA Delay Index and DOT A14 metrics evaluate airside aircraft delays in isolation from terminal buildings. Our empirical econometric analysis across the Top 25 airfields revealed that raw flight delay minutes have virtually no correlation with landside security throughput ($r = -0.062, p = 0.77$). Instead, terminal queue congestion is driven by variance interaction—the coupling between passenger arrival burstiness ($CV_{\text{TSA}}$) and flight delay dispersion ($\sigma_{\text{Delay}}$). To capture this, we evaluated a cross-system volatility interaction term grounded in Kingman's heavy-traffic queuing formula."*

### Q2: "Why are your peak periods non-consecutive?"
* **Response**: *"Rather than using rigid clock hours, we grouped hours by operational congestion dynamics. Commercial airports experience two distinct daily stress periods driven by entirely different mechanisms: a morning surge (05:00–08:00) caused by concentrated passenger arrival waves while flights depart on time, and an evening surge (14:00–22:00) caused by cascading flight delays across the national airspace system. Unifying them into a bimodal peak regime ensures staffing models address both physical failure modes."*

### Q3: "Why not run the Dynamic Hybrid model all the time if it recovers faster during disruptions?"
* **Response**: *"This reflects the fundamental asymmetric trade-off identified in Hypothesis 1. Model 3 requires closed-loop live data feeds from the checkpoint floor every hour ($y_{t-1}$). Under calm, routine conditions, running live sensor ingestion 24/7 introduces unnecessary IT complexity without meaningful gain. Model 2 delivers comparable routine accuracy ($\text{MASE} = 0.680\text{--}0.700$) as an open-loop model, enabling advance shift planning days ahead without live sensor dependencies."*
