# Thesis Update Master Roadmap: Integrating Coupled Volatility & Temporal Regimes

## Purpose & Overview

This directory provides turn-key, step-by-step guidance for updating the graduate thesis manuscript:
**"Evaluating Predictive Techniques to Model Stochastic Airport Passenger Flow"** (Author: Leila Gleich).

These recommendations document the methodological and empirical transition from **static passenger volume clustering** to **Coupled Volatility / Variation Clustering** between TSA security checkpoint throughput and Bureau of Transportation Statistics (BTS) On-Time Performance (OTP) flight operations across the **Top 25 U.S. commercial airfields**.

---

## Directory Contents

| Document | Primary Focus & Target Chapters | Description |
| :--- | :--- | :--- |
| **[`00_README_AND_ROADMAP.md`](file:///Users/leilagleich/Library/CloudStorage/OneDrive-Embry-RiddleAeronauticalUniversity/final-thesis/thesis_docs/recommendations/chapter_updates/00_README_AND_ROADMAP.md)** | Master Overview & Execution Checklist | Comprehensive executive summary, directory index, and step-by-step update checklist. |
| **[`01_CHAPTER_3_METHODOLOGY_GUIDE.md`](file:///Users/leilagleich/Library/CloudStorage/OneDrive-Embry-RiddleAeronauticalUniversity/final-thesis/thesis_docs/recommendations/chapter_updates/01_CHAPTER_3_METHODOLOGY_GUIDE.md)** | Chapter III: Methodology | Mathematical definitions, Coupled Volatility Index, Operational Turbulence Shock Index, 3-tier hierarchical clustering equations, and sample size power proofs. |
| **[`02_CHAPTER_4_RESULTS_TEXT_AND_TABLES.md`](file:///Users/leilagleich/Library/CloudStorage/OneDrive-Embry-RiddleAeronauticalUniversity/final-thesis/thesis_docs/recommendations/chapter_updates/02_CHAPTER_4_RESULTS_TEXT_AND_TABLES.md)** | Chapter IV: Empirical Results | Drop-in text paragraphs, Markdown/LaTeX tables (Tables 4.3b, 4.4a, 4.4b, 4.4c), and figure captions/callouts for Figures 1–4. |
| **[`03_CHAPTER_5_DISCUSSION_AND_ANALYSIS_GUIDE.md`](file:///Users/leilagleich/Library/CloudStorage/OneDrive-Embry-RiddleAeronauticalUniversity/final-thesis/thesis_docs/recommendations/chapter_updates/03_CHAPTER_5_DISCUSSION_AND_ANALYSIS_GUIDE.md)** | Chapter V: Analysis & In-Depth Discussion | Deep-dive interpretations of Lead-Lag Asynchrony, Model Robustness across 84 cells, Disruption Resilience in Summer Peaks, and the Regime-Switched Gated Inference architecture. |
| **[`04_DEFENSE_TALKING_POINTS_AND_COMMITTEE_QA.md`](file:///Users/leilagleich/Library/CloudStorage/OneDrive-Embry-RiddleAeronauticalUniversity/final-thesis/thesis_docs/recommendations/chapter_updates/04_DEFENSE_TALKING_POINTS_AND_COMMITTEE_QA.md)** | Defense Slide Deck & Committee Defense | 20–25 slide structure, anticipated defense questions, and rigorous defense talking points. |

---

## Master Step-by-Step Update Checklist

In a future session, execute the edits following this structured sequence:

- [x] **Step 1: Update Chapter III (Methodology)**:
  - Add Section 3.X on *Coupled Volatility and Variance Formulation*.
  - Insert mathematical formulations for Within-Day TSA $CV$, Delay Dispersion ($\sigma_{\text{Delay}}$), and the Coupled Volatility Index ($CV_{\text{TSA}} \times \sigma_{\text{Delay}}$).
  - Add equation for the Diurnal Operational Turbulence Shock Index ($T(h)$) proving the non-consecutive dual-peak clustering.
  - Detail the $4 \times 7 \times 3 = 84$ cell cross-classification matrix and sample size sufficiency thresholds ($N_{\text{train}} \ge 50\text{--}100, N_{\text{test}} \ge 30$).

- [x] **Step 2: Update Chapter IV (Results)**:
  - Add Section 4.3.3 / 4.4 on *Empirical Coupled Volatility Regimes*.
  - Insert **Table 4.3b**: Master Annual Volatility Regimes Summary (Off-Peak, Mid-Peak, Peak, Holiday).
  - Insert **Table 4.4a**: Day-of-Week Cyclical Volatility Dynamics and Operational Archetypes.
  - Insert **Table 4.4b**: Diurnal Hourly Volatility Clusters conditioned on Day of Week.
  - Insert and reference the 4 high-resolution figures from [`season-analysis/figures/`](file:///Users/leilagleich/Library/CloudStorage/OneDrive-Embry-RiddleAeronauticalUniversity/Gleich-Thesis/season-analysis/figures):
    - Figure 1: Coupled Volatility Phase Space & Annual Seasonality
    - Figure 2: Day of Week Volatility Dynamics
    - Figure 3: Diurnal 24-Hour Volatility Heatmap (Dual Peaks)
    - Figure 4: Statistical Sample Size & Training Sufficiency Boxplot
  - Update Table 4.7 (Holdout Benchmark Matrix) to explain performance variation across volatility regimes.

- [x] **Step 3: Update Chapter V (Analysis & Discussion)**:
  - Enrich Section 5.1 & 5.2 to explain the **Lead-Lag Asynchrony Mechanism**: why morning screening surge volatility peaks first ($CV_{\text{TSA}}$), while flight delay dispersion ($\sigma_{\text{Delay}}$) peaks 8–10 hours later in the evening.
  - Enrich Section 5.3 (Robustness) with statistical confirmation that all 84 cells are viable for supervised learning without empty cells.
  - Enrich Section 5.4 (Resilience) with empirical proof of the **"Empty Checkpoint Fallacy"** in pure ML during Summer Peak convective storms ($\sigma_{\text{Delay}} = 68.43$ min, Cancellations = 3.16%), proving why the Two-Stage Hybrid ($M_5$) is mathematically mandatory.
  - Enrich Section 5.6 with the **Regime-Switched Gated Inference Recommendation** for TSA Operations Control Centers.

- [x] **Step 4: Update Proposal / Slide Deck & Version Control**:
  - Incorporate Slide 8 (Coupled Volatility Phase Space) and Slide 14 (Diurnal Heatmap showing dual peaks).
  - Review anticipated committee questions in [`04_DEFENSE_TALKING_POINTS_AND_COMMITTEE_QA.md`](file:///Users/leilagleich/Library/CloudStorage/OneDrive-Embry-RiddleAeronauticalUniversity/final-thesis/thesis_docs/recommendations/chapter_updates/04_DEFENSE_TALKING_POINTS_AND_COMMITTEE_QA.md).
  - Synchronize and update all version control specifications (`VERSION_CONTROL_AND_PROVENANCE.md`, `README.md`).

---

## Underlying Source Deliverables Reference

All underlying empirical tables and figures are located in:
* Excel Workbook: [`season-analysis/season-analysis.xlsx`](file:///Users/leilagleich/Library/CloudStorage/OneDrive-Embry-RiddleAeronauticalUniversity/final-thesis/season-analysis/season-analysis.xlsx)
* CSV Tables: [`season-analysis/*.csv`](file:///Users/leilagleich/Library/CloudStorage/OneDrive-Embry-RiddleAeronauticalUniversity/final-thesis/season-analysis/)
* Publication Figures: [`thesis_docs/manuscripts/figures/*.png`](file:///Users/leilagleich/Library/CloudStorage/OneDrive-Embry-RiddleAeronauticalUniversity/final-thesis/thesis_docs/manuscripts/figures/)
* Python Runner Script: [`season-analysis/season_analysis_volatility_runner.py`](file:///Users/leilagleich/Library/CloudStorage/OneDrive-Embry-RiddleAeronauticalUniversity/final-thesis/season-analysis/season_analysis_volatility_runner.py)
