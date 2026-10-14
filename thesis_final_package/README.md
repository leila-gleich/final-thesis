# Thesis Final Package
## Evaluating Predictive Techniques to Model Stochastic Airport Passenger Flow

**Author**: Leila Gleich  
**Program**: MSAA / 700B  
**Institution**: Embry-Riddle Aeronautical University  
**Package Date**: October 14, 2026  
**Source Repository**: `final-thesis` (branch: `working-dev`)

---

## Purpose

This is a **curated, deduplicated package** containing the most up-to-date and internally consistent thesis materials — manuscripts, appendix, tables, figures, defense materials, and companion workbooks — organized for committee review and defense preparation.

> [!IMPORTANT]
> All tables, figures, and manuscript references have been verified for internal consistency.

---

## Contents

### `manuscript/` — Full Thesis Manuscript

| File | Description |
|:-----|:------------|
| `Gleich-FinalThesis.md` | **Unified 5-chapter thesis** (Chapters I–V) in APA 7th Edition Markdown |
| `Chapter_I_Introduction.md` | Standalone Chapter I: Introduction, Problem Statement, Research Questions |
| `Chapter_II_Literature_Review.md` | Standalone Chapter II: Literature Review & Theoretical Framework |
| `Chapter_III_Methodology.md` | Standalone Chapter III: Research Design, 4-Tier Filtering, 9-Airport Cohort |
| `Chapter_IV_Findings_Discussion_Conclusions.md` | Standalone Chapters IV & V: Findings, Discussion, and Conclusions |
| `gleich700B_chpIV_chpV_combined.md` | Backup reference: earlier combined Ch IV/V markdown |

### `appendix/` — Master Appendix & Reference Materials

| File | Description |
|:-----|:------------|
| `Master_Appendix.docx` | Complete 14-appendix Word document (Appendices A–N) |
| `appendix_tables.xlsx` | 30-tab companion workbook with APA 7th formatting |
| `glossary.md` | Technical glossary: 99 terms across 6 operational categories |
| `acronyms.md` | Acronyms & abbreviations reference (6 operational domains) |

### `tables/` — Manuscript Tables (16 Core + 3 Supplementary)

All 19 canonical CSV files plus the master Excel workbook (`thesis_tables.xlsx`).

| Table | Description |
|:------|:------------|
| 4.1 | Multi-Source Data Foundation Census |
| 4.2 | Summary Descriptive Statistics |
| 4.3a | Post-Pandemic Temporal Demarcation Evaluation |
| 4.3b | Annual Seasonal Volatility Regimes |
| 4.4a | Day-of-Week Volatility Dynamics & Archetypes |
| 4.5 | Cross-Dataset Econometric Relationships |
| 4.6 | 9-Airport Experimental Cohort Factorial Specification |
| 4.7 | Summary Statistics: 9-Airport vs. Top 25 |
| 4.8 | Day-of-Week Mean Daily Passenger Throughput |
| 4.9 | Empirical Lead-Lag Transfer Dynamics |
| 4.10 | **Master Model Benchmark Matrix** (2025 Holdout) |
| 4.11 | Multi-Pillar Hypothesis Evaluation Matrix |
| 5.1 | Dimension 1: Routine Operational Accuracy (Robustness) |
| 5.2 | Dimension 2: Resilience & Shock Performance |
| 5.3 | Dimension 3: Generalizability & Cross-Airport Transfer |
| 5.4 | Master Asymmetric Trade-Off Matrix |

### `figures/` — Publication-Grade Figures

Organized by chapter:

- **`ch01_intro/`** — Data sample profile, network approach (2 figures)
- **`ch02_lit_review/`** — OTP volatility, queuing dynamics, connecting paradox (6 figures)
- **`ch03_methodology/`** — Model families, data pipeline, filtering, schemas (16 figures)
- **`ch04_results/`** — Volatility clusters, lead-lag curves, benchmark matrix (6 figures)
- **`ch05_discussion/`** — Trade-off triangle, resilience, generalizability, dashboard (4 figures)
- **`appendix/`** — Database profiles, data breakdowns, assumptions (7 figures)
- **`otp_volatility_analysis/`** — Factor weights, values vs. volatility, heatmaps (5 figures)

### `defense/` — Defense Presentation Materials

| File | Description |
|:-----|:------------|
| `Recommended-Thesis-Defense-Deck.pptx` | 32-slide deck with embedded publication figures (7.2 MB) |
| `Thesis-Defense.pptx` | Working defense deck |
| `DEFENSE_PRESENTATION_SCRIPT_25MIN.md` | 25-minute oral examination script (6 timed segments) |

### `workbooks/` — Pipeline Companion Excel Workbooks

| File | Description |
|:-----|:------------|
| `01_top25_clustering.xlsx` | PCA & K-Means clustering of Top 25 airports |
| `02_4tier_filtering.xlsx` | 4-tier purposive filtering pipeline audit |
| `02_top9_cohort_comprehensive_analysis.xlsx` | 9-airport cohort operational profiles |
| `03_lead_lag_deconvolution.xlsx` | ACRP 40 show-up curve parameters |
| `04_model_execution_2025_holdout.xlsx` | 2025 out-of-time holdout benchmark metrics |
| `05_robustness_resilience_generalizability.xlsx` | Multi-dimensional operational evaluation |

---

## Model Nomenclature

| Model | Description |
|:------|:------------|
| **Baseline Control** | Diurnal Naive Persistence ($\widehat{\text{Vol}}_t = \text{Vol}_{t-24}$) |
| **Model 1 (Deterministic)** | Flight Schedule × ACRP 40 Show-Up Convolution |
| **Model 2 (Machine Learning)** | Supervised Decision-Tree Regressor (24 BTS features) |
| **Model 3 (Dynamic Hybrid)** | Two-Stage: Schedule Cycles + Live Error Feedback ($e_{t-1}$) |

---

## Verification

Tables synchronized via `python3 src/analysis/sync_manuscript_tables.py`.  
Provenance tracked in `results/00_VERSION_CONTROL_AND_PROVENANCE.md`.
