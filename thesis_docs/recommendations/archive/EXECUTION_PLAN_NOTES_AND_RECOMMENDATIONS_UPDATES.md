# Antigravity Execution Plan: Notes & Recommendations Harmonization

**Author**: Leila Gleich  
**Institution**: Embry-Riddle Aeronautical University  
**Degree**: Master of Science in Aeronautics / Aviation Data Analytics  
**Date**: September 28, 2026  
**Target Directories**:  
- `Gleich-Thesis/thesis/notes_and_recommendations/`  
- `final-thesis/thesis/notes_and_recommendations/`  

---

## Executive Objective

This execution plan provides unambiguous, turnkey instructions for the Antigravity agent or user to synchronize all files in the `notes_and_recommendations` directory with the conformed empirical results, data scopes, and methodological commitments established on September 28, 2026.

### Core Alignment Pillars:
1. **9-Airport Factorial Design**: 4 Dedicated Checkpoints per Carrier (AA: 4, DL: 4, UA: 4) across 4 Clusters and 4 Terminal Layout Archetypes.
2. **Data Scope Rules**: BTS OTP retains departing flights only from thesis airports (all destinations included); BTS T-100 retains all departing segments from thesis airfields; DB1B provides connecting ratios $(1 - C_i)$.
3. **Temporal Demarcation**: Post-pandemic baseline anchored to May 1, 2022 (grounded via Top 25 network CUSUM / Chow break).
4. **Checkpoint Exclusivity Invariance**: Type I (Hard Air-Gap) vs. Type II (Airside Connected) Kolmogorov-Smirnov test proof ($D = 0.032, p = 0.28$).
5. **Conformed Model Baselines**: M1 is the Rebuilt Deterministic 2-Hr Static Lead schedule ($R^2 = 0.5293, \text{RMSE} = 1265.4, \text{MASE} = 0.942$), serving as a rigorous baseline for M3 ($R^2 = 0.5880$) and M5 ($R^2 = 0.6270$).
6. **Production Results Paths**: Direct references to conformed workbooks in `final-thesis/results/` (`01_top25_clustering.xlsx` to `05_robustness_resilience_generalizability.xlsx`).

---

## Task 1: Update `Top25_Clustering_and_4Tier_Filtering_Guide.md`

### 1.1 Purpose
Replace the outdated prototype table in Section 3.4 (which had DFW as Terminal D and mislabeled cluster names) with the definitive 9-airport balanced factorial matrix, and insert the explicit data scope rules and Type I vs. Type II invariance proofs.

### 1.2 Target Files
- `/Users/leilagleich/Library/CloudStorage/OneDrive-Embry-RiddleAeronauticalUniversity/Gleich-Thesis/thesis/notes_and_recommendations/Top25_Clustering_and_4Tier_Filtering_Guide.md`
- `/Users/leilagleich/Library/CloudStorage/OneDrive-Embry-RiddleAeronauticalUniversity/final-thesis/thesis/notes_and_recommendations/Top25_Clustering_and_4Tier_Filtering_Guide.md`

### 1.3 Exact Modifications

#### Change A: Replace Section 3.4
**Locate Target Section**:
```markdown
### 3.4 The 9-Airport Experimental Cohort ($3 \times 3$ Factorial Grid)

| Carrier | Fortress Hub | Congested Coastal Originator | High-Density O&D / Gateway | Dedicated Terminal Checkpoint |
| :--- | :--- | :--- | :--- | :--- |
| **American Airlines (AA)** | DFW (Terminal D) | PHL (Terminals B/C) | ORD (Terminal 3) | dedicated_exclusive |
| **Delta Air Lines (DL)** | DTW (McNamara) | LGA (Terminal C) | BOS (Terminal A) | dedicated_exclusive |
| **United Airlines (UA)** | EWR (Terminal C) | LAX (Terminal 7) | IAH (Terminal C) | dedicated_exclusive |

#### Justification for Specific Inclusion/Exclusion Decisions:
1. **LGA vs. JFK**: United Airlines permanently vacated JFK in October 2022 (failing Meso temporal continuity), whereas LGA opened Delta's consolidated Terminal C in June 2022, providing unconfounded screening lanes.
2. **PHL vs. SLC**: Salt Lake City funnels all carriers through a single consolidated central screening checkpoint, making carrier isolation impossible. Philadelphia (PHL) provides dedicated American Airlines checkpoints (Terminals B and C).
```

**Replace With**:
```markdown
### 3.4 The 9-Airport Experimental Cohort (Balanced Factorial Matrix)

The purposive filtering pipeline yielded the **9-Airport Master Experimental Cohort** (`{BOS, DFW, DTW, EWR, IAH, LAX, LGA, ORD, PHL}`), structured into an orthogonal factorial design across the three legacy carriers, four operational clusters, and four physical terminal architectures:

| Airport Code | City / Metro Area | Top 25 Rank & Volume (Post-Apr 2022) | Tenant Carrier Flights (OTP Post-Apr 2022) | Dedicated Carrier Checkpoint(s) | Terminal Physical Architecture | Empirical Cluster Assignment |
| :---: | :--- | :--- | :--- | :--- | :--- | :--- |
| **LAX** | Los Angeles, CA | **#3 Volume** (425.5k flights; 129.1M pax) | • DL: 98,364<br>• AA: 91,797<br>• UA: 74,368 | • **DL**: Terminal 3 (`T3 - Passenger`, `Delta One`)<br>• **AA**: Terminal 4 (`Terminal 4 - Passenger`, `T4A`)<br>• **UA**: Terminal 7 (`Terminal 7 - Passenger`) | **Decentralized Terminals** *(Archetype 2)* | **Cluster 0**: Mega-Connecting Gateway |
| **ORD** | Chicago, IL | **#2 Volume** (465.8k flights; 63.6M pax) | • UA: 175,750<br>• AA: 136,006 | • **UA**: Terminal 1 (`CKPT 1`, `CKPT 2`, `CKPT 3A`)<br>• **AA**: Terminal 3 (`CKPT 7`, `CKPT 7A`, `CKPT 8`, `CKPT 9`) | **Dual-Hub Mega Pier** *(Archetype 1)* | **Cluster 0**: Mega-Connecting Gateway |
| **DFW** | Dallas/Fort Worth, TX | **#4 Volume** (379.1k flights; 90.5M pax) | • AA: 246,772 | • **AA**: Terminals A, B, C (`A12/A21`, `C10/C21`, `B9/B30`) | **Multi-Terminal Monoculture Ring** *(Archetype 4)* | **Cluster 0**: Mega-Connecting Gateway |
| **DTW** | Detroit, MI | **#17 Volume** (250.1k flights; 46.2M pax) | • DL: 140,020 | • **DL**: McNamara Terminal (`Red 1`, `Red 2`, `Red 3`, `Red 5/6`) | **Linear Mega-Terminal** *(Archetype 3)* | **Cluster 2**: High-Reliability Fortress Hub |
| **PHL** | Philadelphia, PA | **#22 Volume** (209.8k flights; 40.4M pax) | • AA: 100,968 | • **AA**: Terminals B & C (`Checkpoint B`, `Checkpoint C`) | **Multi-Concourse Finger Pier** *(Archetype 1)* | **Cluster 2**: High-Reliability Fortress Hub |
| **BOS** | Boston, MA | **#6 Volume** (361.7k flights; 63.7M pax) | • DL: 67,408 | • **DL**: Terminal A (`Checkpoint A1` — 22 dedicated gates) | **Satellite Spoke** *(Archetype 4)* | **Cluster 1**: High-Density O&D Focus |
| **IAH** | Houston, TX | **#14 Volume** (268.0k flights; 66.0M pax) | • UA: 146,392 | • **UA**: Terminals C & E (`30/CN`, `31/CS`, `70/E`) | **Sprawling Multi-Pier Hub** *(Archetype 1 / 4)* | **Cluster 1**: High-Density O&D Focus |
| **EWR** | Newark, NJ | **#13 Volume** (270.8k flights; 87.7M pax) | • UA: 151,302 | • **UA**: Terminal C (`CKPT-C1`) | **Slot-Controlled Coastal Pier** *(Archetype 1)* | **Cluster 3**: Congested Coastal Originator |
| **LGA** | New York, NY | **#10 Volume** (293.8k flights; 53.0M pax) | • DL: 77,176 | • **DL**: Terminal C (`TC-CHK`, `CHK West` — 37 dedicated gates) | **Slot-Controlled Urban Pier** *(Archetype 1)* | **Cluster 3**: Congested Coastal Originator |

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│               BALANCED FACTORIAL DESIGN: CARRIERS × CLUSTERS × ARCHETYPES              │
└────────────────────────────────────────────────────────────────────────────────────────┘

                 AMERICAN AIRLINES         DELTA AIR LINES           UNITED AIRLINES
                 (4 Dedicated Hubs)        (4 Dedicated Hubs)        (4 Dedicated Hubs)
              ┌─────────────────────────┬─────────────────────────┬─────────────────────────┐
  CLUSTER 0   │  • LAX (Terminal 4)     │  • LAX (Terminal 3)     │  • LAX (Terminal 7)     │
 (Mega-Hubs)  │  • ORD (Terminal 3)     │                         │  • ORD (Terminal 1)     │
              │  • DFW (Terminals A/B/C)│                         │                         │
              ├─────────────────────────┼─────────────────────────┼─────────────────────────┤
  CLUSTER 1   │                         │  • BOS (Terminal A)     │  • IAH (Terminals C/E)  │
 (High O&D)   │                         │                         │                         │
              ├─────────────────────────┼─────────────────────────┼─────────────────────────┤
  CLUSTER 2   │  • PHL (Terminals B/C)  │  • DTW (McNamara Red)   │                         │
  (Fortress)  │                         │                         │                         │
              ├─────────────────────────┼─────────────────────────┼─────────────────────────┤
  CLUSTER 3   │                         │  • LGA (Terminal C)     │  • EWR (Terminal C)     │
  (Coastal)   │                         │                         │                         │
              └─────────────────────────┴─────────────────────────┴─────────────────────────┘
```

#### Justification for Specific Facility Pairings:
1. **LGA vs. JFK**: United Airlines permanently vacated JFK in October 2022 (failing Meso temporal continuity), whereas LGA opened Delta's consolidated Terminal C in June 2022, providing unconfounded screening lanes (`TC-CHK`, `CHK West`).
2. **PHL vs. SLC**: Salt Lake City funnels all carriers through a single consolidated central screening checkpoint, making carrier isolation impossible. Philadelphia (PHL) provides dedicated American Airlines checkpoints (Terminals B and C), establishing an East Coast fortress control counterpart to Delta's Midwestern fortress at DTW.

### 3.5 Operational Data Scope Rules
To ensure complete demand capture while strictly avoiding cross-talk:
1. **BTS On-Time Performance (OTP) Scope**: Records are filtered to flights where `ORIGIN` is one of the 9 selected airfields. All destination airports are retained, ensuring full capture of all departing flights that induce landside security queues. Flights originating at non-thesis airports arriving at thesis airports are strictly excluded.
2. **BTS Form 41 T-100 Load Factor Scope**: Retains all carrier-segment records departing from the 9 thesis airfields. Monthly route load factors ($LF_{k,m}$) scale scheduled seat capacity to true passenger volume across all domestic outbound routes.
3. **BTS DB1B Connecting Ratio Scaling**: Scheduled departing seats are deflated by $(1 - C_i)$ to remove airside transfer passengers (50%–76% at hubs) who bypass landside checkpoints.
```

#### Change B: Expand Section 4 with Type I vs. Type II Invariance
**Append to Section 4**:
```markdown
### 4.1 Type I vs. Type II Checkpoint Layout Invariance
A critical operational distinction exists between checkpoint layout topologies:
* **Type I (Hard Physical Air-Gap)**: Checkpoints where screened passengers physically cannot board flights for any other carrier without exiting to landside and re-clearing security (BOS T-A, DTW McNamara, LGA T-C, ORD T1/T3, EWR T-C).
* **Type II (Operational Dedication with Airside Connectors)**: Checkpoints predominantly used by a single carrier, but where post-security airside walkways connect to other terminals (LAX T3/T4/T7, DFW Terminals A/B/C, IAH Terminals C/E, PHL Terminals B/C).

To prove that Type II configurations do not introduce passenger mixture leakage:
* A two-sample **Kolmogorov-Smirnov test** evaluated standardized prediction error distributions between Type I and Type II environments.
* The test revealed no statistically significant divergence ($D = 0.032, p = 0.28$).
* TSA Credential Authentication Technology (CAT) scanners and carrier checked-baggage drop locations act as strict landside sorting mechanisms, confirming that Type II layouts exhibit complete operational invariance to Type I air-gapped environments.
```

---

## Task 2: Update `Chapter_4_Chapter_5_Outline_Roadmap.md`

### 2.1 Purpose
1. Replace legacy individual `.csv` table references with official conformed master Excel workbooks in `results/`.
2. Update Section 4.7 to replace SARIMAX with the Rebuilt Deterministic 2-Hr Static Lead ($t+2$) baseline ($R^2 = 0.5293, \text{MASE} = 0.942$).
3. Update Section 4.2 to specify the balanced $4 \times 4$ factorial design.

### 2.2 Target Files
- `/Users/leilagleich/Library/CloudStorage/OneDrive-Embry-RiddleAeronauticalUniversity/Gleich-Thesis/thesis/notes_and_recommendations/Chapter_4_Chapter_5_Outline_Roadmap.md`
- `/Users/leilagleich/Library/CloudStorage/OneDrive-Embry-RiddleAeronauticalUniversity/final-thesis/thesis/notes_and_recommendations/Chapter_4_Chapter_5_Outline_Roadmap.md`

### 2.3 Exact Modifications

#### Change A: Update Companion Deliverables in Section 4.1, 4.2, 4.5, 4.6, 4.7
- In Section 4.1: Point companion deliverables to `results/01_top25_clustering/01_top25_clustering.xlsx` (Sheets: `Census_Master`, `Descriptive_Stats`).
- In Section 4.2: Point companion deliverables to `results/02_4tier_filtering/02_4tier_filtering.xlsx` and `02_top9_cohort_comprehensive_analysis.xlsx`.
- In Section 4.5: Point companion deliverable to `results/02_4tier_filtering/02_top9_cohort_comprehensive_analysis.xlsx` (Sheet: `Econometric_Tests`).
- In Section 4.6: Point companion deliverable to `results/03_lead_lag_deconvolution/03_lead_lag_deconvolution.xlsx`.
- In Section 4.7: Point companion deliverable to `results/04_model_execution_2025_holdout/04_model_execution_2025_holdout.xlsx` and `results/05_robustness_resilience_generalizability/05_robustness_resilience_generalizability.xlsx`.

#### Change B: Update Section 4.7 Model Benchmark Description
**Replace**:
```markdown
* Performance metrics across Naive (M0), SARIMAX (M1), LightGBM Tweedie (M3), and Sequential SARIMA-Tree Hybrid (M5).
```
**With**:
```markdown
* Performance metrics across Diurnal Naive (M0), Rebuilt Deterministic 2-Hr Static Lead (M1: $R^2 = 0.5293, \text{RMSE} = 1265.4, \text{MASE} = 0.942$), LightGBM Tweedie (M3: $R^2 = 0.5880, \text{RMSE} = 1192.9, \text{MASE} = 0.910$), and Sequential SARIMA-Tree Hybrid (M5: $R^2 = 0.6270, \text{RMSE} = 1135.0, \text{MASE} = 0.846$).
```

---

## Task 3: Update `Recommendations_Results_and_Discussion.md`

### 3.1 Purpose
Align cited benchmark metrics with the finalized full-year 2025 holdout results.

### 3.2 Target Files
- `/Users/leilagleich/Library/CloudStorage/OneDrive-Embry-RiddleAeronauticalUniversity/Gleich-Thesis/thesis/notes_and_recommendations/Recommendations_Results_and_Discussion.md`
- `/Users/leilagleich/Library/CloudStorage/OneDrive-Embry-RiddleAeronauticalUniversity/final-thesis/thesis/notes_and_recommendations/Recommendations_Results_and_Discussion.md`

### 3.3 Exact Modifications

#### Change A: Update Item 5 in Section 2.2
**Replace**:
```markdown
5. **Out-of-Time Benchmark Matrix**: 2025 holdout performance comparing Deterministic Naive ($R^2 = 0.4508$), SARIMAX ($R^2 = 0.4375$), LightGBM Tweedie ($R^2 = 0.5880$), and Sequential SARIMA-Tree Hybrid ($R^2 = 0.6270, \text{MASE} = 0.846$).
```
**With**:
```markdown
5. **Out-of-Time Benchmark Matrix**: 2025 holdout performance comparing Deterministic Naive ($R^2 = 0.4508$), Rebuilt Deterministic 2-Hr Static Lead ($R^2 = 0.5293, \text{MASE} = 0.942$), LightGBM Tweedie ($R^2 = 0.5880, \text{MASE} = 0.910$), and Sequential SARIMA-Tree Hybrid ($R^2 = 0.6270, \text{MASE} = 0.846$).
```

#### Change B: Update Dimension 1 and Dimension 3 in Section 3.1
**Replace Dimension 1 Finding**:
```markdown
* **Finding**: Supervised Machine Learning (LightGBM Tweedie) and Sequential Hybrids achieved $\text{MASE}_{\text{routine}} \sim 0.60\text{--}0.61$ under nominal operational conditions.
```
**With**:
```markdown
* **Finding**: Supervised Machine Learning (M3) and Sequential Hybrids (M5) achieved $\text{MASE}_{\text{routine}} = 0.890$ and $0.834$ under nominal operational conditions, significantly outperforming the Rebuilt Deterministic Baseline (M1: $\text{MASE} = 0.942$; Diebold-Mariano $DM = 74.25$ and $79.12, p < 0.0001$).
```

**Replace Dimension 3 Finding**:
```markdown
* **Finding**: Deep neural networks suffered a +48.2% error surge on zero-shot transfer across terminal layouts. Deterministic baselines (+8.4%) and Two-Stage Hybrids (+11.4%) maintained high transferability ($\text{RTR} \sim 1.10$).
```
**With**:
```markdown
* **Finding**: Deep neural networks suffered a +48.2% error surge on zero-shot transfer across terminal layouts. Rebuilt Deterministic baselines (+4.4%, $\text{RTR} = 1.04$) and Probabilistic ML (+7.9%, $\text{RTR} = 1.08$) maintained high transferability, while state-space filtering achieved near-perfect invariance ($\text{RTR} = 1.00$).
```

---

## Task 4: Update and Mirror `VERSION_CONTROL_AND_PROVENANCE.md`

### 4.1 Purpose
Increment release version from v3.0 to v3.1, log all September 28, 2026 milestones, and ensure both repositories contain this audit ledger.

### 4.2 Target Files
- `/Users/leilagleich/Library/CloudStorage/OneDrive-Embry-RiddleAeronauticalUniversity/final-thesis/thesis/notes_and_recommendations/VERSION_CONTROL_AND_PROVENANCE.md` (Update)
- `/Users/leilagleich/Library/CloudStorage/OneDrive-Embry-RiddleAeronauticalUniversity/Gleich-Thesis/thesis/notes_and_recommendations/VERSION_CONTROL_AND_PROVENANCE.md` (Mirror/Create)

### 4.3 Exact Content to Append in Section 1 (Release History)
```markdown
| v3.1    | 2026-09-28 | Methodological Harmonization & Two-Chapter Finalization:    |
|         |            | - Formalized balanced 4x4 factorial design across 9 hubs.   |
|         |            | - Verified OTP departing flights scope (unrestricted dests).|
|         |            | - Econometrically confirmed Type I vs. Type II layout       |
|         |            |   invariance via Kolmogorov-Smirnov test (D=0.032, p=0.28). |
|         |            | - Rebuilt M1 deterministic static 2-hr lead baseline.       |
|         |            | - Structured formal Chapter IV (Findings) and Chapter V      |
|         |            |   (Analysis & Discussion) manuscript separation.            |
```

---

## Task 5: Mirror Missing Master Drafts to `final-thesis`

### 5.1 Purpose
Synchronize master draft documents that currently exist only in `Gleich-Thesis` into `final-thesis/thesis/notes_and_recommendations/`.

### 5.2 Source and Target Paths
1. `Gleich-Thesis/thesis/notes_and_recommendations/Master_Results_and_Discussion_Comprehensive_Draft.md`  
   $\to$ `final-thesis/thesis/notes_and_recommendations/Master_Results_and_Discussion_Comprehensive_Draft.md`
2. `Gleich-Thesis/thesis/notes_and_recommendations/Jargon_and_Buzzword_Replacement_Guide.md`  
   $\to$ `final-thesis/thesis/notes_and_recommendations/Jargon_and_Buzzword_Replacement_Guide.md`

---

## Task 6: Execution Script & Automated Commands

To execute all mirror and synchronization commands automatically in the Antigravity shell:

```bash
# 1. Mirror master drafts from Gleich-Thesis to final-thesis
cp "/Users/leilagleich/Library/CloudStorage/OneDrive-Embry-RiddleAeronauticalUniversity/Gleich-Thesis/thesis/notes_and_recommendations/Master_Results_and_Discussion_Comprehensive_Draft.md" \
   "/Users/leilagleich/Library/CloudStorage/OneDrive-Embry-RiddleAeronauticalUniversity/final-thesis/thesis/notes_and_recommendations/"

cp "/Users/leilagleich/Library/CloudStorage/OneDrive-Embry-RiddleAeronauticalUniversity/Gleich-Thesis/thesis/notes_and_recommendations/Jargon_and_Buzzword_Replacement_Guide.md" \
   "/Users/leilagleich/Library/CloudStorage/OneDrive-Embry-RiddleAeronauticalUniversity/final-thesis/thesis/notes_and_recommendations/"

# 2. Mirror Version Control & Provenance from final-thesis to Gleich-Thesis
cp "/Users/leilagleich/Library/CloudStorage/OneDrive-Embry-RiddleAeronauticalUniversity/final-thesis/thesis/notes_and_recommendations/VERSION_CONTROL_AND_PROVENANCE.md" \
   "/Users/leilagleich/Library/CloudStorage/OneDrive-Embry-RiddleAeronauticalUniversity/Gleich-Thesis/thesis/notes_and_recommendations/"

# 3. Mirror updated guides once edited
cp "/Users/leilagleich/Library/CloudStorage/OneDrive-Embry-RiddleAeronauticalUniversity/Gleich-Thesis/thesis/notes_and_recommendations/Top25_Clustering_and_4Tier_Filtering_Guide.md" \
   "/Users/leilagleich/Library/CloudStorage/OneDrive-Embry-RiddleAeronauticalUniversity/final-thesis/thesis/notes_and_recommendations/"

cp "/Users/leilagleich/Library/CloudStorage/OneDrive-Embry-RiddleAeronauticalUniversity/Gleich-Thesis/thesis/notes_and_recommendations/Chapter_4_Chapter_5_Outline_Roadmap.md" \
   "/Users/leilagleich/Library/CloudStorage/OneDrive-Embry-RiddleAeronauticalUniversity/final-thesis/thesis/notes_and_recommendations/"

cp "/Users/leilagleich/Library/CloudStorage/OneDrive-Embry-RiddleAeronauticalUniversity/Gleich-Thesis/thesis/notes_and_recommendations/Recommendations_Results_and_Discussion.md" \
   "/Users/leilagleich/Library/CloudStorage/OneDrive-Embry-RiddleAeronauticalUniversity/final-thesis/thesis/notes_and_recommendations/"
```

---

## Verification Checklist

- [ ] All 9 airports (`BOS, DFW, DTW, EWR, IAH, LAX, LGA, ORD, PHL`) are mapped to their correct domestic carrier terminals (DFW Terminals A/B/C).
- [ ] Cluster assignments match across all documents (Cluster 0: DFW, LAX, ORD; Cluster 1: BOS, IAH; Cluster 2: DTW, PHL; Cluster 3: EWR, LGA).
- [ ] Companion deliverables reference `results/01_...` through `results/05_...` Excel workbooks.
- [ ] Baseline model M1 is identified as Rebuilt Deterministic 2-Hr Static Lead ($R^2 = 0.5293, \text{MASE} = 0.942$).
- [ ] Both folders (`Gleich-Thesis/...` and `final-thesis/...`) contain identical, synchronized sets of Markdown documents.
