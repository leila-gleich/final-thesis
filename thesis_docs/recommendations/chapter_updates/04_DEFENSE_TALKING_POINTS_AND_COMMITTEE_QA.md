# Thesis Defense Talking Points & Committee Q&A Guide

## 1. Overview & Defense Strategy

When defending the graduate thesis **"Evaluating Predictive Techniques to Model Stochastic Airport Passenger Flow"**, your committee will likely focus on methodological rigor, data integrity, and operational validity. 

The transition to **Coupled Volatility / Variation Clustering** strengthens your defense by providing an econometric justification for why static models fail and proving that your model evaluations are statistically leak-free.

---

## 2. Recommended 22-Slide Defense Presentation Structure

* **Slide 1**: Title, Author, Advisory Committee, Degree Program.
* **Slide 2**: The Research Problem: Terminal Queuing Fragility & TSA Staffing Misallocation.
* **Slide 3**: The Core Thesis Hypotheses (Routine Accuracy, Shock Resilience, Spatial Generalizability).
* **Slide 4**: Multi-Source Federal Data Foundation (67.2M Raw $\to$ 42.1M Post-ETL Cleaned Records across Top 25 Airfields).
* **Slide 5**: Methodological Milestone 1: The Hub Disconnect (Connecting Passenger Deflator via BTS DB1B).
* **Slide 6**: Methodological Milestone 2: Carrier Checkpoint Isolation & Econometric Exclusivity Proofs.
* **Slide 7**: Methodological Milestone 3: The 4-Tiered Purposive Filtering Funnel & 9-Airport Balanced Experimental Cohort.
* **Slide 8**: **Coupled Volatility Discovery**: Why Static Volumes Mask Congestion ($R^2 = 2.5\%$) vs. Volatility ($R^2 = 19.1\%$). *(Show Figure 1: Coupled Volatility Phase Space)*.
* **Slide 9**: **Annual Seasonal Regimes**: The 4 Macro Volatility Regimes (Off-Peak, Mid-Peak, Summer Convective Peak, Holidays). *(Show Table 4.3b)*.
* **Slide 10**: **Day-of-Week Operational Cycles**: Monday Outbound Business Surge vs. Sunday Return Delays. *(Show Figure 2 & Table 4.4a)*.
* **Slide 11**: **Diurnal Non-Consecutive Dual Peaks**: Morning Screening Surge vs. Evening Delay Cascades. *(Show Figure 3 Heatmap)*.
* **Slide 12**: **Statistical Sample Size & Training Sufficiency**: Auditing the 84-Cell Grid ($N_{\text{train}} \ge 50$ in 98.8% of cells). *(Show Figure 4)*.
* **Slide 13**: Empirical Passenger Show-Up Curves: Why Contemporaneous Schedules Fail ($R^2 = 0.198$) and Lead-2 ($t+2$) Succeeds ($R^2 = 0.498$).
* **Slide 14**: Master Model Benchmark Matrix: 2025 Holdout Evaluation ($M_0$ through $M_5$).
* **Slide 15**: Deep-Dive Dimension 1 (Robustness): Supervised ML & Hybrid Accuracy in Routine Flow ($\text{MASE} \approx 0.60$).
* **Slide 16**: Deep-Dive Dimension 2 (Resilience): The "Empty Checkpoint Fallacy" during Summer Storms & Hybrid State Recovery ($R_{\text{MASE}} = 1.28$).
* **Slide 17**: Deep-Dive Dimension 3 (Generalizability): Zero-Shot Cross-Airport Transferability without Layout Overfitting.
* **Slide 18**: Cross-Project Synthesis: Validating ML (Project 1), Queueing Theory (Project 2), and State-Space Tracking (Project 3).
* **Slide 19**: Practical Operational Implementation: The Regime-Switched Gated Inference Engine.
* **Slide 20**: Policy Recommendations for TSA and Airport Authorities.
* **Slide 21**: Major Contributions to Aviation Operations Research.
* **Slide 22**: Conclusion & Committee Q&A.

---

## 3. High-Impact Defense Talking Points

### Talking Point 1: Why Volatility Over Static Passenger Numbers
> *"In airport operations, airlines and the TSA staff to nominal schedules months in advance. When static flights and baseline passenger numbers are compared to delays, the correlation is negligible ($R^2 \approx 2.5\%$). Breakdowns occur when there is **volatility and variance mismatch**. Our analysis proves that the Coupled Volatility Index ($CV_{\text{TSA}} \times \sigma_{\text{Delay}}$) increases by over 41% during peak summer convective periods, driving delay standard deviations up to 68.4 minutes. Modeling volatility captures the true physical queuing friction."*

### Talking Point 2: The Physical Mechanism of Non-Consecutive Dual Peaks
> *"Our diurnal clustering conditioned on Day of Week revealed a non-consecutive dual-peak structure. In the early morning (05:00–08:00), TSA screening volatility peaks at over 11,380 passengers/hour, while flights depart with near-zero delays. Conversely, in the late afternoon and evening (14:00–22:00), passenger screening has moderated, but flight departure delay standard deviations expand beyond 63 minutes due to network-wide aircraft turnaround erosion. Passenger arrivals lead gate departures, whereas flight delays lag and accumulate into the evening."*

### Talking Point 3: Defending the 84-Cell Interaction Matrix against "Overfitting"
> *"A committee member might ask: 'Does segmenting the data into 84 cells (4 Seasons $\times$ 7 Days $\times$ 3 Diurnal blocks) cause small-sample estimator degradation?'*
> *Our response: 'No. We conducted a comprehensive degrees-of-freedom audit across the Candidate B training set (23,400 hourly observations) and the 2025 out-of-time holdout (8,760 observations). Exactly 83 of the 84 cells (98.8%) satisfy the $N_{\text{train}} \ge 50$ threshold, with a median sample depth of 215 observations per cell. Even in holdout testing, 83.3% of cells exceed 30 observations. This guarantees asymptotic statistical power and eliminates sparse leaf-node bias.'"*

---

## 4. Anticipated Committee Questions & Bullet-Proof Answers

### Q1: *"Why did you cluster weeks into annual seasons rather than clustering each calendar day individually?"*
* **Answer**: *"Clustering individual calendar days directly introduces two fatal flaws. First, isolated thunderstorm days cause seasonal labels to jump erratically day-to-day, destroying seasonal continuity. Second, because Sunday is universally a high-volume return day, clustering individual days caused virtually all Sundays to fall into the Peak cluster, leaving only a single Sunday in the entire three-year Off-Peak training set ($N = 4$ observations). By clustering the annual cycle at the ISO weekly level using coupled volatility profiles, we establish coherent macro-seasons while ensuring that every day of the week is well-represented, guaranteeing robust sample sizes across all 84 cells."*

### Q2: *"Why did pure machine learning ($M_3$) degrade so severely during Summer Storm disruptions ($R_{\text{MASE}} = 2.14$)?"*
* **Answer**: *"This is what we termed the 'Empty Checkpoint Fallacy'. Supervised machine learning models rely on scheduled flights shifted by empirical passenger show-up curves. During severe convective storms (where delay dispersion reaches 68.4 minutes and cancellations triple), evening flights are delayed past midnight or ground-stopped. The ML model observes that scheduled departures have vanished from the schedule and falsely predicts that the checkpoint will be empty. In reality, thousands of ticketed passengers are physically stranded inside the terminal concourses. The Two-Stage Hybrid model ($M_5$) avoids this failure mode because its Kalman innovation filter continuously incorporates prior-hour live queue observations ($t-1$), overriding stale flight schedules."*

### Q3: *"Why did you exclude Southwest Airlines (WN) from your carrier-exclusive checkpoint pairing?"*
* **Answer**: *"Southwest operates a fundamentally different passenger show-up distribution than legacy carriers. Because Southwest historically utilized open seating and boarding group positioning (A, B, C groups) along with free checked baggage, their passenger arrival profile is bimodal: passengers arrive either exceptionally early (135+ minutes prior to secure boarding position) or very late (65 minutes, baggage-free business travelers). Legacy carriers (American, Delta, United) exhibit consistent unimodal lognormal arrival distributions ($\tau \sim \text{Lognormal}, E[\tau] \approx 105\text{ min}$). Mixing Southwest into checkpoint pairing violates arrival distribution consistency."*

### Q4: *"Why was LGA chosen over JFK, and PHL chosen over SLC for your 9-airport experimental cohort?"*
* **Answer**: *"United Airlines permanently ceased flight operations at JFK in October 2022, violating our Meso continuity filter requiring concurrent mainline operations by American, Delta, and United. In contrast, LGA opened Delta's new Terminal C in June 2022, providing unconfounded screening lanes. Similarly, Salt Lake City (SLC) funnels all airlines through a single consolidated central security checkpoint, making carrier isolation mathematically impossible. Philadelphia (PHL) provides dedicated American Airlines checkpoints (Terminals B and C), establishing an East Coast fortress control counterpart to Delta's fortress at Detroit (DTW)."*
