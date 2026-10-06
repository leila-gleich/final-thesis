# Thesis Manuscripts, Recommendations & Research Notes Directory

Welcome to the `thesis_docs/` directory of the repository. This folder is organized into four distinct, intuitive pillars:

1. **`ssot/`**: The authoritative **Single Source of Truth (SSOT)** specifications for all five chapters (`Chapter_1_SSOT.md` through `Chapter_5_SSOT.md`), defining immutable empirical metrics, mathematical formulations, sample sizes, and literature lineages.
2. **`manuscripts/`**: Formal thesis manuscript chapters (Word `.docx` and Markdown `.md`), complete unified drafts, graduate proposal, master APA 7 references, and publication figures.
3. **`recommendations/`**: Actionable guidance, turn-key chapter update guides (`chapter_updates/`), defense strategy, and master technical implementation plans (`implementation_plans/`).
4. **`notes/`**: Empirical research notes, methodological justifications (`methodology_memos/`), step-by-step validation reports (`empirical_walkthroughs/`), and governance standards (`provenance_and_standards/`).

---

## Directory Sitemap & File Index

```
thesis_docs/
├── README.md                           <-- Master directory guide (this file)
│
├── ssot/                               <-- Master Single Source of Truth (SSOT) Specifications
│   ├── README.md                       (SSOT directory overview, governance & cross-chapter map)
│   ├── Chapter_1_SSOT.md               (Chapter I: Research Question, H1, Triad, Scope)
│   ├── Chapter_2_SSOT.md               (Chapter II: Literature Taxonomy, Critique, Citations)
│   ├── Chapter_3_SSOT.md               (Chapter III: Mathematical Specs, Pipeline, 84-Cell Grid)
│   ├── Chapter_4_SSOT.md               (Chapter IV: Master Numerical Registry & Model Results)
│   └── Chapter_5_SSOT.md               (Chapter V: Synthesis, H1 Proofs, Gated Inference)
│
├── manuscripts/                        <-- Production manuscript deliverables & figures
│   ├── chp1-intro.md                   (Chapter I: Introduction & Scope)
│   ├── chp2-litreview.md               (Chapter II: Literature Review)
│   ├── chp3-methodology.md             (Chapter III: Methodology)
│   ├── chp4-results.md                 (Chapter IV: Empirical Findings & Results)
│   ├── chp5-discussion.md              (Chapter V: Analysis & Discussion)
│   ├── glossary.md                     (Operational Terminology & Mathematical Glossary)
│   ├── Gleich_700B_Proposal.docx       (Graduate Thesis Proposal Document)
│   ├── Master_References_APA7.docx     (Master APA 7th Edition Reference Suite)
│   ├── archive/                        <-- Archived Precursor & Superseded Drafts
│   │   ├── Chapter_4_Results_Empirical_Findings.docx (Pre-restructure Word draft)
│   │   └── Master_Results_and_Discussion_Comprehensive_Draft.md (Precursor combined draft)
│   └── figures/                        <-- Publication Figures for Chapter IV
│
├── [results/manuscript_tables/]        <-- Conformed CSV Suite for All 16 Manuscript Tables
│   └── (Sync with: python src/analysis/sync_manuscript_tables.py or run_pipeline.py)
│       ├── 01_annual_seasonality_tsa_otp_clustering.png
│       ├── 01_annual_volatility_tsa_otp_clustering.png
│       ├── 02_day_of_week_dynamics.png
│       ├── 02_day_of_week_volatility_dynamics.png
│       ├── 03_diurnal_hourly_clusters_by_dow.png
│       ├── 03_diurnal_hourly_volatility_clusters_by_dow.png
│       └── 04_sample_sufficiency_distribution.png
│
├── recommendations/                    <-- Actionable guides & technical implementation plans
│   ├── chapter_updates/                <-- Turn-key chapter update guides & defense Q&A
│   │   ├── 00_README_AND_ROADMAP.md    (Master update execution checklist)
│   │   ├── 01_CHAPTER_3_METHODOLOGY_GUIDE.md
│   │   ├── 02_CHAPTER_4_RESULTS_TEXT_AND_TABLES.md
│   │   ├── 03_CHAPTER_5_DISCUSSION_AND_ANALYSIS_GUIDE.md
│   │   └── 04_DEFENSE_TALKING_POINTS_AND_COMMITTEE_QA.md
│   └── implementation_plans/           <-- Master implementation blueprints & roadmaps
│       ├── recs-to-implement.md        (Master Blueprint for Future Execution)
│       ├── OTP_FACTOR_WEIGHTING_AND_TSA_VOLATILITY_RECOMMENDATIONS_AND_IMPLEMENTATION_PLAN.md
│       ├── EXECUTION_PLAN_NOTES_AND_RECOMMENDATIONS_UPDATES.md
│       ├── Updated_Thesis_Project_and_Structure_Recommendation.md
│       └── Recommendations_Results_and_Discussion.md
│
└── notes/                              <-- Research notes, working memos & audit trail
    ├── methodology_memos/              <-- Methodological justifications & technical specs
    │   ├── candidate_b_deep_dive_justification.md
    │   ├── Top25_Clustering_and_4Tier_Filtering_Guide.md
    │   ├── tsa_otp_regime_analysis_report.md
    │   ├── DATA_CLEANING_MODELING_AND_METRICS_FRAMEWORK.txt
    │   ├── Chapter_4_Chapter_5_Outline_Roadmap.md
    │   └── section_documents/          (Working section drafts & criteria)
    │       ├── Assumptions Summary.pdf
    │       ├── Methodological_Assumptions_Data_Selection_and_Criteria.md
    │       ├── Non_Tenant_Carrier_Exclusivity_and_Overtraining_Validation.md
    │       ├── Training_Demarcation_and_Model_Evaluation_Methodology.md
    │       ├── airport-criteria-selection.md
    │       └── methodology-with-4tier.md
    ├── empirical_walkthroughs/         <-- Descriptive statistics & verification walkthroughs
    │   ├── Project_Findings_Master_Walkthrough.md
    │   ├── Data_Quality_and_Referential_Integrity_Walkthrough.md
    │   ├── Methodology_with_4Tier_Filtering.md
    │   ├── Approach1_Results_and_Analysis_Summary.txt
    │   ├── Findings_Outline_Master_Overview.txt
    │   ├── Section_1_Intro_and_Post_ETL_Descriptive_Statistics.txt
    │   ├── Section_2_Spatial_and_Temporal_Filtering_Pipeline.txt
    │   ├── Section_3_Filtered_Dataset_Descriptive_Statistics.txt
    │   ├── Section_4_Hypothesis_Aligned_Representative_Model_Selection.txt
    │   └── Section_5_Empirical_Model_Execution_and_Output_Descriptive_Statistics.txt
    └── provenance_and_standards/       <-- Decision logs, style guides & audit specs
        ├── VERSION_CONTROL_AND_PROVENANCE.md
        ├── PROMPT_AND_DECISION_LOG_2026-09-27.md
        └── Jargon_and_Buzzword_Replacement_Guide.md
```

---

## Key Methodological Foundations

1. **Top 25 Operational Clustering**: Operational metrics across the Top 25 U.S. airports were analyzed using Principal Component Analysis (PCA) and K-Means/Ward's clustering, establishing four operational archetypes (Mega-Connecting Gateways, High-Density O&D Focus, High-Reliability Fortress Hubs, Congested Coastal Originators).
2. **Four-Tiered Purposive Filtering Pipeline**: Candidate airports were filtered through Macro scale ($\rho \to 1.0$), Meso Southwest Airlines exclusion (bimodal arrival kernel), Micro checkpoint exclusivity ($P(\text{Carrier}=j^* \mid \text{Checkpoint } k) = 1.0$), and Orthogonal $3 \times 3$ Factorial Grid balance yielding the 9-Airport Experimental Cohort (AA: DFW, PHL, ORD; DL: DTW, LGA, BOS; UA: EWR, IAH, LAX).
3. **Coupled Volatility & Temporal Regimes**: Grounded in the Within-Day TSA Coefficient of Variation ($CV_{\text{TSA}}$), Flight Departure Delay Dispersion ($\sigma_{\text{Delay}}$), Coupled Volatility Index ($\text{CVI} = CV_{\text{TSA}} \times \sigma_{\text{Delay}}$), and Diurnal Operational Turbulence Shock Index ($T(h)$), identifying non-consecutive dual peaks and establishing the 84-cell interaction tensor ($\mathcal{S} \times \mathcal{D} \times \mathcal{H}$).
4. **Out-of-Time 2025 Holdout Evaluation**: All models were trained on Candidate B data (May 2022 – Dec 2024; 23,400 system hours / 195,570 development observations), tuned on 2024 validation data, and benchmarked against the full 12-month 2025 out-of-time holdout dataset (72,053 hourly complex observations / 8,760 system hours across the 9-airport cohort).
5. **Regime-Switched Gated Inference Engine**: Dynamic routing framework directing low-volatility operations ($\text{Turbulence Shock Index } T(h) < 0.75$) to the Supervised Machine Learning Model (Model 2, $\text{MASE} \le 0.70$) and high-volatility operations ($T(h) \ge 0.75$) to the Dynamic Two-Stage Hybrid Model (Model 3, $R_{\text{MASE}} = 1.05, \text{TTR} = 2.8\text{h}$).
