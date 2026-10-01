# CHAPTER I – INTRODUCTION

## 1.1 Context and Operational Motivation
Commercial air travel demand in the United States continues to outstrip the capacity of landside airport terminal infrastructure.  Passenger security‑screening checkpoints have become the primary bottleneck for the National Airspace System (NAS).  Traditional staffing plans rely on static, time‑of‑day tables or simple scaling of published flight schedules.  Post‑pandemic volatility—seasonal demand shocks, severe weather‑induced ground‑delay programs, and abrupt schedule cancellations—has exposed the fragility of these approaches.

## 1.2 Significance of the Study
The thesis advances both theory and practice.  Theoretically, it develops a **multidimensional evaluation framework** that explicitly separates **robustness**, **resilience**, and **generalizability** of forecasting models.  Practically, it delivers decision‑support tools that enable Federal Security Directors (FSDs), airline hub operations managers, and FAA planners to allocate checkpoint staff more accurately, reducing passenger wait times and avoiding unnecessary capital expansion.

## 1.3 Statement of the Problem
Existing checkpoint‑demand models treat passenger arrivals as a direct, contemporaneous function of scheduled departures.  This assumption ignores (i) the **lead‑lag** relationship between ticketed seats and actual landside arrivals, (ii) the **hub‑disconnect** where a large share of passengers transfer airside and never pass through security, and (iii) the lack of a performance metric that captures behavior under extreme disruptions.  Consequently, staffing plans derived from these models regularly under‑ or over‑estimate demand, leading to chronic congestion or idle resources.

## 1.4 Purpose Statement
The primary objective is to **evaluate and compare** three families of predictive models—deterministic baselines, probabilistic/machine‑learning approaches, and sequential two‑stage hybrid architectures—across the three operational dimensions (robustness, resilience, generalizability).  The study further demonstrates how integrating **connecting‑passenger ratios** from BTS DB‑1B surveys and **lead‑time show‑up curves** (ACRP Report 40) improves demand estimation.

## 1.5 Research Question
*Which predictive modeling frameworks are most effective for forecasting airport passenger‑security screening throughput when prioritizing (a) robustness (routine accuracy), (b) resilience (performance under severe disruption), or (c) generalizability (cross‑airport portability) as the primary evaluation metric?*

## 1.6 Delimitations
1. **Geographic scope** – Top 25 U.S. commercial airfields (FAA hub classifications).  
2. **Temporal scope** – Jan 1 2019 through Dec 31 2025; model development limited to the post‑mask‑repeal period (May 1 2022 – Dec 2024).  
3. **Data sources** – Publicly available TSA FOIA checkpoint logs, BTS On‑Time Performance, BTS Form 41 Schedule T‑100, and BTS DB‑1B/DB‑1C ticket‑coupon surveys.  
4. **Evaluation** – Models are assessed on a 12‑month out‑of‑time holdout (2025) and on a 9‑airport experimentally balanced cohort.

## 1.7 Limitations and Assumptions
* **Checkpoint‑level variables** such as exact lane staffing or TSA‑PreCheck lane allocation are not observable; throughput is aggregated across all lanes within a terminal complex.
* **Connecting‑passenger ratios** are assumed stable within a quarterly window; rapid shifts in airline hub‑connectivity could introduce bias.
* **Zero‑throughput intervals** occurring overnight are treated as true operational closures rather than missing data.
* **Model transparency** – Gradient‑boosted decision trees are used for interpretability; deep neural networks are excluded to avoid black‑box opacity.

*The remainder of the thesis provides a detailed literature review (Chapter II), methodological exposition (Chapter III), empirical results (Chapter IV), and an in‑depth discussion (Chapter V).*
