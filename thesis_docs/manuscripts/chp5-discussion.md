# Chapter V

# Discussion

<style>
th {
  font-weight: normal;
}
</style>

## Spatial Architecture and Passenger Behavioral Dynamics
The empirical results confirm that modeling airport checkpoint operations requires decoupling landside originating passenger flow from total airport enplanements. In traditional airport planning literature, passenger demand has frequently been treated as a uniform scaling of scheduled airline departures. This research demonstrates that such assumptions introduce structural biases that render models operationally unusable at large hub airfields:

1. **Connecting Passenger Shielding (The Hub Disconnect)**: At fortress hubs like DFW and DTW, over half of departing passengers transfer airside. Treating total seats as security demand overestimates screening loads by up to 2.5-fold. By multiplying flight seats by $(1 - \text{ConnectingRatio})$ derived from BTS DB1B coupons, the model properly isolates the landside originating passenger fraction.
2. **Terminal Complex Aggregation**: Evaluating individual screening lanes introduces administrative noise resulting from TSO staffing shifts and queue rebalancing between PreCheck and standard lanes. Summing throughput across all lanes within a dedicated terminal complex transforms erratic lane-level counts into a continuous, high-fidelity response signal that aligns with departing flight banks.
3. **Behavioral Invariance Across Terminal Layouts**: The econometric equivalence between physically separate terminal buildings and walkway-connected terminals demonstrates that passenger checked-baggage requirements and digital TSA Credential Authentication Technology (CAT) scanners serve as robust behavioral barriers that prevent post-security terminal cross-over.
4. **Heavy-Traffic Queuing Physics (The Second-Order Driver)**: Traditional models focus exclusively on mean passenger volume $\lambda$. However, from Kingman's heavy-traffic approximation and the Allen-Cunneen formula:
   $$W_q \approx \left(\frac{\rho}{1-\rho}\right) \left(\frac{C_a^2 + C_s^2}{2}\right) \frac{1}{\mu}$$
   where $\rho = \lambda / (c \mu)$ represents traffic intensity, $C_a = \sigma_a / \mu_a$ is the coefficient of variation of passenger arrivals, and $C_s$ is the coefficient of variation of screening service time. As traffic intensity approaches saturation ($\rho \to 1.0$) during morning and evening departure banks, queue delay $W_q$ scales non-linearly with the square of arrival volatility ($C_a^2$). Consequently, predicting the volatility of TSA throughput ($\sigma_{\text{TSA}}$ and $CV_{\text{TSA}}$) is fundamentally more consequential for checkpoint stability than forecasting average volume alone.

## Initial Training and Passenger Show-Up Dynamics
The striking performance gap between unshifted flight schedules ($R^2 = -0.0586$ on out-of-time volatility) and lead-lag passenger show-up schedules ($R^2 = 0.5344$ to $0.6178$) resolves the operational lead-lag time offset inherent in air travel (Airport Cooperative Research Program [ACRP] Report 40; Transportation Research Board, 2010):
* Passengers do not arrive at security when their flight departs; they arrive 1.5 to 3 hours prior (standard ACRP Report 40 passenger show-up distribution; Transportation Research Board, 2010).
* Incorporating lead horizons ($t+1, t+2, t+3$) enables the model to anticipate incoming passenger surges well before gate departure times.
* Furthermore, flight delays must be handled asymmetrically: including same-hour actual flight delays introduces severe lookahead bias (since departure delays are not known until after aircraft push back), whereas incorporating prior-hour delays ($t-1$) provides an effective proxy for airside apron congestion and terminal dwell times while preserving strict operational information availability.

### The Lead-Lag Asynchrony Mechanism
Traditional queuing models in airport terminal planning often assume that passenger arrival intensity $\lambda(t)$ is directly proportional to departing flights in the same time window $t$. The empirical results completely dismantle this unshifted schedule assumption. Across the Top 25 network, the operational cycle is governed by an asynchronous dual-peak structure:

* **Morning Peak (05:00–08:00)**:
  * *Checkpoint Volume*: Peak passenger screening throughput.
  * *Screening Volatility*: Extreme surge volatility ($\sigma_{\text{TSA}} > 11,380$ pax/hr network-wide; complex-level $\sigma_{\text{TSA, hr}} \sim 540\text{--}880$ pax/hr).
  * *Flight Departure Delays*: Low average departure delays (<5 minutes).
  * *Schedule Buffer*: Fresh, unexhausted aircraft turnaround buffers.
* **Evening Peak (14:00–22:00)**:
  * *Checkpoint Volume*: Moderate and tapering screening volumes.
  * *Screening Volatility*: Low to steady arrival volatility.
  * *Flight Departure Delays*: Peak network-wide departure delay dispersion ($\sigma_{\text{Delay}} > 63$ minutes).
  * *Schedule Buffer*: Turnaround buffers fully eroded across the National Airspace System.

* **Pre-Departure Passenger Surge Window (Morning)**: Passengers arrive at screening checkpoints 90 to 120 minutes prior to scheduled departure (conforming to ACRP Report 40 distributions; Transportation Research Board, 2010). Checkpoint arrival volatility peaks early in the day when early-morning outbound banks depart with high schedule reliability.
* **Operational Lag Phase (Evening)**: As the day progresses, delay propagation across the National Airspace System (NAS) compounds. Aircraft turnaround buffers are exhausted by late afternoon, causing departure delay dispersion ($\sigma_{\text{Delay}}$) to peak between 14:00 and 22:00.
* **Synthesis**: Passenger screening throughput temporally **precedes** terminal gate occupancy (passengers must clear security 90 to 120 minutes before departure), whereas flight departure delays accumulate downstream throughout the day as turn times and network delays compound. Aligning flight departures and passenger throughput in the same hour without lead-lag structure introduces severe misspecification error ($R^2 < 0.20$ on volume, and negative $R^2 = -0.0586$ on volatility). Importantly, landside security queues do not cause flight departure delays—airlines enforce strict gate closure rules and depart without missing passengers—rather, systemic airside delays and ground holds cascade backward into the terminal, stranding ticketed passengers landside and creating passenger dwell that unshifted models fail to predict.

## Evaluation Dimension 1: Robustness

Table 5.1  
*Evaluation Dimension 1: Routine Operational Accuracy Across the Four Canonical Models*

| Model Family | Model ID & Specification | $\text{RMSE}_{\text{routine}}$ (pax/hr) | $\text{MASE}_{\text{routine}}$ | Stated Target ($\text{MASE} < 0.70$) | Diebold-Mariano Test vs Control | Academic Status & Operational Role |
| :--- | :--- | :---: | :---: | :---: | :---: | :--- |
| **Baseline Control** | $M_0$: Diurnal Volatility Naive ($y_{t-24}$) | 253.6 | 1.000 | Fails Target | Baseline Reference | Historical 24h persistence control benchmark |
| **Deterministic Baseline** | $M_1^*$: Deterministic Schedule Bank Volatility | 313.4 | 0.945 | Fails Target | Control Baseline | First-principles convolved schedule baseline |
| **Probabilistic / ML** | $M_3$: Supervised Volatility GBR (Combined Values + Vol) | 273.5 | 0.680–0.700 | **Target Met** | $DM = 42.15$ ($p < 0.0001$) | **Routine Pareto Winner**: Fast, zero-feedback, low-compute |
| **Dynamic Hybrid** | $M_5$: Sequential SARIMA-Tree Volatility Hybrid | **222.1** | **0.662** | **Target Met** | $DM = 48.72$ ($p < 0.0001$) | **Lowest Routine RMSE**: In-sample cyclical-tree fit |

*Note*. Intermediate model variations developed during exploratory research—specifically unshifted schedule models ($M_1$), lead-flight-only specifications ($M_2$), and load-factor scaled formulations ($M_4$)—were pruned after the 4-tier filtering pipeline to isolate the four canonical model families representing each fundamental modeling paradigm.

### Empirical Evaluation of Robustness
The primary research hypothesis (**Hypothesis 1**) asserted that *distinct modeling frameworks exhibit asymmetric performance strengths across robustness, resilience, and generalizability, with no single paradigm proving universally superior across all three measures*. Under this first dimension—routine operating conditions (departure delays $< 15$ min, 0 cancellations)—the methodology established two explicit performance targets:
1. **Lowest $\text{RMSE}_{\text{routine}}$** to minimize absolute variance during standard operating banks.
2. **$\text{MASE}_{\text{routine}} < 0.700$**, demonstrating substantial error reduction relative to naive diurnal persistence.

* The findings confirm that both the Supervised Gradient Boosted Regressor ($M_3$) and the Sequential SARIMA-Tree Volatility Hybrid ($M_5$) successfully meet the target threshold, achieving $\text{MASE}_{\text{routine}} \le 0.700$ and $0.662$ respectively, compared to $M_0$ persistence ($\text{MASE} = 1.000$) and deterministic scheduling ($M_1^*$, $\text{MASE} = 0.945$).
* In terms of absolute dispersion, $M_5$ achieves the lowest routine RMSE (**222.1 pax/hr**), capturing 74.83% of holdout volatility variance ($R^2 = 0.7483$) by combining linear SARIMA diurnal cycles with gradient boosted tree residual corrections.
* Non-parametric Wilcoxon signed-rank tests and Diebold-Mariano tests confirm that error reductions are statistically significant ($DM = 42.15$ and $DM = 48.72, p < 0.0001$) across all nine cohort airfields.
* Crucially, from an operational perspective, **$M_3$ delivers the optimal Pareto tradeoff for routine conditions**: it meets the stringent $\text{MASE} < 0.70$ target without requiring live recursive error feedback or heavy compute infrastructure, making it the preferred choice for routine day-to-day checkpoint staffing.

### The Values versus Volatility Paradigm in Routine Operations
Evaluating the Values versus Volatility Paradigm under routine operations provides foundational insights into how checkpoint volatility originates:
1. **Absolute Intraday Dispersion ($\sigma_{\text{TSA, hr}}$)**:
   Predicting diurnal throughput standard deviation benefits from both feature types: Feature Values achieve $R^2 = 0.6229$ ($\text{RMSE} = 271.6$), while Feature Volatility achieves $R^2 = 0.4980$ ($\text{RMSE} = 313.4$). Because absolute variance scales with baseline facility size (Tweedie dispersion property $\text{Var}(Y) \propto \mu^p$), flight volume counts anchor the base magnitude of the facility. Combining values and volatility in the supervised GBR ($M_3$) yields $R^2 = 0.6178$ ($\text{RMSE} = 273.5, \text{MAE} = 178.0$).
2. **Scale-Free Arrival Burstiness ($CV_{\text{TSA, hr}} = \sigma / \mu$)**:
   When normalizing for facility size, Feature Values alone drop to $R^2 = 0.1823$. Feature Volatility models capture $R^2 = 0.1853$. Crucially, the **Combined Dual Model achieves the highest performance ($R^2 = 0.2208$, $\text{RMSE} = 0.1853$)**, proving that relative arrival burstiness reflects the interplay between scheduled bank volume and operational disruption.

### Robustness Across the Interaction Grid and Prevention of Delay Distortion
The coupled volatility analysis substantiates why routine accuracy holds consistently across the entire national airspace:
1. **Preventing Extreme Storm Outliers from Distorting Normal-Day Decision Rules**:
   When a predictive model is trained across all weather regimes simultaneously without stratification, loss functions are dominated by extreme summer storm delay tails ($\sigma_{\text{Delay}} = 68.43\text{ min}$). Under pooled training, decision trees optimize their branching splits to accommodate these rare, chaotic delay spikes, degrading accuracy during clear, on-time operations. By partitioning operations into the 84-cell interaction grid ($\mathcal{S} \times \mathcal{D} \times \mathcal{H}$), training samples are conditioned on homogeneous operational variance states. Decision trees branch on direct operational queuing drivers (route load factors, aircraft seat gauge, and empirical passenger show-up curves) rather than convective storm noise.
2. **Empirical Verification of Degrees of Freedom**:
   The sample size audit confirms that **83 of 84 cells (98.8%)** meet the $N_{\text{train}} \ge 50$ threshold, with a median training depth of **215 observations per cell**. This refutes any critique that fine-grained temporal stratification creates sparse, over-specialized decision nodes.

## Evaluation Dimension 2: Resilience

Table 5.2  
*Evaluation Dimension 2: Resilience and Shock Performance Under Severe Operational Disruption*

| Model Family | Model ID & Specification | $\text{RMSE}_{\text{shock}}$ (pax/hr) | $\text{MASE}_{\text{shock}}$ | Resilience Multiplier ($R_{\text{RMSE}} / R_{\text{MASE}}$) | Stated Target ($R \approx 1.00$, Lowest MASE) | Time-to-Recovery ($\text{TTR}_{\text{shock}}$) | Academic Status & Resilience Behavior |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **Baseline Control** | $M_0$: Diurnal Volatility Naive ($y_{t-24}$) | 398.2 | 1.000 | 1.00 | Static Reference | 8.4 hours | Static persistence benchmark; slow natural dissipation |
| **Deterministic Baseline** | $M_1^*$: Deterministic Schedule Bank Volatility | 412.8 | 1.082 | 1.32 | Fails Target | 7.8 hours | Blind to airside delay cascades; high shock error |
| **Probabilistic / ML** | $M_3$: Supervised Volatility GBR (Combined) | 318.4 | 0.812 | 2.14 | Fails Multiplier | 5.4 hours | Fragile collapse from "Empty Checkpoint Fallacy" |
| **Dynamic Hybrid** | $M_5$: Sequential SARIMA-Tree Volatility Hybrid | **254.2** | **0.694** | **1.05** | **TARGET MET (WINNER)** | **2.8 hours** | **Decisive Winner**: Closed-loop feedback prevents collapse |

### Empirical Evaluation of Resilience Under Disruption
Evaluating the second dimension of **Hypothesis 1**, the methodology posited that **dynamic cyber-physical hybrid models combining structural queuing dynamics with recursive operational telemetry would demonstrate superior resilience during acute disruptions**. Under severe disruption regimes (departure delays $\ge 45$ min or tactical cancellations $\ge 5$), the performance targets were strictly defined:
1. **Resilience Recovery Multiplier ($R_{\text{RMSE}} \approx 1.00$ / $R_{\text{MASE}} \approx 1.00$)**, demonstrating that shock error does not inflate relative to routine performance.
2. **Lowest $\text{MASE}_{\text{shock}}$**, maintaining maximum operational accuracy during irregular operations.
3. **Time-to-Recovery ($\text{TTR} < 4.0\text{ hours}$)**, returning to nominal $\pm 2\sigma$ error bounds quickly.

* The empirical findings establish the Sequential SARIMA-Tree Volatility Hybrid ($M_5$) as the **decisive, undisputed winner of Resilience**:
  * $M_5$ achieves $\text{RMSE}_{\text{shock}} = 254.2\text{ pax/hr}$ and $\text{MASE}_{\text{shock}} = 0.694$ (the lowest across all models), outperforming naive persistence by 30.6% and deterministic scheduling by 35.9%.
  * $M_5$ successfully hits the Resilience Multiplier target with $R_{\text{MASE}} = 1.05 \approx 1.00$, proving that its prediction fidelity remains virtually unperturbed during severe ground stops.
  * Kaplan-Meier survival analysis indicates a Time-to-Recovery of **2.8 hours**, easily beating the $< 4.0\text{ hour}$ benchmark, and recovering 5.0 hours faster than deterministic models ($7.8\text{h}$) and 2.6 hours faster than pure ML ($5.4\text{h}$).
* In stark contrast, pure supervised machine learning ($M_3$) suffers an acute fragility collapse ($R = 2.14 > 2.0$), and deterministic baselines ($M_1^*$) degrade significantly ($R = 1.32, \text{MASE} = 1.082$) due to complete blindness to real-time ground hold dynamics.

### Resilience Mechanics and the Empty Checkpoint Fallacy
The coupled volatility findings explain the exact operational bottleneck mechanism during convective disruptions:
1. **The "Empty Checkpoint Fallacy" in Pure Machine Learning**:
   During the **Summer Convective Peak (*3_PEAK*)**, departure delay dispersion expands to $\sigma_{\text{Delay}} = 68.43\text{ min}$ and cancellations surge to $3.16\%$. A pure machine learning model relying on flight schedules shifted by static show-up curves assumes that because flights scheduled for 18:00 have been delayed to 22:00 or ground-stopped, security checkpoints will experience an immediate demand collapse at 16:00. In reality, passengers arrived at the airport based on their original ticketed itineraries. Thousands of stranded travelers crowd security lines, re-screen after gate changes, or remain landside. Pure ML predicts an empty checkpoint, resulting in massive under-prediction errors ($R = 2.14$).
2. **State-Space Innovation Compensation ($M_5$)**:
   The Dynamic Hybrid dynamically tracks real-time terminal queue states using 1-step recursive error innovation feedback ($e_{t-1} = y_{t-1} - \hat{y}_{t-1}$):
   $$e_t = y_t - C \hat{x}_{t|t-1}$$
   In practical operational terms, this functions like a real-time feedback loop: when live passenger throughput ($y_t$) at the checkpoint exceeds the expectation from delayed flight schedules, the error correction immediately alerts the model that passengers are accumulating in the terminal. The model adjusts its demand forecast upward, preventing the empty checkpoint fallacy and maintaining low disruption error multipliers ($R_{\text{MASE}} = 1.05$).

## Evaluation Dimension 3: Generalizability

Table 5.3  
*Evaluation Dimension 3: Generalizability and Cross-Airport Transfer Performance*

| Model Family | Model ID & Architecture | In-Sample RMSE (pax/hr) | Zero-Shot Transfer RMSE (pax/hr) | Relative Transfer Ratio ($\text{RTR}$) | Transfer Degradation ($\Delta_{\text{transfer}}$) | Change in MASE ($\Delta\text{MASE}$) | Academic Target Status ($\text{RTR}=1.00, \Delta\text{MASE}\le 10\%$) |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **Baseline Control** | $M_0$: Diurnal Naive ($y_{t-24}$) | 253.6 | 253.6 | 1.00 | 0.0% | 0.0% | Benchmark Reference |
| **Deterministic Baseline** | $M_1^*$: Deterministic Sched Bank Volatility | 313.4 | 326.5 | **1.04** | **+4.2%** | **+4.0%** (+0.038) | **TARGET MET (WINNER)** |
| **Probabilistic / ML** | $M_3$: Supervised Volatility GBR | 273.5 | 295.1 | 1.08 | +7.9% | +8.3% (+0.065) | Passes Both Targets ($\le 10\%$) |
| **Dynamic Hybrid** | $M_5$: Sequential SARIMA-Tree Volatility Hybrid | 222.1 | 264.3 | **1.19** | **+19.0%** | **+21.5%** (+0.142) | **FAILS BOTH TARGETS** |

### Empirical Evaluation of Generalizability Across Facilities
Evaluating the third dimension of **Hypothesis 1**, the methodology posited that **first-principles deterministic models would generalize significantly better across distinct terminal layouts than complex, over-parameterized models**. To rigorously test zero-shot transferability without local retraining, models trained on United at Newark Liberty (EWR Terminal C) were directly deployed to Delta at New York LaGuardia (LGA Terminal C) within Cluster 3, holding macro New York TRACON airspace congestion constant while testing spatial transfer across different carrier bank structures and facility geometries.

The performance targets for Generalizability were strictly specified:
1. **Relative Transfer Ratio ($\text{RTR} = \text{RMSE}_{\text{transfer}} / \text{RMSE}_{\text{in-sample}} = 1.00$)**.
2. **Change in MASE on Transfer ($\Delta\text{MASE}_{\text{transfer}} \le 10.0\%$)**, ensuring minimal performance penalty.

* **The Deterministic Schedule Bank Baseline ($M_1^*$) is the DECISIVE WINNER of Generalizability**:
  * $M_1^*$ achieves an $\text{RTR}$ of **1.04** ($\approx 1.00$, target met) and a $\Delta\text{MASE}$ of only **+4.0%** (+0.038, well below the 10.0% ceiling), suffering a mere +4.2% RMSE transfer degradation.
  * Because $M_1^*$ relies on universal physical flight schedule convolution and empirical passenger show-up distributions, its structural formulation is completely invariant to facility-specific quirks. In cross-cluster transfer (DTW $\to$ PHL), $M_1^*$ achieves an $\text{RTR}$ of **1.003**, verifying complete spatial generalizability.
* **The Dynamic Cyber-Physical Hybrid ($M_5$) DECISIVELY FAILS the Generalizability Targets**:
  * $M_5$ experiences a severe **+19.0% transfer degradation**, with an $\text{RTR}$ of **1.19** (failing the target of 1.00) and a $\Delta\text{MASE}$ surge of **+21.5%** (+0.142, failing the $\le 10.0\%$ threshold).
  * This empirical failure confirms the central thesis of asymmetric trade-offs: the non-linear decision tree residual component of $M_5$ overfits to Newark's specific terminal geometry, flight bank timings, and local gate configurations. When transferred to LaGuardia without local recalibration, those specialized decision boundaries fail, imposing a heavy transfer penalty.
* **Supervised Machine Learning ($M_3$)** exhibits robust intermediate portability ($\text{RTR} = 1.08$, $\Delta\text{MASE} = +8.3\% \le 10\%$), passing the transfer targets due to standardized OTP feature scaling.

### Generalizability via Standardized Volatility Archetypes
The architectural contrast between over-parameterized models and volatility-conditioned frameworks highlights two key spatial behaviors:
* **Why Complex Black-Box Models Over-Specialize**: Models trained directly on raw terminal features overfit to local gate layouts, carrier hub bank structures, and unique terminal geometry.
* **Why Volatility Archetypes Generalize**: By categorizing operations into standardized volatility archetypes (e.g., *Outbound Business Surge*, *Midweek Operational Reset*, *Leisure Return Cascade*), the modeling framework abstracts away airport-specific idiosyncrasies. An outbound business surge at Boston Logan (BOS) follows the identical queuing variance profile as an outbound business surge at Chicago O'Hare (ORD). This enables seamless multi-airport deployment across the Top 25 network without site-specific recalibration.

## Master Synthesis and Operational Recommendations

Table 5.4  
*Master Asymmetric Trade-Off Matrix Across the Four Canonical Models*

| Evaluation Dimension | Stated Academic Target | Baseline Control ($M_0$) | Deterministic Baseline ($M_1^*$) | Probabilistic / ML ($M_3$) | Dynamic Hybrid ($M_5$) | Dimension Winner & Operational Justification |
| :--- | :--- | :---: | :---: | :---: | :---: | :--- |
| **Dimension 1: Robustness** (Routine: Delay $< 15$m, 0 Cancels) | Lowest $\text{RMSE}_{\text{routine}}$; $\text{MASE}_{\text{routine}} < 0.70$ | $\text{RMSE} = 253.6$, $\text{MASE} = 1.000$ (Fails) | $\text{RMSE} = 313.4$, $\text{MASE} = 0.945$ (Fails) | $\text{RMSE} = 273.5$, $\text{MASE} = 0.680\text{--}0.700$ (**Target Met**) | $\text{RMSE} = \mathbf{222.1}$ (Lowest), $\text{MASE} = \mathbf{0.662}$ (**Target Met**) | **$M_5$ achieves lowest RMSE**; **$M_3$ wins Routine Pareto Efficiency** (meets target with zero online compute overhead). |
| **Dimension 2: Resilience** (Disruption: Delay $\ge 45$m or Cancels $\ge 5$) | $R_{\text{RMSE}} \approx 1.00$; Lowest $\text{MASE}_{\text{shock}}$; $\text{TTR} < 4.0\text{h}$ | $R = 1.00$, $\text{MASE} = 1.000$, $\text{TTR} = 8.4\text{h}$ | $R = 1.32$, $\text{MASE} = 1.082$, $\text{TTR} = 7.8\text{h}$ | $R = 2.14$ (Fragile), $\text{MASE} = 0.812$, $\text{TTR} = 5.4\text{h}$ | $R = \mathbf{1.05}$ (**Target Met**), $\text{MASE} = \mathbf{0.694}$ (Lowest), $\text{TTR} = \mathbf{2.8\text{h}}$ (**Target Met**) | **$M_5$ DECISIVE WINNER**: Closed-loop recursive feedback ($e_{t-1}$) prevents empty-checkpoint collapse and recovers in 2.8h. |
| **Dimension 3: Generalizability** (Zero-Shot Transfer: EWR $\to$ LGA) | $\text{RTR} = 1.00$; $\Delta\text{MASE} \le 10.0\%$ | $\text{RTR} = 1.00$, $\Delta\text{MASE} = 0.0\%$ (Static Ref) | $\text{RTR} = \mathbf{1.04}$ (**Target Met**), $\Delta\text{MASE} = \mathbf{+4.0\%}$ (**Target Met**) | $\text{RTR} = 1.08$, $\Delta\text{MASE} = +8.3\%$ (Passes) | $\text{RTR} = \mathbf{1.19}$ (**FAILS TARGET**), $\Delta\text{MASE} = \mathbf{+21.5\%}$ (**FAILS TARGET**) | **$M_1^*$ DECISIVE WINNER**: Physical schedule convolution is invariant to facility layout; $M_5$ overfits to local gate geometry. |

### Deep-Dive: Values versus Volatility Paradigm Across Temporal Horizons
A core theoretical contribution of this thesis is the empirical demonstration of the **Values versus Volatility Paradigm**:
1. **Multi-Day Rolling Volatility ($\sigma_{\text{TSA, 7d}}$, pax/day)**:
   * **Feature Values Completely Collapse**: Standard feature values (raw scheduled flights, average delay minutes) generate negative out-of-time test scores ($R^2 = -0.2688$ in OLS; $R^2 = -0.0506$ in GBR). Because scheduled flight counts remain relatively stable across consecutive weeks, static volume features cannot detect shifts in temporal turbulence.
   * **Feature Volatility Succeeds**: In contrast, Feature Volatility attributes (rolling 7-day schedule variance, cancellation volatility, and delay dispersion) achieve **$R^2 = +0.2313$ (OLS) and $R^2 = +0.3105$ (GBR)**, improving to **$R^2 = +0.3166$** in the Combined Model, while slashing RMSE from 4,090.7 to 3,002.3 pax/day.
2. **Delay Volatility Transmission**:
   Cross-dataset econometric correlation demonstrates that **Flight Departure Delay Volatility ($CV_{\text{delay}}$)** is significantly coupled with checkpoint arrival volatility ($r = +0.4373, R^2 = 19.13\%, p = 0.0288$). Conversely, raw flight departure delay minutes show zero linear correlation ($r = -0.0620, p = 0.769$). Delays only disrupt checkpoint operations when they are erratic and disperse passenger arrival timing across banks.
3. **Master Consensus Factor Weights**:
   Synthesizing regularized regressions and tree ensembles confirms that schedule dispersion (`sched_rolling_7d_mean`, 23.73%; `sched_hourly_mean`, 6.91%) and operational volatility (`otp_cancellation_volatility_cv`, 8.79%; `CV_{\text{delay}}`, 4.32%) dominate predictive power, accounting for over 80% of consensus importance.

### The Regime-Switched Gated Inference Engine
To operationalize these empirical findings, the Transportation Security Administration (TSA) and Airport Operations Centers (AOC) should deploy a **Regime-Switched Gated Inference Engine**—an automated decision tool that monitors airport turbulence and automatically selects the most suitable forecasting model:

* **Gate 1: Routine Flow Track ($\text{Turbulence Shock Index } T(h) < 0.75$)**
  * *Operating Regimes*: Calm seasonal periods (*1_OFF_PEAK*), midweek baseline days (Tuesday and Wednesday), and steady midday hours (08:00–13:00).
  * *Assigned Architecture*: The Supervised Volatility Gradient Boosted Regressor ($M_3$).
  * *Operational Profile*: Fast, automated execution delivering superior point accuracy ($\text{MASE} = 0.779$) with near-zero computing overhead and high portability across diverse terminal layouts ($RTR = 1.08$).
* **Gate 2: Tactical Shock Track ($\text{Turbulence Shock Index } T(h) \ge 0.75$)**
  * *Operating Regimes*: Summer severe thunderstorm lines (*3_PEAK*), peak holiday travel corridors, concentrated Monday morning rushes, Sunday evening return cascades, and acute departure delay dispersion ($\sigma_{\text{Delay}} > 45$ min).
  * *Assigned Architecture*: The Sequential Two-Stage SARIMA-Tree Volatility Hybrid ($M_5$).
  * *Operational Profile*: Activates live checkpoint queue feedback ($e_{t-1}$), maintaining tight error bounds ($R_{\text{MASE}} = 1.05$) and rapid recovery ($\text{TTR} = 2.8$ hours) during acute flight delay cascades to prevent checkpoint staffing shortfalls.

### Conformal Prediction and Dynamic Lane Staffing Buffers
Airport checkpoint administrators can directly translate predicted throughput volatility ($\hat{\sigma}_{\text{TSA}, t}$) into risk-buffered lane configurations using conformal prediction principles:
$$c(t) = \left\lceil \frac{\hat{\mu}_t + z_q \cdot \hat{\sigma}_{\text{TSA}, t}}{\mu_{\text{lane}}} \right\rceil$$
where $\mu_{\text{lane}}$ is the nominal throughput capacity of an open screening lane (~180 to 220 pax/lane/hr), and $z_q$ is the coverage quantile factor (e.g., $z_{0.85} = 1.036$ for an 85% non-exceedance guarantee, or the empirical conformal quantile $\hat{q}_{0.85}$). Under traditional deterministic staffing, lanes are scheduled based solely on point expectation $\hat{\mu}_t$, guaranteeing that during stochastic arrival rushes, queues saturate and wait times explode exponentially according to Kingman's formula ($W_q \propto C_a^2$). By dynamically scaling lane capacity with predicted volatility $\hat{\sigma}_t$, airports maintain stable queue wait times without chronic overstaffing during quiescent periods.

### Strategic Implications for Airport and Security Authorities
1. **Dynamic Checkpoint Allocation**: Checkpoint staffing models should replace static time-of-day tables with empirical lead-lag passenger show-up schedules conditioned on flight bank volatility.
2. **Connecting Ratio Integration**: Centralized security operations must dynamically scale demand using airline O&D survey ratios to avoid over-allocating screening lanes at connecting hubs.
3. **Deployment of Two-Stage Hybrid Estimators**: Airport operations centers should adopt the regime-switched framework that utilizes interpretable decision-tree models for routine staffing while incorporating live checkpoint throughput feedback ($t-1$) during severe convective ground stop disruptions.

## Empirical Cross-Project Synthesis
By implementing the research methodology across three distinct computational paradigms—**Supervised Machine Learning (Project 1)**, **First-Principles Queueing Theory (Project 2)**, and **Dynamic State-Space Modeling (Project 3)**—this thesis provides a unified, multi-perspective empirical validation of its overarching hypothesis (**Hypothesis 1**):

1. **Routine Operational Accuracy Validation**:
   * *Project 1 Supervised ML*: The Sequential SARIMA-Tree Volatility Hybrid achieved the highest out-of-time accuracy on the 2025 holdout dataset ($R^2 = 0.7483, \text{MASE} = 0.662, \text{RMSE} = 222.1\text{ pax/hr}$), proving that non-linear gradient-boosted trees excel at capturing complex diurnal patterns.
   * *Project 2 Queueing Simulation*: Proved that when active screening lanes match incoming passenger banks (DTW McNamara Terminal), steady-state waiting times remain exceptionally low ($\mu_{\text{wait}} = 0.9$ min, $P_{95} \le 7.7$ min).

2. **Resilience Validation Under Severe Disruption**:
   * *Project 2 Queue Simulation*: Directly exposed the operational hazard of static lane allocation. Under an acute 50% lane outage combined with a flight surge, static lane allocation saturated, with wait times capping at 60 minutes and accumulating 27,763 passenger-hours of delay. In contrast, the **Dynamic Hybrid Allocation Model** reduced total passenger delay by **80.1%** (slashing backlog to 5,514 passenger-hours and keeping 95th-percentile wait times at 11.5 minutes) by dynamically mobilizing reserve screening capacity.
   * *Project 3 State-Space Tracking*: Demonstrated that recursive Kalman innovation updates immediately recognize delayed flight holds, avoiding the false empty-checkpoint predictions of pure machine learning.

3. **Generalizability Validation (Cross-Airport Portability)**:
   * *Project 3 State-Space Transfer*: When deploying directly without local retraining across matched airport pairs sharing identical airspace (EWR $\to$ LGA in the New York TRACON), the Moving Horizon Baseline suffered an 86.7% error surge ($\text{RTR} = 1.86$) and the Probabilistic Sequence Model degraded by 43.8% ($\text{RTR} = 1.44$).
   * In stark contrast, the **Extended Kalman Filter State-Space Hybrid achieved remarkable transfer stability ($\Delta = 0.0\%, \text{RTR} = 1.00$ on EWR $\to$ LGA; $\text{RTR} = 0.86$ on DTW $\to$ PHL)**. Because state-space models continuously calibrate queue state using live throughput residuals ($t-1$), they achieve seamless cross-airport portability without facility-specific over-specialization.
