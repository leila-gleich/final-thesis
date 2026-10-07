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
- Pristine Markdown table rendering (no "r|" prefixes or broken rows)
- Explicit chapter and section cross-reference notes for each Appendix (A through H)
- Full inclusion of all methodological details from Appendix v1.docx
"""

import os
import pandas as pd

def format_table(df, align=None, column_names=None):
    orig_cols = list(df.columns)
    cols = column_names if column_names is not None else orig_cols
    header = "| " + " | ".join(cols) + " |"
    if align is None:
        sep = "| " + " | ".join([":---"] * len(cols)) + " |"
    else:
        sep = "| " + " | ".join(align) + " |"
    rows = []
    for _, r in df.iterrows():
        row_str = "| " + " | ".join(str(r[c]) if pd.notna(r[c]) else "" for c in orig_cols) + " |"
        rows.append(row_str)
    return "\n".join([header, sep] + rows)

def main():
    root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
    output_path = os.path.join(root_dir, "thesis_docs/manuscripts/appendix.md")
    manuscripts_only_path = os.path.join(root_dir, "thesis_docs/manuscripts/manuscripts-only/appendix.md")

    # Read source CSVs
    eq_csv_path = os.path.join(root_dir, "results/manuscript_tables/appendix_standard_literature_equations.csv")
    table_equations = pd.read_csv(eq_csv_path)

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

    # Format Table B.1
    table_b1_rows = []
    for _, r in table_equations.iterrows():
        eq_id = f"**{r['Equation_ID']}**"
        domain = str(r['Domain_Category'])
        eq_name = str(r['Equation_Name'])
        latex = f"${r['Mathematical_Formulation_LaTeX']}$"
        params = str(r['Parameters_and_Variables'])
        source = str(r['Published_Source_and_Citation'])
        role = str(r['Thesis_Operational_Role'])
        table_b1_rows.append({
            "Equation ID": eq_id,
            "Operational Domain": domain,
            "Formal Equation Name": eq_name,
            "Mathematical Formulation (KaTeX)": latex,
            "Parameters and Variables": params,
            "Peer-Reviewed Citation": source,
            "Thesis Operational Role": role
        })
    df_table_b1 = pd.DataFrame(table_b1_rows)
    formatted_table_b1 = format_table(df_table_b1)

    # Format other tables
    formatted_assumptions = format_table(
        ref_assumptions,
        column_names=["Analysis Level", "Key Methodological Assumption", "Mathematical & Operational Justification", "Critical Failure Mode Prevented"]
    )
    formatted_table_4_7 = format_table(table_4_7)
    formatted_table_4_8 = format_table(table_4_8)
    formatted_db_profiles = format_table(
        ref_db_profiles,
        column_names=["Metric / Characteristic", "TSA FOIA Checkpoint Logs (TSA-V0)", "BTS Flight Performance (OTP-V0)", "BTS T-100 Segment Statistics (T100-V0)"]
    )
    formatted_dataset_breakdown = format_table(
        ref_dataset_breakdown,
        column_names=["Dataset / File", "Analytical Grain", "Record Count (Rows)", "Attribute Count (Cols)", "Storage Size (Parquet)", "Uncompressed RAM (Approx.)", "Operational Notes"]
    )
    formatted_data_top9 = format_table(
        ref_data_top9,
        column_names=["Dataset Entity", "Partition Parquet File Path", "Record Count", "Compression Format", "Operational Description"]
    )
    formatted_db1b_hierarchy = format_table(
        ref_db1b_hierarchy,
        column_names=["BTS Table Level", "Table Acronym", "Analytical Unit / Grain", "Itinerary Representation Example (BOS to LAX)", "Contains Connecting Itineraries?"]
    )
    formatted_table_4_3b = format_table(table_4_3b)
    formatted_table_4_4a = format_table(table_4_4a)
    formatted_table_4_11 = format_table(table_4_11)
    formatted_table_5_2 = format_table(table_5_2)
    formatted_table_5_3 = format_table(table_5_3)
    formatted_policy = format_table(
        table_policy,
        column_names=["Operational Track", "Operating Regime", "Assigned Canonical Architecture", "Target Thresholds", "Empirical Holdout Performance", "Operational Rationale"]
    )
    formatted_backups = format_table(
        ref_backups,
        column_names=["Archival Directory Path", "Hierarchy Level", "Description and Preserved Contents"]
    )

    # Build Document Sections
    doc = []

    # Title & Overview
    doc.append(r"""# Appendix: Econometric Foundations, Methodological Architecture, and Peer-Reviewed Equation Registry
*Evaluating Predictive Techniques to Model Stochastic Airport Passenger Flow (MSAA / Gleich 700B)*  
*Author: Leila Gleich | Committee Review Draft | Embry-Riddle Aeronautical University*

---

## Executive Overview and Structural Organization

This appendix provides the foundational econometric derivations, data engineering profiles, sample filtering audits, empirical seasonal baselines, holdout evaluation benchmarks, and operational implementation frameworks supporting the thesis. The materials are organized across eight dedicated appendices:

* **Appendix A**: Statistical Foundation and Derivation of the Diebold-Mariano ($DM$) Test for Predictive Superiority
* **Appendix B**: Peer-Reviewed Literature Equation Registry and Mathematical Formulations
* **Appendix C**: Methodological Foundations, 4-Tier Filtering Pipeline, and Cohort Econometric Validation
* **Appendix D**: Aviation Data Engineering, Warehouse Architecture, and Hygiene Protocols
* **Appendix E**: Seasonal Volatility Regimes, Operational Taxonomies, and Diurnal Queue Dynamics
* **Appendix F**: Model Evaluation Benchmarks, Resilience Mechanics, and the Values vs. Volatility Paradigm
* **Appendix G**: Real-World Operational Decision Playbook and Dynamic Checkpoint Lane Staffing
* **Appendix H**: Research Limitations, Archival Infrastructure, and Repository Reproducibility

---""")

    # Appendix A
    doc.append(r"""# Appendix A: Statistical Foundation and Derivation of the Diebold-Mariano ($DM$) Test for Predictive Superiority

> *Note on Thesis Cross-References*: This appendix provides the formal mathematical derivations, asymptotic theory, and degrees-of-freedom audits for the statistical significance tests operationalized throughout the thesis. It is referenced in **Chapter III (Methodology)**, Section *Dataset Partitioning and Validation Protocol* and Section *Apparatus and Materials (Evaluation Metric Definition)*; and in **Chapter IV (Results)**, Section *Model Performance in the Context of the Thesis (Asymmetric Hypothesis Testing)* and Section *Empirical Confirmation of Asymmetric Trade-Offs (Hypothesis 1 Verified)*.

## A.1 The Methodological Dilemma: Why a Standard $p$-Value from a Paired $t$-Test Fails in Time-Series Forecasting

A frequent question encountered in applied statistics and operational forecasting is: *Why must researchers utilize the Diebold-Mariano test to establish statistical significance rather than simply calculating a standard $p$-value from a paired $t$-test or regression ANOVA?*

To answer this question rigorously, one must first clarify the relationship between hypothesis tests and probability metrics: **a $p$-value is not an independent statistical test; it is the numerical output generated by a specific test statistic.** A researcher cannot report a $p$-value without selecting an underlying test. Therefore, the methodological issue is not whether to report a $p$-value, but rather *which statistical test must be used to calculate a valid, mathematically defensible $p$-value when comparing time-series forecasting models.*

In standard cross-sectional data analysis, researchers routinely evaluate differences in model error using a standard paired Student's $t$-test on the loss differentials ($d_t = L(e_{1,t}) - L(e_{2,t})$). In the context of commercial aviation time series, however, standard paired tests are statistically invalid because they violate the foundational **independent and identically distributed (i.i.d.)** assumption.

### The Autocorrelation Problem in Airport Security Operations
Hourly passenger throughput at Transportation Security Administration (TSA) security checkpoints and its associated volatility ($\sigma_{\text{TSA}}$ and $CV_{\text{TSA}}$) are characterized by strong **serial autocorrelation**:
1. **Diurnal Schedule Waves**: Airlines coordinate departure banks in tightly synchronized waves (e.g., morning 06:00–08:30 and afternoon 16:00–18:30). If a predictive model underpredicts passenger arrivals at 07:00, the physical accumulation of queuing passengers and lingering terminal lobby congestion ensures that the model's error at 08:00 is not independent of its error at 07:00.
2. **Propagating Flight Delays**: During convective weather disruptions or Air Traffic Control (ATC) ground delay programs, departure delays cascade across connecting aircraft turnarounds throughout the operating day. Consequently, forecast errors exhibit persistent temporal dependency over multi-hour operational horizons.
3. **Multi-Step Forecast Horizons**: When forecasting over an $h$-step horizon ($h > 1$), forecast errors are mathematically guaranteed to follow at least a moving average process of order $h - 1$ ($\text{MA}(h-1)$), directly violating the independence assumption of classical tests.

### The Spurious Statistical Significance Hazard
When standard paired $t$-tests are applied to positively autocorrelated loss differentials, the standard sample variance formula:

$$\widehat{\text{Var}}_{\text{iid}}(\bar{d}) = \frac{s_d^2}{N} = \frac{\frac{1}{N-1}\sum_{t=1}^N (d_t - \bar{d})^2}{N}$$

**severely underestimates the true variance of the mean loss differential.** Because the standard error in the denominator is artificially deflated, the resulting test statistic ($t = \bar{d} / \text{SE}$) is artificially inflated. Consequently, the resulting textbook $p$-value collapses toward zero, producing **spurious statistical significance** (a massive escalation in Type I error rates). A standard paired $t$-test will routinely declare minor, random fluctuations between two models to be "statistically significant at $p < 0.001$" simply because it fails to account for temporal persistence in the underlying flight data.

Furthermore, airport passenger volumes display pronounced **heteroskedasticity** (variance during midday and evening peaks is orders of magnitude greater than variance during overnight curfew hours) and non-Gaussian error tails. The **Diebold-Mariano ($DM$) test** (Diebold & Mariano, 1995) was explicitly formulated to overcome these exact econometric hurdles.

---

## A.2 Mathematical Derivation and Econometric Architecture of the Diebold-Mariano Test

The Diebold-Mariano procedure tests the null hypothesis that two competing forecasting models possess equal predictive accuracy over a given out-of-time evaluation sample, while explicitly correcting for serial correlation and heteroskedasticity in the forecast error differentials.

### Step 1: Formulation of the Loss Differential Series
Let $y_t$ denote the observed passenger throughput volatility at hour $t$ ($t = 1, 2, \dots, N$). Let $\hat{y}_{1,t}$ and $\hat{y}_{2,t}$ denote the forecasts generated by Model 1 and Model 2, respectively, producing forecast errors:

$$e_{1,t} = y_t - \hat{y}_{1,t}, \quad e_{2,t} = y_t - \hat{y}_{2,t}$$

The operational loss associated with each forecast error is determined by a specified loss function $g(e_t)$. While classical regression assumes quadratic loss ($g(e_t) = e_t^2$), the Diebold-Mariano framework permits arbitrary, asymmetric, or scale-free loss functions, such as linear absolute loss ($g(e_t) = |e_t|$) or scaled error loss:

$$g(e_t) = \frac{|e_t|}{\frac{1}{N-24}\sum_{i=25}^N |y_i - y_{i-24}|}$$

The **loss differential** at each observation hour $t$ is defined as:

$$d_t = g(e_{1,t}) - g(e_{2,t})$$

The null hypothesis of equal expected predictive accuracy and the alternative hypothesis of divergent predictive accuracy are stated as:

$$H_0: E[d_t] = 0 \quad \text{versus} \quad H_1: E[d_t] \neq 0$$

### Step 2: The Sample Mean Loss Differential
The sample mean of the loss differential sequence across the holdout sample of size $N$ is calculated as:

$$\bar{d} = \frac{1}{N} \sum_{t=1}^N d_t$$

Under the null hypothesis, $E[\bar{d}] = 0$. However, to construct a standardized test statistic, one must accurately estimate the asymptotic variance of $\bar{d}$ without imposing independence assumptions across $t$.

### Step 3: The Long-Run Covariance Estimator (HAC Adjustment)
Because the loss differential series $\{d_t\}$ is serially correlated up to lag $h-1$, the true variance of the sample mean depends on both the contemporaneous variance and all autocovariances:

$$\text{Var}(\bar{d}) = \frac{1}{N^2} \sum_{t=1}^N \sum_{s=1}^N \text{Cov}(d_t, d_s) = \frac{1}{N} \left[ \gamma_0 + 2 \sum_{k=1}^{N-1} \left(1 - \frac{k}{N}\right) \gamma_k \right]$$

where $\gamma_k = \text{Cov}(d_t, d_{t-k})$ represents the autocovariance of the loss differential at lag $k$. For an $h$-step-ahead forecast, autocovariances beyond lag $h-1$ are theoretically zero under optimal forecasts. The **Heteroskedasticity and Autocorrelation Consistent (HAC)** long-run variance estimator (equivalent to the spectral density of $d_t$ at frequency zero) is defined as:

$$\hat{V}(\bar{d}) = \hat{\gamma}_0 + 2 \sum_{k=1}^{h-1} w_k \hat{\gamma}_k$$

where:
* $\hat{\gamma}_0 = \frac{1}{N} \sum_{t=1}^N (d_t - \bar{d})^2$ is the sample variance.
* $\hat{\gamma}_k = \frac{1}{N} \sum_{t=k+1}^N (d_t - \bar{d})(d_{t-k} - \bar{d})$ is the sample autocovariance at lag $k$.
* $w_k$ is a lag kernel weighting factor. In standard $h$-step forecasting, a uniform rectangular lag window is applied ($w_k = 1$ for $k = 1, \dots, h-1$), or a Bartlett triangular kernel ($w_k = 1 - \frac{k}{h}$) to guarantee positive semi-definiteness in finite samples.

The estimated variance of the sample mean is therefore:

$$\widehat{\text{Var}}(\bar{d}) = \frac{\hat{V}(\bar{d})}{N}$$

### Step 4: The Asymptotic Test Statistic and $p$-Value Derivation
Applying the Central Limit Theorem for weakly dependent, stationary time series, the standardized Diebold-Mariano test statistic converges asymptotically to a standard normal distribution:

$$DM = \frac{\bar{d}}{\sqrt{\widehat{\text{Var}}(\bar{d})}} = \frac{\bar{d}}{\sqrt{\frac{1}{N}\left(\hat{\gamma}_0 + 2\sum_{k=1}^{h-1} w_k \hat{\gamma}_k\right)}} \xrightarrow{d} \mathcal{N}(0, 1)$$

Under the two-sided alternative hypothesis ($H_1: E[d_t] \neq 0$), the exact asymptotic $p$-value is calculated directly from the standard normal cumulative distribution function $\Phi(\cdot)$:

$$p = 2 \left[ 1 - \Phi(|DM|) \right]$$

*Decision Rule*: If $|DM| > z_{\alpha/2}$ (e.g., $|DM| > 3.291$ for $\alpha = 0.001$), the null hypothesis of equal predictive accuracy is rejected. A positive statistic ($DM > 0$) indicates that Model 1 generates significantly higher loss than Model 2 (proving Model 2's empirical superiority), whereas a negative statistic indicates Model 1 superiority.

---

## A.3 Empirical Implementation Across the 2025 Holdout Evaluation Suite

In this thesis research, the candidate predictive modeling suite was tested on the certified **2025 full-year out-of-time holdout dataset** across 12 carrier-exclusive screening complexes within the 9-airport experimental cohort (BOS, DFW, DTW, EWR, IAH, LAX, LGA, ORD, PHL), representing $N = 72,053$ hourly observations across 3,222 complex-days.

The candidate evaluation suite encompasses three primary modeling paradigms benchmarked against an empirical baseline control:
1. **Baseline Control**: Diurnal Volatility Naive Persistence Benchmark ($\widehat{\text{Vol}}_t = \text{Vol}_{t-24}$, non-parametric $\text{MASE} \equiv 1.000$).
2. **Model 1 (Deterministic Flight Schedule Model)**: Deterministic Operational Baseline convolving scheduled airline flight banks across empirical ACRP Report 40 passenger show-up curves ($t+1, t+2, t+3$).
3. **Model 2 (Supervised Machine Learning Model)**: Automated decision-tree regressor incorporating flight schedule dispersion and 24 BTS OTP operational attributes (delays, cancellations, taxi queues).
4. **Model 3 (Dynamic Two-Stage Hybrid Model)**: Sequential two-stage model coupling recurring schedule cycles with live 1-step error innovation feedback ($e_{t-1} = y_{t-1} - \hat{y}_{t-1}$) from the checkpoint floor.

### Table A.1
*Diebold-Mariano Pairwise Statistical Significance Matrix (2025 Holdout Benchmark, $N = 72,053$)*

| Model Comparison | Baseline Model ($M_A$) | Competing Model ($M_B$) | Evaluation Loss Function | $DM$ Test Statistic | Asymptotic $p$-Value | Econometric Conclusion |
| :--- | :--- | :--- | :--- | :---: | :---: | :--- |
| **Model 2 vs. Model 1** | Model 1 (Deterministic) | Model 2 (Machine Learning) | Absolute Scaled Loss | **+42.15** | **$p < 0.0001$** | Model 2 achieves decisive, genuine error reduction over deterministic schedules. |
| **Model 3 vs. Model 1** | Model 1 (Deterministic) | Model 3 (Dynamic Hybrid) | Absolute Scaled Loss | **+48.72** | **$p < 0.0001$** | Model 3 achieves decisive, genuine error reduction over deterministic schedules. |
| **Model 3 vs. Model 2** | Model 2 (Machine Learning) | Model 3 (Dynamic Hybrid) | Absolute Scaled Loss | **+12.84** | **$p < 0.0001$** | Model 3 error reduction over Model 2 is statistically significant in-sample. |
| **Model 1 vs. Baseline** | Baseline Control | Model 1 (Deterministic) | Absolute Scaled Loss | **+8.42** | **$p < 0.0001$** | Model 1 schedule convolution significantly outperforms naive diurnal persistence. |

*Note.* $N = 72,053$ hourly observations across 12 carrier-exclusive checkpoint complexes. Positive $DM$ indicates that Model $B$ yields lower forecast loss than Model $A$. Standard errors estimated using Newey-West Bartlett kernel HAC estimator with lag length $h = 1$. All tests reject the null hypothesis of equal predictive accuracy at $\alpha = 0.0001$.

### Sample Size Sufficiency and Degrees of Freedom
The evaluation sample size ($N = 72,053$) vastly exceeds standard econometric thresholds, satisfying Central Limit Theorem requirements for the asymptotic normality of $DM$:
* Across the **84-Cell Operational Condition Matrix** ($\mathcal{G} = \mathcal{S} \times \mathcal{D} \times \mathcal{H}$), 70 of 84 testing cells (83.3%) maintain $N_{\text{test}} \ge 30$ (median $N_{\text{test}} = 76$).
* For the remaining 14 low-sample cells (e.g., overnight curfew hours during holiday off-peak periods, with $18 \le N_{\text{test}} \le 24$), non-parametric **Wilcoxon signed-rank tests** were executed as a secondary robustness check. In all cases, the non-parametric tests confirmed the Diebold-Mariano conclusions at $p < 0.001$, proving that statistical significance is not an artifact of sample size inflation or distributional distortion.

---

## A.4 Operational Significance vs. Practical Implementation in Terminal Management

A vital distinction for academic committees and airport operational leadership is the divergence between **statistical significance** and **operational Pareto efficiency**:

1. **Statistical Significance Demonstrates Authenticity, Not Implementation Viability**:  
   The Diebold-Mariano test confirms that Model 3's error reduction over Model 2 ($DM = 12.84, p < 0.0001$) is not random chance. In a statistical laboratory, this would conclude the inquiry.
2. **Operational Realities Dictate Asymmetric Trade-Offs ($H_1$)**:  
   On the airport checkpoint floor, Model 3 achieves its statistical superiority by requiring live, uninterrupted 1-step error innovation feedback ($e_{t-1}$) from automated screening sensors. If an Airport Operations Center (AOC) lacks real-time sensor integration or experiences network latency, Model 3 cannot operate.
3. **The Routine Pareto Choice**:  
   Model 2 delivers an operational holdout accuracy of $\text{MASE}_{\text{routine}} = 0.680\text{--}0.700$—fully meeting the TSA operational target ($\text{MASE} < 0.700$)—while relying exclusively on published flight schedules and BTS operational data available hours in advance. Consequently, while Model 3 is statistically superior ($p < 0.0001$), **Model 2 represents the optimal practical strategy for routine, day-to-day checkpoint lane staffing.**

---""")

    # Appendix B
    sec_b = r"""# Appendix B: Peer-Reviewed Equation Registry and Mathematical Formulations

> *Note on Thesis Cross-References*: This appendix establishes the comprehensive mathematical foundations, queuing theorems, and statistical metric definitions utilized throughout the study. It is referenced in **Chapter II (Review of the Relevant Literature)**, Section *Classical Queuing Theory: First Moment (Volume) vs. Second Moment (Volatility)* and Section *The "Values versus Volatility" Paradigm in Transportation Demand*; in **Chapter III (Methodology)**, Section *Predictive Modeling Frameworks and Baseline Control* and Section *Construct Validity Threats and Operational Formulations*; and in **Chapter V (Discussion)**, Section *Connecting Queuing Principles to Dynamic Lane Staffing: The Staffing Safety Cushion*.

## B.1 Comprehensive Peer-Reviewed Mathematical Formulations & Queuing Registry

Table B.1 compiles the complete inventory of 20 peer-reviewed mathematical formulations, queuing theory equations, and econometric tests operationalized throughout this thesis.

### Table B.1
*Peer-Reviewed Literature Equations and Statistical Metric Registry*

{{TABLE_B1}}

*Note.* Adapted from `results/manuscript_tables/appendix_standard_literature_equations.csv`. Statistical notation conforms to APA Style (7th ed.).

---

## B.2 Detailed Derivations of Primary Volatility Targets and Operational Indices

To establish rigorous construct validity, the thesis explicitly departs from traditional static volume modeling and formulates mathematical representations for throughput volatility and operational turbulence:

### 1. Intraday Diurnal Absolute Volatility ($\sigma_{\text{TSA, hr}}$)
Measures the absolute dispersion of hourly screening counts across the 24 hours of calendar day $d$ (in passengers per hour dispersion):

$$\sigma_{\text{TSA, hr}}(d) = \sqrt{\frac{1}{23} \sum_{h=0}^{23} (y_{d, h} - \bar{y}_d)^2}$$

where $y_{d, h}$ represents hourly screened passengers and $\bar{y}_d = \frac{1}{24}\sum_{h=0}^{23} y_{d,h}$ is the daily mean hourly throughput. This target reflects the absolute peak-to-trough amplitude of passenger arrival waves.

### 2. Intraday Scale-Free Relative Volatility ($CV_{\text{TSA, hr}}$)
Normalizes intraday dispersion by average daily throughput:

$$CV_{\text{TSA, hr}}(d) = \frac{\sigma_{\text{TSA, hr}}(d)}{\bar{y}_d} = \frac{\sqrt{\frac{1}{23} \sum_{h=0}^{23} (y_{d, h} - \bar{y}_d)^2}}{\frac{1}{24} \sum_{h=0}^{23} y_{d, h}}$$

By removing baseline airport scale, this scale-free metric measures arrival burstiness and queue surge spikiness independent of facility size, enabling equitable comparisons between medium hubs and mega-connecting facilities.

### 3. Multi-Day Temporal Rolling Volatility ($\sigma_{\text{TSA, 7d}}$)
Measures the 7-day rolling standard deviation of daily passenger volume (in passengers per day):

$$\sigma_{\text{TSA, 7d}}(d) = \sqrt{\frac{1}{6} \sum_{k=0}^6 (Y_{d-k} - \bar{Y}_{7d})^2}$$

where $Y_d$ is total daily passenger volume and $\bar{Y}_{7d} = \frac{1}{7}\sum_{k=0}^6 Y_{d-k}$. This target captures medium-term multi-day passenger flow turbulence induced by convective storms, winter blizzards, and cascading cancellation shocks across the National Airspace System.

### 4. Daily Flight Departure Delay Dispersion ($\sigma_{\text{Delay}, d}$)
Measures the sample standard deviation of departure delays across uncancelled domestic flights on day $d$:

$$\sigma_{\text{Delay}, d} = \sqrt{\frac{1}{N_d - 1}\sum_{i=1}^{N_d} (\text{DepDelay}_{d,i} - \overline{\text{DepDelay}}_d)^2}$$

where $N_d$ is the number of uncancelled departures on day $d$.

### 5. The Coupled Volatility Index ($CVI_d$)
Quantifies the joint interaction between landside arrival variation and airside delay dispersion:

$$CVI_d = CV_{\text{TSA}, d} \times \sigma_{\text{Delay}, d}$$

Systemic queue breakdown is driven by the coupled volatility mismatch between landside passenger arrivals and airside flight departures.

### 6. Diurnal Operational Turbulence Shock Index ($T_{dow}(h)$)
For each hour $h \in [0, 23]$ conditioned on day of week ($dow$):

$$T_{dow}(h) = \max\left( \frac{\sigma_{\text{TSA}, dow}(h)}{\max_k \sigma_{\text{TSA}, dow}(k)}, \frac{\sigma_{\text{intra}, dow}(h) + \sigma_{\text{inter}, dow}(h) \cdot \mathbb{I}(F_{dow}(h) \ge 20)}{\max_k (\sigma_{\text{intra}, dow}(k) + \sigma_{\text{inter}, dow}(k) \cdot \mathbb{I}(F_{dow}(h) \ge 20))} \right)$$

Applying 1D K-Means clustering ($k = 3$) establishes three operational diurnal regimes:
* `1_OFF_PEAK` ($T < 0.35$): Overnight curfew valley characterized by minimal activity.
* `2_MID_PEAK` ($0.35 \le T < 0.75$): Midday steady flow with balanced throughput.
* `3_PEAK` ($T \ge 0.75$): Queuing turbulence driven by acute arrival surges or delay cascades.

---"""
    doc.append(sec_b.replace("{{TABLE_B1}}", formatted_table_b1))

    # Appendix C
    sec_c = r"""# Appendix C: Methodological Foundations, 4-Tier Filtering Pipeline, and Cohort Econometric Validation

> *Note on Thesis Cross-References*: This appendix details the sampling strategy, 4-tier filtering rationale, threat remediation protocols, and econometric validation of single-carrier checkpoint isolation. It is referenced in **Chapter III (Methodology)**, Section *Sample (Macro Categorization & Micro-Level Refinement)*, Section *Four-Tiered Purposive Filtering Pipeline*, and Section *Internal Validity Threats and Remediation Protocols*; and in **Chapter IV (Results)**, Section *Data Filtering and Subset Selection (Four-Phase Filtering Pipeline & Pipeline Results)*, Section *Key Airport Selection Contrasts*, Section *Econometric Validation of Carrier Checkpoint Isolation*, and Section *Local Seasonal and Day-of-Week Differences Across the Nine Selected Airports*.

## C.1 Methodological Assumptions and Threat Remediation Protocols

To ensure rigorous internal and external construct validity across all downstream models, 14 foundational methodological assumptions were operationalized across the research design. Table C.1 documents these assumptions, their mathematical and operational justifications, and the critical failure modes prevented.

### Table C.1
*Methodological Assumptions and Failure Mode Prevention Matrix*

{{TABLE_C1}}

*Note.* Adapted from `figures/04_Appendix_and_Reference/methodological_assumptions.csv`. Formulates the 14-point methodological safeguards isolating genuine passenger screening queues from upstream schedule and network artifacts.

Figure C.1 illustrates the architectural relationship between these methodological safeguards and the terminal queuing pipeline.

Figure C.1  
*Methodological Assumptions and Threat Remediation Architecture*

![Figure C.1: Methodological Assumptions and Threat Remediation Architecture](../../figures/04_Appendix_and_Reference/methodological%20assumptions.png)

*Note.* Diagrammatic layout of the 14-point threat remediation architecture establishing boundary controls from flight dispatch through checkpoint lanes.

### Specific Validity Threats and Operational Formulations
1. **Internal Validity Threats and Remediation Protocols**:  
   A primary threat to internal model validity is the presence of connecting passengers who remain airside and do not pass through a public checkpoint in load factor data. Including them in checkpoint demand estimates inflates predicted originating demand (the "Hub Disconnect"). To reduce this bias, origin-and-destination survey data (BTS DB1B) and airport-specific O&D ratios are used to estimate and remove connecting traffic from passenger flow calculations, isolating true originating landside checkpoint demand.
2. **Construct Validity Threats and Operational Formulations**:  
   Construct validity is affected by checkpoint heterogeneity, as raw lane counts obtained from TSA throughput data combine different screening modes, such as TSA PreCheck, with standard screening lanes, each exhibiting disparate processing rates ($\approx 250\text{--}300$ pax/lane-hr for PreCheck vs. $\approx 150\text{--}180$ pax/lane-hr for standard). To resolve this heterogeneity threat, the methodology constructs scale-free relative volatility metrics ($CV_{\text{TSA}}$) and standardized lane measures rather than unadjusted raw totals.

---

## C.2 Four-Tier Purposive Filtering Pipeline Architecture and Rationale

To systematically evaluate forecasting performance across deterministic baselines, probabilistic architectures, and hybrid queuing models, a multi-tiered, purposive sampling framework was employed to select nine target airfields (BOS, DFW, DTW, EWR, IAH, LAX, LGA, ORD, PHL). Candidate airports were filtered according to four sequential operational criteria:

### Phase 1: Macro Filter (Heavy-Traffic Scale and Checkpoint Congestion)
* **Filtering Criteria**: Restrict the national candidate universe of 450+ commercial airports to the Top 25 commercial airfields ranked by domestic passenger enplanements, capturing 67.2% of nationwide domestic flight movements.
* **Methodological Justification**: In airport queuing dynamics, traffic intensity $\rho_t = \frac{\lambda_t}{c_t \cdot \mu}$ determines queue behavior. Under Kingman's heavy-traffic approximation ($W_q \approx \frac{\rho}{1-\rho}\frac{C_a^2+C_s^2}{2}\frac{1}{\mu}$), passenger delays scale non-linearly only as checkpoint utilization approaches capacity ($\rho_t \to 1.0$). At small regional airports, passenger flow is sparse ($\rho_t \ll 0.3$), preventing queue accumulation and causing throughput to passively mirror unconstrained arrivals without boundary friction. In contrast, Top 25 hub airports reach peak-hour saturation ($\rho_t \to 1.0$) during morning (06:00–08:30) and evening (16:00–18:30) departure banks, generating the empirical queue delays and non-linear dynamics required to train and evaluate congestion-aware models.
* **TSA-OTP Relationship Evolution**: Across the nationwide universe of all commercial airfields, the linear correlation between scheduled flight departures and TSA throughput is low ($r \approx 0.35, R^2 \approx 12.25\%$). At the Top 25 macro scale, this relationship strengthens to $r = 0.4572$ ($R^2 = 20.90\%$) for raw volume, and $r = 0.6704$ ($R^2 = 44.94\%$) when deflated by DB1B connecting ratios.

### Phase 2: Meso Filter (Operational Homogeneity and Southwest Exclusion)
* **Filtering Criteria**: Require concurrent domestic mainline operations by American Airlines, Delta Air Lines, and United Airlines ($>10\%$ market share each), while systematically excluding Southwest Airlines (WN) and Ultra-Low-Cost Carriers (ULCCs). This reduced the pool from 25 to 14 candidate hub airfields.
* **Methodological Justification**: Concurrent legacy carrier operations ensure that cross-carrier comparisons evaluate under identical exogenous airspace conditions ($\delta_t$), canceling common weather ground delay programs and FAA flow management initiatives. Furthermore, Southwest Airlines was excluded due to its passenger arrival behavior: legacy carrier passengers display consistent, unimodal lognormal arrival timing ($\tau \sim \text{Lognormal}, E[\tau] \approx 105\text{ min}$), whereas Southwest's historical open-seating boarding structure and two-free-checked-bags policy generate a bimodal arrival mixture ($\mu_1 \approx 135\text{ min}$ for boarding group maximizers; $\mu_2 \approx 65\text{ min}$ for carry-on business travelers; Pearson, 1894), violating arrival distribution exchangeability ($f_j(\tau) \neq f(\tau)$).
* **TSA-OTP Relationship Evolution**: In the 14-airfield Meso cohort, eliminating Southwest and ULCC scheduling volatility elevated the scheduled flight to TSA throughput correlation to $r = 0.5015$ ($R^2 = 25.15\%$).

### Phase 3: Micro Filter (Carrier Checkpoint Exclusivity)
* **Filtering Criteria**: Require strict single-carrier dedicated screening checkpoint complexes ($P(\text{Carrier} = j^* \mid \text{Checkpoint}_k) = 1.0$). Airfields with shared multi-carrier central screening checkpoints were excluded. This filtered the 14 candidate hubs down to 9 selected airfields.
* **Methodological Justification**: In shared terminal facilities (e.g., Salt Lake City or Phoenix), multiple airlines funnel passengers into shared security queues. Because hub carriers coordinate flight banks, carrier departure schedules are collinear ($\text{Corr}(S_j, S_{j'}) \ge 0.88$, condition number $\kappa > 10^4$), preventing mathematical separation of individual carrier demand. Restricting analysis to dedicated checkpoint complexes collapses collinearity ($\kappa < 25$), directly mapping carrier flight banks to landside checkpoint queues.
* **TSA-OTP Relationship Evolution**: At the airport-wide level for the 9 selected airfields, scheduled flights versus total TSA passengers achieve $r = 0.5453$ ($R^2 = 29.74\%$), while scheduled flights versus true local originating TSA demand (DB1B adjusted) reaches $r = 0.6466$ ($R^2 = 41.81\%$). Furthermore, when evaluated at the dedicated checkpoint complex level, carrier-filtered departing seats explain $70.80\%$ to $77.40\%$ ($R^2$) of checkpoint throughput variance.

### Phase 4: Factorial Cohort (Factorial Matrix Balance)
* **Filtering Criteria**: Construct a balanced factorial matrix across legacy carriers and operational archetypes, retaining the **9-Airport Experimental Cohort** comprising **12 Dedicated Checkpoint Complexes** across BOS, DFW, DTW, EWR, IAH, LAX, LGA, ORD, and PHL.
* **Methodological Justification**: Complete factorial symmetry requires exactly 4 dedicated terminal screening complexes per legacy carrier (American: 4, Delta: 4, United: 4) spanning all four operational clusters (Mega-Connecting Gateways, High-Density O&D Focus, High-Reliability Fortress Hubs, and Congested Coastal Originators) and all four terminal physical archetypes (Decentralized, Linear Mega-Concourse, Multi-Terminal Ring, and Satellite). This orthogonal variation is structurally required to evaluate zero-shot Generalizability across diverse spatial configurations.
* **Crucial Methodological Distinction**: These evolving correlations and seasonal dynamics serve exclusively to justify the four-tier filtering rationale and confirm data validity. **These relationships and dynamics are not used in training the downstream predictive models**, preserving strict econometric separation and preventing data leakage. Furthermore, the analysis at this stage evaluates the 9 selected airports as complete facilities, rather than premature facility checkpoints.

### Table C.2
*Four-Tier Purposive Filtering Pipeline Architecture and Progression Rationale*

| Filtering Tier | Candidate Universe | Inclusion & Exclusion Criteria | Methodological & Queuing Rationale | Scheduled Flight Coupling ($r$) | Throughput Variance Explained ($R^2$) |
| :--- | :--- | :--- | :--- | :---: | :---: |
| **Phase 1: Macro Filter** | $N = 450+ \to 25$ Hubs | Top 25 airfields by commercial enplanements; captures 67.2% of domestic departures | Enforces heavy-traffic queuing limit ($\rho_t \to 1.0$); eliminates regional light-traffic triviality | $r = 0.4572$ (Raw)<br>$r = 0.6704$ (DB1B) | $R^2 = 20.90\%$ (Raw)<br>$R^2 = 44.94\%$ (DB1B) |
| **Phase 2: Meso Filter** | $N = 25 \to 14$ Hubs | Concurrent Big 3 legacy presence (>10% share); excludes Southwest (WN) and ULCCs | Exogenous airspace shock differencing; eliminates bimodal open-seating arrival mixture ($\mu_1 \approx 135$m, $\mu_2 \approx 65$m) | $r = 0.5015$ | $R^2 = 25.15\%$ |
| **Phase 3: Micro Filter** | $N = 14 \to 9$ Hubs | Dedicated single-carrier checkpoint complexes ($P(j^* \mid \text{Checkpoint}) = 1.0$) | Collapses cross-carrier schedule collinearity ($\kappa > 10^4 \to \kappa < 25$); eliminates shared-lane dilution | $r = 0.5453$ (Raw)<br>$r = 0.6466$ (DB1B) | $R^2 = 29.74\%$ (Raw)<br>$R^2 = 41.81\%$ (DB1B) |
| **Phase 4: Factorial Cohort** | $N = 9$ Hubs (12 Complexes) | Balanced $4 \times 4$ matrix: exactly 4 exclusive complexes per carrier across 4 clusters | Unconfounded ANOVA variance structure; enables zero-shot spatial transferability | $r = 0.8414\text{--}0.8798$ | $R^2 = 70.80\%\text{--}77.40\%$ |

*Note.* Evolving correlations reflect progressive noise elimination across macro, meso, micro, and factorial sample specifications.

Figure C.2 illustrates the complete balanced factorial cohort matrix across the 4 operational cluster archetypes and 3 legacy carriers.

Figure C.2  
*Four-Cluster Carrier Matrix and Spatial Transferability*

![Figure C.2: Four-Cluster Carrier Matrix and Spatial Transferability](../../figures/01_Sample_and_Airport_Selection/Power%20of%209%20airports.png)

*Note.* Adapted from `figures/01_Sample_and_Airport_Selection/power_of_9_airports.csv`. Visualizes the orthogonal 4-cluster $\times$ 3-carrier factorial design enabling intra-cluster transfer testing (e.g., EWR $\to$ LGA within Cluster 3).

---

## C.3 Econometric Validation of Carrier Checkpoint Isolation

To mathematically verify that dedicated checkpoints isolate single-carrier demand without unobserved leakage from adjacent airline operations, four formal econometric tests were conducted:

1. **Volume Conservation Test**: Total daily checkpoint throughput tracks carrier ticketed boardings with slope $\rho = 1.00 \pm 0.04$ ($R^2 > 0.95$), proving mass conservation between landside entries and aircraft boardings.
2. **Zero-Flight Intercept Test**: Checkpoint demand when zero carrier flights are scheduled is statistically indistinguishable from zero ($\beta_0 = 12.4\text{ pax/hr}, p = 0.40$), proving that non-carrier passengers do not cross into dedicated lanes.
3. **Cross-Carrier Perpendicularity Test**: Regressing dedicated checkpoint throughput against concurrent departures by other airlines operating in adjacent terminals yields non-significant coefficients ($\beta_{\text{other}} = 0.002, p = 0.62$), confirming zero cross-carrier schedule leakage.
4. **Terminal Layout Invariance Test**: A two-sample Kolmogorov-Smirnov test comparing physically separate terminals (e.g., LGA Terminal C, DTW McNamara) against walkway-connected terminals (e.g., DFW Terminal E, LAX Terminal 4) yielded $D = 0.032$ ($p = 0.28$), confirming that airside walkway connections do not induce statistically significant cross-terminal throughput leakage.

### Table C.3
*Econometric Tests for Carrier Checkpoint Demand Isolation*

| Econometric Validation Test | Econometric Specification / Statistic | Null Hypothesis ($H_0$) | Test Result & Statistical Significance | Operational Interpretation & Integrity Verdict |
| :--- | :--- | :--- | :--- | :--- |
| **1. Volume Conservation Test** | Regress daily TSA throughput on carrier ticketed enplanements | $\beta_1 = 1.00$ (Slope unity) | $\hat{\beta}_1 = 1.00 \pm 0.04, R^2 > 0.95$ | **Passed**: Checkpoint volume precisely accounts for boarded passenger inventory. |
| **2. Zero-Flight Intercept Test** | Estimated throughput when scheduled departing flights $= 0$ | $\beta_0 = 0$ (Zero base load) | $\hat{\beta}_0 = 12.4\text{ pax/hr}, p = 0.40$ | **Passed**: No phantom or unassigned passenger flow enters dedicated screening lines. |
| **3. Cross-Carrier Perpendicularity** | Partial correlation with competing airline flight departures | $\beta_{\text{competing}} = 0$ | $\hat{\beta}_{\text{other}} = 0.002, p = 0.62$ | **Passed**: Adjacent terminal schedule waves do not spill over into dedicated screening queues. |
| **4. Terminal Layout Invariance** | Two-sample Kolmogorov-Smirnov test: Separate vs. Connected | $F_{\text{separate}}(y) = F_{\text{connected}}(y)$ | $D = 0.032, p = 0.28$ | **Passed**: Airside walkways do not induce statistically significant throughput distortion. |

*Note.* Confirms mathematical separation of carrier demand across the 12 dedicated screening complexes.

---

## C.4 Key Airport Selection Contrasts and Cohort Density Profiles

### Structural Facility Contrasts
* **LGA vs. JFK Selection**: United Airlines permanently ceased operations at JFK in October 2022 (failing Meso multi-carrier continuity). In contrast, LGA opened Delta's state-of-the-art consolidated Terminal C in June 2022, providing unconfounded screening lanes with 100% carrier exclusivity.
* **PHL vs. SLC Selection**: Salt Lake City International (SLC) channels all airlines through a single consolidated central screening checkpoint, making carrier isolation structurally impossible. Philadelphia International (PHL) provides dedicated American Airlines checkpoints in Terminals B and C, ensuring clean carrier isolation within Cluster 2.

### Table C.4
*Summary Descriptive Statistics: Nine-Airport Experimental Cohort vs. Top 25 Airfield Network Profile*

{{TABLE_C4}}

*Note.* Adapted from `results/manuscript_tables/table_4_7.csv`. Illustrates that the 9-airport experimental cohort exhibits +16.9% higher flight density, +7.2% higher departure delays, +14.1% higher cancellation rates, and +25.0% higher local originating passenger volume than the broader Top 25 network, ensuring deep exposure to heavy-traffic queuing dynamics.

### Table C.5
*Day-of-Week Mean Daily Passenger Throughput and Ratio Profiles Across the Nine Selected Airports*

{{TABLE_C5}}

*Note.* Adapted from `results/manuscript_tables/table_4_8.csv`. Documents local weekly profiles across the 9 airports:
* **The Pure Corporate Profile (LGA)**: LaGuardia exhibits an extreme day-of-week ratio of 2.30. Throughput peaks on Monday (49,002 pax) and Sunday (48,000 pax) driven by corporate business travel in the Northeast corridor, while Friday drops to 21,310 pax due to business travelers returning home early and leisure travelers avoiding slot-constrained short-haul airfields.
* **The Corporate-to-Weekend Profile (BOS, EWR, PHL, DTW, DFW)**: These facilities peak on Friday (52,244 at BOS; 73,625 at DFW; 69,206 at EWR) as business travelers depart for weekend destinations and leisure getaways overlap, with Tuesday serving as the weekly volume trough (Peak/Trough ratio = 1.14 to 1.23).
* **The Energy Sector & Midweek Profile (IAH, ORD)**: Houston Bush and Chicago O'Hare experience Thursday peaks (53,351 at IAH; 50,706 at ORD) driven by consulting, engineering, and corporate travel schedules, followed by steep Saturday troughs (ratio = 1.19 to 1.26).

---"""
    doc.append(sec_c.replace("{{TABLE_C1}}", formatted_assumptions).replace("{{TABLE_C4}}", formatted_table_4_7).replace("{{TABLE_C5}}", formatted_table_4_8))

    # Appendix D
    sec_d = r"""# Appendix D: Aviation Data Engineering, Warehouse Architecture, and Hygiene Protocols

> *Note on Thesis Cross-References*: This appendix documents the multi-source data feeds, conformed Star Schema staging pipeline, ETL transformations, and feature engineering protocols. It is referenced in **Chapter III (Methodology)**, Section *Temporal Scope and Boundary Definition*, Section *Sources of Data (TSA FOIA, BTS OTP, BTS Form 41 T-100, BTS DB1B)*, Section *Treatment of Data (Extract, Transform, Load)*, and Section *Feature Engineering*; and in **Chapter IV (Results)**, Section *TSA and OTP Throughput Data* and Section *Descriptive Statistics*.

## D.1 Multi-Source Aviation Data Foundation Census and Base Feeds

The analytical data warehouse unifies four authoritative federal aviation feeds spanning the post-pandemic operational era (May 1, 2022 to December 31, 2025):
1. **TSA FOIA Checkpoint Logs**: Obtained via Freedom of Information Act (FOIA) disclosures and cross-referenced with public archival repositories, this feed records hourly passenger screening counts per physical lane across all commercial airports ($19,500,286$ raw records). Following conformed extraction, the warehouse preserves $6,434,732$ lane-hour records across 955 screening lanes at the Top 25 airfields, tracking $2.70$ billion screened passengers.
2. **BTS On-Time Flight Performance (OTP, Form 234)**: Maintained by the Bureau of Transportation Statistics, this feed records individual domestic flight movements ($45,777,091$ raw records). The post-ETL warehouse retains $13,153,654$ domestic departures across 17 reporting carriers, capturing departure delays, taxi-out times, tactical cancellations, and delay cause decompositions.
3. **BTS Form 41 Schedule T-100 Domestic Segment Data**: Published by the BTS Office of Airline Information, Form 41 captures monthly carrier-route-equipment capacity ($1,945,451$ raw records; $422,096$ cleaned observations), providing departing seats, transported passengers, and route load factors.
4. **BTS Origin-Destination Ticket Surveys (DB1B/DB1C)**: A 10% randomized sample of airline ticket itineraries ($12,910,384$ raw coupons; $22,051,557$ conformed coupon records), supplemented by authorized monthly airport traffic reports (such as LAX Air Traffic Statistics). These feeds are utilized to extract quarterly connecting passenger ratios across airport pairs to support originating passenger flow estimation.

### Table D.1
*Master Multi-Source Aviation Data Foundation Census & Base Feed Profiles*

{{TABLE_D1}}

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

{{TABLE_D2}}

*Note.* Adapted from `figures/04_Appendix_and_Reference/dataset_breakdown.csv`. Summarizes feature store files, analytical grain, row counts, and compressed vs. uncompressed storage memory profiles.

### Table D.3
*Filtered Nine-Airport Target Research Cohort Parquet File Profiles*

{{TABLE_D3}}

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

{{TABLE_D4}}

*Note.* Adapted from `figures/04_Appendix_and_Reference/bts_db1b_table_hierarchy.csv`. Details the itinerary representation across ticket, market, and coupon grains used to compute airport-specific connecting deflators: $\text{Demand}_{\text{orig}, t} = \sum \text{Seats}_f \cdot \text{LF}_f \cdot (1 - \text{ConnRatio})$.

Figure D.4 illustrates the structural coupon hierarchy and connecting passenger deflator workflow.

Figure D.4  
*Bureau of Transportation Statistics DB1B Ticket Survey Data Hierarchy*

![Figure D.4: Bureau of Transportation Statistics DB1B Ticket Survey Data Hierarchy](../../figures/04_Appendix_and_Reference/BTS-DB1B_Appendix.png)

*Note.* Visual breakdown of Ticket, Market, and Coupon tables used to de-duplicate transferring passengers.

---

## D.4 Comprehensive Staging ETL Pipeline and Data Hygiene Protocols

The execution of data preparation follows a rigorous, sequential Extract, Transform, Load (ETL) pipeline designed to ingest, clean, standardize, and align the aviation datasets:

### Extract Protocol
1. Download TSA Throughput files from the FOIA reading room (PDFs) spanning 2019 to 2026.
2. Parse PDFs into standardized tabular format (CSV).
3. Download TSA Throughput PDFs and CSVs (2022–2025) from public repository archives (e.g., `https://github.com/mikelor/TsaThroughput`).
4. Cross-reference TSA datapoints to identify temporal gaps, duplicates, and reporting inconsistencies.
5. Download On-Time Flight Performance data (CSVs) spanning 2019 to 2026 for all domestic flights in the United States.
6. Download BTS Form 41 Schedule T-100 Segment Airline Traffic Data and calculate monthly route load factors.
7. Download BTS DB1B ticket survey coupon files and airport-specific origin-and-destination summary statistics.
8. Perform an audit across the 7-year sequence to identify missing data and reporting discontinuities.

### Transform Protocol
1. Standardize timestamps across all feeds to a uniform operational clock (local airport solar operational time).
2. Map and resolve typographical errors, airport names, data mismatches, and checkpoint naming variations.
3. Normalize airport codes, checkpoint prefixes, and common terms (e.g., `Checkpoint` $\to$ `CKPT`).
4. **Spatial Key Resolution and Unidentified Airport Isolation**: Upstream raw TSA logs contained 35,809 records with missing or corrupted airport strings. An automated checkpoint fingerprinting algorithm successfully mapped 7,489 records by identifying unique physical checkpoint string signatures (`dim_checkpoint`). The remaining 22,190 unresolvable records were assigned to a dedicated null surrogate key (`airportId = 0`, flagged with `airportMissing = 1`), preventing the creation of an artificial 9.71-million passenger "phantom airport" that would have distorted econometric demand baselines. All downstream analyses strictly enforce `airportMissing = 0` and `airportId > 0`.
5. **Preserving Scheduled Checkpoint Closures as True Operational Zeros**: A critical operational feature of airport checkpoints is zero throughput during overnight curfews. Across the warehouse, 450,973 records (2.31%) reported zero passengers. Cross-referencing flight movements established that 98.6% of zero values occur between 00:00 and 03:59 local time. Rather than applying moving-average or spline imputations—which would fabricate passenger volume during scheduled overnight lane closures—these intervals were preserved as true operational structural zeros and modeled through zero-bounded count regression (a Tweedie compound Poisson distribution, $p = 1.3$, which naturally accommodates real zero counts without producing impossible negative passenger estimates or requiring artificial data smoothing).
6. **Advance vs. Tactical Cancellation Causality**: Across the 13,153,654 domestic departures, flight cancellations averaged 2.03% (267,019 operations), with 99.4% of unassigned aircraft tail numbers occurring on cancelled flights. To prevent lookahead bias in passenger forecasting (the error of using future information that an airport operations manager would not possess in real time), advance cancellations (>24 hours prior to scheduled departure) were purged from departing seat supply curves, while tactical cancellations (<2 hours prior) were retained, reflecting the operational reality that booked passengers had already completed landside security screening before the carrier issued the cancellation.
7. Separate scheduled flights from actual operated flights to distinguish planned bank structures from tactical executions.
8. Estimate aircraft seat capacities using flight distance, carrier identity, and aircraft equipment/tail-number characteristics.
9. Scale seat counts using route-level load factor data to estimate departing passenger volume.
10. Merge datasets to determine terminal-specific connecting passengers within target complexes using DB1B ticket survey deflators.
11. **Empirical Passenger Show-Up Curve Convolution**: Convolve scheduled flight departure banks across empirical lead-time distributions ($t+1, t+2, t+3$ from ACRP Report 40) and align them with hourly TSA throughput intervals to produce the final conformed modeling dataset.
12. Construct the Values versus Volatility feature representation space:
    * *Feature Values (Levels, 14 Attributes)*: Schedule Scale (`sched_daily_total`, `actual_daily_total`, `sched_hourly_mean`, `sched_rolling_7d_mean`), Cancellations (`daily_cancellations`, `daily_cancel_rate`, `cancel_rolling_7d_mean`, `cancel_rate_rolling_7d_mean`), Delays (`avg_dep_delay_minutes`, `flights_delayed_15min_pct`), Surface Queues (`avg_taxi_out_minutes`), and Network Buffers (`aircraft_gauge_seats`, `route_load_factor_pct`, `connecting_passenger_share_pct`).
    * *Feature Volatilities (Dispersion, 10 Attributes)*: Schedule Dispersion (`sched_hourly_std`, `sched_hourly_cv`, `actual_hourly_std`, `actual_hourly_cv`, `sched_rolling_7d_std`, `sched_rolling_7d_cv`), Cancellation Dispersion (`cancel_rolling_7d_std`, `cancel_rate_rolling_7d_std`, `otp_cancellation_volatility_cv`), and Delay Dispersion (`otp_departure_delay_volatility_cv`).
    * *Combined Dual Paradigm (24 Attributes)*: Interacts both feature spaces to test predictive complementarity.

### Load Protocol
1. Load master conformed data copies to secure persistent cloud storage (OneDrive) and local data warehouse directories.
2. Build relational analytics tables, lookup dimensions, and multidimensional interaction grids.
3. Automate verification audits for schema validity, referential integrity, and row preservation across the 7-year sequence.

### Descriptive Statistics for Post-ETL Data
At the macro network level, the 25 candidate airfields processed an annual mean of 192,160 scheduled commercial domestic departures ($\sigma = 69,376$; median = 177,182), ranging from 95,849 departures at Washington Dulles (IAD) to 360,571 departures at Chicago O'Hare (ORD). Systemwide passenger screening throughput averaged 68.50 million passengers per airfield annually ($\sigma = 27.76$M; median = 66.01M), with Charlotte Douglas (CLT) recording 28.17 million passengers and Los Angeles International (LAX) processing 129.07 million passengers across the multi-year study period.

---

## D.5 Empirical Passenger Show-Up Curve Convolution and Feature Engineering Pipeline

Scheduled flight departures cannot be mapped to checkpoint arrival intervals on a 1-to-1 contemporaneous basis. Drawing upon empirical traveler arrival distributions from ACRP Report 40 (Airport Passenger Terminal Planning and Design; TRB, 2010), scheduled departing seats were convolved across discrete lead horizons ($t+1, t+2, t+3$):

$$\text{Demand}_{\text{convolved}, t} = \sum_{h=1}^3 w_h \cdot \left[ \sum_{f \in \mathcal{F}_{t+h}} \text{Seats}_f \cdot \text{LoadFactor}_f \cdot (1 - \text{ConnectingRatio}) \right]$$

where empirical weights $w_1 = 0.35$ ($t-1$ / final hour), $w_2 = 0.50$ ($t-2$ / primary arrival window), and $w_3 = 0.15$ ($t-3$ / early arrivals) match empirical ACRP Report 40 arrival distributions. (Alternatively parameterized in forward-convolving operational engines as $w_1 = 0.52, w_2 = 0.38, w_3 = 0.10$). In operational terms, this convolution maps scheduled airline departure banks backward in time to reflect when travelers physically enter the terminal. Rather than assuming passengers arrive during their flight's departure hour, the convolution distributes departing seat capacity across the preceding three hours according to empirical behavioral show-up curves.

The complete feature engineering pipeline encompasses five functional operational domains:
1. **Convolved Flight Schedule Volatility Features**: Lead-lag convolved seats, carrier-exclusive scheduled bank dispersion (`sched_hourly_std`, `sched_hourly_cv`), and rolling schedule volatility (`sched_rolling_7d_std`, `sched_rolling_7d_cv`).
2. **Airside Delay and Congestion Features**: Lagged mean departure delay ($t-1$), departure delay dispersion ($\sigma_{\text{Delay}}$), significant delay rate ($\% \ge 15$ min), taxi-out duration, and tactical cancellation counts.
3. **Temporal Cyclical Encodings**: Sine and cosine harmonic transformations of hour-of-day (24-hour cycle) and day-of-week (7-day cycle) to preserve circular continuity across midnight and week boundaries.
4. **Operational Regime Indicators**: Categorical encodings of the 84-cell interaction grid (Season $\times$ Day of Week $\times$ Diurnal Peak Block).
5. **Facility and Aircraft Features**: Screening lane count, checkpoint configuration type (finger pier vs. central hall), mean aircraft seating capacity, and monthly route load factor.

---"""
    doc.append(sec_d.replace("{{TABLE_D1}}", formatted_db_profiles).replace("{{TABLE_D2}}", formatted_dataset_breakdown).replace("{{TABLE_D3}}", formatted_data_top9).replace("{{TABLE_D4}}", formatted_db1b_hierarchy))

    # Appendix E
    sec_e = r"""# Appendix E: Seasonal Volatility Regimes, Operational Taxonomies, and Diurnal Queue Dynamics

> *Note on Thesis Cross-References*: This appendix establishes the three-tier operational taxonomy, empirical seasonal volatility regimes, day-of-week dynamics, and diurnal queue turbulence baselines. It is referenced in **Chapter III (Methodology)**, Section *Quantitative Evaluation Dimensions and Operational Regimes*; in **Chapter IV (Results)**, Section *Defining Seasonality (Annual Seasonal Regimes and Coupled Volatility, Day-of-Week Cyclical Dynamics and Archetypes, Diurnal Non-Consecutive Dual Turbulence Peaks)*; and in **Chapter V (Discussion)**, Section *The Lead-Lag Asynchrony Mechanism* and Section *Robustness Across the Interaction Grid and Prevention of Delay Distortion*.

## E.1 Three-Tier Operational Taxonomy

Airport operating conditions were classified into a defensible three-tier operational taxonomy grounded in FAA Air Traffic Organization and DOT Bureau of Transportation Statistics regulatory standards:

* **Tier 1: Nominal On-Time Baseline**: Departure delays $< 15$ minutes and zero tactical cancellations ($N_{\text{cancels}} = 0$). Grounded in the FAA/DOT A14 regulatory reference benchmark, this regime serves as an experimental control observing pure passenger show-up curves without airside delay distortion.
* **Tier 2: Routine Daily Operations**: Everyday commercial hub operations characterized by ambient 15–30 minute delays, gate holds, and normal 1–2% cancellation churn.
* **Tier 3: Irregular Operations (IROPS)**: Severe convective disruptions, ground delay programs (GDP), and winter weather cascades, defined as hours where departure delays $\ge 45$ minutes or tactical cancellations $\ge 5$.

---

## E.2 Annual Seasonal Volatility Regimes and Coupled Volatility

Commercial aviation stress varies substantially across the calendar year. By analyzing daily within-day passenger arrival coefficient of variation ($CV_{\text{TSA}}$) alongside flight departure delay dispersion ($\sigma_{\text{Delay}}$) across 1,341 post-demarcation days across the Top 25 network, four distinct annual seasonal volatility regimes were established:

$$CVI_d = CV_{\text{TSA}, d} \times \sigma_{\text{Delay}, d}$$

Across the annual calendar, delay dispersion ($\sigma_{\text{Delay}}$) expands monotonically from 46.09 minutes during the winter lull to 68.43 minutes during the summer peak (+48.5% dispersion expansion), driving the Coupled Volatility Index from 27.85 to 39.36 (+41.3%), while flight cancellation rates more than triple from 0.89% to 3.16%.

### Table E.1
*Master Annual Seasonal Volatility Regimes Summary (Top 25 Airfields, $N = 1,341$ Days)*

{{TABLE_E1}}

*Note.* Adapted from `results/manuscript_tables/table_4_3b.csv`. Across the calendar year, flight departure delay dispersion ($\sigma_{\text{Delay}}$) expands monotonically from 46.09 minutes during the winter lull to 68.43 minutes during the summer peak (+48.5%), driving the Coupled Volatility Index from 27.85 to 39.36 (+41.3%) and tripling cancellation rates (0.89% to 3.16%).

---

## E.3 Day-of-Week Volatility Dynamics and Operational Archetypes

Standardizing observations under ISO 8601 ($1 = \text{Monday}, \dots, 7 = \text{Sunday}$) across all Top 25 airfields yields three primary weekly operational archetypes:

1. **Midweek Operational Reset (Tuesday & Wednesday)**: Tuesday and Wednesday represent the most stable operational periods of the week, characterized by the lowest departure delay dispersion ($\sigma_{\text{Delay}} = 50.09\text{ min}$ and $49.27\text{ min}$), lowest share of delayed flights ($19.44\%$ and $20.05\%$), and lowest Coupled Volatility Indices (29.99 and 29.13).
2. **Outbound Corporate Surge (Monday & Thursday)**: Mondays experience the highest within-day TSA arrival volatility across the entire week ($CV = 0.604, CVI = 34.00$), driven by concentrated early-morning business traveler screening banks.
3. **Leisure Return Delay Propagation (Sunday)**: Sundays exhibit the most severe network-wide delay cascades, generating the highest mean departure delay (17.78 min), highest delay dispersion ($\sigma_{\text{Delay}} = 58.07\text{ min}$), and highest rate of flights delayed $\ge 15$ minutes ($25.60\%$).

### Table E.2
*Day-of-Week Volatility Dynamics and Operational Archetypes (Top 25 Airfields, $N = 1,341$ Days)*

{{TABLE_E2}}

*Note.* Adapted from `results/manuscript_tables/table_4_4a.csv`. Establishes empirical cyclical volatility baselines across weekly commercial flight schedules.

---

## E.4 Bimodal Intraday Operational Dynamics: Morning Surge vs. Evening Delay Cascade

Rather than dividing operational days into arbitrary uniform hourly intervals, operations are categorized into three regimes capturing the bimodal diurnal congestion structure of commercial airfields:
* **Off-Peak (00:00–03:00, 3–4 hours daily)**: Overnight curfew valley characterized by sparse departures and minimal checkpoint activity.
* **Mid-Peak (08:00–13:00/16:00, 4–12 hours daily)**: Steady midday plateau marked by consistent passenger screening rates and sufficient aircraft turnaround buffers.
* **Peak Regime**: Unifies two non-consecutive queuing congestion windows driven by distinct operational mechanisms:
  1. *The Morning Bank Surge (05:00–08:00)*: Governed by extreme passenger arrival variance ($\sigma_{\text{TSA}} > 11,380\text{ pax/hr}$ network-wide; complex-level $\sigma \sim 540\text{--}880\text{ pax/hr}$) as business travelers converge on initial outbound banks. Airside flight departure delays are low ($< 5\text{ min}$), and aircraft turnaround buffers are fresh.
  2. *The Evening Delay Cascade (14:00/17:00–22:00)*: Governed by cumulative upstream flight delay propagation across the National Airspace System ($\sigma_{\text{Delay}} > 63.4\text{ min}$). Screening volume is moderate and tapering, but delays severely disrupt passenger show-up synchronization.

### The Lead-Lag Asynchrony Mechanism
Traditional queuing models in airport terminal planning often assume that passenger arrival intensity $\lambda_t$ is directly proportional to departing flights in the same time window $t$. The empirical results completely dismantle this unshifted schedule assumption:
* **Pre-Departure Passenger Surge Window (Morning)**: Passengers arrive at screening checkpoints 90 to 120 minutes prior to scheduled departure. Thus, checkpoint arrival surges lead scheduled flight departure banks by approximately two hours. Morning peak screening occurs when flights are operating completely on schedule and terminal congestion is pure landside queuing friction.
* **Operational Lag Phase (Evening)**: As the day progresses, delay propagation across the National Airspace System (NAS) compounds. Aircraft arriving late from upstream hubs delay downstream departures. However, because outbound passengers have already arrived at the airport based on ticketed flight schedules, terminal lobbies become congested with waiting travelers while checkpoint queues dwindle. This decoupling explains why simultaneous flight and passenger modeling fails unless lead-lag convolutions are operationalized.

### The Diurnal Operational Turbulence Shock Index & 84-Cell Grid
For each hour $h \in [0, 23]$ conditioned on day of week ($dow$):

$$T_{dow}(h) = \max\left( \frac{\sigma_{\text{TSA}, dow}(h)}{\max_k \sigma_{\text{TSA}, dow}(k)}, \frac{\sigma_{\text{intra}, dow}(h) + \sigma_{\text{inter}, dow}(h) \cdot \mathbb{I}(F_{dow}(h) \ge 20)}{\max_k (\sigma_{\text{intra}, dow}(k) + \sigma_{\text{inter}, dow}(k) \cdot \mathbb{I}(F_{dow}(h) \ge 20))} \right)$$

Applying 1D K-Means clustering ($k = 3$) establishes three operational diurnal regimes: `1_OFF_PEAK` ($T < 0.35$), `2_MID_PEAK` ($0.35 \le T < 0.75$), and `3_PEAK` ($T \ge 0.75$).

The cross-classification of the 4 annual seasonal regimes ($\mathcal{S}$), 7 days of the week ($\mathcal{D}$), and 3 diurnal blocks ($\mathcal{H}$) forms an **84-Cell Operational Condition Matrix** ($\mathcal{G} = \mathcal{S} \times \mathcal{D} \times \mathcal{H}$). Across this operational matrix, 83 of 84 cells (98.8%) satisfy the statistical minimum power threshold of $N_{\text{train}} \ge 50$ (median $N_{\text{train}} = 215$), confirming that temporal stratification establishes ample sample depth without sparse-sample estimation bias.

### Preventing Extreme Storm Outliers from Distorting Normal-Day Decision Rules
When a predictive model is trained across all weather regimes simultaneously without separation, the model's rules become distorted by rare, extreme summer storm delays ($\sigma_{\text{Delay}} = 68.43\text{ min}$). Under pooled training, decision trees warp their rules to accommodate these rare storm spikes, degrading accuracy during clear, on-time operations. By conditioning training on distinct operational regimes, decision trees focus on direct operational drivers (route load factors, aircraft seat gauge, and empirical passenger show-up curves) rather than convective storm noise.

---"""
    doc.append(sec_e.replace("{{TABLE_E1}}", formatted_table_4_3b).replace("{{TABLE_E2}}", formatted_table_4_4a))

    # Appendix F
    sec_f = r"""# Appendix F: Model Evaluation Benchmarks, Resilience Mechanics, and the Values vs. Volatility Paradigm

> *Note on Thesis Cross-References*: This appendix presents the empirical holdout evaluation benchmarks across all three operational performance dimensions, resilience mechanics, and the econometric validation of the Values versus Volatility Paradigm ($H_2$). It is referenced in **Chapter III (Methodology)**, Section *Predictive Modeling Frameworks and Baseline Control*; in **Chapter IV (Results)**, Section *Model Development and Execution*, Section *Model Evaluation and Results*, Section *Empirical Confirmation of Asymmetric Trade-Offs (Hypothesis 1 Verified)*, and Section *The Values versus Volatility Paradigm Empirical Results*; and in **Chapter V (Discussion)**, Section *Evaluation Dimension 1: Robustness*, Section *Evaluation Dimension 2: Resilience*, Section *Evaluation Dimension 3: Generalizability*, and Section *Deep-Dive: Values versus Volatility Paradigm Across Temporal Horizons*.

## F.1 Master Multi-Pillar Hypothesis Evaluation Matrix

### Candidate Model Architecture and Mechanics
To evaluate the research questions, the investigation establishes three candidate models representing distinct operational paradigms, benchmarked against an empirical baseline control:
1. **The Baseline Control Benchmark (Daily Persistence)**:
   * *Operational Logic*: Assumes that checkpoint arrival volatility today will exactly mirror the volatility observed at the exact same hour yesterday ($\widehat{\text{Vol}}_t = \text{Vol}_{t-24}$).
   * *Evaluation Role*: Serves as the non-parametric reference standard ($\text{MASE} \equiv 1.000$). Any operational model worth deploying must prove that it beats this simple historical benchmark.
2. **Model 1: Deterministic Flight Schedule Model (Operational Baseline)**:
   * *Operational Logic*: Uses published airline flight schedules, shifted forward in time using empirical passenger show-up distributions from ACRP Report 40 (Airport Passenger Terminal Planning and Design).
   * *Mechanics*: Because passengers arrive 90 to 120 minutes before takeoff, scheduled flight departure banks are convolved across lead arrival horizons ($t+1, t+2, t+3$). This captures the operational ebb and flow of scheduled flight waves without requiring real-time delay telemetry or statistical machine learning.
3. **Model 2: Supervised Machine Learning Model (Flight Operations & Delays)**:
   * *Operational Logic*: Uses an automated decision-tree algorithm trained across the convolved flight schedule and 24 Bureau of Transportation Statistics (BTS) On-Time Performance (OTP) operational features.
   * *Mechanics*: The decision trees learn non-linear operational rules (e.g., how departure delays, tactical cancellations, and surface taxi queues ripple into checkpoint arrival dispersion). It tests whether airside operational data improves checkpoint forecasts over flight schedules alone.
4. **Model 3: Dynamic Two-Stage Hybrid Model (Schedule + Real-Time Feedback)**:
   * *Operational Logic*: Combines the structured foundation of airline flight schedules with live real-time feedback from the checkpoint floor.
   * *Mechanics*:
     * *Stage 1*: Captures recurring daily and weekly flight schedule cycles.
     * *Stage 2*: A decision tree predicts residual volatility shocks caused by flight delays and weather ground stops, dynamically incorporating live 1-step error feedback from the previous hour ($e_{t-1} = y_{t-1} - \hat{y}_{t-1}$). If lines are longer than the flight schedule predicted, the model immediately adjusts upward to track stranded passengers.

### Temporal Boundaries and Partitioning Design
The selected temporal boundary establishes a 32-month development span partitioned into:
* **Training Set**: 20 months (May 1, 2022 to December 31, 2023; 122,847 hourly observations across the filtered 9-airport complex cohort; 404,324 multi-facility observations across the Top 25 network).
* **Validation Set**: 12 months (January 1, 2024 to December 31, 2024; 72,723 hourly observations).
* **Out-of-Time Holdout Test Set**: 12 continuous months (January 1, 2025 to December 31, 2025; 72,053 complex-level observations across 3,222 test complex-days; 215,562 facility-level observations).
* A 7-day operational buffer between partitions prevents multi-day delay cascades from leaking across evaluation boundaries.

### Table F.1
*Master Multi-Pillar Hypothesis Evaluation Matrix (2025 Out-of-Time Holdout Suite, $N = 72,053$)*

{{TABLE_F1}}

*Note.* Adapted from `results/manuscript_tables/table_4_11.csv`. Confirms asymmetric operational trade-offs ($H_1$): Model 3 achieves lowest RMSE (222.1 pax/hr) and decisive resilience ($R_{\text{MASE}} = 1.05$); Model 2 wins Routine Pareto Efficiency ($\text{MASE} = 0.680\text{--}0.700$, zero feedback compute latency); and Model 1 wins Generalizability ($\text{RTR} = 1.04, \Delta\text{MASE} = +4.0\%$).

---

## F.2 Dimension 2: Resilience and Shock Performance Under Severe Operational Disruption

### Table F.2
*Evaluation Dimension 2: Resilience and Shock Performance Under Severe Operational Disruption (IROPS)*

{{TABLE_F2}}

*Note.* Adapted from `results/manuscript_tables/table_5_2.csv`. Evaluated during IROPS hours ($\text{Delay} \ge 45\text{ min}$ or $\text{Cancellations} \ge 5$).

### Resilience Mechanics and the Empty Checkpoint Fallacy
The coupled volatility findings explain the exact operational bottleneck mechanism during severe convective disruptions:
* **The "Empty Checkpoint Fallacy" in Pure Machine Learning**: During summer severe weather events, flight departure delays surge and cancellations spike. A pure machine learning model (Model 2) relying on flight schedules shifted by static show-up curves assumes that because flights scheduled for 18:00 have been delayed to 22:00 or ground-stopped, security checkpoints will experience an immediate demand collapse at 16:00. In reality, passengers arrived at the airport based on their original ticketed itineraries. Thousands of stranded travelers crowd security lines, re-screen after gate changes, or remain landside. Pure machine learning predicts an empty checkpoint, resulting in massive under-prediction errors ($R = 2.14, \text{TTR} = 5.4\text{ hours}$).
* **Live Error Correction in the Dynamic Hybrid (Model 3)**: The Dynamic Hybrid actively senses real-time checkpoint conditions using 1-step recursive error feedback ($e_{t-1} = y_{t-1} - \hat{y}_{t-1}$). In practical terms, this functions like an automated safety valve: when live passenger throughput at the checkpoint exceeds what delayed flight schedules predicted, the error correction immediately alerts the model that passengers are accumulating in the terminal. The model adjusts its demand forecast upward, preventing the empty checkpoint fallacy and maintaining low disruption error multipliers ($R_{\text{MASE}} = 1.05, \text{MASE}_{\text{shock}} = 0.694, \text{TTR} = 2.8\text{ hours}$).

---

## F.3 Dimension 3: Generalizability and Cross-Airport Transfer Performance

### Table F.3
*Evaluation Dimension 3: Generalizability and Cross-Airport Transfer Performance (Zero-Shot EWR $\to$ LGA)*

{{TABLE_F3}}

*Note.* Adapted from `results/manuscript_tables/table_5_3.csv`. Evaluates zero-shot spatial transfer from Newark Terminal C to LaGuardia Terminal C without local retraining.

### Transfer Penalty Mechanics
* **Model 1 Wins Decisive Spatial Generalizability**: Model 1 relies on physical schedule convolution and airport-invariant passenger show-up curves. Under zero-shot transfer from EWR to LGA, it experiences virtually zero performance degradation ($\text{RTR} = 1.04, \Delta\text{MASE} = +4.0\%$), easily meeting the academic target ($\Delta\text{MASE} \le 10.0\%$).
* **Model 3 Fails Spatial Generalizability**: Model 3 suffers a substantial transfer penalty ($\text{RTR} = 1.19, \Delta\text{MASE} = +21.5\%$), decisively failing the generalizability target. The decision tree stage overfits to the physical geometry, lane counts, and sensor calibration of the training airfield (EWR), creating distorted residual predictions when applied zero-shot to an unfamiliar airfield (LGA).

---

## F.4 Deep-Dive: The Values versus Volatility Empirical Paradigm Across Temporal Horizons ($H_2$)

A central theoretical contribution of this thesis is validating the **Values versus Volatility Paradigm ($H_2$)**: predicting checkpoint throughput volatility requires tracking the *volatilities* of airside operational attributes rather than static *values* (levels).

Evaluating across the 2025 out-of-time holdout suite ($N = 3,222$ test complex-days) across the three primary volatility targets proves:

### 1. Intraday Diurnal Absolute Volatility ($\sigma_{\text{TSA, hr}}$, pax/hr dispersion)
* **Values Only**: Achieves $R^2 = 0.6229$ ($\text{RMSE} = 271.6$). Because raw variance naturally scales with airport passenger volume, flight volume counts anchor the base magnitude of the facility.
* **Volatility Only**: Achieves $R^2 = 0.4980$ ($\text{RMSE} = 313.4$).
* **Combined Dual Representation**: Achieves $R^2 = 0.6178$ in non-linear decision trees ($\text{RMSE} = 273.5, \text{MAE} = 178.0$), improving to $R^2 = 0.7042$ ($\text{RMSE} = 240.5$) under unconstrained tree estimators, proving strong complementarity.

### 2. Intraday Scale-Free Relative Volatility ($CV_{\text{TSA, hr}} = \sigma / \mu$, ratio)
* **Values Only**: Drops to $R^2 = 0.0412$ (linear) and $R^2 = 0.1823$ (decision trees). Once scale is removed, raw volume features contain negligible predictive power for arrival burstiness.
* **Volatility Only**: Captures $R^2 = 0.1853$ in decision trees ($\text{RMSE} = 0.148$).
* **Combined Dual Representation**: Outperforms all architectures ($R^2 = 0.2208, \text{RMSE} = 0.1853, \text{MAE} = 0.1010$ in standard trees; $R^2 = 0.3124$ in full ensemble), proving that scale-free arrival burstiness reflects an interaction between carrier schedule volume and operational disruption.

### 3. Multi-Day Temporal Rolling Volatility ($\sigma_{\text{TSA, 7d}}$, pax/day)
* **Feature Values Completely Collapse**: Yielding negative test scores ($R^2 = -0.2688$ in linear regression; $R^2 = -0.0506$ in decision trees). Because static flight counts remain relatively constant across consecutive weeks, static volume levels are blind to temporal turbulence.
* **Feature Volatility Succeeds**: In sharp contrast, Feature Volatility metrics achieve $R^2 = +0.2313$ (linear) and $R^2 = +0.3105$ (decision trees), improving to $R^2 = +0.3166$ in the Combined Model, with RMSE dropping from 4,090.7 to 3,002.3 pax/day. This confirms Hypothesis $H_2$.

### Delay Volatility Transmission Mechanics
Cross-dataset econometric correlation demonstrates that **Flight Departure Delay Volatility ($CV_{\text{delay}}$)** is significantly coupled with checkpoint arrival volatility ($r = +0.4373, R^2 = 19.13\%, p = 0.0288$). Conversely, raw flight departure delay minutes show zero linear correlation ($r = -0.0620, p = 0.769$). Delays only disrupt checkpoint operations when they are erratic and disperse passenger arrival timing across banks.

### Master Consensus Factor Weights
Synthesizing variable importance across models confirms that schedule dispersion (`sched_rolling_7d_mean`, 23.73%; `sched_hourly_mean`, 6.91%) and operational volatility (`otp_cancellation_volatility_cv`, 8.79%; $CV_{\text{delay}}$, 4.32%) dominate predictive power, accounting for over 80% of consensus importance.

### Table F.4
*The Values versus Volatility Paradigm Across Multi-Day Temporal Horizons ($H_2$ Holdout Benchmark)*

| Feature Space Paradigm | Regressor Architecture | Out-of-Time Test Score ($R^2$) | Out-of-Time RMSE (pax/day) | MAE (pax/day) | Empirical Finding & Hypothesis $H_2$ Status |
| :--- | :--- | :---: | :---: | :---: | :--- |
| **Feature Values Only (Levels)** | OLS Linear Regression | **-0.2688** | 4,215.8 | 3,110.4 | Complete failure; static volume levels cannot detect multi-day network turbulence. |
| **Feature Values Only (Levels)** | Decision Tree Regressor | **-0.0506** | 4,090.7 | 2,985.2 | Fails out-of-time test; confirms static flight schedules are blind to delay cascades. |
| **Feature Volatility Only (Dispersion)** | OLS Linear Regression | **+0.2313** | 3,340.2 | 2,420.1 | Strong positive accuracy; delay and cancellation dispersion capture network shock waves. |
| **Feature Volatility Only (Dispersion)** | Decision Tree Regressor | **+0.3105** | 3,215.4 | 2,298.6 | **Confirms $H_2$**: Volatility metrics successfully model multi-day checkpoint turbulence. |
| **Combined Dual Paradigm** | Decision Tree Regressor | **+0.3166** | **3,002.3** | **2,114.7** | Decisive winner: combines facility baseline scale with operational dispersion features. |

*Note.* $N = 3,222$ test complex-days on the 2025 out-of-time holdout suite. Dependent target is multi-day rolling volatility ($\sigma_{\text{TSA, 7d}}$).

---"""
    doc.append(sec_f.replace("{{TABLE_F1}}", formatted_table_4_11).replace("{{TABLE_F2}}", formatted_table_5_2).replace("{{TABLE_F3}}", formatted_table_5_3))

    # Appendix G
    sec_g = r"""# Appendix G: Real-World Operational Decision Playbook and Dynamic Checkpoint Lane Staffing

> *Note on Thesis Cross-References*: This appendix translates the empirical modeling findings into an actionable operational decision playbook and dynamic lane dimensioning rules for airport terminal managers. It is referenced in **Chapter V (Discussion)**, Section *Master Synthesis and Operational Recommendations*, Section *The Regime-Switched Gated Inference Engine: The Airport Operator's Playbook*, Section *Connecting Queuing Principles to Dynamic Lane Staffing: The Staffing Safety Cushion*, and Section *Strategic Implications for Airport and Security Authorities*.

## G.1 Dual-Track Operational Decision Framework / Regime-Switched Gated Inference Engine

To operationalize these empirical findings, the Transportation Security Administration (TSA) and Airport Operations Centers (AOC) should deploy a **Regime-Switched Gated Inference Engine**—an automated decision playbook that monitors airport turbulence in real time and automatically selects the most suitable forecasting model:

### Gate 1: Routine Flow Track (Turbulence Shock Index $T_h < 0.75$)
* **Operating Regimes**: Calm seasonal periods (`1_OFF_PEAK`), midweek baseline days (Tuesday and Wednesday), and steady midday hours ($08:00\text{--}13:00$).
* **Assigned Canonical Architecture**: **The Supervised Machine Learning Model (Model 2)**.
* **Operational Justification**: Fast, automated execution delivering superior point accuracy ($\text{MASE} = 0.680\text{--}0.700$, $\text{RMSE} = 273.5\text{ pax/hr}$) with near-zero computing overhead and high portability across diverse terminal layouts ($\text{RTR} = 1.08, \Delta = +7.9\%$). Running a complex live-updating feedback loop 24/7 during calm periods imposes unnecessary IT costs, sensor maintenance overhead, and latency; Model 2 provides the optimal balance of speed and precision.

### Gate 2: Tactical Shock Track (Turbulence Shock Index $T_h \ge 0.75$)
* **Operating Regimes**: Summer severe thunderstorms (`3_PEAK`), peak holiday travel corridors, concentrated Monday morning flight waves, Sunday evening return cascades, and acute departure delay dispersion ($\sigma_{\text{Delay}} > 45\text{ min}$ or cancellations $\ge 5$).
* **Assigned Canonical Architecture**: **The Dynamic Two-Stage Hybrid (Model 3)**.
* **Operational Justification**: Activates live checkpoint queue feedback ($e_{t-1} = y_{t-1} - \hat{y}_{t-1}$), maintaining tight error bounds ($R_{\text{MASE}} = 1.05, \text{MASE}_{\text{shock}} = 0.694$) and rapid recovery ($\text{TTR} = 2.8\text{ hours}$) during acute flight delay cascades to prevent checkpoint staffing shortfalls and queue blowups.

### Table G.1
*Dual-Track Operational Model Selection Policy Matrix*

{{TABLE_G1}}

*Note.* Adapted from `results/manuscript_tables/dual_track_model_selection_policy.csv`. Operational decision matrix guiding TSA Federal Security Directors (FSD) and Airport Operations Centers in deploying predictive models based on real-time airspace congestion states.

---

## G.2 Connecting Queuing Principles to Dynamic Checkpoint Lane Staffing

A primary practical contribution of this thesis is bridging theoretical queuing theory with actionable checkpoint lane allocation:

### The Checkpoint Tipping Point (Kingman's Queuing Law)
In heavy-traffic queuing theory (Kingman, 1961, 1962), expected passenger waiting time ($W_q$) does not increase in a smooth, straight line. Rather, it follows a steep non-linear curve:

$$W_q \approx \left( \frac{\rho}{1-\rho} \right) \left( \frac{C_a^2 + C_s^2}{2} \right) \frac{1}{\mu}$$

where $\rho = \frac{\lambda}{c \cdot \mu}$ is checkpoint lane utilization, $C_a^2$ is passenger arrival volatility, $C_s^2$ is screening service volatility, and $\mu$ is screening lane service rate. When screening lanes operate near capacity ($\rho \ge 0.85\text{--}0.90$), the multiplier $\frac{\rho}{1-\rho}$ grows exponentially. Even a modest burst of arriving passengers ($C_a^2$) instantly tips the checkpoint into a runaway queue backlog.

### The Dynamic Staffing Safety Cushion
Under traditional deterministic staffing, security lanes are opened based solely on expected average volume ($\hat{\mu}_t$). During flight departure waves, arrival surges push utilization past $\rho = 0.90$, triggering queue spikes and passenger delays.

To solve this, airport checkpoint administrators can translate predicted throughput volatility ($\hat{\sigma}_{\text{TSA}, t}$) directly into risk-buffered lane configurations using conformal prediction principles:

$$c(t) = \left\lceil \frac{\hat{\mu}_t + z_q \cdot \hat{\sigma}_{\text{TSA}, t}}{\mu_{\text{lane}}} \right\rceil$$

where $\mu_{\text{lane}}$ is nominal screening lane capacity (~180 to 220 pax/lane/hr) and $z_q$ is the coverage quantile factor ($z_{0.85} = 1.036$ for an 85% service guarantee; $z_{0.95} = 1.645$). By adding a dynamic volatility buffer ($z_q \cdot \hat{\sigma}_{\text{TSA}, t}$) to lane scheduling, checkpoint administrators cap utilization at a safe threshold ($\rho_t \le 0.85$), effectively clamping the $\frac{\rho}{1-\rho}$ multiplier and preventing exponential wait-time explosions.

---"""
    doc.append(sec_g.replace("{{TABLE_G1}}", formatted_policy))

    # Appendix H
    sec_h = r"""# Appendix H: Research Limitations, Archival Infrastructure, and Repository Reproducibility

> *Note on Thesis Cross-References*: This appendix documents the methodological and operational limitations of the study, along with the archival directory hierarchy and digital artifact preservation structure. It is referenced in **Chapter I (Introduction)**, Section *Delimitations* and Section *Limitations and Assumptions*; in **Chapter III (Methodology)**, Section *Apparatus and Materials* and Section *Internal Validity Threats and Remediation Protocols*; and in **Chapter V (Discussion)**, Section *Strategic Implications for Airport and Security Authorities (Operational and Methodological Boundaries)*.

## H.1 Methodological and Operational Limitations

While the empirical findings provide robust guidance for passenger flow modeling, several operational and data constraints must be recognized:

1. **Staffing and Lane Configuration Opacity**: Due to the proprietary and security-sensitive nature of TSA checkpoint operations, confidential operational variables—such as exact Transportation Security Officer (TSO) shift allocations, active lane counts per 15-minute interval, and manual queue snake reconfigurations—are not publicly available. The methodology controls for this by aggregating lane-level counts into terminal complex throughput totals.
2. **Connecting Passenger Surveys**: The proportion of transferring passengers who remain airside is estimated using quarterly BTS DB1B coupon surveys. The framework assumes that connecting ratios remain stable across monthly operating horizons within given carrier-terminal complexes.
3. **Operational Exogeneity**: Exogenous severe weather disruptions (convective storm lines, winter blizzards) are captured through departure delay distributions and flight cancellation indicators reported in BTS Form 234. While these metrics capture the operational footprint of disruptions, localized landside airport ground access congestion (e.g., roadway traffic or transit delays) is not independently modeled.
4. **Checkpoint Screening Heterogeneity**: Checkpoint throughput records aggregate diverse screening modes, such as TSA PreCheck and standard screening lanes. Because PreCheck lanes achieve substantially higher processing rates (~250–300 pax/lane-hr) than standard lanes (~150–180 pax/lane-hr), raw lane counts introduce throughput rate variance. Constructing scale-free relative volatility metrics ($CV_{\text{TSA}}$) and standardized lane measures normalizes this facility-specific heterogeneity across airfields.

---

## H.2 Archival Data Storage Infrastructure and Repository Organization

To ensure full auditability, scientific reproducibility, and long-term data preservation, the master raw and conformed aviation datasets are archived in a standardized directory hierarchy replicated across secure persistent cloud storage (OneDrive) and local data warehouse paths.

### Table H.1
*OneDrive Archival Backup Directory Structure and Repository Manifest*

{{TABLE_H1}}

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
"""
    doc.append(sec_h.replace("{{TABLE_H1}}", formatted_backups))

    final_content = "\n\n".join(doc) + "\n"

    # Write to main appendix.md
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(final_content)
    print(f"[SUCCESS] Generated: {output_path} ({len(final_content)} characters, {len(final_content.splitlines())} lines)")

    # Write to manuscripts-only appendix.md (adjusting figure relative paths if needed)
    manuscripts_only_content = final_content.replace("../../figures/", "../../../figures/")
    with open(manuscripts_only_path, "w", encoding="utf-8") as f:
        f.write(manuscripts_only_content)
    print(f"[SUCCESS] Generated: {manuscripts_only_path}")

if __name__ == "__main__":
    main()
