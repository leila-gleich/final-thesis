# Chapter I: Introduction


As air travel demand outpaces airport infrastructure growth, inefficient resource allocation has become a critical operational bottleneck (Adacher, Flamini, Guaita & Romano, 2017). Barriers such as prohibitive capital costs and municipal land constraints severely restrict physical terminal expansion (AlKheder et al., 2024; Balliauw & Onghena, 2020; De Neufville & Odoni, 2014; Ozores, 2026). Consequently, airport operators and federal security authorities must extract maximum operational throughput from fixed physical assets through software-driven predictive intelligence.


While predictive models are widely deployed to anticipate terminal demand, the systemic disruptions of the COVID-19 pandemic and subsequent recovery exposed critical vulnerabilities in traditional, accuracy-centric evaluation standards (Sun, Wandelt, & Zhang, 2022). These unprecedented operational disruptions demonstrated that conventional accuracy metrics, while necessary, are insufficient as the sole basis for evaluating models intended for volatile airport operating environments. Specifically, the pandemic revealed that a singular evaluation standard is inadequate across highly variable operational contexts, necessitating the assessment of predictive models through a broader, multidimensional set of performance measures. In airport operations, the most useful predictive model is therefore not necessarily the one with the lowest average forecast error but the model that:

- **Robustness (Remains reliable during routine operations)**: Providing consistent, low-error baseline volatility forecasts during undisturbed flight banks.
- **Resilience (Maintains stability and recovers rapidly during disruptions)**: Absorbing severe exogenous shocks (such as winter freeze events or summer convective ground delay programs) without generating false demand collapses or runaway queue backlogs.
- **Generalizability (Transfers effectively across operational contexts)**: Porting its structural logic across divergent airport terminal layouts and airline hub network topologies without requiring extensive, site-specific historical retraining.

This study examines the suitability of predictive modeling frameworks – spanning deterministic operational baselines (such as persistence and scheduled flight bank dispersion), data-driven decision-tree architectures (automated rule-based machine learning models), and sequential two-stage hybrid models (combining schedule baselines with real-time error correction) – for forecasting Transportation Security Administration (TSA) checkpoint throughput volatility across routine, volatile, and disrupted demand regimes.


## Significance of the Study


This research aims to contribute to both theory and practice by shifting the paradigm of how predictive models are evaluated in unpredictable airport operations. While traditional approaches emphasize static accuracy, this study advances the field by establishing a multidimensional, dynamic evaluation framework that assesses models based on their robustness, resilience, and generalizability. By identifying which forecasting techniques remain reliable during operational disruptions and structural breaks, it offers airport operators actionable, data-driven insights for selecting models that sustain TSA throughput, safety, and service rates under fluctuating post-pandemic conditions.


## Statement of the Problem


Airport passenger arrivals and behaviors are inherently stochastic, varying significantly by time of day, flight schedules, and external factors (Cheng, Zhang, & Guo, 2012; Dönmez, Tükenmez, & Cecen, 2025). Existing models for managing airport passenger flow tend to rely on static or pre‑pandemic assumptions, consequentially failing to account for unpredictable post‑pandemic travel patterns (Ebert, Dutta, Mengersen, Mira, Ruggeri, & Wu, 2021; Hopfe, Lee & Yu, 2024). This mismatch between capacity planning and fluctuating passenger demand contributes to bottlenecks at check‑in counters, TSA checkpoints, and boarding gates, ultimately leading to congestion and inefficient resource allocation. While recent global disruptions have proven that historical baselines are insufficient for contemporary airport logistics, the aviation sector currently lacks a dynamic framework for evaluating predictive models beyond standard accuracy metrics. Because modern forecasting can no longer remain predicated on deterministic conditions, the absence of an adaptable evaluation methodology leaves airports at risk of deploying tools that fail to respond to sudden demand shocks or generalize across shifting operational realities.


## Purpose Statement


The primary objective is to evaluate predictive modeling techniques, such as regression, machine learning, and queuing simulation, to optimize airport capacity via technological rather than physical – and more costly – intervention. By analyzing the relationship between flight operations and TSA throughput, this study evaluates various predictive modeling frameworks against the primary criteria of robustness, resilience, and generalizability. Rather than seeking a singular, universally optimal model, this research identifies which frameworks perform best under each distinct metric. Ultimately, this comparative analysis provides management with the strategic flexibility to adopt the most appropriate forecasting approach based on their specific operational priorities.


## Research Questions


Which predictive modeling frameworks – spanning deterministic persistence controls, deterministic schedule dispersion baselines, supervised machine learning tree ensembles, and sequential two-stage hybrids – are most effective for forecasting airport passenger security screening throughput volatility ($\sigma_{\text{TSA}}$ and $CV_{\text{TSA}}$) when prioritizing robustness (routine operational accuracy), resilience (stability under convective weather and delay disruptions), or generalizability (cross-airport portability across terminal layouts) as the primary operational evaluation metric?


The Asymmetric Trade-Off $H_1$ : Across the candidate modeling paradigms evaluated following four-tiered purposive filtering (deterministic flight schedules, supervised machine learning, and dynamic two-stage hybrid), no individual approach will prove superior across all three performance measures (robustness, resilience, and generalizability).

- $H_{1a}$ (Robustness Target: Lowest $RMSE_{\text{routine}}$ and $MASE_{\text{routine}} < 0.700$): Supervised machine learning (Model 2) and two-stage dynamic hybrids (Model 3) will successfully achieve the robustness target ($MASE_{\text{routine}} < 0.700$) under nominal operating conditions by capturing non-linear flight schedule dispersion and lead-lag passenger arrivals, whereas naive persistence (Baseline Control) and deterministic flight schedules (Model 1) will fail this threshold ($MASE \ge 0.94$). Supervised machine learning (Model 2) will deliver the computationally lightweight, Pareto-efficient routine solution with zero online feedback latency.
- $H_{1b}$ (Resilience Target: $RRMSE≈1.00 RMASE≈1.00$, Lowest $MASE_{\text{shock}}$, and $TTR<4.0 hours$): The Dynamic Two-Stage Hybrid (Model 3) will be the sole architecture to satisfy the resilience target due to recursive 1-step error innovation feedback ($e_{t-1}$). Static supervised machine learning (Model 2) will experience severe performance degradation ($R \ge 2.0$) resulting from the Empty Checkpoint Fallacy during flight ground delays, while deterministic baselines (Model 1) will remain blind to downline delay cascades.
- $H_{1c}$ (Generalizability Target: $RTR \approx 1.00$ and $\Delta MASE_{\text{transfer}} \le 10.0\%$): The Deterministic Flight Schedule Model (Model 1) will decisively satisfy the generalizability target ($RTR≈1.00,ΔMASE≤10.0%$) under zero-shot spatial transfer without local retraining because flight schedule convolution is invariant to local terminal geometry. Conversely, the Dynamic Hybrid (Model 3) will decisively fail the generalizability target ($RTR≫1.00,ΔMASE>10.0%$) due to decision tree terminal geometry overfitting.

## Delimitations


This study focuses on U.S. airports and uses post-pandemic TSA throughput and flight performance data from 2019 to 2025. It excludes pre-pandemic and pandemic-period activity except where needed to define the post-pandemic baseline. Dynamic queuing models and simulationbased methods are assessed using standard statistical measures, including pvalue, R2 squared, mean squared error (MSE), root mean squared error (RMSE), and mean absolute percentage error (MAPE). These delimitations are detailed in the appendix.


## Limitations and Assumptions


Due to reliance on public data, confidential variables like staffing and manual queue management fall outside the scope of this analysis. While external factors such as weather, regulatory impacts, or IT outages may not be fully accounted for, the framework assumes that utilized data is consistent and findings from the selected airports are generalizable across similar facilities and circumstances. Additionally, the methodology relies on the ability to apply monthly data on load factor to the prediction of TSA throughput on an hourly and seasonal level. These limitations are detailed in the appendix.
