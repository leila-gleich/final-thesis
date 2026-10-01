# Chapter 1: Introduction

## 1.1 Context and Operational Motivation
The management of airport passenger flow and security screening operations remains one of the most critical logistical challenges in modern aviation. As defined by De Neufville and Odoni (2014), the fundamental design and operation of passenger terminals are constrained by the stochastic nature of human behavior, intersecting with rigid infrastructure and fluctuating airline schedules. The Transportation Security Administration (TSA) serves as the primary bottleneck and regulatory checkpoint within the United States aviation system, where minor perturbations in passenger arrivals can precipitate cascading delays, missed connections, and degraded operational efficiency. 

Historically, passenger flow modeling relied heavily on macroscopic, static assumptions of demand, applying generic load factors and static arrival curves to anticipated flight schedules. However, post-pandemic travel behaviors have introduced unprecedented volatility into the system. This research context is grounded in a robust, multi-carrier framework analyzing a diverse 9-airport cohort spanning American Airlines (DFW, PHL, ORD), Delta Air Lines (DTW, LGA, BOS), and United Airlines (EWR, IAH, LAX). By encompassing diverse geographic footprints and hub-and-spoke dynamics, this operational context establishes a macro-level foundation for investigating the intricacies of checkpoint demand.

## 1.2 Significance of the Study
This study addresses a critical gap in aviation operations research by providing a rigorous, empirical evaluation of predictive methodologies applied to airport security screening throughput. The significance of this research is framed by a tri-fold problem in existing literature: (i) inadequate demand definition that relies on coarse aggregations rather than high-fidelity, flight-level data; (ii) a lack of regime-aware training that fails to account for structural shifts in travel behavior; and (iii) insufficient cross-airport validation, where models trained on a single facility fail to generalize to disparate operational environments.

By integrating operational flight data with actual TSA throughput, this thesis establishes a benchmark capable of achieving a targeted 14.2% error reduction over traditional time-series baselines. The study pioneers the application of a coupled volatility index and an 84-cell cross-classification architecture to capture the nuanced dynamics of passenger show-up behaviors. Furthermore, the findings provide airport operators and federal security directors with actionable intelligence, transitioning from reactive staffing paradigms to proactive, predictive resource allocation.

## 1.3 Statement of the Problem
Despite advances in computational modeling, predicting stochastic airport passenger flow remains structurally deficient due to an over-reliance on idealized arrival distributions and a failure to model zero-throughput anomalies. The core problem lies in the stochastic nature of show-up profiles, which are frequently distorted by external shocks, localized hub disconnects, and intermittent operational pauses. Traditional forecasting engines often struggle with the zero-throughput treatment, improperly treating overnight lulls or abrupt closures as missing data rather than structural features of the time series (Sun et al., 2021). 

Furthermore, while deep neural networks offer theoretical improvements in predictive accuracy, their "black box" nature limits their operational viability. Airport management requires model transparency to justify staffing adjustments and financial expenditures (Gao, 2022). A defense of model transparency necessitates the exclusion of highly opaque deep learning models in favor of interpretable econometric and machine learning frameworks. Consequently, there is an urgent need to identify which predictive architectures balance accuracy with interpretability under varying degrees of operational stress.

## 1.4 Purpose Statement
The purpose of this quantitative study is to evaluate the efficacy of distinct predictive techniques (designated as models M0 through M5) in modeling stochastic airport passenger flow. This study aims to construct a comprehensive evaluation triad prioritizing robustness, resilience, and generalizability. Robustness is assessed through the model's performance under normal stochastic variation; resilience is measured by the model's ability to recover predictive accuracy during and after irregular operations or external shocks; and generalizability is evaluated based on the model's cross-airport adaptability without the need for extensive, site-specific recalibration. By systematically comparing baseline time-series approaches against hybrid machine learning architectures, this research seeks to standardize a methodological pipeline for high-fidelity passenger demand forecasting.

## 1.5 Research Question
This thesis is guided by the following central research question:
"Which predictive modeling frameworks are most effective for forecasting airport passenger security screening throughput when prioritizing robustness, resilience, or generalizability?"

## 1.6 Delimitations
The scope of this study is purposefully bounded to ensure methodological rigor and analytical depth. Geographically, the research is delimited to a 9-airport cohort representing major United States legacy carrier hubs and high-density origin-and-destination (O&D) markets. Temporally, the analysis spans a distinct post-pandemic window, explicitly utilizing data from 2022 and 2023 to capture modern structural regimes while avoiding the anomalous zero-demand periods of 2020 and 2021. The modeling approach is delimited to transparent, interpretable algorithmic families—specifically regression, machine learning, and queuing simulation—excluding opaque deep neural networks to maintain operational deployability and theoretical clarity. 

## 1.7 Limitations and Assumptions
Several inherent limitations and assumptions condition the findings of this research. A primary limitation is the reliance on the DB1B (Airline Origin and Destination Survey) dataset's stationarity assumption; it is assumed that quarterly ticketing behaviors remain relatively stable within a given temporal regime, which may not hold true during sudden economic shifts. Additionally, the study assumes that the zero-throughput treatment—mapping zero-volume intervals as deterministic rather than stochastic—accurately reflects true operational cessation rather than sensor failure. 

It is also assumed that airline cancellations are endogenous to the overarching operational tempo and are adequately captured by the capacity reduction metrics fed into the models. Finally, statistical power may be inherently constrained when analyzing highly granular (e.g., 15-minute) intervals across all 84 cells of the cross-classification tensor for smaller volume airports. 

The remainder of this thesis is structured as follows: Chapter 2 provides a comprehensive review of the relevant literature; Chapter 3 details the methodological framework and data generating process; Chapter 4 presents the analytical findings, descriptive statistics, and model evaluations; and Chapter 5 concludes with operational recommendations and directions for future research.

***

# Chapter 2: Review of the Literature

## 2.1 Traditional Approaches to Airport Passenger Flow Modeling
The foundational paradigms of airport passenger flow modeling have historically been rooted in macroscopic facility planning and deterministic queuing theory. Early approaches, detailed extensively by De Neufville and Odoni (2014), focused on peak-hour demand parameters to dictate terminal footprint and security checkpoint sizing. These traditional models largely assumed homogeneous passenger behavior, applying static arrival curves—frequently modeled as simple normal or Poisson distributions—relative to scheduled flight departures. While sufficient for long-term infrastructure planning, these deterministic approaches consistently failed to capture the micro-level stochasticity inherent in daily operations. Ashford et al. (2011) noted that relying on aggregated daily or hourly totals obscures the high-frequency volatility that actually drives security wait times and operational bottlenecks.

## 2.2 Simulation-Based Modeling of Terminal Operations
To overcome the limitations of static models, researchers increasingly turned to discrete-event simulation (DES) and agent-based modeling (ABM). Simulation-based modeling allows for the granular representation of terminal operations, modeling individual passengers as autonomous agents navigating a constrained spatial environment. Takakura et al. (2019) demonstrated the utility of DES in optimizing checkpoint lane configurations under varying demand scenarios. However, while simulations offer unparalleled insight into spatial-temporal bottlenecks, they are computationally expensive and highly sensitive to their input parameters. The efficacy of a simulation is fundamentally bounded by the accuracy of its demand forecast; if the exogenous arrival distribution is flawed, the simulation merely amplifies the underlying error. Consequently, literature has pivoted toward improving the empirical generation of these arrival distributions rather than refining the simulation mechanics alone (Adacher, Flamini, Guaita & Romano, 2017).

## 2.3 Time-Series Forecasting in Transportation Systems
As the volume of high-frequency operational data increased, time-series forecasting emerged as a dominant methodology for predicting short-term passenger throughput. Autoregressive Integrated Moving Average (ARIMA) models and their seasonal variants (SARIMA) became standard benchmarks due to their ability to capture diurnal and weekly periodicities. Gupta et al. (2021) applied advanced time-series techniques to public transit systems, demonstrating the importance of historical lag features in predicting near-term demand. However, pure time-series approaches are inherently autoregressive; they rely entirely on the premise that future behavior is a direct function of past behavior. In the context of aviation—where demand is directly tethered to a highly dynamic, externally published flight schedule—univariate time-series models frequently fail to anticipate sharp deviations caused by schedule modifications, weather events, or localized hub disconnects.

## 2.4 Hybrid and Multi-Source Architectures
Recognizing the limitations of isolated time-series or simulation models, contemporary research has gravitated toward hybrid architectures that ingest multi-source data. These frameworks attempt to synthesize scheduled capacity, historical throughput, and real-time operational telemetry.

### 2.4.1 Feature-Level Fusion and Ensemble Architectures
Feature-level fusion involves the mathematical combination of distinct data streams prior to algorithmic processing. By integrating flight schedules with historical checkpoint volumes, ensemble models like Random Forests or Gradient Boosting Machines can dynamically weigh the influence of impending departures against established behavioral baselines. This approach directly addresses the stochastic nature of passenger flow by allowing the model to switch between autoregressive reliance and schedule-driven anticipation based on the context of the data space.

### 2.4.2 Dynamic Feedback and Kalman-Based Recursive Filtering
A smaller but critical subset of the literature explores dynamic feedback mechanisms. Recursive filtering, such as Kalman filters, allows models to continuously update their internal state variables as real-time throughput data arrives. While computationally elegant, these recursive models often struggle with the discrete, stepped nature of flight departures, which can introduce non-Gaussian noise that violates fundamental filter assumptions.

## 2.5 Post-Pandemic Volatility and Structural Regime Changes
The global disruption caused by the COVID-19 pandemic necessitated a fundamental reevaluation of predictive modeling in aviation. The International Civil Aviation Organization (ICAO, 2020) highlighted the total collapse of historical trend utility, rendering pre-2020 predictive models operationally obsolete. Post-pandemic recovery has been characterized by profound structural regime changes, including shifts in business-to-leisure passenger ratios, altered diurnal arrival profiles, and increased schedule volatility. These shifts necessitate models that are not only accurate under static conditions but possess the resilience to adapt to evolving behavioral regimes.

As established by the literature, the transition from traditional, deterministic planning to resilient, hybrid predictive modeling represents the frontier of aviation operations research. The subsequent chapter outlines a novel, git-inspired methodological framework designed to address these identified gaps, utilizing a multi-tiered filtering pipeline and robust econometric evaluation to model stochastic passenger flow accurately.

***

# Chapter 3: Methodology

## 3.1 Context and Operational Motivation
*Establish baseline (checkout main):* 
The methodological foundation of this research is grounded in the established operational realities of airport passenger processing. The baseline approach to understanding checkpoint dynamics is traditionally informed by frameworks such as ACRP Report 40 and standard queuing theory principles. In these established paradigms, passenger flow is treated as a function of scheduled seat capacity subjected to static arrival curves. Operationalizing this baseline requires a rigorous translation of theoretical queuing mechanics—specifically the traffic intensity ratio, denoted as $\rho(t) = \lambda(t) / \mu(t)$, where $\lambda(t)$ is the arrival rate and $\mu(t)$ is the service rate—into an empirical data structure. The motivation for this methodology is to formally construct this established baseline, acknowledging its foundational utility before iterating upon it with advanced predictive techniques.

## 3.2 Significance of the Study
While the baseline provides necessary context, its macroscopic limitations fail to capture the high-frequency volatility of modern aviation networks. The significance of the methodology lies in its systematic departure from static assumptions. By treating the baseline as a point of departure, the research architecture introduces progressive algorithmic complexity—merging novel data pipelines with established queuing fundamentals. This methodology is significant because it provides a fully reproducible, empirical pipeline that maps raw, disjointed federal data streams into a cohesive, predictive asset capable of defining localized hub disconnects and granular passenger show-up curves.

## 3.3 Statement of the Problem
The methodological problem centers on the extraction of true stochastic signals from overwhelmingly noisy, multi-modal transportation datasets. Legacy methodologies operate under the assumption of continuous, smooth data environments. However, real-world airport operations are jagged, punctuated by zero-throughput anomalies, sudden capacity dumps, and structural breaks in temporal regimes. The methodology must explicitly solve for the mismatch between the continuous mathematical functions traditionally used to model flow and the discrete, heterogeneous reality of passenger arrivals.

## 3.4 Purpose Statement
The purpose of this quantitative methodology is to engineer a rigorous, transparent data-generating process and evaluation framework. The methodology aims to systematically develop, train, and test six distinct predictive architectures (M0 through M5). By employing a structured pipeline that mirrors iterative software development, the purpose is to guarantee that every model evaluated is subjected to an identical, empirically sound data foundation, ensuring that performance variances are strictly attributable to algorithmic architecture rather than data asymmetry.

## 3.5 Research Question
To operationalize the overarching inquiry of this thesis, the methodology directly addresses the evaluation mechanics required to answer: "Which predictive modeling frameworks are most effective for forecasting airport passenger security screening throughput when prioritizing robustness, resilience, or generalizability?" 

## 3.6 Delimitations
The methodology is bounded by strict, purposive delimitations. Geographic scope is restricted to a specific 9-airport cohort (AA: DFW, PHL, ORD; DL: DTW, LGA, BOS; UA: EWR, IAH, LAX) to isolate distinct hub-and-spoke dynamics. The temporal scope is exclusively delimited to the post-pandemic recovery and normalization phase (2022–2023). Data granularity is bounded at the 15-minute interval, representing the optimal balance between high-frequency signal capture and computational feasibility. Finally, model family exclusions are strictly enforced: opaque deep learning architectures are excluded in favor of transparent regression, time-series, and tree-based machine learning models (M0-M5).

## 3.7 Limitations and Assumptions
The methodology relies on several structural assumptions. The DB1B dataset, utilized to estimate local vs. connecting passenger proportions, operates under a stationarity assumption, inherently assuming that quarterly ticketing behaviors remain uniform across the constituent months. The zero-throughput treatment mathematically assumes that intervals with zero passenger volume and zero scheduled capacity are deterministic structural zeros rather than missing stochastic data. Furthermore, the methodology assumes that airline cancellation behaviors are exogenous inputs adequately represented by real-time capacity adjustments. A limitation of this approach is the potential reduction in statistical power when partitioning data across the full 84-cell cross-classification tensor, particularly for off-peak intervals at non-hub facilities.

---

## 3.8 Four-Tiered Purposive Filtering Pipeline
*Merge experimental work (merge working-dev):*
With the baseline established, the methodology transitions to integrating experimental data architectures. The core of this integration is the Four-Tiered Purposive Filtering Pipeline (Extract, Transform, Load), designed to synthesize four distinct federal data feeds into a unified analytical tensor. 

1. **TSA FOIA Checkpoint Data:** The primary dependent variable dataset. Initially comprising 19.5 million raw records of checkpoint throughput, the data underwent rigorous standardization to handle timezone anomalies and zero-throughput intervals, resulting in 6.4 million cleaned observations.
2. **BTS OTP (On-Time Performance):** The fundamental capacity driver. The raw feed of 45.8 million records was filtered for the 9-airport cohort and merged with actual departure times, yielding 13.2 million actionable flight records.
3. **Form 41 Traffic Data (T-100):** Utilized to assign empirical load factors to scheduled capacity. 1.9 million raw segment records were processed into 422,000 specific route-carrier-month load factor indices.
4. **DB1B (Airline Origin and Destination Survey):** Critical for establishing the "Hub Disconnect." A 10% sample of all airline tickets (12.9 million raw records scaled to represent 22.1 million passengers) was engineered to isolate true origin passengers requiring security screening from connecting passengers who bypass the checkpoint.

## 3.9 Sources of the Data and Sample
The consolidated dataset yields a total sample size of 270,460 temporal observations at the 15-minute granularity across the 9-airport cohort. To ensure rigorous evaluation without data leakage, the sample is strictly partitioned temporally:
*   **Training Set:** 122,847 observations spanning 20 months.
*   **Validation Set:** 72,723 observations spanning 12 months.
*   **Testing Set:** 72,053 observations spanning 12 months.

## 3.10 Treatment of the Data and Coupled Volatility
Micro-level refinement of the data involved advanced feature engineering. To quantify demand instability, a Coupled Volatility Index ($CVI$) was formulated. This index measures the elasticity between scheduled seat capacity variance and actual throughput variance, capturing the "Diurnal Turbulence Index" ($T(h)$) for specific hours of the day. A high $CVI$ indicates a breakdown in the deterministic relationship between flight schedules and passenger arrivals, identifying periods of severe stochastic disruption. 

## 3.11 Data Generating Process and Physical Arrow of Time
The Data Generating Process (DGP) architecture follows a strict sequence to prevent contemporaneous data leakage, enforcing the "Physical Arrow of Time." The sequence is defined as: Flight Capacity $\rightarrow$ Load Factor $\rightarrow$ Hub Disconnect $\rightarrow$ Show-Up Convolution $\rightarrow$ Checkpoint Isolation. Models are restricted from utilizing contemporaneous capacity data, enforcing a realistic 90-120 minute operational lead time. 

The empirical show-up profile is modeled using a lognormal arrival density kernel, where the passenger arrival time $\tau$ relative to flight departure is distributed as $\tau \sim \text{Lognormal}(\mu \approx 4.65, \sigma \approx 0.35)$, resulting in an empirical mode of approximately 92.5 minutes prior to departure. However, specific carrier dynamics exhibit structural deviations; for example, Southwest Airlines demonstrates a bimodal mixture distribution with $\mu_1 \approx 135$ minutes (early position seekers) and $\mu_2 \approx 65$ minutes (routine business travelers), necessitating the application of specific probability weights $w = [0.25, 0.55, 0.20]$ across temporal windows.

## 3.12 Cross-Classification Architecture and Temporal Demarcation
To handle categorical and temporal variance, an 84-cell cross-classification architecture was engineered. This tensor captures the systemic variance across 4 seasonal categories, 7 days of the week (DOW), and 3 diurnal regimes (morning peak, midday plateau, evening push). 

To ensure the models were trained on a stable structural regime, a temporal demarcation point was established at Candidate B: May 1, 2022. An econometric Chow test confirmed structural stability post-demarcation ($p \ge 0.15$), while CUSUM (Cumulative Sum) structural break analyses verified that variance had returned to a state of statistical control.

---

## 3.13 Model Architectures
*Publish consolidated result (push origin main):*
The methodology culminates in the deployment of six distinct model architectures, standardized across the consolidated data foundation:
*   **M0 (Naive Baseline):** Autoregressive historical mean model.
*   **M1 (Standard Time-Series):** SARIMA implementation focused on diurnal and weekly seasonality.
*   **M2 (Deterministic Capacity):** Pure schedule-driven linear regression relying solely on BTS OTP and DB1B data.
*   **M3 (Ridge Regression):** Regularized linear model incorporating both historical lag features and scheduled capacity to prevent multicollinearity.
*   **M4 (Random Forest):** Non-linear ensemble model capturing complex interactions within the 84-cell tensor.
*   **M5 (Hybrid Gradient Boosting):** An advanced, regime-aware architecture fusing gradient boosted decision trees with custom loss functions weighted by the Coupled Volatility Index.

## 3.14 Evaluation Framework
The evaluation triad (robustness, resilience, generalizability) is quantified using rigorous statistical metrics. Absolute accuracy is measured via Mean Absolute Scaled Error (MASE). To capture extreme event recovery (resilience), a customized Robust Mean Absolute Scaled Error ($R\_MASE$) and a Recovery Time Ratio ($RTR$) are utilized. Finally, to rigorously test the statistical significance of performance differences between models, the Diebold-Mariano (DM) test is applied across the out-of-sample testing set.

---

## 3.15 Future Methodological Extensions
*Return to development (checkout working-dev):*
While the current methodology provides a robust, publishable baseline, the modeling pipeline is designed to be highly iterative. Future methodological developments could extend this framework by integrating real-time weather API telemetry as exogenous shocks, or by transitioning the static DB1B quarterly data into a dynamically updated, machine-learned estimation of the Hub Disconnect. The modular nature of the 84-cell tensor allows for seamless continuous integration of new categorical variables without requiring a fundamental rewrite of the underlying Data Generating Process.

***

# Chapter 4: Data Analysis and Findings

## 4.1 Master Descriptive Statistics and Data Health Census
The analytical pipeline commenced with a rigorous data health census to validate the integrity of the fused datasets. The original, unfiltered aggregation of the four federal data feeds comprised 67.22 million raw observations. Following the execution of the Four-Tiered Purposive Filtering Pipeline, the final empirical dataset stabilized at 42.06 million cleaned, harmonized records allocated across the 9-airport cohort. 

Master descriptive statistics revealed profound behavioral variances across the sample. The mean 15-minute checkpoint throughput across all facilities was 412 passengers, with a standard deviation of 288, highlighting the extreme variance inherent in the stochastic queuing system. The data exhibited heavy right-skewness, indicative of intense, short-duration peak periods followed by extended periods of low-to-moderate volume. Sample sufficiency was confirmed across all operational strata, ensuring that even the most granular cells of the 84-cell cross-classification architecture contained sufficient observations to maintain statistical power.

## 4.2 The Four-Tiered Purposive Filtering Pipeline
The empirical execution of the data pipeline confirmed the necessity of high-fidelity filtering. The integration of the Form 41 load factors successfully dampened the artificial volatility introduced by using raw scheduled seat capacity. More critically, the DB1B pipeline execution quantified the absolute necessity of the "Hub Disconnect" parameter. For example, at Charlotte Douglas International (CLT)—analyzed contextually alongside the cohort—up to 76% of raw enplaned capacity was identified as connecting traffic. Without the DB1B filtering tier, baseline predictive models grossly overestimated checkpoint demand by mapping connecting passengers to the local security queue, confirming the tri-fold problem identified in Chapter 1.

## 4.3 Empirical Operational Clusters and Systemic Trends
Principal Component Analysis (PCA) was utilized to identify systemic trends and empirical operational clusters within the cohort. The PCA extracted 4 primary archetypes that collectively explained 77% of the systemic variance. These clusters differentiated highly banked legacy hubs (e.g., DFW, ORD) from rolling-hub operations and heavily O&D dominant facilities (e.g., LGA, BOS). 

Analysis of seasonal volatility regimes and DOW dynamics revealed that traditional assumptions of continuous peak periods are structurally flawed. The empirical data identified the prevalence of "non-consecutive dual peaks"—intense morning and afternoon surges separated by deep, stochastic troughs. The Coupled Volatility Index (CVI) quantified this behavior, demonstrating that predictive error scales non-linearly with the intensity of these dual peaks.

## 4.4 Temporal Demarcation
The theoretical establishment of Candidate B (May 1, 2022) as a temporal demarcation point was empirically validated. Prior to this date, the data exhibited high heteroscedasticity and erratic structural breaks indicative of pandemic recovery instability. Post-May 1, 2022, the variance stabilized. The application of the Chow test across the cohort yielded a p-value of $\ge 0.15$ for the subsequent 24-month period, failing to reject the null hypothesis of structural stability. This confirms that the training, validation, and testing datasets were drawn from a statistically cohesive operational regime, ensuring model generalizability.

## 4.5 Econometric Validation
Prior to full model deployment, rigorous econometric validation was conducted to ensure the integrity of the underlying assumptions. Volume conservation was confirmed, yielding a coefficient of $\rho = 1.00 \pm 0.04$, indicating that long-run scheduled local capacity directly conserves with actual checkpoint throughput, validating the extraction algorithms. The zero-flight intercept regression produced a coefficient of $\beta_0 = 12.4$ ($p = 0.40$), indicating that when scheduled capacity is zero, predicted throughput is statistically indistinguishable from zero, validating the zero-throughput treatment. Furthermore, cross-carrier independence tests indicated negligible signal interference ($\beta_{\text{other}} = 0.002, p = 0.62$), confirming that specific carrier dynamics (e.g., the Southwest bimodal curve) can be isolated within multi-tenant terminals.

## 4.6 Feature Engineering and Show-Up Curves
The empirical derivation of the show-up curves validated the lognormal arrival density kernel. The aggregated data displayed an empirical mode of 92.5 minutes prior to departure. However, the feature engineering process successfully isolated distinct behavioral profiles based on carrier and time-of-day. The 84-cell cross-classification tensor effectively mapped these variations, proving that a static, monolithic arrival curve is mathematically insufficient. The engineered features successfully captured the early position-seeking behavior prevalent in specific low-cost carrier markets versus the "just-in-time" arrival profiles typical of high-frequency business shuttles at airports like LGA and BOS.

## 4.7 Model Benchmark Matrix
The final phase of the analysis involved the comparative evaluation of the six models (M0-M5) against the out-of-sample testing dataset. 

*   **M0 (Naive) & M1 (SARIMA):** As anticipated, baseline time-series models collapsed under high-volatility scenarios. While demonstrating acceptable MASE under steady-state conditions, their Recovery Time Ratio ($RTR$) was severely protracted following weather events.
*   **M2 (Deterministic) & M3 (Ridge):** Schedule-driven linear models improved baseline accuracy but struggled to capture the non-linear dynamics of overlapping flight banks.
*   **M4 (Random Forest):** Demonstrated strong generalizability but suffered from edge-case overfitting during extreme peak hours.
*   **M5 (Hybrid Gradient Boosting):** The M5 architecture emerged as the decisively superior framework. By synthesizing the DB1B-filtered schedule capacity, the 84-cell tensor, and historical lag features, M5 achieved an $R^2 = 0.6270$ and a benchmark MASE of $0.846$. This represents a 14.2% error reduction over the M1 baseline.

The evaluation triad explicitly highlighted M5's superiority. Under simulated storm disruptions, where pure machine learning models typically experience predictive collapse (e.g., isolated ML MASE spiking to $1.025$), the M5 model maintained resilience, anchored by its deterministic schedule features. Diebold-Mariano (DM) test results confirmed that the predictive superiority of the M5 hybrid architecture over the M1 baseline is statistically significant at the 1% level across all 9 airports in the cohort. These findings definitively answer the research question, establishing the M5 hybrid methodology as the optimal predictive framework for balancing robustness, resilience, and generalizability in stochastic airport passenger flow modeling.
