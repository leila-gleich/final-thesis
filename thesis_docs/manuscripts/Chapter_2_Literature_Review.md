# CHAPTER II: REVIEW OF RELEVANT LITERATURE

---

## 2.1 Traditional Approaches and Operational Complexity

As commercial aviation navigates a period of sustained traffic expansion that threatens to outpace the physical limitations of existing terminal infrastructure, the impracticality of continuous brick-and-mortar expansion has shifted operational focus toward software-driven, data-informed terminal capacity management (De Neufville & Odoni, 2014). Airport landside subsystems—specifically ticketing halls, passenger security screening checkpoints, and departure gate hold-rooms—operate as tightly coupled queuing networks. When demand outstrips processing capacity at security screening, congestion ripples backward into check-in areas and forward into departure concourses, inducing ground delays and passenger misconnections across the National Airspace System (Adacher et al., 2017).

### 2.1.1 Uncertainty, Batch Arrival Dynamics, and Flight Banks
A fundamental operational challenge in airport passenger demand forecasting is that passenger arrivals do not follow a uniform, steady stream. Rather, arrivals are characterized by high variability and concentrated "batches" induced by airline flight bank scheduling (Peterson et al., 1995; Cheng et al., 2012). Airlines operating hub-and-spoke networks intentionally cluster flight departures into narrow 45-to-90-minute waves to maximize connecting passenger transfer opportunities. Consequently, landside screening checkpoints experience severe demand surges that saturate screening lane capacity far more rapidly than smooth, uncoordinated traffic streams (Dönmez et al., 2025).

### 2.1.2 Classical Queuing Theory Foundations and Limitations
To translate unpredictable passenger movements into quantifiable system states, traditional airport planning has relied upon Queuing Theory (Odoni, 1986; Wang, 2017). Early terminal capacity models utilized Poisson arrival distributions ($M/M/s$ or $M/G/s$ queues) to calculate queue lengths and average waiting times relative to a target Level of Service (LOS) (Araujo & Repolho, 2015).

However, classical Poisson models rest on the assumption of a constant, time-invariant arrival rate ($\lambda$), which fails in commercial airports where flight banks generate severe non-linear fluctuations (Wang, 2018). While researchers subsequently transitioned toward Non-Homogeneous Poisson Processes (NHPP) to allow arrival rates to vary across hourly intervals (Brunetta et al., 1999), NHPP models still assume independent arrivals. In operational reality, passengers arriving on the same flight are strongly correlated, and hub connecting passengers never enter landside security queues at all (Guo et al., 2022). These simplifying assumptions limit the ability of purely analytical queuing equations to capture the volatility of contemporary terminal operations (Adeke, 2018).

---

## 2.2 Simulation Modeling and Real-Time Terminal Management

### 2.2.1 Discrete Event Simulation (DES) and Operational Limits
To overcome the mathematical rigidities of analytical queuing equations, airport planners widely adopted Discrete Event Simulation (DES) (Brown & Madhavan, 2011; Leone & Liu, 2011). Unlike static spreadsheets, DES models track individual passengers through a time-indexed sequence of discrete operational milestones (e.g., ticket scan, divestiture, metal detector screening, item retrieval).

Despite high visual fidelity, DES models exhibit critical operational limitations when deployed for real-time airport management:
1. **Calibration Sensitivity**: Small changes in baseline assumptions—such as secondary bag-search alarm rates or Transportation Security Officer (TSO) divestiture coaching times—produce disproportionately large shifts in modeled queue wait times (Brown & Madhavan, 2011).
2. **Computational Latency**: Simulating hundreds of thousands of individual passenger agents during severe, unfolding flight disruptions requires immense computational time, rendering DES impractical for real-time tactical lane reallocation (Takakuwa & Oyama, 2004; Bießlich et al., 2014).
3. **Passive Traveler Assumptions**: Standard simulation models treat passengers as passive entities following rigid rules, failing to reflect how travelers dynamically adjust arrival timing based on mobile flight delay notifications (Alodhaibi et al., 2017).

---

## 2.3 Time-Series Analysis and Data-Driven Predictive Frameworks

### 2.3.1 Statistical Time-Series Foundations (ARIMA and SARIMA)
To achieve faster, automated forecasts, transportation planners turned to empirical time-series models, such as Autoregressive Integrated Moving Average (ARIMA) and Seasonal ARIMA (SARIMA) formulations (Li et al., 2017). These models capture the dominant diurnal (24-hour) and day-of-week (168-hour) cyclical rhythms of airport operations. When augmented with exogenous variables (SARIMAX)—such as scheduled airline seat capacity—they provide computationally lightweight, transparent baseline estimates. However, linear time-series formulations struggle during operational structural breaks, such as severe weather ground stops, because they assume fixed autoregressive relationships that cannot accommodate sudden delay cascades.

### 2.3.2 Non-Linear Machine Learning and Sequential Neural Networks
To model complex non-linear relationships that linear statistical models cannot represent, recent aviation literature has explored machine learning algorithms, including Long Short-Term Memory (LSTM) recurrent networks, Gated Recurrent Units (GRU), and Gradient-Boosted Decision Trees (GBM) (Hopfe et al., 2024; Ribeiro et al., 2025). 

While deep neural networks can approximate complex multi-source interactions (e.g., weather indices, search engine trends, flight departure status), they introduce significant operational challenges in airport settings:
* **The "Black-Box" Interpretability Hurdle**: Airport Federal Security Directors (FSDs) and TSA operations planners cannot verify why a deep neural network predicts a sudden passenger volume spike, making them reluctant to commit staffing based on opaque model outputs (Adadi & Berrada, 2018; Viaña et al., 2024).
* **Facility-Specific Over-Specialization**: Highly parameterized neural networks tend to memorize terminal-specific gate layouts, unique local carrier flight banks, and idiosyncratic physical geometry, causing their forecast accuracy to degrade sharply when transferred to unfamiliar airports (Wang et al., 2025).

---

## 2.4 Hybrid Architectures: Combining Operational Structure with Data-Driven Adaptability

To resolve the tension between the transparency of traditional queuing models and the non-linear flexibility of modern machine learning, transportation researchers have converged toward **hybrid architectures** (Brun et al., 2025; Had et al., 2025).

### 2.4.1 Integrating Queuing Principles with Decision-Tree Algorithms
Rather than deploying fully end-to-end black-box models, effective hybrid architectures combine:
1. **First-Principles Operational Baselines**: Using established flight schedules, empirical passenger show-up curves (**ACRP Report 40**), and airline connecting passenger survey ratios (BTS DB1B) to establish a deterministic baseline demand estimate.
2. **Transparent Decision-Rule Adjustments**: Deploying interpretable machine learning—specifically **Gradient-Boosted Decision Trees**—to predict residual demand shifts caused by real-time flight delays, gate holds, and severe weather cancellations (Ribeiro et al., 2025).

Decision trees offer a critical operational advantage over deep neural networks: their branching structure can be directly mapped to operational rules (e.g., *"If flight departure delay exceeds 45 minutes and aircraft capacity exceeds 180 seats, adjust predicted security demand downward in the scheduled departure hour and upward in the preceding dwell window"*).

### 2.4.2 Dynamic Feedback and Real-Time State Tracking
During severe operational disruptions (such as summer convective thunderstorm ground stops), static schedules become obsolete. Recent research demonstrates that incorporating **recursive error-correction feedback** (such as Kalman filtering or sequential residual tracking) allows forecasting models to monitor live checkpoint throughput ($t-1$) and dynamically adjust queue demand states in real time, preventing the massive under-prediction typical of static flight schedule models (Ebert et al., 2021; Wu et al., 2024).

---

## 2.5 Post-Pandemic Operational Volatility and the Need for Multi-Dimensional Evaluation

While predictive modeling literature has historically focused on maximizing point accuracy under nominal operating conditions, the unprecedented disruptions of the COVID-19 pandemic and subsequent recovery demonstrated that single-metric evaluations are fundamentally inadequate (Sun et al., 2022; Li et al., 2023). In volatile modern aviation environments, predictive models must be evaluated across three distinct, complementary operational dimensions:

1. **Robustness (Routine Operational Accuracy)**: The consistency and precision of forecast models under nominal, clear-weather operating conditions with on-time flight operations (Lin, 2022).
2. **Resilience (Performance Under Severe Disruption)**: The capacity of a forecasting framework to maintain error bounded-ness, resist demand collapse, and recover rapidly during major exogenous shocks, such as Ground Delay Programs (GDP), severe winter blizzards, and summer convective thunderstorm ground stops (Schultz et al., 2021; Kazda et al., 2022).
3. **Generalizability (Cross-Airport Portability)**: The external validity and portability of trained model structures when deployed across structurally diverse airport terminal complexes without requiring site-specific historical recalibration (Tang et al., 2023; Güner & Seçkin Codal, 2024).

By formalizing these three operational pillars, this study provides a comprehensive, domain-grounded evaluation framework that bridges the gap between theoretical machine learning and defensible, deployable airport operations planning.
