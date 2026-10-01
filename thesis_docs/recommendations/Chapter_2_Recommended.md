# CHAPTER II – LITERATURE REVIEW

## 2.1 Traditional Approaches and Operational Complexity
Airline passenger demand has traditionally been modeled using static, time‑of‑day curves or deterministic scaling of scheduled flight departures (De Neufville & Odoni, 2014).  These approaches treat the airport security‑screening checkpoint as a simple, linear function of flight volume, ignoring the stochastic nature of passenger arrivals and the heterogeneity of airport terminal layouts.  The literature repeatedly notes that when demand exceeds lane capacity, queuing congestion propagates backwards, inflating ground‑delay programs and increasing passenger miss‑connections (Adacher et al., 2017).

## 2.2 Simulation Modeling and Real‑Time Terminal Management
Discrete‑Event Simulation (DES) became the de‑facto tool for high‑fidelity terminal planning (Brown & Madhavan, 2011; Leone & Liu, 2011).  While DES captures individual passenger trajectories, its calibration sensitivity, computational latency, and reliance on passive traveler behavior limit its suitability for real‑time operational decision‑making (Takakuwa & Oyama, 2004; Bießlich et al., 2014).  Recent work has introduced adaptive simulation ensembles that integrate live flight‑status feeds, yet the latency remains prohibitive for hour‑by‑hour staffing adjustments.

## 2.3 Time‑Series Analysis & Data‑Driven Predictive Frameworks
Statistical time‑series models such as ARIMA and SARIMA provide lightweight, interpretable baselines for hourly checkpoint throughput (Li et al., 2017).  Extending these models with exogenous variables (SARIMAX) improves performance but still assumes a linear relationship between scheduled departures and passenger arrivals.  Machine‑learning techniques—gradient‑boosted decision trees (LightGBM), LSTM, GRU—have shown superior accuracy in capturing non‑linear interactions among weather, flight delays, and passenger‑show‑up behavior (Hopfe et al., 2024; Ribeiro et al., 2025).  However, deep‑neural networks incur interpretability challenges (Adadi & Berrada, 2018) and often over‑specialize to site‑specific gate configurations, reducing cross‑airport transferability.

## 2.4 Hybrid Architectures: Combining Operational Structure with Data‑Driven Adaptability
Hybrid models reconcile the transparency of queuing theory with the flexibility of machine learning.  Recent studies embed first‑principles operational baselines (e.g., deterministic passenger‑arrival curves derived from ACRP Report 40) and augment them with gradient‑boosted residual predictors that capture real‑time disruption signals (Ribeiro et al., 2025).  This architecture allows decision makers to trace model decisions to concrete operational rules—critical for TSA and FAA acceptance.

## 2.5 Post‑Pandemic Operational Volatility and the Need for Multi‑Dimensional Evaluation
The COVID‑19 pandemic fundamentally altered travel behavior, introducing abrupt demand spikes and collapses that static models cannot capture (Sun et al., 2022).  Researchers now emphasize **robustness** (routine accuracy), **resilience** (performance under extreme weather or airline cancellations), and **generalizability** (portability across airports with differing gate layouts) as essential evaluation pillars (Li et al., 2023).  This thesis adopts that three‑dimensional framework to systematically compare deterministic, probabilistic, and hybrid forecasting paradigms.

*The next chapters build on this literature foundation to describe data acquisition, methodological design, and empirical evaluation.*
