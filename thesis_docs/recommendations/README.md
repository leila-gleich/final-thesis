# Recommendations Directory Index & Architecture

**Location**: `thesis_docs/recommendations/`  
**Author**: Leila Gleich  
**Institution**: Embry-Riddle Aeronautical University (ERAU)  
**Target Repository**: `final-thesis`  
**Last Updated**: October 11, 2026  

---

## Directory Architecture

```
thesis_docs/recommendations/
├── README.md                           <-- Master Index (This File)
├── standardize-formulas-rec.md         <-- Active proposal: Standardize formulas (T(h), CVI) with literature formulations
├── chapter_updates/                    <-- Active chapter recommendations & defense preparation
│   ├── chp5-joc-telemetry-rec.md       <-- Active proposal: Airside-Landside JOC Telemetry for Chapter 5 Section 5.6
│   └── defense-talking-points-qa.md    <-- Active guide: 22-slide defense deck, talking points & committee Q&A
└── archive/                            <-- Completed guides, historical plans & implemented recommendations
    ├── README.md                       <-- Archive Directory Index
    ├── EXECUTION_PLAN_NOTES_AND_RECOMMENDATIONS_UPDATES.md
    ├── draft-recs/                     <-- Archived preliminary draft notes
    ├── completed_chapter_updates/      <-- Implemented chapter guides (00-03, litreview-rec, finalthesisv1-rec)
    └── completed_implementation_plans/ <-- 100% Implemented technical plans (REC-01 to REC-14, OTP Plan, etc.)
```

---

## 1. Active Recommendations & Guides

The following documents remain active as pending proposals or active defense preparation materials:

| Document | Category / Scope | Key Focus & Description |
| :--- | :--- | :--- |
| **[`standardize-formulas-rec.md`](file:///Users/leilagleich/Library/CloudStorage/OneDrive-Embry-RiddleAeronauticalUniversity/final-thesis/thesis_docs/recommendations/standardize-formulas-rec.md)** | Methodological Proposal | Replaces author-invented mathematical formulas ($T(h)$ and $\text{CVI}$) with standard literature equivalents: 1D $K$-Means clustering ($k=3$), FAA A14 operational thresholds, and econometric Bivariate Volatility Interaction terms ($CV_{\text{TSA}} \times \sigma_{\text{Delay}}$). |
| **[`chp5-joc-telemetry-rec.md`](file:///Users/leilagleich/Library/CloudStorage/OneDrive-Embry-RiddleAeronauticalUniversity/final-thesis/thesis_docs/recommendations/chapter_updates/chp5-joc-telemetry-rec.md)** | Chapter V Proposal | Draft text (Options A & B) for Chapter V, Section 5.6 proposing a synchronized Joint Operations Center (JOC) telemetry link connecting checkpoint volatility to airline Departure Control Systems (DCS). |
| **[`defense-talking-points-qa.md`](file:///Users/leilagleich/Library/CloudStorage/OneDrive-Embry-RiddleAeronauticalUniversity/final-thesis/thesis_docs/recommendations/chapter_updates/defense-talking-points-qa.md)** | Defense Preparation | Master 22-slide presentation structure, high-impact defense talking points, and anticipated committee examination Q&A. |

---

## 2. Completed & Archived Chapter Guides (`archive/completed_chapter_updates/`)

All chapter update guides whose recommendations have been fully drafted and integrated into the active manuscript suite are preserved in [`archive/completed_chapter_updates/`](file:///Users/leilagleich/Library/CloudStorage/OneDrive-Embry-RiddleAeronauticalUniversity/final-thesis/thesis_docs/recommendations/archive/completed_chapter_updates/):

* **[`finalthesisv1-rec.md`](file:///Users/leilagleich/Library/CloudStorage/OneDrive-Embry-RiddleAeronauticalUniversity/final-thesis/thesis_docs/recommendations/archive/completed_chapter_updates/finalthesisv1-rec.md)**: Master Recommendation Report for 14-letter Appendix cross-referencing precision, OMML KaTeX math restoration, and authentic aviation terminology replacement across Chapters I–V (100% implemented in `final-thesis-v1/`).
* **[`litreview-rec.md`](file:///Users/leilagleich/Library/CloudStorage/OneDrive-Embry-RiddleAeronauticalUniversity/final-thesis/thesis_docs/recommendations/archive/completed_chapter_updates/litreview-rec.md)**: 101-citation census and section-by-section literature review synthesis (100% integrated into `chp2-litreview.md`).
* **Chapter Update Guides 00–03**: Historical drafting roadmaps for Chapters 3, 4, and 5 (`00_README_AND_ROADMAP.md`, `01_CHAPTER_3_METHODOLOGY_GUIDE.md`, `02_CHAPTER_4_RESULTS_TEXT_AND_TABLES.md`, `03_CHAPTER_5_DISCUSSION_AND_ANALYSIS_GUIDE.md`).

---

## 3. Completed & Archived Implementation Plans (`archive/completed_implementation_plans/`)

All technical and empirical modeling plans have been **100% implemented, tested, and verified** in the codebase (passing 52/52 tests) and are preserved in [`archive/completed_implementation_plans/`](file:///Users/leilagleich/Library/CloudStorage/OneDrive-Embry-RiddleAeronauticalUniversity/final-thesis/thesis_docs/recommendations/archive/completed_implementation_plans/):

* **[`OTP_FACTOR_WEIGHTING_AND_TSA_VOLATILITY_RECOMMENDATIONS_AND_IMPLEMENTATION_PLAN.md`](file:///Users/leilagleich/Library/CloudStorage/OneDrive-Embry-RiddleAeronauticalUniversity/final-thesis/thesis_docs/recommendations/archive/completed_implementation_plans/OTP_FACTOR_WEIGHTING_AND_TSA_VOLATILITY_RECOMMENDATIONS_AND_IMPLEMENTATION_PLAN.md)**: Master plan for Candidate B demarcation (May 1, 2022), forward arrival kernel convolution ($0.25 L_1 + 0.55 L_2 + 0.20 L_3$) with T-100 load factors, fleet upgauging drift, OTP factor weighting hierarchy, and 2025 out-of-time holdout benchmarks.
* **[`recs-to-implement.md`](file:///Users/leilagleich/Library/CloudStorage/OneDrive-Embry-RiddleAeronauticalUniversity/final-thesis/thesis_docs/recommendations/archive/completed_implementation_plans/recs-to-implement.md)**: Master index tracking REC-01 through REC-14.
* **Modular Technical Plans**: REC-01 through REC-14.
* **Structural Guides**: `Updated_Thesis_Project_and_Structure_Recommendation.md` & `Recommendations_Results_and_Discussion.md`.
