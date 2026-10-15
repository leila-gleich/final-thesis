# Appendix B.2: Master Literature Equation Registry
## Evaluating Predictive Techniques to Model Stochastic Airport Passenger Flow (MSAA / Gleich 700B)

```
====================================================================================================
PROJECT: Evaluating Predictive Techniques to Model Stochastic Airport Passenger Flow
AUTHOR: Leila Gleich | INSTITUTION: Embry-Riddle Aeronautical University
DEGREE: Master of Science in Aeronautics / Aviation Data Analytics (MSAA / Gleich 700B)
DOCUMENT: Appendix B.2 - Master Literature Equation Registry (20 Peer-Reviewed Equations)
COMPANION WORKBOOKS: master_thesis_tables.xlsx ('Table_B2_Equations') | appendix_tables.xlsx
====================================================================================================
```

## Executive Summary & Theoretical Grounding

This document compiles the **Master Literature Equation Registry (Table B.2)**, formalizing all **20 standard, peer-reviewed mathematical formulations, queuing approximations, capacity accounting identities, statistical error metrics, and econometric hypothesis tests** operationalized throughout Chapters I through V of this thesis.

A central theoretical and empirical contribution of this thesis is the formal transition from raw volume modeling ($y_t$) to **passenger screening throughput volatility** ($\sigma_{\text{TSA, hr}}$, $\text{CV}_{\text{TSA, hr}}$, and $\sigma_{\text{TSA, 7d}}$). Under **Kingman's heavy-traffic queuing formula** ($W_q \approx \frac{\rho}{1-\rho} \frac{C_a^2 + C_s^2}{2} \frac{1}{\mu}$), expected passenger queue delays escalate non-linearly with the squared coefficient of arrival variation ($C_a^2$) as checkpoint server utilization approaches capacity ($\rho \to 1.0$). Accordingly, every equation in this registry is rigorously indexed to its underlying queuing dynamics, operational data grain, and commercial aviation context.

---

## 1. Master Literature Equation Registry Table (Table B.2)

### Table B.2
*Master Literature Equation Registry: 20 Peer-Reviewed Operational Equations*

| Equation ID | Domain Category & Equation Name | Mathematical Formulation (LaTeX) | Parameters & Operational Variables | Published Literature Source & Citation | Thesis Operational Role |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **EQ-01** | **Kingman's Heavy-Traffic Queuing Approximation (Single-Server)**<br>*(Domain: Stochastic Queuing & Congestion Theory)* | $\displaystyle W_q \approx \left(\frac{\rho}{1-\rho}\right) \left(\frac{C_a^2 + C_s^2}{2}\right) \frac{1}{\mu}$ | • **$W_q$**: Mean waiting time in queue<br>• **$\rho$**: Server utilization (traffic intensity)<br>• **$C_a$**: Coefficient of variation of inter-arrival times<br>• **$C_s$**: Coefficient of variation of service times<br>• **$\mu$**: Mean service rate | Kingman, J. F. C. (1961). The single server queue in heavy traffic. Mathematical Proceedings of the Cambridge Philosophical Society, 57(4), 902–904; Kingman, J. F. C. (1962). On queues in heavy traffic. Journal of the Royal Statistical Society: Series B, 24(2), 383–392. | Establishes the fundamental theoretical queuing foundation of the thesis: checkpoint queues scale quadratically with arrival volatility ($C_a^2$) as checkpoint utilization approaches capacity ($\rho \to 1.0$), proving why predicting throughput volatility is operationally superior to predicting raw mean volume. |
| **EQ-02** | **Kingman-Whitt Multi-Server Heavy-Traffic Approximation (G/G/s Queue)**<br>*(Domain: Stochastic Queuing & Congestion Theory)* | $\displaystyle W_q \approx \left( \frac{\rho^{\sqrt{2(s+1)}-1}}{s(1-\rho)} \right) \left( \frac{C_a^2 + C_s^2}{2} \right) \frac{1}{\mu}$ | • **$W_q$**: Expected queue wait time<br>• **$s$**: Number of active parallel screening lanes<br>• **$\rho$**: Multi-server utilization ($\lambda / (s \cdot \mu)$)<br>• **$C_a$**: Arrival coefficient of variation<br>• **$C_s$**: Service time coefficient of variation<br>• **$\mu$**: Lane processing rate | Whitt, W. (1993). Approximations for the GI/G/m queue. Production and Operations Management, 2(2), 114–161; Marchal, W. G. (1976). An approximate formula for waiting time in GI/G/1. Operations Research, 24(3), 473–474. | Extends Kingman queuing principles to multi-lane airport security screening checkpoints (s parallel lanes), demonstrating buffer depletion under high lane utilization across Top 25 commercial airfields. |
| **EQ-03** | **Traffic Intensity / Checkpoint Utilization Ratio**<br>*(Domain: Stochastic Queuing & Congestion Theory)* | $\displaystyle \rho(t) = \frac{\lambda(t)}{c(t) \cdot \mu}$ | • **$\rho(t)$**: Instantaneous traffic intensity at hour $t$<br>• **$\lambda(t)$**: Hourly passenger arrival demand rate<br>• **$c(t)$**: Number of open screening lanes at hour $t$<br>• **$\mu_{\text{lane}}$**: Nominal screening throughput rate per lane (pax/lane-hr) | Kendall, D. G. (1953). Stochastic processes occurring in the theory of queues and their analysis by the method of the imbedded Markov chain. The Annals of Mathematical Statistics, 24(3), 338–354; Erlang, A. K. (1909). | Operationalized in Chapter III Macro Filtering (§3.4): small regional airfields operate at $\rho \ll 0.30$ (preventing queue formation), whereas Top 25 hubs routinely hit $\rho \to 1.0$ during bank surges (05:00–08:30 and 16:00–18:30). |
| **EQ-04** | **Lognormal Passenger Show-Up Lead-Time Distribution**<br>*(Domain: Passenger Lead-Time & Arrival Curves)* | $\displaystyle \tau \sim \text{Lognormal}(\mu, \sigma^2), \quad \mathbb{E}[\tau] \approx 105\text{ min}$ | • **$\tau$**: Lead time (minutes before scheduled departure) that ticketed passengers present at security<br>• **$\mu$**: Log-scale mean<br>• **$\sigma$**: Log-scale dispersion<br>• **$\mathbb{E}[\tau]$**: Expected show-up lead time ($\approx 105$ minutes for domestic legacy flights) | Airport Cooperative Research Program (ACRP). (2010). ACRP Report 40: Airport Curbside and Terminal Area Planning. Transportation Research Board, National Academies of Sciences, Engineering, and Medicine. | Governs the empirical lead-lag passenger arrival distribution convolving scheduled flight banks into landside security arrival curves across American Airlines, Delta Air Lines, and United Airlines. |
| **EQ-05** | **Gaussian Mixture Bimodal Boarding Arrival Distribution**<br>*(Domain: Passenger Lead-Time & Arrival Curves)* | $\displaystyle \tau_{\text{WN}} \sim w_1 \mathcal{N}(\mu_1, \sigma_1^2) + (1 - w_1) \mathcal{N}(\mu_2, \sigma_2^2)$ | • **$\tau_{\text{WN}}$**: Southwest Airlines passenger arrival lead time<br>• **$w_1$**: Weight of boarding position maximizers ($\approx 135$ min lead time)<br>• **$(1 - w_1)$**: Weight of carry-on business travelers ($\approx 65$ min lead time) | ACRP Report 40 (TRB, 2010); Pearson, K. (1894). Contributions to the mathematical theory of evolution. Philosophical Transactions of the Royal Society of London, 185, 71–110. | Empirically demonstrates that unassigned boarding produces bimodal arrival distributions, justifying Southwest Airlines exclusion under Meso Filtering to prevent passenger show-up heterogeneity. |
| **EQ-06** | **Local Originating Passenger Demand Accounting Identity**<br>*(Domain: Operational Accounting & Filtering)* | $\displaystyle \text{Demand}_{\text{orig}, t} = \sum_{f \in \mathcal{F}_t} \text{Seats}_f \cdot \text{LoadFactor}_f \cdot (1 - \text{ConnectingRatio}_{\text{airport}})$ | • **$\text{Demand}_{\text{orig}, t}$**: True originating passenger demand entering landside screening at hour $t$<br>• **$\text{Seats}_f$**: Aircraft seat capacity for flight $f$<br>• **$\text{LoadFactor}_f$**: Route-level passenger load factor<br>• **$\text{ConnectingRatio}_{\text{airport}}$**: Quarterly airport connecting percentage from DB1B | Bureau of Transportation Statistics (BTS). (2024). Form 41 Schedule T-100 Segment Data and DB1B Airline Origin and Destination Survey. U.S. Department of Transportation. | Resolves the Hub Disconnect: subtracts transferring passengers who never enter landside security queues, increasing explained schedule-to-checkpoint variance from 20.9% to 44.9% across the Top 25 airfields. |
| **EQ-07** | **Discrete Empirical Lead-Time Convolution (Finite Impulse Response)**<br>*(Domain: Passenger Lead-Time & Arrival Curves)* | $\displaystyle \text{Demand}_{\text{convolved}, t} = \sum_{h=1}^{3} w_h \cdot \left[ \sum_{f \in \mathcal{F}_{t+h}} \text{Seats}_f \cdot \text{LoadFactor}_f \cdot (1 - \text{ConnectingRatio}) \right]$ | • **$w_h$**: Empirical ACRP arrival weights: $w_1$ ($t+1$ hr lead) = 0.52, $w_2$ ($t+2$ hr lead) = 0.38, $w_3$ ($t+3$ hr lead) = 0.10, where $\sum w_h = 1.0$<br>• **$\mathcal{F}_{t+h}$**: Set of scheduled departures at hours $t+1, t+2, t+3$ | ACRP Report 40 (TRB, 2010); Oppenheim, A. V., & Schafer, R. W. (2009). Discrete-Time Signal Processing (3rd ed.). Prentice Hall. | The physical operational engine of Model 1 (Deterministic Flight Schedule Model), convolving scheduled departure banks into landside arrival hours to forecast baseline passenger demand. |
| **EQ-08** | **Intraday Diurnal Absolute Volume Volatility (Dispersion)**<br>*(Domain: Statistical Moments & Volatility Targets)* | $\displaystyle \sigma_{\text{TSA, hr}}(d) = \sqrt{\frac{1}{23} \sum_{h=0}^{23} (y_{d, h} - \bar{y}_d)^2}$ | • **$\sigma_{\text{TSA, hr}}(d)$**: Diurnal standard deviation of hourly passenger screening throughput on day $d$ (pax/hr)<br>• **$y_{d, h}$**: Hourly TSA throughput at hour $h$<br>• **$\bar{y}_d$**: Daily mean hourly throughput | Pearson, K. (1894). Contributions to the mathematical theory of evolution. Philosophical Transactions of the Royal Society of London, 185, 71–110. | Primary dependent modeling target 1: captures within-day absolute demand dispersion across the 24 hours of each day (in pax/hr), isolating bank surge amplitudes. |
| **EQ-09** | **Intraday Scale-Free Relative Arrival Volatility (Coefficient of Variation)**<br>*(Domain: Statistical Moments & Volatility Targets)* | $\displaystyle \text{CV}_{\text{TSA, hr}}(d) = \frac{\sigma_{\text{TSA, hr}}(d)}{\bar{y}_d} = \frac{\sqrt{\frac{1}{23}\sum_{h=0}^{23} (y_{d,h} - \bar{y}_d)^2}}{\frac{1}{24}\sum_{h=0}^{23} y_{d,h}}$ | • **$\text{CV}_{\text{TSA, hr}}(d)$**: Dimensionless ratio of hourly standard deviation to daily mean throughput | Pearson, K. (1895). Notes on regression and inheritance in the case of two parents. Proceedings of the Royal Society of London, 58, 240–242. | Primary dependent modeling target 2: removes facility baseline scale to quantify pure arrival burstiness and queue surge spikiness across different checkpoint geometries. |
| **EQ-10** | **Multi-Day Temporal Rolling Volatility**<br>*(Domain: Statistical Moments & Volatility Targets)* | $\displaystyle \sigma_{\text{TSA, 7d}}(d) = \sqrt{\frac{1}{6} \sum_{k=0}^{6} (Y_{d-k} - \bar{Y}_{7d})^2}$ | • **$\sigma_{\text{TSA, 7d}}(d)$**: Rolling 7-day standard deviation of daily passenger volume (pax/day)<br>• **$Y_{d-k}$**: Total daily throughput on day $d-k$<br>• **$\bar{Y}_{7d}$**: 7-day rolling mean daily throughput | Box, G. E., Jenkins, G. M., Reinsel, G. C., & Ljung, G. M. (2015). Time Series Analysis: Forecasting and Control (5th ed.). John Wiley & Sons. | Primary dependent modeling target 3: captures medium-term multi-day network turbulence caused by severe winter storm systems, convective ground delay programs, and cancellation cascades. |
| **EQ-11** | **Daily Flight Departure Delay Dispersion**<br>*(Domain: Statistical Moments & Volatility Targets)* | $\displaystyle \sigma_{\text{Delay}, d} = \sqrt{\frac{1}{N_d - 1}\sum_{i=1}^{N_d} (\text{DepDelay}_{d,i} - \bar{\text{DepDelay}}_d)^2}$ | • **$\sigma_{\text{Delay}, d}$**: Sample standard deviation of flight departure delays across uncancelled domestic departures on day $d$ (minutes)<br>• **$\text{DepDelay}_{d,i}$**: Actual minus scheduled departure time for flight $i$<br>• **$N_d$**: Total domestic departures on day $d$ | Standard sample variance; Bureau of Transportation Statistics (BTS). (2024). Airline On-Time Performance Data Technical Reporting Directives. | Primary airside explanatory volatility metric: exhibits strong operational coupling with landside checkpoint arrival volatility ($r = +0.4373, p < 0.05$), while raw delay minutes show zero correlation ($r = -0.062$). |
| **EQ-12** | **Root Mean Squared Error (RMSE)**<br>*(Domain: Time-Series Forecasting & Error Metrics)* | $\displaystyle \text{RMSE} = \sqrt{\frac{1}{N}\sum_{t=1}^N (y_t - \hat{y}_t)^2}$ | • **$\text{RMSE}$**: Quadratic loss forecast error (pax/hr)<br>• **$y_t$**: Actual observed volatility<br>• **$\hat{y}_t$**: Model-predicted volatility<br>• **$N$**: Sample evaluation hours | Standard quadratic loss metric in statistical estimation and econometric forecasting. | Governing absolute error metric for Dimension 1 (Robustness): Model 3 achieves lowest RMSE (222.1 pax/hr) on the 2025 holdout dataset (-91.3 pax/hr vs Model 1). |
| **EQ-13** | **Mean Absolute Error (MAE)**<br>*(Domain: Time-Series Forecasting & Error Metrics)* | $\displaystyle \text{MAE} = \frac{1}{N} \sum_{t=1}^N \left\vert y_t - \hat{y}_t \right\vert$ | • **$\text{MAE}$**: Linear loss forecast error (pax/hr)<br>• Absolute difference between observed and predicted values | Standard linear loss metric in time-series forecasting and regression. | Measures typical magnitude of point forecast errors without quadratic penalty for outliers; Model 3 achieves 142.8 pax/hr across dedicated screening complexes. |
| **EQ-14** | **Mean Forecast Bias (Directional Systematic Error)**<br>*(Domain: Time-Series Forecasting & Error Metrics)* | $\displaystyle \text{Bias} = \frac{1}{N} \sum_{t=1}^N (\hat{y}_t - y_t)$ | • **$\text{Bias}$**: Mean directional error (pax/hr); negative values indicate systematic under-prediction; positive values indicate over-prediction | Standard forecast bias metric in operations research and inventory management. | Evaluates systematic under-prediction during bank surges: Model 1 displays -42.1 pax/hr bias; Model 2 exhibits -18.4 pax/hr; Model 3 maintains near-zero bias (-8.5 pax/hr). |
| **EQ-15** | **Mean Absolute Scaled Error (MASE)**<br>*(Domain: Time-Series Forecasting & Error Metrics)* | $\displaystyle \text{MASE} = \frac{\frac{1}{N}\sum_{t=1}^N \left\vert y_t - \hat{y}_t \right\vert}{\frac{1}{N-24}\sum_{t=25}^N \left\vert y_t - y_{t-24} \right\vert}$ | • **$\text{MASE}$**: Scale-free relative forecast accuracy metric; numerator is candidate model MAE; denominator is in-sample mean absolute error of 24-hour diurnal naive persistence control | Hyndman, R. J., & Koehler, A. B. (2006). Another look at measures of forecast accuracy. International Journal of Forecasting, 22(4), 679–688. | Primary scale-free benchmark metric across all models and regimes: Baseline Control is calibrated at $\text{MASE} \equiv 1.000$; Model 2 achieves $\text{MASE} = 0.779$; Model 3 achieves champion $\text{MASE} = 0.662$. |
| **EQ-16** | **Diebold-Mariano Test Statistic for Equal Predictive Accuracy**<br>*(Domain: Hypothesis & Significance Testing)* | $\displaystyle \text{DM} = \frac{\bar{d}}{\sqrt{\widehat{\text{Var}}(\bar{d}) / N}} \sim \mathcal{N}(0, 1)$ | • **$d_t = e_{1,t}^2 - e_{2,t}^2$**: Loss differential at time $t$ between Model 1 and competing model<br>• **$\bar{d}$**: Sample mean loss differential<br>• **$\widehat{\text{Var}}(\bar{d})$**: Asymptotic long-run Newey-West HAC variance of loss differential | Diebold, F. X., & Mariano, R. S. (1995). Comparing predictive accuracy. Journal of Business & Economic Statistics, 13(3), 253–263. | Formally proves that Model 2 ($DM = 42.15, p < 0.0001$) and Model 3 ($DM = 48.72, p < 0.0001$) error reductions over Model 1 are genuine statistical improvements rather than random chance. |
| **EQ-17** | **Chow Test Statistic for Structural Breaks in Linear Regressions**<br>*(Domain: Hypothesis & Significance Testing)* | $\displaystyle F = \frac{(\text{RSS}_C - (\text{RSS}_1 + \text{RSS}_2)) / k}{(\text{RSS}_1 + \text{RSS}_2) / (N_1 + N_2 - 2k)} \sim F(k, N_1 + N_2 - 2k)$ | • **$\text{RSS}_C$**: Residual sum of squares of pooled model<br>• **$\text{RSS}_1, \text{RSS}_2$**: Residual sums of squares of pre- and post-break sub-periods<br>• **$k$**: Number of model parameters<br>• **$N_1, N_2$**: Sample sizes of pre- and post-break sub-periods | Chow, G. C. (1960). Tests of equality between sets of coefficients in two linear regressions. Econometrica, 28(3), 591–605. | Statistically justified the Candidate B temporal demarcation point (May 1, 2022 post-mask mandate): Chow test confirms structural stability ($p \ge 0.15$) for the post-mandate modern operational regime. |
| **EQ-18** | **CUSUM Test for Structural Parameter Stability**<br>*(Domain: Hypothesis & Significance Testing)* | $\displaystyle W_t = \sum_{r=k+1}^t \frac{w_r}{\hat{\sigma}_w}$ | • **$W_t$**: Cumulative sum of standardized recursive residuals $w_r$<br>• **$w_r$**: Standardized recursive residual at step $r$<br>• **$\hat{\sigma}_w$**: Sample standard deviation of recursive residuals<br>• **$k$**: Number of regression regressors | Brown, R. L., Durbin, J., & Evans, J. M. (1975). Techniques for testing the constancy of regression relationships over time. Journal of the Royal Statistical Society: Series B, 37(2), 149–163. | Demonstrates that cumulative recursive residuals stay strictly within the 95% confidence bands from May 2022 through Dec 2025, validating model training data integrity. |
| **EQ-19** | **Peak-to-Average Ratio (PAR / Crest Factor)**<br>*(Domain: Statistical Moments & Volatility Targets)* | $\displaystyle \text{PAR}_d = \frac{\max_{h \in [0,23]} y_{d,h}}{\frac{1}{24}\sum_{h=0}^{23} y_{d,h}}$ | • **$\text{PAR}_d$**: Ratio of maximum hourly throughput on day $d$ to daily average hourly volume; measures acute demand concentration into a single peak hour | Standard engineering and operational metrics (Crest Factor / Peak-to-Average Ratio); Oppenheim & Schafer (2009). | Standard literature replacement for $S_{\text{TSA}}$: identifies days where checkpoint queues experience extreme surge concentration into an acute morning or evening rush hour. |
| **EQ-20** | **Volatility-Buffered Safety Capacity Lane Dimensioning Rule**<br>*(Domain: Operational Dimensioning & Staffing)* | $\displaystyle c(t) = \left\lceil \frac{\hat{\mu}_t + z_q \cdot \hat{\sigma}_{\text{TSA}, t}}{\mu_{\text{lane}}} \right\rceil$ | • **$c(t)$**: Recommended integer number of open screening lanes at hour $t$<br>• **$\hat{\mu}_t$**: Expected hourly passenger arrivals<br>• **$\hat{\sigma}_{\text{TSA}, t}$**: Forecasted arrival volatility<br>• **$z_q$**: Normal service coverage quantile factor ($z_{0.95} = 1.645$)<br>• **$\mu_{\text{lane}}$**: Lane throughput capacity (pax/lane-hr) | Erlang, A. K. (1917); Kolesar, P., & Green, L. (1998). Insights on capacity planning using a queuing model. Management Science; Whitt, W. (1992). Understanding the efficiency of multi-server service systems. Management Science, 38(5), 708–723. | Translates volatility forecasts into actionable security checkpoint lane dimensioning in Chapter V (§5.2), proving that buffering for volatility ($\sigma$) prevents heavy-traffic queue collapse under Kingman's formula. |

*Note.* Master census of all 20 peer-reviewed operational, queuing, econometrics, and lane allocation equations utilized across Chapters I–V. Mathematical formulations strictly adhere to APA Style (7th ed.) and authentic commercial aviation operations nomenclature. Conformed CSV source: `results/manuscript_tables/appendix_standard_literature_equations.csv`.

---

## 2. Detailed Mathematical Derivations & Operational Context by Research Domain

The 20 equations are organized into seven distinct operational research domains, detailed below with formal display math, parameter inventories, and thesis cross-references.

### Domain: Stochastic Queuing & Congestion Theory

#### EQ-01: Kingman's Heavy-Traffic Queuing Approximation (Single-Server)

$$W_q \approx \left(\frac{\rho}{1-\rho}\right) \left(\frac{C_a^2 + C_s^2}{2}\right) \frac{1}{\mu}$$

* **Plain-Text Formulation**: `W_q ≈ [rho / (1 - rho)] * [(C_a^2 + C_s^2) / 2] * (1 / mu)`
* **Published Source / Citation**: Kingman, J. F. C. (1961). The single server queue in heavy traffic. Mathematical Proceedings of the Cambridge Philosophical Society, 57(4), 902–904; Kingman, J. F. C. (1962). On queues in heavy traffic. Journal of the Royal Statistical Society: Series B, 24(2), 383–392.
* **Thesis Operational Role**: Establishes the fundamental theoretical queuing foundation of the thesis: checkpoint queues scale quadratically with arrival volatility ($C_a^2$) as checkpoint utilization approaches capacity ($\rho \to 1.0$), proving why predicting throughput volatility is operationally superior to predicting raw mean volume.
* **Parameters & Operational Definitions**:
  - **$W_q$**: Mean waiting time in queue
  - **$\rho$**: Server utilization (traffic intensity)
  - **$C_a$**: Coefficient of variation of inter-arrival times
  - **$C_s$**: Coefficient of variation of service times
  - **$\mu$**: Mean service rate

#### EQ-02: Kingman-Whitt Multi-Server Heavy-Traffic Approximation (G/G/s Queue)

$$W_q \approx \left( \frac{\rho^{\sqrt{2(s+1)}-1}}{s(1-\rho)} \right) \left( \frac{C_a^2 + C_s^2}{2} \right) \frac{1}{\mu}$$

* **Plain-Text Formulation**: `W_q ≈ [rho^(sqrt(2*(s+1)) - 1) / (s*(1 - rho))] * [(C_a^2 + C_s^2) / 2] * (1 / mu)`
* **Published Source / Citation**: Whitt, W. (1993). Approximations for the GI/G/m queue. Production and Operations Management, 2(2), 114–161; Marchal, W. G. (1976). An approximate formula for waiting time in GI/G/1. Operations Research, 24(3), 473–474.
* **Thesis Operational Role**: Extends Kingman queuing principles to multi-lane airport security screening checkpoints (s parallel lanes), demonstrating buffer depletion under high lane utilization across Top 25 commercial airfields.
* **Parameters & Operational Definitions**:
  - **$W_q$**: Expected queue wait time
  - **$s$**: Number of active parallel screening lanes
  - **$\rho$**: Multi-server utilization ($\lambda / (s \cdot \mu)$)
  - **$C_a$**: Arrival coefficient of variation
  - **$C_s$**: Service time coefficient of variation
  - **$\mu$**: Lane processing rate

#### EQ-03: Traffic Intensity / Checkpoint Utilization Ratio

$$\rho(t) = \frac{\lambda(t)}{c(t) \cdot \mu}$$

* **Plain-Text Formulation**: `rho(t) = lambda(t) / (c(t) * mu)`
* **Published Source / Citation**: Kendall, D. G. (1953). Stochastic processes occurring in the theory of queues and their analysis by the method of the imbedded Markov chain. The Annals of Mathematical Statistics, 24(3), 338–354; Erlang, A. K. (1909).
* **Thesis Operational Role**: Operationalized in Chapter III Macro Filtering (§3.4): small regional airfields operate at $\rho \ll 0.30$ (preventing queue formation), whereas Top 25 hubs routinely hit $\rho \to 1.0$ during bank surges (05:00–08:30 and 16:00–18:30).
* **Parameters & Operational Definitions**:
  - **$\rho(t)$**: Instantaneous traffic intensity at hour $t$
  - **$\lambda(t)$**: Hourly passenger arrival demand rate
  - **$c(t)$**: Number of open screening lanes at hour $t$
  - **$\mu_{\text{lane}}$**: Nominal screening throughput rate per lane (pax/lane-hr)

---

### Domain: Passenger Lead-Time & Arrival Curves

#### EQ-04: Lognormal Passenger Show-Up Lead-Time Distribution

$$\tau \sim \text{Lognormal}(\mu, \sigma^2), \quad \mathbb{E}[\tau] \approx 105\text{ min}$$

* **Plain-Text Formulation**: `tau ~ Lognormal(mu, sigma^2), with E[tau] ≈ 105 minutes`
* **Published Source / Citation**: Airport Cooperative Research Program (ACRP). (2010). ACRP Report 40: Airport Curbside and Terminal Area Planning. Transportation Research Board, National Academies of Sciences, Engineering, and Medicine.
* **Thesis Operational Role**: Governs the empirical lead-lag passenger arrival distribution convolving scheduled flight banks into landside security arrival curves across American Airlines, Delta Air Lines, and United Airlines.
* **Parameters & Operational Definitions**:
  - **$\tau$**: Lead time (minutes before scheduled departure) that ticketed passengers present at security
  - **$\mu$**: Log-scale mean
  - **$\sigma$**: Log-scale dispersion
  - **$\mathbb{E}[\tau]$**: Expected show-up lead time ($\approx 105$ minutes for domestic legacy flights)

#### EQ-05: Gaussian Mixture Bimodal Boarding Arrival Distribution

$$\tau_{\text{WN}} \sim w_1 \mathcal{N}(\mu_1, \sigma_1^2) + (1 - w_1) \mathcal{N}(\mu_2, \sigma_2^2)$$

* **Plain-Text Formulation**: `tau_WN ~ w1 * N(mu1, sigma1^2) + (1 - w1) * N(mu2, sigma2^2)`
* **Published Source / Citation**: ACRP Report 40 (TRB, 2010); Pearson, K. (1894). Contributions to the mathematical theory of evolution. Philosophical Transactions of the Royal Society of London, 185, 71–110.
* **Thesis Operational Role**: Empirically demonstrates that unassigned boarding produces bimodal arrival distributions, justifying Southwest Airlines exclusion under Meso Filtering to prevent passenger show-up heterogeneity.
* **Parameters & Operational Definitions**:
  - **$\tau_{\text{WN}}$**: Southwest Airlines passenger arrival lead time
  - **$w_1$**: Weight of boarding position maximizers ($\approx 135$ min lead time)
  - **$(1 - w_1)$**: Weight of carry-on business travelers ($\approx 65$ min lead time)

#### EQ-07: Discrete Empirical Lead-Time Convolution (Finite Impulse Response)

$$\text{Demand}_{\text{convolved}, t} = \sum_{h=1}^{3} w_h \cdot \left[ \sum_{f \in \mathcal{F}_{t+h}} \text{Seats}_f \cdot \text{LoadFactor}_f \cdot (1 - \text{ConnectingRatio}) \right]$$

* **Plain-Text Formulation**: `Demand_convolved(t) = sum_{h=1..3} [ w_h * Demand_orig(t+h) ]`
* **Published Source / Citation**: ACRP Report 40 (TRB, 2010); Oppenheim, A. V., & Schafer, R. W. (2009). Discrete-Time Signal Processing (3rd ed.). Prentice Hall.
* **Thesis Operational Role**: The physical operational engine of Model 1 (Deterministic Flight Schedule Model), convolving scheduled departure banks into landside arrival hours to forecast baseline passenger demand.
* **Parameters & Operational Definitions**:
  - **$w_h$**: Empirical ACRP arrival weights: $w_1$ ($t+1$ hr lead) = 0.52, $w_2$ ($t+2$ hr lead) = 0.38, $w_3$ ($t+3$ hr lead) = 0.10, where $\sum w_h = 1.0$
  - **$\mathcal{F}_{t+h}$**: Set of scheduled departures at hours $t+1, t+2, t+3$

---

### Domain: Operational Accounting & Filtering

#### EQ-06: Local Originating Passenger Demand Accounting Identity

$$\text{Demand}_{\text{orig}, t} = \sum_{f \in \mathcal{F}_t} \text{Seats}_f \cdot \text{LoadFactor}_f \cdot (1 - \text{ConnectingRatio}_{\text{airport}})$$

* **Plain-Text Formulation**: `Demand_orig(t) = sum_{f in F_t} [ Seats_f * LoadFactor_f * (1 - ConnectingRatio_airport) ]`
* **Published Source / Citation**: Bureau of Transportation Statistics (BTS). (2024). Form 41 Schedule T-100 Segment Data and DB1B Airline Origin and Destination Survey. U.S. Department of Transportation.
* **Thesis Operational Role**: Resolves the Hub Disconnect: subtracts transferring passengers who never enter landside security queues, increasing explained schedule-to-checkpoint variance from 20.9% to 44.9% across the Top 25 airfields.
* **Parameters & Operational Definitions**:
  - **$\text{Demand}_{\text{orig}, t}$**: True originating passenger demand entering landside screening at hour $t$
  - **$\text{Seats}_f$**: Aircraft seat capacity for flight $f$
  - **$\text{LoadFactor}_f$**: Route-level passenger load factor
  - **$\text{ConnectingRatio}_{\text{airport}}$**: Quarterly airport connecting percentage from DB1B

---

### Domain: Statistical Moments & Volatility Targets

#### EQ-08: Intraday Diurnal Absolute Volume Volatility (Dispersion)

$$\sigma_{\text{TSA, hr}}(d) = \sqrt{\frac{1}{23} \sum_{h=0}^{23} (y_{d, h} - \bar{y}_d)^2}$$

* **Plain-Text Formulation**: `sigma_TSA_hr(d) = sqrt( (1 / 23) * sum_{h=0..23} (y_{d,h} - y_bar_d)^2 )`
* **Published Source / Citation**: Pearson, K. (1894). Contributions to the mathematical theory of evolution. Philosophical Transactions of the Royal Society of London, 185, 71–110.
* **Thesis Operational Role**: Primary dependent modeling target 1: captures within-day absolute demand dispersion across the 24 hours of each day (in pax/hr), isolating bank surge amplitudes.
* **Parameters & Operational Definitions**:
  - **$\sigma_{\text{TSA, hr}}(d)$**: Diurnal standard deviation of hourly passenger screening throughput on day $d$ (pax/hr)
  - **$y_{d, h}$**: Hourly TSA throughput at hour $h$
  - **$\bar{y}_d$**: Daily mean hourly throughput

#### EQ-09: Intraday Scale-Free Relative Arrival Volatility (Coefficient of Variation)

$$\text{CV}_{\text{TSA, hr}}(d) = \frac{\sigma_{\text{TSA, hr}}(d)}{\bar{y}_d} = \frac{\sqrt{\frac{1}{23}\sum_{h=0}^{23} (y_{d,h} - \bar{y}_d)^2}}{\frac{1}{24}\sum_{h=0}^{23} y_{d,h}}$$

* **Plain-Text Formulation**: `CV_TSA_hr(d) = sigma_TSA_hr(d) / y_bar_d`
* **Published Source / Citation**: Pearson, K. (1895). Notes on regression and inheritance in the case of two parents. Proceedings of the Royal Society of London, 58, 240–242.
* **Thesis Operational Role**: Primary dependent modeling target 2: removes facility baseline scale to quantify pure arrival burstiness and queue surge spikiness across different checkpoint geometries.
* **Parameters & Operational Definitions**:
  - **$\text{CV}_{\text{TSA, hr}}(d)$**: Dimensionless ratio of hourly standard deviation to daily mean throughput

#### EQ-10: Multi-Day Temporal Rolling Volatility

$$\sigma_{\text{TSA, 7d}}(d) = \sqrt{\frac{1}{6} \sum_{k=0}^{6} (Y_{d-k} - \bar{Y}_{7d})^2}$$

* **Plain-Text Formulation**: `sigma_TSA_7d(d) = sqrt( (1 / 6) * sum_{k=0..6} (Y_{d-k} - Y_bar_7d)^2 )`
* **Published Source / Citation**: Box, G. E., Jenkins, G. M., Reinsel, G. C., & Ljung, G. M. (2015). Time Series Analysis: Forecasting and Control (5th ed.). John Wiley & Sons.
* **Thesis Operational Role**: Primary dependent modeling target 3: captures medium-term multi-day network turbulence caused by severe winter storm systems, convective ground delay programs, and cancellation cascades.
* **Parameters & Operational Definitions**:
  - **$\sigma_{\text{TSA, 7d}}(d)$**: Rolling 7-day standard deviation of daily passenger volume (pax/day)
  - **$Y_{d-k}$**: Total daily throughput on day $d-k$
  - **$\bar{Y}_{7d}$**: 7-day rolling mean daily throughput

#### EQ-11: Daily Flight Departure Delay Dispersion

$$\sigma_{\text{Delay}, d} = \sqrt{\frac{1}{N_d - 1}\sum_{i=1}^{N_d} (\text{DepDelay}_{d,i} - \bar{\text{DepDelay}}_d)^2}$$

* **Plain-Text Formulation**: `sigma_Delay(d) = sqrt( (1 / (N_d - 1)) * sum_{i=1..N_d} (DepDelay_{d,i} - DepDelay_bar_d)^2 )`
* **Published Source / Citation**: Standard sample variance; Bureau of Transportation Statistics (BTS). (2024). Airline On-Time Performance Data Technical Reporting Directives.
* **Thesis Operational Role**: Primary airside explanatory volatility metric: exhibits strong operational coupling with landside checkpoint arrival volatility ($r = +0.4373, p < 0.05$), while raw delay minutes show zero correlation ($r = -0.062$).
* **Parameters & Operational Definitions**:
  - **$\sigma_{\text{Delay}, d}$**: Sample standard deviation of flight departure delays across uncancelled domestic departures on day $d$ (minutes)
  - **$\text{DepDelay}_{d,i}$**: Actual minus scheduled departure time for flight $i$
  - **$N_d$**: Total domestic departures on day $d$

#### EQ-19: Peak-to-Average Ratio (PAR / Crest Factor)

$$\text{PAR}_d = \frac{\max_{h \in [0,23]} y_{d,h}}{\frac{1}{24}\sum_{h=0}^{23} y_{d,h}}$$

* **Plain-Text Formulation**: `PAR_d = max(y_{d,h}) / mean(y_{d,h})`
* **Published Source / Citation**: Standard engineering and operational metrics (Crest Factor / Peak-to-Average Ratio); Oppenheim & Schafer (2009).
* **Thesis Operational Role**: Standard literature replacement for $S_{\text{TSA}}$: identifies days where checkpoint queues experience extreme surge concentration into an acute morning or evening rush hour.
* **Parameters & Operational Definitions**:
  - **$\text{PAR}_d$**: Ratio of maximum hourly throughput on day $d$ to daily average hourly volume; measures acute demand concentration into a single peak hour

---

### Domain: Time-Series Forecasting & Error Metrics

#### EQ-12: Root Mean Squared Error (RMSE)

$$\text{RMSE} = \sqrt{\frac{1}{N}\sum_{t=1}^N (y_t - \hat{y}_t)^2}$$

* **Plain-Text Formulation**: `RMSE = sqrt( (1 / N) * sum_{t=1..N} (y_t - y_hat_t)^2 )`
* **Published Source / Citation**: Standard quadratic loss metric in statistical estimation and econometric forecasting.
* **Thesis Operational Role**: Governing absolute error metric for Dimension 1 (Robustness): Model 3 achieves lowest RMSE (222.1 pax/hr) on the 2025 holdout dataset (-91.3 pax/hr vs Model 1).
* **Parameters & Operational Definitions**:
  - **$\text{RMSE}$**: Quadratic loss forecast error (pax/hr)
  - **$y_t$**: Actual observed volatility
  - **$\hat{y}_t$**: Model-predicted volatility
  - **$N$**: Sample evaluation hours

#### EQ-13: Mean Absolute Error (MAE)

$$\text{MAE} = \frac{1}{N} \sum_{t=1}^N \left\vert y_t - \hat{y}_t \right\vert$$

* **Plain-Text Formulation**: `MAE = (1 / N) * sum_{t=1..N} |y_t - y_hat_t|`
* **Published Source / Citation**: Standard linear loss metric in time-series forecasting and regression.
* **Thesis Operational Role**: Measures typical magnitude of point forecast errors without quadratic penalty for outliers; Model 3 achieves 142.8 pax/hr across dedicated screening complexes.
* **Parameters & Operational Definitions**:
  - **$\text{MAE}$**: Linear loss forecast error (pax/hr)
  - Absolute difference between observed and predicted values

#### EQ-14: Mean Forecast Bias (Directional Systematic Error)

$$\text{Bias} = \frac{1}{N} \sum_{t=1}^N (\hat{y}_t - y_t)$$

* **Plain-Text Formulation**: `Bias = (1 / N) * sum_{t=1..N} (y_hat_t - y_t)`
* **Published Source / Citation**: Standard forecast bias metric in operations research and inventory management.
* **Thesis Operational Role**: Evaluates systematic under-prediction during bank surges: Model 1 displays -42.1 pax/hr bias; Model 2 exhibits -18.4 pax/hr; Model 3 maintains near-zero bias (-8.5 pax/hr).
* **Parameters & Operational Definitions**:
  - **$\text{Bias}$**: Mean directional error (pax/hr); negative values indicate systematic under-prediction; positive values indicate over-prediction

#### EQ-15: Mean Absolute Scaled Error (MASE)

$$\text{MASE} = \frac{\frac{1}{N}\sum_{t=1}^N \left\vert y_t - \hat{y}_t \right\vert}{\frac{1}{N-24}\sum_{t=25}^N \left\vert y_t - y_{t-24} \right\vert}$$

* **Plain-Text Formulation**: `MASE = MAE_model / MAE_naive_24h_persistence`
* **Published Source / Citation**: Hyndman, R. J., & Koehler, A. B. (2006). Another look at measures of forecast accuracy. International Journal of Forecasting, 22(4), 679–688.
* **Thesis Operational Role**: Primary scale-free benchmark metric across all models and regimes: Baseline Control is calibrated at $\text{MASE} \equiv 1.000$; Model 2 achieves $\text{MASE} = 0.779$; Model 3 achieves champion $\text{MASE} = 0.662$.
* **Parameters & Operational Definitions**:
  - **$\text{MASE}$**: Scale-free relative forecast accuracy metric; numerator is candidate model MAE; denominator is in-sample mean absolute error of 24-hour diurnal naive persistence control

---

### Domain: Hypothesis & Significance Testing

#### EQ-16: Diebold-Mariano Test Statistic for Equal Predictive Accuracy

$$\text{DM} = \frac{\bar{d}}{\sqrt{\widehat{\text{Var}}(\bar{d}) / N}} \sim \mathcal{N}(0, 1)$$

* **Plain-Text Formulation**: `DM = d_bar / sqrt(Var_hat(d_bar) / N) ~ N(0, 1)`
* **Published Source / Citation**: Diebold, F. X., & Mariano, R. S. (1995). Comparing predictive accuracy. Journal of Business & Economic Statistics, 13(3), 253–263.
* **Thesis Operational Role**: Formally proves that Model 2 ($DM = 42.15, p < 0.0001$) and Model 3 ($DM = 48.72, p < 0.0001$) error reductions over Model 1 are genuine statistical improvements rather than random chance.
* **Parameters & Operational Definitions**:
  - **$d_t = e_{1,t}^2 - e_{2,t}^2$**: Loss differential at time $t$ between Model 1 and competing model
  - **$\bar{d}$**: Sample mean loss differential
  - **$\widehat{\text{Var}}(\bar{d})$**: Asymptotic long-run Newey-West HAC variance of loss differential

#### EQ-17: Chow Test Statistic for Structural Breaks in Linear Regressions

$$F = \frac{(\text{RSS}_C - (\text{RSS}_1 + \text{RSS}_2)) / k}{(\text{RSS}_1 + \text{RSS}_2) / (N_1 + N_2 - 2k)} \sim F(k, N_1 + N_2 - 2k)$$

* **Plain-Text Formulation**: `F = [ (RSS_C - (RSS_1 + RSS_2)) / k ] / [ (RSS_1 + RSS_2) / (N_1 + N_2 - 2k) ]`
* **Published Source / Citation**: Chow, G. C. (1960). Tests of equality between sets of coefficients in two linear regressions. Econometrica, 28(3), 591–605.
* **Thesis Operational Role**: Statistically justified the Candidate B temporal demarcation point (May 1, 2022 post-mask mandate): Chow test confirms structural stability ($p \ge 0.15$) for the post-mandate modern operational regime.
* **Parameters & Operational Definitions**:
  - **$\text{RSS}_C$**: Residual sum of squares of pooled model
  - **$\text{RSS}_1, \text{RSS}_2$**: Residual sums of squares of pre- and post-break sub-periods
  - **$k$**: Number of model parameters
  - **$N_1, N_2$**: Sample sizes of pre- and post-break sub-periods

#### EQ-18: CUSUM Test for Structural Parameter Stability

$$W_t = \sum_{r=k+1}^t \frac{w_r}{\hat{\sigma}_w}$$

* **Plain-Text Formulation**: `W_t = sum_{r=k+1..t} [ w_r / sigma_hat_w ]`
* **Published Source / Citation**: Brown, R. L., Durbin, J., & Evans, J. M. (1975). Techniques for testing the constancy of regression relationships over time. Journal of the Royal Statistical Society: Series B, 37(2), 149–163.
* **Thesis Operational Role**: Demonstrates that cumulative recursive residuals stay strictly within the 95% confidence bands from May 2022 through Dec 2025, validating model training data integrity.
* **Parameters & Operational Definitions**:
  - **$W_t$**: Cumulative sum of standardized recursive residuals $w_r$
  - **$w_r$**: Standardized recursive residual at step $r$
  - **$\hat{\sigma}_w$**: Sample standard deviation of recursive residuals
  - **$k$**: Number of regression regressors

---

### Domain: Operational Dimensioning & Staffing

#### EQ-20: Volatility-Buffered Safety Capacity Lane Dimensioning Rule

$$c(t) = \left\lceil \frac{\hat{\mu}_t + z_q \cdot \hat{\sigma}_{\text{TSA}, t}}{\mu_{\text{lane}}} \right\rceil$$

* **Plain-Text Formulation**: `c(t) = ceil( (mu_hat_t + z_q * sigma_hat_t) / mu_lane )`
* **Published Source / Citation**: Erlang, A. K. (1917); Kolesar, P., & Green, L. (1998). Insights on capacity planning using a queuing model. Management Science; Whitt, W. (1992). Understanding the efficiency of multi-server service systems. Management Science, 38(5), 708–723.
* **Thesis Operational Role**: Translates volatility forecasts into actionable security checkpoint lane dimensioning in Chapter V (§5.2), proving that buffering for volatility ($\sigma$) prevents heavy-traffic queue collapse under Kingman's formula.
* **Parameters & Operational Definitions**:
  - **$c(t)$**: Recommended integer number of open screening lanes at hour $t$
  - **$\hat{\mu}_t$**: Expected hourly passenger arrivals
  - **$\hat{\sigma}_{\text{TSA}, t}$**: Forecasted arrival volatility
  - **$z_q$**: Normal service coverage quantile factor ($z_{0.95} = 1.645$)
  - **$\mu_{\text{lane}}$**: Lane throughput capacity (pax/lane-hr)

---

## 3. Methodological Synthesis & Hypothesis Mapping

The 20 literature equations collectively operationalize the central findings and core hypotheses of this investigation:

1. **The Heavy-Traffic Law of Volatility ($H_1$)**: Under **EQ-01**, **EQ-02**, and **EQ-03**, queue length and passenger delay blowouts scale quadratically with arrival volatility ($C_a^2$) rather than mean volume. This mathematical reality proves why static volume models collapse during flight bank peaks, whereas volatility-informed models maintain queuing stability.
2. **Resolution of the Hub Disconnect**: **EQ-06** resolves the classical transfer bypass paradox by deflating scheduled seats by the empirical DB1B connecting ratio, preventing connecting passengers who remain in sterile concourses from artificially inflating landside passenger demand forecasts.
3. **Asymmetric Operational Trade-Offs**: **EQ-12** (RMSE), **EQ-13** (MAE), **EQ-14** (Bias), and **EQ-15** (MASE) establish the rigorous multi-dimensional evaluation grid proving Hypothesis 1 ($H_1$):
   - **Dimension 1 (Robustness)**: Model 3 achieves lowest RMSE ($222.1$ pax/hr, **EQ-12**); Model 2 wins Routine Pareto Efficiency ($\text{MASE} = 0.680\text{--}0.700$, **EQ-15**).
   - **Dimension 2 (Resilience)**: Model 3 decisively dominates irregular operations ($R_{\text{MASE}} = 1.05, \text{TTR} = 2.8$h) through live prior-hour recursive error innovation feedback ($e_{t-1} = y_{t-1} - \hat{y}_{t-1}$).
   - **Dimension 3 (Generalizability)**: Model 1 wins zero-shot spatial transfer without retraining ($\text{RTR} = 1.04, \Delta\text{MASE} = +4.0\%$) because deterministic schedule convolution (**EQ-07**) is layout-invariant.
4. **Econometric Verification**: **EQ-16** (Diebold-Mariano test) confirms that error reductions achieved by Model 2 ($DM = 42.15, p < 0.0001$) and Model 3 ($DM = 48.72, p < 0.0001$) over Model 1 are statistically significant after Newey-West HAC serial correlation adjustments.
5. **Actionable Checkpoint Staffing**: **EQ-20** bridges predictive modeling with floor operations, demonstrating that dimensioning physical screening lanes with a volatility buffer ($z_q \cdot \hat{\sigma}_{\text{TSA}, t}$) prevents catastrophic queue wait-time escalation.

---

*Document certified compliant with APA Style (7th ed.), authentic commercial aviation operations nomenclature, and ERU MSAA standards.*