import re

def main():
    with open("thesis_docs/manuscripts/glossary.md", "r") as f:
        text = f.read()

    parts = re.split(r"\n(?=### )", text)
    raw_entries = parts[1:]
    table_split = re.split(r"\n(?=## Thematic Cross-Reference Matrix)", raw_entries[-1])
    raw_entries[-1] = table_split[0]

    entry_dict = {}
    for e in raw_entries:
        m = re.match(r"### (.*?)\n", e)
        if m:
            entry_dict[m.group(1).strip()] = e.strip()

    cat_definitions = [
        {
            "id": "cat1",
            "title": "Category 1: Aviation Infrastructure, Federal Agencies, and Programs",
            "short": "Infrastructure, Agencies & Programs",
            "desc": "This category defines the physical airport terminal zones, federal regulatory bodies, operational coordination command centers, and traveler security programs that govern commercial aviation across the National Airspace System.",
            "terms": [
                "Air Traffic Control (ATC)",
                "Airport Operations Center (AOC)",
                "Airside",
                "Credential Authentication Technology (CAT)",
                "Federal Aviation Administration (FAA)",
                "Federal Security Director (FSD)",
                "Freedom of Information Act (FOIA)",
                "Ground Delay Program (GDP)",
                "Landside",
                "National Airspace System (NAS)",
                "Terminal Radar Approach Control (TRACON)",
                "Transportation Security Administration (TSA)",
                "Transportation Security Officer (TSO)",
                "TSA PreCheck",
                "Ultra-Low-Cost Carrier (ULCC)"
            ]
        },
        {
            "id": "cat2",
            "title": "Category 2: Federal Aviation Datasets, Data Hygiene, and Conformance",
            "short": "Datasets & Data Hygiene",
            "desc": "This category covers the official federal aviation data sources, data hygiene protocols, timeline integrity standards, and relational warehouse conformance rules used across the multi-source 2019–2025 study baseline.",
            "terms": [
                "Advance Flight Cancellation",
                "Airborne Flight Duration",
                "Available Seats per Route-Month",
                "Bureau of Transportation Statistics (BTS)",
                "BTS DB1B / DB1C Origin-Destination Ticket Surveys",
                "BTS Form 41 Schedule T-100 Domestic Segment Data",
                "BTS Form 234 (On-Time Performance / OTP)",
                "Candidate B Demarcation",
                "Checkpoint Fingerprinting Algorithm",
                "Flight Departure Delay ($\\text{DepDelay}$)",
                "Lookahead Bias",
                "Operational Separation Buffer",
                "Overnight Structural Zero",
                "Runway Taxi-Out Queue Time",
                "Tactical Flight Cancellation"
            ]
        },
        {
            "id": "cat3",
            "title": "Category 3: Terminal Queuing Dynamics and Passenger Arrival Behavior",
            "short": "Queuing & Passenger Dynamics",
            "desc": "This category details the physical, temporal, and behavioral dynamics of passenger movement through airport terminals, including passenger arrival show-up curves, airline flight bank waves, connecting passenger transfers, and queuing bottlenecks.",
            "terms": [
                "Airport Cooperative Research Program (ACRP) Report 40",
                "Batch Arrival Dynamics",
                "Bimodal Arrival Mixture",
                "Checkpoint Lane Throughput ($y_{k,l,t}$)",
                "Connecting Passenger Deflator",
                "Connecting Passenger Ratio",
                "Convolved Passenger Show-Up Curve",
                "Dedicated Terminal Screening Complex",
                "Divestiture",
                "Empty Checkpoint Fallacy",
                "Flight Bank (Departure Wave)",
                "Hub Disconnect",
                "Hub-and-Spoke Network",
                "Lead-Lag Asynchrony",
                "Level of Service (LOS)",
                "Multi-Carrier Schedule Collinearity",
                "Origin and Destination (O&D)",
                "Originating Passenger (Local Originating Demand)",
                "Queuing Theory",
                "Show-Up Curve",
                "Traffic Intensity ($\\rho(t)$)"
            ]
        },
        {
            "id": "cat4",
            "title": "Category 4: Operational Volatility, Seasonality, and Experimental Filtering",
            "short": "Volatility & Filtering",
            "desc": "This category encompasses the mathematical indices, cyclical volatility metrics, and purposive sampling funnels used to quantify airport operational turbulence and isolate unconfounded research cohorts.",
            "terms": [
                "84-Cell Operational Condition Matrix ($\\mathcal{G} = \\mathcal{S} \\times \\mathcal{D} \\times \\mathcal{H}$)",
                "Coefficient of Variation ($CV_{\\text{TSA}}$)",
                "Coupled Volatility Index ($\\text{CVI}_d$)",
                "Diurnal Non-Consecutive Dual Turbulence Peaks",
                "Flight Departure Delay Dispersion ($\\sigma_{\\text{Delay}, d}$)",
                "Load Factor",
                "Nine-Airport Balanced Experimental Cohort",
                "Operational Turbulence Shock Index ($T_{dow}(h)$)",
                "Peak Surge Shock Ratio ($S_{\\text{TSA}, d}$)",
                "Purposive Four-Tiered Filtering Funnel"
            ]
        },
        {
            "id": "cat5",
            "title": "Category 5: Predictive Modeling Paradigms and Architectures",
            "short": "Predictive Modeling",
            "desc": "This category covers the benchmark forecasting models, decision-tree machine learning algorithms, time-series baselines, and real-time state-space tracking methods evaluated across Chapters III, IV, and V.",
            "terms": [
                "Autoregressive Integrated Moving Average (ARIMA / SARIMA / SARIMAX)",
                "Discrete Event Simulation (DES)",
                "Gated Recurrent Unit (GRU)",
                "Gradient-Boosted Decision Trees (GBM / HistGBM)",
                "Kalman Filtering / State-Space Innovation Feedback",
                "Long Short-Term Memory (LSTM)",
                "Model $M_0$ (Diurnal Seasonal Naive Benchmark)",
                "Model $M_1$ (Unshifted Same-Hour Schedule Baseline)",
                "Model $M_1^*$ (Deterministic 2-Hour Static Lead Baseline)",
                "Model $M_2$ (Empirical Show-Up Curve Model)",
                "Model $M_3$ (Stochastic Operational Tree Regressor)",
                "Model $M_4$ (Full Tri-Modal Pipeline Regressor)",
                "Model $M_5$ (Sequential Two-Stage Hybrid Model)",
                "Non-Homogeneous Poisson Process (NHPP)",
                "Regime-Switched Gated Inference Engine",
                "Tweedie Compound Poisson Distribution"
            ]
        },
        {
            "id": "cat6",
            "title": "Category 6: Operational Evaluation Dimensions, Forecast Metrics, and Statistical Tests",
            "short": "Evaluation & Statistics",
            "desc": "This category defines the multi-dimensional evaluation criteria (robustness, resilience, and generalizability), quantitative accuracy metrics, and formal hypothesis tests used to assess model performance.",
            "terms": [
                "Coefficient of Determination ($R^2$)",
                "Conformal Quantile Prediction Bounds",
                "Cumulative Sum (CUSUM) Structural Break Test",
                "Diebold-Mariano ($DM$) Test",
                "Disruption Error Multiplier ($R_{\\text{MASE}}$)",
                "Generalizability (Evaluation Dimension 3)",
                "Kaplan-Meier Survival Analysis",
                "Mean Absolute Error (MAE)",
                "Mean Absolute Percentage Error (MAPE)",
                "Mean Absolute Scaled Error (MASE)",
                "Mean Forecast Bias",
                "Out-of-Time Holdout Evaluation",
                "Relative Transfer Ratio (RTR)",
                "Resilience (Evaluation Dimension 2)",
                "Robustness (Evaluation Dimension 1)",
                "Root Mean Squared Error (RMSE)",
                "Time-to-Recovery ($\\text{TTR}_{\\text{shock}}$)",
                "Transfer Error Penalty ($\\Delta_{\\text{transfer}}$)",
                "Welch's $t$-Test",
                "Wilcoxon Signed-Rank Test",
                "Zero-Flight Intercept Test",
                "Zero-Shot Transfer Deployment"
            ]
        }
    ]

    def make_anchor(term):
        t = term.replace("$M_0$", "m0")
        t = t.replace("$M_1^*", "m1-star")
        t = t.replace("$M_1$", "m1")
        t = t.replace("$M_2$", "m2")
        t = t.replace("$M_3$", "m3")
        t = t.replace("$M_4$", "m4")
        t = t.replace("$M_5$", "m5")
        t = t.replace("$R^2$", "r-squared")
        t = re.sub(r"\\[a-zA-Z]+", "", t)
        t = re.sub(r"[\$\{\}\(\)]", "", t)
        t = re.sub(r"[^a-zA-Z0-9\s\-]", "", t).strip().lower()
        return "-".join(t.split())

    def clean_sort_key(term):
        clean = re.sub(r"\(.*?\)", "", term)
        clean = re.sub(r"\$.*?\$", "", clean)
        clean = re.sub(r"[^a-zA-Z0-9\s]", " ", clean).strip().lower()
        return clean.split()

    all_items = []
    for c in cat_definitions:
        for t in c["terms"]:
            all_items.append((t, c["short"], c["id"]))

    all_items.sort(key=lambda x: clean_sort_key(x[0]))

    quick_finder_rows = []
    for t, cat_name, cat_id in all_items:
        anchor = make_anchor(t)
        quick_finder_rows.append(f"| [{t}](#{anchor}) | {cat_name} |")

    quick_finder_table = "| Technical Term | Category Classification |\n| :--- | :--- |\n" + "\n".join(quick_finder_rows)

    out_lines = []
    out_lines.append("# Glossary of Technical Terms by Operational Category\n")
    out_lines.append("This glossary defines the operational concepts, aviation data systems, statistical metrics, and predictive modeling methods used across Chapters I through V of this manuscript. In accordance with the *Publication Manual of the American Psychological Association* (7th ed.; APA, 2020) guidelines for academic dissertations and technical manuscripts, terms are organized hierarchically into six operational categories that mirror the functional workflow of commercial airport operations and predictive analytics.\n")
    out_lines.append("To support airport Federal Security Directors (FSDs), operational planners, and transportation researchers without an advanced background in machine learning, each definition is written in plain, intuitive language and grounded in airport operations. Terms within each category are arranged in strict alphabetical order. For readers seeking a specific term across the entire manuscript, the Alphabetical Quick-Finder Index below provides immediate navigation to all 99 entries.\n")
    out_lines.append("## Alphabetical Quick-Finder Index\n")
    out_lines.append(quick_finder_table + "\n")
    out_lines.append("---\n")

    for cat in cat_definitions:
        out_lines.append(f"## {cat['title']}\n")
        out_lines.append(f"*{cat['desc']}*\n")
        sorted_terms = sorted(cat["terms"], key=lambda t: clean_sort_key(t))
        for t in sorted_terms:
            entry_text = entry_dict[t]
            anchor = make_anchor(t)
            entry_text_mod = re.sub(r"^### (.*?)$", f'<a id="{anchor}"></a>\n### \\1', entry_text)
            out_lines.append(entry_text_mod + "\n")
        out_lines.append("---\n")

    full_content = "\n".join(out_lines)

    with open("thesis_docs/manuscripts/glossary.md", "w") as f:
        f.write(full_content)

    print("Categorized glossary generated successfully. Total length:", len(full_content))

if __name__ == "__main__":
    main()
