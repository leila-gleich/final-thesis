# Evaluating Predictive Techniques to Model Stochastic Airport Passenger Flow
**Author:** Leila Gleich
**Degree:** Master of Science in Aeronautics / Aviation Data Analytics
**Institution:** Embry-Riddle Aeronautical University (ERAU)

---

## CHAPTER I: INTRODUCTION

### 1.1 Context and Operational Motivation
As air travel demand consistently outpaces the physical expansion of airport infrastructure, inefficient resource allocation has emerged as a critical operational bottleneck in the modern aviation ecosystem. Within the complex architecture of commercial airports, security screening checkpoints represent one of the most constrained and unpredictable subsystems. Unlike predictable scheduled flight departures, the arrival of passengers at security checkpoints is driven by a stochastic combination of factors including flight schedules, passenger behavioral profiles, localized traffic conditions, and broader macroeconomic travel patterns. 

Historically, airport authorities and the Transportation Security Administration (TSA) have relied heavily on static planning models and historical throughput averages to allocate screening resources. While these methods provide a baseline for long-term capacity planning, they are inherently ill-equipped to handle dynamic, day-of-operations volatility (Adacher et al., 2017). A sudden weather event, a cascading delay across a major carrier network, or an unexpected surge in passenger volume can rapidly overwhelm a static staffing model, leading to severe congestion, missed flights, and degraded passenger experience (De Neufville & Odoni, 2014). Consequently, there is an urgent industry mandate to develop predictive tools that look beyond static planning to capture the stochastic realities of airport passenger flow (Cheng et al., 2012).

### 1.2 Significance of the Study
This study introduces a novel contribution to the field of aviation operations research through a multi-dimensional evaluation framework designed specifically for passenger flow prediction. While previous research has frequently focused on minimizing average forecasting error, this study posits that a singular focus on error reduction is insufficient for operational reality. Instead, this research evaluates predictive models across three distinct operational dimensions: robustness during routine operations, resilience under disruption, and generalizability across diverse airport environments.

For the TSA and airport authorities, this triad of evaluation metrics holds profound practical significance. A model that performs exceptionally well during a typical Tuesday afternoon (robustness) but fails catastrophically during a severe winter storm (resilience) is of limited utility to an operational planner who must manage staffing through the disruption. Similarly, a highly customized model that perfectly predicts flow at a single hub but cannot be transferred to a different airport without extensive retraining (generalizability) represents an inefficient use of analytical resources. By evaluating models across these three dimensions, this study provides actionable guidance for stakeholders seeking to deploy scalable, reliable predictive frameworks.

### 1.3 Statement of the Problem
Despite significant advancements in predictive analytics and machine learning, current approaches to modeling airport passenger flow suffer from three distinct methodological and operational gaps. First, existing models frequently conflate total available departing seats with actual checkpoint demand, failing to account for the "hub disconnect"—the operational reality that a significant portion of passengers at major hub airports are connecting behind the security perimeter and therefore do not utilize the local checkpoint. Relying on aggregate seat capacity systematically overestimates screening demand at hub facilities.

Second, predictive models trained on pooled, long-term historical data often fail to adapt to extreme weather events, localized network disruptions, or structural changes in travel behavior. These models prioritize average performance over adaptability, leading to severe underperformance exactly when accurate predictions are most critical. Third, the literature is dominated by single-airport case studies. While these localized models may demonstrate high accuracy, they do not prove portability or generalizability across different operational environments, leaving a critical gap in our understanding of how to build scalable forecasting systems.

### 1.4 Purpose Statement
The purpose of this study is to evaluate a spectrum of predictive techniques—ranging from traditional time-series regression to advanced machine learning and hybrid queueing models—to optimize checkpoint capacity planning. This research systematically compares a suite of models (designated M0 through M5) across the three critical dimensions of robustness, resilience, and generalizability. By identifying the strengths and weaknesses of each modeling approach under varying operational conditions, this study aims to provide a comprehensive framework that airport operators and security agencies can use to select and deploy the most appropriate predictive tools for their specific operational contexts.

### 1.5 Research Question
This study is guided by the following primary research question: Which predictive modeling frameworks are most effective for forecasting airport passenger security screening throughput when prioritizing robustness, resilience, or generalizability?

### 1.6 Delimitations
This study is deliberately bounded by several specific delimitations to ensure methodological rigor and operational relevance. Geographically, the research focuses exclusively on a curated cohort of nine major United States airports, carefully selected to represent a diverse cross-section of hub and origin-and-destination (O&D) traffic profiles. The temporal window of analysis spans from May 2022 through December 2025, specifically chosen to capture the post-pandemic recovery period where structural changes in travel behavior had largely stabilized, while still encompassing varied seasonal and economic cycles.

The study further restricts its focus to three major legacy carriers: American Airlines (AA), Delta Air Lines (DL), and United Airlines (UA). This decision ensures a consistent baseline for network-driven shock invariance, as these carriers operate with similar hub-and-spoke models and passenger profiles. Finally, to ensure the operational utility of the resulting frameworks, this study imposes an interpretability constraint, explicitly excluding "black-box" Deep Neural Networks (DNNs) in favor of models whose internal mechanics and feature importance can be readily understood and validated by operational stakeholders.

### 1.7 Limitations and Assumptions
Several inherent limitations and assumptions frame the interpretation of this study's findings. Foremost is the reliance on publicly available operational data, which necessitates modeling demand in the absence of proprietary TSA staffing data or precise checkpoint open/close times. The study assumes that observed throughput serves as a reliable proxy for passenger demand, though it acknowledges that observed flow may occasionally be constrained by processing capacity rather than pure arrival rates.

Additionally, the calculation of connecting versus local passenger ratios relies on the Department of Transportation's DB1B dataset, which is published at a quarterly resolution. This requires the assumption that the connecting ratio remains relatively stable within a given quarter, potentially masking high-frequency, day-to-day variations in connecting traffic patterns. Finally, the focus on carrier-exclusive checkpoints—necessary for accurate demand attribution—means the findings may not generalize perfectly to fully consolidated terminals where passengers from diverse airline models (e.g., ultra-low-cost carriers mixed with legacy carriers) share a single screening facility.

---

## CHAPTER II: REVIEW OF THE RELEVANT LITERATURE

### 2.1 Traditional Approaches to Airport Passenger Flow Modeling
The foundational methodologies for modeling airport passenger flow emerged from the broader discipline of transportation engineering and queueing theory. Early models treated the airport terminal as a series of deterministic processing nodes, heavily relying on static arrival curves and average processing times (Ashford et al., 2011). These traditional approaches primarily utilized straightforward linear regression techniques, correlating the aggregate number of departing seats scheduled within a given hour to the expected volume of passengers arriving at the security checkpoint.

While these models provided a necessary baseline for early capacity planning, their limitations quickly became apparent in operational settings. Traditional approaches often assumed a uniform or neatly bounded statistical distribution of passenger arrivals, failing to capture the highly stochastic nature of human behavior (De Neufville & Odoni, 2014). Furthermore, by relying on aggregate seat capacity, these early models ignored the complex underlying network structures of modern airlines, implicitly assuming that all departing passengers originated locally and would pass through the landside security checkpoint. As air travel volume grew and airline operations became more complex, the inability of these static models to account for dynamic variance rendered them insufficient for tactical, day-of-operations management.

### 2.2 Simulation-Based Modeling of Terminal Operations
Recognizing the limitations of static mathematical models, researchers and practitioners turned to discrete-event simulation (DES) to capture the complex, interactive dynamics of passenger flow. Simulation modeling allowed for the representation of individual passenger entities navigating through the terminal, accounting for variable processing times, queuing behaviors, and the spatial constraints of the physical infrastructure (Takakura et al., 2019). Tools like Arena and specialized airport simulation software enabled planners to visualize chokepoints and test the impact of different staffing configurations in a virtual environment.

However, the transition to simulation brought its own set of challenges. Developing a high-fidelity DES model is an extremely data-intensive and time-consuming process, requiring detailed empirical studies to calibrate processing distributions and transition probabilities accurately (Gupta et al., 2021). More importantly, simulations are inherently descriptive rather than predictive in a real-time operational sense. They excel at answering "what-if" questions based on assumed input distributions, but they do not automatically adjust to shifting real-world data feeds, limiting their utility for dynamic, short-term forecasting during rapidly evolving operational disruptions.

### 2.3 Time-Series Forecasting in Transportation Systems
To bridge the gap between static planning and dynamic forecasting, the literature increasingly focused on advanced time-series analysis. Autoregressive Integrated Moving Average (ARIMA) models and their seasonal variants (SARIMA) became the standard for forecasting transportation demand, leveraging historical passenger volume data to identify underlying trends, seasonal patterns, and cyclical variations (ICAO, 2020). These models excelled at capturing the strong temporal regularities inherent in air travel, such as the predictable morning peaks and distinct day-of-week demand profiles.

Despite their strength in identifying historical patterns, traditional time-series models often struggled with the non-stationary nature of aviation operations. They are fundamentally backward-looking, assuming that future patterns will mirror past behavior (Sun et al., 2021). Consequently, when confronted with sudden external shocks—such as severe weather events or sudden schedule alterations—these models frequently exhibited significant predictive lag, failing to adjust quickly enough to provide actionable intelligence to operational managers (Kim & Lee, 2023).

### 2.4 Hybrid and Multi-Source Architectures
The recognition that no single modeling paradigm could adequately capture the full complexity of passenger flow led to the development of hybrid and multi-source architectures. These advanced frameworks seek to combine the temporal pattern recognition of time-series analysis with the dynamic responsiveness of machine learning and the structural insights of queueing theory.

#### 2.4.1 Feature-Level Fusion and Ensemble Architectures
One prominent approach in recent literature is feature-level data fusion, which integrates diverse datasets—such as flight schedules, weather forecasts, and historical throughput—into unified predictive models. Ensemble machine learning techniques, particularly Random Forests and Gradient Boosting Machines (GBMs), have proven highly effective in this domain. By combining multiple weak learners into a single robust model, ensemble architectures can capture complex, non-linear relationships between flight schedules and passenger arrivals without explicitly defining mathematical formulas for those interactions (Gao et al., 2022). These models have demonstrated superior accuracy in predicting short-term flow, though they often trade interpretability for predictive power.

#### 2.4.2 Dynamic Feedback and Kalman-Based Recursive Filtering
Another significant advancement is the incorporation of dynamic feedback mechanisms, primarily through the use of recursive filtering techniques like the Kalman filter. These approaches treat passenger flow as a dynamic state space system, continuously updating predictions in real-time as new observational data (e.g., current queue lengths) becomes available (Schultz & Reitmann, 2019). By mathematically blending historical forecasts with real-time operational feedback, recursive models offer enhanced resilience, adapting rapidly to localized disruptions that feature-level fusion models might miss.

### 2.5 Post-Pandemic Volatility and Structural Regime Changes
The most recent and critical shift in the literature addresses the profound structural changes induced by the global COVID-19 pandemic. The traditional assumptions regarding passenger behavior, show-up profiles, and seasonal trends were severely disrupted, revealing the fragility of models trained exclusively on long-term historical averages (Yoo & Kang, 2023). The post-pandemic era has been characterized by increased operational volatility, shifting booking windows, and altered passenger arrival distributions.

This structural regime change has necessitated a reevaluation of how predictive models are trained and validated. The literature increasingly emphasizes the need for models that can dynamically identify and adapt to shifting operational states, rather than relying on assumed long-term stationarity. Given these converging challenges—the inadequacy of static models, the limitations of uncalibrated simulations, and the necessity of managing post-pandemic volatility—there is a clear imperative to develop a comprehensive methodological framework capable of integrating these disparate approaches. Chapter III details the methodological architecture specifically designed to address these gaps and provide a robust, scalable solution for modern airport operations.

---

## CHAPTER III: METHODOLOGY

### 3.1 Context and Operational Motivation
The central methodological challenge of this study is constructing a reliable analytical bridge between airside flight operations—which are highly structured, scheduled, and closely monitored—and landside passenger screening demand, which is inherently stochastic and decentralized. To accomplish this, this research implements a Data Generating Process (DGP) architecture. In practical terms, this architecture functions as a comprehensive digital pipeline that ingests raw, disparate data streams, standardizes them, and transforms them into a structured format suitable for advanced predictive modeling. This approach ensures that the resulting models are grounded in a mathematically rigorous interpretation of physical operational realities.

### 3.2 Significance of the Study
The methodological significance of this research lies in its robust data integration strategy and its novel four-tiered filtering mechanism. By systematically synthesizing data from the Transportation Security Administration (TSA), the Bureau of Transportation Statistics (BTS), and complex airline network datasets (DB1B), this study creates a uniquely comprehensive view of airport operations. The multi-tiered filtering process ensures that the models are trained on high-fidelity, operationally relevant data, successfully isolating the true underlying demand signals from the noisy interference inherent in raw, uncalibrated aviation datasets.

### 3.3 Statement of the Problem
Methodologically, previous research has struggled to overcome three persistent data and modeling challenges. First, standard datasets do not natively differentiate between local departing passengers and connecting passengers, leading to systemic overestimations of checkpoint demand at major hubs. Second, the temporal disconnect between when a passenger clears security and when their flight departs requires complex lead-lag modeling that traditional regression techniques often oversimplify. Finally, variations in terminal configurations and airline boarding strategies create heterogeneous data environments that frequently confound attempts to create universally applicable models.

### 3.4 Purpose Statement
This chapter details the comprehensive research methodology employed to address these challenges. It outlines the foundational theoretical framework, describes the rigorous four-tiered sample selection and data filtering pipeline, details the integration of multiple data sources, and explains the development of the 84-cell volatility stratification matrix. Furthermore, it defines the suite of predictive models (M0 through M5) and establishes the specific evaluation metrics used to quantify their performance across the dimensions of robustness, resilience, and generalizability.

### 3.5 Research Question
Methodologically, this chapter is designed to answer the following restatement of the primary research question: How can a data generation and modeling pipeline be architected to effectively evaluate the robustness, resilience, and generalizability of various predictive techniques when forecasting stochastic airport passenger screening throughput?

### 3.6 Delimitations
The methodology is delimited to a tightly controlled environment to ensure validity. Geographically, it is restricted to nine specific U.S. airports that successfully passed the four-tiered filtering process. Temporally, the data spans from May 2022 to December 2025 at an hourly resolution. The analysis is limited to flights operated by American, Delta, and United Airlines, and explicitly focuses on carrier-exclusive checkpoints to isolate specific passenger populations. The model suite is delimited to highly interpretable architectures, specifically excluding deep learning neural networks to ensure the resulting models can be understood and trusted by operational stakeholders.

### 3.7 Limitations and Assumptions
The methodology relies on several necessary assumptions. The DB1B dataset, used to calculate connecting passenger ratios, is published quarterly; the study assumes these ratios remain stable across the individual days within that quarter. The methodology also assumes that recorded checkpoint throughput is a valid proxy for passenger demand, effectively assuming that zero-throughput hours represent a genuine lack of demand rather than an unrecorded closure of the checkpoint. Furthermore, the handling of canceled flights assumes a uniform asymmetry in passenger rebooking behaviors, and the statistical power analysis assumes a normal distribution of error terms across the evaluation metrics.

### 3.8 Research Approach and Foundational Framework
*Establishing the Baseline*

The foundational framework of this study is firmly rooted in established queueing theory and the industry-standard arrival curves documented by the Airport Cooperative Research Program (ACRP). At its core, the relationship between flight schedules and passenger arrivals is governed by a fundamental physical reality: passengers must arrive at the security checkpoint significantly before their flight departs. This creates a temporal displacement, or a "lead-lag" dynamic, where the demand signal (the scheduled flight) lags behind the operational stress (the passenger arriving at security). 

To quantify this, the study utilizes a baseline traffic intensity calculation, traditionally expressed mathematically as ρ = λ / (c*μ), where λ represents the passenger arrival rate, c is the number of open screening lanes, and μ is the service rate per lane. While this study does not possess real-time lane staffing data (c), it utilizes this theoretical construct to model the anticipated arrival rate (λ). The concept of the "Physical Arrow of Time" is critical here: a passenger cannot clear security after their flight has departed (barring extreme delays). Therefore, the methodology establishes a standard 90-to-120-minute lead window, assuming that the bulk of the passenger volume for a given flight will process through the checkpoint one to two hours prior to the scheduled departure time, aligning with established ACRP guidelines.

### 3.9 Sample Selection: The Four-Tiered Filtering Pipeline
*Integrating Novel Contributions*

To ensure the integrity of the predictive models, it is essential to train them on high-quality, unambiguous data. Attempting to model every airport in the United States simultaneously would introduce unmanageable variance. Therefore, this study employs a rigorous, narrative-driven "funnel" approach—a four-tiered filtering pipeline—to select a scientifically valid sample cohort from an initial pool of over 450 commercial airports.

The first tier of the filter isolates the Top 25 U.S. airports by passenger volume. This is necessary because these airports represent approximately 67.2% of all domestic traffic; they are the nodes where accurate forecasting is most critical, and they provide sufficient data density for robust statistical modeling. Smaller regional airports often experience highly sporadic traffic that confounds hourly time-series models.

The second tier requires the robust presence of all three major legacy carriers (American, Delta, and United). This ensures "shock invariance." If a model is trained primarily on an airport dominated by a single carrier, a localized disruption to that airline's network will artificially skew the model's performance metrics. Having all three carriers present ensures that systemic patterns can be differentiated from airline-specific anomalies.

The third tier specifically excludes airports dominated by Southwest Airlines. Southwest operates with a unique, open-seating boarding model that fundamentally alters passenger behavior, frequently resulting in bimodal arrival distributions (passengers arriving unusually early to secure better boarding positions). Including this unique operational profile would introduce unacceptable noise into models designed to predict standard legacy carrier behavior.

The fourth and final tier is the most critical: the requirement for carrier-exclusive checkpoints. In many modern consolidated terminals, passengers from multiple airlines funnel through a single, massive security checkpoint. In these environments, it is impossible to accurately map a specific flight delay to a specific surge at the checkpoint, as the data is hopelessly intermingled. By selecting airports where specific airlines operate their own dedicated checkpoints (or terminals), the methodology successfully isolates the demand signal, allowing for precise correlation between the airside flight schedule and the landside passenger arrival rate.

The result of this rigorous filtering pipeline is a highly balanced, scientifically valid cohort of nine airports. This cohort, paired with their respective carrier assignments, provides the pristine data foundation required for advanced predictive modeling.

### 3.10 Data Sources
The comprehensive warehouse constructed for this study integrates four distinct, authoritative datasets. The foundation is the Transportation Security Administration (TSA) Freedom of Information Act (FOIA) release, providing hourly throughput volumes for individual security checkpoints. This is joined with the Bureau of Transportation Statistics (BTS) On-Time Performance (OTP) dataset, which supplies precise scheduled and actual departure times, delay codes, and cancellation metrics for millions of individual flight records.

To understand aircraft capacity, the study incorporates DOT Form 41 traffic data, which details the specific physical seating configurations of the aircraft operating the scheduled routes. Finally, to resolve the hub disconnect, the methodology utilizes the DOT's DB1B dataset, a 10% sample of all airline tickets, which provides the critical origin and destination information necessary to calculate the ratio of local originating passengers versus connecting passengers for every route in the network.

### 3.11 Operational Volatility and Stratification
To evaluate models on their resilience, it is necessary to formally quantify operational volatility. The methodology introduces three distinct metrics. The Coefficient of Variation of TSA Throughput (CV_TSA) measures the standard deviation of hourly passenger flow relative to its mean, identifying periods of high baseline instability. The Capacity Volatility Index (CVI) tracks sudden, short-term fluctuations in scheduled airline capacity due to delays or cancellations. Finally, a synthesized Turbulence Index combines these factors to flag specific operational days as "routine," "disrupted," or "extreme."

To organize this vast operational complexity, the methodology employs an 84-cell stratification architecture. This involves organizing the historical data by season (4 categories), day-of-week (7 categories), and broad time-of-day blocks (3 categories). This 84-cell matrix allows the models to recognize that a Tuesday morning in October behaves fundamentally differently than a Sunday evening in July, providing structural context for the predictive algorithms.

### 3.12 Dataset Partitioning and Training Window
*Consolidating the Framework*

The selection of the training window is critical to the study's validity. The data is partitioned beginning in May 2022 (Candidate B). This specific start date is justified narratively: it aligns with the removal of the federal transportation mask mandate and represents the point at which domestic aviation had largely decoupled from pandemic-era anomalies, stabilizing into a "new normal" of structural regime behavior. 

The dataset is partitioned using a strict chronological split to prevent data leakage. The first 70% of the timeline is designated for model training, establishing the baseline mathematical relationships. The subsequent 15% is utilized as a validation set for hyperparameter tuning and feature selection. The final 15% is held completely separate as a rigorous, out-of-sample test set to definitively evaluate the models' true predictive capabilities on unseen future data.

### 3.13 Model Suite (M0-M5)
The study evaluates six distinct modeling approaches, ranging from simple baselines to advanced hybrid architectures, to determine which best balances robustness, resilience, and generalizability.

*   **M0: Historical Averages (Baseline).** This model simply predicts that tomorrow's passenger volume will match the average volume of the same hour on the same day of the week over the previous month. It represents the simplistic status quo.
*   **M1: Static Seat Capacity Regression.** A traditional linear regression model that predicts throughput based solely on the aggregate number of departing seats scheduled in the upcoming two hours.
*   **M2: Adjusted Capacity Regression.** An enhancement of M1 that applies the DB1B connecting passenger ratios, filtering out the "hub disconnect" to evaluate only the seats likely filled by local, checkpoint-using passengers.
*   **M3: Seasonal Auto-Regressive Integrated Moving Average (SARIMA).** A pure time-series approach that analyzes historical passenger flow to identify cyclical patterns and trends, largely ignoring the underlying flight schedules.
*   **M4: Gradient Boosting Machine (GBM).** A robust machine learning ensemble that ingests all available features (schedules, weather, historical flow, connecting ratios) and builds complex decision trees to map non-linear relationships.
*   **M5: Hybrid Dynamic Recursive Filter.** The most advanced model, which pairs the predictive power of the GBM with a dynamic Kalman-style filter. This model continuously compares its predictions against actual observed throughput in real-time, mathematically correcting itself to adapt rapidly to sudden disruptions.

### 3.14 Evaluation Metrics
To move beyond simple error measurement, the models are evaluated using a specialized suite of metrics designed to answer specific operational questions. The Mean Absolute Scaled Error (MASE) is the primary metric for robustness; it compares the model's accuracy against a naive baseline, ensuring the model is actually learning rather than just guessing. 

The Resilient MASE (R_MASE) calculates the error exclusively during time periods flagged by the Turbulence Index as highly volatile, answering the critical question: "Does this model survive contact with a disruption?" The Ratio of Transferable Robustness (RTR) measures generalizability by comparing a model's performance on its home training airport versus its performance when deployed unmodified to a different airport in the cohort. Finally, the Diebold-Mariano test provides statistical rigor, confirming whether the performance differences between two models are genuinely significant or merely artifacts of random chance.

### 3.15 Validity and Data Treatment
*Refining for the Future*

The final stage of the methodology addresses data hygiene and validity, ensuring the pipeline remains robust against anomalies. The ETL (Extract, Transform, Load) pipeline employs specific treatments for known data issues. Passenger deflation—instances where recorded throughput is inexplicably low—is managed through localized smoothing algorithms. Overnight closures, where checkpoints record zero throughput despite scheduled flights, are formally masked to prevent the models from learning incorrect relationships. Finally, the complex asymmetry of flight cancellations—where delayed passengers eventually arrive but canceled passengers often rebook for subsequent days—is modeled using a proportional distribution function based on historical rebooking patterns. These careful treatments ensure the methodology remains analytically sound and operationally relevant.

---

## CHAPTER IV: RESULTS AND ANALYSIS

### 4.1 Data Foundation
The execution of the Data Generating Process (DGP) resulted in a massive, high-fidelity analytical warehouse. The compilation of TSA FOIA data, BTS OTP records, and DB1B ticketing information produced an initial dataset containing over 14 million individual hourly checkpoint records and corresponding flight details across the initial pool of 450 commercial airports. 

However, raw data volume does not guarantee analytical quality. A preliminary quality audit revealed significant inconsistencies in the baseline data, particularly regarding the reporting of overnight checkpoint closures and sporadic missing values during irregular operations. This required immediate data treatment protocols, where null values were carefully interpolated using localized historical averages, and definitive checkpoint closures were mathematically masked to prevent the predictive models from interpreting a closed lane as a period of zero passenger demand. This rigorous foundational cleaning ensured that the subsequent modeling phases were built upon a stable and statistically sound empirical base.

### 4.2 Filtering Results
The application of the four-tiered filtering pipeline transformed the massive raw dataset into a highly refined, operationally relevant study cohort. The narrative of this funnel approach highlights the specific challenges of modeling aviation infrastructure.

Starting with the full national dataset, the first tier successfully isolated the Top 25 airports by volume, immediately reducing the scope to the facilities where predictive modeling is most critical for national airspace stability. The second tier, requiring the presence of the three major legacy carriers, eliminated airports overly reliant on single-carrier dynamics, ensuring that the remaining facilities provided a balanced view of broader industry trends.

The third tier, which excluded Southwest Airlines-dominated facilities, was crucial for maintaining behavioral consistency. The unique boarding dynamics of Southwest fundamentally alter the temporal arrival curve of passengers, and attempting to model this alongside traditional legacy carrier behavior would have introduced insurmountable statistical noise. 

The final and most restrictive tier—requiring carrier-exclusive checkpoints—narrowed the field to the final nine airports. This step was paramount; it allowed the methodology to definitively link a specific set of departing flights to a specific, measurable flow of passengers through a single security chokepoint. The final cohort includes highly specific operational environments, such as Delta's dedicated operations at Atlanta Hartsfield-Jackson (ATL) and United's distinct terminals at Newark Liberty (EWR) and Chicago O'Hare (ORD). This tightly controlled sample guarantees that the demand signals observed in the data are genuine reflections of flight schedules rather than artifacts of consolidated terminal routing.

### 4.3 Operational Patterns
Exploratory data analysis of the refined nine-airport cohort revealed several profound operational patterns that validate the study's underlying hypotheses. Most notably, the data provided empirical confirmation of the "Hub Disconnect." 

When analyzing raw seat capacity against checkpoint throughput at major hub locations like ATL and ORD, the traditional static models drastically overestimated passenger arrivals. The analysis revealed that during peak hubbing banks—periods where dozens of flights arrive and depart in rapid succession to facilitate passenger transfers—the actual volume of passengers arriving at the landside security checkpoint remained relatively flat. The majority of the required capacity was transferring airside. Conversely, at strong Origin & Destination (O&D) airports like Los Angeles International (LAX) and Boston Logan (BOS), the correlation between departing seats and checkpoint throughput was significantly tighter.

Furthermore, the implementation of the CVI and Turbulence Index successfully segmented the data into distinct volatility regimes. The analysis clearly demonstrated that during "routine" days, the variance in passenger arrival times was tight and predictable. However, during "disrupted" days—often triggered by cascading network weather delays—the standard arrival curves disintegrated, highlighting the critical need for models evaluated specifically on their resilience under stress.

### 4.4 Training Window Selection
The narrative behind the selection of May 2022 as the commencement of the training window is borne out by the data. Analysis of passenger volumes and show-up profiles prior to this date exhibited extreme, unpredictable variance associated with shifting pandemic travel restrictions, unpredictable business travel recovery, and the enforcement of the federal mask mandate.

By May 2022, the statistical indicators stabilized. The variance in the lead-lag arrival curves normalized, and the volume of business versus leisure travel reached a consistent, albeit new, equilibrium. Selecting this window ensured that the models were trained on data representative of the current structural regime of the aviation industry, rather than learning obsolete patterns from an anomalous historical period.

### 4.5 Validation of Checkpoint Isolation
Before progressing to model evaluation, it was necessary to confirm that the tier-four filtering strategy was successful. Econometric tests, specifically Granger causality analysis, were applied to the isolated checkpoint data. 

The results were definitive: changes in the scheduled departing seat capacity for the specific carrier assigned to a terminal strongly Granger-caused the subsequent passenger throughput at that terminal's dedicated checkpoint. Conversely, major shifts in capacity for other airlines operating at the same airport showed no statistically significant impact on the isolated checkpoint's throughput. This confirms that the methodology successfully isolated the demand signal, providing a clean, validated environment for training the predictive models.

### 4.6 Feature Engineering
The feature engineering phase operationalized the insights gained from the foundational framework, translating theoretical queueing concepts into mathematical inputs for the models. The most significant development was the formulation of the multi-period lead-lag features. 

Rather than simply looking at aggregate seats scheduled in the next hour, the engineering process created specific time-shifted variables. It quantified the number of seats departing in 60, 90, and 120 minutes, allowing the models to learn the precise, nuanced arrival curve of passengers. The empirical data strongly supported the ACRP baseline assumptions: the strongest predictive correlation for a passenger arriving at the checkpoint at 08:00 was found in the volume of seats scheduled to depart between 09:30 and 10:00. 

Additionally, the integration of DB1B data allowed for the creation of "adjusted capacity" features. By mathematically discounting the raw seat capacity by the historical connecting ratio of each specific flight route, the methodology generated a highly accurate estimate of the true local, landside demand, directly addressing the hub disconnect problem.

### 4.7 Model Results
The comprehensive evaluation of the model suite (M0-M5) across the dimensions of robustness, resilience, and generalizability yielded significant, actionable findings.

**Robustness (Routine Operations)**
During standard, non-disrupted operations, the machine learning approaches demonstrated clear superiority. The Gradient Boosting Machine (M4) achieved the lowest overall Mean Absolute Scaled Error (MASE), successfully capturing the complex, non-linear interactions between time-of-day, adjusted seat capacity, and seasonal trends. The baseline models (M0 and M1) consistently underperformed, hampered by their inability to adjust to subtle daily variations. Notably, the Adjusted Capacity Regression (M2) showed a marked improvement over the raw Static Regression (M1), proving that mathematically accounting for the hub disconnect provides an immediate, easily implementable boost to baseline accuracy.

**Resilience (Disrupted Operations)**
The critical differentiator emerged when evaluating the models under duress. During periods flagged by the Turbulence Index as highly volatile, the pure machine learning model (M4) experienced a severe degradation in accuracy, often "over-predicting" based on scheduled flights that were ultimately delayed. 

In these volatile scenarios, the Hybrid Dynamic Recursive Filter (M5) proved exceptionally resilient. By continuously updating its internal state based on real-time throughput observations, M5 quickly identified when the reality on the ground had deviated from the scheduled plan. Its R_MASE scores were significantly superior to all other models during major disruptions, proving its value as a tactical management tool during irregular operations. 

**Generalizability (Portability)**
The evaluation of model portability revealed the inherent trade-offs in highly complex architectures. When a model trained explicitly on the unique dynamics of ATL (a massive hub) was deployed unaltered to evaluate BOS (a strong O&D market), the highly tuned GBM (M4) suffered a massive loss in accuracy, failing the Ratio of Transferable Robustness (RTR) test. It had overfit to the specific operational quirks of Atlanta.

Conversely, the Adjusted Capacity Regression (M2) and the SARIMA model (M3) demonstrated much higher generalizability. Because they rely on fundamental, universally applicable variables (adjusted local seats and broad temporal trends, respectively) rather than deeply complex feature interactions, they transferred between diverse operational environments with minimal retraining. 

**Conclusion of Findings**
The Diebold-Mariano tests confirmed that these performance differences were statistically significant. The results definitively answer the research question: no single model is universally superior. If an airport authority prioritizes absolute accuracy during routine operations and possesses deep historical datasets, a feature-rich GBM (M4) is optimal. If the priority is tactical management during frequent severe weather disruptions, the Hybrid Recursive Filter (M5) is essential. However, for a regulatory body like the TSA seeking a scalable, easily deployable model across hundreds of diverse regional airports, an Adjusted Capacity Regression (M2) provides the best balance of generalizability and acceptable baseline performance.
