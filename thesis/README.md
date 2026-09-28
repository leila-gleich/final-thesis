# Thesis Manuscripts, Outlines & Recommendations Directory

Welcome to the `thesis/` directory of the repository. This folder contains all formal thesis manuscript files, graduate proposal documents, master APA 7 references, outline roadmaps, and academic/operational recommendations.

---

## Directory Sitemap & File Index

```
thesis/
├── README.md                           <-- Master thesis directory guide (this file)
│
├── manuscripts/                        <-- Production manuscript chapters (Markdown .md & Word .docx)
│   ├── Chapter_1_Introduction.docx     (Chapter I: Introduction & Scope)
│   ├── Chapter_2_Literature_Review.docx (Chapter II: Literature Review)
│   ├── Chapter_3_Methodology.md        (Chapter III: Methodology - Markdown with Coupled Volatility)
│   ├── Chapter_3_Methodology.docx      (Chapter III: Methodology - Word)
│   ├── Chapter_4_Results_Empirical_Findings.md (Chapter IV: Empirical Results - Markdown)
│   ├── Chapter_4_Results_Empirical_Findings.docx (Chapter IV: Empirical Results - Word)
│   ├── Chapter_5_Analysis_and_Discussion.md (Chapter V: Analysis & Discussion - Markdown)
│   ├── Gleich_700B_Proposal.docx       (Graduate Thesis Proposal Document)
│   ├── Master_References_APA7.docx     (Master APA 7th Edition Reference Suite)
│   └── figures/                        <-- Publication Figures for Chapter IV
│       ├── 01_annual_volatility_tsa_otp_clustering.png
│       ├── 02_day_of_week_volatility_dynamics.png
│       ├── 03_diurnal_hourly_volatility_clusters_by_dow.png
│       └── 04_sample_sufficiency_distribution.png
│
├── thesis_update_recommendations/      <-- Turn-key Chapter Update Guides & Roadmap
│   ├── 00_README_AND_ROADMAP.md        (Master update execution checklist)
│   ├── 01_CHAPTER_3_METHODOLOGY_GUIDE.md
│   ├── 02_CHAPTER_4_RESULTS_TEXT_AND_TABLES.md
│   ├── 03_CHAPTER_5_DISCUSSION_AND_ANALYSIS_GUIDE.md
│   └── 04_DEFENSE_TALKING_POINTS_AND_COMMITTEE_QA.md
│
└── notes_and_recommendations/          <-- Historical Outlines, Guides & Drafts
    ├── Master_Results_and_Discussion_Comprehensive_Draft.md (Unified Chapter IV & V Master Text)
    ├── Recommendations_Results_and_Discussion.md            (Academic, Operational & Defense Guide)
    ├── Top25_Clustering_and_4Tier_Filtering_Guide.md        (Top 25 PCA/K-Means & 4-Tier Funnel Guide)
    └── Chapter_4_Chapter_5_Outline_Roadmap.md               (Five-Section Structural Roadmap)
```

---

## Key Methodological Foundations

1. **Top 25 Operational Clustering**: Operational metrics across the Top 25 U.S. airports were analyzed using Principal Component Analysis (PCA) and K-Means/Ward's clustering, establishing four operational archetypes (Mega-Connecting Gateways, High-Density O&D Focus, High-Reliability Fortress Hubs, Congested Coastal Originators).
2. **Four-Tiered Purposive Filtering Pipeline**: Candidate airports were filtered through Macro scale ($\rho \to 1.0$), Meso Southwest Airlines exclusion (bimodal arrival kernel), Micro checkpoint exclusivity ($P(\text{Carrier}=j^* \mid \text{Checkpoint } k) = 1.0$), and Orthogonal $3 \times 3$ Factorial Grid balance yielding the 9-Airport Experimental Cohort (AA: DFW, PHL, ORD; DL: DTW, LGA, BOS; UA: EWR, IAH, LAX).
3. **Coupled Volatility & Temporal Regimes**: Grounded in the Within-Day TSA Coefficient of Variation ($CV_{\text{TSA}}$), Flight Departure Delay Dispersion ($\sigma_{\text{Delay}}$), Coupled Volatility Index ($\text{CVI} = CV_{\text{TSA}} \times \sigma_{\text{Delay}}$), and Diurnal Operational Turbulence Shock Index ($T(h)$), identifying non-consecutive dual peaks and establishing the 84-cell interaction tensor ($\mathcal{S} \times \mathcal{D} \times \mathcal{H}$).
4. **Out-of-Time 2025 Holdout Evaluation**: All models were trained on Candidate B data (May 2022 – Dec 2024; 23,400 system hours / 195,570 development observations), tuned on 2024 validation data, and benchmarked against the full 12-month 2025 out-of-time holdout dataset (72,053 hourly complex observations / 8,760 system hours across the 9-airport cohort).
5. **Regime-Switched Gated Inference Engine**: Dynamic routing framework directing low-volatility operations ($\text{CVI} < 30$) to LightGBM ($M_3, \text{MASE} \approx 0.60$) and high-volatility operations ($\text{CVI} \ge 35$) to Two-Stage State-Space Hybrids ($M_5, R_{\text{MASE}} \le 1.28$).
