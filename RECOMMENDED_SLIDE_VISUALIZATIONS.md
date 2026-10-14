# Recommended Slide Visualizations Guide: Master Defense Deck
**Author**: Leila Gleich  
**Institution**: Embry-Riddle Aeronautical University  
**Degree**: Master of Science in Aeronautics (MSAA / Gleich 700B)  
**Target Deck**: `master-docs/Master-defense-deck.pptx` (32 Slides, 16:9 Widescreen)  
**Companion Oral Script**: `DEFENSE_PRESENTATION_SCRIPT_25MIN.md`  

---

## 1. Executive Design Philosophy & Visual Principles

The committee defense requires a clean, authoritative, and minimalistic aesthetic suitable for graduate aerospace research. To prevent visual fatigue, presentation slides should adhere to these core principles:

1. **Zero Raw Screenshot Dumps**: Avoid pasting raster screenshots of data tables or whole pages. Instead, use clean native PowerPoint tables, vector SmartArt diagrams, KPI metric callouts, and centered mathematical display equations.
2. **Equation Typography**: Raw LaTeX markup (e.g., `$\bar{W}_q \approx \frac{\rho}{1-\rho}$`) does not render automatically inside PowerPoint text boxes. Format equations using **PowerPoint’s native Math Type** (`Alt + =` on Windows, or `Insert > Equation` on Mac) or clean display typography with formal math symbols.
3. **White Space & Visual Breathing Room**: Replace dense walls of paragraph text and repetitive rounded box borders with high-contrast, structured visual anchors (3-column comparison cards, horizontal chevron process flows, and stat callouts).
4. **Color Palette**:
   - **Primary**: ERAU Deep Navy (`#0A2240`) — Headings, major metric numbers, primary bars.
   - **Accent**: Slate Grey (`#475569`) & Aviation Blue (`#2563EB`) — Subheadings, active states, key equations.
   - **Muted**: Neutral Light Grey (`#F8FAFC`) — Subtle card fills and background contrast.
   - **Alerts**: Dark Green (`#166534`) — Targets met / winners; Dark Amber (`#B45309`) — Brittleness / caveats.

---

## 2. Slide-by-Slide Visual Specifications (Slides 1–32)

### Slide 1: Title Slide
* **Slide Title**: *Evaluating Predictive Techniques to Model Stochastic Airport Passenger Flow*
* **Recommended Visual Architecture**:
  - Full-width dark navy top accent band (`0.25"` height).
  - Centered typographic hierarchy:
    - Kicker: `EMBRY-RIDDLE AERONAUTICAL UNIVERSITY  |  GRADUATE THESIS DEFENSE` (12 pt Bold, `#2563EB`).
    - Main Title: Bold 38 pt Calibri Navy (`#0A2240`).
    - Subtitle: 16 pt Slate Grey (`#475569`).
    - Metadata Block: Candidate name, degree program, and date.
* **Content Elements**: No shapes, no boxes, no screenshots. Clean typographic elegance.

---

### Slide 2: Presentation Roadmap
* **Slide Title**: *Executive Roadmap*
* **Recommended Visual Architecture**:
  - **SmartArt Layout**: Horizontal 6-box chevron or 2-row × 3-column process grid (`Insert > SmartArt > Process > Chevron List` or `Grid Matrix`).
* **Visual Elements**:
  - 6 numbered milestone nodes:
    1. *01: Research Problem & Queuing Friction*
    2. *02: Literature & Model Evolution*
    3. *03: Econometric Data Pipeline*
    4. *04: Empirical Volatility Regimes*
    5. *05: Holdout Benchmarks & Multi-Pillar Testing*
    6. *06: Operational Playbook & Conclusion*
* **Eliminated**: Dense descriptive paragraphs. The speaker's voice carries the details.

---

### Slide 3: The Research Problem (Kingman's Queuing Friction)
* **Slide Title**: *The Terminal Queuing Problem*
* **Recommended Visual Architecture**:
  - **Left 50%**: Centered Native Math Equation Callout Card.
  - **Right 50%**: High-contrast 2-block operational contrast (Rigid Infrastructure vs. Asymmetric Mechanism).
* **Centered Mathematical Formula**:
  $$\bar{W}_q \approx \left(\frac{\rho}{1 - \rho}\right) \cdot \left(\frac{C_a^2 + C_s^2}{2}\right) \cdot \left(\frac{1}{\mu}\right)$$
* **Equation Annotation (Centered beneath)**:
  - $\rho \to 1.0$: Checkpoint lane utilization approaching saturation capacity.
  - $C_a^2$: Arrival flow variance (burstiness). Delay scales *quadratically* with arrival volatility!
  - $\mu$: Service rate per screening lane.
* **Right Block Graphics**:
  - Top Card: **Inflexible Infrastructure** (AIT scanners & TSO rosters cannot expand in real-time).
  - Bottom Card: **Temporal Asynchrony** (Passenger arrivals lead flight banks by 2 hours; departure delays lag and cascade into evening banks).

---

### Slide 4: Research Purpose & Objectives
* **Slide Title**: *Research Purpose & Operational Objectives*
* **Recommended Visual Architecture**:
  - **SmartArt Layout**: 3 Horizontal Arrow Cards or 3 Vertical Pillar Cards (`Insert > SmartArt > Process > Horizontal Process`).
* **3 Visual Anchor Pillars**:
  1. **Pivot to Volatility**: Modeling within-day dispersion ($\sigma_{\text{TSA}}$) and scale-free burstiness ($CV_{\text{TSA}}$) rather than static headcounts.
  2. **Multi-Paradigm Evaluation**: Benchmarking deterministic flight schedules, supervised ML, and 2-stage dynamic hybrids against daily persistence.
  3. **Context-Aware Optimality**: Establishing that model superiority depends strictly on operational priorities (routine vs. shock vs. transfer).

---

### Slide 5: Research Question (RQ₁)
* **Slide Title**: *Primary Research Question*
* **Recommended Visual Architecture**:
  - **Top Card**: Prominent quoted italicized callout block containing the formal question statement.
  - **Bottom 3 Cards**: Horizontal triad representing the 3 operational priority branches.
* **Bottom Triad Breakdown**:
  - Card 1: **Robustness** (Routine on-time baseline accuracy, delays $< 15$ min, 0 cancellations).
  - Card 2: **Resilience** (Disruption shock stability during convective IROPS, delays $\ge 45$ min).
  - Card 3: **Generalizability** (Zero-shot spatial portability across unfamiliar airport concourse geometries).

---

### Slide 6: Master Hypothesis: The Asymmetric Trade-Off (H₁)
* **Slide Title**: *Hypothesis: The Asymmetric Trade-Off ($H_1$)*
* **Recommended Visual Architecture**:
  - **Top Anchor Banner**: Formal $H_1$ statement: *Across candidate paradigms, no individual model is universally dominant across all three performance measures.*
  - **Bottom SmartArt / 3 Comparative Cards**:
    - **$H_{1a}$ (Robustness)**: Machine Learning & Dynamic Hybrids achieve $\text{MASE} < 0.700$. Schedules fail.
    - **$H_{1b}$ (Resilience)**: Dynamic Hybrid is sole resilient winner ($R_{\text{MASE}} \approx 1.05$). ML collapses ($R = 2.14$).
    - **$H_{1c}$ (Generalizability)**: Deterministic schedule wins zero-shot transfer ($\Delta\text{MASE} \le 10\%$). Hybrids fail.

---

### Slide 7: Evaluative Trio (Multi-Pillar Framework)
* **Slide Title**: *The Multi-Pillar Performance Framework*
* **Recommended Visual Architecture**:
  - **Left 50%**: Native Triangle Diagram or 3-Axis Radar Illustration representing the Trade-Off Space.
  - **Right 50%**: 3 Horizontal Specification Strips.
* **Specification Strips**:
  - **Robustness**: Target $\text{MASE} < 0.700$, lowest $\text{RMSE}_{\text{routine}}$.
  - **Resilience**: Target $R_{\text{MASE}} \approx 1.00$, $\text{TTR} < 4.0\text{ h}$.
  - **Generalizability**: Target $\text{RTR} \le 1.05$, $\Delta\text{MASE} \le 10.0\%$.

---

### Slide 8: Chronological Evolution of Literature
* **Slide Title**: *Evolution of Terminal Flow Literature*
* **Recommended Visual Architecture**:
  - **Top SmartArt Timeline**: 4-node horizontal timeline (`Insert > SmartArt > Timeline > Basic Timeline`).
    - *1990s: Deterministic Flight Bank Schedules*
    - *2000s: Discrete-Event Micro-Simulation (Simio, CAST)*
    - *2015+: Supervised Machine Learning (GBRT, Random Forests)*
    - *Today: Dynamic Two-Stage Sequential Hybrids*
  - **Bottom Graphic**: 2-Column Paradigm Trade-off Table (Strengths vs. Operational Shortcomings).

---

### Slide 9: Literature Gap: Volatility vs. Volume
* **Slide Title**: *The Static Fallacy in Terminal Modeling*
* **Recommended Visual Architecture**:
  - **Left Card**: Centered Mathematical Formula for Relative Volatility.
    $$CV_{\text{TSA}} = \frac{\sigma_{\text{TSA}}}{\mu_{\text{TSA}}}$$
    *(Dimensionless arrival burstiness normalizing scale across mega vs. medium hubs).*
  - **Right Visual Contrast Card**:
    - Static Headcount ($y_t$ vs. Delays): $r = -0.062, p = 0.77 \implies R^2 = 2.5\%$ (Fails!).
    - Volatility Dispersion ($CV_{\text{TSA}}$ vs. $CV_{\text{delay}}$): $r = +0.4373, p < 0.05 \implies R^2 = 19.1\%$ (Strong coupling!).

---

### Slide 10: Deterministic Flight Schedules & Classical Queueing (Model 1)
* **Slide Title**: *Deterministic Flight Schedules & Classical Queueing*
* **Recommended Visual Architecture**:
  - **Left Card**: Centered Convolution Formula.
    $$\widehat{Y}_t = \sum_{i} \left[\text{Seats}_i \cdot (1 - S_{\text{connect}}) \cdot P(t - \text{DEP}_i)\right]$$
    *Convolving scheduled flight banks across ACRP Report 40 lognormal show-up curves $P(\tau)$.*
  - **Right Card**: Operational Strengths & Fatal Flaws (100% transparent and interpretable, but completely blind to flight delay ripples and taxi queues).

---

### Slide 11: Shift to Micro-Simulation Modeling
* **Slide Title**: *The Shift to Micro-Simulation Modeling*
* **Recommended Visual Architecture**:
  - **Side-by-Side Pro/Con Balance**: 2 Clean Vertical Cards (`Pros` in soft green outline, `Cons` in soft amber outline).
* **Content Breakdown**:
  - **High Spatial Resolution (Strengths)**: Resolves individual passenger walking, PreCheck vs. standard lane splitting, and concourse geometry.
  - **The Dispatch Latency Barrier (Shortcomings)**: 20–45 minute re-run times; hundreds of micro-parameters that become obsolete during convective storm ground stops.

---

### Slide 12: Supervised Machine Learning (Model 2)
* **Slide Title**: *Supervised Machine Learning (Model 2)*
* **Recommended Visual Architecture**:
  - **Left 30%**: Large KPI Callout: `24` (BTS OTP & Flight Schedule Features).
  - **Right 70%**: Dual Operational Regime Breakdown (Routine vs. Shock).
* **Right Panel Elements**:
  - **Routine Flow**: Delivers low-compute Pareto fit ($\text{MASE} = 0.680\text{--}0.700$, zero feedback latency).
  - **The Empty Checkpoint Fallacy (Shock Collapse)**: When ground stops cancel flights, ML predicts zero volume while thousands of delayed passengers pack terminal lobbies.

---

### Slide 13: Sequential Two-Stage Hybrids (Model 3)
* **Slide Title**: *Sequential Two-Stage Hybrid Architectures (Model 3)*
* **Recommended Visual Architecture**:
  - **Top Centered Formula Card**:
    $$\widehat{Y}_t = M_{\text{base}}(\text{Schedule}_t, \mathbf{X}_t) + \alpha \cdot (Y_{t-1} - \widehat{Y}_{t-1})$$
  - **Bottom 2 Architectural Blocks**:
    - *Stage 1 (Operational Baseline)*: Captures macro flight schedules, aircraft gauge, and seasonal rhythms.
    - *Stage 2 (Real-Time Floor Feedback)*: Injects prior-hour queue innovation ($e_{t-1}$), instantly overriding stale schedules during storm disruptions.

---

### Slide 14: COVID-19 Demarcation & Sample Stability
* **Slide Title**: *The Structural Impact of COVID-19 Demarcation*
* **Recommended Visual Architecture**:
  - **3 Metric KPI Callout Cards**:
    1. **May 1, 2022**: Federal mask mandate dissolved; structural demarcation cutoff.
    2. **Chow Test $F = 1.42$**: $p = 0.18$ (Fails to reject null; confirms structural time-series stability across 44 months).
    3. **84.7% Load Factor**: Full recovery to pre-pandemic operational baseline.
* **Bottom Note**: CUSUM recursive residuals prove that 2020–2021 data contains severe distortion and must be purged.

---

### Slide 15: Why Aviation Demands Dynamic Performance Measures
* **Slide Title**: *Why Aviation Demands Dynamic Performance Measures*
* **Recommended Visual Architecture**:
  - **SmartArt Triad**: 3 Horizontal Visual Banners highlighting the operational risk of relying on global annual RMSE.
* **3 Risk Dimensions**:
  1. **Nominal Operations**: Tolerant of small variance; priority is low computational latency.
  2. **Severe Storm Shocks (IROPS)**: Airport crises occur here; algorithms must survive the Empty Checkpoint Fallacy.
  3. **New Concourse Transfer**: Capital expansion cannot wait 12 months for local model retraining.

---

### Slide 16: Research Methodology Overview
* **Slide Title**: *Research Methodology Overview*
* **Recommended Visual Architecture**:
  - **SmartArt Layout**: 5-Stage Horizontal Chevron Flow (`Insert > SmartArt > Process > Chevron Process`).
* **5 Canonical ERAU Chapters / Stages**:
  - `3.1 Approach`: Comparative evaluation of 4 paradigms across 3 pillars.
  - `3.2 Sample`: 4-tier filtering isolating 9 airports & 12 carrier-exclusive complexes.
  - `3.3 Sources`: 67.2M raw records conformed to 42.1M Star Schema rows.
  - `3.4 Validity`: DB1B connecting deflator, carrier isolation, 168-h purge buffer.
  - `3.5 Treatment`: Out-of-time 2025 holdout and Diebold-Mariano tests.

---

### Slide 17: Forecasting Model Families & Baseline Control
* **Slide Title**: *Forecasting Model Families & Baseline Control*
* **Recommended Visual Architecture**:
  - **4-Column Clean Table / Cards**:
    - **Baseline Control**: Daily Persistence ($\widehat{Y}_t = Y_{t-24}$, non-parametric $\text{MASE} \equiv 1.000$).
    - **Model 1**: Deterministic Flight Schedule (convolving show-up curves over scheduled banks).
    - **Model 2**: Supervised Machine Learning (Tweedie gradient-boosted trees + 24 OTP features).
    - **Model 3**: Dynamic Two-Stage Hybrid (Schedule base + real-time 1-step error innovation).

---

### Slide 18: Four-Phase Research Lifecycle
* **Slide Title**: *Four-Phase Research Execution Lifecycle*
* **Recommended Visual Architecture**:
  - **4 Grid Cards (Table 3.1 Architecture)**:
    - *Phase 1 (Data Foundation & ETL)*: TSA FOIA, BTS OTP, T-100, DB1B conformed into DuckDB Star Schema.
    - *Phase 2 (Econometric Filtering)*: 4-tier funnel isolating 12 carrier-exclusive screening environments.
    - *Phase 3 (Feature Engineering & Calibration)*: 24 OTP features, 84-cell interaction grid ($N_{\text{train}} \ge 50$ in 98.8% of cells).
    - *Phase 4 (Multi-Pillar Hypothesis Testing)*: Out-of-time 2025 holdout across Robustness, Resilience, Generalizability.

---

### Slide 19: Methodological Safeguards & Leakage Prevention
* **Slide Title**: *Methodological Safeguards & Data Integrity*
* **Recommended Visual Architecture**:
  - **2 × 2 Clean Matrix**:
    - **7-Day Purge Buffer**: 168-hour embargo between training and test holdout eliminates autoregressive memory leakage.
    - **Connecting Passenger Deflator**: Scales seat capacity by local originating share ($1 - S_{\text{connect}}$) via BTS DB1B.
    - **Carrier Screening Isolation**: Eliminates multi-carrier passenger mixing by selecting dedicated single-airline terminals.
    - **Strict Information Availability ($t-1$)**: Zero lookahead bias; models ingest only telemetry realized before prediction hour.

---

### Slide 20: Chapter IV Empirical Results Architecture
* **Slide Title**: *Chapter IV Empirical Results Architecture*
* **Recommended Visual Architecture**:
  - **Numbered Step-Ladder Flow**:
    - `Section 4.1`: Exploratory Data Analysis & The Values vs. Volatility Discovery.
    - `Section 4.2`: Four-Tier Filtering & Factorial Experimental Cohort Specification.
    - `Section 4.3`: Model Development, Feature Engineering, and 2025 Holdout Execution.
    - `Section 4.4`: Multi-Pillar Hypothesis Testing Across the Evaluative Trio.

---

### Slide 21: Descriptive Statistics: 9-Airport Cohort vs. Top 25
* **Slide Title**: *Empirical Baseline: 9-Airport Cohort vs. Top 25*
* **Recommended Visual Architecture**:
  - **Top Row (4 Big-Number KPI Stat Blocks)**:
    - `+16.9%`: Scheduled Flight Density (224,576 annual flights vs. 192,160).
    - `+14.1%`: Higher Cancellation Rate (1.63% vs. 1.43%).
    - `+25.0%`: True Originating Demand (16.4M vs. 13.1M pax).
    - `+5.8%`: Elevated Arrival Volatility ($CV_{\text{TSA}} = 0.8728$ vs. $0.8250$).
  - **Bottom Card**: Summary establishing that the 9-airport cohort represents genuine high-congestion operational stress fronts.

---

### Slide 22: The Four-Tier Purposive Filtering Funnel
* **Slide Title**: *The Four-Tier Purposive Filtering Pipeline*
* **Recommended Visual Architecture**:
  - **Funnel / Stepped Process Flow (`Table 3.2`)**:
    1. **Macro Tier (Commercial Scale)**: 450+ airports $\to$ Top 25 large hubs (68% of commercial traffic).
    2. **Meso Tier (Carrier Presence)**: Screened for continuous American, Delta, United presence (Eliminated JFK).
    3. **Micro Tier (Physical Isolation)**: Filtered out consolidated checkpoints (Eliminated SLC).
    4. **Cohort Tier (Factorial Balance)**: 9 airports, 12 carrier-exclusive complexes, 4 operational clusters.

---

### Slide 23: 9-Airport Experimental Cohort Specification
* **Slide Title**: *The 9-Airport Experimental Cohort Specification*
* **Recommended Visual Architecture**:
  - **Clean Native 3 × 3 Airport Badge Grid (`Table 4.6`)**:
    - **ATL**: Delta Domestic South
    - **BOS**: Delta A / American B
    - **DFW**: American A, B, C
    - **DTW**: Delta McNamara
    - **EWR**: United Terminal C
    - **LAX**: Delta 3 / AA 4 / United 7
    - **LGA**: Delta Terminal C
    - **ORD**: United T1 / American T3
    - **PHL**: American Terminals B/C
  - **Summary**: Full balance across American (5), Delta (5), and United (4).

---

### Slide 24: Annual Seasonal Volatility Regimes
* **Slide Title**: *Annual Seasonal Volatility Regimes*
* **Recommended Visual Architecture**:
  - **4 Macro Season Cards (`Table 4.3b`)**:
    1. **Off-Peak Winter (Weeks 1–8, 45–46)**: Low volume, minimal delays, high baseline predictability.
    2. **Mid-Peak Spring (Weeks 9–21, 36–44)**: Elevated business travel, balanced flight banks.
    3. **Summer Convective Peak (Weeks 22–35)**: Highest delay dispersion ($\sigma_{\text{delay}} = 68.4$ min), thunderstorms, peak $CV_{\text{TSA}}$.
    4. **Holiday Travel Peaks (Weeks 47–52)**: Maximum passenger headcounts, leisure travelers, non-consecutive surges.

---

### Slide 25: Day-of-Week Volatility & Bimodal Diurnal Peaks
* **Slide Title**: *Day-of-Week Volatility & Bimodal Diurnal Peaks*
* **Recommended Visual Architecture**:
  - **Left Card: Day-of-Week Operational Archetypes**:
    - *Monday (Outbound Business Surge)*: Peak early morning TSA throughput (05:00–08:00), minimal departure delays.
    - *Sunday (Inbound Leisure Return)*: Evening aircraft delay cascades; flight delay standard deviation expands by $+35\%$.
  - **Right Card: Bimodal Diurnal Asynchrony**:
    - *Morning Peak (05:00–08:00)*: Screening surges to 11,380 pax/hr; near-zero delays.
    - *Evening Peak (14:00–22:00)*: Screening moderates; aircraft departure delays exceed 63 minutes.

---

### Slide 26: Empirical Lead-Lag Passenger Show-Up Dynamics
* **Slide Title**: *Empirical Passenger Show-Up Curve Convolution*
* **Recommended Visual Architecture**:
  - **Centered Equation Card**:
    $$R^2(t+2) = 0.5347 \quad \text{vs.} \quad R^2(t) = 0.1982$$
  - **Key Empirical Bullet Highlights**:
    - Contemporaneous flight schedules ($t$) fail completely ($R^2 < 20\%$).
    - Checkpoint arrival correlation peaks at a 2-hour lead ($t+2$), explaining $53.5\%$ of arrival variance ($F = 142.80$).
    - Validates ACRP Report 40 lognormal show-up dynamics for terminal planning.

---

### Slide 27: Certified 2025 Holdout Benchmarks (Table 4.10)
* **Slide Title**: *Certified 2025 Out-of-Time Holdout Benchmarks*
* **Recommended Visual Architecture**:
  - **Clean Native PowerPoint Table**:

| Paradigm | Model Name | Test $R^2$ | RMSE (pax/hr) | MAE (pax/hr) | Test MASE | Forecast Bias | Target Status |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **Baseline Control** | Daily Persistence ($t-24$) | 0.6719 | 253.6 | 179.3 | 1.000 | -0.7 | Empirical Benchmark |
| **Model 1** | Deterministic Schedule | 0.4980 | 313.4 | 215.9 | 0.945 | -42.1 | Passed ($\text{MASE} < 1.0$) |
| **Model 2** | Supervised Machine Learning | 0.6178 | 273.5 | 178.0 | 0.779 | -18.4 | Passed ($\text{MASE} < 0.850$) |
| **Model 3** | Dynamic Two-Stage Hybrid | **0.7483** | **222.1** | **142.8** | **0.662** | **-8.5** | **Decisive Holdout Winner** |

---

### Slide 28: Multi-Pillar Hypothesis Testing (Table 4.11 / Table 5.4)
* **Slide Title**: *Multi-Pillar Hypothesis Testing: The Asymmetric Trade-Off*
* **Recommended Visual Architecture**:
  - **3 Distinct Evaluation Pillar Cards**:
    - **Dimension 1: Robustness (Nominal Rhythms)**:
      - Winner: Model 3 ($\text{RMSE} = 222.1, \text{MASE} = 0.662$); Model 2 wins routine Pareto efficiency ($\text{MASE} = 0.680\text{--}0.700$). Confirms **$H_{1a}$**.
    - **Dimension 2: Resilience (Convective IROPS Shocks)**:
      - Winner: Model 3 ($R_{\text{MASE}} = \mathbf{1.05}$, $\text{TTR} = \mathbf{2.8\text{ h}}$). Model 2 collapses ($R = 2.14$). Confirms **$H_{1b}$**.
    - **Dimension 3: Generalizability (Zero-Shot Spatial Portability)**:
      - Winner: Model 1 ($\text{RTR} = \mathbf{1.04}, \Delta\text{MASE} = \mathbf{+4.0\%}$). Model 3 fails ($\text{RTR} = 1.19, \Delta\text{MASE} = +21.5\%$). Confirms **$H_{1c}$**.

---

### Slide 29: Deep-Dive Dimension 2: Resilience & The Empty Checkpoint Fallacy
* **Slide Title**: *Dimension 2: Disruption Resilience & Shock Recovery*
* **Recommended Visual Architecture**:
  - **Centered Math Formula**:
    $$R_{\text{MASE}} = \frac{\text{MASE}_{\text{shock}}}{\text{MASE}_{\text{routine}}}$$
  - **Side-by-Side Mechanism Explanation**:
    - **The Empty Checkpoint Fallacy (Model 2 Collapse)**: Storms cause ground stops $\to$ flights cancelled from airline feed $\to$ decision tree predicts zero passengers $\to$ terminal lobbies overwhelmed with stranded travelers ($R = 2.14$).
    - **Hybrid Error Innovation Rescue (Model 3)**: Live prior-hour floor count ($Y_{t-1}$) detects stranded passengers $\to$ lifts forecast back to reality ($R = 1.05, \text{TTR} = 2.8\text{ h}$).

---

### Slide 30: Deep-Dive Dimension 3: Generalizability & Spatial Transfer
* **Slide Title**: *Dimension 3: Generalizability & Spatial Transfer*
* **Recommended Visual Architecture**:
  - **Centered Math Formula**:
    $$\text{RTR} = \frac{\text{RMSE}_{\text{transfer}}}{\text{RMSE}_{\text{in-sample}}}$$
  - **Comparison Card (Newark EWR $\to$ LaGuardia LGA Zero-Shot)**:
    - **Model 1 (Deterministic Physics)**: $\text{RTR} = 1.04, \Delta\text{MASE} = +4.0\%$ (Passes target). Passenger arrival psychology is invariant across airports!
    - **Model 3 (Dynamic Hybrid)**: $\text{RTR} = 1.19, \Delta\text{MASE} = +21.5\%$ (Decisively fails). Supervised decision trees overfit to Newark's unique taxiways, concourse geometry, and bank structures.

---

### Slide 31: Real-World Implementation: The Operator's Playbook
* **Slide Title**: *Real-World Aviation Application: The Operator's Playbook*
* **Recommended Visual Architecture**:
  - **3 Implementation Action Cards**:
    1. **Dynamic Checkpoint Rostering**: Abandon static tables. Roster TSA lanes using $t+2$ flight bank convolutions combined with conformal $q85$ safety cushions (+1.2 lanes).
    2. **Connecting Ratio Deflation**: Dynamically scale flight seats by airline O&D ticket survey data (BTS DB1B) to stop over-staffing connecting hubs.
    3. **Regime-Switched Gated Engine**: Deploy pure ML (Model 2) during nominal operations for zero latency; automatically switch to Dynamic Hybrid (Model 3) when delays $\ge 45$ min.

---

### Slide 32: Research Synthesis & Final Conclusion
* **Slide Title**: *Research Synthesis & Concluding Takeaway*
* **Recommended Visual Architecture**:
  - **Centered Headline**: *Transforming Airport Security Screening from Reactive Firefighting to Resilient Stochastic Synchronization*
  - **4 Bulleted Takeaways**:
    - Volatility ($\sigma_{\text{TSA}}, CV_{\text{TSA}}$), not static volume, governs heavy-traffic queuing under Kingman's law.
    - Formalized and proved the Asymmetric Trade-Off ($H_1$): no single model wins all dimensions.
    - Real-time error feedback ($t-1$) defeats the Empty Checkpoint Fallacy during severe convective storms.
    - The Regime-Switched Gated Engine delivers operational resilience without sacrificing routine compute efficiency.
  - **Closing Line**: *Thank you for your guidance, mentorship, and support.*

---

## 3. Checklist for Clean PowerPoint Execution

When building or editing the slides in PowerPoint:
- [ ] Ensure all mathematical equations use native PowerPoint Math (`Alt + =`) with display styling.
- [ ] Ensure no raster table screenshots are pasted; format tables using PowerPoint native tables with clean horizontal borders (APA 7 style).
- [ ] Maintain consistent 16:9 widescreen layout (`13.333"` × `7.5"`).
- [ ] Keep margins at least `0.8"` on left/right and `0.4"` on top/bottom to allow ample white space.
- [ ] Ensure slide typography strictly pairs Calibri (sans-serif headers and body) with Georgia or Cambria Math (equations).
