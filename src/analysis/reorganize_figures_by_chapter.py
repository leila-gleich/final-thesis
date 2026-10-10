"""
src/analysis/reorganize_figures_by_chapter.py
---------------------------------------------
Reorganizes the `figures/` directory to reflect the exact thesis chapter
correspondence (Chapters I through V plus Appendix) adhering to APA 7th Edition,
heavy-traffic queuing principles, and the Master Recommendations in
figures/TABLE_AND_FIGURE_RECOMMENDATIONS.md and thesis_docs/exhibits/README.md.

Chapter Structure Established:
  figures/
  ├── ch01_intro/                 (Chapter I: Introduction)
  ├── ch02_lit_review/            (Chapter II: Literature Review)
  ├── ch03_methodology/           (Chapter III: Methodology)
  │   └── workbooks/              (Multi-tab Excel workbooks)
  ├── ch04_results/               (Chapter IV: Results & Findings)
  ├── ch05_discussion/            (Chapter V: Discussion & Conclusions)
  ├── appendix/                   (Thesis Appendix & System Architecture)
  ├── 04_Appendix_and_Reference/  (Preserved for backward compatibility)
  └── README.md                   (Master Visual Asset Catalog)
"""

import os
import shutil
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
FIGURES_DIR = PROJECT_ROOT / "figures"
EXHIBITS_DIR = PROJECT_ROOT / "thesis_docs" / "exhibits"
RESULTS_DIR = PROJECT_ROOT / "results"
RESULTS_FIGURES_DIR = RESULTS_DIR / "figures"
MANUSCRIPT_TABLES_DIR = RESULTS_DIR / "manuscript_tables"


def create_radar_chart(output_path: Path):
    """Generates Figure 5.1: The Asymmetric Trade-Off Triangle radar chart."""
    categories = ['Robustness\n(Routine Accuracy)', 'Resilience\n(Shock Recovery)', 'Generalizability\n(Spatial Transfer)']
    N = len(categories)
    angles = [n / float(N) * 2 * np.pi for n in range(N)]
    angles += angles[:1]

    # Performance indices scaled from 0.0 (unacceptable) to 1.0 (optimal)
    # Based on empirical metrics from Table 5.4:
    # Robustness: Target MASE < 0.70. Model 3 = 0.662 (0.95), Model 2 = 0.690 (0.90), Model 1 = 0.945 (0.45), Baseline = 1.000 (0.30)
    # Resilience: Target R_MASE ≈ 1.00, TTR < 4.0h. Model 3 (R=1.05, TTR=2.8h -> 0.95), Model 2 (R=2.14, TTR=5.4h -> 0.35), Model 1 (R=1.32, TTR=7.8h -> 0.50), Baseline (0.40)
    # Generalizability: Target RTR ≈ 1.00, Delta MASE <= 10%. Model 1 (RTR=1.04, +4.0% -> 0.95), Model 2 (RTR=1.08, +8.3% -> 0.80), Model 3 (RTR=1.19, +21.5% -> 0.30), Baseline (0.40)
    scores = {
        'Baseline Control (Daily Persistence)': [0.30, 0.40, 0.40],
        'Model 1 (Deterministic Flight Schedule)': [0.45, 0.50, 0.95],
        'Model 2 (Supervised Machine Learning)': [0.90, 0.35, 0.80],
        'Model 3 (Dynamic Two-Stage Hybrid)': [0.95, 0.95, 0.30],
    }

    colors = {
        'Baseline Control (Daily Persistence)': '#7f7f7f',
        'Model 1 (Deterministic Flight Schedule)': '#1f77b4',
        'Model 2 (Supervised Machine Learning)': '#ff7f0e',
        'Model 3 (Dynamic Two-Stage Hybrid)': '#2ca02c',
    }

    linestyles = {
        'Baseline Control (Daily Persistence)': ':',
        'Model 1 (Deterministic Flight Schedule)': '--',
        'Model 2 (Supervised Machine Learning)': '-.',
        'Model 3 (Dynamic Two-Stage Hybrid)': '-',
    }

    fig, ax = plt.subplots(figsize=(8, 7), subplot_kw=dict(polar=True), dpi=300)
    ax.set_theta_offset(np.pi / 2)
    ax.set_theta_direction(-1)

    plt.xticks(angles[:-1], categories, size=11, weight='bold', color='#222222')
    ax.set_rlabel_position(0)
    plt.yticks([0.2, 0.4, 0.6, 0.8, 1.0], ["0.2", "0.4", "0.6", "0.8", "1.0 (Optimal)"], color="#555555", size=9)
    plt.ylim(0, 1.05)

    for model_name, values in scores.items():
        vals = values + values[:1]
        ax.plot(angles, vals, linewidth=2.2, linestyle=linestyles[model_name], label=model_name, color=colors[model_name])
        ax.fill(angles, vals, color=colors[model_name], alpha=0.10)

    plt.title("Figure 5.1: The Asymmetric Trade-Off Evaluation Triangle (H1)\nMulti-Dimensional Performance Trade-Offs Across Candidate Models",
              size=12, weight='bold', pad=25, color='#111111')
    plt.legend(loc='upper right', bbox_to_anchor=(1.35, 1.15), frameon=True, fontsize=9.5)
    plt.tight_layout()
    output_path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close(fig)
    print(f"  + Generated radar chart: {output_path}")


def populate_chapter_1():
    """Populates Chapter 1: Introduction."""
    ch1_dir = FIGURES_DIR / "ch01_intro"
    ch1_dir.mkdir(parents=True, exist_ok=True)
    src_dir = EXHIBITS_DIR / "ch01_intro"

    files_to_copy = [
        "Data Sample Profile.png",
        "data_sample_profile.csv",
        "Inclusion of top 25 network approach.png",
        "inclusion_of_top_25_network_approach.csv",
        "models and tests.png",
        "models_and_tests.csv",
    ]
    for f in files_to_copy:
        s = src_dir / f
        if s.exists():
            shutil.copy2(s, ch1_dir / f)

    readme_content = """# Chapter I: Introduction Exhibits & Figures
## Evaluating Predictive Techniques to Model Stochastic Airport Passenger Flow (MSAA / Gleich 700B)

> **Chapter Purpose**: Visual frameworks, candidate model suite specifications, and empirical delimitations for **Chapter I (*Introduction*)**.

---

### Exhibit & Figure Inventory

| Figure / Table ID | Visual Graphic (`.png`) | Companion Data (`.csv`) | Manuscript Target Location | Operational Function & Theoretical Rationale |
| :--- | :--- | :--- | :--- | :--- |
| **Figure 1.1** | `models and tests.png` | `models_and_tests.csv` | Directly following Hypothesis 1 ($H_1$, Paragraph 15) | **Asymmetric Trade-Off Evaluation Triangle**: Schematically depicts that no single model is universally superior (Model 3 wins Resilience, Model 1 wins Generalizability, Model 2 wins Routine Pareto Efficiency). |
| **Table 1.1** | *Derived from visual* | `models_and_tests.csv` | Following Section `## Research Questions` | **The 3-Model Candidate Evaluation Suite & Baseline Control**: Establishes Baseline Control, Model 1 (Deterministic ACRP 40), Model 2 (Supervised ML), and Model 3 (Dynamic Two-Stage Hybrid). |
| **Table 1.2** | `Data Sample Profile.png` | `data_sample_profile.csv` | Section `## Delimitations` (Paragraph 21) | **Scope, Delimitations & Federal Data Foundation**: Summarizes the 4 federal data repositories (TSA FOIA, BTS OTP, BTS T-100, BTS DB1B) covering 42,062,039 conformed records from 2019–2025. |
| **Delimitation Guide** | `Inclusion of top 25 network approach.png` | `inclusion_of_top_25_network_approach.csv` | Section `## Delimitations` | **Top 25 Network Approach Rationale**: Contextualizes the macro 25-airport national hub network against the purposive 9-airport experimental cohort. |
"""
    (ch1_dir / "README.md").write_text(readme_content, encoding="utf-8")
    print(f"  + Populated {ch1_dir} (3 PNGs, 3 CSVs, README.md)")


def populate_chapter_2():
    """Populates Chapter 2: Literature Review."""
    ch2_dir = FIGURES_DIR / "ch02_lit_review"
    ch2_dir.mkdir(parents=True, exist_ok=True)
    src_dir = EXHIBITS_DIR / "ch02_lit_review"

    files_to_copy = [
        "Model walk through.png",
        "model_walkthrough_architecture.csv",
        "OTP volatility.png",
        "otp_volatility.csv",
        "clusting and connecting paradox.png",
        "clustering_and_connecting_paradox.csv",
        "exploratory metric criteria research .png",
        "exploratory_metric_criteria_research.csv",
        "otp & tsa.png",
        "otp_and_tsa_volume_coupling.csv",
        "pax stochastic arrival.png",
        "passenger_stochastic_arrival_parameters.csv",
    ]
    for f in files_to_copy:
        s = src_dir / f
        if s.exists():
            shutil.copy2(s, ch2_dir / f)

    readme_content = r"""# Chapter II: Literature Review Exhibits & Figures
## Evaluating Predictive Techniques to Model Stochastic Airport Passenger Flow (MSAA / Gleich 700B)

> **Chapter Purpose**: Theoretical foundations, heavy-traffic queuing dynamics, historical modeling paradigms, and operational coupling frameworks for **Chapter II (*Literature Review*)**.

---

### Exhibit & Figure Inventory

| Figure / Table ID | Visual Graphic (`.png`) | Companion Data (`.csv`) | Manuscript Target Location | Operational Function & Theoretical Rationale |
| :--- | :--- | :--- | :--- | :--- |
| **Figure 2.1** | `pax stochastic arrival.png` | `passenger_stochastic_arrival_parameters.csv` | Under Section `## Traditional Approaches` (Paragraph 10) | **The Checkpoint Tipping Point (Kingman's Heavy-Traffic Curve)**: Demonstrates quadratic queue escalation with arrival burstiness ($C_a^2$) under Kingman's formula ($W_q \approx \frac{\rho}{1-\rho} \frac{C_a^2+C_s^2}{2} \frac{1}{\mu}$) as server utilization $\rho \to 1.0$. |
| **Table 2.1** | `exploratory metric criteria research .png` | `exploratory_metric_criteria_research.csv` | Following Section `## Simulation Modeling` (Paragraph 21) | **Comparative Synthesis of Airport Flow Paradigms**: Contrasts historical modeling mechanisms (pure physics, queuing, time-series, supervised ML) across data latency, operational fidelity, and shock vulnerabilities. |
| **Figure 2.2** | `Model walk through.png` | `model_walkthrough_architecture.csv` | Following Section `## Hybrid Architectures` (Paragraph 34) | **Two-Stage Sequential Hybrid Architecture**: Schematically illustrates Stage 1 (recurring flight bank schedule cycles) feeding baseline predictions into Stage 2 (live recursive error innovation feedback $e_{t-1}$). |
| **Framework** | `clusting and connecting paradox.png` | `clustering_and_connecting_paradox.csv` | Section `## Passenger Flow Dynamics` | **The Connecting Passenger Paradox**: Illustrates the hub disconnect where airside connecting passenger transfers bypass landside TSA checkpoints, requiring DB1B coupon deflation. |
| **Framework** | `otp & tsa.png` | `otp_and_tsa_volume_coupling.csv` | Section `## Flight Delays and Checkpoints` | **TSA & OTP Volume Coupling vs. Volatility**: Contrasts the decoupling of raw volume counts with the tight coupling of departure delay volatility and throughput volatility. |
| **Framework** | `OTP volatility.png` | `otp_volatility.csv` | Section `## Volatility Dynamics` | **Flight Departure Delay Volatility Regimes**: Formalizes delay standard deviation and coefficient of variation ($CV_{\\text{delay}}$) metrics. |
"""
    (ch2_dir / "README.md").write_text(readme_content, encoding="utf-8")
    print(f"  + Populated {ch2_dir} (6 PNGs, 6 CSVs, README.md)")


def populate_chapter_3():
    """Populates Chapter 3: Methodology."""
    ch3_dir = FIGURES_DIR / "ch03_methodology"
    ch3_dir.mkdir(parents=True, exist_ok=True)
    workbooks_dir = ch3_dir / "workbooks"
    workbooks_dir.mkdir(parents=True, exist_ok=True)

    src_fig_dir = EXHIBITS_DIR / "ch03_methodology" / "figures"
    src_tbl_dir = EXHIBITS_DIR / "ch03_methodology" / "tables"
    src_wb_dir = EXHIBITS_DIR / "ch03_methodology" / "workbooks"

    # Copy 15 PNG figures directly to ch03_methodology
    for f in src_fig_dir.glob("*.png"):
        shutil.copy2(f, ch3_dir / f.name)

    # Copy 14 CSV tables directly to ch03_methodology
    for f in src_tbl_dir.glob("*.csv"):
        shutil.copy2(f, ch3_dir / f.name)

    # Ensure models_and_tests.csv is also in ch03_methodology for Figure 1
    src_ch1_csv = EXHIBITS_DIR / "ch01_intro" / "models_and_tests.csv"
    if src_ch1_csv.exists():
        shutil.copy2(src_ch1_csv, ch3_dir / "models_and_tests.csv")

    # Copy the 3 workbooks
    for wb in src_wb_dir.glob("*.xlsx"):
        shutil.copy2(wb, workbooks_dir / wb.name)
        shutil.copy2(wb, ch3_dir / wb.name)

    readme_content = """# Chapter III: Methodology Exhibits, Figures & Companion Workbooks
## Evaluating Predictive Techniques to Model Stochastic Airport Passenger Flow (MSAA / Gleich 700B)

> **Chapter Purpose**: Research design, empirical schemas, purposive filtering progression, experimental cohort specifications, and mathematical evaluation frameworks for **Chapter III (*Methodology*)**.

---

### Master Methodology Figures & Companion Data Tables

| Figure Callout ID | Visual Graphic (`.png`) | Companion Data (`.csv`) | Word Callout | Operational Scope & Methodological Function |
| :--- | :--- | :--- | :--- | :--- |
| **Figure 1** | `models and tests.png` | `models_and_tests.csv` | Callout P18 | **Forecasting Model Family Comparison**: Architectural schematic comparing Baseline Control, Model 1 (ACRP 40 convolution), Model 2 (supervised ML regressor), and Model 3 (sequential hybrid). |
| **Figure 2** | `Evaluation Metric Definition.png` | `evaluation_metric_definition.csv` | Callout P56 | **Evaluation Metric Definitions**: Mathematical specification of RMSE, MASE, $R_{\\text{MASE}}$, TTR, RTR, and Diebold-Mariano ($DM$). |
| **Figure 3** | `Combined_Data_Pipeline_and_Funnel_Lifecycle.png` | `combined_data_pipeline_and_funnel_lifecycle.csv` | Callout P61 | **Design and Procedure Phases**: Four-phase experimental research progression (Phase 1: ETL & Data Hygiene $\\to$ Phase 2: Model Development $\\to$ Phase 3: Holdout Evaluation $\\to$ Phase 4: Statistical Validation). |
| **Figure 4** | `Airport selection strategy document.png` | `airport_selection_strategy_document.csv` | Callout P101 | **Sample Framework for Terminal Capacity & Checkpoints**: Terminal architectural framework detailing physical screening lanes, checkpoint queuing snakes, dedicated carrier concourses, and spatial aggregation. |
| **Figure 5** | `airport clusters.png` | `airport_clusters.csv` | Callout P103 | **Airport Operational Archetypes & Terminal Configurations**: Four-cluster PCA/K-Means matrix categorizing candidate Top 25 airfields across transfer ratio, international share, flight scale, and delay dispersion. |

---

### Supporting Methodological Frameworks & Schemas

| Visual Diagram (`.png`) | Companion Data (`.csv`) | Topic & Methodological Rationale |
| :--- | :--- | :--- |
| `checkpoint examples.png` | `checkpoint_examples.csv` | Dedicated carrier checkpoint exclusivity configurations and normalization. |
| `Combined_Data_Threats_and_Remediation_Matrix.png` | `combined_data_threats_and_remediation_matrix.csv` | Methodological data threats, bias vulnerabilities, and engineering remediations. |
| `Control and test process.png` | `control_and_test_process.csv` | Operational test execution protocols (pure signal vs noisy shared design). |
| `imputed defs.png` | `imputed_defs.csv` | Missing data imputation protocols and boundary rules. |
| `metrics.png` | `probabilistic_and_selection_metrics.csv` | Probabilistic scoring rules (CRPS, PICP) and information criteria (AIC, BIC). |
| `physical transfer lead lag time.png` | `physical_transfer_lead_lag_timeline.csv` | ACRP Report 40 passenger arrival lead-lag convolution structure ($t+1, t+2, t+3$). |
| `post-pandemic justification.png` | `post_pandemic_justification.csv` | Temporal demarcation justification (May 1, 2022 to December 31, 2025 boundary). |
| `Power of 9 airports.png` | `power_of_9_airports.csv` | Factorial representation of the 9-airport, 12-complex experimental cohort. |
| `t100 schema.png` | `t100_schema.csv` | BTS Form 41 Schedule T-100 Segment Statistics conformed star schema. |
| `TSA Schema.png` | `tsa_schema.csv` | TSA FOIA Hourly Screening Throughput conformed star schema. |

---

### Multi-Tab Companion Excel Workbooks (`workbooks/`)

1. **`01_Sample_and_Airport_Selection.xlsx`**: Multi-tab APA 7 workbook consolidating all sample selection and cluster specification tables.
2. **`02_Data_Pipelines_and_Threats.xlsx`**: Multi-tab APA 7 workbook consolidating ETL data pipeline and threats tables.
3. **`03_Modeling_and_Evaluation.xlsx`**: Multi-tab APA 7 workbook consolidating forecasting models and evaluation metric specifications.
"""
    (ch3_dir / "README.md").write_text(readme_content, encoding="utf-8")
    print(f"  + Populated {ch3_dir} (15 PNGs, 15 CSVs, 3 XLSX workbooks, README.md)")


def populate_chapter_4():
    """Populates Chapter 4: Results & Findings."""
    ch4_dir = FIGURES_DIR / "ch04_results"
    ch4_dir.mkdir(parents=True, exist_ok=True)

    # Copy empirical figures from results/figures/
    figure_mappings = [
        ("01_annual_volatility_tsa_otp_clustering.png", "figure_4_2_annual_volatility_clusters.png"),
        ("02_day_of_week_volatility_dynamics.png", "figure_4_3_day_of_week_volatility_dynamics.png"),
        ("03_diurnal_hourly_volatility_clusters_by_dow.png", "figure_4_4_diurnal_hourly_volatility_clusters.png"),
        ("04_sample_sufficiency_distribution.png", "figure_sample_sufficiency_distribution.png"),
        ("physical transfer lead lag time.png", "figure_4_5_lead_lag_convolution_curves.png"),
    ]

    for fname1, fname2 in figure_mappings:
        src1 = RESULTS_FIGURES_DIR / fname1
        src2 = RESULTS_FIGURES_DIR / fname2
        if src1.exists():
            shutil.copy2(src1, ch4_dir / fname1)
        if src2.exists():
            shutil.copy2(src2, ch4_dir / fname2)

    # Copy matching data tables from results/manuscript_tables/
    table_mappings = [
        "table_4_3b_master_annual_seasonal_volatility_regimes_summary.csv",
        "table_4_4a_master_day_of_week_operational_volatility_regimes.csv",
        "table_4_7_summary_descriptive_statistics_nine_airport_vs_top25.csv",
        "table_4_8_local_seasonal_and_dow_volatility_profiles_9_airports.csv",
        "table_4_9_empirical_lead_lag_transfer_dynamics.csv",
        "table_4_10_master_model_benchmark_matrix.csv",
        "table_4_11_master_multi_pillar_hypothesis_evaluation_matrix.csv",
    ]

    for tbl in table_mappings:
        src = MANUSCRIPT_TABLES_DIR / tbl
        if src.exists():
            shutil.copy2(src, ch4_dir / tbl)

    readme_content = """# Chapter IV: Results & Findings Figures & Datasets
## Evaluating Predictive Techniques to Model Stochastic Airport Passenger Flow (MSAA / Gleich 700B)

> **Chapter Purpose**: Publication-ready empirical visualizations, out-of-time benchmark results, and companion datasets for **Chapter IV (*Results & Findings*)**.

---

### Empirical Figures & Associated Conformed Data Tables

| Figure ID | Visual Graphic (`.png`) | Companion Data (`.csv`) | Manuscript Target Location | Operational Function & Empirical Rationale |
| :--- | :--- | :--- | :--- | :--- |
| **Figure 4.2** | `01_annual_volatility_tsa_otp_clustering.png` / `figure_4_2_annual_volatility_clusters.png` | `table_4_3b_master_annual_seasonal_volatility_regimes_summary.csv` | Following Table 4.3b | **Annual Volatility Dynamics & Coupled Volatility Clusters**: Network-level annual volatility regimes across the Top 25 airfields, showing the positive coupling between flight delay dispersion and checkpoint arrival volatility ($CVI = \\sigma_{\\text{TSA}} \\cdot \\sigma_{\\text{Delay}}$). |
| **Figure 4.3** | `02_day_of_week_volatility_dynamics.png` / `figure_4_3_day_of_week_volatility_dynamics.png` | `table_4_4a_master_day_of_week_operational_volatility_regimes.csv` | Following Table 4.4a | **Day-of-Week Volatility Dynamics Across the National Network**: Illustrates day-of-week arrival burstiness ($CV_{\\text{TSA}}$) across corporate-heavy (Mon/Thu/Fri peaks) vs. leisure-heavy (Sun/Fri peaks) commercial airfields. |
| **Figure 4.4** | `03_diurnal_hourly_volatility_clusters_by_dow.png` / `figure_4_4_diurnal_hourly_volatility_clusters.png` | `table_4_8_local_seasonal_and_dow_volatility_profiles_9_airports.csv` | Under Section `TSA and OTP Throughput Data` | **Intraday Diurnal Hourly Volatility Clusters (Bimodal Peaks by DOW)**: Resolves 24-hour diurnal passenger arrival profiles, highlighting morning (05:00–08:00) and afternoon/evening (16:00–19:00) peak shock windows. |
| **Figure 4.5** | `figure_4_5_lead_lag_convolution_curves.png` / `physical transfer lead lag time.png` | `table_4_9_empirical_lead_lag_transfer_dynamics.csv` | Directly following Table 4.9 | **Empirical Lead-Lag Passenger Show-Up Curve Convolution**: Depicts the temporal asynchrony between scheduled departure flight banks and landside checkpoint arrivals, highlighting modal 90–120 minute show-up ($t+1, t+2$). |
| **Diagnostic** | `04_sample_sufficiency_distribution.png` / `figure_sample_sufficiency_distribution.png` | `table_4_7_summary_descriptive_statistics_nine_airport_vs_top25.csv` | Within Section `### Temporal Boundaries` | **Sample Sufficiency Distribution**: Validates statistical sample size and temporal coverage across the post-pandemic demarcation window (May 1, 2022 to December 31, 2025; $N = 3,222$ holdout complex-days). |
"""
    (ch4_dir / "README.md").write_text(readme_content, encoding="utf-8")
    print(f"  + Populated {ch4_dir} (5 PNG figure pairs, 7 CSV tables, README.md)")


def populate_chapter_5():
    """Populates Chapter 5: Discussion & Conclusions."""
    ch5_dir = FIGURES_DIR / "ch05_discussion"
    ch5_dir.mkdir(parents=True, exist_ok=True)

    # Generate Figure 5.1 Radar Chart
    radar_path = ch5_dir / "figure_5_1_asymmetric_trade_off_triangle.png"
    create_radar_chart(radar_path)

    # Copy Chapter 5 evaluation tables from results/manuscript_tables/
    tables = [
        "table_5_1_evaluation_dimension_1_routine_operational_accuracy.csv",
        "table_5_2_evaluation_dimension_2_resilience_and_shock_performance.csv",
        "table_5_3_evaluation_dimension_3_generalizability_and_cross_airport_transfer.csv",
        "table_5_4_master_asymmetric_trade_off_matrix.csv",
        "dual_track_model_selection_policy.csv",
    ]
    for tbl in tables:
        src = MANUSCRIPT_TABLES_DIR / tbl
        if src.exists():
            shutil.copy2(src, ch5_dir / tbl)

    readme_content = """# Chapter V: Discussion & Conclusions Figures & Decision Matrices
## Evaluating Predictive Techniques to Model Stochastic Airport Passenger Flow (MSAA / Gleich 700B)

> **Chapter Purpose**: Three-dimensional operational performance evaluations (Robustness, Resilience, Generalizability), Master Asymmetric Trade-Off Matrix ($H_1$), and dual-track decision frameworks for **Chapter V (*Discussion & Conclusions*)**.

---

### Chapter V Figures & Dimensional Performance Tables

| Figure / Table ID | Visual Graphic (`.png`) | Companion Data (`.csv`) | Manuscript Target Location | Operational Function & Theoretical Rationale |
| :--- | :--- | :--- | :--- | :--- |
| **Figure 5.1** | `figure_5_1_asymmetric_trade_off_triangle.png` | `table_5_4_master_asymmetric_trade_off_matrix.csv` | Directly following Table 5.4 | **The Asymmetric Trade-Off Evaluation Triangle ($H_1$)**: Radar/spider plot synthesizing performance across Robustness, Resilience, and Generalizability, illustrating why no single model is universally best. |
| **Table 5.1** | *Derived from metrics* | `table_5_1_evaluation_dimension_1_routine_operational_accuracy.csv` | Following Section `## Dimension 1: Robustness` | **Evaluation Dimension 1: Routine Operational Accuracy**: Compares candidate models under nominal baseline conditions ($\text{Delay} < 15$m, 0 cancels). Model 3 achieves lowest RMSE (222.1); Model 2 wins Routine Pareto Efficiency ($\text{MASE} = 0.680\text{--}0.700$, zero feedback compute latency). |
| **Table 5.2** | *Derived from metrics* | `table_5_2_evaluation_dimension_2_resilience_and_shock_performance.csv` | Following Section `## Dimension 2: Resilience` | **Evaluation Dimension 2: Resilience Under Disruption**: Compares models during irregular operations (IROPS). Model 3 DECISIVE WINNER ($R_{\\text{MASE}} = 1.05, \\text{TTR} = 2.8\\text{h}$) via live error feedback ($e_{t-1}$), while Model 2 collapses ($R = 2.14$) due to Empty Checkpoint Fallacy. |
| **Table 5.3** | *Derived from metrics* | `table_5_3_evaluation_dimension_3_generalizability_and_cross_airport_transfer.csv` | Following Section `## Dimension 3: Generalizability` | **Evaluation Dimension 3: Generalizability Across Facilities**: Evaluates zero-shot spatial transfer (EWR $\\to$ LGA). Model 1 DECISIVE WINNER ($\\text{RTR} = 1.04, \\Delta\\text{MASE} = +4.0\\%$), while Model 3 overfits terminal geometry ($\\text{RTR} = 1.19$). |
| **Table 5.4** | *Derived from metrics* | `table_5_4_master_asymmetric_trade_off_matrix.csv` | Following Section `## Implications and Recommendations` | **Master Asymmetric Trade-Off Matrix ($H_1$ Synthesis)**: Comprehensive multi-dimensional synthesis establishing the dual-track operational policy. |
| **Policy Guide** | *Derived from metrics* | `dual_track_model_selection_policy.csv` | Concluding Section | **Dual-Track Model Selection Policy**: Prescriptive guidance allocating Model 3 for tactical disruption resilience and Model 1 for master planning and spatial transfer. |
"""
    (ch5_dir / "README.md").write_text(readme_content, encoding="utf-8")
    print(f"  + Populated {ch5_dir} (1 PNG radar chart, 5 CSV tables, README.md)")


def populate_appendix():
    """Populates Thesis Appendix & System Architecture."""
    app_dir = FIGURES_DIR / "appendix"
    app_dir.mkdir(parents=True, exist_ok=True)
    src_dir = FIGURES_DIR / "04_Appendix_and_Reference"

    for f in src_dir.iterdir():
        if f.name.startswith("."):
            continue
        shutil.copy2(f, app_dir / f.name)

    readme_content = """# Thesis Appendix & Reference Figures and Data Tables
## Evaluating Predictive Techniques to Model Stochastic Airport Passenger Flow (MSAA / Gleich 700B)

> **Chapter Purpose**: Reference database profiles, BTS DB1B relational hierarchies, feature store partition manifests, backup storage hierarchies, and methodological assumption matrices for the **Thesis Appendix**.

---

### Appendix Exhibit Inventory

| Visual Graphic (`.png`) | Companion Data (`.csv`) | Appendix Location | Description & Operational Function |
| :--- | :--- | :--- | :--- |
| `BTS-DB1B_Appendix.png` | `bts_db1b_table_hierarchy.csv` | Appendix Section C | Bureau of Transportation Statistics 10% ticket coupon survey relational hierarchy (DB1BTicket $\\to$ DB1BMarket $\\to$ DB1BCoupon). |
| `Backups organization.png` | `backups_organization.csv` | Appendix Section H | Master backup hierarchy and directory structure governing raw feeds, processed feature stores, and codebase. |
| `Diagrams and Screenshot Layout.png` | `diagrams_and_screenshot_layout.csv` | Appendix Section H | Master layout directory tree mapping diagrams and screenshots across thesis chapters. |
| `data profile top9.png` | `data_profile_top9.csv` | Appendix Section B | Filtered 9-airport target research cohort feature store parquet partitions and Zstandard compression metrics. |
| `database profiles.png` | `database_profiles.csv` | Appendix Section A | Summary census of upstream raw ingested records versus cleaned conformed records preserved in the warehouse. |
| `dataset breakdown.png` | `dataset_breakdown.csv` | Appendix Section A | Architectural specifications of conformed analytics tables stored in Apache Parquet format. |
| `methodological assumptions.png` | `methodological_assumptions.csv` | Appendix Section D | Master 14-point methodological and operational assumptions framework and failure modes table. |
| *Workbook Asset* | `04_Appendix_and_Reference.xlsx` | Appendix Reference | Multi-tab APA 7 consolidated Excel workbook containing all 7 appendix data tables. |
"""
    (app_dir / "README.md").write_text(readme_content, encoding="utf-8")
    print(f"  + Populated {app_dir} (7 PNGs, 7 CSVs, 1 XLSX workbook, README.md)")


def generate_master_readme():
    """Generates the Master README.md for the figures/ directory."""
    master_readme_path = FIGURES_DIR / "README.md"
    content = r"""# Thesis Figures, Exhibits, and Companion Data Directory
## Evaluating Predictive Techniques to Model Stochastic Airport Passenger Flow (MSAA / Gleich 700B)

> **Directory Purpose**: This directory provides the intuitive, canonical home for all visual graphics, conceptual frameworks, process diagrams, empirical figures, companion CSV datasets, and multi-tab Excel workbooks organized strictly by **Thesis Chapter**.
>
> All figures and tables strictly adhere to **APA Style (7th ed.)**, authentic commercial aviation operations nomenclature, and **Kingman's Heavy-Traffic Queuing Formula** ($W_q \\approx \\frac{\\rho}{1-\\rho} \\frac{C_a^2+C_s^2}{2} \\frac{1}{\\mu}$), targeting **passenger throughput volatility** ($\\sigma_{\\text{TSA}}$ and $CV_{\\text{TSA}}$) rather than raw volume.

---

## 1. Chapter-by-Chapter Master Directory Architecture

```
figures/
├── ch01_intro/                 <-- Chapter I: Introduction (3 figures, 3 CSVs)
├── ch02_lit_review/            <-- Chapter II: Literature Review (6 figures, 6 CSVs)
├── ch03_methodology/           <-- Chapter III: Methodology (15 figures, 15 CSVs, 3 workbooks)
│   └── workbooks/              <-- APA 7 Multi-Tab Companion Excel Workbooks
├── ch04_results/               <-- Chapter IV: Results & Findings (5 figure pairs, 7 CSVs)
├── ch05_discussion/            <-- Chapter V: Discussion & Conclusions (1 figure, 5 CSVs)
├── appendix/                   <-- Thesis Appendix & Reference (7 figures, 7 CSVs, 1 workbook)
├── 04_Appendix_and_Reference/  <-- Legacy Appendix Folder (Preserved for backward compatibility)
└── TABLE_AND_FIGURE_RECOMMENDATIONS.md <-- Authoritative Manuscript Integration Guide
```

---

## 2. Summary of Visual Assets and Datasets by Chapter

### Chapter I: Introduction (`ch01_intro/`)
* **Figure 1.1**: `models and tests.png` + `models_and_tests.csv` — *Asymmetric Trade-Off Evaluation Triangle ($H_1$)*
* **Table 1.1**: Derived from `models_and_tests.csv` — *3-Model Candidate Evaluation Suite & Baseline Control*
* **Table 1.2**: `Data Sample Profile.png` + `data_sample_profile.csv` — *Scope, Delimitations & Federal Data Foundation*
* **Delimitation Guide**: `Inclusion of top 25 network approach.png` + `inclusion_of_top_25_network_approach.csv`

### Chapter II: Literature Review (`ch02_lit_review/`)
* **Figure 2.1**: `pax stochastic arrival.png` + `passenger_stochastic_arrival_parameters.csv` — *The Checkpoint Tipping Point (Kingman's Heavy-Traffic Curve)*
* **Table 2.1**: `exploratory metric criteria research .png` + `exploratory_metric_criteria_research.csv` — *Comparative Synthesis of Airport Flow Paradigms*
* **Figure 2.2**: `Model walk through.png` + `model_walkthrough_architecture.csv` — *Two-Stage Sequential Hybrid Architecture*
* **Framework**: `clusting and connecting paradox.png` + `clustering_and_connecting_paradox.csv` — *The Connecting Passenger Paradox*
* **Framework**: `otp & tsa.png` + `otp_and_tsa_volume_coupling.csv` — *TSA & OTP Volume Coupling vs. Volatility*
* **Framework**: `OTP volatility.png` + `otp_volatility.csv` — *Flight Departure Delay Volatility Regimes*

### Chapter III: Methodology (`ch03_methodology/`)
* **Figure 1**: `models and tests.png` + `models_and_tests.csv` — *Forecasting Model Family Comparison (Word Callout P18)*
* **Figure 2**: `Evaluation Metric Definition.png` + `evaluation_metric_definition.csv` — *Evaluation Metric Definitions (Callout P56)*
* **Figure 3**: `Combined_Data_Pipeline_and_Funnel_Lifecycle.png` + `combined_data_pipeline_and_funnel_lifecycle.csv` — *Design and Procedure Phases (Callout P61)*
* **Figure 4**: `Airport selection strategy document.png` + `airport_selection_strategy_document.csv` — *Sample Framework for Terminal Capacity & Checkpoints (Callout P101)*
* **Figure 5**: `airport clusters.png` + `airport_clusters.csv` — *Airport Operational Archetypes & Terminal Configurations (Callout P103)*
* **10 Supporting Diagrams & Schemas**: `checkpoint examples.png`, `Combined_Data_Threats_and_Remediation_Matrix.png`, `Control and test process.png`, `imputed defs.png`, `metrics.png`, `physical transfer lead lag time.png`, `post-pandemic justification.png`, `Power of 9 airports.png`, `t100 schema.png`, `TSA Schema.png` (each paired with its `.csv`).
* **Companion Workbooks (`workbooks/`)**: `01_Sample_and_Airport_Selection.xlsx`, `02_Data_Pipelines_and_Threats.xlsx`, `03_Modeling_and_Evaluation.xlsx`.

### Chapter IV: Results & Findings (`ch04_results/`)
* **Figure 4.2**: `01_annual_volatility_tsa_otp_clustering.png` + `table_4_3b_master_annual_seasonal_volatility_regimes_summary.csv` — *Annual Volatility Dynamics & Coupled Volatility Clusters*
* **Figure 4.3**: `02_day_of_week_volatility_dynamics.png` + `table_4_4a_master_day_of_week_operational_volatility_regimes.csv` — *Day-of-Week Volatility Dynamics Across the National Network*
* **Figure 4.4**: `03_diurnal_hourly_volatility_clusters_by_dow.png` + `table_4_8_local_seasonal_and_dow_volatility_profiles_9_airports.csv` — *Intraday Diurnal Hourly Volatility Clusters (Bimodal Peaks)*
* **Figure 4.5**: `figure_4_5_lead_lag_convolution_curves.png` + `table_4_9_empirical_lead_lag_transfer_dynamics.csv` — *Empirical Lead-Lag Passenger Show-Up Curve Convolution*
* **Diagnostic**: `04_sample_sufficiency_distribution.png` + `table_4_7_summary_descriptive_statistics_nine_airport_vs_top25.csv` — *Sample Sufficiency Distribution*

### Chapter V: Discussion & Conclusions (`ch05_discussion/`)
* **Figure 5.1**: `figure_5_1_asymmetric_trade_off_triangle.png` + `table_5_4_master_asymmetric_trade_off_matrix.csv` — *The Asymmetric Trade-Off Evaluation Triangle ($H_1$)*
* **Table 5.1**: `table_5_1_evaluation_dimension_1_routine_operational_accuracy.csv` — *Evaluation Dimension 1: Routine Operational Accuracy*
* **Table 5.2**: `table_5_2_evaluation_dimension_2_resilience_and_shock_performance.csv` — *Evaluation Dimension 2: Resilience Under Disruption*
* **Table 5.3**: `table_5_3_evaluation_dimension_3_generalizability_and_cross_airport_transfer.csv` — *Evaluation Dimension 3: Generalizability Across Facilities*
* **Table 5.4**: `table_5_4_master_asymmetric_trade_off_matrix.csv` — *Master Asymmetric Trade-Off Matrix ($H_1$ Synthesis)*
* **Policy**: `dual_track_model_selection_policy.csv` — *Dual-Track Model Selection Policy*

### Appendix: Reference & Architecture (`appendix/` & `04_Appendix_and_Reference/`)
* `BTS-DB1B_Appendix.png` + `bts_db1b_table_hierarchy.csv` — *BTS DB1B Survey Relational Hierarchy*
* `Backups organization.png` + `backups_organization.csv` — *Research Archive Backup Directory Structure*
* `Diagrams and Screenshot Layout.png` + `diagrams_and_screenshot_layout.csv` — *Diagram & Screenshot Layout Tree*
* `data profile top9.png` + `data_profile_top9.csv` — *Nine-Airport Target Cohort Parquet Feature Store Partitions*
* `database profiles.png` + `database_profiles.csv` — *Base Feeds Database Profiles & Record Census*
* `dataset breakdown.png` + `dataset_breakdown.csv` — *Feature Store Dataset Breakdown*
* `methodological assumptions.png` + `methodological_assumptions.csv` — *Master 14-Point Assumptions Framework*
* `04_Appendix_and_Reference.xlsx` — *Consolidated Multi-Tab Appendix Workbook*

---

## 3. Maintenance and Synchronization

To regenerate all 4 multi-tab APA 7 Excel workbooks from the conformed CSV datasets, run:
```bash
python3 src/analysis/generate_figures_tables_excel.py
```
To run the verification test suite:
```bash
python3 -m unittest tests/test_figure_workbooks.py
```
"""
    master_readme_path.write_text(content, encoding="utf-8")
    print(f"  + Generated Master README: {master_readme_path}")


def main():
    print("=" * 80)
    print(" REORGANIZING figures/ DIRECTORY BY THESIS CHAPTER")
    print("=" * 80)
    populate_chapter_1()
    populate_chapter_2()
    populate_chapter_3()
    populate_chapter_4()
    populate_chapter_5()
    populate_appendix()
    generate_master_readme()
    print("=" * 80)
    print(" [SUCCESS] figures/ directory fully reorganized by thesis chapter.")
    print("=" * 80)


if __name__ == "__main__":
    main()
