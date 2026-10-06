# Standard Operating Procedure (SOP): Updating Manuscripts, Tables & Spreadsheets
====================================================================================================
PROJECT: Forecasting the Volatility of Airport Passenger Security Screening Throughput (MSAA / Gleich 700B)
AUTHOR: Leila Gleich | INSTITUTION: Embry-Riddle Aeronautical University
LOCATION: thesis_docs/MANUSCRIPT_AND_DATA_UPDATE_SOP.md
RELEASE VERSION: v4.7 | DATE: October 2026
====================================================================================================

This document provides definitive, step-by-step instructions for researchers and AI agents on how to update manuscript text, numerical findings, empirical tables, and Excel workbooks in this repository while preserving strict referential integrity, academic formatting, and provenance standards.

---

## 1. System Architecture & The Single Direction of Data Flow

To eliminate discrepancies between research drafts, raw model outputs, and published figures, the repository operates on an automated, single-direction data synchronization pipeline:

```
[Chapter SSOT Specifications]
  `thesis_docs/ssot/Chapter_1_SSOT.md` through `Chapter_5_SSOT.md`
       │  (Authoritative benchmark metrics, sample sizes, and definitions)
       ▼
[Production Markdown Manuscripts]
  `thesis_docs/manuscripts/chp1-intro.md` through `chp5-discussion.md`
       │  (Prose narrative, APA 7 formatting, and primary Markdown tables)
       ▼
[Automated Table Extraction & Synchronization Engine]
  `src/analysis/sync_manuscript_tables.py` (or `python run_pipeline.py`)
       ├─────────────────────────────────────────┐
       ▼                                         ▼
[Conformed CSV Spreadsheets]             [Multi-Tab Companion Excel Workbooks]
  `results/manuscript_tables/`             `results/01_top25_clustering.xlsx`
  `results/tables/`                        `results/02_4tier_filtering.xlsx`
  (16 canonical CSV tables + short links)   `results/02_top9_cohort_comprehensive_analysis.xlsx`
                                           `results/03_lead_lag_deconvolution.xlsx`
                                           `results/04_model_execution_2025_holdout.xlsx`
                                           `results/05_robustness_resilience_generalizability.xlsx`
       │                                         │
       └─────────────────────────────────────────┘
                         ▼
[Version Control & Provenance Audit Ledger]
  `results/00_VERSION_CONTROL_AND_PROVENANCE.md`
```

---

## 2. Non-Negotiable Operational Constraints (From AGENTS.md)

Before making any change, ensure strict compliance with the following rules:

1. **Zero Modifications to Word Documents (`.docx`)**:
   * Under **NO circumstances** edit, overwrite, modify, or delete any `.docx` file in the repository (e.g., `Chp-2-LitReview.docx`, `Proposal_Gleich_700B.docx`).
   * Microsoft Word files are reserved exclusively for the author's manual committee review drafts.
   * All editing is performed exclusively in Markdown (`.md`), Python (`.py`), CSV (`.csv`), or Excel (`.xlsx`).
2. **Primary Target is Throughput Volatility (NOT Volume)**:
   * The dependent variable is **TSA Throughput Volatility** ($\sigma_{\text{TSA}}$ and $CV_{\text{TSA}}$), grounded in Kingman's heavy-traffic queuing physics ($W_q \propto C_a^2$). Never re-frame the core task as predicting raw passenger volume ($y_t$).
3. **The 3-Model Candidate Evaluation Suite & Baseline Control**:
   * Evaluation is strictly restricted to:
     * **Baseline Control**: Daily Persistence Benchmark ($y_{t-24}$, non-parametric $\text{MASE} \equiv 1.000$).
     * **Model 1**: Deterministic Flight Schedule Model (convolved ACRP Report 40 arrival curves).
     * **Model 2**: Supervised Machine Learning Model (decision trees with 24 BTS OTP attributes).
     * **Model 3**: Dynamic Two-Stage Hybrid Model (flight schedule baseline + live 1-step error innovation feedback $e_{t-1}$).
   * **Zero Developer Tags**: Never use internal code variable tags ($M_0, M_1^*, M_3, M_5, M_1, M_2, M_4$) in manuscript prose or tables.
   * **Preserve Asymmetric Trade-Offs ($H_1$)**: Model 3 is NOT universally dominant (it wins Resilience, Model 1 wins Generalizability, and Model 2 wins Routine Pareto Efficiency).
4. **Strict Aviation Terminology Filter**:
   * Use authentic commercial aviation terminology (*Nominal On-Time Baseline*, *Routine Daily Operations*, *Irregular Operations / IROPS*, *Connecting Passenger Deflator*).
   * Prohibit lab-science or physics jargon (*quiescent/sterile control*, *Wiener-Hopf deconvolution*, *cyber-physical manifolds*).

---

## 3. Step-by-Step Change Workflows

### Workflow A: Updating Manuscript Prose, Narrative, or Qualitative Framing
*Use this workflow when refining academic arguments, adjusting tone, adding literature citations, or improving readability for qualitative readers.*

1. **Edit the Target Markdown Manuscript**:
   * Edit the corresponding file in `thesis_docs/manuscripts/`:
     * Chapter 1: `chp1-intro.md`
     * Chapter 2: `chp2-litreview.md`
     * Chapter 3: `chp3-methodology.md`
     * Chapter 4: `chp4-results.md`
     * Chapter 5: `chp5-discussion.md`
     * Master Definitions: `glossary.md`
2. **Review Formatting & Tone**:
   * Ensure APA 7th Edition compliance (italicize statistical symbols: *$M$*, *$SD$*, *$p$*, *$R^2$*, *$DM$*).
   * Maintain intuitive operational analogies (*The Checkpoint Tipping Point*, *The Staffing Safety Cushion*, *The Empty Checkpoint Fallacy*, *The Airport Operator's Playbook*).
3. **Update Provenance Ledger**:
   * Open `results/00_VERSION_CONTROL_AND_PROVENANCE.md` and document the change scope, affected files, and academic rationale in Section 1.
4. **Verify Safety & Cleanliness**:
   * Verify zero `.docx` files touched:
     ```bash
     git status --porcelain | grep -i '\.docx'
     ```
5. **Commit to Git**:
   ```bash
   git add thesis_docs/manuscripts/ results/00_VERSION_CONTROL_AND_PROVENANCE.md
   git commit -m "docs(manuscript): refine Chapter X qualitative framing and literature synthesis"
   ```

---

### Workflow B: Updating Numerical Metrics, Empirical Findings, or Table Data
*Use this workflow when model parameters, test statistics, sample sizes, or benchmark numbers change.*

1. **Step 1 — Update the Single Source of Truth (SSOT)**:
   * Update the authoritative metric values in the corresponding SSOT file (`thesis_docs/ssot/Chapter_X_SSOT.md`).
   * This guarantees that the master benchmark contract remains synchronized across all five chapters.
2. **Step 2 — Update the Primary Manuscript Markdown Table**:
   * In `thesis_docs/manuscripts/chp4-results.md` (for Tables 4.1 through 4.11) or `thesis_docs/manuscripts/chp5-discussion.md` (for Tables 5.1 through 5.4), edit the Markdown table cells to reflect the new numbers.
3. **Step 3 — Run the Automated Synchronization Engine**:
   * Execute the table extraction script from the repository root:
     ```bash
     python3 src/analysis/sync_manuscript_tables.py
     ```
   * *What this script automatically does*:
     1. Parses all 16 tables from the Markdown manuscripts.
     2. Sanitizes LaTeX notation into plain CSV text.
     3. Overwrites all conformed CSV files in `results/manuscript_tables/` and `results/tables/`.
     4. Updates the matching sheets and cells in all multi-tab companion Excel workbooks in `results/`:
        - `results/01_top25_clustering/01_top25_clustering.xlsx`
        - `results/02_4tier_filtering/02_top9_cohort_comprehensive_analysis.xlsx`
        - `results/03_lead_lag_deconvolution/03_lead_lag_deconvolution.xlsx`
        - `results/04_model_execution_2025_holdout/04_model_execution_2025_holdout.xlsx`
        - `results/05_robustness_resilience_generalizability/05_robustness_resilience_generalizability.xlsx`
     5. Regenerates `results/manuscript_tables/README.md`.
4. **Step 4 — Execute the Test Suite**:
   * Verify that no data pipelines or unit tests broke:
     ```bash
     python3 -m unittest discover tests
     ```
   * Ensure all 38 tests pass (`OK`).
5. **Step 5 — Update Provenance**:
   * Update `results/00_VERSION_CONTROL_AND_PROVENANCE.md` detailing the revised empirical values and analytical justification.
6. **Step 6 — Verify Word Document Safety & Commit**:
   * Check `.docx` safety:
     ```bash
     git status --porcelain | grep -i '\.docx'
     ```
   * Stage and commit all synchronized files:
     ```bash
     git add -A
     git commit -m "feat(results): update Table X.Y benchmark metrics and synchronize CSV/Excel workbooks"
     ```

---

### Workflow C: Re-Running Analytical Code, Models, or ETL Pipelines
*Use this workflow when executing the end-to-end predictive pipeline.*

1. **Execute Master Pipeline**:
   ```bash
   python3 run_pipeline.py
   ```
   *This executes*:
   - Step 1: Top 25 PCA & K-Means clustering (`src/etl/perform_top25_clustering.py`)
   - Step 2: 4-Tier filtering pipeline (`src/etl/apply_4tier_filtering.py`)
   - Step 3: Referential integrity audit (`src/etl/pipeline_audit.py`)
   - Step 4: Physics-informed feature pipeline (`src/features/feature_pipeline.py`)
   - Step 5: Candidate models execution (`src/models/baselines.py`, `machine_learning.py`, `hybrid_sarima_tree.py`)
   - Step 6: Multi-pillar quantitative evaluation suite (`src/models/eval_pillars.py`)
   - Step 7: Dual-track operational policy rules (`src/models/dual_track_eval.py`)
   - Step 8: Master manuscript table synchronization (`src/analysis/sync_manuscript_tables.py`)
2. **Execute Seasonal Regimes Analysis (if updating seasonal tensor)**:
   ```bash
   python3 src/analysis/season_analysis_volatility_runner.py
   ```
3. **Execute OTP Volatility Module (if updating factor weights)**:
   ```bash
   python3 otp_volatility_analysis/run_otp_volatility_analysis.py
   ```
4. **Run Verification & Commit**:
   - Run tests: `python3 -m unittest discover tests`
   - Update `results/00_VERSION_CONTROL_AND_PROVENANCE.md`
   - Commit all updated code, CSVs, and Excel workbooks to Git.

---

## 4. Master Table Catalog & Companion Spreadsheet Mapping

Every empirical table has an exact 1-to-1 match across Markdown manuscripts, conformed CSVs, and companion Excel workbooks:

| Table ID | Title / Scope | Manuscript Location | Conformed CSV (`results/manuscript_tables/`) | Companion Excel Workbook (`results/`) |
| :--- | :--- | :--- | :--- | :--- |
| **Table 4.1** | Multi-Source Data Foundation Census | `chp4-results.md` | `table_4_1_master_post_etl_multi_source_data_foundation_census.csv` | `01_top25_clustering/01_top25_clustering.xlsx` |
| **Table 4.2** | Post-ETL Master Summary Statistics | `chp4-results.md` | `table_4_2_post_etl_master_summary_descriptive_statistics.csv` | `01_top25_clustering/01_top25_clustering.xlsx` |
| **Table 4.3a** | Temporal Demarcation Evaluation | `chp4-results.md` | `table_4_3a_post_pandemic_temporal_demarcation_evaluation.csv` | `01_top25_clustering/seasonality_and_regimes/top25_seasonality_regimes_and_events.xlsx` |
| **Table 4.3b** | Annual Seasonal Volatility Regimes | `chp4-results.md` | `table_4_3b_master_annual_seasonal_volatility_regimes_summary.csv` | `01_top25_clustering/seasonality_and_regimes/season-analysis.xlsx` |
| **Table 4.4a** | Day-of-Week Volatility Archetypes | `chp4-results.md` | `table_4_4a_day_of_week_volatility_dynamics_and_operational_archetypes.csv` | `01_top25_clustering/seasonality_and_regimes/season-analysis.xlsx` |
| **Table 4.5** | Cross-Dataset Econometric Relationships | `chp4-results.md` | `table_4_5_master_cross_dataset_econometric_relationships.csv` | `01_top25_clustering/01_top25_clustering.xlsx` |
| **Table 4.6** | 9-Airport Factorial Specification | `chp4-results.md` | `table_4_6_nine_airport_experimental_cohort_factorial_specification.csv` | `02_4tier_filtering/02_4tier_filtering.xlsx` |
| **Table 4.7** | 9-Airport vs. Top 25 Descriptive Stats | `chp4-results.md` | `table_4_7_summary_descriptive_statistics_nine_airport_vs_top25.csv` | `02_4tier_filtering/02_4tier_filtering.xlsx` |
| **Table 4.8** | Day-of-Week Mean Daily Throughput | `chp4-results.md` | `table_4_8_day_of_week_mean_daily_passenger_throughput_nine_airports.csv` | `02_4tier_filtering/02_top9_cohort_comprehensive_analysis.xlsx` |
| **Table 4.9** | Empirical Lead-Lag Transfer Dynamics | `chp4-results.md` | `table_4_9_empirical_lead_lag_transfer_dynamics.csv` | `03_lead_lag_deconvolution/03_lead_lag_deconvolution.xlsx` |
| **Table 4.10** | Master Model Benchmark Matrix (2025 Holdout) | `chp4-results.md` | `table_4_10_master_model_benchmark_matrix.csv` | `04_model_execution_2025_holdout/04_model_execution_2025_holdout.xlsx` |
| **Table 4.11** | Master Multi-Pillar Hypothesis Matrix | `chp4-results.md` | `table_4_11_master_multi_pillar_hypothesis_evaluation_matrix.csv` | `05_robustness_resilience_generalizability/05_robustness_resilience_generalizability.xlsx` |
| **Table 5.1** | Dimension 1: Routine Accuracy (Robustness) | `chp5-discussion.md` | `table_5_1_evaluation_dimension_1_routine_operational_accuracy.csv` | `05_robustness_resilience_generalizability/05_robustness_resilience_generalizability.xlsx` |
| **Table 5.2** | Dimension 2: Resilience Under Shock | `chp5-discussion.md` | `table_5_2_evaluation_dimension_2_resilience_and_shock_performance.csv` | `05_robustness_resilience_generalizability/05_robustness_resilience_generalizability.xlsx` |
| **Table 5.3** | Dimension 3: Generalizability (Zero-Shot) | `chp5-discussion.md` | `table_5_3_evaluation_dimension_3_generalizability_and_cross_airport_transfer.csv` | `05_robustness_resilience_generalizability/05_robustness_resilience_generalizability.xlsx` |
| **Table 5.4** | Master Asymmetric Trade-Off Matrix | `chp5-discussion.md` | `table_5_4_master_asymmetric_trade_off_matrix.csv` | `05_robustness_resilience_generalizability/05_robustness_resilience_generalizability.xlsx` |

---

## 5. Pre-Commit Verification Checklist

Before creating any Git commit, verify every item on this checklist:

```bash
# 1. Verify zero Microsoft Word documents were modified:
git status --porcelain | grep -i '\.docx' || echo "CHECK 1 PASSED: Zero docx modified"

# 2. Synchronize all tables (if any numbers or manuscripts changed):
python3 src/analysis/sync_manuscript_tables.py

# 3. Verify the unit test suite passes:
python3 -m unittest discover tests

# 4. Check git status for unexpected or unversioned files:
git status

# 5. Commit with conventional commit formatting:
git add -A
git commit -m "feat/fix/docs: clear, descriptive summary of changes"
```

====================================================================================================
END OF STANDARD OPERATING PROCEDURE
====================================================================================================
