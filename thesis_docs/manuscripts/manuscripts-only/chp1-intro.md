# Chapter I

## Introduction

As air travel demand outpaces airport infrastructure growth, inefficient resource allocation has become a critical operational bottleneck (Adacher, Flamini, Guaita & Romano, 2017). While existing predictive models are increasingly used to forecast airport passenger flow management, the systemic shocks of the COVID-19 pandemic underscored limitations within traditional, accuracy-centric performance metrics to handle abrupt demand shocks, structural breaks, and changing operating constraints. These unprecedented operational disruptions demonstrated that conventional accuracy metrics, while necessary, are insufficient as the sole basis for evaluating models intended for volatile airport operating environments. Specifically, the pandemic revealed that a singular evaluation standard is inadequate across highly variable operational contexts, necessitating the assessment of predictive models through a broader, multidimensional set of performance measures. In airport operations, the most useful predictive model is therefore not necessarily the one with the lowest average forecast error but the model that:

- **Remains reliable during routine operations (Robustness)**: Providing consistent, low-error baseline volatility forecasts during undisturbed flight banks.

- **Maintains stability and recovers rapidly during disruptions (Resilience)**: Absorbing severe exogenous shocks (such as winter freeze events or summer convective ground delay programs) without generating false demand collapses or runaway queue backlogs.

- **Transfers effectively across operational contexts (Generalizability)**: Porting its structural logic across divergent airport terminal layouts and airline hub network topologies without requiring extensive, site-specific historical retraining.

This study systematically examines the suitability of predictive modeling frameworks – spanning deterministic operational baselines (such as persistence and scheduled flight bank dispersion), data-driven decision-tree architectures (automated rule-based machine learning models), and sequential two-stage hybrid models (combining schedule baselines with real-time error correction) – for forecasting Transportation Security Administration (TSA) checkpoint throughput volatility across routine, volatile, and disrupted demand regimes.

## Significance of the Study

This research aims to contribute to both theory and practice by shifting the paradigm of how predictive models are evaluated in unpredictable airport operations. While traditional approaches emphasize static accuracy, this study advances the field by establishing a multidimensional, dynamic evaluation framework that assesses models based on their robustness, resilience, and generalizability. By identifying which forecasting techniques remain reliable during operational disruptions and structural breaks, it offers airport operators actionable, data-driven insights for selecting models that sustain TSA throughput, safety, and service rates under fluctuating post-pandemic conditions.

## Statement of the Problem

Airport passenger arrivals and behaviors are inherently stochastic, varying significantly by time of day, flight schedules, and external factors (Cheng, Zhang, & Guo, 2012; Dönmez, Tükenmez, & Cecen, 2025). Existing models for managing airport passenger flow tend to rely on static or pre‑pandemic assumptions, consequentially failing to account for unpredictable post‑pandemic travel patterns (Ebert, Dutta, Mengersen, Mira, Ruggeri, & Wu, 2021; Hopfe, Lee & Yu, 2024). This mismatch between capacity planning and fluctuating passenger demand contributes to bottlenecks at check‑in counters, TSA checkpoints, and boarding gates, ultimately leading to congestion and inefficient resource allocation. While recent global disruptions have proven that historical baselines are insufficient for contemporary airport logistics, the aviation sector currently lacks a dynamic framework for evaluating predictive models beyond standard accuracy metrics. Because modern forecasting can no longer remain predicated on deterministic conditions, the absence of an adaptable evaluation methodology leaves airports at risk of deploying tools that fail to respond to sudden demand shocks or generalize across shifting operational realities.

## Purpose Statement

The primary objective is to evaluate predictive modeling techniques, such as regression, machine learning, and queuing simulation, to optimize airport capacity via technological rather than physical – and more costly – intervention. By analyzing the relationship between flight operations and TSA throughput, this study evaluates various predictive modeling frameworks against the primary criteria of robustness, resilience, and generalizability. Rather than seeking a singular, universally optimal model, this research identifies which frameworks perform best under each distinct metric. Ultimately, this comparative analysis provides management with the strategic flexibility to adopt the most appropriate forecasting approach based on their specific operational priorities.

## Research Questions

Which predictive modeling frameworks – spanning deterministic persistence controls, deterministic schedule dispersion baselines, supervised machine learning tree ensembles, and sequential two-stage hybrids – are most effective for forecasting airport passenger security screening throughput volatility ($\sigma _{TSA}$ and $CV_{TSA}$) when prioritizing **robustness** (routine operational accuracy), **resilience** (stability under convective weather and delay disruptions), or **generalizability** (cross-airport portability across terminal layouts) as the primary operational evaluation metric?

**Master Asymmetric Trade-Off Hypothesis **$H_{1}$ : Across the candidate modeling paradigms evaluated following four-tiered purposive filtering (deterministic flight schedules, supervised machine learning, and dynamic two-stage hybrid), no individual approach will prove superior across all three performance measures (robustness, resilience, and generalizability).

## Delimitations

This study focuses on U.S. airports and uses post-pandemic TSA throughput and flight performance data from 2019 to 2025. It excludes pre-pandemic and pandemic-period activity except where needed to define the post-pandemic baseline. Dynamic queuing models and simulationbased methods are assessed using standard statistical measures, including pvalue, R2 squared, mean squared error (MSE), root mean squared error (RMSE), and mean absolute percentage error (MAPE). These delimitations are detailed in the appendix.

- **Geographic Scope**: This study evaluates commercial air traffic and security screening operations within the contiguous United States, focusing on the Top 25 commercial airfields categorized under FAA hub classifications, capturing 67.2% of nationwide domestic flight departures.

- **Temporal Scope**: The longitudinal dataset spans January 1, 2019 through December 31, 2025 ($N=22,491$ airport-days; 42.06 million conformed fact records). Model training and evaluation are focused on the verified post-pandemic operational regime starting May 1, 2022 (following the nationwide rescission of federal transportation mask mandates), reserving the full 12-month calendar year of 2025 (3,222 airport-days) as a strict out-of-time holdout evaluation window.

- **Data Sources**: Analysis is delimited to publicly accessible and FOIA-disclosed federal aviation datasets, including TSA Freedom of Information Act (FOIA) hourly screening logs per physical lane, Bureau of Transportation Statistics (BTS) On-Time Flight Performance records (Form 234; capturing flight-level departure delays and cancellations), BTS Schedule T-100 Segment traffic (reporting monthly aircraft seating capacity and load factors), and BTS DB1B/DB1C 10% ticket coupon surveys (identifying local originating vs. airside connecting passenger proportions).

- **Evaluation Standards**: Model performance is measured using rigorous operational forecasting metrics: Root Mean Squared Error (RMSE; capturing overall forecast spread while penalizing peak-hour misses), Mean Absolute Scaled Error (MASE; scaling errors against a simple persistence baseline where values below 1.0 indicate superior skill), the Disruption Error Multiplier ($R_{MASE}$; measuring whether forecast errors grow or remain stable during severe storm disruptions), and the Relative Transfer Ratio (RTR; assessing the accuracy penalty when deploying a model to a new airport without retraining).

## Limitations and Assumptions

Due to reliance on public data, confidential variables like staffing and manual queue management fall outside the scope of this analysis. While external factors such as weather, regulatory impacts, or IT outages may not be fully accounted for, the framework assumes that utilized data is consistent and findings from the selected airports are generalizable across similar facilities and circumstances. Additionally, the methodology relies on the ability to apply monthly data on load factor to the prediction of TSA throughput on an hourly and seasonal level. These limitations are detailed in the appendix.

- **Staffing and Lane Configuration Opacity**: Due to the proprietary and security-sensitive nature of TSA checkpoint operations, confidential operational variables—such as exact Transportation Security Officer (TSO) shift allocations, active lane counts per 15-minute interval, and manual queue snake reconfigurations—are not publicly available. The methodology controls for this by aggregating lane-level counts into terminal complex throughput totals.

- **Connecting Passenger Surveys**: The proportion of transferring passengers who remain airside is estimated using quarterly BTS DB1B coupon surveys. The framework assumes that connecting ratios remain stable across monthly operating horizons within given carrier-terminal complexes.

- **Operational Exogeneity**: Exogenous severe weather disruptions (convective storm lines, winter blizzards) are captured through departure delay distributions and flight cancellation indicators reported in BTS Form 234.
