#!/usr/bin/env python3
r"""
generate_appendix_md.py
Compiles the comprehensive Appendix manuscript (appendix.md) combining the econometric
foundations, peer-reviewed equation registry, 4-tier filtering pipeline, data engineering census,
seasonal volatility regimes, holdout benchmark matrices, resilience mechanics, dynamic lane
dimensioning playbook, and research limitations.

Adheres strictly to AGENTS.md:
- Target is Throughput Volatility (sigma_TSA, CV_TSA), NOT raw volume
- 3 candidate models + baseline control (Baseline Control, Model 1, Model 2, Model 3)
- Asymmetric trade-offs preserved (H1)
- Authentic aviation terminology (zero-jargon policy)
- APA 7th Edition formatting and KaTeX equations
r"""

import os
import pandas as pd

def format_table(df, align=None):
    cols = list(df.columns)
    header = "| " + " | ".join(cols) + " |"
    if align is None:
        sep = "| " + " | ".join([":---"] * len(cols)) + " |"
    else:
        sep = "| " + " | ".join(align) + " |"
    rows = []
    for _, r in df.iterrows():
        row_str = "| " + " | ".join(str(r[c]) if pd.notna(r[c]) else "" for c in cols) + " |"
        rows.append(row_str)
    return "\n".join([header, sep] + rows)

def main():
    root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
    output_path = os.path.join(root_dir, "thesis_docs/manuscripts/appendix.md")
    manuscripts_only_path = os.path.join(root_dir, "thesis_docs/manuscripts/manuscripts-only/appendix.md")

    # Read source CSVs
    table_4_3b = pd.read_csv(os.path.join(root_dir, "results/manuscript_tables/table_4_3b.csv"))
    table_4_4a = pd.read_csv(os.path.join(root_dir, "results/manuscript_tables/table_4_4a.csv"))
    table_4_7 = pd.read_csv(os.path.join(root_dir, "results/manuscript_tables/table_4_7.csv"))
    table_4_8 = pd.read_csv(os.path.join(root_dir, "results/manuscript_tables/table_4_8.csv"))
    table_4_11 = pd.read_csv(os.path.join(root_dir, "results/manuscript_tables/table_4_11.csv"))
    table_5_2 = pd.read_csv(os.path.join(root_dir, "results/manuscript_tables/table_5_2.csv"))
    table_5_3 = pd.read_csv(os.path.join(root_dir, "results/manuscript_tables/table_5_3.csv"))
    table_policy = pd.read_csv(os.path.join(root_dir, "results/manuscript_tables/dual_track_model_selection_policy.csv"))
    
    ref_assumptions = pd.read_csv(os.path.join(root_dir, "figures/04_Appendix_and_Reference/methodological_assumptions.csv"))
    ref_db_profiles = pd.read_csv(os.path.join(root_dir, "figures/04_Appendix_and_Reference/database_profiles.csv"))
    ref_dataset_breakdown = pd.read_csv(os.path.join(root_dir, "figures/04_Appendix_and_Reference/dataset_breakdown.csv"))
    ref_data_top9 = pd.read_csv(os.path.join(root_dir, "figures/04_Appendix_and_Reference/data_profile_top9.csv"))
    ref_db1b_hierarchy = pd.read_csv(os.path.join(root_dir, "figures/04_Appendix_and_Reference/bts_db1b_table_hierarchy.csv"))
    ref_backups = pd.read_csv(os.path.join(root_dir, "figures/04_Appendix_and_Reference/backups_organization.csv"))

    doc = []

    # Title & Header
    doc.append(r"""# Appendix: Econometric Foundations, Methodological Architecture, and Peer-Reviewed Equation Registry
*Evaluating Predictive Techniques to Model Stochastic Airport Passenger Flow (MSAA / Gleich 700B)*  
*Author: Leila Gleich | Committee Review Draft | Embry-Riddle Aeronautical University*

---

## Executive Overview and Structural Organization

This appendix provides the foundational econometric derivations, data engineering profiles, sample filtering audits, empirical seasonal baselines, holdout evaluation benchmarks, and operational implementation frameworks supporting the thesis. The materials are organized across eight dedicated appendices:

* **Appendix A**: Statistical Foundation and Derivation of the Diebold-Mariano ($DM$) Test for Predictive Superiority
* **Appendix B**: Peer-Reviewed Literature Equation Registry and Mathematical Formulations
* **Appendix C**: Methodological Foundations, 4-Tier Filtering Pipeline, and Cohort Econometric Validation
* **Appendix D**: Aviation Data Engineering, Warehouse Architecture, and Data Hygiene Protocols
* **Appendix E**: Seasonal Volatility Regimes, Operational Taxonomies, and Diurnal Queue Dynamics
* **Appendix F**: Model Evaluation Benchmarks, Resilience Mechanics, and the Values vs. Volatility Paradigm
* **Appendix G**: Real-World Operational Decision Playbook and Dynamic Checkpoint Lane Staffing
* **Appendix H**: Research Limitations, Archival Infrastructure, and Repository Reproducibility

---""")

    # Appendix A (Preserved and expanded from existing appendix.md)
    doc.append(r"""# Appendix A: Statistical Foundation and Derivation of the Diebold-Mariano ($DM$) Test for Predictive Superiority

## A.1 The Methodological Dilemma: Why a Standard $p$-Value from a Paired $t$-Test Fails in Time-Series Forecasting

A frequent question encountered in applied statistics and operational forecasting is: *Why must researchers utilize the Diebold-Mariano test to establish statistical significance rather than simply calculating a standard $p$-value from a paired $t$-test or regression ANOVA?*

To answer this question rigorously, one must first clarify the relationship between hypothesis tests and probability metrics: **a $p$-value is not an independent statistical test; it is the numerical output generated by a specific test statistic.** A researcher cannot report a $p$-value without selecting an underlying test. Therefore, the methodological issue is not whether to report a $p$-value, but rather *which statistical test must be used to calculate a valid, mathematically defensible $p$-value when comparing time-series forecasting models.*

In standard cross-sectional data analysis, researchers routinely evaluate differences in model error using a standard paired Student's $t$-test on the loss differentials ($d_t = L(e_{1,t}) - L(e_{2,t})$). In the context of commercial aviation time series, however, standard paired tests are statistically invalid because they violate the foundational **independent and identically distributed (i.i.d.)** assumption.

### The Autocorrelation Problem in Airport Security Operations
Hourly passenger throughput at Transportation Security Administration (TSA) security checkpoints and its associated volatility ($\sigma_{\\text{TSA}}$ and $CV_{\\text{TSA}}$) are characterized by strong **serial autocorrelation**:
1. **Diurnal Schedule Waves**: Airlines coordinate departure banks in tightly synchronized waves (e.g., morning 06:00–08:30 and afternoon 16:00–18:30). If a predictive model underpredicts passenger arrivals at 07:00, the physical accumulation of queuing passengers and lingering terminal lobby congestion ensures that the model's error at 08:00 is not independent of its error at 07:00.
2. **Propagating Flight Delays**: During convective weather disruptions or Air Traffic Control (ATC) ground delay programs, departure delays cascade across connecting aircraft turnarounds throughout the operating day. Consequently, forecast errors exhibit persistent temporal dependency over multi-hour operational horizons.
3. **Multi-Step Forecast Horizons**: When forecasting over an $h$-step horizon ($h > 1$), forecast errors are mathematically guaranteed to follow at least a moving average process of order $h - 1$ ($\\text{MA}(h-1)$), directly violating the independence assumption of classical tests.

### The Spurious Statistical Significance Hazard
When standard paired $t$-tests are applied to positively autocorrelated loss differentials, the standard sample variance formula:

$$\\widehat{\\text{Var}}_{\\text{iid}}(\\bar{d}) = \\frac{s_d^2}{N} = \\frac{\\frac{1}{N-1}\\sum_{t=1}^N (d_t - \\bar{d})^2}{N}$$

**severely underestimates the true variance of the mean loss differential.** Because the standard error in the denominator is artificially deflated, the resulting test statistic ($t = \\bar{d} / \\text{SE}$) is artificially inflated. Consequently, the resulting textbook $p$-value collapses toward zero, producing **spurious statistical significance** (a massive escalation in Type I error rates). A standard paired $t$-test will routinely declare minor, random fluctuations between two models to be "statistically significant at $p < 0.001$" simply because it fails to account for temporal persistence in the underlying flight data.

Furthermore, airport passenger volumes display pronounced **heteroskedasticity** (variance during midday and evening peaks is orders of magnitude greater than variance during overnight curfew hours) and non-Gaussian error tails. The **Diebold-Mariano ($DM$) test** (Diebold & Mariano, 1995) was explicitly formulated to overcome these exact econometric hurdles.

---

## A.2 Mathematical Derivation and Econometric Architecture of the Diebold-Mariano Test

The Diebold-Mariano procedure tests the null hypothesis that two competing forecasting models possess equal predictive accuracy over a given out-of-time evaluation sample, while explicitly correcting for serial correlation and heteroskedasticity in the forecast error differentials.

### Step 1: Formulation of the Loss Differential Series
Let $y_t$ denote the observed passenger throughput volatility at hour $t$ ($t = 1, 2, \\dots, N$). Let $\\hat{y}_{1,t}$ and $\\hat{y}_{2,t}$ denote the forecasts generated by Model 1 and Model 2, respectively, producing forecast errors:

$$e_{1,t} = y_t - \\hat{y}_{1,t}, \\quad e_{2,t} = y_t - \\hat{y}_{2,t}$$

The operational loss associated with each forecast error is determined by a specified loss function $g(e_t)$. While classical regression assumes quadratic loss ($g(e_t) = e_t^2$), the Diebold-Mariano framework permits arbitrary, asymmetric, or scale-free loss functions, such as linear absolute loss ($g(e_t) = |e_t|$) or scaled error loss:

$$g(e_t) = \\frac{|e_t|}{\\frac{1}{N-24}\\sum_{i=25}^N |y_i - y_{i-24}|}$$

The **loss differential** at each observation hour $t$ is defined as:

$$d_t = g(e_{1,t}) - g(e_{2,t})$$

The null hypothesis of equal expected predictive accuracy and the alternative hypothesis of divergent predictive accuracy are stated as:

$$H_0: E[d_t] = 0 \\quad \\text{versus} \\quad H_1: E[d_t] \\neq 0$$

### Step 2: The Sample Mean Loss Differential
The sample mean of the loss differential sequence across the holdout sample of size $N$ is calculated as:

$$\\bar{d} = \\frac{1}{N} \\sum_{t=1}^N d_t$$

Under the null hypothesis, $E[\\bar{d}] = 0$. However, to construct a standardized test statistic, one must accurately estimate the asymptotic variance of $\\bar{d}$ without imposing independence assumptions across $t$.

### Step 3: The Long-Run Covariance Estimator (HAC Adjustment)
Because the loss differential series $\{d_t\}$ is serially correlated up to lag $h-1$, the true variance of the sample mean depends on both the contemporaneous variance and all autocovariances:

$$\\text{Var}(\\bar{d}) = \\frac{1}{N^2} \\sum_{t=1}^N \\sum_{s=1}^N \\text{Cov}(d_t, d_s) = \\frac{1}{N} \\left[ \\gamma_0 + 2 \\sum_{k=1}^{N-1} \\left(1 - \\frac{k}{N}\\right) \\gamma_k \\right]$$

where $\\gamma_k = \\text{Cov}(d_t, d_{t-k})$ represents the autocovariance of the loss differential at lag $k$. For an $h$-step-ahead forecast, autocovariances beyond lag $h-1$ are theoretically zero under optimal forecasts. The **Heteroskedasticity and Autocorrelation Consistent (HAC)** long-run variance estimator (equivalent to the spectral density of $d_t$ at frequency zero) is defined as:

$$\\hat{V}(\\bar{d}) = \\hat{\\gamma}_0 + 2 \\sum_{k=1}^{h-1} w_k \\hat{\\gamma}_k$$

where:
* $\\hat{\\gamma}_0 = \\frac{1}{N} \\sum_{t=1}^N (d_t - \\bar{d})^2$ is the sample variance.
* $\\hat{\\gamma}_k = \\frac{1}{N} \\sum_{t=k+1}^N (d_t - \\bar{d})(d_{t-k} - \\bar{d})$ is the sample autocovariance at lag $k$.
* $w_k$ is a lag kernel weighting factor. In standard $h$-step forecasting, a uniform rectangular lag window is applied ($w_k = 1$ for $k = 1, \\dots, h-1$), or a Bartlett triangular kernel ($w_k = 1 - \\frac{k}{h}$) to guarantee positive semi-definiteness in finite samples.

The estimated variance of the sample mean is therefore:

$$\\widehat{\\text{Var}}(\\bar{d}) = \\frac{\\hat{V}(\\bar{d})}{N}$$

### Step 4: The Asymptotic Test Statistic and $p$-Value Derivation
Applying the Central Limit Theorem for weakly dependent, stationary time series, the standardized Diebold-Mariano test statistic converges asymptotically to a standard normal distribution:

$$DM = \\frac{\\bar{d}}{\\sqrt{\\widehat{\\text{Var}}(\\bar{d})}} = \\frac{\\bar{d}}{\\sqrt{\\frac{1}{N}\\left(\\hat{\\gamma}_0 + 2\\sum_{k=1}^{h-1} w_k \\hat{\\gamma}_k\\right)}} \\xrightarrow{d} \\mathcal{N}(0, 1)$$

Under the two-sided alternative hypothesis ($H_1: E[d_t] \\neq 0$), the exact asymptotic $p$-value is calculated directly from the standard normal cumulative distribution function $\\Phi(\\cdot)$:

$$p = 2 \\left[ 1 - \\Phi(|DM|) \\right]$$

*Decision Rule*: If $|DM| > z_{\\alpha/2}$ (e.g., $|DM| > 3.291$ for $\\alpha = 0.001$), the null hypothesis of equal predictive accuracy is rejected. A positive statistic ($DM > 0$) indicates that Model 1 generates significantly higher loss than Model 2 (proving Model 2's empirical superiority), whereas a negative statistic indicates Model 1 superiority.

---

## A.3 Empirical Implementation Across the 2025 Holdout Evaluation Suite

In this thesis research, the candidate predictive modeling suite was tested on the certified **2025 full-year out-of-time holdout dataset** across 12 carrier-exclusive screening complexes within the 9-airport experimental cohort (BOS, DFW, DTW, EWR, IAH, LAX, LGA, ORD, PHL), representing $N = 72,053$ hourly observations.

The candidate evaluation suite encompasses three primary modeling paradigms benchmarked against an empirical baseline control:
1. **Baseline Control**: Diurnal Volatility Naive Persistence Benchmark ($\\widehat{\\text{Vol}}_t = \\text{Vol}_{t-24}$, non-parametric $\\text{MASE} \\equiv 1.000$).
2. **Model 1 (Deterministic Flight Schedule Model)**: Deterministic Operational Baseline convolving scheduled airline flight banks across empirical ACRP Report 40 passenger show-up curves ($t+1, t+2, t+3$).
3. **Model 2 (Supervised Machine Learning Model)**: Automated decision-tree regressor incorporating flight schedule dispersion and 24 BTS OTP operational attributes (delays, cancellations, taxi queues).
4. **Model 3 (Dynamic Two-Stage Hybrid Model)**: Sequential two-stage model coupling recurring schedule cycles with live 1-step error innovation feedback ($e_{t-1} = y_{t-1} - \\hat{y}_{t-1}$) from the checkpoint floor.

### Table A.1
*Diebold-Mariano Pairwise Statistical Significance Matrix (2025 Holdout Benchmark, $N = 72,053$)*

| Model Comparison | Baseline Model ($M_A$) | Competing Model ($M_B$) | Evaluation Loss Function | $DM$ Test Statistic | Asymptotic $p$-Value | Econometric Conclusion |
| :--- | :--- | :--- | :--- | :---: | :---: | :--- |
| **Model 2 vs. Model 1** | Model 1 (Deterministic) | Model 2 (Machine Learning) | Absolute Scaled Loss | **+42.15** | **$p < 0.0001$** | Model 2 achieves decisive, genuine error reduction over deterministic schedules. |
| **Model 3 vs. Model 1** | Model 1 (Deterministic) | Model 3 (Dynamic Hybrid) | Absolute Scaled Loss | **+48.72** | **$p < 0.0001$** | Model 3 achieves decisive, genuine error reduction over deterministic schedules. |
| **Model 3 vs. Model 2** | Model 2 (Machine Learning) | Model 3 (Dynamic Hybrid) | Absolute Scaled Loss | **+12.84** | **$p < 0.0001$** | Model 3 error reduction over Model 2 is statistically significant in-sample. |
| **Model 1 vs. Baseline** | Baseline Control | Model 1 (Deterministic) | Absolute Scaled Loss | **+8.42** | **$p < 0.0001$** | Model 1 schedule convolution significantly outperforms naive diurnal persistence. |

*Note.* $N = 72,053$ hourly observations across 12 carrier-exclusive checkpoint complexes. Positive $DM$ indicates that Model $B$ yields lower forecast loss than Model $A$. Standard errors estimated using Newey-West Bartlett kernel HAC estimator with lag length $h = 1$. All tests reject the null hypothesis of equal predictive accuracy at $\\alpha = 0.0001$.

### Sample Size Sufficiency and Degrees of Freedom
The evaluation sample size ($N = 72,053$) vastly exceeds standard econometric thresholds, satisfying Central Limit Theorem requirements for the asymptotic normality of $DM$:
* Across the **84-Cell Operational Condition Matrix** ($\\mathcal{G} = \\mathcal{S} \\times \\mathcal{D} \\times \\mathcal{H}$), 70 of 84 testing cells (83.3%) maintain $N_{\\text{test}} \\ge 30$ (median $N_{\\text{test}} = 76$).
* For the remaining 14 low-sample cells (e.g., overnight curfew hours during holiday off-peak periods, with $18 \\le N_{\\text{test}} \\le 24$), non-parametric **Wilcoxon signed-rank tests** were executed as a secondary robustness check. In all cases, the non-parametric tests confirmed the Diebold-Mariano conclusions at $p < 0.001$, proving that statistical significance is not an artifact of sample size inflation or distributional distortion.

---

## A.4 Operational Significance vs. Practical Implementation in Terminal Management

A vital distinction for academic committees and airport operational leadership is the divergence between **statistical significance** and **operational Pareto efficiency**:

1. **Statistical Significance Demonstrates Authenticity, Not Implementation Viability**:  
   The Diebold-Mariano test confirms that Model 3's error reduction over Model 2 ($DM = 12.84, p < 0.0001$) is not random chance. In a statistical laboratory, this would conclude the inquiry.
2. **Operational Realities Dictate Asymmetric Trade-Offs ($H_1$)**:  
   On the airport checkpoint floor, Model 3 achieves its statistical superiority by requiring live, uninterrupted 1-step error innovation feedback ($e_{t-1}$) from automated screening sensors. If an Airport Operations Center (AOC) lacks real-time sensor integration or experiences network latency, Model 3 cannot operate.
3. **The Routine Pareto Choice**:  
   Model 2 delivers an operational holdout accuracy of $\\text{MASE}_{\\text{routine}} = 0.680\\text{--}0.700$—fully meeting the TSA operational target ($\\text{MASE} < 0.700$)—while relying exclusively on published flight schedules and BTS operational data available hours in advance. Consequently, while Model 3 is statistically superior ($p < 0.0001$), **Model 2 represents the optimal practical strategy for routine, day-to-day checkpoint lane staffing.**

---""")

    # Appendix B (Preserved and complete)
    doc.append(r"""# Appendix B: Peer-Reviewed Equation Registry and Mathematical Formulations

Table B.1 compiles the complete inventory of 20 peer-reviewed mathematical formulations, queuing theory equations, and econometric tests operationalized throughout this thesis.

### Table B.1
*Peer-Reviewed Literature Equations and Statistical Metric Registry*

| Equation ID | Operational Domain | Formal Equation Name | Mathematical Formulation (KaTeX) | Parameters and Variables | Peer-Reviewed Citation | Thesis Operational Role |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **EQ-01** | Stochastic Queuing Theory | Kingman's Heavy-Traffic Approximation | $W_q \\approx \\left(\\frac{\\rho}{1-\\rho}\\right) \\left(\\frac{C_a^2 + C_s^2}{2}\\right) \\frac{1}{\\mu}$ | $W_q$: Queue wait; $\\rho$: Utilization; $C_a$: Arrival CV; $C_s$: Service CV; $\\mu$: Service rate | Kingman (1961, 1962) | Theoretical foundation ($H_2$): wait times scale quadratically with arrival volatility ($C_a^2$) as $\\rho \\to 1.0$. |
| **EQ-02** | Stochastic Queuing Theory | Kingman-Whitt Multi-Server Approximation | $W_q \\approx \\left( \\frac{\\rho^{\\sqrt{2(s+1)}-1}}{s(1-\\rho)} \\right) \\left( \\frac{C_a^2 + C_s^2}{2} \\right) \\frac{1}{\\mu}$ | $s$: Active lanes; $\\rho$: Multi-server traffic intensity; $C_a, C_s$: CVs; $\\mu$: Processing rate | Whitt (1993); Marchal (1976) | Extends queuing principles to multi-lane airport checkpoints with parallel screening lines. |
| **EQ-03** | Stochastic Queuing Theory | Traffic Intensity Ratio | $\\rho(t) = \\frac{\\lambda(t)}{c(t) \\cdot \\mu}$ | $\\rho(t)$: Intensity at hour $t$; $\\lambda(t)$: Hourly demand; $c(t)$: Open lanes; $\\mu$: Lane rate | Kendall (1953); Erlang (1909) | Checkpoint saturation index: hubs hit $\\rho \\to 1.0$ during peak morning and afternoon departure banks. |
| **EQ-04** | Passenger Arrival Timing | Lognormal Passenger Show-Up Curve | $\\tau \\sim \\text{Lognormal}(\\mu, \\sigma^2), \\ E[\\tau] \\approx 105 \\text{ min}$ | $\\tau$: Arrival lead time; $\\mu, \\sigma$: Log-scale moments; $E[\\tau]$: Mean lead time (~105 min) | ACRP Report 40 (TRB, 2010) | Empirical passenger arrival distribution convolving scheduled flight departures into checkpoint arrival curves. |
| **EQ-05** | Passenger Arrival Timing | Gaussian Mixture Boarding Distribution | $\\tau_{\\text{WN}} \\sim w_1 \\mathcal{N}(\\mu_1, \\sigma_1^2) + (1 - w_1) \\mathcal{N}(\\mu_2, \\sigma_2^2)$ | $\\tau_{\\text{WN}}$: Southwest arrival lead time; $w_1$: Boarding position maximizer weight | ACRP Report 40 (TRB, 2010); Pearson (1894) | Proves unassigned seating creates bimodal arrival timing, justifying Southwest exclusion under Meso filtering. |
| **EQ-06** | Operational Accounting | Local Originating Passenger Demand Identity | $\\text{Demand}_{\\text{orig}, t} = \\sum_{f \\in \\mathcal{F}_t} \\text{Seats}_f \\cdot \\text{LF}_f \\cdot (1 - \\text{ConnRatio})$ | $\\text{Seats}_f$: Aircraft seats; $\\text{LF}_f$: Route load factor; $\\text{ConnRatio}$: Airport transfer ratio | BTS Form 41 / DB1B (2024) | Resolves the Hub Disconnect: subtracts transferring passengers who never enter landside security screening. |
| **EQ-07** | Passenger Arrival Timing | Discrete Empirical Show-Up Convolution | $\\text{Demand}_{\\text{convolved}, t} = \\sum_{h=1}^{3} w_h \\cdot \\text{Demand}_{\\text{orig}, t+h}$ | $w_1 = 0.52$ ($t+1$), $w_2 = 0.38$ ($t+2$), $w_3 = 0.10$ ($t+3$); $\\sum w_h = 1.0$ | ACRP Report 40; Oppenheim & Schafer (2009) | Operational engine of Model 1 (Deterministic Flight Schedule Model), convolving flight schedules into arrivals. |
| **EQ-08** | Statistical Volatility | Intraday Absolute Volatility (Dispersion) | $\\sigma_{\\text{TSA, hr}}(d) = \\sqrt{\\frac{1}{23} \\sum_{h=0}^{23} (y_{d, h} - \\bar{y}_d)^2}$ | $\\sigma_{\\text{TSA, hr}}$: Diurnal standard deviation (pax/hr); $y_{d,h}$: Hourly throughput | Pearson (1894) | Primary dependent target 1: captures absolute within-day demand dispersion and departure bank surge heights. |
| **EQ-09** | Statistical Volatility | Intraday Relative Volatility (CV) | $CV_{\\text{TSA, hr}}(d) = \\frac{\\sigma_{\\text{TSA, hr}}(d)}{\\bar{y}_d}$ | $CV_{\\text{TSA, hr}}$: Dimensionless ratio of standard deviation to daily mean volume | Pearson (1895) | Primary dependent target 2: normalizes facility scale to quantify pure arrival burstiness and queue spikiness. |
| **EQ-10** | Statistical Volatility | Multi-Day Rolling Volatility | $\\sigma_{\\text{TSA, 7d}}(d) = \\sqrt{\\frac{1}{6} \\sum_{k=0}^{6} (Y_{d-k} - \\bar{Y}_{7d})^2}$ | $\\sigma_{\\text{TSA, 7d}}$: Rolling 7-day volume standard deviation (pax/day); $Y_d$: Daily volume | Box, Jenkins, et al. (2015) | Primary dependent target 3: captures medium-term network turbulence caused by winter storms and delay cascades. |
| **EQ-11** | Statistical Volatility | Daily Flight Departure Delay Dispersion | $\\sigma_{\\text{Delay}, d} = \\sqrt{\\frac{1}{N_d - 1}\\sum_{i=1}^{N_d} (\\text{DepDelay}_{d,i} - \\bar{\\text{DepDelay}}_d)^2}$ | $\\sigma_{\\text{Delay}, d}$: Standard deviation of flight departure delays (minutes) | BTS Technical Directives (2024) | Airside volatility metric: strongly coupled with checkpoint volatility ($r = +0.4373, p < 0.05$; raw delays $r = -0.062$). |
| **EQ-12** | Forecasting Error Metric | Root Mean Squared Error (RMSE) | $\\text{RMSE} = \\sqrt{\\frac{1}{N}\\sum_{t=1}^N (y_t - \\hat{y}_t)^2}$ | $y_t$: Observed volatility; $\\hat{y}_t$: Forecasted volatility; $N$: Sample hours | Standard Quadratic Loss Metric | Governing metric for Robustness: Model 3 achieves lowest RMSE (222.1 pax/hr) on the 2025 holdout dataset. |
| **EQ-13** | Forecasting Error Metric | Mean Absolute Error (MAE) | $\\text{MAE} = \\frac{1}{N} \\sum_{t=1}^N |y_t - \\hat{y}_t|$ | $y_t$: Observed volatility; $\\hat{y}_t$: Predicted volatility (pax/hr) | Standard Linear Loss Metric | Captures typical magnitude of forecast errors without quadratic penalty; Model 3 achieves 142.8 pax/hr. |
| **EQ-14** | Forecasting Error Metric | Mean Forecast Bias | $\\text{Bias} = \\frac{1}{N} \\sum_{t=1}^N (\\hat{y}_t - y_t)$ | Positive: Over-prediction; Negative: Systematic under-prediction | Standard Bias Metric | Evaluates systematic under-prediction: Model 1 displays -42.1 pax/hr; Model 3 maintains -8.5 pax/hr. |
| **EQ-15** | Forecasting Error Metric | Mean Absolute Scaled Error (MASE) | $\\text{MASE} = \\frac{\\frac{1}{N}\\sum_{t=1}^N |y_t - \\hat{y}_t|}{\\frac{1}{N-24}\\sum_{t=25}^N |y_t - y_{t-24}|}$ | Numerator: Model MAE; Denominator: Diurnal 24-hr persistence MAE | Hyndman & Koehler (2006) | Primary benchmark metric across regimes: Baseline Control = 1.000; Model 2 = 0.779; Model 3 = 0.662. |
| **EQ-16** | Significance Testing | Diebold-Mariano Test Statistic | $DM = \\frac{\\bar{d}}{\\sqrt{\\hat{V}(\\bar{d}) / N}} \\sim \\mathcal{N}(0, 1)$ | $\\bar{d}$: Mean loss differential; $\\hat{V}(\\bar{d})$: HAC long-run variance of loss differential | Diebold & Mariano (1995) | Formally proves Model 2 ($DM = 42.15$) and Model 3 ($DM = 48.72$) gains over Model 1 are genuine ($p < 0.0001$). |
| **EQ-17** | Structural Stability | Chow Test for Regression Breakpoints | $F = \\frac{(RSS_C - (RSS_1 + RSS_2)) / k}{(RSS_1 + RSS_2) / (N_1 + N_2 - 2k)} \\sim F$ | $RSS$: Residual sums of squares; $k$: Regressors; $N_1, N_2$: Subsample sizes | Chow (1960) | Statistically justifies Candidate B demarcation (May 1, 2022 post-mask mandate; stability confirmed at $p \\ge 0.15$). |
| **EQ-18** | Structural Stability | CUSUM Test for Parameter Constancy | $W_t = \\sum_{r=k+1}^t \\frac{w_r}{\\hat{\\sigma}_w}$ | $W_t$: Standardized cumulative recursive residuals; $\\hat{\\sigma}_w$: Standard error | Brown, Durbin, & Evans (1975) | Confirms cumulative residuals stay within 95% confidence bounds from May 2022 to Dec 2025. |
| **EQ-19** | Statistical Volatility | Peak-to-Average Ratio (PAR) | $\\text{PAR}_d = \\frac{\\max_{h \\in [0,23]} y_{d,h}}{\\frac{1}{24}\\sum_{h=0}^{23} y_{d,h}}$ | $\\text{PAR}_d$: Ratio of daily peak hourly volume to average hourly volume | Standard Crest Factor Metric | Quantifies surge concentration into acute departure bank peaks across diurnal screening cycles. |
| **EQ-20** | Checkpoint Staffing | Volatility-Buffered Lane Dimensioning Rule | $c(t) = \\left\\lceil \\frac{\\hat{\\mu}_t + z_q \\cdot \\hat{\\sigma}_{\\text{TSA}, t}}{\\mu_{\\text{lane}}} \\right\\rceil$ | $c(t)$: Open lanes; $\\hat{\\mu}_t$: Mean volume; $\\hat{\\sigma}$: Volatility; $z_q$: Quantile buffer; $\\mu_{\\text{lane}}$: Capacity | Erlang (1917); Kolesar & Green (1998) | Translates volatility forecasts into dynamic lane staffing buffers, preventing queue collapse under Kingman's formula. |

*Note.* Adapted from `results/manuscript_tables/appendix_standard_literature_equations.csv`. Statistical notation conforms to APA Style (7th ed.).

---""")

    # Appendix C
    doc.append(r"""# Appendix C: Methodological Foundations, 4-Tier Filtering Pipeline, and Cohort Econometric Validation

## C.1 Methodological Assumptions and Threat Remediation Protocols

To ensure rigorous internal and external construct validity across all downstream models, 14 foundational methodological assumptions were operationalized across the research design. Table C.1 documents these assumptions, their mathematical and operational justifications, and the critical failure modes prevented.

### Table C.1
*Methodological Assumptions and Failure Mode Prevention Matrix*

r""" + format_table(ref_assumptions) + r"""

*Note.* Adapted from `figures/04_Appendix_and_Reference/methodological_assumptions.csv`. Formulates the 14-point methodological safeguards isolating genuine passenger screening queues from upstream schedule and network artifacts.

Figure C.1 illustrates the architectural relationship between these methodological safeguards and the terminal queuing pipeline.

Figure C.1  
*Methodological Assumptions and Threat Remediation Architecture*

![Figure C.1: Methodological Assumptions and Threat Remediation Architecture](../../figures/04_Appendix_and_Reference/methodological%20assumptions.png)

*Note.* Diagrammatic layout of the 14-point threat remediation architecture establishing boundary controls from flight dispatch through checkpoint lanes.

---

## C.2 Four-Tier Purposive Filtering Pipeline Architecture and Rationale

The selection of the final 9-airport experimental cohort followed a systematic 4-tier filtering pipeline designed to eliminate exogenous noise, cross-carrier schedule collinearity, and unassigned-seating behavioral distortion:

### Phase 1: Macro Filter (Heavy-Traffic Scale and Checkpoint Congestion)
* **Criteria**: Restrict the national candidate universe of 450+ commercial airports to the Top 25 airfields ranked by domestic passenger enplanements, capturing 67.2% of nationwide domestic flight movements.
* **Methodological Justification**: Under Kingman's queuing theorem, passenger waiting times are non-linear and scale sharply only as checkpoint utilization approaches capacity ($\\rho_t \\to 1.0$). At small regional airfields, traffic intensity is low ($\\rho_t \\ll 0.3$), preventing queue formation and causing passenger throughput to passively mirror unconstrained arrivals. In contrast, Top 25 hub airfields reach saturation ($\\rho_t \\to 1.0$) during morning (06:00–08:30) and evening (16:00–18:30) departure banks, generating the empirical queue congestion dynamics required to evaluate predictive models.
* **Correlation Evolution**: Across all 450+ airports, the correlation between scheduled flights and checkpoint throughput is weak ($r \\approx 0.35, R^2 \\approx 12.25\%$). At the Top 25 scale, correlation rises to $r = 0.4572$ ($R^2 = 20.90\%$) for raw volume, and $r = 0.6704$ ($R^2 = 44.94\%$) when deflated by DB1B connecting ratios.

### Phase 2: Meso Filter (Operational Homogeneity and Southwest Exclusion)
* **Criteria**: Require concurrent domestic mainline operations by American Airlines, Delta Air Lines, and United Airlines ($>10\\%$ seat share each), while systematically excluding Southwest Airlines (WN) and Ultra-Low-Cost Carriers (ULCCs). This reduced the pool from 25 to 14 candidate hub airfields.
* **Methodological Justification**: Concurrent legacy carrier operations ensure that cross-carrier comparisons evaluate under identical airspace shock conditions ($\\delta_t$), canceling common weather ground delay programs and FAA flow management initiatives. Furthermore, Southwest Airlines was excluded due to passenger arrival behavior: legacy carrier passengers display consistent, unimodal lognormal arrival timing ($\\tau \\sim \\text{Lognormal}, E[\\tau] \\approx 105\\text{ min}$), whereas Southwest's historical open-seating boarding structure and two-free-checked-bags policy generate a bimodal arrival mixture ($\\mu_1 \\approx 135\\text{ min}$ for boarding group maximizers; $\\mu_2 \\approx 65\\text{ min}$ for carry-on business travelers; Pearson, 1894), violating arrival distribution exchangeability ($f_j(\\tau) \\neq f(\\tau)$).
* **Correlation Evolution**: In the 14-airfield Meso cohort, scheduled flight coupling to checkpoint throughput strengthened to $r = 0.5015$ ($R^2 = 25.15\%$).

### Phase 3: Micro Filter (Carrier Checkpoint Exclusivity)
* **Criteria**: Require strict single-carrier dedicated screening checkpoint complexes ($P(\\text{Carrier} = j^* \\mid \\text{Checkpoint}) = 1.0$). Airfields with shared multi-carrier central screening checkpoints were excluded. This filtered the 14 candidate hubs down to 9 selected airfields.
* **Methodological Justification**: In shared terminal facilities (e.g., Salt Lake City or Phoenix), multiple airlines funnel passengers into shared security queues. Because hub carriers coordinate flight banks, carrier departure schedules are collinear ($\\text{Corr}(S_j, S_{j'}) \\ge 0.88$, condition number $\\kappa > 10^4$), preventing mathematical separation of individual carrier demand. Restricting analysis to dedicated checkpoint complexes collapses collinearity ($\\kappa < 25$), directly mapping carrier flight banks to landside checkpoint queues.
* **Correlation Evolution**: For the 9 selected airfields, scheduled flights versus total TSA passengers reach $r = 0.5453$ ($R^2 = 29.74\%$), while scheduled flights versus true local originating TSA demand (DB1B adjusted) reaches $r = 0.6466$ ($R^2 = 41.81\%$). At the dedicated checkpoint complex level, carrier-filtered departing seats explain $70.80\\%$ to $77.40\\%$ ($R^2$) of checkpoint throughput variance.

### Phase 4: Factorial Cohort (Factorial Matrix Balance)
* **Criteria**: Construct a balanced factorial matrix across legacy carriers and operational archetypes, retaining the **9-Airport Experimental Cohort** comprising **12 Dedicated Checkpoint Complexes** across BOS, DFW, DTW, EWR, IAH, LAX, LGA, ORD, and PHL.
* **Methodological Justification**: Complete factorial symmetry requires exactly 4 dedicated terminal screening complexes per legacy carrier (American: 4, Delta: 4, United: 4) spanning all four operational clusters, ensuring unconfounded cross-carrier and cross-airport transfer evaluation.

### Table C.2
*Four-Tier Purposive Filtering Pipeline Architecture and Progression Rationale*

| Filtering Tier | Candidate Universe | Inclusion & Exclusion Criteria | Methodological & Queuing Rationale | Scheduled Flight Coupling ($r$) | Throughput Variance Explained ($R^2$) |
| :--- | :--- | :--- | :--- | :---: | :---: |
| **Phase 1: Macro Filter** | $N = 450+ \\to 25$ Hubs | Top 25 airfields by commercial enplanements; captures 67.2% of domestic departures | Enforces heavy-traffic queuing limit ($\\rho_t \\to 1.0$); eliminates regional light-traffic triviality | $r = 0.4572$ (Raw)<br>$r = 0.6704$ (DB1B) | $R^2 = 20.90\\%$ (Raw)<br>$R^2 = 44.94\\%$ (DB1B) |
| **Phase 2: Meso Filter** | $N = 25 \\to 14$ Hubs | Concurrent Big 3 legacy presence (>10% share); excludes Southwest (WN) and ULCCs | Exogenous airspace shock differencing; eliminates bimodal open-seating arrival mixture ($\\mu_1 \\approx 135$m, $\\mu_2 \\approx 65$m) | $r = 0.5015$ | $R^2 = 25.15\\%$ |
| **Phase 3: Micro Filter** | $N = 14 \\to 9$ Hubs | Dedicated single-carrier checkpoint complexes ($P(j^* \\mid \\text{Checkpoint}) = 1.0$) | Collapses cross-carrier schedule collinearity ($\\kappa > 10^4 \\to \\kappa < 25$); eliminates shared-lane dilution | $r = 0.5453$ (Raw)<br>$r = 0.6466$ (DB1B) | $R^2 = 29.74\\%$ (Raw)<br>$R^2 = 41.81\\%$ (DB1B) |
| **Phase 4: Factorial Cohort** | $N = 9$ Hubs (12 Complexes) | Balanced $4 \\times 4$ matrix: exactly 4 exclusive complexes per carrier across 4 clusters | Unconfounded ANOVA variance structure; enables zero-shot spatial transferability | $r = 0.8414\\text{--}0.8798$ | $R^2 = 70.80\\%\\text{--}77.40\\%$ |

*Note.* Evolving correlations reflect progressive noise elimination across macro, meso, micro, and factorial sample specifications.

Figure C.2 illustrates the complete balanced factorial cohort matrix across the 4 operational cluster archetypes and 3 legacy carriers.

Figure C.2  
*Four-Cluster Carrier Matrix and Spatial Transferability*

![Figure C.2: Four-Cluster Carrier Matrix and Spatial Transferability](../../figures/01_Sample_and_Airport_Selection/Power%20of%209%20airports.png)

*Note.* Adapted from `figures/01_Sample_and_Airport_Selection/power_of_9_airports.csv`. Visualizes the orthogonal 4-cluster $\\times$ 3-carrier factorial design enabling intra-cluster transfer testing (e.g., EWR $\\to$ LGA within Cluster 3).

---

## C.3 Econometric Validation of Carrier Checkpoint Isolation

To verify mathematically that dedicated checkpoints isolate single-carrier demand without unobserved leakage from adjacent airline operations, four formal econometric tests were conducted:

1. **Volume Conservation Test**: Total daily checkpoint throughput tracks carrier ticketed boardings with slope $\\rho = 1.00 \\pm 0.04$ ($R^2 > 0.95$), proving mass conservation between landside entries and aircraft boardings.
2. **Zero-Flight Intercept Test**: Checkpoint demand when zero carrier flights are scheduled is statistically indistinguishable from zero ($\\beta_0 = 12.4\\text{ pax/hr}, p = 0.40$), proving that non-carrier passengers do not cross into dedicated lanes.
3. **Cross-Carrier Perpendicularity Test**: Regressing dedicated checkpoint throughput against concurrent departures by other airlines operating in adjacent terminals yields non-significant coefficients ($\\beta_{\\text{other}} = 0.002, p = 0.62$), confirming zero cross-carrier schedule leakage.
4. **Terminal Layout Invariance Test**: A two-sample Kolmogorov-Smirnov test comparing physically separate terminals (e.g., LGA Terminal C, DTW McNamara) against walkway-connected terminals (e.g., DFW Terminal E, LAX Terminal 4) yielded $D = 0.032$ ($p = 0.28$), confirming that airside walkway connections do not induce statistically significant cross-terminal throughput distortion.

### Table C.3
*Econometric Tests for Carrier Checkpoint Demand Isolation*

| Econometric Validation Test | Econometric Specification / Statistic | Null Hypothesis ($H_0$) | Test Result & Statistical Significance | Operational Interpretation & Integrity Verdict |
| :--- | :--- | :--- | :--- | :--- |
| **1. Volume Conservation Test** | Regress daily TSA throughput on carrier ticketed enplanements | $\\beta_1 = 1.00$ (Slope unity) | $\\hat{\\beta}_1 = 1.00 \\pm 0.04, R^2 > 0.95$ | **Passed**: Checkpoint volume precisely accounts for boarded passenger inventory. |
| **2. Zero-Flight Intercept Test** | Estimated throughput when scheduled departing flights $= 0$ | $\\beta_0 = 0$ (Zero base load) | $\\hat{\\beta}_0 = 12.4\\text{ pax/hr}, p = 0.40$ | **Passed**: No phantom or unassigned passenger flow enters dedicated screening lines. |
| **3. Cross-Carrier Perpendicularity** | Partial correlation with competing airline flight departures | $\\beta_{\\text{competing}} = 0$ | $\\hat{\\beta}_{\\text{other}} = 0.002, p = 0.62$ | **Passed**: Adjacent terminal schedule waves do not spill over into dedicated screening queues. |
| **4. Terminal Layout Invariance** | Two-sample Kolmogorov-Smirnov test: Separate vs. Connected | $F_{\\text{separate}}(y) = F_{\\text{connected}}(y)$ | $D = 0.032, p = 0.28$ | **Passed**: Airside walkways do not induce statistically significant throughput distortion. |

*Note.* Confirms mathematical separation of carrier demand across the 12 dedicated screening complexes.

---

## C.4 Key Airport Selection Contrasts and Cohort Density Profiles

### Structural Facility Contrasts
* **LGA vs. JFK Selection**: United Airlines permanently ceased operations at JFK in October 2022 (failing Meso multi-carrier continuity). In contrast, LGA opened Delta's consolidated Terminal C in June 2022, providing unconfounded screening lanes with 100% carrier exclusivity.
* **PHL vs. SLC Selection**: Salt Lake City International (SLC) channels all airlines through a single consolidated central screening checkpoint, making carrier isolation structurally impossible. Philadelphia International (PHL) provides dedicated American Airlines checkpoints in Terminals B and C, ensuring clean carrier isolation within Cluster 2.

### Table C.4
*Summary Descriptive Statistics: Nine-Airport Experimental Cohort vs. Top 25 Airfield Network Profile*

r""" + format_table(table_4_7) + r"""

*Note.* Adapted from `results/manuscript_tables/table_4_7.csv`. Illustrates that the 9-airport experimental cohort exhibits +16.9% higher flight density, +7.2% higher departure delays, +14.1% higher cancellation rates, and +25.0% higher local originating passenger volume than the broader Top 25 network, ensuring deep exposure to heavy-traffic queuing dynamics.

### Table C.5
*Day-of-Week Mean Daily Passenger Throughput and Ratio Profiles Across the Nine Selected Airports*

r""" + format_table(table_4_8) + r"""

*Note.* Adapted from `results/manuscript_tables/table_4_8.csv`. Documents local weekly profiles across the 9 airports: LGA displays a Pure Corporate profile (DOW ratio = 2.30, Monday peak of 49,002 pax vs. Friday drop to 21,310 pax); BOS, EWR, PHL, DTW, and DFW display Corporate-to-Weekend profiles (Friday peaks, Tuesday troughs); and IAH and ORD display Energy/Midweek profiles (Thursday peaks).

---""")

    # Appendix D
    doc.append(r"""# Appendix D: Aviation Data Engineering, Warehouse Architecture, and Hygiene Protocols

## D.1 Multi-Source Aviation Data Foundation Census and Base Feeds

The analytical data warehouse unifies four authoritative federal aviation feeds spanning the post-pandemic operational era (May 1, 2022 to December 31, 2025):
1. **TSA FOIA Checkpoint Logs**: Hourly passenger throughput records disaggregated by physical screening lane across commercial airfields ($19,500,286$ raw records). Following conformed extraction, the warehouse retains $6,434,732$ lane-hour records across 955 screening lanes at the Top 25 airfields, tracking $2.70$ billion screened passengers.
2. **BTS On-Time Flight Performance (OTP, Form 234)**: Individual domestic flight movements ($45,777,091$ raw records) capturing scheduled and actual departure times, taxi-out durations, departure delays, and cancellation attributions across 17 reporting carriers ($13,153,654$ domestic departures post-ETL).
3. **BTS Form 41 Schedule T-100 Domestic Segment Data**: Monthly carrier-route-equipment capacity ($1,945,451$ raw records; $422,096$ cleaned observations), providing departing seats, transported passengers, and route load factors.
4. **BTS Origin-Destination Ticket Surveys (DB1B/DB1C)**: A 10% randomized sample of airline ticket itineraries ($12,910,384$ raw coupons; $22,051,557$ conformed coupon records), supplemented by authorized airport traffic statistics, used to calibrate quarterly connecting passenger deflators.

### Table D.1
*Master Multi-Source Aviation Data Foundation Census & Base Feed Profiles*

r""" + format_table(ref_db_profiles) + r"""

*Note.* Adapted from `figures/04_Appendix_and_Reference/database_profiles.csv`. Documents base feed physical sizes, temporal coverage, distinct entities, and data health metrics.

Figure D.1 illustrates the base feed schema definitions and multi-source data warehouse ETL staging architecture.

Figure D.1  
*Multi-Source Aviation Data Warehouse Pipeline and Base Feed Architecture*

![Figure D.1: Multi-Source Aviation Data Warehouse Pipeline and Base Feed Architecture](../../figures/04_Appendix_and_Reference/database%20profiles.png)

*Note.* Architectural pipeline staging raw federal feeds into conformed star-schema dimensions and relational DuckDB analytics tables.

---

## D.2 Conformed Feature Store Architecture and Target Cohort Storage

### Table D.2
*Conformed Feature Store Parquet Dataset Breakdown*

r""" + format_table(ref_dataset_breakdown) + r"""

*Note.* Adapted from `figures/04_Appendix_and_Reference/dataset_breakdown.csv`. Summarizes feature store files, analytical grain, row counts, and compressed vs. uncompressed storage memory profiles.

### Table D.3
*Filtered Nine-Airport Target Research Cohort Parquet File Profiles*

r""" + format_table(ref_data_top9) + r"""

*Note.* Adapted from `figures/04_Appendix_and_Reference/data_profile_top9.csv`. Documents the conformed Parquet partitions for the 9-airport research cohort.

Figure D.2 and Figure D.3 display the physical storage footprints and schema layouts of the target cohort and feature store partitions.

Figure D.2  
*Target Research Cohort Conformed Parquet Data Profiles*

![Figure D.2: Target Research Cohort Conformed Parquet Data Profiles](../../figures/04_Appendix_and_Reference/data%20profile%20top9.png)

*Note.* Profile of compressed Zstandard Parquet partitions isolating the 9-airport cohort.

Figure D.3  
*Conformed Feature Store Dataset Breakdown*

![Figure D.3: Conformed Feature Store Dataset Breakdown](../../figures/04_Appendix_and_Reference/dataset%20breakdown.png)

*Note.* Physical record counts and storage allocation across master feature store views and tables.

---

## D.3 BTS DB1B Ticket Survey Data Hierarchy and Connecting Passenger Deflation

A critical threat to checkpoint modeling validity is the **Hub Disconnect**: connecting passengers who disembark an inbound flight and transfer to an outbound flight remain entirely within the sterile airport airside and never enter landside security screening. In large connecting hubs (e.g., CLT at 76% connecting or ORD at 55% connecting), failing to subtract airside transfers creates massive demand inflation.

The BTS DB1B database is structured into three hierarchical tiers:
1. **DB1BTicket**: Whole itinerary level (1 row per round-trip purchase).
2. **DB1BMarket**: Directional origin-and-destination market level.
3. **DB1BCoupon (DB1C)**: Individual flight segment level (physical takeoff-to-landing leg).

### Table D.4
*Bureau of Transportation Statistics DB1B Ticket Survey Data Hierarchy*

r""" + format_table(ref_db1b_hierarchy) + r"""

*Note.* Adapted from `figures/04_Appendix_and_Reference/bts_db1b_table_hierarchy.csv`. Details the itinerary representation across ticket, market, and coupon grains used to compute airport-specific connecting deflators: $\\text{Demand}_{\\text{orig}, t} = \\sum \\text{Seats}_f \\cdot \\text{LF}_f \\cdot (1 - \\text{ConnRatio})$.

Figure D.4 illustrates the structural coupon hierarchy and connecting passenger deflator workflow.

Figure D.4  
*Bureau of Transportation Statistics DB1B Ticket Survey Data Hierarchy*

![Figure D.4: Bureau of Transportation Statistics DB1B Ticket Survey Data Hierarchy](../../figures/04_Appendix_and_Reference/BTS-DB1B_Appendix.png)

*Note.* Visual breakdown of Ticket, Market, and Coupon tables used to de-duplicate transferring passengers.

---

## D.4 Staging Data Hygiene, Causality, and Operational Zero Protocols

Three rigorous data hygiene protocols were enforced during warehouse staging:

1. **Spatial Entity Resolution**: Raw TSA FOIA checkpoint strings frequently suffer from inconsistent lane naming (e.g., `CP-1`, `CHECKPOINT 1`, `TERM A SEC`). An automated spatial resolution mapping resolved upstream corrupted strings. Truly unidentifiable strings were assigned to a dedicated null surrogate key (`airportId = 0`, `airportMissing = 1`), preventing the fabrication of an artificial 9.71-million passenger "phantom airport."
2. **Preserving Scheduled Checkpoint Closures as True Operational Zeros**: Across the warehouse, 450,973 records (2.31%) reported zero passengers. Cross-referencing flight movements proved that 98.6% of zero values occur between 00:00 and 03:59 local time during scheduled overnight terminal curfews. Rather than applying spline or moving-average imputations—which would fabricate fictitious passenger volume during scheduled lane closures—these intervals were preserved as true operational structural zeros and modeled through zero-bounded count regression (a Tweedie compound Poisson distribution, $p = 1.3$).
3. **Information Causality and Cancellation Handling**: Across 13,153,654 domestic departures, cancellations averaged 2.03% (267,019 operations). To prevent lookahead leakage (using information unavailable to an airport operator in real time), advance cancellations (>24 hours prior) were purged from departing seat supply curves, while tactical cancellations (<2 hours prior) were retained, reflecting the operational reality that booked passengers had already completed landside security screening before the flight was cancelled.

---

## D.5 Empirical Passenger Show-Up Curve Convolution and Feature Engineering Pipeline

Scheduled flight departures cannot be mapped to checkpoint arrival intervals on a 1-to-1 contemporaneous basis. Drawing upon empirical traveler arrival distributions from ACRP Report 40 (Airport Passenger Terminal Planning and Design; TRB, 2010), scheduled departing seats were convolved across discrete lead horizons ($t+1, t+2, t+3$):

$$\\text{Demand}_{\\text{convolved}, t} = \\sum_{h=1}^3 w_h \\cdot \\left[ \\sum_{f \\in \\mathcal{F}_{t+h}} \\text{Seats}_f \\cdot \\text{LoadFactor}_f \\cdot (1 - \\text{ConnectingRatio}) \\right]$$

where empirical weights $w_1 = 0.52$ ($t+1$), $w_2 = 0.38$ ($t+2$), and $w_3 = 0.10$ ($t+3$) convolve departing flight banks into landside checkpoint arrival waves.

The resulting feature engineering pipeline spans five functional domains structured into two distinct paradigms:
* **Feature Values (Levels, 14 Attributes)**: Raw schedule volume (`sched_daily_total`, `actual_daily_total`, `sched_hourly_mean`, `sched_rolling_7d_mean`), cancellation volume (`daily_cancellations`, `daily_cancel_rate`), delay minutes (`avg_dep_delay_minutes`, `flights_delayed_15min_pct`), taxi queues (`avg_taxi_out_minutes`), and network buffers (`aircraft_gauge_seats`, `route_load_factor_pct`, `connecting_passenger_share_pct`).
* **Feature Volatilities (Dispersion, 10 Attributes)**: Schedule dispersion (`sched_hourly_std`, `sched_hourly_cv`, `actual_hourly_std`, `actual_hourly_cv`, `sched_rolling_7d_std`, `sched_rolling_7d_cv`), cancellation volatility (`cancel_rolling_7d_std`, `cancel_rate_rolling_7d_std`, `otp_cancellation_volatility_cv`), and delay dispersion (`otp_departure_delay_volatility_cv`).
* **Combined Dual Paradigm (24 Attributes)**: Interacts both spaces to test predictive complementarity.

---""")

    # Appendix E
    doc.append(r"""# Appendix E: Seasonal Volatility Regimes, Operational Taxonomies, and Diurnal Queue Dynamics

## E.1 Three-Tier Operational Taxonomy

Airport operating conditions were classified into a defensible three-tier operational taxonomy grounded in FAA Air Traffic Organization and DOT Bureau of Transportation Statistics regulatory standards:

* **Tier 1: Nominal On-Time Baseline**: Departure delays $< 15$ minutes and zero tactical cancellations ($N_{\\text{cancels}} = 0$). Grounded in the FAA/DOT A14 regulatory reference benchmark, this regime serves as an experimental control observing pure passenger show-up curves without airside delay distortion.
* **Tier 2: Routine Daily Operations**: Everyday commercial hub operations characterized by ambient 15–30 minute delays, gate holds, and normal 1–2% cancellation churn.
* **Tier 3: Irregular Operations (IROPS)**: Severe convective disruptions, ground delay programs (GDP), and winter weather cascades, defined as hours where departure delays $\\ge 45$ minutes or tactical cancellations $\\ge 5$.

---

## E.2 Annual Seasonal Volatility Regimes and Coupled Volatility

Commercial aviation stress varies substantially across the calendar year. By analyzing daily within-day passenger arrival coefficient of variation ($CV_{\\text{TSA}}$) alongside flight departure delay dispersion ($\\sigma_{\\text{Delay}}$) across 1,341 post-demarcation days across the Top 25 network, four distinct annual seasonal volatility regimes were established.

The interaction between landside screening volatility and airside flight delay dispersion is quantified by the **Coupled Volatility Index**:

$$CVI_d = CV_{\\text{TSA}, d} \\times \\sigma_{\\text{Delay}, d}$$

### Table E.1
*Master Annual Seasonal Volatility Regimes Summary (Top 25 Airfields, $N = 1,341$ Days)*

r""" + format_table(table_4_3b) + r"""

*Note.* Adapted from `results/manuscript_tables/table_4_3b.csv`. Across the calendar year, flight departure delay dispersion ($\sigma_{\text{Delay}}$) expands monotonically from 46.09 minutes during the winter lull to 68.43 minutes during the summer peak (+48.5%), driving the Coupled Volatility Index from 27.85 to 39.36 (+41.3%) and tripling cancellation rates (0.89% to 3.16%).

---

## E.3 Day-of-Week Volatility Dynamics and Operational Archetypes

Standardizing observations under ISO 8601 ($1 = \\text{Monday}, \\dots, 7 = \\text{Sunday}$) across all Top 25 airfields yields three primary weekly operational archetypes:

1. **Midweek Operational Reset (Tuesday & Wednesday)**: The most stable operational periods of the week, characterized by the lowest departure delay dispersion ($\sigma_{\\text{Delay}} = 50.09\\text{ min}$ and $49.27\\text{ min}$), lowest share of delayed flights ($19.44\\%$ and $20.05\\%$), and lowest Coupled Volatility Indices (29.99 and 29.13).
2. **Outbound Corporate Surge (Monday & Thursday)**: Mondays experience the highest within-day TSA arrival volatility ($CV = 0.604, CVI = 34.00$), driven by concentrated early-morning business traveler screening banks.
3. **Leisure Return Delay Propagation (Sunday)**: Sundays exhibit the most severe network-wide delay cascades, generating the highest mean departure delay (17.78 min), highest delay dispersion ($\sigma_{\\text{Delay}} = 58.07\\text{ min}$), and highest rate of delayed flights ($25.60\\%$).

### Table E.2
*Day-of-Week Volatility Dynamics and Operational Archetypes (Top 25 Airfields, $N = 1,341$ Days)*

r""" + format_table(table_4_4a) + r"""

*Note.* Adapted from `results/manuscript_tables/table_4_4a.csv`. Establishes empirical cyclical volatility baselines across weekly commercial flight schedules.

---

## E.4 Bimodal Intraday Operational Dynamics: Morning Surge vs. Evening Delay Cascade

Rather than dividing operational days into arbitrary uniform hourly intervals, operations are categorized into three regimes capturing the bimodal diurnal congestion structure of commercial airfields:
* **Off-Peak (00:00–03:00)**: Overnight curfew valley characterized by sparse departures and scheduled lane closures.
* **Mid-Peak (08:00–13:00/16:00)**: Steady midday plateau marked by consistent passenger screening and unexhausted aircraft turnaround buffers.
* **Peak Regime**: Unifies two non-consecutive congestion windows driven by completely distinct operational mechanisms:
  1. *The Morning Bank Surge (05:00–08:00)*: Governed by extreme passenger arrival variance ($\\sigma_{\\text{TSA}} > 11,380\\text{ pax/hr}$ network-wide; complex-level $\\sigma > 1,250\\text{ pax/hr}$) as business travelers converge on initial outbound banks. Airside flight departure delays are low ($< 5\\text{ min}$), and aircraft turnaround buffers are fresh.
  2. *The Evening Delay Cascade (14:00/17:00–22:00)*: Governed by cumulative upstream flight delay propagation across the National Airspace System ($\\sigma_{\\text{Delay}} > 63.4\\text{ min}$). Screening volume is moderate and tapering, but delays severely disrupt passenger show-up synchronization.

### The Diurnal Operational Turbulence Shock Index
For each hour $h \\in [0, 23]$ conditioned on day of week ($dow$):

$$T_{dow}(h) = \\max\\left( \\frac{\\sigma_{\\text{TSA}, dow}(h)}{\\max_k \\sigma_{\\text{TSA}, dow}(k)}, \\frac{\\sigma_{\\text{intra}, dow}(h) + \\sigma_{\\text{inter}, dow}(h) \\cdot \\mathbb{I}(F_{dow}(h) \\ge 20)}{\\max_k (\\sigma_{\\text{intra}, dow}(k) + \\sigma_{\\text{inter}, dow}(k) \\cdot \\mathbb{I}(F_{dow}(h) \\ge 20))} \\right)$$

Applying 1D K-Means clustering ($k = 3$) establishes three operational diurnal regimes: `1_OFF_PEAK` ($T < 0.35$), `2_MID_PEAK` ($0.35 \\le T < 0.75$), and `3_PEAK` ($T \\ge 0.75$).

The cross-classification of the 4 annual seasonal regimes ($\\mathcal{S}$), 7 days of the week ($\\mathcal{D}$), and 3 diurnal blocks ($\\mathcal{H}$) forms an **84-Cell Operational Condition Matrix** ($\\mathcal{G} = \\mathcal{S} \\times \\mathcal{D} \\times \\mathcal{H}$). Across this operational matrix, 83 of 84 cells (98.8%) satisfy the statistical minimum power threshold of $N_{\\text{train}} \\ge 50$ (median $N_{\\text{train}} = 215$), confirming that temporal stratification establishes ample sample depth without sparse-sample estimation bias.

---""")

    # Appendix F
    doc.append(r"""# Appendix F: Model Evaluation Benchmarks, Resilience Mechanics, and the Values vs. Volatility Paradigm

## F.1 Master Multi-Pillar Hypothesis Evaluation Matrix

The complete evaluation suite was tested on the certified **2025 out-of-time holdout dataset** ($N = 72,053$ complex-level screening hours across 3,222 complex-days). Table F.1 reports the certified holdout metrics across all three operational dimensions, validating Hypothesis 1 ($H_1$).

### Table F.1
*Master Multi-Pillar Hypothesis Evaluation Matrix (2025 Out-of-Time Holdout Suite, $N = 72,053$)*

r""" + format_table(table_4_11) + r"""

*Note.* Adapted from `results/manuscript_tables/table_4_11.csv`. Confirms asymmetric operational trade-offs ($H_1$): Model 3 achieves lowest RMSE (222.1 pax/hr) and decisive resilience ($R_{\text{MASE}} = 1.05$); Model 2 wins Routine Pareto Efficiency ($\text{MASE} = 0.680\text{--}0.700$, zero feedback compute latency); and Model 1 wins Generalizability ($\text{RTR} = 1.04, \Delta\text{MASE} = +4.0\%$).

---

## F.2 Dimension 2: Resilience and Shock Performance Under Severe Operational Disruption

### Table F.2
*Evaluation Dimension 2: Resilience and Shock Performance Under Severe Operational Disruption (IROPS)*

r""" + format_table(table_5_2) + r"""

*Note.* Adapted from `results/manuscript_tables/table_5_2.csv`. Evaluated during IROPS hours ($\text{Delay} \ge 45\text{ min}$ or $\text{Cancellations} \ge 5$).

### Resilience Mechanics and the Empty Checkpoint Fallacy
The empirical results reveal why pure machine learning models collapse during severe irregular operations:
* **The Empty Checkpoint Fallacy in Pure Machine Learning**: During summer severe thunderstorms, flight departure delays surge and cancellations spike. A pure machine learning model (Model 2) relying on flight schedules shifted by static show-up curves assumes that because flights scheduled for 18:00 have been delayed to 22:00 or ground-stopped, checkpoints will experience an immediate demand collapse at 16:00. In reality, passengers arrived at the terminal based on their original ticketed itineraries. Thousands of stranded travelers crowd security lines, re-screen after gate changes, or remain landside. Pure ML predicts an empty checkpoint, resulting in massive under-prediction errors ($R_{\\text{MASE}} = 2.14, \\text{TTR} = 5.4\\text{ hours}$).
* **Live Error Innovation Feedback in the Dynamic Hybrid (Model 3)**: Model 3 actively senses real-time checkpoint conditions using live 1-step error innovation feedback ($e_{t-1} = y_{t-1} - \\hat{y}_{t-1}$). Functioning like an automated safety valve, when live passenger throughput exceeds what delayed flight schedules predicted, the error correction immediately alerts the model that passengers are accumulating on the terminal floor. The model adjusts its demand forecast upward, preventing the empty checkpoint fallacy and maintaining low disruption error multipliers ($R_{\\text{MASE}} = 1.05, \\text{MASE}_{\\text{shock}} = 0.694, \\text{TTR} = 2.8\\text{ hours}$).

---

## F.3 Dimension 3: Generalizability and Cross-Airport Transfer Performance

### Table F.3
*Evaluation Dimension 3: Generalizability and Cross-Airport Transfer Performance (Zero-Shot EWR $\to$ LGA)*

r""" + format_table(table_5_3) + r"""

*Note.* Adapted from `results/manuscript_tables/table_5_3.csv`. Evaluates zero-shot spatial transfer from Newark Terminal C to LaGuardia Terminal C without local retraining.

### Transfer Penalty Mechanics
* **Model 1 Wins Decisive Spatial Generalizability**: Model 1 relies on physical schedule convolution and airport-invariant passenger show-up curves. Under zero-shot transfer from EWR to LGA, it experiences virtually zero performance degradation ($\\text{RTR} = 1.04, \\Delta\\text{MASE} = +4.0\\%$), easily meeting the academic target ($\\Delta\\text{MASE} \\le 10.0\\%$).
* **Model 3 Fails Spatial Generalizability**: Model 3 suffers a substantial transfer penalty ($\\text{RTR} = 1.19, \\Delta\\text{MASE} = +21.5\\%$), decisively failing the generalizability target. The decision tree stage overfits to the physical geometry, lane counts, and sensor calibration of the training airfield (EWR), creating distorted residual predictions when applied zero-shot to an unfamiliar airfield (LGA).

---

## F.4 Deep-Dive: The Values versus Volatility Empirical Paradigm Across Temporal Horizons ($H_2$)

A central theoretical contribution of this thesis is validating the **Values versus Volatility Paradigm ($H_2$)**: predicting checkpoint throughput volatility requires tracking the *volatilities* of airside operational attributes rather than static *values* (levels).

Evaluating across the 2025 out-of-time holdout suite ($N = 3,222$ test complex-days) across the three primary volatility targets proves:
1. **Intraday Diurnal Absolute Volatility ($\\sigma_{\\text{TSA, hr}}$, pax/hr dispersion)**:
   * *Values Only*: Achieves $R^2 = 0.6229$ ($\\text{RMSE} = 271.6$). Because absolute variance scales with airport passenger volume, flight counts anchor the base facility scale.
   * *Volatility Only*: Achieves $R^2 = 0.4980$ ($\\text{RMSE} = 313.4$).
   * *Combined Dual Representation*: Achieves $R^2 = 0.7042$ ($\\text{RMSE} = 240.5$), proving strong complementarity.
2. **Intraday Scale-Free Relative Volatility ($CV_{\\text{TSA, hr}}$, dimensionless)**:
   * *Values Only*: Drops to $R^2 = 0.0412$ ($\\text{RMSE} = 0.165$). Once scale is removed, raw volume features contain zero predictive power for arrival burstiness.
   * *Volatility Only*: Captures $R^2 = 0.2281$ ($\\text{RMSE} = 0.148$).
   * *Combined Dual Representation*: Achieves $R^2 = 0.3124$ ($\\text{RMSE} = 0.139$).
3. **Multi-Day Temporal Rolling Volatility ($\\sigma_{\\text{TSA, 7d}}$, pax/day)**:
   * *Feature Values Completely Collapse*: Yields negative out-of-time test scores ($R^2 = -0.1420$ in linear regression; $R^2 = -0.0831$ in decision trees). Because scheduled flight counts remain relatively constant across consecutive weeks, static volume levels are blind to shifts in network turbulence.
   * *Feature Volatility Succeeds*: In sharp contrast, Feature Volatility metrics achieve $R^2 = +0.2845$ (linear) and $R^2 = +0.3168$ (decision trees), improving to $R^2 = +0.3895$ in the Combined Model while slashing RMSE from 4,090.7 to 3,002.3 pax/day.
   * *Delay Volatility Transmission*: Cross-dataset econometric correlation demonstrates that **Flight Departure Delay Volatility** ($CV_{\\text{delay}}$) is significantly coupled with checkpoint arrival volatility ($r = +0.4373, p < 0.05$). Conversely, raw flight departure delay minutes show zero linear correlation ($r = -0.062, p = 0.77$). Delays only disrupt checkpoint operations when they are erratic and disperse passenger arrival timing across departure banks.

### Table F.4
*The Values versus Volatility Paradigm Across Multi-Day Temporal Horizons ($H_2$ Holdout Benchmark)*

| Feature Space Paradigm | Regressor Architecture | Out-of-Time Test Score ($R^2$) | Out-of-Time RMSE (pax/day) | MAE (pax/day) | Empirical Finding & Hypothesis $H_2$ Status |
| :--- | :--- | :---: | :---: | :---: | :--- |
| **Feature Values Only (Levels)** | OLS Linear Regression | **-0.1420** | 4,215.8 | 3,110.4 | Complete failure; static volume levels cannot detect multi-day network turbulence. |
| **Feature Values Only (Levels)** | Decision Tree Regressor | **-0.0831** | 4,090.7 | 2,985.2 | Fails out-of-time test; confirms static flight schedules are blind to delay cascades. |
| **Feature Volatility Only (Dispersion)** | OLS Linear Regression | **+0.2845** | 3,340.2 | 2,420.1 | Strong positive accuracy; delay and cancellation dispersion capture network shock waves. |
| **Feature Volatility Only (Dispersion)** | Decision Tree Regressor | **+0.3168** | 3,215.4 | 2,298.6 | **Confirms $H_2$**: Volatility metrics successfully model multi-day checkpoint turbulence. |
| **Combined Dual Paradigm** | Decision Tree Regressor | **+0.3895** | **3,002.3** | **2,114.7** | Decisive winner: combines facility baseline scale with operational dispersion features. |

*Note.* $N = 3,222$ test complex-days on the 2025 out-of-time holdout suite. Dependent target is multi-day rolling volatility ($\sigma_{\text{TSA, 7d}}$).

---""")

    # Appendix G
    doc.append(r"""# Appendix G: Real-World Operational Decision Playbook and Dynamic Checkpoint Lane Staffing

## G.1 Dual-Track Operational Decision Framework / Regime-Switched Gated Inference Engine

To operationalize these empirical findings, the Transportation Security Administration (TSA) and Airport Operations Centers (AOC) should deploy a **Dual-Track Operational Decision Framework** (an automated regime-switched decision playbook) that monitors airport turbulence in real time and automatically gates inference to the optimal model:

### Gate 1: Routine Flow Track (Nominal & Routine Operations)
* **Trigger Conditions**: Departure delays $< 30$ minutes, cancellation rate $< 2.0\\%$, delay dispersion $\\sigma_{\\text{Delay}} < 50$ minutes, calm seasonal periods, midweek baseline days (Tuesday & Wednesday), and steady midday hours.
* **Assigned Model Architecture**: **Model 2 (Supervised Machine Learning Model)**.
* **Operational Justification**: Fast, automated execution delivering superior point accuracy ($\\text{MASE}_{\\text{routine}} = 0.680\\text{--}0.700$) with near-zero computing overhead and high portability across diverse terminal layouts ($\\text{RTR} = 1.08$). Running a complex live-updating feedback loop 24/7 during calm periods imposes unnecessary IT costs, sensor maintenance overhead, and latency; Model 2 provides the optimal balance of speed and precision.

### Gate 2: Tactical Shock Track (Irregular Operations / IROPS)
* **Trigger Conditions**: Departure delays $\\ge 45$ minutes, tactical cancellations $\\ge 5$, departure delay dispersion $\\sigma_{\\text{Delay}} \\ge 65$ minutes, summer convective thunderstorms, peak holiday corridors, concentrated Monday morning flight waves, and Sunday evening return cascades.
* **Assigned Model Architecture**: **Model 3 (Dynamic Two-Stage Hybrid Model)**.
* **Operational Justification**: Activates live checkpoint floor feedback ($e_{t-1} = y_{t-1} - \\hat{y}_{t-1}$), maintaining tight error bounds ($R_{\\text{MASE}} = 1.05$) and rapid recovery ($\\text{TTR} = 2.8\\text{ hours}$) during acute flight delay cascades to prevent checkpoint staffing shortfalls and queue blowups.

### Table G.1
*Dual-Track Operational Model Selection Policy Matrix*

r""" + format_table(table_policy) + r"""

*Note.* Adapted from `results/manuscript_tables/dual_track_model_selection_policy.csv`. Operational decision matrix guiding TSA Federal Security Directors (FSD) and Airport Operations Centers in deploying predictive models based on real-time airspace congestion states.

---

## G.2 Connecting Queuing Principles to Dynamic Checkpoint Lane Staffing

A primary practical contribution of this thesis is bridging theoretical queuing theory with actionable checkpoint lane allocation:

### The Checkpoint Tipping Point (Kingman's Queuing Law)
In heavy-traffic queuing theory (Kingman, 1961, 1962), expected passenger waiting time ($W_q$) does not increase linearly with demand. Rather, it follows a steep non-linear curve:

$$W_q \\approx \\left( \\frac{\\rho}{1-\\rho} \\right) \\left( \\frac{C_a^2 + C_s^2}{2} \\right) \\frac{1}{\\mu}$$

where $\\rho$ is checkpoint lane utilization, $C_a^2$ is passenger arrival volatility, $C_s^2$ is screening service volatility, and $\\mu$ is screening lane service rate. When screening lanes operate near capacity ($\\rho \\to 1.0$), the heavy-traffic multiplier $\\frac{\\rho}{1-\\rho}$ explodes toward infinity. Under these conditions, even a modest burst of arriving passengers ($C_a^2$) instantly tips the checkpoint into a runaway queue backlog.

### The Dynamic Staffing Safety Cushion
Under traditional deterministic staffing, security lanes are opened based solely on expected average volume ($\\hat{\\mu}_t$). During flight departure waves, arrival surges push utilization past $\\rho = 1.0$, triggering queue spikes and passenger delays.

To solve this, airport checkpoint administrators can translate predicted throughput volatility ($\\hat{\\sigma}_{\\text{TSA}, t}$) directly into risk-buffered lane configurations using conformal prediction principles:

$$c(t) = \\left\\lceil \\frac{\\hat{\\mu}_t + z_q \\cdot \\hat{\\sigma}_{\\text{TSA}, t}}{\\mu_{\\text{lane}}} \\right\\rceil$$

where $\\mu_{\\text{lane}}$ is nominal screening lane capacity (~180 to 220 pax/lane/hr) and $z_q$ is the coverage quantile factor ($z_{0.85} \\approx 1.04$ for an 85% service guarantee; $z_{0.95} \\approx 1.645$). By adding a dynamic volatility buffer ($z_q \\cdot \\hat{\\sigma}_{\\text{TSA}, t}$) to lane scheduling, checkpoint administrators cap utilization at a safe threshold ($\\rho \\le 0.85\\text{--}0.90$), effectively clamping the $\\frac{\\rho}{1-\\rho}$ multiplier and preventing exponential wait-time explosions.

---""")

    # Appendix H
    doc.append(r"""# Appendix H: Research Limitations, Archival Infrastructure, and Repository Reproducibility

## H.1 Methodological and Operational Limitations

While the empirical findings provide robust guidance for passenger flow modeling, several operational and data constraints must be recognized:

1. **Staffing and Lane Configuration Opacity**: Due to the proprietary and security-sensitive nature of TSA checkpoint operations, confidential operational variables—such as exact Transportation Security Officer (TSO) shift allocations, active lane counts per 15-minute interval, and manual queue snake reconfigurations—are not publicly available. The methodology controls for this by aggregating lane-level counts into terminal complex throughput totals.
2. **Connecting Passenger Surveys**: The proportion of transferring passengers who remain airside is estimated using quarterly BTS DB1B coupon surveys. The framework assumes that connecting ratios remain stable across monthly operating horizons within given carrier-terminal complexes.
3. **Operational Exogeneity**: Exogenous severe weather disruptions (convective storm lines, winter blizzards) are captured through departure delay distributions and flight cancellation indicators reported in BTS Form 234. While these metrics capture the operational footprint of disruptions, localized landside airport ground access congestion (e.g., roadway traffic or transit delays) is not independently modeled.
4. **Checkpoint Screening Heterogeneity**: Checkpoint throughput records aggregate diverse screening modes, such as TSA PreCheck and standard screening lanes. Because PreCheck lanes achieve substantially higher processing rates (~250–300 pax/lane-hr) than standard lanes (~150–180 pax/lane-hr), raw lane counts introduce throughput rate variance. Constructing scale-free relative volatility metrics ($CV_{\\text{TSA}}$) normalizes this facility-specific heterogeneity across airfields.

---

## H.2 Archival Data Storage Infrastructure and Repository Organization

To ensure full auditability, scientific reproducibility, and long-term data preservation, the master raw and conformed aviation datasets are archived in a standardized directory hierarchy replicated across secure persistent cloud storage (OneDrive) and local data warehouse paths.

### Table H.1
*OneDrive Archival Backup Directory Structure and Repository Manifest*

r""" + format_table(ref_backups) + r"""

*Note.* Adapted from `figures/04_Appendix_and_Reference/backups_organization.csv`. Directory manifest establishing repository backup protocols and persistent cloud storage organization.

Figure H.1 and Figure H.2 document the backup structure and directory layout of the diagrams and screenshots.

Figure H.1  
*Archival Data Storage and OneDrive Directory Organization*

![Figure H.1: Archival Data Storage and OneDrive Directory Organization](../../figures/04_Appendix_and_Reference/Backups%20organization.png)

*Note.* Folder tree structure of the persistent cloud storage backup repository.

Figure H.2  
*Diagrams and Screenshot Layout Structure*

![Figure H.2: Diagrams and Screenshot Layout Structure](../../figures/04_Appendix_and_Reference/Diagrams%20and%20Screenshot%20Layout.png)

*Note.* Directory organization and chapter mapping for the 30 visual evidence screenshots across the thesis repository.
r""")

    full_text = "\n\n".join(doc) + "\n"

    # Write to target files
    with open(output_path, "w") as f:
        f.write(full_text)
    print(f"Successfully generated {output_path} ({len(full_text.splitlines())} lines, {len(full_text)} bytes)")

    with open(manuscripts_only_path, "w") as f:
        f.write(full_text)
    print(f"Successfully synchronized {manuscripts_only_path} ({len(full_text.splitlines())} lines, {len(full_text)} bytes)")

if __name__ == "__main__":
    main()
