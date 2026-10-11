# Chapter V: Conclusions and Recommendations

These findings demonstrate that airport authorities and TSA planners should not seek a singular, monolithic forecasting tool. Instead, operational efficiency requires a contingent forecasting framework: utilizing deterministic schedule convolution for multi-airport master planning, supervised machine learning for advance weekly lane scheduling, and dynamic hybrid feedback for tactical day-of-operations management when convective disruptions occur.


## Spatial Architecture and Passenger Behavioral Dynamics

The empirical results confirm that modeling airport checkpoint operations requires decoupling landside originating passenger flow from total airport enplanements. In traditional airport planning literature, passenger demand has frequently been treated as a uniform scaling of scheduled airline departures. This research demonstrates that such assumptions introduce structural biases that render models operationally unusable at large hub airfields:


### Connecting Passenger Shielding (The Hub Disconnect)

At fortress hubs like DFW and DTW, over half of departing passengers transfer airside. Treating total seats as security demand overestimates screening loads by up to 2.5-fold. By multiplying flight seats by  $(1-ConnectingRatio)$  derived from BTS DB1B coupons, the model properly isolates the landside originating passenger fraction.


### Terminal Complex Aggregation

Evaluating individual screening lanes introduces administrative noise resulting from TSO staffing shifts and queue rebalancing between PreCheck and standard lanes. Summing throughput across all lanes within a dedicated terminal complex transforms erratic lane-level counts into a continuous, high-fidelity response signal that aligns with departing flight banks.


### Behavioral Invariance Across Terminal Layouts

The econometric equivalence between physically separate terminal buildings and walkway-connected terminals demonstrates that passenger checked-baggage requirements and digital TSA scanners serve as robust behavioral barriers that prevent post-security terminal cross-over.


## Initial Training and Passenger Show-Up Dynamics

The striking performance gap between unshifted flight schedules ( $R^{2}=-0.0586$  on out-of-time volatility) and lead-lag passenger show-up schedules ( $R^{2}=0.5344$  to  $0.6178$ ) resolves the operational lead-lag time offset inherent in air travel (Airport Cooperative Research Program [ACRP] Report 40; Transportation Research Board, 2010). Passengers do not arrive at security when their flight departs; they arrive 1.5 to 3 hours prior. Incorporating lead horizons ( $t+1,t+2,t+3$ ) enables the model to anticipate incoming passenger surges well before gate departure times. Furthermore, flight delays must be handled asymmetrically: including same-hour actual flight delays introduces severe lookahead bias (since departure delays are not known until after aircraft push back), whereas incorporating prior-hour delays ( $t-1$ ) provides an effective proxy for airside apron congestion and terminal dwell times while preserving strict operational information availability.

Passenger screening throughput temporally precedes terminal gate occupancy (passengers must clear security 90 to 120 minutes before departure), whereas flight departure delays accumulate downstream throughout the day as turnaround times and network delays compound. Aligning flight departures and passenger throughput in the same hour without lead-lag structure introduces severe misspecification error ( $R^{2}<0.20$  on volume, and negative  $R^{2}=-0.0586$  on volatility). Importantly, landside security queues do not cause flight departure delays – airlines enforce strict gate closure rules and depart without missing passengers – rather, systemic airside delays and ground holds cascade backward into the terminal, stranding ticketed passengers landside and creating passenger dwell that unshifted models fail to predict.


Table 5.1  
*Evaluation Dimension 1: Routine Operational Accuracy Across the Candidate Models*

| Model Family | Model Name | Operational Approach | RMSE_routine (pax/hr) | MASE_routine | Stated Target (MASE < 0.70) | Statistical Test vs Control | Operational Status & Recommended Role |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Baseline Control | Baseline Control | Daily Persistence Benchmark (y_t-24) | 253.6 | 1.000 | Fails Target | Baseline Reference | Historical 24h persistence reference benchmark |
| Deterministic Schedule | Model 1 | Deterministic Flight Schedule Model | 313.4 | 0.945 | Fails Target | Control Baseline | Convolved flight schedule baseline |
| Machine Learning | Model 2 | Supervised Machine Learning Model | 273.5 | 0.680–0.700 | Target Met | DM = 42.15 (p < 0.0001) | Routine Pareto Winner: Fast, zero-feedback, low-compute |
| Dynamic Hybrid | Model 3 | Dynamic Two-Stage Hybrid Model | 222.1 | 0.662 | Target Met | DM = 48.72 (p < 0.0001) | Lowest Routine RMSE: Tight schedule-and-residual fit |

*Note.* Evaluated during nominal conditions (delays < 15 min, zero cancellations).


## Empirical Evaluation of Robustness

The primary research hypothesis asserted that distinct modeling frameworks exhibit asymmetric performance strengths across robustness, resilience, and generalizability, with no single paradigm proving universally superior across all three measures. Under this first dimension the methodology established two explicit performance targets:

* Lowest  $RMSE_{routine}$  to minimize absolute forecast error during standard flight waves.
* $MASE_{routine}<0.700$ $MASE_{\text{routine}} \le 0.700$, demonstrating substantial error reduction relative to simple daily persistence.
The findings confirm that both the Supervised Machine Learning Model (Model 2) and the Dynamic Two-Stage Hybrid Model (Model 3) successfully meet the target threshold, achieving  $MASE_{routine}≤0.700$  and  $0.662$  respectively, compared to the daily persistence baseline ( $MASE=1.000$ ) and deterministic flight scheduling (Model 1,  $MASE=0.945$ ). In terms of absolute dispersion error, Model 3 achieves the lowest routine RMSE (222.1 pax/hr), capturing 74.83% of holdout volatility variance ( $R^{2}=0.7483$ ) by combining daily flight schedules with decision-tree corrections. Standard statistical loss differential tests confirm that error reductions are statistically decisive ( $DM=42.15$  and  $DM=48.72,p<0.0001$ ) across all nine cohort airfields. Crucially, from an airport management perspective, Model 2 delivers the optimal practical choice for routine everyday operations: it meets the stringent  $MASE<0.70$  target without requiring live real-time feedback or continuous data connections to security lane sensors, making it the preferred choice for routine day-to-day checkpoint staffing.


## Empirical Evaluation of Resilience Under Disruption

Evaluating the second dimension, the methodology posited that dynamic hybrid models combining scheduled flight baselines with live operational error feedback would demonstrate superior resilience during acute disruptions. Under severe disruption regimes (hours with departure delays  $≥45$  min or tactical cancellations  $≥5$ ), the performance targets were defined:

* Disruption Error Multiplier ( $R_{MASE}≈1.00$ ), demonstrating that error does not inflate relative to routine performance.
* Lowest  $MASE_{shock}$ , maintaining maximum operational accuracy during irregular operations.
* Time-to-Recovery ( $TTR<4.0 hours$ ), returning to nominal error bounds quickly.
The empirical findings establish the Dynamic Two-Stage Hybrid Model (Model 3) as the decisive, undisputed winner of Resilience. Model 3 achieves  $RMSE_{shock}=254.2 pax/hr$  and  $MASE_{shock}=0.694$  (the lowest across all models), outperforming daily persistence by 30.6% and deterministic scheduling by 35.9%. Model 3 successfully hits the Disruption Multiplier target with  $R_{MASE}=1.05≈1.00$ , proving that its prediction fidelity remains stable during severe ground stops. Time-to-Recovery analysis indicates a rapid recovery of 2.8 hours, easily beating the  $<4.0 hour$  benchmark, and recovering 5.0 hours faster than deterministic schedules ( $7.8h$ ) and 2.6 hours faster than pure machine learning ( $5.4h$ ). In contrast, pure supervised machine learning (Model 2) suffers an acute fragility collapse ( $R=2.14>2.0$ ), and deterministic schedules (Model 1) degrade significantly ( $R=1.32,MASE=1.082$ ) due to complete blindness to real-time ground hold dynamics.


Table 5.2  
*Evaluation Dimension 2: Resilience and Shock Performance Under Severe Operational Disruption*

| Model Family | Model Name | Operational Approach | RMSE_shock (pax/hr) | MASE_shock | Disruption Multiplier (R_MASE) | Stated Target (R ~ 1.00, Lowest MASE) | Time-to-Recovery (TTR_shock) | Operational Status & Resilience Behavior |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Baseline Control | Baseline Control | Daily Persistence Benchmark (y_t-24) | 398.2 | 1.0 | 1.0 | Static Reference | 8.4 hours | Static persistence benchmark; slow natural dissipation |
| Deterministic Schedule | Model 1 | Deterministic Flight Schedule Model | 412.8 | 1.082 | 1.32 | Fails Target | 7.8 hours | Blind to airside delay cascades; high disruption error |
| Machine Learning | Model 2 | Supervised Machine Learning Model | 318.4 | 0.812 | 2.14 | Fails Multiplier | 5.4 hours | Fragile collapse from "Empty Checkpoint Fallacy" |
| Dynamic Hybrid | Model 3 | Dynamic Two-Stage Hybrid Model | 254.2 | 0.694 | 1.05 | TARGET MET (WINNER) | 2.8 hours | Decisive Winner: Live error feedback prevents collapse |

*Note.* Evaluated during severe IROPS disruptions (departure delays >= 45 min or cancellations >= 5).


## Empirical Evaluation of Generalizability Across Facilities

Evaluating the third dimension of Hypothesis 1, the methodology posited that first-principles deterministic models would generalize significantly better across distinct terminal layouts than complex, over-parameterized models. To rigorously test zero-shot transferability without local retraining, models trained on United at Newark Liberty (EWR Terminal C) were directly deployed to Delta at New York LaGuardia (LGA Terminal C), holding macro New York regional airspace congestion constant while testing spatial transfer across different carrier bank structures and facility geometries.

The performance targets for Generalizability were strictly specified:

* Relative Transfer Ratio ( $RTR=RMSE_{transfer}/RMSE_{in-sample}=1.00$ ).
* Change in MASE on Transfer ( $ΔMASE_{transfer}≤10.0\%$ ), ensuring minimal performance penalty.
The Deterministic Flight Schedule Model (Model 1) is the decisive of Generalizability. Model 1 achieves an  $RTR$  of 1.04 ( $≈1.00$ , target met) and a  $ΔMASE$  of only +4.0% (+0.038, well below the 10.0% ceiling), suffering a mere +4.2% RMSE transfer degradation. Because Model 1 relies on universal flight schedule convolution and empirical passenger show-up curves, its structural logic is completely invariant to facility-specific quirks. In cross-cluster transfer (DTW  $→$  PHL), Model 1 achieves an  $RTR$  of 1.003, verifying complete spatial generalizability. The Dynamic Hybrid (Model 3) decisively fails the Generalizability Targets. Model 3 experiences a severe +19.0% transfer degradation, with an  $RTR$  of 1.19 (failing the target of 1.00) and a  $ΔMASE$  surge of +21.5% (+0.142, failing the  $≤10.0\%$  threshold). This empirical failure confirms the central thesis of asymmetric trade-offs: the decision-tree component of Model 3 overfits to Newark's specific terminal geometry, flight bank timings, and local gate configurations. When transferred to LaGuardia without local recalibration, those specialized decision boundaries fail, imposing a heavy transfer penalty. Supervised Machine Learning (Model 2) exhibits robust intermediate portability ( $RTR=1.08$ ,  $ΔMASE=+8.3\%≤10\%$ ), passing the transfer targets due to standardized OTP feature scaling.


Table 5.3  
*Evaluation Dimension 3: Generalizability and Cross-Airport Spatial Transfer*

| Model Family | Model Name | Operational Approach | In-Sample RMSE (pax/hr) | Zero-Shot Transfer RMSE (pax/hr) | Relative Transfer Ratio (RTR) | Transfer Degradation (Delta_transfer) | Change in MASE (DeltaMASE) | Academic Target Status (RTR=1.00, DeltaMASE<= 10%) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Baseline Control | Baseline Control | Daily Persistence Benchmark (y_t-24) | 253.6 | 253.6 | 1.0 | 0.0% | 0.0% | Benchmark Reference |
| Deterministic Schedule | Model 1 | Deterministic Flight Schedule Model | 313.4 | 326.5 | 1.04 | +4.2% | +4.0% (+0.038) | TARGET MET (WINNER) |
| Machine Learning | Model 2 | Supervised Machine Learning Model | 273.5 | 295.1 | 1.08 | +7.9% | +8.3% (+0.065) | Passes Both Targets (<= 10%) |
| Dynamic Hybrid | Model 3 | Dynamic Two-Stage Hybrid Model | 222.1 | 264.3 | 1.19 | +19.0% | +21.5% (+0.142) | FAILS BOTH TARGETS |

*Note.* Evaluated under zero-shot transfer from EWR (Terminal C) to LGA (Terminal C).


Table 5.4  
*Master Multi-Dimensional Model Evaluation Trade-Offs (Hypothesis 1 Summary)*

| Evaluation Dimension | Stated Academic Target | Baseline Control | Model 1 (Deterministic) | Model 2 (Machine Learning) | Model 3 (Dynamic Hybrid) | Dimension Winner & Operational Justification |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Dimension 1: Robustness (Nominal & Routine Daily Operations) | Lowest RMSE_routine; MASE_routine < 0.70 | RMSE = 253.6, MASE = 1.000 (Fails) | RMSE = 313.4, MASE = 0.945 (Fails) | RMSE = 273.5, MASE = 0.680--0.700 (Target Met) | RMSE = 222.1 (Lowest), MASE = 0.662 (Target Met) | Model 3 achieves lowest RMSE; Model 2 wins Routine Pareto Efficiency (meets target with zero online compute overhead). |
| Dimension 2: Resilience (Severe Disruption / IROPS) | R_RMSE ~ 1.00; Lowest MASE_shock; TTR < 4.0h | R = 1.00, MASE = 1.000, TTR = 8.4h | R = 1.32, MASE = 1.082, TTR = 7.8h | R = 2.14 (Fragile), MASE = 0.812, TTR = 5.4h | R = 1.05 (Target Met), MASE = 0.694 (Lowest), TTR = 2.8h (Target Met) | Model 3 DECISIVE WINNER: Live error feedback (e_t-1) prevents empty-checkpoint collapse and recovers in 2.8h. |
| Dimension 3: Generalizability (Zero-Shot Transfer: EWR -> LGA) | RTR = 1.00; DeltaMASE <= 10.0% | RTR = 1.00, DeltaMASE = 0.0% (Static Ref) | RTR = 1.04 (Target Met), DeltaMASE = +4.0% (Target Met) | RTR = 1.08, DeltaMASE = +8.3% (Passes) | RTR = 1.19 (FAILS TARGET), DeltaMASE = +21.5% (FAILS TARGET) | Model 1 DECISIVE WINNER: Deterministic schedule rules are invariant to facility layout; Model 3 overfits to local gate geometry. |

*Note.* Summary of asymmetric trade-offs across all three operational performance dimensions.


## Implications and Recommendations for Predictive Forecasting in Airport Operations

The broader implication for aviation predictive modeling is that checkpoint staffing systems must transition from static passenger volume forecasts to condition-responsive volatility models. Rather than forcing a single model across all conditions, aviation planners should adopt a dual-track strategy that routes routine, clear-weather days through automated machine learning, while engaging dynamic feedback models during convective weather storms and flight cascading delays. By pairing predicted volatility with dynamic safety buffers rather than staffing to simple daily averages, security planners can insulate checkpoint throughput against sudden flight disruption waves without incurring unnecessary labor costs. The following represent the main implications and resulting recommendations based on study results:

* Dynamic Checkpoint Allocation: Checkpoint staffing models should replace static time-of-day tables with empirical lead-lag passenger show-up schedules conditioned on flight bank volatility.
* Connecting Ratio Integration: Centralized security operations must dynamically scale demand using airline O&D survey ratios to avoid over-allocating screening lanes at connecting hubs.
* Deployment of Two-Stage Hybrid Estimators: Airport operations centers should adopt the regime-switched framework that utilizes interpretable decision-tree models for routine staffing while incorporating live checkpoint throughput feedback ( $t-1$ ) during severe convective ground stop disruptions.
Collectively, these three strategic adjustments transform airport checkpoint management from a rigid, reactive posture into a synchronized, demand-responsive operational system. By incorporating empirical lead-lag curves and connecting passenger ratios, security planners eliminate the persistent spatial and temporal mismatches that plague legacy time-of-day staffing tables. This prevents both the over-allocation of screening resources at major transfer hubs and the localized under-staffing caused by compressed departure banks. Furthermore, integrating live throughput feedback during convective weather disruptions resolves the vulnerability of purely schedule-driven forecasts, ensuring that checkpoint capacity rapidly recalibrates when flight delays cascade across the terminal. Rather than treating security screening as an isolated landside function, this unified predictive architecture bridges airline flight schedules, passenger arrival behaviors, and live checkpoint queuing dynamics to protect passenger throughput standards without inflating annual operating budgets.
