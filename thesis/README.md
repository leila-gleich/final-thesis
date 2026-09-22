# Thesis Manuscripts, Outlines & Recommendations Directory

Welcome to the `thesis/` directory of the repository. This folder contains all formal thesis manuscript files, graduate proposal documents, master APA 7 references, outline roadmaps, and academic/operational recommendations.

---

## Directory Sitemap & File Index

```
thesis/
├── README.md                           <-- Master thesis directory guide (this file)
│
├── manuscripts/                        <-- Production manuscript chapters (Word .docx & Markdown .md)
│   ├── Chapter_1_Introduction.docx     (Chapter I: Introduction & Scope)
│   ├── Chapter_2_Literature_Review.docx (Chapter II: Literature Review)
│   ├── Chapter_3_Methodology.docx      (Chapter III: Methodology)
│   ├── Chapter_4_Results_Empirical_Findings.md (Chapter IV: Empirical Results - Markdown)
│   ├── Chapter_4_Results_Empirical_Findings.docx (Chapter IV: Empirical Results - Word)
│   ├── Chapter_5_Analysis_and_Discussion.md (Chapter V: Analysis & Discussion - Markdown)
│   ├── Gleich_700B_Proposal.docx       (Graduate Thesis Proposal Document)
│   └── Master_References_APA7.docx     (Master APA 7th Edition Reference Suite)
│
└── notes_and_recommendations/          <-- Outlines, Guides & Recommendations
    ├── Master_Results_and_Discussion_Comprehensive_Draft.md (Unified Chapter IV & V Master Text)
    ├── Recommendations_Results_and_Discussion.md            (Academic, Operational & Defense Guide)
    ├── Top25_Clustering_and_4Tier_Filtering_Guide.md        (Top 25 PCA/K-Means & 4-Tier Funnel Guide)
    └── Chapter_4_Chapter_5_Outline_Roadmap.md               (Five-Section Structural Roadmap)
```

---

## Key Methodological Foundations

1. **Top 25 Operational Clustering**: Operational metrics across the Top 25 U.S. airports were analyzed using Principal Component Analysis (PCA) and K-Means/Ward's clustering, establishing four operational archetypes (Mega-Connecting Gateways, High-Density O&D Focus, High-Reliability Fortress Hubs, Congested Coastal Originators).
2. **Four-Tiered Purposive Filtering Pipeline**: Candidate airports were filtered through Macro scale ($\rho \to 1.0$), Meso Southwest Airlines exclusion (bimodal arrival kernel), Micro checkpoint exclusivity ($P(\text{Carrier}=j^* \mid \text{Checkpoint } k) = 1.0$), and Orthogonal $3 \times 3$ Factorial Grid balance yielding the 9-Airport Experimental Cohort (AA: DFW, PHL, ORD; DL: DTW, LGA, BOS; UA: EWR, IAH, LAX).
3. **Out-of-Time 2025 Holdout Evaluation**: All models were trained on Candidate B data (May 2022 – Dec 2023), tuned on 2024 validation data, and benchmarked against the full 12-month 2025 out-of-time holdout dataset (215,562 hourly observations).
