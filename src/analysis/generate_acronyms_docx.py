"""
generate_acronyms_docx.py
=========================
Generates the comprehensive, APA 7th Edition-compliant Word document (.docx)
and synchronized Markdown (.md) files for the List of Acronyms and Abbreviations
used across Chapters I through V of the master's thesis:

"Evaluating Predictive Techniques to Model Stochastic Airport Passenger Flow"
(Leila Gleich, MSAA / Gleich 700B, Embry-Riddle Aeronautical University).

Non-Negotiable Compliance:
- Policy 1.1: Explicitly requested in writing by the user in the current session.
- Policy 2.1: Primary dependent target is Throughput Volatility (sigma_TSA, CV_TSA), NOT volume.
- Policy 3.1 & 3.2: 3 candidate models + baseline control; zero internal code tags (M0, M1*, M3, M5).
- Policy 4.1: Asymmetric performance trade-offs preserved (Model 1 wins Generalizability,
              Model 2 wins Routine Pareto Efficiency, Model 3 wins Resilience & RMSE).
- Policy 5: Authentic aviation terminology (Nominal On-Time Baseline, Routine Daily Operations,
            Irregular Operations / IROPS); zero prohibited lab jargon.
- Policy 6.1: APA 7th Edition table formatting (top rule, header underline, bottom rule,
              no vertical rules, Times New Roman typography).
"""

import os
import sys
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import qn, nsdecls

# Master Dictionary of Acronyms across the Thesis Manuscripts
ACRONYM_DATA = [
    # A
    {
        "acronym": "A14",
        "full_term": "Air Carrier On-Time Reporting Benchmark (14-Minute Arrival Delay Tolerance)",
        "category": "Regulatory & Air Traffic Management",
        "cat_id": 1,
        "definition": "The federal regulatory reporting benchmark established by the Federal Aviation Administration (FAA) and Bureau of Transportation Statistics (BTS) under 14 CFR Part 234. A commercial domestic flight is classified as on-time if it arrives at the gate within 14 minutes and 59 seconds of its scheduled gate arrival time. In the thesis, A14 defines the boundary of the Nominal On-Time Baseline regime (departure delays < 15 minutes, zero cancellations)."
    },
    {
        "acronym": "AA",
        "full_term": "American Airlines",
        "category": "Commercial Air Carriers",
        "cat_id": 4,
        "definition": "Major U.S. network legacy carrier (IATA code: AA). In the thesis, carrier-exclusive terminal complexes operated by American Airlines are analyzed at Dallas/Fort Worth (DFW), Charlotte Douglas (CLT), Philadelphia (PHL), and New York LaGuardia (LGA) during the purposive 4-tier filtering process to isolate unconfounded flight bank arrivals."
    },
    {
        "acronym": "ACRP",
        "full_term": "Airport Cooperative Research Program",
        "category": "Aviation Research & Literature",
        "cat_id": 1,
        "definition": "An applied research program sponsored by the FAA and administered by the Transportation Research Board (TRB). ACRP Report 40 ('Airport Passenger Convergent and Terminal Processing') provides the empirical passenger show-up curves convolved across scheduled airline flight banks in Model 1 (Deterministic Flight Schedule Model)."
    },
    {
        "acronym": "AI",
        "full_term": "Artificial Intelligence",
        "category": "Predictive Modeling & Computational Methods",
        "cat_id": 6,
        "definition": "The overarching computer science discipline encompassing machine learning, statistical pattern recognition, and autonomous operational decision systems; evaluated in the literature review to contrast empirical data-driven forecasting with deterministic operational models."
    },
    {
        "acronym": "ANN",
        "full_term": "Artificial Neural Network",
        "category": "Predictive Modeling & Computational Methods",
        "cat_id": 6,
        "definition": "A class of machine learning models structured as interconnected artificial neuron layers; reviewed in terminal passenger flow and delay modeling literature and contrasted with tree-based regressors and two-stage hybrid models."
    },
    {
        "acronym": "ANOVA",
        "full_term": "Analysis of Variance",
        "category": "Evaluation Metrics & Econometric Statistics",
        "cat_id": 7,
        "definition": "Statistical hypothesis testing framework used in empirical exploratory data analysis to evaluate variance components and statistical significance across airport clusters, days of the week, and operational disturbance regimes."
    },
    {
        "acronym": "AOC",
        "full_term": "Airport Operations Center",
        "category": "Airport Infrastructure & Operations",
        "cat_id": 2,
        "definition": "The central operational command facility at a commercial airport where airport authority staff, airline operations dispatchers, TSA security leadership, and law enforcement monitor real-time passenger terminal flow, gate assignments, runway conditions, and emergency responses."
    },
    {
        "acronym": "APA",
        "full_term": "American Psychological Association",
        "category": "Academic & Publishing Standards",
        "cat_id": 7,
        "definition": "The authoritative academic publishing standard (APA 7th edition, 2020) governing manuscript layout, heading hierarchy, in-text citations, statistical reporting format, and table structure (three horizontal rules, zero vertical rules) across the thesis."
    },
    {
        "acronym": "APE",
        "full_term": "Absolute Percentage Error",
        "category": "Evaluation Metrics & Econometric Statistics",
        "cat_id": 7,
        "definition": "The observation-level forecasting error ratio defined as |y_t - ŷ_t| / y_t. In the thesis, shown to produce catastrophic division-by-zero explosions during overnight checkpoint curfew hours when actual screening volumes approach zero (y_t ≈ 0), methodologically invalidating Mean Absolute Percentage Error (MAPE)."
    },
    {
        "acronym": "ARIMA",
        "full_term": "Autoregressive Integrated Moving Average",
        "category": "Predictive Modeling & Computational Methods",
        "cat_id": 6,
        "definition": "Classical linear time-series forecasting model combining autoregressive lags (p), integrated differencing (d), and moving average error innovations (q); serves as a benchmark in time-series passenger demand and terminal queue literature."
    },
    {
        "acronym": "ATC",
        "full_term": "Air Traffic Control",
        "category": "Regulatory & Air Traffic Management",
        "cat_id": 2,
        "definition": "The Federal Aviation Administration operational service responsible for directing aircraft safely on runways, taxiways, and throughout the National Airspace System, managing ground traffic sequencing and en-route flight separations."
    },
    {
        "acronym": "ATCSCC",
        "full_term": "Air Traffic Control System Command Center",
        "category": "Regulatory & Air Traffic Management",
        "cat_id": 2,
        "definition": "Centralized FAA air traffic management facility in Warrenton, Virginia, that monitors nationwide airspace demand and coordinates traffic management initiatives, including Ground Delay Programs (GDPs), ground stops, and airspace routing reconfigurations."
    },
    {
        "acronym": "ATL",
        "full_term": "Hartsfield-Jackson Atlanta International Airport",
        "category": "Airport Cohort & Airfield Codes",
        "cat_id": 4,
        "definition": "Major commercial connecting hub (IATA code: ATL; Delta Air Lines primary mega-complex). Evaluated in the Top 25 network clustering census; excluded from the primary 9-airport experimental cohort during 4-tier filtering due to extreme connecting transfer ratios (>65%) that confound TSA checkpoint throughput."
    },

    # B
    {
        "acronym": "BI",
        "full_term": "Business Intelligence",
        "category": "Data Systems & Information Architecture",
        "cat_id": 3,
        "definition": "Data systems, dashboards, and reporting architectures deployed by airport authorities and federal directors to track terminal checkpoint throughput, queue waiting times, and resource allocation."
    },
    {
        "acronym": "BOS",
        "full_term": "Boston Logan International Airport",
        "category": "Airport Cohort & Airfield Codes",
        "cat_id": 4,
        "definition": "Commercial airport (IATA code: BOS). Evaluated in Top 25 network clustering and 4-tier filtering as a prominent Northeast commercial origin-and-destination complex."
    },
    {
        "acronym": "BTS",
        "full_term": "Bureau of Transportation Statistics",
        "category": "Federal Aviation Datasets & Schemas",
        "cat_id": 3,
        "definition": "Statistical operating administration within the U.S. Department of Transportation (USDOT) that collects, compiles, and publishes official national transportation datasets, including BTS Form 234 (On-Time Performance), Form 41 (Schedule T-100), and the DB1B Origin and Destination Survey."
    },
    {
        "acronym": "BTS Form 41",
        "full_term": "BTS Form 41 Financial and Operating Statistics (Schedule T-100)",
        "category": "Federal Aviation Datasets & Schemas",
        "cat_id": 3,
        "definition": "Federal regulatory reporting schedule filed by commercial airlines containing monthly non-stop domestic flight segment records, available aircraft seat capacity, flown revenue passenger counts, and passenger load factors."
    },
    {
        "acronym": "BTS Form 234",
        "full_term": "BTS Form 234 Airline On-Time Performance Survey",
        "category": "Federal Aviation Datasets & Schemas",
        "cat_id": 3,
        "definition": "Mandatory monthly flight-by-flight operational database providing departure delays, arrival delays, taxi-out queue durations, airborne times, and cause-of-delay categories (Carrier, Weather, NAS, Security, Late Aircraft) across reporting air carriers."
    },

    # C
    {
        "acronym": "CAT",
        "full_term": "Credential Authentication Technology",
        "category": "Airport Infrastructure & Operations",
        "cat_id": 2,
        "definition": "Digital identity verification scanners deployed at TSA checkpoint lanes that scan traveler photo identification (driver's licenses, passports) to confirm flight reservations directly against airline manifest databases in real time without requiring a boarding pass."
    },
    {
        "acronym": "CKPT",
        "full_term": "Checkpoint",
        "category": "Airport Infrastructure & Operations",
        "cat_id": 2,
        "definition": "Standard operational abbreviation used in TSA screening logs, database schemas, and terminal facility blueprints denoting a physical passenger screening checkpoint complex."
    },
    {
        "acronym": "CLT",
        "full_term": "Charlotte Douglas International Airport",
        "category": "Airport Cohort & Airfield Codes",
        "cat_id": 4,
        "definition": "Major connecting hub (IATA code: CLT) dominated by American Airlines. Evaluated during 4-tier filtering and Top 25 network clustering to examine connecting transfer passenger deconvolution."
    },
    {
        "acronym": "CNN",
        "full_term": "Convolutional Neural Network",
        "category": "Predictive Modeling & Computational Methods",
        "cat_id": 6,
        "definition": "Deep artificial neural network architecture employing convolutional filter banks over temporal sequences; reviewed in terminal passenger flow and delay modeling literature."
    },
    {
        "acronym": "COVID-19",
        "full_term": "Coronavirus Disease 2019",
        "category": "Operational Regimes & Demarcation",
        "cat_id": 7,
        "definition": "Global viral pandemic causing historic structural disruption across the commercial aviation sector; in the thesis, the study baseline utilizes Candidate B demarcation (May 1, 2022 to December 31, 2025) to isolate post-mask-mandate stable passenger behavior from pandemic anomalies."
    },
    {
        "acronym": "CSV",
        "full_term": "Comma-Separated Values",
        "category": "Data Systems & Information Architecture",
        "cat_id": 3,
        "definition": "Standard tabular data file format used across the thesis repository to store reproducible research tables, benchmark outputs, and conformed experimental metrics."
    },
    {
        "acronym": "CT",
        "full_term": "Computed Tomography",
        "category": "Airport Infrastructure & Operations",
        "cat_id": 2,
        "definition": "Advanced 3D X-ray screening technology deployed at TSA checkpoint lanes that generates high-resolution volumetric scans of carry-on baggage, altering lane service times and processing efficiency."
    },
    {
        "acronym": "CTU",
        "full_term": "Central Terminal Unit",
        "category": "Airport Infrastructure & Operations",
        "cat_id": 2,
        "definition": "Architectural classification for centralized airport passenger processing terminal facilities, as distinguished from decentralized or modular satellite concourses."
    },
    {
        "acronym": "CUSUM",
        "full_term": "Cumulative Sum Structural Break Test",
        "category": "Evaluation Metrics & Econometric Statistics",
        "cat_id": 7,
        "definition": "Sequential statistical quality control chart and econometric test used in Chapter III to detect structural parameter shifts and change-points across time-series error residuals, validating post-COVID sample stability."
    },
    {
        "acronym": "CV",
        "full_term": "Coefficient of Variation",
        "category": "Evaluation Metrics & Econometric Statistics",
        "cat_id": 7,
        "definition": "Dimensionless scale-free measure of relative dispersion defined as the ratio of the standard deviation to the mean (CV = σ / μ). Used throughout the thesis to quantify passenger arrival burstiness independent of airport size."
    },
    {
        "acronym": "CVI",
        "full_term": "Coupled Volatility Index (Landside-Airside Volatility Interaction Term)",
        "category": "Evaluation Metrics & Econometric Statistics",
        "cat_id": 7,
        "definition": "Operational interaction term defined as the product of scale-free passenger throughput volatility (CV_TSA) and flight departure delay dispersion (σ_Delay), measuring compounding operational turbulence when landside surges coincide with airside flight delays."
    },
    {
        "acronym": "CV_TSA",
        "full_term": "Coefficient of Variation of TSA Passenger Screening Throughput",
        "category": "Evaluation Metrics & Econometric Statistics",
        "cat_id": 7,
        "definition": "Primary scale-free dependent target of the thesis, defined as the hourly standard deviation of passenger screening throughput divided by mean hourly throughput across the diurnal cycle (CV_TSA,hr = σ_hr / μ_hr). Captures checkpoint arrival burstiness."
    },

    # D
    {
        "acronym": "DB1B",
        "full_term": "Airline Origin and Destination Survey (Data Bank 1B)",
        "category": "Federal Aviation Datasets & Schemas",
        "cat_id": 3,
        "definition": "A 10% random sample of all commercial airline passenger tickets collected quarterly by the Bureau of Transportation Statistics, reporting complete itinerary routings, operating carriers, and true origin-destination pairs."
    },
    {
        "acronym": "DB1C",
        "full_term": "Origin and Destination Ticket Coupon Survey (Data Bank 1C)",
        "category": "Federal Aviation Datasets & Schemas",
        "cat_id": 3,
        "definition": "Flight-coupon segment table within the BTS DB1B database used in Chapter III to calculate carrier-specific transfer ratios and derive the Connecting Passenger Deflator."
    },
    {
        "acronym": "DCA",
        "full_term": "Ronald Reagan Washington National Airport",
        "category": "Airport Cohort & Airfield Codes",
        "cat_id": 4,
        "definition": "Perimeter-restricted, slot-controlled commercial airport in Arlington, Virginia (IATA code: DCA), evaluated in Top 25 network clustering."
    },
    {
        "acronym": "DDL",
        "full_term": "Data Definition Language",
        "category": "Data Systems & Information Architecture",
        "cat_id": 3,
        "definition": "SQL schema specification syntax defining table structures, column data types, primary keys, and relational constraints in the conformed research warehouse."
    },
    {
        "acronym": "DEN",
        "full_term": "Denver International Airport",
        "category": "Airport Cohort & Airfield Codes",
        "cat_id": 4,
        "definition": "Major connecting hub and commercial mega-airport (IATA code: DEN). Analyzed during Top 25 network clustering as a dual-carrier hub complex (United / Southwest)."
    },
    {
        "acronym": "DES",
        "full_term": "Discrete Event Simulation",
        "category": "Predictive Modeling & Computational Methods",
        "cat_id": 5,
        "definition": "Computational simulation modeling technique that represents an airport terminal as a discrete sequence of events in time (passenger arrivals, ID checks, bag divestiture, X-ray scanning). Evaluated in Chapter II as high-fidelity but computationally prohibitive for real-time dispatch."
    },
    {
        "acronym": "DFW",
        "full_term": "Dallas Fort Worth International Airport",
        "category": "Airport Cohort & Airfield Codes",
        "cat_id": 4,
        "definition": "American Airlines primary mega-connecting hub (IATA code: DFW). Evaluated in Top 25 clustering and 4-tier filtering to benchmark terminal passenger transfer dynamics."
    },
    {
        "acronym": "DL",
        "full_term": "Delta Air Lines",
        "category": "Commercial Air Carriers",
        "cat_id": 4,
        "definition": "Major U.S. network legacy carrier (IATA code: DL). Operates dedicated terminal complexes analyzed at Detroit (DTW McNamara Terminal), Salt Lake City (SLC), and New York LaGuardia (LGA Terminal C)."
    },
    {
        "acronym": "DM",
        "full_term": "Diebold-Mariano Test Statistic",
        "category": "Evaluation Metrics & Econometric Statistics",
        "cat_id": 7,
        "definition": "Non-parametric econometric test comparing the predictive accuracy of competing time-series forecasts under serial correlation and heteroskedasticity. Formulated in Appendix C to establish rigorous statistical significance of Model 2 and Model 3 over Model 1."
    },
    {
        "acronym": "DOT",
        "full_term": "Department of Transportation",
        "category": "Regulatory & Air Traffic Management",
        "cat_id": 1,
        "definition": "United States Department of Transportation (USDOT), the cabinet department overseeing federal transportation agencies including the FAA and BTS."
    },
    {
        "acronym": "DOW",
        "full_term": "Day of Week",
        "category": "Operational Regimes & Demarcation",
        "cat_id": 7,
        "definition": "Categorical temporal feature capturing cyclical weekly demand fluctuations (e.g., Thursday/Friday business travel waves versus Sunday leisure return peaks)."
    },
    {
        "acronym": "DTW",
        "full_term": "Detroit Metropolitan Wayne County Airport",
        "category": "Airport Cohort & Airfield Codes",
        "cat_id": 4,
        "definition": "Major connecting hub (IATA code: DTW). The McNamara Terminal at DTW represents an isolated carrier-dedicated screening facility (Delta Air Lines) evaluated in the balanced 4x4 experimental cohort."
    },

    # E
    {
        "acronym": "ETL",
        "full_term": "Extract, Transform, and Load",
        "category": "Data Systems & Information Architecture",
        "cat_id": 3,
        "definition": "The three-stage data pipeline architecture utilized to ingest raw federal records (TSA FOIA, BTS OTP, BTS T-100, DB1B), execute data cleansing and schema conformance, and load star-schema analytical tables."
    },
    {
        "acronym": "EWR",
        "full_term": "Newark Liberty International Airport",
        "category": "Airport Cohort & Airfield Codes",
        "cat_id": 4,
        "definition": "Primary commercial hub (IATA code: EWR). Terminal C, an isolated United Airlines screening complex, serves as the primary development testbed airfield for lead-lag deconvolution and the in-sample baseline for zero-shot spatial transfer."
    },

    # F
    {
        "acronym": "FAA",
        "full_term": "Federal Aviation Administration",
        "category": "Regulatory & Air Traffic Management",
        "cat_id": 1,
        "definition": "Operating administration of the U.S. Department of Transportation responsible for the safety, air traffic management, regulatory oversight, and infrastructure standards of civil aviation."
    },
    {
        "acronym": "FIFO",
        "full_term": "First-In, First-Out",
        "category": "Queuing Theory & Passenger Dynamics",
        "cat_id": 5,
        "definition": "Classical queuing discipline where passengers are screened in the exact sequential order of their arrival at the checkpoint queue entrance."
    },
    {
        "acronym": "FINM",
        "full_term": "Fusion Intelligence Network Model",
        "category": "Predictive Modeling & Computational Methods",
        "cat_id": 6,
        "definition": "Predictive multi-source intelligence architecture cited in literature integrating heterogeneous data feeds across airside and landside operations."
    },
    {
        "acronym": "FOIA",
        "full_term": "Freedom of Information Act",
        "category": "Federal Aviation Datasets & Schemas",
        "cat_id": 3,
        "definition": "Federal public records disclosure statute (5 U.S.C. § 552) through which the multi-year, hourly checkpoint-lane passenger screening dataset was acquired from the TSA for this research."
    },
    {
        "acronym": "FSD",
        "full_term": "Federal Security Director",
        "category": "Airport Infrastructure & Operations",
        "cat_id": 2,
        "definition": "Senior executive official appointed by the TSA stationed at commercial airports, exercising operational authority over checkpoint staffing, screening procedures, and terminal security compliance."
    },

    # G
    {
        "acronym": "G/G/c",
        "full_term": "General Arrival / General Service / c-Server Queuing Model",
        "category": "Queuing Theory & Passenger Dynamics",
        "cat_id": 5,
        "definition": "Kendall notation for a multi-server queuing system with arbitrary inter-arrival distributions, arbitrary service times, and c parallel screening lanes operating in parallel."
    },
    {
        "acronym": "GBM",
        "full_term": "Gradient Boosting Machine",
        "category": "Predictive Modeling & Computational Methods",
        "cat_id": 6,
        "definition": "Supervised machine learning ensemble architecture that builds sequential decision trees to minimize empirical loss. Serves as the core regressor in Model 2 (Supervised Machine Learning Model)."
    },
    {
        "acronym": "GBDT",
        "full_term": "Gradient-Boosted Decision Trees",
        "category": "Predictive Modeling & Computational Methods",
        "cat_id": 6,
        "definition": "Alternative designation for Gradient Boosting Machines emphasizing tree-based weak learners."
    },
    {
        "acronym": "GDP",
        "full_term": "Ground Delay Program",
        "category": "Regulatory & Air Traffic Management",
        "cat_id": 2,
        "definition": "FAA air traffic management initiative implemented during severe weather or congestion that holds departing aircraft on the ground at origin airports, inducing lead-lag flight departure delays."
    },
    {
        "acronym": "GI/G/1",
        "full_term": "General Independent Arrival / General Service / Single Server Queuing Model",
        "category": "Queuing Theory & Passenger Dynamics",
        "cat_id": 5,
        "definition": "Kendall queuing notation representing single-server queues with general independent arrivals and service distributions, underlying Kingman's heavy-traffic approximation."
    },
    {
        "acronym": "GRU",
        "full_term": "Gated Recurrent Unit",
        "category": "Predictive Modeling & Computational Methods",
        "cat_id": 6,
        "definition": "Gated recurrent neural network architecture that models sequential temporal dependencies with reset and update gates; evaluated in Chapter II deep learning literature."
    },
    {
        "acronym": "GSPN",
        "full_term": "Generalized Stochastic Petri Nets",
        "category": "Predictive Modeling & Computational Methods",
        "cat_id": 6,
        "definition": "Mathematical and graphical modeling formalism utilized in terminal simulation literature to analyze concurrent, stochastic passenger movements."
    },

    # H
    {
        "acronym": "HAC",
        "full_term": "Heteroskedasticity and Autocorrelation Consistent",
        "category": "Evaluation Metrics & Econometric Statistics",
        "cat_id": 7,
        "definition": "Econometric covariance matrix estimator (Newey-West) that yields robust, unconfounded standard errors and test statistics when time-series residuals exhibit autocorrelation and conditional heteroskedasticity."
    },
    {
        "acronym": "HistGBM",
        "full_term": "Histogram-Based Gradient Boosting Machine",
        "category": "Predictive Modeling & Computational Methods",
        "cat_id": 6,
        "definition": "Optimized decision-tree gradient boosting implementation (scikit-learn HistGradientBoostingRegressor) that discretizes continuous features into integer bins; utilized in Model 2 for fast, robust execution."
    },
    {
        "acronym": "HOD",
        "full_term": "Hour of Day",
        "category": "Operational Regimes & Demarcation",
        "cat_id": 7,
        "definition": "Categorical temporal unit representing each of the 24 discrete hours within an operational day, capturing diurnal passenger bank rhythms."
    },
    {
        "acronym": "HPC",
        "full_term": "High-Performance Computing",
        "category": "Data Systems & Information Architecture",
        "cat_id": 3,
        "definition": "Distributed multi-core server infrastructure utilized for intensive ETL data processing, deconvolution algorithms, and machine learning cross-validation."
    },
    {
        "acronym": "HQBN",
        "full_term": "Hybrid Queue-based Bayesian Network",
        "category": "Predictive Modeling & Computational Methods",
        "cat_id": 6,
        "definition": "Probabilistic graphical modeling architecture combining Bayesian inference with queuing formulas to predict multi-stage airport delay propagation."
    },

    # I
    {
        "acronym": "IAD",
        "full_term": "Washington Dulles International Airport",
        "category": "Airport Cohort & Airfield Codes",
        "cat_id": 4,
        "definition": "Commercial hub airport (IATA code: IAD) in Northern Virginia operated by MWAA; evaluated in Top 25 network clustering as a United Airlines East Coast hub."
    },
    {
        "acronym": "IAH",
        "full_term": "George Bush Intercontinental Airport (Houston)",
        "category": "Airport Cohort & Airfield Codes",
        "cat_id": 4,
        "definition": "United Airlines primary southern hub complex (IATA code: IAH). Evaluated in the Top 25 network clustering and 4-tier filtering pipeline for dedicated terminal screening analysis."
    },
    {
        "acronym": "IATA",
        "full_term": "International Air Transport Association",
        "category": "Aviation Research & Literature",
        "cat_id": 1,
        "definition": "Global trade association representing commercial airlines, establishing international air transport standards, schedule data formats, and airport Level of Service (LOS) passenger space criteria."
    },
    {
        "acronym": "ICAO",
        "full_term": "International Civil Aviation Organization",
        "category": "Regulatory & Air Traffic Management",
        "cat_id": 1,
        "definition": "Specialized agency of the United Nations establishing global international civil aviation principles, airspace safety regulations, and airport design standards."
    },
    {
        "acronym": "IEEE",
        "full_term": "Institute of Electrical and Electronics Engineers",
        "category": "Academic & Publishing Standards",
        "cat_id": 7,
        "definition": "Professional technical organization publishing peer-reviewed research in transportation engineering, intelligent systems, and computational algorithms."
    },
    {
        "acronym": "ILP",
        "full_term": "Integer Linear Programming",
        "category": "Predictive Modeling & Computational Methods",
        "cat_id": 6,
        "definition": "Mathematical optimization technique used in terminal resource allocation and lane scheduling literature to determine optimal lane opening schedules subject to discrete constraints."
    },
    {
        "acronym": "IROPS",
        "full_term": "Irregular Operations",
        "category": "Operational Regimes & Demarcation",
        "cat_id": 7,
        "definition": "Severe operational disruptions (convective storms, equipment failures, ground stops; departure delays ≥ 45 min or cancellations ≥ 5) driving checkpoint queue spikes. Constitutes the core test regime for Dimension 2 (Resilience)."
    },
    {
        "acronym": "ISO",
        "full_term": "International Organization for Standardization",
        "category": "Academic & Publishing Standards",
        "cat_id": 7,
        "definition": "Independent international non-governmental organization developing worldwide industrial, quality, and data security standards."
    },
    {
        "acronym": "IT",
        "full_term": "Information Technology",
        "category": "Data Systems & Information Architecture",
        "cat_id": 3,
        "definition": "Enterprise computing, database architecture, and network infrastructure supporting airline reservation systems and airport operational command systems."
    },

    # J
    {
        "acronym": "JFK",
        "full_term": "John F. Kennedy International Airport",
        "category": "Airport Cohort & Airfield Codes",
        "cat_id": 4,
        "definition": "Major international gateway in New York (IATA code: JFK). Analyzed during Top 25 network clustering and contrasted with LGA in 4-tier filtering to examine decentralized multi-terminal structures."
    },

    # K
    {
        "acronym": "KS",
        "full_term": "Kolmogorov-Smirnov Test",
        "category": "Evaluation Metrics & Econometric Statistics",
        "cat_id": 7,
        "definition": "Non-parametric statistical goodness-of-fit test comparing empirical distributions; utilized in Chapter III to confirm distributional invariance across airport terminal layouts (D = 0.032, p = 0.28)."
    },

    # L
    {
        "acronym": "LAWA",
        "full_term": "Los Angeles World Airports",
        "category": "Airport Infrastructure & Operations",
        "cat_id": 2,
        "definition": "The proprietary municipal airport authority governing Los Angeles International Airport (LAX) and Van Nuys Airport, providing operational terminal passenger statistics."
    },
    {
        "acronym": "LAX",
        "full_term": "Los Angeles International Airport",
        "category": "Airport Cohort & Airfield Codes",
        "cat_id": 4,
        "definition": "Major West Coast commercial mega-airport (IATA code: LAX). Evaluated in the Top 25 network clustering and 4-tier filtering pipeline as a multi-carrier origin-and-destination complex."
    },
    {
        "acronym": "LGA",
        "full_term": "LaGuardia Airport",
        "category": "Airport Cohort & Airfield Codes",
        "cat_id": 4,
        "definition": "Commercial hub airport in New York (IATA code: LGA). Terminal B/C serves as the zero-shot spatial transfer evaluation airfield (EWR → LGA) for testing model generalizability without retraining in Dimension 3."
    },
    {
        "acronym": "LOS",
        "full_term": "Level of Service",
        "category": "Queuing Theory & Passenger Dynamics",
        "cat_id": 5,
        "definition": "Standardized qualitative metric framework (IATA Airport Development Reference Manual) rating passenger waiting times, terminal crowding, and space availability from LOS A (excellent) to LOS F (system breakdown)."
    },
    {
        "acronym": "LR",
        "full_term": "Linear Regression",
        "category": "Predictive Modeling & Computational Methods",
        "cat_id": 6,
        "definition": "Fundamental statistical modeling approach estimating linear relationships between operational predictors and passenger flow."
    },
    {
        "acronym": "LSTM",
        "full_term": "Long Short-Term Memory",
        "category": "Predictive Modeling & Computational Methods",
        "cat_id": 6,
        "definition": "Advanced recurrent neural network architecture with input, forget, and output gating mechanisms that capture long-term sequential dependencies in time-series data."
    },

    # M
    {
        "acronym": "M/G/c",
        "full_term": "Markovian Arrival / General Service / c-Server Queuing Model",
        "category": "Queuing Theory & Passenger Dynamics",
        "cat_id": 5,
        "definition": "Kendall notation for a queuing system with Poisson arrivals, arbitrary service time distributions, and c parallel screening lanes."
    },
    {
        "acronym": "M/M/1",
        "full_term": "Markovian Arrival / Markovian Service / Single-Server Queuing Model",
        "category": "Queuing Theory & Passenger Dynamics",
        "cat_id": 5,
        "definition": "Classical queuing model with Poisson arrivals and exponential service times operating with a single server; foundational baseline in queuing literature."
    },
    {
        "acronym": "M/M/c",
        "full_term": "Markovian Arrival / Markovian Service / c-Server Queuing Model",
        "category": "Queuing Theory & Passenger Dynamics",
        "cat_id": 5,
        "definition": "Multi-server Erlang delay queuing model assuming Poisson arrivals and memoryless service rates across c parallel screening lanes."
    },
    {
        "acronym": "MAE",
        "full_term": "Mean Absolute Error",
        "category": "Evaluation Metrics & Econometric Statistics",
        "cat_id": 7,
        "definition": "Standard linear loss metric calculating the average magnitude of absolute forecasting errors in original physical units (pax/hr or pax/day): MAE = (1/n) Σ |y_t - ŷ_t|."
    },
    {
        "acronym": "MAPE",
        "full_term": "Mean Absolute Percentage Error",
        "category": "Evaluation Metrics & Econometric Statistics",
        "cat_id": 7,
        "definition": "Relative percentage error metric: MAPE = (100/n) Σ |(y_t - ŷ_t) / y_t|. In the thesis, proven to be mathematically invalid for hourly checkpoint modeling due to overnight structural zeros (y_t ≈ 0 pax/hr) causing division-by-zero explosions."
    },
    {
        "acronym": "MASE",
        "full_term": "Mean Absolute Scaled Error",
        "category": "Evaluation Metrics & Econometric Statistics",
        "cat_id": 7,
        "definition": "Scale-independent forecast accuracy metric (Hyndman & Koehler, 2006) normalizing model MAE against the in-sample mean absolute error of a naive diurnal persistence baseline. Values < 1.000 indicate superiority over persistence."
    },
    {
        "acronym": "MATLAB",
        "full_term": "Matrix Laboratory",
        "category": "Data Systems & Information Architecture",
        "cat_id": 3,
        "definition": "Proprietary numerical computing and simulation environment frequently cited in early airport terminal simulation and queue optimization literature."
    },
    {
        "acronym": "MB",
        "full_term": "Megabyte",
        "category": "Data Systems & Information Architecture",
        "cat_id": 3,
        "definition": "Standard digital storage unit (1,048,576 bytes) used in reporting raw data feed sizes and memory footprints."
    },
    {
        "acronym": "MDI",
        "full_term": "Mean Decrease in Impurity",
        "category": "Predictive Modeling & Computational Methods",
        "cat_id": 6,
        "definition": "Gini or variance-based feature importance metric in tree ensembles measuring the total reduction in criterion impurity contributed by each operational predictor."
    },
    {
        "acronym": "ML",
        "full_term": "Machine Learning",
        "category": "Predictive Modeling & Computational Methods",
        "cat_id": 6,
        "definition": "Automated algorithmic discipline learning predictive patterns from data; instantiated in Model 2 (Supervised Machine Learning Model)."
    },
    {
        "acronym": "MPC",
        "full_term": "Model Predictive Control",
        "category": "Predictive Modeling & Computational Methods",
        "cat_id": 6,
        "definition": "Advanced feedback control methodology optimizing operational control actions (e.g., lane staffing schedules) over a rolling finite time horizon using dynamic system models."
    },
    {
        "acronym": "MSAA",
        "full_term": "Master of Science in Aeronautics",
        "category": "Academic & Publishing Standards",
        "cat_id": 7,
        "definition": "The graduate degree program at Embry-Riddle Aeronautical University under which this thesis (Gleich 700B) was conducted and submitted."
    },
    {
        "acronym": "MSE",
        "full_term": "Mean Squared Error",
        "category": "Evaluation Metrics & Econometric Statistics",
        "cat_id": 7,
        "definition": "Quadratic error loss metric calculating the mean of squared residuals: MSE = (1/n) Σ (y_t - ŷ_t)²."
    },

    # N
    {
        "acronym": "NARX",
        "full_term": "Nonlinear Autoregressive with Exogenous Input",
        "category": "Predictive Modeling & Computational Methods",
        "cat_id": 6,
        "definition": "Dynamic neural network architecture incorporating recurrent autoregressive feedback alongside external driving time-series inputs."
    },
    {
        "acronym": "NAS",
        "full_term": "National Airspace System",
        "category": "Regulatory & Air Traffic Management",
        "cat_id": 2,
        "definition": "The comprehensive common network of United States airspace, air navigation facilities, airports, air traffic control towers, and operational regulations overseen by the FAA."
    },
    {
        "acronym": "NASA",
        "full_term": "National Aeronautics and Space Administration",
        "category": "Aviation Research & Literature",
        "cat_id": 1,
        "definition": "U.S. government agency conducting advanced aerospace research and developing air traffic management decision-support systems."
    },
    {
        "acronym": "NHPP",
        "full_term": "Non-Homogeneous Poisson Process",
        "category": "Queuing Theory & Passenger Dynamics",
        "cat_id": 5,
        "definition": "Stochastic arrival point process where the arrival intensity rate λ(t) varies continuously over time, capturing time-varying passenger arrival intensity across flight banks."
    },

    # O
    {
        "acronym": "O&D",
        "full_term": "Origin and Destination",
        "category": "Federal Aviation Datasets & Schemas",
        "cat_id": 3,
        "definition": "Classification of air passengers denoting true originating trip origin and final destination, distinguishing local originating travelers entering security checkpoints from connecting transfer passengers."
    },
    {
        "acronym": "OAG",
        "full_term": "Official Aviation Guide",
        "category": "Federal Aviation Datasets & Schemas",
        "cat_id": 3,
        "definition": "Commercial global aviation data provider supplying scheduled airline timetables, flight numbers, and aircraft equipment assignments."
    },
    {
        "acronym": "OLS",
        "full_term": "Ordinary Least Squares",
        "category": "Evaluation Metrics & Econometric Statistics",
        "cat_id": 7,
        "definition": "Classical linear regression estimation technique minimizing the sum of squared differences between observed and predicted values."
    },
    {
        "acronym": "ORD",
        "full_term": "Chicago O'Hare International Airport",
        "category": "Airport Cohort & Airfield Codes",
        "cat_id": 4,
        "definition": "Major domestic connecting mega-hub (IATA code: ORD). Evaluated in Top 25 network clustering as a dual-carrier connecting hub (United Terminal 1 / American Terminal 3)."
    },
    {
        "acronym": "OTP",
        "full_term": "On-Time Performance",
        "category": "Federal Aviation Datasets & Schemas",
        "cat_id": 3,
        "definition": "Airline operational reliability database (BTS Form 234) tracking flight departure delays, arrival delays, taxi times, and cancellation dynamics across reporting U.S. carriers."
    },

    # P
    {
        "acronym": "PAR",
        "full_term": "Passenger Arrival Rate",
        "category": "Queuing Theory & Passenger Dynamics",
        "cat_id": 5,
        "definition": "The instantaneous or hourly volume of passengers entering the security checkpoint queuing area per unit time (pax/hr)."
    },
    {
        "acronym": "PHL",
        "full_term": "Philadelphia International Airport",
        "category": "Airport Cohort & Airfield Codes",
        "cat_id": 4,
        "definition": "Commercial airport (IATA code: PHL). Evaluated in the Top 25 clustering and 4-tier filtering pipeline as an American Airlines hub complex."
    },
    {
        "acronym": "PreCheck",
        "full_term": "TSA PreCheck Expedited Screening Program",
        "category": "Airport Infrastructure & Operations",
        "cat_id": 2,
        "definition": "TSA trusted traveler program allowing vetted passengers to utilize dedicated screening lanes with reduced divestiture protocols (shoes, belts, light jackets remain on), resulting in higher service throughput rates."
    },
    {
        "acronym": "PSO",
        "full_term": "Particle Swarm Optimization",
        "category": "Predictive Modeling & Computational Methods",
        "cat_id": 6,
        "definition": "Computational metaheuristic optimization algorithm inspired by biological flocking behaviors, evaluated in terminal literature for hyperparameter tuning."
    },
    {
        "acronym": "PSO-BP",
        "full_term": "Particle Swarm Optimization with Back Propagation",
        "category": "Predictive Modeling & Computational Methods",
        "cat_id": 6,
        "definition": "Hybrid machine learning optimization algorithm combining particle swarm optimization with backpropagation neural networks to optimize network weights."
    },

    # R
    {
        "acronym": "R²",
        "full_term": "Coefficient of Determination (R-Squared)",
        "category": "Evaluation Metrics & Econometric Statistics",
        "cat_id": 7,
        "definition": "Statistical goodness-of-fit metric measuring the proportion of total variance in the dependent target (throughput volatility or volume) explained by the predictive model."
    },
    {
        "acronym": "RF",
        "full_term": "Random Forest",
        "category": "Predictive Modeling & Computational Methods",
        "cat_id": 6,
        "definition": "Ensemble supervised machine learning regressor constructing multiple randomized decision trees to capture non-linear feature interactions."
    },
    {
        "acronym": "R_MASE",
        "full_term": "Disruption Error Multiplier (Resilience Multiplier)",
        "category": "Evaluation Metrics & Econometric Statistics",
        "cat_id": 7,
        "definition": "Core evaluation metric for Dimension 2 (Resilience) defined as the ratio of forecast error under irregular operations to nominal baseline error: R_MASE = MASE_shock / MASE_nominal. Values close to 1.00 denote robust operational recovery."
    },
    {
        "acronym": "RMSE",
        "full_term": "Root Mean Squared Error",
        "category": "Evaluation Metrics & Econometric Statistics",
        "cat_id": 7,
        "definition": "Standard quadratic performance metric calculating the square root of mean squared forecasting errors in original physical units (pax/hr or pax/day): RMSE = √[(1/n) Σ (y_t - ŷ_t)²]."
    },
    {
        "acronym": "RTR",
        "full_term": "Relative Transfer Ratio (Transfer Error Penalty)",
        "category": "Evaluation Metrics & Econometric Statistics",
        "cat_id": 7,
        "definition": "Core evaluation metric for Dimension 3 (Generalizability) quantifying zero-shot spatial transfer degradation: RTR = RMSE_transfer / RMSE_in-sample. Ratios near 1.00 denote portable model logic."
    },

    # S
    {
        "acronym": "SARIMA",
        "full_term": "Seasonal Autoregressive Integrated Moving Average",
        "category": "Predictive Modeling & Computational Methods",
        "cat_id": 6,
        "definition": "Linear time-series model extending ARIMA with seasonal lag polynomials (P, D, Q)_s to capture recurring 24-hour diurnal operational cycles."
    },
    {
        "acronym": "SARIMAX",
        "full_term": "Seasonal Autoregressive Integrated Moving Average with Exogenous Regressors",
        "category": "Predictive Modeling & Computational Methods",
        "cat_id": 6,
        "definition": "SARIMA model augmented with time-varying external covariates (scheduled departures, flight delays, weather indicators)."
    },
    {
        "acronym": "SEA",
        "full_term": "Seattle-Tacoma International Airport",
        "category": "Airport Cohort & Airfield Codes",
        "cat_id": 4,
        "definition": "Pacific Northwest commercial hub (IATA code: SEA) dominated by Alaska Airlines; analyzed in Top 25 network clustering."
    },
    {
        "acronym": "SESAR",
        "full_term": "Single European Sky ATM Research",
        "category": "Regulatory & Air Traffic Management",
        "cat_id": 1,
        "definition": "European operational and technological modernization initiative harmonizing air traffic management systems across European airspace."
    },
    {
        "acronym": "SLAM",
        "full_term": "Simple Landside Aggregate Model",
        "category": "Predictive Modeling & Computational Methods",
        "cat_id": 6,
        "definition": "Operations research macroscopic passenger simulation model (Brunetta et al., 1999) translating airline schedules into aggregate terminal area occupancies."
    },
    {
        "acronym": "SLC",
        "full_term": "Salt Lake City International Airport",
        "category": "Airport Cohort & Airfield Codes",
        "cat_id": 4,
        "definition": "Commercial hub airport (IATA code: SLC). Delta Air Lines consolidated terminal evaluated in 4-tier filtering for single-terminal hub processing."
    },
    {
        "acronym": "SSOT",
        "full_term": "Single Source of Truth",
        "category": "Academic & Publishing Standards",
        "cat_id": 7,
        "definition": "Architectural repository governance principle maintaining authoritative, conformed specification files (e.g., Chapter 1–5 SSOTs) to eliminate version conflict."
    },
    {
        "acronym": "SVM",
        "full_term": "Support Vector Machine",
        "category": "Predictive Modeling & Computational Methods",
        "cat_id": 6,
        "definition": "Supervised learning model using hyperplanes in high-dimensional space for classification or regression, evaluated in airport literature."
    },

    # T
    {
        "acronym": "T-100",
        "full_term": "BTS Form 41 Schedule T-100 Domestic Segment Data",
        "category": "Federal Aviation Datasets & Schemas",
        "cat_id": 3,
        "definition": "Monthly regulatory airline reporting dataset providing non-stop domestic flight segment seat capacities, transported passengers, and aircraft load factors."
    },
    {
        "acronym": "TRACON",
        "full_term": "Terminal Radar Approach Control",
        "category": "Regulatory & Air Traffic Management",
        "cat_id": 2,
        "definition": "FAA air traffic control radar facility managing aircraft arrivals, departures, and sequencing within a 30- to 50-mile radius of high-density metropolitan airports (e.g., New York TRACON for EWR, LGA, JFK)."
    },
    {
        "acronym": "TRB",
        "full_term": "Transportation Research Board",
        "category": "Aviation Research & Literature",
        "cat_id": 1,
        "definition": "Division of the National Academies of Sciences, Engineering, and Medicine that manages national transportation research programs including the Airport Cooperative Research Program (ACRP)."
    },
    {
        "acronym": "TSA",
        "full_term": "Transportation Security Administration",
        "category": "Regulatory & Air Traffic Management",
        "cat_id": 1,
        "definition": "Federal homeland security agency within the Department of Homeland Security responsible for civil aviation security, passenger screening, and checkpoint operations across U.S. commercial airports."
    },
    {
        "acronym": "TSO",
        "full_term": "Transportation Security Officer",
        "category": "Airport Infrastructure & Operations",
        "cat_id": 2,
        "definition": "Frontline federal security personnel employed by the TSA staffing checkpoint screening lanes, operating CAT scanners, body scanners (AIT), and baggage inspection systems."
    },
    {
        "acronym": "TTR",
        "full_term": "Time-to-Recovery",
        "category": "Evaluation Metrics & Econometric Statistics",
        "cat_id": 7,
        "definition": "Resilience evaluation metric quantifying the operational elapsed time (in hours) required for forecast residuals to return to nominal baseline accuracy bounds following an IROPS disruption shock."
    },

    # U
    {
        "acronym": "UA",
        "full_term": "United Airlines",
        "category": "Commercial Air Carriers",
        "cat_id": 4,
        "definition": "Major U.S. network legacy carrier (IATA code: UA). Operates dedicated hub terminal complexes analyzed at Newark (EWR Terminal C), Chicago (ORD Terminal 1), and Houston (IAH Terminal C)."
    },
    {
        "acronym": "ULCC",
        "full_term": "Ultra-Low-Cost Carrier",
        "category": "Commercial Air Carriers",
        "cat_id": 4,
        "definition": "Airline operating point-to-point routes with unbundled fares and aggressive ancillaries (e.g., Spirit, Frontier, Allegiant); characterized by unique passenger check-in arrival curves and bag divestiture patterns."
    },
    {
        "acronym": "USDOT",
        "full_term": "United States Department of Transportation",
        "category": "Regulatory & Air Traffic Management",
        "cat_id": 1,
        "definition": "Cabinet-level federal department responsible for national transportation policy, funding, and administrative oversight of the FAA and BTS."
    },

    # V
    {
        "acronym": "VIF",
        "full_term": "Variance Inflation Factor",
        "category": "Evaluation Metrics & Econometric Statistics",
        "cat_id": 7,
        "definition": "Multicollinearity diagnostic measuring the inflation of regression coefficient variance due to collinearity among predictors; used in Chapter III to assess flight schedule collinearity."
    },
    {
        "acronym": "VM",
        "full_term": "Virtual Machine",
        "category": "Data Systems & Information Architecture",
        "cat_id": 3,
        "definition": "Virtualized computing environment used in research data pipeline execution and reproducible analytics."
    },

    # W
    {
        "acronym": "WN",
        "full_term": "Southwest Airlines",
        "category": "Commercial Air Carriers",
        "cat_id": 4,
        "definition": "Major domestic air carrier (IATA code: WN). In the thesis, Southwest is excluded from the primary experimental cohort during 4-tier filtering because its point-to-point network, multi-carrier terminal sharing, and lack of assigned seat banks confound carrier-exclusive checkpoint isolation."
    },
    {
        "acronym": "WSC",
        "full_term": "Winter Simulation Conference",
        "category": "Academic & Publishing Standards",
        "cat_id": 7,
        "definition": "Premier international conference on discrete-event and continuous computer simulation, cited in airport queuing simulation literature."
    },

    # X
    {
        "acronym": "XAI",
        "full_term": "Explainable Artificial Intelligence",
        "category": "Predictive Modeling & Computational Methods",
        "cat_id": 6,
        "definition": "Methodological frameworks (e.g., SHAP, permutation feature importance) that render complex machine learning decisions interpretable to airport operations directors."
    }
]

# Operational Categories Definition
CATEGORIES = [
    {
        "id": 1,
        "title": "Category 1: Federal Aviation Agencies, Regulatory Bodies, and Research Organizations",
        "short_title": "Agencies, Regulators & Research",
        "description": "This category covers the federal government departments, regulatory authorities, international standards organizations, and national transportation research boards that govern civil aviation safety, airspace management, and transportation research across the National Airspace System."
    },
    {
        "id": 2,
        "title": "Category 2: Airport Infrastructure, Air Traffic Control, and Terminal Security Operations",
        "short_title": "Infrastructure, ATC & Security Operations",
        "description": "This category defines the physical airport terminal zones, centralized command centers, air traffic radar facilities, passenger identity hardware, and security screening personnel that manage terminal passenger flow and airspace sequencing."
    },
    {
        "id": 3,
        "title": "Category 3: Federal Aviation Datasets, Data Hygiene, and Information Architecture",
        "short_title": "Federal Datasets & Data Architecture",
        "description": "This category details the official federal regulatory data feeds, ticket survey archives, flight segment schedules, pipeline architectures, and relational warehouse schemas synthesized over the 2019–2025 study baseline."
    },
    {
        "id": 4,
        "title": "Category 4: Study Airport Cohort and Commercial Air Carrier Codes",
        "short_title": "Airport Cohort & Carrier Codes",
        "description": "This category lists the official IATA/FAA three-letter airport codes evaluated across the Top 25 network clustering census and the balanced 9-airport experimental cohort, along with two-letter air carrier codes and operational business models."
    },
    {
        "id": 5,
        "title": "Category 5: Terminal Queuing Dynamics, Passenger Flow, and Arrival Processes",
        "short_title": "Queuing Dynamics & Passenger Flow",
        "description": "This category encompasses the formal queuing theory models, stochastic point processes, Kendall queue classifications, service level ratings, and empirical show-up curves governing traveler arrival burstiness and checkpoint bottlenecks."
    },
    {
        "id": 6,
        "title": "Category 6: Predictive Modeling Architectures, Machine Learning, and Time-Series Methods",
        "short_title": "Predictive Modeling & Machine Learning",
        "description": "This category covers the mathematical forecasting paradigms, econometric time-series models, decision-tree ensembles, deep recurrent neural networks, and feedback control architectures benchmarked in the predictive modeling suite."
    },
    {
        "id": 7,
        "title": "Category 7: Predictive Evaluation Metrics, Econometric Statistics, and Operational Regimes",
        "short_title": "Evaluation Metrics & Econometric Statistics",
        "description": "This category defines the formal statistical error loss functions, scale-free volatility indices, asymptotic econometric tests, temporal operational regimes, and multi-dimensional evaluation pillars (Robustness, Resilience, Generalizability)."
    }
]

def sort_key(item):
    # alphanumeric clean sort
    acr = item["acronym"]
    clean = acr.replace("²", "2").replace("_", "").replace("-", "").replace("/", "").replace("&", "")
    return clean.upper()

ACRONYM_DATA.sort(key=sort_key)

def set_cell_margins(cell, top=100, bottom=100, left=140, right=140):
    """Set cell padding in dxa (1 pt = 20 dxa)."""
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = OxmlElement('w:tcMar')
    for m, val in [('w:top', top), ('w:bottom', bottom), ('w:left', left), ('w:right', right)]:
        node = OxmlElement(m)
        node.set(qn('w:w'), str(val))
        node.set(qn('w:type'), 'dxa')
        tcMar.append(node)
    tcPr.append(tcMar)

def apply_apa_table_borders(table, header_rows=1):
    """Apply strict APA 7th Edition table borders:
       - Top border of table (0.75 pt solid black)
       - Bottom border of header row (0.75 pt solid black)
       - Bottom border of last row (0.75 pt solid black)
       - Zero vertical rules, zero internal horizontal rules.
    """
    tblPr = table._tbl.tblPr
    tblBorders = OxmlElement('w:tblBorders')
    
    # Top border of entire table
    top = OxmlElement('w:top')
    top.set(qn('w:val'), 'single')
    top.set(qn('w:sz'), '6') # 0.75 pt
    top.set(qn('w:space'), '0')
    top.set(qn('w:color'), '000000')
    tblBorders.append(top)
    
    # Bottom border of entire table
    bottom = OxmlElement('w:bottom')
    bottom.set(qn('w:val'), 'single')
    bottom.set(qn('w:sz'), '6')
    bottom.set(qn('w:space'), '0')
    bottom.set(qn('w:color'), '000000')
    tblBorders.append(bottom)
    
    # Left, right, insideV = none
    for edge in ('left', 'right', 'insideV', 'insideH'):
        el = OxmlElement(f'w:{edge}')
        el.set(qn('w:val'), 'none')
        tblBorders.append(el)
        
    tblPr.append(tblBorders)
    
    # Apply bottom border to header row cells
    for r_idx in range(header_rows):
        header_row = table.rows[r_idx]
        for cell in header_row.cells:
            tcPr = cell._tc.get_or_add_tcPr()
            tcBorders = tcPr.first_child_found_in('w:tcBorders')
            if tcBorders is None:
                tcBorders = OxmlElement('w:tcBorders')
                tcPr.append(tcBorders)
            b_bottom = OxmlElement('w:bottom')
            b_bottom.set(qn('w:val'), 'single')
            b_bottom.set(qn('w:sz'), '6') # 0.75 pt
            b_bottom.set(qn('w:space'), '0')
            b_bottom.set(qn('w:color'), '000000')
            tcBorders.append(b_bottom)

def build_word_document(output_path):
    doc = docx.Document()
    
    # Configure 1.0-inch margins on all sides (APA 7th Edition)
    section = doc.sections[0]
    section.top_margin = Inches(1.0)
    section.bottom_margin = Inches(1.0)
    section.left_margin = Inches(1.0)
    section.right_margin = Inches(1.0)
    section.page_width = Inches(8.5)
    section.page_height = Inches(11.0)
    
    # Default Normal style font
    normal_style = doc.styles['Normal']
    normal_style.font.name = 'Times New Roman'
    normal_style.font.size = Pt(12)
    normal_style.font.color.rgb = RGBColor(0, 0, 0)
    
    # -------------------------------------------------------------
    # Title / Preliminary Header Block
    # -------------------------------------------------------------
    p_inst = doc.add_paragraph()
    p_inst.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_inst.paragraph_format.space_before = Pt(0)
    p_inst.paragraph_format.space_after = Pt(2)
    r_inst = p_inst.add_run("EMBRY-RIDDLE AERONAUTICAL UNIVERSITY")
    r_inst.font.name = "Times New Roman"
    r_inst.font.size = Pt(11)
    r_inst.font.bold = True
    
    p_prog = doc.add_paragraph()
    p_prog.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_prog.paragraph_format.space_before = Pt(0)
    p_prog.paragraph_format.space_after = Pt(2)
    r_prog = p_prog.add_run("College of Aeronautics | Department of Graduate Studies")
    r_prog.font.name = "Times New Roman"
    r_prog.font.size = Pt(10)
    r_prog.font.italic = True
    
    p_sub = doc.add_paragraph()
    p_sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_sub.paragraph_format.space_before = Pt(0)
    p_sub.paragraph_format.space_after = Pt(14)
    r_sub = p_sub.add_run("Master of Science in Aeronautics / Graduate Capstone Project (MSAA 700B)")
    r_sub.font.name = "Times New Roman"
    r_sub.font.size = Pt(10)
    r_sub.font.italic = True
    
    # Main Document Heading
    p_title = doc.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_title.paragraph_format.space_before = Pt(6)
    p_title.paragraph_format.space_after = Pt(4)
    r_title = p_title.add_run("LIST OF ACRONYMS AND ABBREVIATIONS")
    r_title.font.name = "Times New Roman"
    r_title.font.size = Pt(14)
    r_title.font.bold = True
    
    p_thesis_title = doc.add_paragraph()
    p_thesis_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_thesis_title.paragraph_format.space_before = Pt(0)
    p_thesis_title.paragraph_format.space_after = Pt(4)
    r_thesis = p_thesis_title.add_run("Evaluating Predictive Techniques to Model Stochastic Airport Passenger Flow")
    r_thesis.font.name = "Times New Roman"
    r_thesis.font.size = Pt(11)
    r_thesis.font.bold = True
    
    p_author = doc.add_paragraph()
    p_author.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_author.paragraph_format.space_before = Pt(0)
    p_author.paragraph_format.space_after = Pt(18)
    r_author = p_author.add_run("Author: Leila Gleich | Degree Candidate: Master of Science in Aeronautics")
    r_author.font.name = "Times New Roman"
    r_author.font.size = Pt(10.5)
    r_author.font.italic = True
    
    # -------------------------------------------------------------
    # Executive Scope & Purpose Section
    # -------------------------------------------------------------
    p_h1 = doc.add_paragraph()
    p_h1.paragraph_format.space_before = Pt(12)
    p_h1.paragraph_format.space_after = Pt(6)
    r_h1 = p_h1.add_run("Operational Scope and Purpose")
    r_h1.font.name = "Times New Roman"
    r_h1.font.size = Pt(12)
    r_h1.font.bold = True
    
    p_intro1 = doc.add_paragraph()
    p_intro1.paragraph_format.space_before = Pt(0)
    p_intro1.paragraph_format.space_after = Pt(6)
    p_intro1.paragraph_format.line_spacing = 1.15
    p_intro1.add_run(
        "This document compiles and defines the comprehensive inventory of technical acronyms, federal agency "
        "abbreviations, aviation data schemas, airport and carrier codes, queuing theory notations, machine learning "
        "architectures, and econometric evaluation metrics used across Chapters I through V of this thesis. "
        "In commercial aviation and airport security operations, interdisciplinary communication bridges federal regulatory bodies "
        "(FAA, TSA), statistical data providers (BTS), airline operators, and terminal security planners. To eliminate "
        "ambiguity and support dissertation committee review in accordance with the Publication Manual of the American "
        "Psychological Association (7th ed.; APA, 2020), this document provides a dual-presentation architecture:"
    )
    
    # Bullet points explaining the two parts
    bullets = [
        ("Part I: Master Alphabetical Index (Table 1)", 
         "A unified, quick-reference master table listing all 100+ acronyms in strict alphabetical order, specifying each term's formal expansion, operational domain classification, and primary function in the thesis methodology."),
        ("Part II: Categorized Operational Descriptions", 
         "In-depth narrative profiles organized into seven operational categories matching the functional workflow of airport terminal analytics: (1) Federal Agencies & Regulators; (2) Airport Infrastructure & Terminal Security; (3) Federal Datasets & Data Architecture; (4) Airport Cohort & Carrier Codes; (5) Queuing Dynamics & Passenger Flow; (6) Predictive Modeling & Machine Learning; and (7) Evaluation Metrics & Econometric Statistics.")
    ]
    for b_title, b_desc in bullets:
        p_b = doc.add_paragraph(style='List Bullet')
        p_b.paragraph_format.space_before = Pt(0)
        p_b.paragraph_format.space_after = Pt(3)
        p_b.paragraph_format.line_spacing = 1.15
        r_bt = p_b.add_run(f"{b_title}: ")
        r_bt.font.name = "Times New Roman"
        r_bt.font.bold = True
        r_bd = p_b.add_run(b_desc)
        r_bd.font.name = "Times New Roman"
        
    p_intro2 = doc.add_paragraph()
    p_intro2.paragraph_format.space_before = Pt(6)
    p_intro2.paragraph_format.space_after = Pt(14)
    p_intro2.paragraph_format.line_spacing = 1.15
    p_intro2.add_run(
        "A foundational methodological principle of this research is that airport terminal queue stability and passenger delay risks "
        "are governed not merely by static passenger volumes, but by the volatility of checkpoint throughput (within-day "
        "standard deviation σ_TSA,hr, scale-free Coefficient of Variation CV_TSA, and multi-day temporal dispersion σ_TSA,7d). "
        "Under Kingman's heavy-traffic queuing formula (W_q ≈ [ρ / (1 - ρ)] [(C_a² + C_s²) / 2] [1 / μ]), expected waiting times "
        "scale quadratically with arrival volatility (C_a²) as checkpoint lane utilization approaches capacity (ρ → 1.0). "
        "Accordingly, all operational terms, model formulations, and evaluation metrics defined herein are grounded in "
        "authentic commercial aviation operations, airline flight scheduling cycles, and airport passenger flow dynamics."
    )
    
    # -------------------------------------------------------------
    # Part I: Master Alphabetical Table (APA 7th Format)
    # -------------------------------------------------------------
    p_part1 = doc.add_paragraph()
    p_part1.paragraph_format.space_before = Pt(14)
    p_part1.paragraph_format.space_after = Pt(4)
    r_part1 = p_part1.add_run("Part I: Master Alphabetical Index")
    r_part1.font.name = "Times New Roman"
    r_part1.font.size = Pt(12)
    r_part1.font.bold = True
    
    # Table Label (Line 1: Table 1, Bold)
    p_t1_lbl = doc.add_paragraph()
    p_t1_lbl.paragraph_format.space_before = Pt(6)
    p_t1_lbl.paragraph_format.space_after = Pt(0)
    r_t1_lbl = p_t1_lbl.add_run("Table 1")
    r_t1_lbl.font.name = "Times New Roman"
    r_t1_lbl.font.size = Pt(11)
    r_t1_lbl.font.bold = True
    
    # Table Title (Line 2: Italic)
    p_t1_tit = doc.add_paragraph()
    p_t1_tit.paragraph_format.space_before = Pt(0)
    p_t1_tit.paragraph_format.space_after = Pt(6)
    r_t1_tit = p_t1_tit.add_run("Master Index of Acronyms, Operational Expansions, and Thesis Applications")
    r_t1_tit.font.name = "Times New Roman"
    r_t1_tit.font.size = Pt(11)
    r_t1_tit.font.italic = True
    
    # Create Table: 4 columns
    # Printable width: 6.5 in. Col 0: 1.1 in, Col 1: 2.0 in, Col 2: 1.3 in, Col 3: 2.1 in
    table = doc.add_table(rows=len(ACRONYM_DATA) + 1, cols=4)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    col_widths = [Inches(1.1), Inches(2.0), Inches(1.3), Inches(2.1)]
    
    # Table Header Row
    headers = [
        "Acronym / Abbreviation",
        "Full Expansion / Stand-For Term",
        "Operational Category",
        "Primary Thesis Application"
    ]
    hdr_row = table.rows[0]
    trPr = hdr_row._tr.get_or_add_trPr()
    trPr.append(OxmlElement('w:tblHeader'))
    trPr.append(OxmlElement('w:cantSplit'))
    
    for c_idx, cell in enumerate(hdr_row.cells):
        cell.width = col_widths[c_idx]
        set_cell_margins(cell, top=100, bottom=100, left=120, right=120)
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.LEFT
        p.paragraph_format.space_before = Pt(2)
        p.paragraph_format.space_after = Pt(2)
        p.paragraph_format.line_spacing = 1.05
        run = p.add_run(headers[c_idx])
        run.font.name = "Times New Roman"
        run.font.size = Pt(10)
        run.font.bold = True
        
    # Populate Table Rows
    for r_idx, item in enumerate(ACRONYM_DATA):
        row = table.rows[r_idx + 1]
        # cantSplit on every row
        r_trPr = row._tr.get_or_add_trPr()
        r_trPr.append(OxmlElement('w:cantSplit'))
        
        # Col 0: Acronym
        cell_0 = row.cells[0]
        cell_0.width = col_widths[0]
        set_cell_margins(cell_0, top=70, bottom=70, left=120, right=120)
        p0 = cell_0.paragraphs[0]
        p0.paragraph_format.space_before = Pt(1)
        p0.paragraph_format.space_after = Pt(1)
        p0.paragraph_format.line_spacing = 1.05
        run0 = p0.add_run(item["acronym"])
        run0.font.name = "Times New Roman"
        run0.font.size = Pt(9.5)
        run0.font.bold = True
        
        # Col 1: Full Term
        cell_1 = row.cells[1]
        cell_1.width = col_widths[1]
        set_cell_margins(cell_1, top=70, bottom=70, left=120, right=120)
        p1 = cell_1.paragraphs[0]
        p1.paragraph_format.space_before = Pt(1)
        p1.paragraph_format.space_after = Pt(1)
        p1.paragraph_format.line_spacing = 1.05
        run1 = p1.add_run(item["full_term"])
        run1.font.name = "Times New Roman"
        run1.font.size = Pt(9.5)
        
        # Col 2: Category
        cell_2 = row.cells[2]
        cell_2.width = col_widths[2]
        set_cell_margins(cell_2, top=70, bottom=70, left=120, right=120)
        p2 = cell_2.paragraphs[0]
        p2.paragraph_format.space_before = Pt(1)
        p2.paragraph_format.space_after = Pt(1)
        p2.paragraph_format.line_spacing = 1.05
        run2 = p2.add_run(item["category"])
        run2.font.name = "Times New Roman"
        run2.font.size = Pt(9.0)
        
        # Col 3: Primary Thesis Application
        cell_3 = row.cells[3]
        cell_3.width = col_widths[3]
        set_cell_margins(cell_3, top=70, bottom=70, left=120, right=120)
        p3 = cell_3.paragraphs[0]
        p3.paragraph_format.space_before = Pt(1)
        p3.paragraph_format.space_after = Pt(1)
        p3.paragraph_format.line_spacing = 1.05
        run3 = p3.add_run(item["definition"])
        run3.font.name = "Times New Roman"
        run3.font.size = Pt(9.0)
        
    apply_apa_table_borders(table, header_rows=1)
    
    # Table Note (APA 7th Format)
    p_note = doc.add_paragraph()
    p_note.paragraph_format.space_before = Pt(4)
    p_note.paragraph_format.space_after = Pt(18)
    p_note.paragraph_format.line_spacing = 1.15
    r_n1 = p_note.add_run("Note. ")
    r_n1.font.name = "Times New Roman"
    r_n1.font.size = Pt(9.5)
    r_n1.font.italic = True
    r_n2 = p_note.add_run(
        "All terms and acronyms are grounded in authentic aviation operations, queuing theory, and empirical econometric "
        "modeling across Chapters I through V of this thesis. Primary evaluation models include Baseline Control (Diurnal Persistence), "
        "Model 1 (Deterministic Flight Schedule Model), Model 2 (Supervised Machine Learning Model), and Model 3 (Dynamic Two-Stage "
        "Hybrid Model). Internal variable tags (M0, M1*, M3, M5) are excluded in compliance with repository governance rules."
    )
    r_n2.font.name = "Times New Roman"
    r_n2.font.size = Pt(9.5)
    
    # -------------------------------------------------------------
    # Part II: Categorized Operational Descriptions
    # -------------------------------------------------------------
    p_part2 = doc.add_paragraph()
    p_part2.paragraph_format.space_before = Pt(16)
    p_part2.paragraph_format.space_after = Pt(6)
    r_part2 = p_part2.add_run("Part II: Categorized Operational Descriptions")
    r_part2.font.name = "Times New Roman"
    r_part2.font.size = Pt(12)
    r_part2.font.bold = True
    
    p_part2_intro = doc.add_paragraph()
    p_part2_intro.paragraph_format.space_before = Pt(0)
    p_part2_intro.paragraph_format.space_after = Pt(12)
    p_part2_intro.paragraph_format.line_spacing = 1.15
    p_part2_intro.add_run(
        "To provide deeper contextual understanding for airport Federal Security Directors (FSDs), operational planners, "
        "and graduate committee reviewers, this section organizes all technical abbreviations into seven operational domains. "
        "Each entry details the concept's exact expansion, its operational significance in terminal checkpoint management, "
        "and its specific analytical deployment in this study."
    )
    
    for cat in CATEGORIES:
        # Category Heading (Level 2 Heading)
        p_cat_h = doc.add_paragraph()
        p_cat_h.paragraph_format.space_before = Pt(14)
        p_cat_h.paragraph_format.space_after = Pt(4)
        r_cat_h = p_cat_h.add_run(cat["title"])
        r_cat_h.font.name = "Times New Roman"
        r_cat_h.font.size = Pt(11.5)
        r_cat_h.font.bold = True
        
        # Category Scope Description
        p_cat_desc = doc.add_paragraph()
        p_cat_desc.paragraph_format.space_before = Pt(0)
        p_cat_desc.paragraph_format.space_after = Pt(8)
        p_cat_desc.paragraph_format.line_spacing = 1.15
        r_cat_desc = p_cat_desc.add_run(cat["description"])
        r_cat_desc.font.name = "Times New Roman"
        r_cat_desc.font.size = Pt(10)
        r_cat_desc.font.italic = True
        
        # Filter items in this category
        cat_items = [it for it in ACRONYM_DATA if it["cat_id"] == cat["id"]]
        cat_items.sort(key=sort_key)
        
        for it in cat_items:
            # Term Heading / Run
            p_entry = doc.add_paragraph()
            p_entry.paragraph_format.space_before = Pt(3)
            p_entry.paragraph_format.space_after = Pt(4)
            p_entry.paragraph_format.line_spacing = 1.15
            
            # Acronym in Bold
            r_entry_acr = p_entry.add_run(f"{it['acronym']} – {it['full_term']}: ")
            r_entry_acr.font.name = "Times New Roman"
            r_entry_acr.font.size = Pt(10.5)
            r_entry_acr.font.bold = True
            
            # Definition text
            r_entry_def = p_entry.add_run(it["definition"])
            r_entry_def.font.name = "Times New Roman"
            r_entry_def.font.size = Pt(10.5)
            
    # Save Word document
    doc.save(output_path)
    print(f"Successfully generated Word document: {output_path}")

def build_markdown_document(output_path):
    lines = []
    lines.append("# List of Acronyms and Abbreviations")
    lines.append("")
    lines.append("> **Thesis Title**: *Evaluating Predictive Techniques to Model Stochastic Airport Passenger Flow*  ")
    lines.append("> **Author**: Leila Gleich | **Degree**: Master of Science in Aeronautics (MSAA / Gleich 700B)  ")
    lines.append("> **Institution**: Embry-Riddle Aeronautical University, College of Aeronautics  ")
    lines.append("> **Standards Compliance**: APA 7th Edition, Strict Aviation Terminology, Throughput Volatility Focus")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## Operational Scope and Purpose")
    lines.append("")
    lines.append("This document compiles and defines the comprehensive inventory of technical acronyms, federal agency "
                 "abbreviations, aviation data schemas, airport and carrier codes, queuing theory notations, machine learning "
                 "architectures, and econometric evaluation metrics used across Chapters I through V of this manuscript. "
                 "In commercial aviation and airport security operations, interdisciplinary communication bridges federal regulatory bodies "
                 "(FAA, TSA), statistical data providers (BTS), airline operators, and terminal security planners. To eliminate "
                 "ambiguity and support dissertation committee review in accordance with the *Publication Manual of the American "
                 "Psychological Association* (7th ed.; APA, 2020), this document provides a dual-presentation architecture:")
    lines.append("")
    lines.append("1. **Part I: Master Alphabetical Index (Table 1)**: A unified, quick-reference master table listing all 100+ acronyms in strict alphabetical order, specifying each term's formal expansion, operational domain classification, and primary function in the thesis methodology.")
    lines.append("2. **Part II: Categorized Operational Descriptions**: In-depth narrative profiles organized into seven operational categories matching the functional workflow of airport terminal analytics.")
    lines.append("")
    lines.append("A foundational methodological principle of this research is that airport terminal queue stability and passenger delay risks "
                 "are governed not merely by static passenger volumes, but by the **volatility of checkpoint throughput** (within-day "
                 "standard deviation $\\sigma_{\\text{TSA, hr}}$, scale-free Coefficient of Variation $CV_{\\text{TSA}}$, and multi-day temporal dispersion $\\sigma_{\\text{TSA, 7d}}$). "
                 "Under Kingman's heavy-traffic queuing formula ($W_q \\approx \\frac{\\rho}{1-\\rho} \\frac{C_a^2 + C_s^2}{2} \\frac{1}{\\mu}$), expected waiting times "
                 "scale quadratically with arrival volatility ($C_a^2$) as checkpoint lane utilization approaches capacity ($\\rho \\to 1.0$). "
                 "Accordingly, all operational terms, model formulations, and evaluation metrics defined herein are grounded in "
                 "authentic commercial aviation operations, airline flight scheduling cycles, and airport passenger flow dynamics.")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## Part I: Master Alphabetical Index")
    lines.append("")
    lines.append("Table 1  ")
    lines.append("*Master Index of Acronyms, Operational Expansions, and Thesis Applications*")
    lines.append("")
    lines.append("| Acronym / Abbreviation | Full Expansion / Stand-For Term | Operational Category | Primary Thesis Application |")
    lines.append("| :--- | :--- | :--- | :--- |")
    
    for it in ACRONYM_DATA:
        acr = it["acronym"].replace("|", "\\|")
        term = it["full_term"].replace("|", "\\|")
        cat = it["category"].replace("|", "\\|")
        defn = it["definition"].replace("|", "\\|")
        lines.append(f"| **{acr}** | {term} | {cat} | {defn} |")
        
    lines.append("")
    lines.append("*Note.* All terms and acronyms are grounded in authentic aviation operations, queuing theory, and empirical econometric "
                 "modeling across Chapters I through V of this thesis. Primary evaluation models include Baseline Control (Diurnal Persistence), "
                 "Model 1 (Deterministic Flight Schedule Model), Model 2 (Supervised Machine Learning Model), and Model 3 (Dynamic Two-Stage "
                 "Hybrid Model). Internal variable tags ($M_0, M_1^*, M_3, M_5$) are excluded in compliance with repository governance rules.")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## Part II: Categorized Operational Descriptions")
    lines.append("")
    lines.append("To provide deeper contextual understanding for airport Federal Security Directors (FSDs), operational planners, "
                 "and graduate committee reviewers, this section organizes all technical abbreviations into seven operational domains.")
    lines.append("")
    
    for cat in CATEGORIES:
        lines.append(f"### {cat['title']}")
        lines.append("")
        lines.append(f"*{cat['description']}*")
        lines.append("")
        cat_items = [it for it in ACRONYM_DATA if it["cat_id"] == cat["id"]]
        cat_items.sort(key=sort_key)
        
        for it in cat_items:
            lines.append(f"#### {it['acronym']} – {it['full_term']}")
            lines.append(f"{it['definition']}")
            lines.append("")
            
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(f"Successfully generated Markdown document: {output_path}")

def main():
    docx_path = "thesis_docs/manuscripts/List_of_Acronyms_and_Abbreviations.docx"
    docx_v1_path = "thesis_docs/manuscripts/Acronyms v1.docx"
    md_path = "thesis_docs/manuscripts/acronyms.md"
    md_only_path = "thesis_docs/manuscripts/manuscripts-only/acronyms.md"
    
    build_word_document(docx_path)
    build_word_document(docx_v1_path)
    build_markdown_document(md_path)
    build_markdown_document(md_only_path)
    
if __name__ == "__main__":
    main()
