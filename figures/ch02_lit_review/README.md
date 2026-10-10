# Chapter II: Literature Review Exhibits & Figures
## Evaluating Predictive Techniques to Model Stochastic Airport Passenger Flow (MSAA / Gleich 700B)

> **Chapter Purpose**: Theoretical foundations, heavy-traffic queuing dynamics, historical modeling paradigms, and operational coupling frameworks for **Chapter II (*Literature Review*)**.

---

### Exhibit & Figure Inventory

| Figure / Table ID | Visual Graphic (`.png`) | Companion Data (`.csv`) | Manuscript Target Location | Operational Function & Theoretical Rationale |
| :--- | :--- | :--- | :--- | :--- |
| **Figure 2.1** | `pax stochastic arrival.png` | `passenger_stochastic_arrival_parameters.csv` | Under Section `## Traditional Approaches` (Paragraph 10) | **The Checkpoint Tipping Point (Kingman's Heavy-Traffic Curve)**: Demonstrates quadratic queue escalation with arrival burstiness ($C_a^2$) under Kingman's formula ($W_q \approx \frac{\rho}{1-\rho} \frac{C_a^2+C_s^2}{2} \frac{1}{\mu}$) as server utilization $\rho \to 1.0$. |
| **Table 2.1** | `exploratory metric criteria research .png` | `exploratory_metric_criteria_research.csv` | Following Section `## Simulation Modeling` (Paragraph 21) | **Comparative Synthesis of Airport Flow Paradigms**: Contrasts historical modeling mechanisms (pure physics, queuing, time-series, supervised ML) across data latency, operational fidelity, and shock vulnerabilities. |
| **Figure 2.2** | `Model walk through.png` | `model_walkthrough_architecture.csv` | Following Section `## Hybrid Architectures` (Paragraph 34) | **Two-Stage Sequential Hybrid Architecture**: Schematically illustrates Stage 1 (recurring flight bank schedule cycles) feeding baseline predictions into Stage 2 (live recursive error innovation feedback $e_{t-1}$). |
| **Framework** | `clusting and connecting paradox.png` | `clustering_and_connecting_paradox.csv` | Section `## Passenger Flow Dynamics` | **The Connecting Passenger Paradox**: Illustrates the hub disconnect where airside connecting passenger transfers bypass landside TSA checkpoints, requiring DB1B coupon deflation. |
| **Framework** | `otp & tsa.png` | `otp_and_tsa_volume_coupling.csv` | Section `## Flight Delays and Checkpoints` | **TSA & OTP Volume Coupling vs. Volatility**: Contrasts the decoupling of raw volume counts with the tight coupling of departure delay volatility and throughput volatility. |
| **Framework** | `OTP volatility.png` | `otp_volatility.csv` | Section `## Volatility Dynamics` | **Flight Departure Delay Volatility Regimes**: Formalizes delay standard deviation and coefficient of variation ($CV_{\\text{delay}}$) metrics. |
