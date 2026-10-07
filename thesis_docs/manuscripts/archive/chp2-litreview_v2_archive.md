# Chapter II

# Review of the Relevant Literature

## Traditional Approaches and Operational Complexity
As commercial aviation navigates a period of sustained traffic expansion that threatens to outpace the physical limitations of existing terminal infrastructure, the impracticality of continuous brick-and-mortar expansion has shifted operational focus toward software-driven, data-informed terminal capacity management (De Neufville & Odoni, 2014). Airport landside subsystems—specifically ticketing halls, passenger security screening checkpoints, and departure gate hold-rooms—operate as tightly coupled queuing networks. When demand outstrips processing capacity at security screening, congestion ripples backward into check-in areas and forward into departure concourses, inducing ground delays, boarding holds, and passenger misconnections across the National Airspace System (Adacher et al., 2017).

### Uncertainty, Batch Arrival Dynamics, and Flight Banks
A fundamental operational challenge in airport passenger demand forecasting is that passenger arrivals do not follow a uniform, steady stream. Rather, arrivals are characterized by high variability and concentrated "batches" induced by airline flight bank scheduling (Cheng et al., 2012; Peterson et al., 1995). Airlines operating hub-and-spoke networks intentionally cluster flight departures into narrow 45-to-90-minute waves to maximize connecting passenger transfer opportunities. Consequently, landside screening checkpoints experience severe demand surges that saturate screening lane capacity far more rapidly than smooth, uncoordinated traffic streams (Dönmez et al., 2025).

### Classical Queuing Theory: First Moment (Volume) vs. Second Moment (Volatility)
To translate unpredictable passenger movements into quantifiable system states, traditional airport planning has relied upon Queuing Theory (Odoni, 1986; Wang, 2017)—the mathematical study of waiting lines and congestion. Early terminal capacity models utilized Poisson arrival distributions (such as $M/M/s$ or $M/G/s$ queuing formulas, which calculate queue lengths and wait times based on assumed random arrival rates and screening speeds) relative to an airport's target Level of Service (LOS; industry benchmarks defining acceptable passenger waiting times and crowding thresholds) (Araujo & Repolho, 2015).

However, classical Poisson models rest on the assumption of a constant, time-invariant arrival rate ($\lambda$), which fails in commercial airports where flight banks generate severe non-linear fluctuations (Wang, 2018). While researchers subsequently transitioned toward Non-Homogeneous Poisson Processes (NHPP; queuing equations where passenger arrival rates vary across hourly intervals to reflect daily peaks and valleys) (Brunetta et al., 1999), NHPP models still evaluate queuing solely through the lens of expected volume (the first-order moment: $\mu = E[Y]$). 

In operational reality, heavy-traffic queuing principles (Kingman, 1961; Whitt, 1993) demonstrate that expected queue wait times ($W_q$) and queue backlogs in general $G/G/s$ screening facilities scale not with mean volume, but linearly with the **squared coefficient of variation of arrival times ($C_a^2$) and service times ($C_s^2$)** via the Allen-Cunneen approximation:
$$W_q \approx \left( \frac{\rho^{\sqrt{2(s+1)}-1}}{s(1-\rho)} \right) \left( \frac{C_a^2 + C_s^2}{2} \right) \frac{1}{\mu}$$
where $\rho = \frac{\lambda}{s \mu}$ represents checkpoint utilization. As checkpoint utilization approaches capacity ($\rho \to 1.0$) during morning and evening departure peaks, any increase in arrival volatility ($C_a^2$) triggers exponential queue length expansion and terminal crowd surges. Modeling and forecasting **throughput volatility** ($\sigma_{\text{TSA}}$ and $CV_{\text{TSA}}$) is therefore the vital prerequisite for robust lane staffing and queue stability (Adeke, 2018; Guo et al., 2022).

## The "Values versus Volatility" Paradigm in Transportation Demand
In modern econometric and volatility forecasting literature (Andersen & Bollerslev, 1998; Engle, 2001; Hansen & Lunde, 2005), a central research question is whether predicting the volatility of a stochastic process requires tracking the **values** (levels, volumes, and magnitudes) of explanatory variables, the **volatility** (dispersion, standard deviations, and coefficients of variation) of those variables, or a **dual combined representation**.

In commercial aviation operations, this duality manifests across two operational horizons:
1. **Intraday Diurnal Volatility**: The within-day standard deviation ($\sigma_{\text{TSA, hr}}$) naturally scales with airport passenger volume due to Tweedie-Poisson compound dispersion ($\text{Var}(Y) \propto \mu^p$), allowing feature values (e.g., total scheduled flights, aircraft seats) to serve as a strong baseline predictor. However, when normalized into scale-free relative burstiness ($CV_{\text{TSA, hr}} = \sigma / \mu$), volume levels lose explanatory power.
2. **Multi-Day Rolling Volatility**: Over multi-day horizons ($\sigma_{\text{TSA, 7d}}$), static flight volumes remain largely unchanged across seasonal schedules. Consequently, models relying exclusively on static feature values fail to anticipate medium-term passenger turbulence. Forecasting disruption-driven turbulence requires tracking the volatility of operational features—specifically rolling schedule variance ($\sigma_{\text{sched}}$), flight cancellation volatility ($CV_{\text{cancel}}$), and departure delay dispersion ($\sigma_{\text{Delay}}$) (Hopfe et al., 2024).

## Simulation Modeling and Real-Time Terminal Management

### Discrete Event Simulation and Operational Limits
To overcome the mathematical rigidities of analytical queuing equations, airport planners widely adopted Discrete Event Simulation (DES) (Brown & Madhavan, 2011; Leone & Liu, 2011). Unlike static spreadsheets, DES models track individual simulated passengers through a chronological sequence of discrete physical milestones: ticket scanning, divestiture (removing shoes, jackets, laptops, and liquids for X-ray inspection), body scanning, and item retrieval.

Despite high visual fidelity, DES models exhibit critical operational limitations when deployed for real-time airport management:
1. **Calibration Sensitivity**: Small changes in baseline assumptions—such as secondary bag-search alarm rates or Transportation Security Officer (TSO; federal screening personnel) divestiture coaching times—produce disproportionately large shifts in modeled queue wait times (Brown & Madhavan, 2011).
2. **Computational Latency**: Simulating hundreds of thousands of individual passenger agents during severe, unfolding flight disruptions requires immense computational time, rendering DES impractical for real-time tactical lane reallocation (Bießlich et al., 2014; Takakuwa & Oyama, 2004).
3. **Passive Traveler Assumptions**: Standard simulation models treat passengers as passive entities following rigid rules, failing to reflect how travelers dynamically adjust arrival timing based on mobile flight delay notifications (Alodhaibi et al., 2017).

## Time-Series Analysis and Data-Driven Predictive Frameworks

### Statistical Time-Series Foundations
To achieve faster, automated forecasts, transportation planners turned to empirical time-series models, such as Autoregressive Integrated Moving Average (ARIMA) and Seasonal ARIMA (SARIMA) formulations (Li et al., 2017). These models predict future hours by capturing the dominant diurnal (24-hour) and day-of-week (168-hour) cyclical rhythms of airport operations. When augmented with exogenous variables (SARIMAX)—such as published airline scheduled seat capacity—they provide computationally lightweight, transparent baseline estimates. However, linear time-series formulations struggle during operational structural breaks, such as severe weather ground stops, because they assume fixed historical relationships that cannot accommodate sudden delay cascades.

### Non-Linear Machine Learning and Sequential Neural Networks
To model complex non-linear relationships that linear statistical models cannot represent, recent aviation literature has explored machine learning algorithms, including deep sequence models such as Long Short-Term Memory (LSTM) recurrent networks, Gated Recurrent Units (GRU), and tree ensembles like Gradient-Boosted Decision Trees (GBM) (Hopfe et al., 2024; Ribeiro et al., 2025).

While deep neural networks can approximate complex multi-source interactions (e.g., weather indices, search engine trends, flight departure status), they introduce significant operational challenges in airport settings:
* **The "Black-Box" Interpretability Hurdle**: Airport Federal Security Directors (FSDs) and TSA operations planners cannot verify why a deep neural network predicts a sudden passenger volume spike, making them reluctant to commit staffing based on opaque model outputs (Adadi & Berrada, 2018; Viaña et al., 2024).
* **Facility-Specific Over-Specialization**: Highly parameterized neural networks tend to memorize terminal-specific gate layouts, unique local carrier flight banks, and idiosyncratic terminal layouts and gate configurations, causing their forecast accuracy to degrade sharply when transferred to unfamiliar airports (Wang et al., 2025).

## Hybrid Architectures: Combining Operational Structure with Data-Driven Adaptability
To resolve the tension between the transparency of traditional queuing models and the non-linear flexibility of modern machine learning, transportation researchers have converged toward hybrid architectures (Brun et al., 2025; Had et al., 2025).

### Integrating Queuing Principles with Decision-Tree Algorithms
Rather than deploying fully end-to-end black-box models, effective hybrid architectures combine:
1. **First-Principles Operational Baselines**: Using established flight schedules, empirical passenger show-up curves (Airport Cooperative Research Program [ACRP] Report 40; Transportation Research Board, 2010), and airline connecting passenger survey ratios (BTS DB1B) to establish a deterministic baseline volatility estimate.
2. **Transparent Decision-Rule Adjustments**: Deploying interpretable machine learning—specifically Gradient-Boosted Decision Trees—to predict residual volatility shifts caused by real-time flight delays, gate holds, and severe weather cancellations (Ribeiro et al., 2025).

Decision trees offer a critical operational advantage over deep neural networks: their branching structure functions like intuitive, transparent operational rules (e.g., *"If departure delay dispersion exceeds 45 minutes and cancellation rate exceeds 5%, adjust expected security volatility upward by +35%"*).

### Dynamic Feedback and Real-Time State Tracking
During severe operational disruptions (such as summer convective thunderstorm ground stops), static schedules become obsolete. Recent research demonstrates that incorporating recursive error-correction feedback (such as Kalman filtering, which functions like an automated tracking system that compares predicted volatility to actual volatility at time $t-1$ and immediately updates the expected backlog) allows forecasting models to monitor live checkpoint throughput and dynamically adjust queue demand states in real time, preventing the massive under-prediction typical of static flight schedule models (Ebert et al., 2021; Wu et al., 2024).

## Multi-Dimensional Operational Evaluation
While predictive modeling literature has historically focused on maximizing point accuracy under nominal operating conditions, the unprecedented disruptions of the COVID-19 pandemic and subsequent recovery demonstrated that single-metric evaluations are fundamentally inadequate (Li et al., 2023; Sun et al., 2022). In volatile modern aviation environments, predictive models must be evaluated across three distinct, complementary operational dimensions:

1. **Robustness (Routine Operational Accuracy)**: The consistency and precision of forecast models under nominal, clear-weather operating conditions with on-time flight operations (Lin, 2022).
2. **Resilience (Performance Under Severe Disruption)**: The capacity of a forecasting framework to maintain error bounded-ness, resist demand collapse, and recover rapidly during major exogenous shocks, such as Ground Delay Programs (GDP; FAA traffic initiatives holding departures at origin gates during destination weather bottlenecks), severe winter blizzards, and summer convective thunderstorm ground stops (Kazda et al., 2022; Schultz et al., 2021).
3. **Generalizability (Cross-Airport Portability)**: The external validity and portability of trained model structures when deployed across structurally diverse airport terminal complexes without requiring site-specific historical recalibration (Güner & Seçkin Codal, 2024; Tang et al., 2023).

By formalizing these three operational pillars, this study provides a comprehensive, domain-grounded evaluation framework that bridges the gap between theoretical machine learning and defensible, deployable airport operations planning.
