# CHAPTER I SINGLE SOURCE OF TRUTH (SSOT) SPECIFICATION
====================================================================================================
PROJECT: Evaluating Predictive Techniques to Model Stochastic Airport Passenger Flow
AUTHOR: Leila Gleich | INSTITUTION: Embry-Riddle Aeronautical University
DEGREE: Master of Science in Aeronautics / Aviation Data Analytics
DOCUMENT: Chapter I Single Source of Truth (SSOT) Reference Specification
RELEASE VERSION: v4.0 (SemVer-Data) | DATE: October 2026
CANONICAL LOCATION: thesis_docs/ssot/Chapter_1_SSOT.md
COMPANION DRAFT: thesis_docs/manuscripts/Chapter_1_Introduction.md
====================================================================================================

## 1. PURPOSE AND SCOPE OF THE SSOT DOCUMENT

This document serves as the **definitive, immutable Single Source of Truth (SSOT)** for Chapter I (Introduction & Scope) of the graduate thesis. 

It defines the formal theoretical foundation, research questions, overarching hypothesis ($H_1$), operational dimensions, delimitations, limitations, and institutional scope standards. Any manuscript draft, defense presentation, or journal article must adhere strictly to the definitions, formulations, and boundaries anchored herein.

---

## 2. CANONICAL CHAPTER I OUTLINE ARCHITECTURE

Chapter I is structured into seven core sections:

```
CHAPTER I: INTRODUCTION
├── 1.1 Context and Operational Motivation
│   ├── The National Airspace System Capacity Dilemma
│   ├── Limitations of Conventional Undisturbed Error Metrics
│   └── The Triad of Operational Evaluation (Robustness, Resilience, Generalizability)
├── 1.2 Significance of the Study
│   ├── Decoupling Flight Schedules from Passenger Show-Up Timing
│   └── Operational Value for Federal Security Directors and Airline Planners
├── 1.3 Statement of the Problem
│   ├── Post-Pandemic Volatility & Inadequacy of Pre-Pandemic Assumptions
│   └── Absence of a Dynamic, Multi-Dimensional Evaluation Framework
├── 1.4 Purpose Statement
│   ├── Objective Comparison of Forecasting Paradigms (Deterministic, ML, Hybrid)
│   └── Capacity Optimization via Software Intelligence vs. Capital Infrastructure
├── 1.5 Research Question
│   └── Verbatim Primary Operational Inquiry
├── 1.6 Delimitations
│   ├── Geographic Scope (Top 25 Contiguous U.S. Commercial Hubs)
│   ├── Temporal Scope (2019–2025 Baseline; May 1, 2022 Candidate B Demarcation)
│   ├── Data Feed Boundaries (TSA FOIA, BTS OTP, BTS T-100, BTS DB1B)
│   └── Metric Standards (RMSE, MASE, R_MASE, RTR, Diebold-Mariano)
└── 1.7 Limitations and Assumptions
    ├── Checkpoint Staffing & Lane Configuration Opacity (TSO Shift Secrecy)
    ├── Passenger Checked-Baggage & Pre-Security Dwell (ACRP Report 40)
    ├── Connecting Transfer Ratio Stability (Quarterly DB1B Granularity)
    └── Operational Exogeneity (Exogenous Convective Storms & Cancellations)
```

---

## 3. MASTER CONCEPTUAL & THEORETICAL REGISTRY

### 3.1 Verbatim Primary Research Question

> **"Which predictive modeling frameworks are most effective for forecasting airport passenger security screening throughput when prioritizing robustness (routine operational accuracy), resilience (stability under convective weather and delay disruptions), or generalizability (cross-airport portability across terminal layouts) as the primary operational evaluation metric?"**

### 3.2 Core Thesis Hypothesis ($H_1$)

* **Overarching Hypothesis ($H_1$)**: Across the three forecasting paradigms (deterministic operational baselines, data-driven machine learning, and sequential state-space hybrids), **no individual architecture will prove universally superior across all three evaluation dimensions**. Rather, systematic trade-offs exist:
  * **$H_{1a}$ (Robustness)**: Non-linear machine learning models ($M_3$ LightGBM) and two-stage hybrids ($M_5$) will demonstrate superior routine operational accuracy ($\text{MASE}_{\text{routine}} < 0.90$) by capturing complex non-linear day-of-week, aircraft gauge, and lead-lag arrival distributions.
  * **$H_{1b}$ (Resilience)**: Sequential two-stage hybrid models ($M_5$) will demonstrate superior disruption resilience ($R_{\text{MASE}} \le 1.30$, time-to-recovery $\text{TTR} \le 4.0\text{ hours}$), resisting the "empty checkpoint fallacy" that degrades pure machine learning models during severe weather delay cascades.
  * **$H_{1c}$ (Generalizability)**: Simple deterministic physical rules ($M_1^*$) and convolved machine learning models ($M_3$) will exhibit superior zero-shot spatial transferability ($\text{RTR} \le 1.10$, error degradation $\le 10\%$) because empirical passenger show-up curves abstract away facility-specific terminal over-fitting.

### 3.3 The Triad of Operational Evaluation Dimensions

1. **Dimension 1: Robustness (Routine Operational Accuracy)**
   - *Operational Definition*: The accuracy, precision, and consistency of the forecast model during nominal, undisturbed operating conditions ($\text{Departure Delay} < 15\text{ minutes}$, zero tactical cancellations).
   - *Primary Metrics*: $\text{RMSE}_{\text{routine}}$, $\text{MAE}_{\text{routine}}$, $\text{MASE}_{\text{routine}}$ (target $< 0.900$), Diebold-Mariano significance test ($p < 0.001$).
2. **Dimension 2: Resilience (Performance Under Severe Disruption)**
   - *Operational Definition*: The stability, error bounded-ness, and speed of recovery of the forecast model during acute exogenous operational shocks ($\text{Departure Delay} \ge 45\text{ minutes}$ or tactical cancellations $\ge 5$).
   - *Primary Metrics*: $\text{RMSE}_{\text{shock}}$, $\text{MASE}_{\text{shock}}$, Disruption Error Multiplier ($R_{\text{MASE}} = \text{MASE}_{\text{shock}} / \text{MASE}_{\text{routine}}$, target $< 1.30$), Time-to-Recovery ($\text{TTR}_{\text{shock}} \le 4.0\text{ hours}$ via Kaplan-Meier survival curves).
3. **Dimension 3: Generalizability (Cross-Airport Transferability)**
   - *Operational Definition*: The external validity and zero-shot portability of a trained model when deployed to an unfamiliar airport facility without site-specific historical recalibration.
   - *Primary Metrics*: Zero-Shot $\text{RMSE}_{\text{transfer}}$, Relative Transfer Ratio ($\text{RTR} = \text{RMSE}_{\text{transfer}} / \text{RMSE}_{\text{in-sample}}$, target $\le 1.10$), Transfer Degradation Penalty ($\Delta_{\text{transfer}} \le 10.0\%$), and $\Delta\text{MASE} < +0.100$.

### 3.4 Formal Research Delimitations

1. **Geographic Delimitation**: Restricted to the contiguous United States, specifically the candidate network of the **Top 25 commercial airfields** ranked by FAA passenger enplanements (capturing 67.2% of nationwide domestic operations), filtered down to the **9-Airport Experimental Cohort** (12 dedicated screening complexes).
2. **Temporal Delimitation**: The multi-source analytical warehouse spans **January 1, 2019 through December 31, 2025** (7 continuous years; 61,344 calendar hours). Model training is delimited to the post-pandemic operational equilibrium beginning **May 1, 2022** (Candidate B; 44 continuous months), reserving **calendar year 2025** (8,760 hours) as an untouched out-of-time holdout.
3. **Carrier Delimitation**: Delimited to the "Big Three" U.S. network legacy carriers—**American Airlines (AA), Delta Air Lines (DL), and United Airlines (UA)**—to guarantee operational homogeneity and common airspace shock invariance ($\delta_t$), systematically excluding Southwest Airlines (WN) due to bimodal arrival mixture violations.
4. **Data Source Delimitation**: Exclusively utilizes publicly available and FOIA-disclosed federal aviation datasets: TSA FOIA hourly screening logs, BTS OTP (Form 234), BTS Schedule T-100 Segment capacity, and BTS DB1B/DB1C 10% ticket surveys.

### 3.5 Formal Limitations and Methodological Assumptions

1. **Staffing and Lane Configuration Opacity**: Real-time TSO lane allocations, lane opening schedules, and manual queue snake reconfigurations are proprietary and security-sensitive. The methodology addresses this by aggregating throughput across all physical lanes within dedicated terminal screening complexes ($Y_{kt}$).
2. **Passenger Checked Baggage & Pre-Security Dwell**: Airline baggage check and ticket counter dwell times are proprietary. Pre-security passenger lead times are modeled through empirical passenger show-up curves derived from **ACRP Report 40 (*Airport Passenger Terminal Planning and Design*)**.
3. **Connecting Passenger Survey Granularity**: Airside connecting ratios are derived from quarterly BTS DB1B surveys. Ratios are assumed to be operationally stable across monthly scheduling blocks within specific carrier-terminal pairs.
4. **Operational Exogeneity**: Flight departure delays and cancellations reported in BTS Form 234 are treated as exogenous inputs capturing terminal apron congestion and NAS-wide ground delay programs.

---

## 4. CANONICAL SYSTEM BASELINE NUMBERS

| Metric / Parameter | Value | Source / Benchmark |
| :--- | :---: | :--- |
| **Longitudinal Multi-Source Period** | Jan 1, 2019 – Dec 31, 2025 (7 Years) | Master Analytical Warehouse |
| **Raw Federal Fact Records** | 67,222,828 fact rows | Upstream Federal Staging |
| **Cleaned Conformed Fact Records** | 42,062,039 conformed rows | Conformed Warehouse Census |
| **Candidate Airfield Universe** | Top 25 U.S. Commercial Hubs | FAA Passenger Enplanements |
| **Share of National Domestic Flights** | 67.2% of U.S. domestic flights | BTS Form 234 National Base |
| **Candidate B Demarcation Date** | May 1, 2022 | Post-Mask Mandate Repeal |
| **Candidate B Total Span** | 44 continuous months | 2022-05 to 2025-12 |
| **Candidate B Development Span** | 32 continuous months | 2022-05 to 2024-12 |
| **Out-of-Time Holdout Window** | 12 continuous months | Jan 1, 2025 – Dec 31, 2025 |

---

## 5. TERMINOLOGY & GOVERNANCE RULES

Chapter I enforces the terminology guidelines established in `thesis_docs/notes/provenance_and_standards/Jargon_and_Buzzword_Replacement_Guide.md`:
* **Use**: "Empirical Passenger Show-Up Curve" (or "Lead-Lag Passenger Arrival Distribution"). **Never use**: "physics-based continuous arrival kernel convolution".
* **Use**: "Carrier Checkpoint Isolation". **Never use**: "orthogonal Wiener-Hopf deconvolution operator".
* **Use**: "Connecting Passenger Deflator" (or "The Hub Disconnect"). **Never use**: "DB1B transfer deflation manifold".
* **Use**: "Routine Operational Accuracy, Resilience Under Disruption, Cross-Airport Transferability". **Never use**: "cyber-physical stability manifolds".

---

## 6. CROSS-CHAPTER INTEGRATION ROADMAP

* **Handoff to Chapter II (Literature Review)**: Chapter I establishes the failure of static planning tables and unconstrained queuing models; Chapter II provides the theoretical foundation (queuing theory, DES, SARIMA, ML, and hybrid state-space filtering).
* **Handoff to Chapter III (Methodology)**: Chapter I establishes the three evaluation dimensions and research delimitations; Chapter III translates them into mathematical formulas, the 4-phase filtering pipeline, and the 84-cell interaction tensor.
* **Handoff to Chapter IV (Findings)**: Chapter I defines the core hypothesis ($H_1$); Chapter IV provides the empirical benchmark matrix (Table 4.10 and Table 4.11) evaluating $H_1$.
* **Handoff to Chapter V (Discussion)**: Chapter I defines the operational motivation; Chapter V translates the empirical confirmation of $H_{1a}, H_{1b}, H_{1c}$ into the Regime-Switched Gated Inference Engine.

====================================================================================================
END OF CHAPTER I SINGLE SOURCE OF TRUTH (SSOT) SPECIFICATION
====================================================================================================
