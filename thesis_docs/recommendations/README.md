# Recommendations Directory Index & Architecture

**Location**: `thesis_docs/recommendations/`  
**Author**: Leila Gleich  
**Institution**: Embry-Riddle Aeronautical University (ERAU)  
**Target Repository**: `final-thesis`  
**Date**: September 30, 2026  

---

## Executive Workflow & Maintenance Protocols

To ensure all 14 technical recommendations are implemented consistently, consult the master workflow guide:
- 📖 **[`EXECUTION_WORKFLOW_AND_MAINTENANCE_GUIDE.md`](file:///Users/leilagleich/Library/CloudStorage/OneDrive-Embry-RiddleAeronauticalUniversity/final-thesis/thesis_docs/recommendations/EXECUTION_WORKFLOW_AND_MAINTENANCE_GUIDE.md)**: Establishes the uniform 5-step implementation loop, status transition lifecycle (`STATUS: NOT IMPLEMENTED` $\to$ `STATUS: IMPLEMENTED` $\to$ `STATUS: VERIFIED`), code standards, and unit testing requirements.

---

### Directory Architecture

```
thesis_docs/recommendations/
├── README.md                                       <-- Master Index (This File)
├── PROPOSED_EDITS_ELIMINATE_ORIGINAL_FORMULAS.md   <-- Active proposal: Eliminate original formulas (T(h), CVI)
├── implementation_plans/                           <-- Active / Pending implementation plans
│   └── OTP_FACTOR_WEIGHTING_AND_TSA_VOLATILITY_RECOMMENDATIONS_AND_IMPLEMENTATION_PLAN.md
├── chapter_updates/                                <-- Active presentation & defense guides
│   └── 04_DEFENSE_TALKING_POINTS_AND_COMMITTEE_QA.md
└── archive/                                        <-- Completed guides, historical plans & implemented recs
    ├── README.md
    ├── EXECUTION_PLAN_NOTES_AND_RECOMMENDATIONS_UPDATES.md
    ├── completed_chapter_updates/                  <-- Completed Chapter 3-5 update guides (00 to 03)
    └── completed_implementation_plans/             <-- 100% Implemented technical plans (REC-01 to REC-14, etc.)
```

---

## 1. Active Implementation Plans & Proposals

* **[`OTP_FACTOR_WEIGHTING_AND_TSA_VOLATILITY_RECOMMENDATIONS_AND_IMPLEMENTATION_PLAN.md`](file:///Users/leilagleich/Library/CloudStorage/OneDrive-Embry-RiddleAeronauticalUniversity/final-thesis/thesis_docs/recommendations/implementation_plans/OTP_FACTOR_WEIGHTING_AND_TSA_VOLATILITY_RECOMMENDATIONS_AND_IMPLEMENTATION_PLAN.md)**: Master plan for OTP factor weighting, values vs. volatility duality, and live airside-landside JOC telemetry.
* **[`PROPOSED_EDITS_ELIMINATE_ORIGINAL_FORMULAS.md`](file:///Users/leilagleich/Library/CloudStorage/OneDrive-Embry-RiddleAeronauticalUniversity/final-thesis/thesis_docs/recommendations/PROPOSED_EDITS_ELIMINATE_ORIGINAL_FORMULAS.md)**: Proposal to eliminate author-created mathematical formulas ($T(h)$, $\text{CVI}$) in favor of standard literature methods (1D $K$-Means clustering, FAA A14 thresholds, and Bivariate Volatility Interaction terms).

---

## 2. Completed & Archived Implementation Plans (`archive/completed_implementation_plans/`)

All 14 technical modular recommendations (REC-01 to REC-14) have been **100% implemented, verified, and unit-tested** in the codebase (passing 38/38 tests) and are preserved in [`archive/completed_implementation_plans/`](file:///Users/leilagleich/Library/CloudStorage/OneDrive-Embry-RiddleAeronauticalUniversity/final-thesis/thesis_docs/recommendations/archive/completed_implementation_plans/):
* 📖 Master Index: [`recs-to-implement.md`](file:///Users/leilagleich/Library/CloudStorage/OneDrive-Embry-RiddleAeronauticalUniversity/final-thesis/thesis_docs/recommendations/archive/completed_implementation_plans/recs-to-implement.md)
* Modular Plans: REC-01 through REC-14
* Structural Guidance: `Updated_Thesis_Project_and_Structure_Recommendation.md` & `Recommendations_Results_and_Discussion.md`

---

## 3. Manuscript Chapter & Defense Guides (`chapter_updates/`)

| Guide File | Target Chapter / Purpose | Key Focus |
| :--- | :--- | :--- |
| **[`04_DEFENSE_TALKING_POINTS_AND_COMMITTEE_QA.md`](file:///Users/leilagleich/Library/CloudStorage/OneDrive-Embry-RiddleAeronauticalUniversity/final-thesis/thesis_docs/recommendations/chapter_updates/04_DEFENSE_TALKING_POINTS_AND_COMMITTEE_QA.md)** | Defense Deck & Committee Defense | 20–25 slide deck outline, talking points, anticipated committee Q&A. |

> [!NOTE]
> The text, equations, and tables from chapter update guides 00–03 have been fully incorporated into the active manuscripts in [`thesis_docs/manuscripts/`](file:///Users/leilagleich/Library/CloudStorage/OneDrive-Embry-RiddleAeronauticalUniversity/final-thesis/thesis_docs/manuscripts/) and archived in [`thesis_docs/recommendations/archive/completed_chapter_updates/`](file:///Users/leilagleich/Library/CloudStorage/OneDrive-Embry-RiddleAeronauticalUniversity/final-thesis/thesis_docs/recommendations/archive/completed_chapter_updates/).

