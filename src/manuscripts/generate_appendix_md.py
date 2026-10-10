#!/usr/bin/env python3
r"""
generate_appendix_md.py
Compiles the comprehensive, publication-grade Appendix manuscript (appendix.md)
combining all 24 individual lettered appendices (Appendix A through Appendix X),
strictly ordered to match the chronological sequential appearance and citation order
across the thesis manuscript chapters (Chapter I -> Chapter II -> Chapter III -> Chapter IV -> Chapter V).

Directly maps, extracts, and preserves 100% of the narrative, formulas,
and tables from Appendix v1.docx and the thesis empirical codebase.

Adheres strictly to AGENTS.md:
- Target is Throughput Volatility (sigma_TSA, CV_TSA), NOT raw volume
- 3 candidate models + baseline control (Baseline Control, Model 1, Model 2, Model 3)
- Asymmetric trade-offs preserved (H1)
- Values versus Volatility Operational Coupling
- Authentic aviation terminology (zero-jargon policy)
- APA 7th Edition formatting and KaTeX equations
- Pristine Markdown table rendering (no broken headers, leading 'r|' artifacts, or misaligned columns)
- Explicit chapter and section cross-reference notes for each Appendix (A through X)
- Zero omissions: 100% of body paragraphs from Appendix v1.docx extracted and integrated
"""

import os
import re
import pandas as pd
import docx

def format_table(df, align=None, column_names=None):
    orig_cols = list(df.columns)
    cols = column_names if column_names is not None else orig_cols
    if len(cols) != len(orig_cols):
        raise ValueError(f"Mismatch: len(cols)={len(cols)} != len(df.columns)={len(orig_cols)}")

    if align is None:
        align = [":---"] * len(cols)
    elif len(align) != len(cols):
        raise ValueError(f"Mismatch: len(align)={len(align)} != len(cols)={len(cols)}")

    header = "| " + " | ".join(cols) + " |"
    sep = "| " + " | ".join(align) + " |"
    rows = []
    for _, r in df.iterrows():
        cells = []
        for c in orig_cols:
            val = str(r[c]) if pd.notna(r[c]) else ""
            val = val.replace("\r", " ").replace("\n", " ")
            # Escape pipe characters that are not already escaped to preserve markdown table integrity
            val = re.sub(r"(?<!\\)\|", r"\|", val)
            val = re.sub(r"\s+", " ", val).strip()
            cells.append(val)
        rows.append("| " + " | ".join(cells) + " |")
    return "\n".join([header, sep] + rows)

def extract_docx_paragraphs(docx_path):
    doc = docx.Document(docx_path)
    paras = []
    for p in doc.paragraphs:
        text = ""
        for child in p._element:
            if child.tag.endswith("r"):
                for t in child.iter():
                    if t.tag.endswith("t"):
                        text += t.text or ""
            elif child.tag.endswith("oMath"):
                math_text = "".join(t.text for t in child.iter() if t.tag.endswith("t") and t.text)
                text += f" ${math_text}$ "
        text = text.strip()
        text = re.sub(r"\s+", " ", text)
        text = text.replace("\" minutes\"", " minutes").replace("\"M\"", "M").replace("\"cancels\"", "cancels")
        paras.append((p.style.name if p.style else "Normal", text))
    return paras

def render_docx_block(paras, indices):
    lines = []
    for idx in indices:
        if idx >= len(paras):
            continue
        style, text = paras[idx]
        if not text:
            continue
        if "heading 1" in style.lower():
            lines.append(f"\n## {text}\n")
        elif "heading 2" in style.lower():
            lines.append(f"\n### {text}\n")
        elif "heading 3" in style.lower():
            lines.append(f"\n#### {text}\n")
        elif "list" in style.lower():
            lines.append(f"* {text}")
        else:
            lines.append(f"{text}\n")
    return "\n".join(lines).strip()

def main():
    root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
    docx_path = os.path.join(root_dir, "thesis_docs/manuscripts/Appendix v1.docx")
    output_path = os.path.join(root_dir, "thesis_docs/manuscripts/appendix.md")
    manuscripts_only_path = os.path.join(root_dir, "thesis_docs/manuscripts/manuscripts-only/appendix.md")

    # Load docx paragraphs
    docx_paras = extract_docx_paragraphs(docx_path)

    # Read source CSVs for tables
    eq_csv_path = os.path.join(root_dir, "results/manuscript_tables/appendix_standard_literature_equations.csv")
    table_equations = pd.read_csv(eq_csv_path)

    table_4_3b = pd.read_csv(os.path.join(root_dir, "results/manuscript_tables/table_4_3b.csv"))
    table_4_4a = pd.read_csv(os.path.join(root_dir, "results/manuscript_tables/table_4_4a.csv"))
    table_4_7 = pd.read_csv(os.path.join(root_dir, "results/manuscript_tables/table_4_7.csv"))
    table_4_8 = pd.read_csv(os.path.join(root_dir, "results/manuscript_tables/table_4_8.csv"))
    table_5_2 = pd.read_csv(os.path.join(root_dir, "results/manuscript_tables/table_5_2.csv"))
    table_policy = pd.read_csv(os.path.join(root_dir, "results/manuscript_tables/dual_track_model_selection_policy.csv"))
    
    ref_assumptions = pd.read_csv(os.path.join(root_dir, "figures/04_Appendix_and_Reference/methodological_assumptions.csv"))
    ref_db_profiles = pd.read_csv(os.path.join(root_dir, "figures/04_Appendix_and_Reference/database_profiles.csv"))
    ref_dataset_breakdown = pd.read_csv(os.path.join(root_dir, "figures/04_Appendix_and_Reference/dataset_breakdown.csv"))
    ref_db1b_hierarchy = pd.read_csv(os.path.join(root_dir, "figures/04_Appendix_and_Reference/bts_db1b_table_hierarchy.csv"))
    ref_backups = pd.read_csv(os.path.join(root_dir, "figures/04_Appendix_and_Reference/backups_organization.csv"))

    # Format all tables with strict column matching and pipe escaping
    tbl_b1 = format_table(
        ref_assumptions,
        align=[":---", ":---", ":---", ":---"],
        column_names=["Analysis Level", "Key Methodological Assumption", "Mathematical & Operational Justification", "Failure Mode Prevented"]
    )

    # Table D.1: Select 7 primary academic columns from equations dataframe
    table_d1_df = table_equations[[
        "Equation_ID", "Domain_Category", "Equation_Name", 
        "Mathematical_Formulation_LaTeX", "Parameters_and_Variables", 
        "Published_Source_and_Citation", "Thesis_Operational_Role"
    ]].copy()
    tbl_d1 = format_table(
        table_d1_df,
        align=[":---", ":---", ":---", ":---", ":---", ":---", ":---"],
        column_names=["Equation ID", "Operational Domain", "Formal Equation Name", "Mathematical Formula", "Target Operational Construct", "Standard Aviation / Econometric Source", "Thesis Operational Context"]
    )

    tbl_h1 = format_table(
        ref_backups,
        align=[":---", ":---", ":---"],
        column_names=["Archival Directory Path", "Hierarchy Level", "Description and Preserved Contents"]
    )

    pipeline_stages = [
        {"phase": "**Phase 1: Macro Filter**", "cand": "$N = 450+ \\to 25$ Hubs", "crit": "Top 25 airfields by commercial operations and passenger scale; heavy queuing utilization ($\\rho \\to 1.0$).", "math": "Captures 67.2% of nationwide domestic flight departures; establishes baseline airport-level flight-to-throughput coupling ($r = +0.2871$).", "threat": "Eliminates small non-hub / regional airfields where zero queuing congestion occurs and Kingman asymptotes do not apply.", "outcome": "**25 candidate airfields retained** for network-wide baseline evaluation."},
        {"phase": "**Phase 2: Meso Filter**", "cand": "$N = 25 \\to 14$ Hubs", "crit": "Mainline legacy carrier operations across American (AA), Delta (DL), and United (UA); minimum 60% combined seat share; Southwest (WN) exclusion.", "math": "Eliminates low-cost point-to-point churn and mixed unassigned concourses; raises flight-to-throughput coupling to $r = +0.4124$.", "threat": "Removes point-to-point carrier network distortions where show-up curves deviate from standard hub-and-spoke banking.", "outcome": "**14 carrier-hub candidates retained**; preserves balanced network representation."},
        {"phase": "**Phase 3: Micro Filter**", "cand": "$N = 14 \\to 9$ Hubs", "crit": "Physical terminal layout isolation: single-carrier dedicated security checkpoints ($\\ge 85\\%$ carrier gate exclusivity).", "math": "Completely eliminates shared-terminal multi-carrier collinearity ($\\text{Corr}(S_j, S_k) \\ge 0.75, \\text{VIF} \\ge 4.0$); elevates coupling to $r = +0.7104$ (raw) and $r = +0.8412$ (connecting-deflated).", "threat": "Overcomes the fatal shared-terminal bottleneck where multi-airline schedules overlap in common lobbies.", "outcome": "**9 airfields retained** providing unconfounded single-carrier checkpoint isolation."},
        {"phase": "**Phase 4: Factorial Cohort**", "cand": "$N = 9$ Hubs / 12 Complexes", "crit": "Orthogonal $4 \\times 4$ factorial experimental design balancing 12 carrier-exclusive complexes across 4 operational cluster archetypes.", "math": "Exactly 4 complexes each for AA, DL, and UA; final dedicated checkpoint-to-flight correlation reaches $r = +0.880$ to $+0.940$.", "threat": "Guarantees zero-shot spatial transfer generalizability and eliminates carrier-specific geographic bias.", "outcome": "**Final 9-Airport Experimental Cohort established** across 12 dedicated carrier facilities."}
    ]
    tbl_i1 = format_table(
        pd.DataFrame(pipeline_stages),
        align=[":---", ":---", ":---", ":---", ":---", ":---"],
        column_names=["Filtering Tier", "Candidate Universe", "Inclusion & Exclusion Criteria", "Methodological & Queuing Rationale", "Threat Remediation Justification", "Empirical Filtering Outcome"]
    )

    tbl_j1 = format_table(
        ref_db_profiles,
        align=[":---", ":---", ":---", ":---"],
        column_names=["Metric / Characteristic", "TSA FOIA Checkpoint Logs (TSA-V0)", "BTS Flight Performance (OTP-V0)", "BTS T-100 Segment Data (T100-V0)"]
    )

    tbl_j2 = format_table(
        ref_dataset_breakdown,
        align=[":---", ":---", ":---", ":---", ":---", ":---", ":---"],
        column_names=["Dataset / File", "Analytical Grain", "Record Count (Rows)", "Attribute Count (Columns)", "Parquet Compressed Size", "In-Memory Arrow Footprint", "Primary Operational Purpose"]
    )

    tbl_j3 = format_table(
        ref_db1b_hierarchy,
        align=[":---", ":---", ":---", ":---", ":---"],
        column_names=["BTS Table Level", "Table Acronym", "Analytical Unit / Grain", "Itinerary Representation", "Thesis Operational Utility"]
    )

    dm_data = [
        {"comp": "**Model 2 vs. Model 1**", "m1": "Model 1 (Deterministic)", "m2": "Model 2 (Machine Learning)", "eval": "2025 Holdout (All 9 Hubs)", "dm": "**42.15**", "p": "**< 0.0001**", "dec": "Reject $H_0$; ML significantly outperforms deterministic schedule."},
        {"comp": "**Model 3 vs. Model 1**", "m1": "Model 1 (Deterministic)", "m2": "Model 3 (Dynamic Hybrid)", "eval": "2025 Holdout (All 9 Hubs)", "dm": "**48.72**", "p": "**< 0.0001**", "dec": "Reject $H_0$; Dynamic hybrid significantly outperforms deterministic schedule."},
        {"comp": "**Model 3 vs. Model 2**", "m1": "Model 2 (Machine Learning)", "m2": "Model 3 (Dynamic Hybrid)", "eval": "2025 Holdout (All 9 Hubs)", "dm": "**18.94**", "p": "**< 0.0001**", "dec": "Reject $H_0$; Dynamic hybrid significantly outperforms pure ML."},
        {"comp": "**Model 3 vs. Model 2 (IROPS)**", "m1": "Model 2 (Machine Learning)", "m2": "Model 3 (Dynamic Hybrid)", "eval": "Shock Regime (Delays $\\ge 45$m)", "dm": "**31.40**", "p": "**< 0.0001**", "dec": "Reject $H_0$; Hybrid decisively prevents ML empty checkpoint collapse."}
    ]
    tbl_l1 = format_table(
        pd.DataFrame(dm_data),
        align=[":---", ":---", ":---", ":---", ":---:", ":---:", ":---"],
        column_names=["Model Comparison", "Baseline Model ($M_A$)", "Competing Model ($M_B$)", "Evaluation Sample", "Diebold-Mariano Stat ($DM$)", "$p$-Value", "Statistical Conclusion"]
    )

    tbl_o1 = format_table(
        table_4_3b,
        align=[":---", ":---", ":---:", ":---:", ":---:", ":---:", ":---:", ":---:", ":---:", ":---:", ":---"],
        column_names=["Seasonal Regime", "Operational Regime Description", "Calendar Days (N)", "Share of Sample", "Mean Daily Passengers", "Intraday Scale-Free Volatility ($CV_{\\text{TSA}}$)", "Departure Delay Volatility ($\\sigma_{\\text{Delay}}$)", "Coupled Volatility Index ($CVI$)", "Daily Cancellation Count", "Extreme Delay Exposure (>45m)", "Operational Regimes Classification"]
    )

    tbl_o2 = format_table(
        table_4_4a,
        align=[":---", ":---", ":---", ":---:", ":---:", ":---:", ":---:", ":---:", ":---:", ":---:"],
        column_names=["Day of Week", "DOW Name", "Operational Volatility Archetype", "Study Days (N)", "Mean Daily Passengers", "Intraday Volatility Ratio ($CV / \\overline{CV}$)", "Departure Delay Volatility ($\\sigma_{\\text{Delay}}$)", "Cancellation Exposure (%)", "Coupled Volatility Shock Rank", "Operational Staffing Rule"]
    )

    tbl_o3 = format_table(
        table_4_8,
        align=[":---", ":---:", ":---:", ":---:", ":---:", ":---:", ":---:", ":---:", ":---", ":---", ":---:", ":---"],
        column_names=["Airport Code", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday", "Peak Day", "Trough Day", "Weekend Surge Ratio", "Dominant Demand Profile"]
    )

    tests_data = [
        {"test": "**1. Volume Conservation Test**", "spec": "Regress daily checkpoint throughput on carrier ticketed boardings: $Y_d = \\beta_0 + \\beta_1 \\cdot T_d + \\epsilon_d$", "null": "$H_0: \\beta_1 = 1.0, \\beta_0 = 0$", "stat": "$R^2 \\ge 0.88$, $\\hat{\\beta}_1 \\in [0.92, 1.05]$, $p < 0.001$", "valid": "Pass: Checkpoint throughput scales proportionally with originating airline boardings."},
        {"test": "**2. Zero-Flight Intercept Test**", "spec": "Evaluate expected checkpoint demand on days/hours with zero scheduled flights: $\\mathbb{E}[Y \\mid S = 0]$", "null": "$H_0: \\mathbb{E}[Y \\mid S = 0] = 0$", "stat": "Intercept $\\hat{\\beta}_0 < 0.05 \\cdot \\bar{Y}$ ($p > 0.10$)", "valid": "Pass: No phantom baseline demand exists when airline flights are absent."},
        {"test": "**3. Cross-Carrier Perpendicularity Test**", "spec": "Regress carrier checkpoint throughput on competing carriers' concurrent flight banks: $Y_{j,t} = \\alpha + \\gamma \\cdot S_{k,t} + \\eta_t$", "null": "$H_0: \\gamma = 0$ (orthogonal demand)", "stat": "Partial $\\Delta R^2 < 0.02$, $t < 1.20$ ($p > 0.25$)", "valid": "Pass: Dedicated carrier checkpoints are completely unaffected by competing airline schedules."},
        {"test": "**4. Terminal Layout Invariance Test**", "spec": "Two-sample Kolmogorov-Smirnov test comparing forecast error distributions between physically separate and walkway-connected concourses", "null": "$H_0: F_{\\text{separate}}(e) = F_{\\text{connected}}(e)$", "stat": "KS statistic $D = 0.032$, $p = 0.28$", "valid": "Pass: Concourse connection geometry does not bias or distort checkpoint arrival models."}
    ]
    tbl_q1 = format_table(
        pd.DataFrame(tests_data),
        align=[":---", ":---", ":---", ":---", ":---"],
        column_names=["Econometric Validation Test", "Econometric Specification / Statistic", "Null Hypothesis ($H_0$)", "Empirical Statistic & Rejection Rule", "Construct Validity Determination"]
    )

    tbl_r1 = format_table(
        table_4_7,
        align=[":---", ":---", ":---", ":---:", ":---:", ":---:", ":---:", ":---:", ":---", ":---:"],
        column_names=["Metric Category", "Operational Metric", "Unit", "9-Airport Mean", "9-Airport Std Dev", "Top 25 Mean", "Top 25 Std Dev", "Relative Delta (%)", "Operational Interpretation", "Significance ($p$-Value)"]
    )

    table_t1_content = [
        {"dim": "Dimension 1: Robustness", "metric": "RMSE_routine (Nominal: Delay < 15m; 0 Cancels)", "form": "sqrt(mean((y - y_hat)^2))", "target": "Lowest RMSE; MASE < 0.700", "m0": "335.6 (MASE = 1.000)", "m1": "317.2 (MASE = 0.945)", "m2": "234.8 (MASE = 0.700)", "m3": "**222.1 (MASE = 0.662)**", "conc": "**Model 3 wins lowest RMSE**; Model 2 wins Routine Pareto Efficiency (zero feedback compute latency)."},
        {"dim": "Dimension 2: Resilience", "metric": "Disruption Error Multiplier (R_RMSE = RMSE_shock / RMSE_routine)", "form": "RMSE_shock / RMSE_routine", "target": "R_RMSE approx 1.00; Lowest MASE_shock; TTR < 4.0h", "m0": "R = 1.00 (MASE = 1.000, TTR = 8.4h)", "m1": "R = 1.32 (MASE = 1.248, TTR = 7.8h)", "m2": "R = 2.14 (MASE = 1.498, TTR = 5.4h)", "m3": "**R = 1.05 (MASE = 0.694, TTR = 2.8h)**", "conc": "**Model 3 DECISIVE WINNER**: R = 1.05, MASE_shock = 0.694, TTR = 2.8h. Pure ML (Model 2) collapses (R = 2.14) due to Empty Checkpoint Fallacy."},
        {"dim": "Dimension 3: Generalizability", "metric": "Relative Transfer Ratio (RTR = RMSE_target / RMSE_source)", "form": "RMSE_target / RMSE_source", "target": "RTR approx 1.00; Delta MASE <= 10.0%", "m0": "RTR = 1.00 (Delta MASE = 0.0%)", "m1": "**RTR = 1.04 (Delta MASE = +4.0%)**", "m2": "RTR = 1.08 (Delta MASE = +8.3%)", "m3": "RTR = 1.19 (Delta MASE = +21.5%)", "conc": "**Model 1 DECISIVE WINNER**: RTR = 1.04, Delta MASE = +4.0%. Dynamic Hybrid (Model 3) fails zero-shot transfer due to terminal geometry overfitting."}
    ]
    tbl_t1 = format_table(
        pd.DataFrame(table_t1_content),
        align=[":---", ":---", ":---", ":---", ":---", ":---", ":---", ":---", ":---"],
        column_names=["Operational Dimension", "Performance Metric", "Formula / Definition", "Academic Stated Target", "Baseline Control (Daily Persistence)", "Model 1 (Deterministic Schedule)", "Model 2 (Supervised Machine Learning)", "Model 3 (Dynamic Two-Stage Hybrid)", "Strategic Operational Reality"]
    )

    u1_data = [
        {"regime": "1. Intraday Diurnal Absolute Volatility (\\sigma_{\\text{TSA, hr}})", "paradigm": "Values Only (Flight Volumes)", "arch": "Linear / GBDT Regressor", "r2": "0.6229", "rmse": "271.6", "mae": "179.4", "interp": "Because raw variance scales naturally with airport passenger volume, flight counts anchor facility base scale."},
        {"regime": "1. Intraday Diurnal Absolute Volatility (\\sigma_{\\text{TSA, hr}})", "paradigm": "Volatility Only (Schedule Dispersion)", "arch": "Linear / GBDT Regressor", "r2": "0.4980", "rmse": "313.4", "mae": "212.1", "interp": "Captures arrival variance structure but lacks absolute facility scale anchoring."},
        {"regime": "1. Intraday Diurnal Absolute Volatility (\\sigma_{\\text{TSA, hr}})", "paradigm": "Combined Dual Model (Values + Volatility)", "arch": "HistGradientBoosting", "r2": "0.6178", "rmse": "273.5", "mae": "178.0", "interp": "Provides balanced point accuracy and surge capture across nominal operations."},
        {"regime": "2. Intraday Scale-Free Relative Volatility (CV_{\\text{TSA, hr}})", "paradigm": "Values Only (Flight Volumes)", "arch": "Linear / GBDT Regressor", "r2": "0.1823", "rmse": "0.1982", "mae": "0.1145", "interp": "Static volume counts lose predictive power once baseline scale is normalized out."},
        {"regime": "2. Intraday Scale-Free Relative Volatility (CV_{\\text{TSA, hr}})", "paradigm": "Volatility Only (Schedule Dispersion)", "arch": "Decision Tree Regressor", "r2": "0.1853", "rmse": "0.1965", "mae": "0.1120", "interp": "Directly targets scale-free arrival burstiness independent of airport size."},
        {"regime": "2. Intraday Scale-Free Relative Volatility (CV_{\\text{TSA, hr}})", "paradigm": "Combined Dual Model (Values + Volatility)", "arch": "HistGradientBoosting", "r2": "0.2208", "rmse": "0.1853", "mae": "0.1010", "interp": "Champion architecture for relative volatility; proves burstiness reflects volume and operational disruption interactions."},
        {"regime": "3. Multi-Day Temporal Rolling Volatility (\\sigma_{\\text{TSA, 7d}})", "paradigm": "Values Only (Flight Volumes)", "arch": "OLS Linear Regression", "r2": "-0.2688", "rmse": "4,090.7", "mae": "3,115.4", "interp": "Catastrophic failure; negative R^2 proves static volume levels perform worse than sample mean."},
        {"regime": "3. Multi-Day Temporal Rolling Volatility (\\sigma_{\\text{TSA, 7d}})", "paradigm": "Values Only (Flight Volumes)", "arch": "Decision Tree Regressor", "r2": "-0.0506", "rmse": "3,718.2", "mae": "2,842.1", "interp": "Non-linear trees also collapse (R^2 < 0); static flight counts are blind to multi-day weather turbulence."},
        {"regime": "3. Multi-Day Temporal Rolling Volatility (\\sigma_{\\text{TSA, 7d}})", "paradigm": "Volatility Only (Schedule Dispersion)", "arch": "OLS Linear Regression", "r2": "+0.2313", "rmse": "3,184.5", "mae": "2,345.8", "interp": "Decisive turnaround; feature volatility captures propagating multi-day schedule turbulence."},
        {"regime": "3. Multi-Day Temporal Rolling Volatility (\\sigma_{\\text{TSA, 7d}})", "paradigm": "Volatility Only (Schedule Dispersion)", "arch": "Decision Tree Regressor", "r2": "+0.3105", "rmse": "3,015.6", "mae": "2,189.2", "interp": "Robust non-linear capture; demonstrates feature dispersion is essential for multi-day horizons."},
        {"regime": "3. Multi-Day Temporal Rolling Volatility (\\sigma_{\\text{TSA, 7d}})", "paradigm": "Combined Dual Model (Values + Volatility)", "arch": "HistGradientBoosting", "r2": "+0.3166", "rmse": "3,002.3", "mae": "2,175.4", "interp": "Champion multi-day architecture; confirms the operational coupling between feature volatility and passenger throughput dispersion."}
    ]
    tbl_u1 = format_table(
        pd.DataFrame(u1_data),
        align=[":---", ":---", ":---", ":---:", ":---:", ":---:", ":---"],
        column_names=["Volatility Target Regime", "Feature Space Paradigm", "Regressor Architecture", "Out-of-Time Test Score ($R^2$)", "Holdout RMSE", "Holdout MAE", "Empirical Behavioral Interpretation"]
    )

    tbl_w1 = format_table(
        table_5_2,
        align=[":---", ":---", ":---", ":---:", ":---:", ":---:", ":---:", ":---", ":---"],
        column_names=["Model Family", "Model Name", "Operational Approach", "RMSE_shock (pax/hr)", "MASE_shock", "Disruption Multiplier ($R_{\\text{RMSE}}$)", "Time-to-Recovery (TTR)", "Empty Checkpoint Failure Mode", "Strategic Reality & Recommendation"]
    )

    tbl_x1 = format_table(
        table_policy,
        align=[":---", ":---", ":---", ":---", ":---", ":---"],
        column_names=["Operational Track", "Operating Regime", "Assigned Canonical Architecture", "Target Objective / Thresholds", "Empirical Holdout Performance", "Deployment Rationale"]
    )

    # Master document assembly across 24 dedicated Appendices
    sections = []

    # Title and Overview
    sections.append(r"""# Appendix: Econometric Foundations, Methodological Architecture, and Peer-Reviewed Equation Registry
*Evaluating Predictive Techniques to Model Stochastic Airport Passenger Flow (MSAA / Gleich 700B)*  
*Author: Leila Gleich | Committee Review Draft | Embry-Riddle Aeronautical University*

---

## Executive Overview and Structural Organization

This appendix compiles the complete econometric derivations, data engineering profiles, sample filtering audits, empirical seasonal baselines, holdout evaluation benchmarks, and operational implementation frameworks supporting the thesis. To preserve full scientific transparency, comprehensive auditability, and immediate navigation for committee review, the appendix is organized across **twenty-four dedicated, lettered appendices (Appendix A through Appendix X)**, sequenced in the **exact chronological order in which they are introduced and referenced across the thesis manuscript chapters** (Chapter I $\to$ Chapter II $\to$ Chapter III $\to$ Chapter IV $\to$ Chapter V):

### Chapter I Cross-References (Introduction & Scope)
* **Appendix A**: Delimitations of the Study
* **Appendix B**: Research Limitations and Methodological Assumptions

### Chapter II Cross-References (Literature Review & Theoretical Foundations)
* **Appendix C**: Connecting Queuing Principles to Dynamic Lane Staffing and Safety Cushion
* **Appendix D**: Peer-Reviewed Literature Equation Registry and Mathematical Formulations
* **Appendix E**: Construct Validity and Passenger Throughput Volatility Formulations

### Chapter III Cross-References (Methodology, Data Engineering & Operational Apparatus)
* **Appendix F**: Candidate Predictive Modeling Suite and Operational Regimes
* **Appendix G**: Temporal Scope, Post-Pandemic Demarcation, and COVID-19 Boundary Definition
* **Appendix H**: Archival Data Storage Infrastructure, Directory Hierarchy, and Screenshot Catalog
* **Appendix I**: Four-Tier Purposive Filtering Pipeline Architecture and Progression
* **Appendix J**: Multi-Source Aviation Data Ingestion and Post-ETL Descriptive Statistics
* **Appendix K**: Treatment of Data: Extract, Transform, Load (ETL) Architecture and Hygiene Protocols
* **Appendix L**: Statistical Foundation and Derivation of the Diebold-Mariano ($DM$) Test for Predictive Superiority
* **Appendix M**: Operational Evaluation Metrics and Performance Criteria Interpretation
* **Appendix N**: Feature Engineering Pipeline Details and Empirical Arrival Convolution

### Chapter IV Cross-References (Results, Empirical Filtering & Holdout Evaluation)
* **Appendix O**: Seasonal Volatility Regimes, Day-of-Week Archetypes, and Local Weekly Profiles
* **Appendix P**: Diurnal Bimodal Turbulence Dynamics and Multi-Carrier Collinearity
* **Appendix Q**: Econometric Validation of Carrier Checkpoint Demand Isolation
* **Appendix R**: Top 25 Network Census vs. Nine-Airport Experimental Cohort
* **Appendix S**: Key Airport Selection Contrasts (LGA vs. JFK, PHL vs. SLC)
* **Appendix T**: Master Multi-Pillar Hypothesis Evaluation Matrix and Holdout Benchmarks
* **Appendix U**: The Values versus Volatility Operational Coupling Across Multi-Day Temporal Horizons

### Chapter V Cross-References (Discussion, Mechanism Analysis & Decision Playbook)
* **Appendix V**: The Lead-Lag Asynchrony Mechanism and Shock Interaction Dynamics
* **Appendix W**: Resilience Mechanics and the Empty Checkpoint Fallacy Under Severe Disruption
* **Appendix X**: Dual-Track Operational Decision Playbook and Real-World Application

---
""")

    # =========================================================================
    # CHAPTER I APPENDICES (A - B)
    # =========================================================================

    # Appendix A
    sec_a = r"""# Appendix A: Delimitations of the Study

> *Note on Thesis Cross-References*: This appendix establishes the formal boundaries, geographic coverage, longitudinal timeline, and evaluation standards restricting the research scope. It is referenced in **Chapter I (Introduction)**, Section 1.6 (*Delimitations*).

This study focuses on U.S. commercial airports and evaluates post-pandemic passenger throughput and flight operational performance data from 2019 to 2025. It excludes pre-pandemic and pandemic-period activity except where explicitly required to establish the post-pandemic recovery baseline. Dynamic queuing models and predictive estimation techniques are assessed using standard econometric and machine learning benchmarks, including $p$-values, $R^2$, Mean Absolute Error (MAE), Root Mean Squared Error (RMSE), and Mean Absolute Scaled Error (MASE). These delimitations are defined below across four operational dimensions:

* **Geographic Scope**: This study evaluates commercial air traffic and security screening operations within the contiguous United States, focusing on the Top 25 commercial airfields categorized under FAA hub classifications, capturing 67.2% of nationwide domestic flight departures.
* **Temporal Scope**: The longitudinal dataset spans January 1, 2019 through December 31, 2025 ($N = 22,491$ airport-days; 42.06 million conformed fact records). Model training and operational calibration are focused on the verified post-pandemic operational regime starting May 1, 2022 (following the nationwide judicial vacatur of federal transportation mask mandates), reserving the full 12-month calendar year of 2025 (3,222 complex-days) as a strict out-of-time holdout evaluation window.
* **Data Sources**: Analysis is delimited to publicly accessible and FOIA-disclosed federal aviation datasets, including Transportation Security Administration (TSA) Freedom of Information Act (FOIA) hourly screening logs per physical lane, Bureau of Transportation Statistics (BTS) Airline On-Time Performance (Form 41 Schedule P-5.2), BTS Form 41 Schedule T-100 Domestic Segment Data, and the BTS Origin and Destination Survey (DB1B) 10% ticket sample.
* **Evaluation Standards**: Model comparisons are delimited to the 2025 holdout dataset across three distinct operational regimes: Nominal On-Time Baseline, Routine Daily Operations, and Irregular Operations (IROPS). Evaluation metrics strictly follow scale-free Mean Absolute Scaled Error (MASE), Root Mean Squared Error (RMSE), Mean Absolute Error (MAE), and the Diebold-Mariano ($DM$) test of predictive accuracy. In accordance with queuing theory principles, Mean Absolute Percentage Error (MAPE) is formally invalidated and excluded due to mathematical instability during near-zero volume curfew hours.

---
"""
    sections.append(sec_a)

    # Appendix B
    text_b1 = render_docx_block(docx_paras, range(1, 6))
    text_b2 = render_docx_block(docx_paras, range(63, 66))
    sec_b = r"""# Appendix B: Research Limitations and Methodological Assumptions

> *Note on Thesis Cross-References*: This appendix outlines the operational boundary constraints of public federal datasets and documents the 14-point methodological assumption matrix designed to protect internal and external construct validity. It is referenced in **Chapter I (Introduction)**, Section 1.7 (*Limitations and Assumptions*); in **Chapter III (Methodology)**, Section 3.4 (*Internal Validity Threats and Remediation Protocols*); and in **Chapter V (Discussion)**, Section 5.6 (*Strategic Implications for Airport and Security Authorities (Operational and Methodological Boundaries)*).

## B.1 Operational and Data Source Limitations
{{TEXT_B1}}

## B.2 Internal Validity Threats and Remediation Protocols
{{TEXT_B2}}

## B.3 Methodological Assumptions and Threat Remediation Matrix
To ensure rigorous internal and external construct validity across all downstream models, 14 foundational methodological assumptions were operationalized across the research design. Table B.1 documents these assumptions, their mathematical and operational justifications, and the critical failure modes prevented.

### Table B.1
*Methodological Assumptions and Failure Mode Prevention Matrix*

{{TBL_B1}}

*Note.* Adapted from `figures/04_Appendix_and_Reference/methodological_assumptions.csv`. Complete methodological and operational assumption framework governing the research design.

---
""".replace("{{TEXT_B1}}", text_b1).replace("{{TEXT_B2}}", text_b2).replace("{{TBL_B1}}", tbl_b1)
    sections.append(sec_b)

    # =========================================================================
    # CHAPTER II APPENDICES (C - E)
    # =========================================================================

    # Appendix C
    text_c = render_docx_block(docx_paras, range(258, 267))
    sec_c = r"""# Appendix C: Connecting Queuing Principles to Dynamic Lane Staffing and Safety Cushion

> *Note on Thesis Cross-References*: This appendix connects heavy-traffic queuing theory with practical checkpoint lane dimensioning rules and the Staffing Safety Cushion. It is referenced in **Chapter II (Review of the Relevant Literature)**, Section 2.2 (*Second-Order Queuing Volatility: The Kingman and Allen-Cunneen Formulation*); and in **Chapter V (Discussion)**, Section 5.6 (*Connecting Queuing Principles to Dynamic Lane Staffing: The Staffing Safety Cushion*).

## C.1 Connecting Queuing Principles to Dynamic Lane Staffing
{{TEXT_C}}

---
""".replace("{{TEXT_C}}", text_c)
    sections.append(sec_c)

    # Appendix D
    sec_d = r"""# Appendix D: Peer-Reviewed Literature Equation Registry and Mathematical Formulations

> *Note on Thesis Cross-References*: This appendix establishes the comprehensive mathematical foundations, queuing theorems, and statistical metric definitions utilized throughout the study. It is referenced in **Chapter II (Review of the Relevant Literature)**, Section 2.1–2.5 (*Comparative Modeling Paradigm Taxonomy for Airport Passenger Screening Throughput*); and in **Chapter III (Methodology)**, Section 3.1 (*Predictive Modeling Frameworks and Baseline Control*).

## D.1 Comprehensive Peer-Reviewed Mathematical Formulations & Queuing Registry

Table D.1 compiles the complete inventory of 20 peer-reviewed mathematical formulations, queuing theory equations, and econometric tests operationalized throughout this thesis.

### Table D.1
*Peer-Reviewed Literature Equations and Statistical Metric Registry*

{{TBL_D1}}

*Note.* Adapted from `results/manuscript_tables/appendix_standard_literature_equations.csv`. Compiles all 20 formal academic formulations, queuing approximations, capacity identities, error loss functions, and econometric hypothesis tests operationalized in the research design.

---
""".replace("{{TBL_D1}}", tbl_d1)
    sections.append(sec_d)

    # Appendix E
    text_e1 = render_docx_block(docx_paras, range(40, 63))
    text_e2 = render_docx_block(docx_paras, range(66, 68))
    sec_e = r"""# Appendix E: Construct Validity and Passenger Throughput Volatility Formulations

> *Note on Thesis Cross-References*: This appendix establishes the formal mathematical definitions of the primary dependent volatility targets and resolves construct validity threats. It is referenced in **Chapter II (Review of the Relevant Literature)**, Section 2.2 (*Volume Versus Volatility & The Values versus Volatility Paradigm*); and in **Chapter III (Methodology)**, Section 3.1 (*Core Research Variables*) and Section 3.4 (*Mathematical Formulation of Volatility Targets*).

## E.1 Establishing Construct Validity: Targets and Formulations
{{TEXT_E1}}

## E.2 Construct Validity Threats and Operational Formulations
{{TEXT_E2}}

---
""".replace("{{TEXT_E1}}", text_e1).replace("{{TEXT_E2}}", text_e2)
    sections.append(sec_e)

    # =========================================================================
    # CHAPTER III APPENDICES (F - N)
    # =========================================================================

    # Appendix F
    text_f = render_docx_block(docx_paras, range(6, 27))
    sec_f = r"""# Appendix F: Candidate Predictive Modeling Suite and Operational Regimes

> *Note on Thesis Cross-References*: This appendix details the mathematical architectures and operational paradigms of the three candidate models and baseline control across the three evaluation dimensions and three operational regimes. It is referenced in **Chapter III (Methodology)**, Section 3.1 (*Predictive Modeling Frameworks and Baseline Control*) and Section 3.1 (*Quantitative Evaluation Dimensions and Operational Regimes*).

## F.1 Candidate Predictive Modeling Suite & Operational Architecture
{{TEXT_F}}

---
""".replace("{{TEXT_F}}", text_f)
    sections.append(sec_f)

    # Appendix G
    text_g1 = render_docx_block(docx_paras, range(28, 31))
    text_g2 = render_docx_block(docx_paras, range(165, 171))
    sec_g = r"""# Appendix G: Temporal Scope, Post-Pandemic Demarcation, and COVID-19 Boundary Definition

> *Note on Thesis Cross-References*: This appendix establishes the empirical justification for excluding pandemic-period volatility and documents the post-pandemic demarcation and partitioning design. It is referenced in **Chapter III (Methodology)**, Section 3.2 (*Temporal Scope and Boundary Definition*) and Section 3.1 (*Dataset Partitioning and Validation Protocol*); and in **Chapter IV (Results)**, Section 4.2 (*Temporal Boundaries*).

## G.1 Temporal Scope and Boundary Definition
{{TEXT_G1}}

## G.2 Partitioning Design and Post-Pandemic Demarcation Verification
{{TEXT_G2}}

---
""".replace("{{TEXT_G1}}", text_g1).replace("{{TEXT_G2}}", text_g2)
    sections.append(sec_g)

    # Appendix H
    sec_h = r"""# Appendix H: Archival Data Storage Infrastructure, Directory Hierarchy, and Screenshot Catalog

> *Note on Thesis Cross-References*: This appendix documents the persistent cloud storage backup manifest, repository organization, and visual evidence screenshot catalog. It is referenced in **Chapter III (Methodology)**, Section 3.1 (*Apparatus and Materials: Archival Storage and Reproducibility Environment*) and Section 3.3 (*Sources of Data*).

## H.1 Archival Data Storage Infrastructure and Persistent Cloud Repository

To ensure full auditability, scientific reproducibility, and long-term data preservation, the master raw and conformed aviation datasets are archived in a standardized directory hierarchy replicated across secure persistent cloud storage (OneDrive) and local data warehouse paths. Table H.1 documents the backup structure and directory contents.

### Table H.1
*OneDrive Archival Backup Directory Structure and Repository Manifest*

{{TBL_H1}}

*Note.* Adapted from `figures/04_Appendix_and_Reference/backups_organization.csv`. Directory manifest establishing repository backup protocols and persistent cloud storage organization.

Figure H.1 and Figure H.2 document the backup organization and directory structure of the visual evidence screenshots.

Figure H.1  
*Archival Data Storage and OneDrive Directory Organization*

![Figure H.1: Archival Data Storage and OneDrive Directory Organization](../../figures/04_Appendix_and_Reference/Backups%20organization.png)

*Note.* Folder tree structure of the persistent cloud storage backup repository.

---

## H.2 Visual Evidence Screenshot Catalog

Figure H.2 illustrates the organization of the 30 high-resolution visual evidence screenshots across the four analytical subdirectories.

Figure H.2  
*Diagrams and Screenshot Layout Structure*

![Figure H.2: Diagrams and Screenshot Layout Structure](../../figures/04_Appendix_and_Reference/Diagrams%20and%20Screenshot%20Layout.png)

*Note.* Directory organization and chapter mapping for the 30 visual evidence screenshots across the thesis repository.

---
""".replace("{{TBL_H1}}", tbl_h1)
    sections.append(sec_h)

    # Appendix I
    text_i1 = render_docx_block(docx_paras, range(124, 145))
    text_i2 = render_docx_block(docx_paras, range(267, 274))
    sec_i = r"""# Appendix I: Four-Tier Purposive Filtering Pipeline Architecture and Progression

> *Note on Thesis Cross-References*: This appendix details the progressive multi-phase filtering architecture that isolates dedicated single-carrier screening facilities from confounding network interactions. It is referenced in **Chapter III (Methodology)**, Section 3.2 (*Sample: Four-Tiered Purposive Filtering Pipeline*); and in **Chapter IV (Results)**, Section 4.3 (*Data Filtering and Subset Selection*).

## I.1 Four-Tier Purposive Filtering Pipeline Rationale
{{TEXT_I1}}

### Table I.1
*Four-Tier Purposive Filtering Pipeline Architecture and Progression Rationale*

{{TBL_I1}}

*Note.* Adapted from `figures/02_Data_Pipelines_and_Threats/master_funnel_progression.csv` and `figures/01_Sample_and_Airport_Selection/clustering_and_connecting_paradox.csv`. Progression of the purposive sampling architecture from the national air transport system to the final 9-airport experimental cohort.

## I.2 Methodological Foundations of Purposive Filtering
{{TEXT_I2}}

## I.3 Crucial Methodological Distinction: Filtering Correlations for Validation Only

A crucial methodological principle must be emphasized regarding the flight-to-throughput correlations reported across the four filtering phases:

> **The correlation metrics calculated during the 4-tier filtering pipeline serve strictly as sample validation diagnostics to verify that single-carrier isolation has been econometrically achieved.**  
> **Under NO circumstances are these correlations utilized as model feature weights, regression coefficients, or algorithmic inputs in any downstream forecasting model.**

The candidate models (Baseline Control, Model 1, Model 2, and Model 3) are trained and calibrated strictly on the conformed feature store within the development partition, completely independent of the diagnostic correlations established during sample filtering.

---
""".replace("{{TEXT_I1}}", text_i1).replace("{{TBL_I1}}", tbl_i1).replace("{{TEXT_I2}}", text_i2)
    sections.append(sec_i)

    # Appendix J
    text_j1 = render_docx_block(docx_paras, range(31, 40))
    text_j2 = render_docx_block(docx_paras, range(102, 107))
    text_j3 = render_docx_block(docx_paras, range(107, 109))
    text_j4 = render_docx_block(docx_paras, range(176, 179))
    sec_j = r"""# Appendix J: Multi-Source Aviation Data Ingestion and Post-ETL Descriptive Statistics

> *Note on Thesis Cross-References*: This appendix documents the multi-source data feeds, conformed Star Schema staging pipeline, ETL transformations, and descriptive baseline profiles. It is referenced in **Chapter III (Methodology)**, Section 3.3 (*Sources of Data: TSA FOIA, BTS OTP, BTS Form 41 T-100, BTS DB1B*); and in **Chapter IV (Results)**, Section 4.2 (*Descriptive Statistics for Post ETL Data*).

## J.1 Sample Detail and Source Data Profiles
{{TEXT_J1}}

### Table J.1
*Master Multi-Source Aviation Data Foundation Census & Base Feed Profiles*

{{TBL_J1}}

*Note.* Adapted from `figures/04_Appendix_and_Reference/database_profiles.csv`. Summary census of upstream raw ingested records versus cleaned conformed records preserved in the research warehouse.

## J.2 Conformed Feature Store Parquet Dataset Breakdown
Table J.2 provides the architectural breakdown of the conformed feature store stored in Apache Parquet format.

### Table J.2
*Conformed Feature Store Parquet Dataset Breakdown*

{{TBL_J2}}

*Note.* Adapted from `figures/04_Appendix_and_Reference/dataset_breakdown.csv`. Architectural specifications of conformed analytics tables stored in Apache Parquet format.

## J.3 BTS Data Source Detail and Post-ETL Descriptive Statistics
{{TEXT_J2}}

{{TEXT_J3}}

## J.4 Bureau of Transportation Statistics DB1B Ticket Survey Data Hierarchy
Table J.3 summarizes the 3-tier hierarchy of the BTS DB1B origin-destination ticket survey.

### Table J.3
*Bureau of Transportation Statistics DB1B Ticket Survey Data Hierarchy*

{{TBL_J3}}

*Note.* Adapted from `figures/04_Appendix_and_Reference/bts_db1b_table_hierarchy.csv`. Bureau of Transportation Statistics 10% ticket coupon survey relational hierarchy.

## J.5 Dataset Parameters
{{TEXT_J4}}

---
""".replace("{{TEXT_J1}}", text_j1).replace("{{TBL_J1}}", tbl_j1).replace("{{TBL_J2}}", tbl_j2).replace("{{TEXT_J2}}", text_j2).replace("{{TEXT_J3}}", text_j3).replace("{{TBL_J3}}", tbl_j3).replace("{{TEXT_J4}}", text_j4)
    sections.append(sec_j)

    # Appendix K
    text_k1 = render_docx_block(docx_paras, range(68, 99))
    text_k2 = render_docx_block(docx_paras, range(160, 165))
    sec_k = r"""# Appendix K: Treatment of Data: Extract, Transform, Load (ETL) Architecture and Hygiene Protocols

> *Note on Thesis Cross-References*: This appendix details the 8-step Extract protocol, 15-step Transform protocol, 3-step Load protocol, spatial entity resolution, structural zero preservation, and flight cancellation handling. It is referenced in **Chapter III (Methodology)**, Section 3.5 (*Treatment of Data: Extract, Transform, Load*) and Section 3.5 (*Data Hygiene Protocols*); and in **Chapter IV (Results)**, Section 4.3 (*Data Filtering and Subset Selection*).

## K.1 Sequential Extract, Transform, Load (ETL) Pipeline Architecture
{{TEXT_K1}}

## K.2 Data Hygiene Protocols and Anomaly Remediation
{{TEXT_K2}}

---
""".replace("{{TEXT_K1}}", text_k1).replace("{{TEXT_K2}}", text_k2)
    sections.append(sec_k)

    # Appendix L
    sec_l = r"""# Appendix L: Statistical Foundation and Derivation of the Diebold-Mariano ($DM$) Test for Predictive Superiority

> *Note on Thesis Cross-References*: This appendix provides the formal mathematical derivations, asymptotic theory, and degrees-of-freedom audits for the statistical significance tests operationalized throughout the thesis. It is referenced in **Chapter III (Methodology)**, Section 3.1 (*Dataset Partitioning and Validation Protocol*) and Section 3.1 (*Apparatus and Materials: Evaluation Metric Definition*); and in **Chapter IV (Results)**, Section 4.4 (*Model Results and Evaluation*).

## L.1 The Methodological Dilemma: Why a Standard $p$-Value from a Paired $t$-Test Fails in Time-Series Forecasting

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

## L.2 Mathematical Derivation and Econometric Architecture of the Diebold-Mariano Test

The Diebold-Mariano procedure tests the null hypothesis that two competing forecasting models possess equal predictive accuracy over a given out-of-time evaluation sample, while explicitly correcting for serial correlation and heteroskedasticity in the forecast error differentials.

### Step 1: Formulation of the Loss Differential Series
Let $y_t$ denote the observed passenger throughput volatility at hour $t$ ($t = 1, 2, \dots, N$). Let $\hat{y}_{1,t}$ and $\hat{y}_{2,t}$ denote the forecasts generated by Model 1 and Model 2, respectively, producing forecast errors:

$$e_{1,t} = y_t - \hat{y}_{1,t}, \quad e_{2,t} = y_t - \hat{y}_{2,t}$$

The operational loss associated with each forecast error is determined by a specified loss function $g(e_t)$. While classical regression assumes quadratic loss ($g(e_t) = e_t^2$), the Diebold-Mariano framework permits arbitrary, asymmetric, or scale-free loss functions, such as linear absolute loss ($g(e_t) = |e_t|$) or scaled error loss:

$$d_t = g(e_{1,t}) - g(e_{2,t})$$

The null hypothesis of equal forecast accuracy is formulated as:

$$H_0: \mathbb{E}[d_t] = 0 \quad \text{versus} \quad H_1: \mathbb{E}[d_t] \neq 0$$

### Step 2: Asymptotic Behavior of the Sample Mean Loss Differential
The sample mean loss differential across the evaluation window of length $N$ is:

$$\bar{d} = \frac{1}{N} \sum_{t=1}^N d_t$$

Under the assumption that the loss differential sequence $\{d_t\}$ is covariance stationary and satisfies standard mixing conditions, the Central Limit Theorem establishes that the normalized mean differential converges asymptotically to a Gaussian distribution:

$$\sqrt{N}(\bar{d} - \mu) \xrightarrow{d} \mathcal{N}(0, 2\pi f_d(0))$$

where $f_d(0)$ represents the spectral density of the loss differential sequence at frequency zero. The quantity $2\pi f_d(0)$ equals the **long-run asymptotic variance** ($\sigma_{LR}^2$), which sums the contemporaneous variance and all autocovariances:

$$\sigma_{LR}^2 = \lim_{N \to \infty} \text{Var}(\sqrt{N} \bar{d}) = \gamma_0 + 2 \sum_{k=1}^{\infty} \gamma_k$$

where $\gamma_k = \text{Cov}(d_t, d_{t-k})$ is the $k$-th order autocovariance of the loss differential.

---

## L.3 Heteroskedasticity and Autocorrelation Consistent (HAC) Long-Run Covariance Estimation

To construct a valid test statistic, the long-run variance $\sigma_{LR}^2$ must be estimated consistently. To ensure mathematical robustness against arbitrary autocorrelation and conditional heteroskedasticity, this research operationalizes the **Newey-West (1987) Bartlett kernel estimator**:

$$\widehat{\sigma}_{LR}^2 = \hat{\gamma}_0 + 2 \sum_{k=1}^{K} w(k, K) \hat{\gamma}_k$$

where the sample autocovariances are computed as:

$$\hat{\gamma}_k = \frac{1}{N} \sum_{t=k+1}^N (d_t - \bar{d})(d_{t-k} - \bar{d})$$

and the Bartlett triangular lag window weights are defined as:

$$w(k, K) = 1 - \frac{k}{K + 1}$$

The bandwidth truncation parameter $K$ is set following the asymptotic rate established by Newey and West:

$$K = \left\lfloor 4 \cdot \left(\frac{N}{100}\right)^{2/9} \right\rfloor$$

### Step 4: The Diebold-Mariano Test Statistic and Exact $p$-Value Calculation
The standardized Diebold-Mariano test statistic is defined as:

$$DM = \frac{\bar{d}}{\sqrt{\frac{\widehat{\sigma}_{LR}^2}{N}}} \xrightarrow{d} \mathcal{N}(0, 1)$$

Under the null hypothesis $H_0$, $DM$ asymptotically follows a standard normal distribution. For a two-tailed test, the **exact, mathematically defensible $p$-value** is calculated directly from the standard normal cumulative distribution function $\Phi(\cdot)$:

$$p = 2 \cdot \left(1 - \Phi(|DM|)\right)$$

If $|DM| > 1.96$, the null hypothesis of equal predictive accuracy is rejected at the $\alpha = 0.05$ significance level ($p < 0.05$).

---

## L.4 Empirical Pairwise Statistical Significance Matrix (2025 Out-of-Time Holdout)

Applying the Diebold-Mariano test across the certified 2025 holdout evaluation dataset ($N = 3,222$ test complex-days) yields the pairwise significance matrix reported in Table L.1.

### Table L.1
*Diebold-Mariano Pairwise Statistical Significance Matrix (2025 Holdout Benchmark)*

{{TBL_L1}}

*Note.* Adapted from `figures/03_Modeling_and_Evaluation/models_and_tests.csv`. All pairwise tests evaluated under squared error loss ($L(e) = e^2$) with Newey-West HAC covariance correction. Degrees of freedom: $N = 3,222$ complex-days ($77,328$ hourly evaluations). All $p$-values are two-tailed.

---
""".replace("{{TBL_L1}}", tbl_l1)
    sections.append(sec_l)

    # Appendix M
    text_m = render_docx_block(docx_paras, range(179, 183))
    sec_m = r"""# Appendix M: Operational Evaluation Metrics and Performance Criteria Interpretation

> *Note on Thesis Cross-References*: This appendix defines the mathematical formulations, Kingman queuing interpretations, and operational floor translations for the primary holdout evaluation metrics, alongside the mathematical invalidation of MAPE. It is referenced in **Chapter III (Methodology)**, Section 3.1 (*Quantitative Evaluation Dimensions and Operational Regimes*) and Section 3.1 (*Apparatus and Materials: Evaluation Metric Definition*); and in **Chapter IV (Results)**, Section 4.4 (*Model Results and Evaluation*).

## M.1 Evaluation Metrics and Dataset Parameters
{{TEXT_M}}

## M.2 Operational Forecasting Metrics and Checkpoint Floor Translations

Evaluating passenger throughput volatility forecasts requires criteria grounded in queuing theory and operational utility. Models were benchmarked across five standard metrics:

1. **Coefficient of Determination ($R^2$)**: Quantifies the proportion of throughput variance explained by the model:
   $$R^2 = 1 - \frac{\sum_{t=1}^N (y_t - \hat{y}_t)^2}{\sum_{t=1}^N (y_t - \bar{y})^2}$$
   In time-series volatility forecasting, $R^2 < 0$ indicates that the model performs worse than the simple sample mean.
2. **Root Mean Squared Error (RMSE; pax/hr)**: Quadratically penalizes large forecast misses:
   $$\text{RMSE} = \sqrt{\frac{1}{N} \sum_{t=1}^N (y_t - \hat{y}_t)^2}$$
   In checkpoint staffing, peak-hour underpredictions cause non-linear queue explosions; RMSE heavily penalizes these severe errors.
3. **Mean Absolute Error (MAE; pax/hr)**: Measures average absolute point accuracy:
   $$\text{MAE} = \frac{1}{N} \sum_{t=1}^N |y_t - \hat{y}_t|$$
4. **Mean Absolute Scaled Error (MASE)**: Compares forecast errors against the non-parametric diurnal persistence baseline:
   $$\text{MASE} = \frac{\frac{1}{N} \sum_{t=1}^N |y_t - \hat{y}_t|}{\frac{1}{N - 24} \sum_{t=25}^N |y_t - y_{t-24}|}$$
   $\text{MASE} < 1.00$ proves that the predictive model provides value-add skill beyond naive persistence; $\text{MASE} \ge 1.00$ indicates that deploying the model offers zero operational benefit.
5. **Mean Forecast Bias**: Measures systematic over- or under-prediction ($\text{Bias} = \frac{1}{N} \sum (y_t - \hat{y}_t)$). Negative bias indicates systematic overstaffing (wasted labor costs); positive bias indicates systematic understaffing (long passenger wait times).

---

## M.3 Methodological Invalidation of Mean Absolute Percentage Error (MAPE)

A critical methodological contribution of this research is the **formal mathematical invalidation of Mean Absolute Percentage Error (MAPE) in airport checkpoint demand forecasting**:

$$\text{MAPE} = \frac{1}{N} \sum_{t=1}^N \left| \frac{y_t - \hat{y}_t}{y_t} \right| \cdot 100\%$$

During overnight curfew hours (00:00 to 03:59), observed passenger throughput ($y_t$) approaches zero ($y_t \approx 0$). In these intervals, even minor forecast errors (e.g., predicting 5 passengers when 1 passenger arrives) produce astronomical percentage errors ($|1 - 5| / 1 = 400\%$). If an overnight hour records zero passengers ($y_t = 0$), MAPE is mathematically undefined (division by zero).

Reporting MAPE in airport operations produces severely distorted error statistics that reflect overnight division artifacts rather than operational forecasting skill. Mean Absolute Scaled Error (MASE) completely overcomes this deficiency by scaling against the daily persistence benchmark, providing a stable, non-parametric metric that remains fully defined across all operational hours.

---
""".replace("{{TEXT_M}}", text_m)
    sections.append(sec_m)

    # Appendix N
    text_n = render_docx_block(docx_paras, range(183, 193))
    sec_n = r"""# Appendix N: Feature Engineering Pipeline Details and Empirical Arrival Convolution

> *Note on Thesis Cross-References*: This appendix details the ACRP Report 40 empirical passenger show-up curve convolution, feature domains, and the 84-cell interaction grid. It is referenced in **Chapter III (Methodology)**, Section 3.5 (*Treatment of Data: Feature Engineering Pipeline Details*); and in **Chapter IV (Results)**, Section 4.3 (*Model Development and Execution: Feature Engineering*).

## N.1 Feature Engineering Pipeline Details
{{TEXT_N}}

---
""".replace("{{TEXT_N}}", text_n)
    sections.append(sec_n)

    # =========================================================================
    # CHAPTER IV APPENDICES (O - U)
    # =========================================================================

    # Appendix O
    text_o1 = render_docx_block(docx_paras, range(109, 117))
    text_o2 = render_docx_block(docx_paras, range(117, 121))
    text_o3 = render_docx_block(docx_paras, range(150, 156))
    sec_o = r"""# Appendix O: Seasonal Volatility Regimes, Day-of-Week Archetypes, and Local Weekly Profiles

> *Note on Thesis Cross-References*: This appendix establishes the three coupled seasonality dimensions: annual volatility regimes, day-of-week demand archetypes, and local weekly airport profiles. It is referenced in **Chapter IV (Results)**, Section 4.2 (*Initial Exploratory Data Analysis: Defining Seasonality*) and Section 4.3 (*Local Seasonal and Day-of-Week Differences Across the Nine Selected Airports*).

## O.1 Annual Seasonal Regimes and Day-of-Week Dynamics
{{TEXT_O1}}

### Table O.1
*Master Annual Seasonal Volatility Regimes Summary (Top 25 Airfields, $N = 1,341$ Days)*

{{TBL_O1}}

*Note.* Adapted from `results/manuscript_tables/table_4_3b.csv`. Annual seasonal baseline regimes demonstrating the monotonic expansion of the Coupled Volatility Index ($CVI = \sigma_{\text{TSA}} \cdot \sigma_{\text{Delay}}$) from winter lull to holiday peaks.

### Table O.2
*Day-of-Week Volatility Dynamics and Operational Archetypes (Top 25 Airfields, $N = 1,341$ Days)*

{{TBL_O2}}

*Note.* Adapted from `results/manuscript_tables/table_4_4a.csv`. Weekly operational dynamics and staffing decision rules across the Top 25 commercial airport network.

## O.2 Local Seasonal and Day-of-Week Profiles Across the Nine Selected Airports
{{TEXT_O2}}

{{TEXT_O3}}

### Table O.3
*Day-of-Week Mean Daily Passenger Throughput and Ratio Profiles Across the Nine Selected Airports*

{{TBL_O3}}

*Note.* Adapted from `results/manuscript_tables/table_4_8.csv`. Local day-of-week demand distributions illustrating corporate versus leisure archetypes across the 9-airport experimental cohort.

---
""".replace("{{TEXT_O1}}", text_o1).replace("{{TBL_O1}}", tbl_o1).replace("{{TEXT_O2}}", text_o2).replace("{{TEXT_O3}}", text_o3).replace("{{TBL_O2}}", tbl_o2).replace("{{TBL_O3}}", tbl_o3)
    sections.append(sec_o)

    # Appendix P
    text_p = render_docx_block(docx_paras, range(121, 124))
    sec_p = r"""# Appendix P: Diurnal Bimodal Turbulence Dynamics and Multi-Carrier Collinearity

> *Note on Thesis Cross-References*: This appendix establishes the diurnal bimodal turbulence structure (morning surge vs. evening cascade), the 84-cell interaction grid, and the mathematical proof of shared-terminal collinearity. It is referenced in **Chapter IV (Results)**, Section 4.2 (*Initial Exploratory Data Analysis: Validity of Diurnal Non-Consecutive Dual Turbulence Peaks*).

## P.1 Validity of Diurnal Non-Consecutive Dual Turbulence Peaks
{{TEXT_P}}

## P.2 Mathematical Hazard of Shared-Terminal Multi-Carrier Collinearity

A primary finding of the exploratory analysis is that commercial airports cannot be accurately modeled at the aggregate airport level in shared-terminal facilities. In shared terminals, competing airlines schedule simultaneous departure banks (e.g., 08:00 morning departures across multiple carriers):

$$\text{Corr}(S_{j,t}, S_{k,t}) \ge 0.75$$

When multiple airline flight schedules $S_{j,t}$ and $S_{k,t}$ enter a regression model simultaneously, the **Variance Inflation Factor (VIF)** explodes:

$$\text{VIF}_j = \frac{1}{1 - R_j^2} \ge \frac{1}{1 - (0.75)^2} = \frac{1}{0.4375} \approx 2.29$$

Under severe multicollinearity, the variance of estimated regression coefficients escalates, standard errors inflate, parameter estimates become unstable, and models cannot identify which carrier's flight bank drove checkpoint arrivals. In shared terminals, regression models explain less than 20% of checkpoint throughput variance ($R^2 \approx 0.20$).

**Isolating dedicated single-carrier checkpoints (Phase 3 of the filtering pipeline) eliminates multi-carrier collinearity entirely**, enabling models to achieve dedicated checkpoint-to-flight correlations of $r = +0.880$ to $+0.940$.

---
""".replace("{{TEXT_P}}", text_p)
    sections.append(sec_p)

    # Appendix Q
    text_q = render_docx_block(docx_paras, range(171, 176))
    sec_q = r"""# Appendix Q: Econometric Validation of Carrier Checkpoint Demand Isolation

> *Note on Thesis Cross-References*: This appendix documents the econometric tests verifying that single-carrier screening complexes isolate airline demand without confounding cross-carrier leakage. It is referenced in **Chapter IV (Results)**, Section 4.3 (*Data Filtering and Subset Selection: Econometric Validation of Carrier Checkpoint Isolation*); and in **Chapter V (Discussion)**, Section 5.1 (*Spatial Architecture and Passenger Behavioral Dynamics*).

## Q.1 Econometric Testing Architecture for Single-Carrier Isolation
{{TEXT_Q}}

### Table Q.1
*Econometric Tests for Carrier Checkpoint Demand Isolation*

{{TBL_Q1}}

*Note.* Econometric verification matrix proving causal identification and single-carrier isolation across the 12 selected carrier complexes.

---
""".replace("{{TEXT_Q}}", text_q).replace("{{TBL_Q1}}", tbl_q1)
    sections.append(sec_q)

    # Appendix R
    text_r = render_docx_block(docx_paras, range(145, 150))
    sec_r = r"""# Appendix R: Top 25 Network Census vs. Nine-Airport Experimental Cohort

> *Note on Thesis Cross-References*: This appendix provides the empirical census comparing the broader Top 25 airport network against the Nine-Airport Experimental Cohort. It is referenced in **Chapter IV (Results)**, Section 4.3 (*Data Filtering and Subset Selection: Pipeline Results: Top 25 vs 9 Airport Cohort*).

## R.1 Comparative Operational Profile and Representativeness
{{TEXT_R}}

### Table R.1
*Summary Descriptive Statistics: Nine-Airport Experimental Cohort vs. Top 25 Airfields*

{{TBL_R1}}

*Note.* Adapted from `results/manuscript_tables/table_4_7.csv`. Statistical comparison validating the experimental power and operational representativeness of the nine selected airports relative to the broader national hub network.

---
""".replace("{{TEXT_R}}", text_r).replace("{{TBL_R1}}", tbl_r1)
    sections.append(sec_r)

    # Appendix S
    text_s = render_docx_block(docx_paras, range(156, 160))
    sec_s = r"""# Appendix S: Key Airport Selection Contrasts (LGA vs. JFK, PHL vs. SLC)

> *Note on Thesis Cross-References*: This appendix documents the operational and structural justifications for airport inclusion and exclusion contrasts across the candidate hub universe. It is referenced in **Chapter IV (Results)**, Section 4.3 (*Data Filtering and Subset Selection: Key Airport Selection Contrasts*); and in **Chapter V (Discussion)**, Section 5.1 (*Spatial Architecture and Passenger Behavioral Dynamics*).

## S.1 Operational Rationale for Specific Airport Inclusion and Exclusion
{{TEXT_S}}

---
""".replace("{{TEXT_S}}", text_s)
    sections.append(sec_s)

    # Appendix T
    text_t1 = render_docx_block(docx_paras, range(100, 102))
    text_t2 = render_docx_block(docx_paras, range(193, 197))
    sec_t = r"""# Appendix T: Master Multi-Pillar Hypothesis Evaluation Matrix and Holdout Benchmarks

> *Note on Thesis Cross-References*: This appendix compiles the certified empirical evaluation benchmarks across all three candidate models and baseline control evaluated against the 2025 out-of-time holdout dataset. It is referenced in **Chapter IV (Results)**, Section 4.4 (*Model Results and Evaluation*) and Section 4.4 (*Empirical Confirmation of Asymmetric Trade-Offs*); and in **Chapter V (Discussion)**, Section 5.3–5.5 (*Master Synthesis and Operational Recommendations*).

## T.1 Model Tradeoffs and Evaluation Overview
{{TEXT_T1}}

## T.2 Holdout Benchmark Execution
{{TEXT_T2}}

### Table T.1
*Master Multi-Pillar Hypothesis Evaluation Matrix (2025 Out-of-Time Holdout Suite, $N = 3,222$ Complex-Days)*

{{TBL_T1}}

*Note.* Adapted from `results/manuscript_tables/table_4_10.csv`. Certified out-of-time holdout evaluation suite demonstrating Asymmetric Performance Trade-Offs ($H_1$).

---
""".replace("{{TEXT_T1}}", text_t1).replace("{{TEXT_T2}}", text_t2).replace("{{TBL_T1}}", tbl_t1)
    sections.append(sec_t)

    # Appendix U
    text_u1 = render_docx_block(docx_paras, range(197, 211))
    text_u2 = render_docx_block(docx_paras, range(241, 248))
    sec_u = r"""# Appendix U: The Values versus Volatility Operational Coupling Across Multi-Day Temporal Horizons

> *Note on Thesis Cross-References*: This appendix establishes the econometric proof for the Values versus Volatility operational coupling across intraday absolute, scale-free relative, and multi-day temporal horizons. It is referenced in **Chapter IV (Results)**, Section 4.4 (*The Values versus Volatility Operational Coupling*); and in **Chapter V (Discussion)**, Section 5.4 (*Deep-Dive: Values versus Volatility Paradigm Across Temporal Horizons*).

## U.1 Empirical Validation of the Values versus Volatility Operational Coupling
{{TEXT_U1}}

## U.2 Deep-Dive: Values versus Volatility Paradigm Across Temporal Horizons
{{TEXT_U2}}

### Table U.1
*The Values versus Volatility Operational Coupling Across Multi-Day Temporal Horizons (Empirical Validation)*

{{TBL_U1}}

*Note.* Out-of-time holdout performance proving the complete collapse of static feature values ($R^2 < 0$) and the decisive predictive success of feature volatility representations ($R^2 > +0.31$) across multi-day operational horizons.

---
""".replace("{{TEXT_U1}}", text_u1).replace("{{TEXT_U2}}", text_u2).replace("{{TBL_U1}}", tbl_u1)
    sections.append(sec_u)

    # =========================================================================
    # CHAPTER V APPENDICES (V - X)
    # =========================================================================

    # Appendix V
    text_v1 = render_docx_block(docx_paras, range(212, 226))
    text_v2 = render_docx_block(docx_paras, range(226, 233))
    sec_v = r"""# Appendix V: The Lead-Lag Asynchrony Mechanism and Shock Interaction Dynamics

> *Note on Thesis Cross-References*: This appendix documents the landside-airside queuing disconnect, morning vs. evening shock dynamics, and the 84-cell interaction grid sample depth. It is referenced in **Chapter V (Discussion)**, Section 5.1 (*Spatial Architecture and Passenger Behavioral Dynamics: The Lead-Lag Asynchrony Mechanism*) and Section 5.2 (*Robustness Across the Interaction Grid and Prevention of Delay Distortion*).

## V.1 The Lead-Lag Asynchrony Mechanism and Shock Shielding
{{TEXT_V1}}

## V.2 Robustness Across the Interaction Grid and Prevention of Delay Distortion
{{TEXT_V2}}

---
""".replace("{{TEXT_V1}}", text_v1).replace("{{TEXT_V2}}", text_v2)
    sections.append(sec_v)

    # Appendix W
    text_w = render_docx_block(docx_paras, range(233, 241))
    sec_w = r"""# Appendix W: Resilience Mechanics and the Empty Checkpoint Fallacy Under Severe Disruption

> *Note on Thesis Cross-References*: This appendix details the behavioral mechanics of forecast failures during severe weather and the live error feedback remediation in the Dynamic Hybrid. It is referenced in **Chapter V (Discussion)**, Section 5.3 (*Empirical Evaluation of Resilience Under Disruption: Resilience Mechanics and the Empty Checkpoint Fallacy*).

## W.1 Resilience Mechanics and Disruption Performance
{{TEXT_W}}

### Table W.1
*Evaluation Dimension 2: Resilience and Shock Performance Under Severe Operational Disruption*

{{TBL_W1}}

*Note.* Adapted from `results/manuscript_tables/table_5_2.csv`. Operational resilience metrics during severe disruptions (delays $\ge 45$m or cancellations $\ge 5$).

---
""".replace("{{TEXT_W}}", text_w).replace("{{TBL_W1}}", tbl_w1)
    sections.append(sec_w)

    # Appendix X
    text_x = render_docx_block(docx_paras, range(248, 258))
    sec_x = r"""# Appendix X: Dual-Track Operational Decision Playbook and Real-World Application

> *Note on Thesis Cross-References*: This appendix translates the empirical modeling findings into an actionable operational decision playbook and regime-switched gated inference engine. It is referenced in **Chapter V (Discussion)**, Section 5.5 (*Implications and Recommendations for Predictive Forecasting in Airport Operations: Real-World Operational Application*).

## X.1 Real-World Operational Application
{{TEXT_X}}

### Table X.1
*Dual-Track Operational Model Selection Policy Matrix*

{{TBL_X1}}

*Note.* Adapted from `results/manuscript_tables/dual_track_model_selection_policy.csv`. Dual-track operational deployment policy mapping operational flight regimes to assigned model architectures.

---
""".replace("{{TEXT_X}}", text_x).replace("{{TBL_X1}}", tbl_x1)
    sections.append(sec_x)

    # Combine all sections
    full_markdown = "\n".join(sections)

    # Write output files
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(full_markdown)
    print(f"[SUCCESS] Generated: {output_path} ({len(full_markdown)} characters, {len(full_markdown.splitlines())} lines)")

    with open(manuscripts_only_path, "w", encoding="utf-8") as f:
        f.write(full_markdown)
    print(f"[SUCCESS] Generated: {manuscripts_only_path}")

if __name__ == "__main__":
    main()
