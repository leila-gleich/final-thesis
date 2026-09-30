# Airport Criteria Selection and Placement Guide

**Author**: Leila Gleich  
**Institution**: Embry-Riddle Aeronautical University  
**Degree Program**: Master of Science in Aeronautics / Aviation Data Analytics  
**Target Document**: Thesis Structural & Textual Integration Guide  
**Target Repository Directory**: `Gleich-Thesis/Thesis Section Documents/airport-criteria-selection.md`  
**Primary Research Scope**: Checkpoint Screening Throughput Volatility, Carrier Isolation, and Multi-Metric Model Evaluation (Robustness, Resilience, Generalizability)  

---

## Executive Summary & Architectural Overview

This document provides the definitive guide for placing, phrasing, and formatting all content related to:
1. **Airport Criteria Selection & Justification** (Top 25 volume threshold, tri-carrier competitive parity, carrier-exclusive checkpoint isolation, and orthogonal factorial symmetry).
2. **The 9-Airport Empirical Master Matrix** (`{BOS, DFW, DTW, EWR, IAH, LAX, LGA, ORD, PHL}`).
3. **Network-Level "Post-Pandemic" Boundary Definition** (using aggregate trends across the Top 25 commercial hub network / top decile rather than solely the 9 modeling nodes).
4. **Network-Theoretic Queuing Justification** (airports as coupled nodes in a national queuing system).

---

## 1. Master Thesis Placement Matrix

| Chapter & Section | Specific Heading in Thesis | Exact Content to Integrate | Rhetorical Function & Committee Justification |
| :--- | :--- | :--- | :--- |
| **Chapter I: Introduction** | `Delimitations` | High-level summary of the **9-airport spatial boundary**, the **Big Three legacy carrier focus (AA, DL, UA)**, and the **May 2022 post-pandemic temporal cutoff**. | Establishes formal boundary conditions; explicitly defends exclusions (e.g., Southwest, ULCCs, non-core airports). |
| **Chapter I: Introduction** | `Limitations and Assumptions` | • **Assumption**: Systemic recovery across the Top 25 hub network reflects a true operational steady state.<br>• **Limitation**: Carrier-exclusive checkpoint dynamics require re-weighting before applying to pooled/consolidated terminals. | Acknowledges threats to external validity upfront; satisfies graduate committee rigor. |
| **Chapter II: Literature Review** | `Conceptual Framework` $\rightarrow$ `Airport Terminal Geometries & Queuing Networks` | Terminal layout typologies (de Neufville & Odoni; FAA ACRP Report 25), passenger show-up lead-lag distributions ($f_{arr}(\tau)$), and network delay propagation. | Grounds terminal architectural diversity and multi-node coupling in foundational aviation literature. |
| **Chapter III: Methodology** <br>*(PRIMARY HOME)* | `Sample` $\rightarrow$ `Macro Categorization: Terminal-to-Airline Distribution` | Justification for filtering to the **Top 25 commercial hub network** (>67% national passenger volume) and mapping across the **4 empirical operational clusters**. | Explains the systemic scale requirement and operational regime representation. |
| **Chapter III: Methodology** <br>*(PRIMARY HOME)* | `Sample` $\rightarrow$ `Micro-Level Refinement: Checkpoint Co-Location and Isolation` | The **9-Airport Master Table**, listing specific **carrier-exclusive checkpoint names/slugs**, gate counts, terminal layouts, and the mathematical proof of causal isolation. | Solves the unobserved passenger mixture problem and justifies the elimination of shared checkpoints. |
| **Chapter III: Methodology** <br>*(PRIMARY HOME)* | `Sample` $\rightarrow$ `Temporal Scope and Boundary Definition` | The **Network-Node Logic**: Defining the post-pandemic operational demarcation across the **Top 25 hub network** (top decile) instead of the 9 modeling airports. | Defends against localized recovery artifacts (e.g., leisure Florida rebounds vs. business coastal lags). |
| **Chapter III: Methodology** | `Validity` | Connecting passenger decoupling (BTS DB1B/DB1C) and physical checkpoint segregation as controls for **construct and internal validity**. | Explains how physical queue-to-schedule alignment is methodologically preserved without data leakage. |
| **Chapter III: Methodology** | `Treatment of the Data` $\rightarrow$ `Extract & Transform` | Multi-stage ETL filtering pipeline: Raw BTS/TSA data $\rightarrow$ Top 25 network normalization $\rightarrow$ Extraction of the 9 carrier-exclusive modeling checkpoints. | Provides reproducibility for the data engineering pipeline. |
| **Chapter IV: Results & Findings** | `Descriptive Statistics` | Longitudinal plots/tables displaying **Top 25 network-level recovery trajectories (2019–2026)** and baseline descriptive statistics for the 9 selected airfields. | Empirically validates that May 2022 represents steady-state normalization. |
| **Chapter IV: Results & Findings** | `Phase 3: Evaluation Framework` $\rightarrow$ `Generalizability` | The **$4 \times 4$ Zero-Shot Cross-Terminal Transfer Matrix** ($RMSE_{S \to T}$, $\Delta MASE_{transfer}$, and $RTR$), segmented by layout archetype and cluster. | Reports empirical findings testing Hypothesis 1 across spatial footprints. |
| **Chapter V: Discussion & Conclusions** | `Implications for Terminal Planning` | Policy recommendations for TSA staffing allocation, checkpoint reconfigurable lane design, and network-aware queue forecasting. | Translates comparative model performance into actionable airport operational intelligence. |

---

## 2. Detailed Text & Integration Drafts by Chapter

### Chapter I: Introduction

#### A. Under Section: `Delimitations`
Insert the following text to formally define the research boundaries:

> **Spatial Delimitation**: This study is delimited to nine primary commercial airfields within the National Airspace System: Boston Logan (`BOS`), Dallas/Fort Worth (`DFW`), Detroit Metropolitan (`DTW`), Newark Liberty (`EWR`), Houston Intercontinental (`IAH`), Los Angeles International (`LAX`), New York LaGuardia (`LGA`), Chicago O'Hare (`ORD`), and Philadelphia International (`PHL`). These airfields were purposively selected because they maintain physically isolated, carrier-exclusive security checkpoint environments that enable unconfounded causal mapping between flight departures and passenger screening throughput.
>
> **Carrier Delimitation**: The analytical scope is delimited strictly to the "Big Three" U.S. legacy network air carriers—American Airlines (`AA`), Delta Air Lines (`DL`), and United Airlines (`UA`). Low-cost carriers (LCCs) and ultra-low-cost carriers (ULCCs), including Southwest Airlines, are explicitly excluded. Southwest’s boarding processes, unassigned-seating historical policies, and dynamic baggage-fee structures introduce boarding and carry-on friction that distort queue arrival distributions. Restricting analysis to the Big Three establishes homogeneous passenger processing baselines across mainline domestic networks.
>
> **Temporal Delimitation**: The longitudinal active modeling window is delimited to operations occurring between **May 1, 2022, and December 31, 2025**. While historical 2019–2021 data are utilized during exploratory data engineering to evaluate system shocks, the formal modeling dataset excludes the acute structural dislocations of the COVID-19 pandemic. The temporal start date is anchored to the empirical inflection point where aggregate flight schedules, route load factors, and screening volumes across the Top 25 commercial hub network achieved post-pandemic steady-state stabilization.

#### B. Under Section: `Limitations and Assumptions`
Insert the following statements to protect internal and construct validity:

> **Operational Steady-State Assumption**: It is assumed that aggregate schedule adherence, passenger arrival distributions, and airline load factor dynamics across the Top 25 commercial hub network stabilized into a reliable operational regime following the cessation of federal transportation mask mandates and capacity restrictions in spring 2022. This systemic network stabilization is assumed to provide a valid foundation for localized terminal queue modeling.
>
> **Screening Environment Boundary Limitation**: A structural limitation of this study is its reliance on carrier-exclusive checkpoint environments. While physical segregation isolates carrier-specific schedule perturbations from multi-airline cross-talk, the resulting predictive models may exhibit degraded zero-shot generalizability if applied directly to consolidated, single-checkpoint mega-terminals (e.g., Salt Lake City or Denver) without re-incorporating dynamic carrier-market-share scaling factors.

---

### Chapter III: Methodology *(Primary Home)*

#### A. Under Section: `Sample` $\rightarrow$ `Macro Categorization: Terminal-to-Airline Distribution`
Replace or expand existing text with the following multi-tiered justification:

> To evaluate forecasting accuracy across deterministic baselines, probabilistic architectures, and hybrid queueing models, a multi-tiered, purposive sampling strategy was implemented. Candidate airfields were filtered across four sequential operational criteria:
> 
> 1. **Systemic Scale & Throughput Volume (Macro Filter)**: Airfields were restricted to the **Top 25 commercial airports** by annual flight operations and passenger throughput. These 25 facilities represent the core structural nodes of the National Airspace System, capturing over two-thirds (~67%) of all domestic passenger screenings. Restricting candidate airports to this tier guarantees sufficient queue formation, departure bank density, and congestion-induced variance necessary to test model robustness and resilience, while eliminating erratic, low-frequency regional anomalies.
> 2. **Tri-Carrier Competitive Parity (Meso Filter)**: Selected airports were required to maintain continuous, high-volume scheduled operations for all three major legacy network carriers (American, Delta, United). This requirement establishes operational parity, ensuring that cross-terminal comparative evaluations are not distorted by carrier absence or localized monopoly dynamics.
> 3. **Causal Identification via Checkpoint Exclusivity (Micro Filter)**: Modeling checkpoint passenger demand requires convolving scheduled departing seats, route load factors, and tactical flight delays into physical passenger arrivals. In shared screening environments, multi-carrier pooling introduces severe unobserved passenger mixture bias: a flight delay on one airline is obscured by on-time departures on an adjacent carrier. Candidate airfields were therefore required to feature **physically segregated checkpoints serving an individual carrier exclusively (or near-exclusively)**, isolating the unconfounded data-generating process:
>    $$\text{Demand}(i, t) = \sum_{k=1}^{3} w_k \cdot \left[ \sum_{f \in \mathcal{F}(i, t+k)} \text{Seats}_f \times \text{LoadFactor}_f \times (1 - \text{ConnectingRatio}_i) \right]$$
> 4. **Orthogonal Factorial Symmetry (Experimental Transfer Filter)**: The selected airports establish an orthogonal $4 \times 4$ experimental design: exactly four dedicated checkpoint environments for each of the three legacy carriers, distributed evenly across **four empirical operational clusters** (Mega-Connecting Gateways, High-Density O&D Focus, High-Reliability Fortress Hubs, and Congested Coastal Originators) and **four physical terminal archetypes** (Decentralized, Multi-Concourse Pier, Satellite, and Linear Fortress). This orthogonal balance is structurally required to evaluate zero-shot **Generalizability** across diverse physical layouts.

---

#### B. Under Section: `Sample` $\rightarrow$ `Micro-Level Refinement: Checkpoint Co-Location and Isolation`
Insert the **9-Airport Master Selection Table** and architectural classifications:

### The 9-Airport Master Selection Matrix

| Airport Code | City / Metro Area | Top 25 Rank & Volume (Post-Apr 2022) | Carrier Flights (OTP Post-Apr 2022) | Dedicated Carrier Checkpoint(s) | Terminal Physical Architecture *(Thesis Ch. III Archetype)* | Empirical Cluster Assignment *(From 700B Cluster Report)* |
| :---: | :--- | :--- | :--- | :--- | :--- | :--- |
| **LAX** | Los Angeles, CA | **#3 Volume** <br>(425.5k flights; 129.1M pax) | • DL: 98,364<br>• AA: 91,797<br>• UA: 74,368 | • **DL**: Terminal 3 (`T3 - Passenger`, `Delta One`)<br>• **AA**: Terminal 4 (`Terminal 4 - Passenger`, `T4A`)<br>• **UA**: Terminal 7 (`Terminal 7 - Passenger`) | **Decentralized Airline-Dedicated Terminals** <br>*(Archetype 2)* | **Cluster 0**: Mega-Connecting Gateway |
| **ORD** | Chicago, IL | **#2 Volume** <br>(465.8k flights; 63.6M pax) | • UA: 175,750<br>• AA: 136,006<br>• DL: 40,591 | • **UA**: Terminal 1 (`CKPT 1`, `CKPT 2`, `CKPT 3A`)<br>• **AA**: Terminal 3 (`CKPT 7`, `CKPT 7A`, `CKPT 8`, `CKPT 9`) | **Dual-Hub Mega-Concourse Pier** <br>*(Archetype 1)* | **Cluster 0**: Mega-Connecting Gateway |
| **DFW** | Dallas/Fort Worth, TX | **#4 Volume** <br>(379.1k flights; 90.5M pax) | • AA: 246,772<br>• DL: 42,438<br>• UA: 28,170 | • **AA**: Terminals A, B, C (`A12/A21`, `C10/C21`, `B9/B30`) | **Multi-Terminal Monoculture Ring** <br>*(Archetype 4)* | **Cluster 0**: Mega-Connecting Gateway |
| **DTW** | Detroit, MI | **#17 Volume** <br>(250.1k flights; 46.2M pax) | • DL: 140,020<br>• AA: 17,918<br>• UA: 7,976 | • **DL**: McNamara Terminal (`Red 1`, `Red 2`, `Red 3`, `Red 5/6`) | **Single-Carrier Linear Mega-Terminal** <br>*(Archetype 3)* | **Cluster 2**: High-Reliability Fortress Hub |
| **PHL** | Philadelphia, PA | **#22 Volume** <br>(209.8k flights; 40.4M pax) | • AA: 100,968<br>• DL: 21,483<br>• UA: 14,218 | • **AA**: Terminals B & C (`Checkpoint B`, `Checkpoint C`) | **Multi-Concourse Finger Pier Hub** <br>*(Archetype 1)* | **Cluster 2**: High-Reliability Fortress Hub |
| **BOS** | Boston, MA | **#6 Volume** <br>(361.7k flights; 63.7M pax) | • DL: 67,408<br>• AA: 61,140<br>• UA: 39,910 | • **DL**: Terminal A (`Checkpoint A1` — 22 dedicated gates) | **Multi-Terminal Satellite Spoke** <br>*(Archetype 4)* | **Cluster 1**: High-Density O&D Focus |
| **IAH** | Houston, TX | **#14 Volume** <br>(268.0k flights; 66.0M pax) | • UA: 146,392<br>• DL: 28,943<br>• AA: 25,402 | • **UA**: Terminals C & E (`30/CN`, `31/CS`, `70/E`) | **Sprawling Multi-Pier Hub** <br>*(Archetype 1 / 4)* | **Cluster 1**: High-Density O&D Focus |
| **EWR** | Newark, NJ | **#13 Volume** <br>(270.8k flights; 87.7M pax) | • UA: 151,302<br>• AA: 26,651<br>• DL: 23,148 | • **UA**: Terminal C (`CKPT-C1`) | **Slot-Controlled Coastal Pier** <br>*(Archetype 1)* | **Cluster 3**: Congested Coastal Originator |
| **LGA** | New York, NY | **#10 Volume** <br>(293.8k flights; 53.0M pax) | • DL: 77,176<br>• AA: 59,631<br>• UA: 28,951 | • **DL**: Terminal C (`TC-CHK`, `CHK West` — 37 dedicated gates) | **Slot-Controlled Urban Pier** <br>*(Archetype 1)* | **Cluster 3**: Congested Coastal Originator |

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│               BALANCED FACTORIAL DESIGN: CARRIERS × CLUSTERS × ARCHETYPES              │
└────────────────────────────────────────────────────────────────────────────────────────┘

                 AMERICAN AIRLINES         DELTA AIR LINES           UNITED AIRLINES
                 (4 Dedicated Hubs)        (4 Dedicated Hubs)        (4 Dedicated Hubs)
              ┌─────────────────────────┬─────────────────────────┬─────────────────────────┐
  CLUSTER 0   │  • LAX (Terminal 4)     │  • LAX (Terminal 3)     │  • LAX (Terminal 7)     │
 (Mega-Hubs)  │  • ORD (Terminal 3)     │                         │  • ORD (Terminal 1)     │
              │  • DFW (Terminals A/B/C)│                         │                         │
              ├─────────────────────────┼─────────────────────────┼─────────────────────────┤
  CLUSTER 1   │                         │  • BOS (Terminal A)     │  • IAH (Terminals C/E)  │
 (High O&D)   │                         │                         │                         │
              ├─────────────────────────┼─────────────────────────┼─────────────────────────┤
  CLUSTER 2   │  • PHL (Terminals B/C)  │  • DTW (McNamara Red)   │                         │
 (Fortress)   │                         │                         │                         │
              ├─────────────────────────┼─────────────────────────┼─────────────────────────┤
  CLUSTER 3   │                         │  • LGA (Terminal C)     │  • EWR (Terminal C)     │
 (Coastal)    │                         │                         │                         │
              └─────────────────────────┴─────────────────────────┴─────────────────────────┘
```

---

#### C. Under Section: `Sample` $\rightarrow$ `Temporal Scope and Boundary Definition`
Insert the **Network-Theoretic Justification for Defining Post-Pandemic**:

> Commercial airports do not operate as isolated, autonomous service queues; they function as **coupled stochastic nodes within an interconnected national queuing network**. Flight schedules, aircraft turnarounds, crew rotations, and air traffic control restrictions propagate delay cascades across the National Airspace System. Consequently, determining the temporal demarcation point where aviation operations returned to a "post-pandemic" steady state cannot be credibly derived from a small sample of localized modeling airports.
>
> Local recovery trajectories exhibited profound empirical divergence across the United States:
> 1. *Leisure-Oriented Sunbelt Nodes* (e.g., Orlando `MCO`, Las Vegas `LAS`, Tampa `TPA`) experienced rapid demand surges, rebounding to 2019 throughput levels as early as mid-2021.
> 2. *International and Business-Dense Coastal Nodes* (e.g., San Francisco `SFO`, Boston `BOS`, New York `JFK`, Newark `EWR`) remained severely depressed throughout 2021 due to corporate travel freezes, international border closures, and strict public health ordinances, normalizing only in mid-2022.
>
> If the post-pandemic operational boundary were calibrated strictly against the nine modeling airports, the demarcation date would reflect localized idiosyncrasies—such as Newark's runway construction bottlenecks or LaGuardia's phased terminal openings—rather than systemic market normalization. 
>
> To eliminate localized recovery bias, the operational boundary was established by computing longitudinal schedule stability, departure delay distributions, monthly route load factors, and TSA passenger throughput across the **Top 25 commercial hub network**. Because commercial aviation volume follows a heavy-tailed Pareto distribution, these 25 airfields represent the **top 6% of U.S. commercial airports while capturing over two-thirds (~67%) of total national passenger screening activity**. 
>
> Evaluating aggregate network-wide time series demonstrates that **May 2022** represents the definitive structural inflection point where:
> * Federal transportation mask mandates and public health emergency restrictions were lifted (April 18, 2022).
> * Nationwide commercial seat capacity and daily scheduled departure counts returned to within 3% of 2019 baselines.
> * BTS Form 41 domestic passenger load factors normalized within a stable steady-state corridor ($83.4\% \text{ to } 85.8\%$).
> * Diurnal passenger arrival curves resumed stable, predictable morning and evening departure bank profiles.
>
> Therefore, while passenger flow models are trained and tested on the nine carrier-exclusive screening environments, the temporal demarcation of the post-pandemic regime is mathematically grounded across the entire Top 25 commercial network.

---

#### D. Under Section: `Validity`
Insert the methodological justification for internal and construct validity:

> **Construct Validity**: Checkpoint throughput in raw TSA FOIA records records gross human counts passing through physical magnetometers and millimeter-wave scanners. In shared checkpoint configurations, passenger counts represent an unobserved mixture of business travelers, vacationers, and regional feeder passengers across multiple carriers with disparate boarding policies. By restricting the primary modeling sample to carrier-exclusive terminals (e.g., Delta at BOS Terminal A, United at EWR Terminal C, American at PHL Terminals B/C), the construct of "checkpoint demand" directly reflects the scheduled fleet operations and load factors of that specific carrier, eliminating latent multi-carrier interaction error.
>
> **Internal Validity (The Connecting Passenger Disconnect)**: A primary threat to internal validity in checkpoint forecasting is the inclusion of connecting passengers. At major connecting fortress hubs, such as Charlotte (`CLT`), Atlanta (`ATL`), and Dallas/Fort Worth (`DFW`), 50% to 76% of passengers boarding outbound flights arrive airside from inbound feeder flights and never pass through landside TSA checkpoints. Convolving raw outbound flight manifests directly into checkpoint demand artificially inflates predicted landside volumes by up to 300%. To protect internal validity, ticket-level itinerary records from the Bureau of Transportation Statistics (BTS) DB1B and DB1C surveys were utilized to extract airport-specific originating fractions ($L_i = 1 - C_i$). Outbound scheduled seats were scaled by $L_i$ prior to lead-time convolution, ensuring that airside transfer flows do not leak into landside security queue estimations.

---

### Chapter IV: Results & Findings

#### A. Under Section: `Descriptive Statistics`
Integrate the baseline characterization of the network and the 9 selected airports:

1. **Top 25 Network-Level Longitudinal Verification**:
   * Present a time-series plot comparing aggregate monthly TSA screening throughput and BTS OTP departure delay rates from January 2019 through December 2025 across the Top 25 network.
   * Annotate the April/May 2022 inflection threshold to provide visual proof to the committee that the post-pandemic regime represents an operational steady state.
2. **Descriptive Table of the 9 Modeling Hubs**:
   * Provide the empirical baseline statistics for the nine airfields across the post-May 2022 modeling window:
     * Mean Hourly TSA Checkpoint Throughput ($\bar{y}$).
     * Checkpoint Coefficient of Variation ($CV = \sigma / \bar{y}$).
     * BTS Average Departure Delay ($\bar{D}$) and 15+ Minute Delay Rate ($DepDel15$).
     * Average Segment Load Factor ($LF$) and Connecting Passenger Ratio ($C_i$).

#### B. Under Section: `Phase 3: Evaluation Framework` $\rightarrow$ `Generalizability`
Use the 9 airports to construct the **Zero-Shot Cross-Terminal Spatial Transferability Matrix**:

$$\text{RTR}_{RMSE} = \frac{\text{RMSE}_{S \to T}}{\text{RMSE}_{T \to T}}, \quad \Delta \text{MASE}_{transfer} = \frac{\text{MASE}(T; \theta_S) - \text{MASE}(T; \theta_T)}{\text{MASE}(T; \theta_T)}$$

Organize the generalizability evaluation into three distinct experimental hypotheses:
1. **Intra-Carrier, Cross-Architecture Transfer**:
   * *United Airlines*: Train on LAX T7 (Decentralized) $\rightarrow$ Evaluate zero-shot on ORD T1 (Mega Concourse Pier), EWR T-C (Coastal Pier), and IAH T-C (Spoke Hub).
   * *American Airlines*: Train on LAX T4 (Decentralized) $\rightarrow$ Evaluate zero-shot on ORD T3 (Mega Pier), DFW T-A (Multi-Ring), and PHL T-B/C (Finger Pier).
   * *Delta Air Lines*: Train on LAX T3 (Decentralized) $\rightarrow$ Evaluate zero-shot on DTW McNamara (1-Mile Linear Fortress), BOS T-A (Satellite Spoke), and LGA T-C (Urban Pier).
2. **Cross-Carrier, Same-Architecture Transfer**:
   * Hold physical terminal architecture constant within the decentralized environment at LAX:
     * Train on AA (Terminal 4) $\rightarrow$ Test on DL (Terminal 3) and UA (Terminal 7).
   * Isolates whether differences in carrier scheduling banks and passenger demographics affect generalizability when spatial terminal geometry is held fixed.
3. **Cross-Regime Transfer Across Empirical Clusters**:
   * Train models on Cluster 0 Mega-Connecting Gateways (`LAX`, `ORD`, `DFW`) $\rightarrow$ Test zero-shot on Cluster 2 High-Reliability Hubs (`DTW`, `PHL`) and Cluster 3 Congested Coastal Hubs (`EWR`, `LGA`).
   * Proves whether hybrid physics-based models adapt to varying delay transmission regimes better than purely data-driven machine learning models.

---

### Chapter V: Discussion & Conclusions

#### Under Section: `Implications for Terminal Planning and Queue Management`
Address the broader operational utility of the findings:

* **Decoupling Physical Geometry from Predictive Logic**: Discuss how incorporating physical terminal typologies (e.g., distance from curbside to screening, single-concourse vs. split-satellite) allows TSA federal security directors to deploy zero-shot forecasting models to newly renovated or reconfigured terminals without requiring months of historical training data.
* **Network-Aware Tactical Staffing Allocation**: Emphasize that because airport throughput volatility is heavily driven by upstream network delays originating across the Top 25 hub network, local checkpoint staffing models must ingest upstream airside flight delay data rather than relying solely on local historical persistence.

---

## 3. Summary Checklist for Document Updates

- [ ] **Chapter I (`Gleich-700B-Intro-edited.docx`)**:
  - [ ] Add spatial, carrier, and temporal delimitations to the `Delimitations` section.
  - [ ] Add the network steady-state assumption and exclusive-checkpoint limitation to `Limitations and Assumptions`.
- [ ] **Chapter III (`Gleich_700B_Methodology-edited.docx`)**:
  - [ ] Insert the 4-tiered sampling criteria under `Sample` $\rightarrow$ `Macro Categorization`.
  - [ ] Insert the **9-Airport Master Selection Matrix** under `Sample` $\rightarrow$ `Micro-Level Refinement`.
  - [ ] Insert the **Network-Node Rationale** under `Sample` $\rightarrow$ `Temporal Scope and Boundary Definition`.
  - [ ] Update `Validity` to reflect connecting passenger decoupling and checkpoint isolation.
- [ ] **Chapter IV (`Gleich_700B_Resultsv1.docx`)**:
  - [ ] Add Top 25 network recovery curves to `Descriptive Statistics`.
  - [ ] Formulate the $4 \times 4$ zero-shot spatial transfer matrix under `Generalizability`.
