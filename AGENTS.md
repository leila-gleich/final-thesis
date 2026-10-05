# AGENTS.md: Repository Agent Rules & Operational Constitution
# Evaluating Predictive Techniques to Model Stochastic Airport Passenger Flow (MSAA / Gleich 700B)

> **CRITICAL DIRECTIVE FOR ALL AI AGENTS, SUBAGENTS, AND AUTOMATED ASSISTANTS**:  
> This document defines the non-negotiable operational constitution and domain rules governing all work in this repository (`final-thesis`). Every AI agent operating in this repository is strictly bound by these rules. Before proposing any changes, modifying any code, answering questions, or generating tables, you MUST adhere strictly to the policies below.

---

## 1. Non-Negotiable Operational Constraints

### Policy 1.1: Zero Edits to Microsoft Word Documents (`.docx`)
* **Strict Rule**: Under NO circumstances may any agent create, modify, overwrite, delete, or touch any Microsoft Word document (`.docx`) in this repository **unless the user explicitly states otherwise in writing within the current session**.
* All manuscript editing, drafts, table updates, and academic prose work must be conducted exclusively in Markdown (`.md`), Python (`.py`), CSV (`.csv`), Excel (`.xlsx`), or plain text (`.txt`) files.
* Microsoft Word files are reserved exclusively for the author's manual committee review drafts.

### Policy 1.2: Commit After Each Individual Task
* **Strict Rule**: Immediately upon completing each discrete task, bug fix, analysis update, or documentation edit, the agent **MUST create a Git commit** with an informative, professional commit message adhering to conventional commit formatting (e.g., `feat: ...`, `fix: ...`, `docs: ...`, `refactor: ...`).
* Never leave uncommitted changes or dirty worktrees across task boundaries. Verify clean git status after committing.

### Policy 1.3: Always Synchronize Version Control & Provenance Records
* **Strict Rule**: Whenever any model, table, analytical script, data schema, or manuscript section is updated, the agent MUST update `results/00_VERSION_CONTROL_AND_PROVENANCE.md`.
* Ensure every release, fix, or revision records the version identifier, date, modified file inventory, and explicit academic rationale.

### Policy 1.4: Always Synchronize All Associated Tables in CSV and Excel
* **Strict Rule**: Whenever any metric, model benchmark, descriptive statistic, or parameter changes, the agent MUST synchronize BOTH:
  1. The **conformed CSV files** in `results/manuscript_tables/` and `results/tables/`.
  2. The **multi-tab companion Excel workbooks** in `results/` (`01_top25_clustering.xlsx`, `02_4tier_filtering.xlsx`, `02_top9_cohort_comprehensive_analysis.xlsx`, `03_lead_lag_deconvolution.xlsx`, `04_model_execution_2025_holdout.xlsx`, `05_robustness_resilience_generalizability.xlsx`).
* Always execute or verify with `python3 src/analysis/sync_manuscript_tables.py` to ensure exact mathematical synchronization across all tabular outputs.

---

## 2. Core Research Problem & Target Formulation

### Policy 2.1: Primary Dependent Target is Throughput Volatility (NOT Volume)
* **Core Research Objective**: This thesis models and forecasts the **volatility of TSA passenger screening throughput** ($\sigma_{\text{TSA}}$ and $CV_{\text{TSA}}$), **NOT raw passenger volume ($y_t$)**.
* **Queuing Physics Rationale**: Under Kingman's heavy-traffic queuing formula ($W_q \approx \frac{\rho}{1-\rho} \frac{C_a^2 + C_s^2}{2} \frac{1}{\mu}$), checkpoint queues and passenger delays scale quadratically with arrival volatility ($C_a^2$) as checkpoint utilization approaches capacity ($\rho \to 1.0$).
* **Primary Targets Evaluated**:
  1. **Intraday Diurnal Absolute Volatility ($\sigma_{\text{TSA, hr}}$, pax/hr dispersion)**: Standard deviation across the 24 hours of day $d$.
  2. **Intraday Scale-Free Relative Volatility ($CV_{\text{TSA, hr}} = \sigma / \mu$, dimensionless)**: Scale-free arrival burstiness normalized across small vs. mega checkpoints.
  3. **Multi-Day Rolling Volatility ($\sigma_{\text{TSA, 7d}}$, pax/day)**: Rolling 7-day standard deviation capturing network turbulence.
* **The Values versus Volatility Paradigm ($H_2$)**: Static volume feature levels fail on multi-day volatility ($R^2 < 0$), whereas feature volatility metrics succeed ($R^2 > +0.31$). Checkpoint arrival volatility is coupled with flight departure delay volatility ($CV_{\text{delay}}: r = +0.4373, p < 0.05$), while raw delay minutes show zero correlation ($r = -0.062, p = 0.77$).

---

## 3. The 4-Model Canonical Evaluation Suite

### Policy 3.1: Exactly Four Canonical Models (Plus Pruned Variations Rationale)
Following the 4-tier filtering pipeline (which established the 9-airport experimental cohort across 12 carrier-exclusive complexes), the evaluation suite is restricted to **exactly four canonical models (one per paradigm, plus control)**:
1. **$M_0$ (Baseline Control Benchmark)**: Diurnal Volatility Naive Persistence ($\widehat{\text{Vol}}_t = \text{Vol}_{t-24}$, non-parametric $\text{MASE} \equiv 1.000$).
2. **$M_1^*$ (Deterministic Physical Baseline)**: Deterministic Schedule Bank Volatility Baseline (ACRP Report 40 lead-lag show-up curve convolution across lead horizons $t+1, t+2, t+3$).
3. **$M_3$ (Probabilistic & Machine Learning Architecture)**: Supervised Volatility Gradient Boosted Regressor (Combined Values + Volatility across 24 BTS OTP attributes).
4. **$M_5$ (Dynamic Cyber-Physical Hybrid Framework)**: Sequential Two-Stage SARIMA-Tree Volatility Hybrid with live 1-step error innovation feedback ($e_{t-1}$).

### Policy 3.2: Pruned Intermediate Variations Must Remain Archived
* **$M_1$ (Unshifted Contemporaneous Schedule)**: Pruned due to severe phase distortion ($r = 0.12$) ignoring the 105-minute mean lead time. Superseded by convolved $M_1^*$.
* **$M_2$ (Lead Flights Only Baseline)**: Pruned due to truncation bias during afternoon secondary delay cascades.
* **$M_4$ (Load-Factor Scaled Linear Regression)**: Pruned due to mathematical redundancy with non-linear capacity interactions in $M_3$ and $M_5$.

---

## 4. Operational Performance Dimensions & Asymmetric Trade-Offs

### Policy 4.1: The Hybrid Model ($M_5$) is NOT Universally Dominant
Never state or imply that the hybrid model ($M_5$) is universally best across all performance measures. The thesis explicitly demonstrates **Asymmetric Trade-Offs ($H_1$)**:

| Evaluation Dimension | Operational Regime | Stated Academic Target | Dimension Winner & Strategic Reality |
| :--- | :--- | :--- | :--- |
| **Dimension 1: Robustness** | Nominal On-Time Baseline ($\text{Delay} < 15$m, 0 Cancels) & Routine Daily Operations | Lowest $\text{RMSE}_{\text{routine}}$ & $\mathbf{\text{MASE}_{\text{routine}} < 0.700}$ | **$M_5$ achieves lowest RMSE** ($\text{RMSE} = 222.1, \text{MASE} = 0.662$); **$M_3$ wins Routine Pareto Efficiency** ($\text{MASE} = 0.680\text{--}0.700$, zero feedback compute latency). |
| **Dimension 2: Resilience** | Irregular Operations / IROPS ($\text{Delay} \ge 45$m or Cancels $\ge 5$) | Recovery Multiplier $\mathbf{R_{\text{RMSE}} \approx 1.00}$, lowest $\text{MASE}_{\text{shock}}$, $\mathbf{\text{TTR} < 4.0\text{h}}$ | **$M_5$ DECISIVE WINNER**: $R_{\text{MASE}} = \mathbf{1.05}$, $\text{MASE}_{\text{shock}} = \mathbf{0.694}$, $\text{TTR} = \mathbf{2.8\text{h}}$. Pure ML ($M_3$) fragilely collapses ($R = 2.14$) due to Empty Checkpoint Fallacy. |
| **Dimension 3: Generalizability** | Zero-Shot Spatial Transfer (EWR $\to$ LGA) without retraining | Relative Transfer Ratio $\mathbf{\text{RTR} \approx 1.00}$ & $\mathbf{\Delta\text{MASE}_{\text{transfer}} \le 10.0\%}$ | **$M_1^*$ DECISIVE WINNER**: $\text{RTR} = \mathbf{1.04}$, $\Delta\text{MASE} = \mathbf{+4.0\%}$. **$M_5$ DECISIVELY FAILS**: $\text{RTR} = \mathbf{1.19} > 1.00$, $\Delta\text{MASE} = \mathbf{+21.5\%} > 10.0\%$ due to decision tree terminal geometry overfitting. |

---

## 5. Strict Aviation Terminology Filter (Zero-Jargon Policy)

### Policy 5.1: Grounding in Authentic Aviation Operations
All text, metrics, table titles, and code documentation must use authentic commercial aviation, airline operations, TSA security, and FAA Air Traffic Organization language.

### Policy 5.2: Three-Tier Operational Taxonomy
* **Tier 1: Nominal On-Time Baseline**: Departure delays $< 15$ minutes and cancellations $= 0$ (FAA/DOT A14 regulatory reference benchmark).
* **Tier 2: Routine Daily Operations**: Everyday commercial hub operations with ambient 15–30 minute delays and normal 1–2% cancellation churn.
* **Tier 3: Irregular Operations (IROPS)**: Severe convective disruptions, ground stops, delays $\ge 45$ minutes, and cancellations $\ge 5$.

### Policy 5.3: Prohibited Jargon vs. Mandatory Aviation Terminology
| PROHIBITED JARGON / LAB-SPEAK (DO NOT USE) | MANDATORY AVIATION TERM (USE INSTEAD) |
| :--- | :--- |
| *Quiescent / Sterile Control* | **Nominal On-Time Baseline** (or FAA A14 Reference Case) |
| *Ambient noise / low-amplitude churn* | **Routine Daily Operations** (or Ambient Operational Churn) |
| *Acute shock state / severe perturbation* | **Irregular Operations (IROPS)** (or Severe Convective Disruption) |
| *Orthogonal Wiener-Hopf deconvolution operator* | **Carrier Checkpoint Isolation** (Dedicated Carrier Terminals) |
| *Continuous physics-based arrival kernel convolution* | **Empirical Passenger Show-Up Curve Convolution** ($t+1, t+2, t+3$) |
| *Type I (air-gapped) vs. Type II (airside connected)* | **Physically Separate Terminals vs. Walkway-Connected Terminals** |
| *DB1B transfer deflation manifold* | **Connecting Passenger Deflator** (or The Hub Disconnect) |
| *Continuous Static Stability* | **Routine Operational Accuracy (Robustness)** |
| *Cyber-physical stability manifolds* | **Two-Stage Sequential Hybrid Model** |
| *Entropy, manifold transitions, fluid physics* | **Queuing Dynamics, Arrival Burstiness, Flight Bank Synchronization** |

---

## 6. Formatting & Academic Standards

### Policy 6.1: APA 7th Edition Compliance
* **Table Layout**: Table number on line 1 (`Table 4.10`), title on line 2 in italics (`*Title of Table in Title Case*`), horizontal rules, no vertical rules, notes on the bottom line (`*Note.* ...`).
* **Statistical Reporting**: Italicize all statistical notation: *$M$*, *$SD$*, *$p$*, *$R^2$*, *$F$*, *$t$*, *$z$*, *$r$*, *$N$*, *$n$*, and *$DM$*.
* **Heading Hierarchy**: Adhere strictly to Level 1 (`#`), Level 2 (`##`), Level 3 (`###`), Level 4 (`####`).

### Policy 6.2: Single Source of Truth (SSOT) Architecture
* Before proposing structural revisions, consult the authoritative chapter SSOTs:
  - `thesis_docs/ssot/README.md`
  - `thesis_docs/ssot/Chapter_1_SSOT.md` through `Chapter_5_SSOT.md`
  - `thesis_docs/manuscripts/glossary.md`

---

## 7. Mandatory Agent Task Completion Checklist
Before concluding ANY task, every agent must verify:
- [ ] Were Microsoft Word documents (`.docx`) preserved untouched (0 edits)?
- [ ] Does all analysis and prose target throughput volatility ($\sigma_{\text{TSA}}$ / $CV_{\text{TSA}}$) rather than raw volume?
- [ ] Were the 4 canonical models ($M_0, M_1^*, M_3, M_5$) evaluated with asymmetric trade-offs preserved?
- [ ] Were all lab-science/physics jargon terms replaced with authentic aviation operations terms?
- [ ] Are all 16 tables in CSV and companion Excel workbooks fully synchronized?
- [ ] Has `results/00_VERSION_CONTROL_AND_PROVENANCE.md` been updated with the change log?
- [ ] Was a Git commit created with an appropriate, descriptive commit message?
