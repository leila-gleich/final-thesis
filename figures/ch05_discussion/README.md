# Chapter V: Discussion & Conclusions Figures & Decision Matrices
## Evaluating Predictive Techniques to Model Stochastic Airport Passenger Flow (MSAA / Gleich 700B)

> **Chapter Purpose**: Three-dimensional operational performance evaluations (Robustness, Resilience, Generalizability), Master Asymmetric Trade-Off Matrix ($H_1$), and dual-track decision frameworks for **Chapter V (*Discussion & Conclusions*)**.

---

### Chapter V Figures & Dimensional Performance Tables

| Figure / Table ID | Visual Graphic (`.png`) | Companion Data (`.csv`) | Manuscript Target Location | Operational Function & Theoretical Rationale |
| :--- | :--- | :--- | :--- | :--- |
| **Figure 5.1** | `figure_5_1_asymmetric_trade_off_triangle.png` | `table_5_4_master_asymmetric_trade_off_matrix.csv` | Directly following Table 5.4 | **The Asymmetric Trade-Off Evaluation Triangle ($H_1$)**: Radar/spider plot synthesizing performance across Robustness, Resilience, and Generalizability, illustrating why no single model is universally best. |
| **Table 5.1** | *Derived from metrics* | `table_5_1_evaluation_dimension_1_routine_operational_accuracy.csv` | Following Section `## Dimension 1: Robustness` | **Evaluation Dimension 1: Routine Operational Accuracy**: Compares candidate models under nominal baseline conditions ($	ext{Delay} < 15$m, 0 cancels). Model 3 achieves lowest RMSE (222.1); Model 2 wins Routine Pareto Efficiency ($	ext{MASE} = 0.680	ext{--}0.700$, zero feedback compute latency). |
| **Table 5.2** | *Derived from metrics* | `table_5_2_evaluation_dimension_2_resilience_and_shock_performance.csv` | Following Section `## Dimension 2: Resilience` | **Evaluation Dimension 2: Resilience Under Disruption**: Compares models during irregular operations (IROPS). Model 3 DECISIVE WINNER ($R_{\text{MASE}} = 1.05, \text{TTR} = 2.8\text{h}$) via live error feedback ($e_{t-1}$), while Model 2 collapses ($R = 2.14$) due to Empty Checkpoint Fallacy. |
| **Table 5.3** | *Derived from metrics* | `table_5_3_evaluation_dimension_3_generalizability_and_cross_airport_transfer.csv` | Following Section `## Dimension 3: Generalizability` | **Evaluation Dimension 3: Generalizability Across Facilities**: Evaluates zero-shot spatial transfer (EWR $\to$ LGA). Model 1 DECISIVE WINNER ($\text{RTR} = 1.04, \Delta\text{MASE} = +4.0\%$), while Model 3 overfits terminal geometry ($\text{RTR} = 1.19$). |
| **Table 5.4** | *Derived from metrics* | `table_5_4_master_asymmetric_trade_off_matrix.csv` | Following Section `## Implications and Recommendations` | **Master Asymmetric Trade-Off Matrix ($H_1$ Synthesis)**: Comprehensive multi-dimensional synthesis establishing the dual-track operational policy. |
| **Policy Guide** | *Derived from metrics* | `dual_track_model_selection_policy.csv` | Concluding Section | **Dual-Track Model Selection Policy**: Prescriptive guidance allocating Model 3 for tactical disruption resilience and Model 1 for master planning and spatial transfer. |
