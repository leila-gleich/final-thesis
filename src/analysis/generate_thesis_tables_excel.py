"""
src/analysis/generate_thesis_tables_excel.py
---------------------------------------------
Generates the master multi-tab Excel workbook `thesis_tables.xlsx` formatted strictly
according to APA Style (7th ed.) as demonstrated in `results/sample-tables.docx`
and the reference template tab `table-format`:

1. No table filters or dropdown arrows (no ListObjects / auto-filters).
2. Clean APA horizontal rule boundaries:
   - Header row: thin horizontal rule above (top) and below (bottom).
   - Data rows: no internal horizontal or vertical gridlines.
   - Last data row: thin horizontal rule below (bottom).
   - No background fills or zebra striping (clean white/transparent).
3. First sheet: 'Contents' interactive linked navigation sheet with clickable links.
4. Second sheet: 'table-format' reference example tab.
5. All 16 empirical manuscript tables from Chapter 4 and Chapter 5 using short names.
6. Companion Dual-Track Operational Model Selection Policy (`dual_track_policy`).

Outputs to:
- results/thesis_tables.xlsx
- results/manuscript_tables/thesis_tables.xlsx
"""

import csv
from pathlib import Path
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

# Directory resolution
BASE_DIR = Path(__file__).resolve().parent.parent.parent
RESULTS_DIR = BASE_DIR / "results"
MANUSCRIPT_TABLES_DIR = RESULTS_DIR / "manuscript_tables"
TABLES_DIR = RESULTS_DIR / "tables"

# Comprehensive metadata catalog for all tables
TABLE_CATALOG = [
    {
        "table_id": "Table 4.1",
        "short_name": "table_4_1",
        "csv_file": "table_4_1.csv",
        "title": "Master Post-ETL Multi-Source Data Foundation Census (Full Candidate Commercial Network)",
        "chapter": "Chapter 4: Results",
        "focus": "Census of 4 conformed federal feeds (TSA FOIA, BTS OTP, BTS T-100, BTS DB1B) covering 42,062,039 records",
        "dimension": "Data Foundation & ETL Census",
        "companion_wb": "01_top25_clustering.xlsx",
        "note": "Note. Master census of all candidate commercial airfields across the four conformed federal data feeds (TSA FOIA, BTS OTP, BTS T-100, BTS DB1B). Total conformed analytical database size: 42,062,039 records."
    },
    {
        "table_id": "Table 4.2",
        "short_name": "table_4_2",
        "csv_file": "table_4_2.csv",
        "title": "Post-ETL Master Summary Descriptive Statistics (Top 25 Cleaned Data Warehouse)",
        "chapter": "Chapter 4: Results",
        "focus": "Master descriptive moments (mean, std dev, median, IQR, skewness, kurtosis) across all operational variables",
        "dimension": "Descriptive Statistics",
        "companion_wb": "01_top25_clustering.xlsx",
        "note": "Note. Parametric and non-parametric descriptive statistics across 1,341 post-demarcation days (May 1, 2022 to December 31, 2025) across the Top 25 airfields. Primary dependent target: hourly throughput volatility (sigma_TSA,hr)."
    },
    {
        "table_id": "Table 4.3a",
        "short_name": "table_4_3a",
        "csv_file": "table_4_3a.csv",
        "title": "Post-Pandemic Temporal Demarcation Evaluation Across the Top 25 Network",
        "chapter": "Chapter 4: Results",
        "focus": "Comparison of Candidate A (Mature Post-Pandemic) and Candidate B (Early Post-Mask Regime; Selected, 44 months)",
        "dimension": "Temporal Demarcation",
        "companion_wb": "top25_seasonality_regimes_and_events.xlsx",
        "note": "Note. Empirical evaluation of post-pandemic temporal demarcation regimes. Candidate B (May 1, 2022 to December 31, 2025; 44 months, N = 1,341 days) was formally selected for maximum statistical power while preserving structural stability."
    },
    {
        "table_id": "Table 4.3b",
        "short_name": "table_4_3b",
        "csv_file": "table_4_3b.csv",
        "title": "Master Annual Seasonal Volatility Regimes Summary (Top 25 Airfields)",
        "chapter": "Chapter 4: Results",
        "focus": "Annual seasonal volatility regimes (Off-Peak, Mid-Peak, Peak, Holiday) across 1,341 post-demarcation days",
        "dimension": "Seasonality & Volatility Regimes",
        "companion_wb": "season-analysis.xlsx",
        "note": "Note. Master annual seasonal volatility regimes across 1,341 post-demarcation calendar days across the Top 25 airfields. CV_hr represents the scale-free coefficient of variation of hourly throughput."
    },
    {
        "table_id": "Table 4.4a",
        "short_name": "table_4_4a",
        "csv_file": "table_4_4a.csv",
        "title": "Day-of-Week Volatility Dynamics and Operational Archetypes (Top 25 Airfields)",
        "chapter": "Chapter 4: Results",
        "focus": "Weekly cyclical dynamics and operational archetypes across Monday through Sunday",
        "dimension": "Weekly Cyclical Dynamics",
        "companion_wb": "season-analysis.xlsx",
        "note": "Note. Day-of-week volatility dynamics aggregated across 1,341 calendar days and Top 25 airfields. N = 191 to 192 observations per day of week. CV represents the scale-free coefficient of variation."
    },
    {
        "table_id": "Table 4.5",
        "short_name": "table_4_5",
        "csv_file": "table_4_5.csv",
        "title": "Master Cross-Dataset Econometric Relationships (Top 25 Airfields)",
        "chapter": "Chapter 4: Results",
        "focus": "Econometric coupling between TSA checkpoint volumes and BTS OTP delays/capacity across 12 operational dimensions",
        "dimension": "Econometric Coupling",
        "companion_wb": "01_top25_clustering.xlsx",
        "note": "Note. Econometric coupling between flight operational features and checkpoint throughput volatility. Checkpoint arrival volatility is coupled with departure delay volatility (r = +0.4373, p < 0.05), while static delay minutes show no correlation (r = -0.062, p = 0.77)."
    },
    {
        "table_id": "Table 4.6",
        "short_name": "table_4_6",
        "csv_file": "table_4_6.csv",
        "title": "The Nine-Airport Experimental Cohort Factorial Specification",
        "chapter": "Chapter 4: Results",
        "focus": "Balanced 4x4 factorial design across 12 carrier-exclusive complexes at 9 hubs (BOS, DFW, DTW, EWR, IAH, LAX, LGA, ORD, PHL)",
        "dimension": "Experimental Cohort Design",
        "companion_wb": "02_4tier_filtering.xlsx",
        "note": "Note. Balanced 4x4 factorial specification establishing the 9-airport experimental cohort across 12 carrier-exclusive complexes, controlling for physical checkpoint topology and hub banking structure."
    },
    {
        "table_id": "Table 4.7",
        "short_name": "table_4_7",
        "csv_file": "table_4_7.csv",
        "title": "Summary Descriptive Statistics: Nine-Airport Experimental Cohort Versus Top 25 Universe",
        "chapter": "Chapter 4: Results",
        "focus": "Formal comparison proving sample representativeness of the 9-airport experimental cohort against the Top 25 universe",
        "dimension": "Sample Representativeness",
        "companion_wb": "02_4tier_filtering.xlsx",
        "note": "Note. Formal Welch's two-sample t-tests demonstrating no statistically significant differences between the 9-airport experimental cohort and the Top 25 airport universe across operational metrics (all p > 0.05)."
    },
    {
        "table_id": "Table 4.8",
        "short_name": "table_4_8",
        "csv_file": "table_4_8.csv",
        "title": "Day-of-Week Mean Daily Passenger Throughput Across the Nine Selected Airports",
        "chapter": "Chapter 4: Results",
        "focus": "Local airport DOW profiles, weekly peak/trough days, and Peak/Trough ratios (highlighting LGA corporate profile = 2.30)",
        "dimension": "Local Airport Demand Profiles",
        "companion_wb": "02_top9_cohort_comprehensive_analysis.xlsx",
        "note": "Note. Mean daily passenger throughput by day of week across the 9 selected commercial hubs, identifying local weekly peak and trough days and peak/trough demand ratios."
    },
    {
        "table_id": "Table 4.9",
        "short_name": "table_4_9",
        "csv_file": "table_4_9.csv",
        "title": "Empirical Lead-Lag Transfer Dynamics (Scheduled Flights Versus Checkpoint Demand)",
        "chapter": "Chapter 4: Results",
        "focus": "Asymmetric correlation and explanatory power across Lag t-1, Same-Hour t, Lead t+1, t+2, t+3, and convolved kernels",
        "dimension": "Lead-Lag Show-Up Dynamics",
        "companion_wb": "03_lead_lag_deconvolution.xlsx",
        "note": "Note. Lead-lag transfer dynamics between scheduled flight departures and checkpoint throughput demand. Peak explanatory power occurs at lead horizons t+1 and t+2; convolved ACRP Report 40 passenger show-up curves achieve R^2 = 0.4985."
    },
    {
        "table_id": "Table 4.10",
        "short_name": "table_4_10",
        "csv_file": "table_4_10.csv",
        "title": "Master Model Benchmark Matrix for TSA Throughput Volatility (2025 Full-Year Out-of-Time Holdout)",
        "chapter": "Chapter 4: Results",
        "focus": "Master benchmark matrix across candidate predictive models and baseline control on 72,053 holdout observations",
        "dimension": "Model Evaluation (Holdout)",
        "companion_wb": "04_model_execution_2025_holdout.xlsx",
        "note": "Note. Primary dependent variable is hourly throughput volatility (sigma_TSA,hr). Full-year 2025 out-of-time holdout (N = 72,053 hourly complex observations). MASE is scaled relative to the Baseline Control daily persistence benchmark (MASE = 1.000)."
    },
    {
        "table_id": "Table 4.11",
        "short_name": "table_4_11",
        "csv_file": "table_4_11.csv",
        "title": "Master Multi-Pillar Hypothesis Evaluation Matrix Across the Four Models (Throughput Volatility)",
        "chapter": "Chapter 4: Results",
        "focus": "Formal empirical hypothesis test matrix across Robustness, Resilience, and Generalizability with explicit targets",
        "dimension": "Hypothesis Testing (H1)",
        "companion_wb": "05_robustness_resilience_generalizability.xlsx",
        "note": "Note. Master multi-pillar hypothesis evaluation matrix across Robustness, Resilience, and Generalizability. Demonstrates asymmetric trade-offs (H1) and confirms the values versus volatility operational coupling."
    },
    {
        "table_id": "Table 5.1",
        "short_name": "table_5_1",
        "csv_file": "table_5_1.csv",
        "title": "Evaluation Dimension 1: Routine Operational Accuracy Across the Candidate Models",
        "chapter": "Chapter 5: Discussion",
        "focus": "Robustness evaluation under nominal flight conditions (RMSE, MASE, stated target MASE < 0.70, Diebold-Mariano test)",
        "dimension": "Dimension 1: Robustness",
        "companion_wb": "05_robustness_resilience_generalizability.xlsx",
        "note": "Note. Dimension 1 (Robustness) nominal baseline: departure delays < 15 min and cancellations = 0. Stated target: MASE_routine < 0.700. Model 3 achieves lowest RMSE (222.1 pax/hr); Model 2 wins Routine Pareto Efficiency (MASE = 0.680-0.700, low compute latency)."
    },
    {
        "table_id": "Table 5.2",
        "short_name": "table_5_2",
        "csv_file": "table_5_2.csv",
        "title": "Evaluation Dimension 2: Resilience and Shock Performance Under Severe Operational Disruption",
        "chapter": "Chapter 5: Discussion",
        "focus": "Resilience evaluation under severe weather ground stops and delay programs (RMSE, MASE, R_MASE ≈ 1.00, TTR < 4.0h)",
        "dimension": "Dimension 2: Resilience",
        "companion_wb": "05_robustness_resilience_generalizability.xlsx",
        "note": "Note. Dimension 2 (Resilience) disruption regime: departure delays >= 45 min or cancellations >= 5. Stated target: R_MASE ≈ 1.00, TTR < 4.0 hours. Model 3 is decisive winner (R_MASE = 1.05, MASE_shock = 0.694, TTR = 2.8 hrs). Pure ML (Model 2) collapses (R = 2.14)."
    },
    {
        "table_id": "Table 5.3",
        "short_name": "table_5_3",
        "csv_file": "table_5_3.csv",
        "title": "Evaluation Dimension 3: Generalizability and Cross-Airport Transfer Performance",
        "chapter": "Chapter 5: Discussion",
        "focus": "Zero-shot spatial transfer evaluation from EWR to LGA without retraining (RMSE, RTR = 1.00, Delta MASE <= 10.0%)",
        "dimension": "Dimension 3: Generalizability",
        "companion_wb": "05_robustness_resilience_generalizability.xlsx",
        "note": "Note. Dimension 3 (Generalizability) zero-shot spatial transfer from Newark (EWR) to LaGuardia (LGA) holding TRACON airspace constant. Stated target: RTR ≈ 1.00, Delta MASE <= 10.0%. Model 1 is decisive winner (RTR = 1.04, Delta MASE = +4.0%). Model 3 fails target (RTR = 1.19, Delta MASE = +21.5%)."
    },
    {
        "table_id": "Table 5.4",
        "short_name": "table_5_4",
        "csv_file": "table_5_4.csv",
        "title": "Master Asymmetric Trade-Off Matrix Across the Candidate Models",
        "chapter": "Chapter 5: Discussion",
        "focus": "Synthesis of architectural trade-offs demonstrating asymmetric performance strengths across the candidate models",
        "dimension": "Architectural Synthesis",
        "companion_wb": "05_robustness_resilience_generalizability.xlsx",
        "note": "Note. Master synthesis of architectural trade-offs confirming Hypothesis 1 (H1). Model 3 wins Robustness and Resilience; Model 1 wins Generalizability; Model 2 wins Routine Pareto Efficiency. No model family is universally dominant."
    },
    {
        "table_id": "Policy 5.1",
        "short_name": "dual_track_policy",
        "csv_file": "dual_track_model_selection_policy.csv",
        "title": "Dual-Track Operational Model Selection Policy",
        "chapter": "Chapter 5: Discussion",
        "focus": "Gated operational deployment rules for Gate 1 (Routine Flow Track -> Model 2) and Gate 2 (Tactical Shock Track -> Model 3)",
        "dimension": "Deployment Policy Matrix",
        "companion_wb": "05_robustness_resilience_generalizability.xlsx",
        "note": "Note. Gated operational deployment rules based on the empirical regime indicator T(h). Gate 1 routes routine flow conditions to Model 2; Gate 2 routes tactical shock states to Model 3."
    }
]

from src.utils.excel_styling import parse_cell_value


def build_thesis_tables_workbook():
    """Builds the APA 7th formatted thesis_tables.xlsx workbook with no filters."""
    print("\n[EXCEL GENERATOR] Building APA-formatted thesis_tables.xlsx (no filters, clean boundary rules)...")
    
    # Check if existing thesis_tables.xlsx has table-format sheet to preserve
    existing_table_format_cells = None
    existing_table_format_heights = {}
    existing_table_format_widths = {}
    existing_wb_path = RESULTS_DIR / "thesis_tables.xlsx"
    if existing_wb_path.exists():
        try:
            prev_wb = openpyxl.load_workbook(existing_wb_path)
            if "table-format" in prev_wb.sheetnames:
                prev_ws = prev_wb["table-format"]
                existing_table_format_cells = []
                for r in range(1, prev_ws.max_row + 1):
                    if prev_ws.row_dimensions[r].height:
                        existing_table_format_heights[r] = prev_ws.row_dimensions[r].height
                    r_data = []
                    for c in range(1, prev_ws.max_column + 1):
                        cell = prev_ws.cell(r, c)
                        r_data.append({
                            "val": cell.value,
                            "font": cell.font,
                            "border": cell.border,
                            "align": cell.alignment
                        })
                    existing_table_format_cells.append(r_data)
                for c in range(1, prev_ws.max_column + 1):
                    col_let = get_column_letter(c)
                    if col_let in prev_ws.column_dimensions:
                        existing_table_format_widths[col_let] = prev_ws.column_dimensions[col_let].width
        except Exception as e:
            print(f"  [NOTE] Could not read existing table-format sheet: {e}")

    wb = openpyxl.Workbook()
    wb.remove(wb.active)  # Remove default blank sheet

    # APA 7th Border Rules (Thin black horizontal lines, no vertical rules)
    thin_black = Side(style="thin", color="000000")
    border_header = Border(top=thin_black, bottom=thin_black)
    border_last_row = Border(bottom=thin_black)
    border_none = Border()

    # APA Typography (Calibri, black, no fill)
    font_toc_title = Font(name="Calibri", size=13, bold=True, color="000000")
    font_toc_sub = Font(name="Calibri", size=10, italic=True, color="555555")
    font_toc_instr = Font(name="Calibri", size=10, bold=False, color="333333")
    
    font_header = Font(name="Calibri", size=11, bold=False, color="000000")
    font_header_bold = Font(name="Calibri", size=11, bold=True, color="000000")
    font_data = Font(name="Calibri", size=11, bold=False, color="000000")
    font_link = Font(name="Calibri", size=10, bold=True, color="000563C1", underline="single")
    font_table_id = Font(name="Calibri", size=11, bold=True, color="000000")
    font_table_title = Font(name="Calibri", size=11, italic=True, color="000000")
    font_note = Font(name="Calibri", size=10, italic=True, color="333333")

    # =========================================================================
    # 1. CREATE 'Contents' SHEET (First Sheet)
    # =========================================================================
    ws_toc = wb.create_sheet(title="Contents")
    ws_toc.views.sheetView[0].showGridLines = True
    ws_toc.freeze_panes = "A6"

    # Title block
    ws_toc["A1"] = "THESIS MASTER EMPIRICAL TABLES CATALOG (thesis_tables.xlsx)"
    ws_toc["A1"].font = font_toc_title
    ws_toc.row_dimensions[1].height = 24

    ws_toc["A2"] = "Evaluating Predictive Techniques to Model Stochastic Airport Passenger Flow | MSAA / Gleich 700B | Leila Gleich"
    ws_toc["A2"].font = font_toc_sub
    ws_toc.row_dimensions[2].height = 18

    ws_toc["A3"] = "Interactive Table Index: Click any Sheet Name or Table ID to navigate directly to that table. Every worksheet includes a '⬅ Return to Table of Contents' link in Cell A1."
    ws_toc["A3"].font = font_toc_instr
    ws_toc.row_dimensions[3].height = 20

    ws_toc.row_dimensions[4].height = 10  # blank buffer

    # TOC Headers (Row 5)
    toc_headers = [
        "Table ID",
        "Sheet Tab (Click to Jump)",
        "Official Manuscript Table Title",
        "Manuscript Chapter",
        "Dimensions",
        "Operational Scope & Core Finding",
        "Evaluation Dimension"
    ]
    ws_toc.row_dimensions[5].height = 26
    for col_idx, h_text in enumerate(toc_headers, 1):
        cell = ws_toc.cell(row=5, column=col_idx, value=h_text)
        cell.font = font_header
        cell.border = border_header
        cell.alignment = Alignment(horizontal="center" if col_idx != 2 else "left", vertical="center", wrap_text=True)

    # Populate TOC rows
    toc_current_row = 6
    
    # Add Reference Template row in TOC
    ws_toc.row_dimensions[toc_current_row].height = 20
    c_ref_id = ws_toc.cell(row=toc_current_row, column=1, value="Template")
    c_ref_id.font = font_link
    c_ref_id.hyperlink = "#'table-format'!A1"
    c_ref_id.alignment = Alignment(horizontal="center", vertical="center")

    c_ref_tab = ws_toc.cell(row=toc_current_row, column=2, value="table-format")
    c_ref_tab.font = font_link
    c_ref_tab.hyperlink = "#'table-format'!A1"
    c_ref_tab.alignment = Alignment(horizontal="left", vertical="center")

    ws_toc.cell(row=toc_current_row, column=3, value="APA Style Reference Template (Demographic Characteristics)").font = font_data
    ws_toc.cell(row=toc_current_row, column=4, value="Results Appendix").font = font_data
    ws_toc.cell(row=toc_current_row, column=5, value="8 rows x 4 cols").font = font_data
    ws_toc.cell(row=toc_current_row, column=6, value="APA 7th Edition Sample Table Template (Clean boundary rules, no filters, no fill)").font = font_data
    ws_toc.cell(row=toc_current_row, column=7, value="Formatting Specification").font = font_data
    for c in range(1, 8):
        ws_toc.cell(row=toc_current_row, column=c).border = border_none
    toc_current_row += 1

    # Populate catalog rows
    for item in TABLE_CATALOG:
        short_name = item["short_name"]
        t_id = item["table_id"]
        csv_path = MANUSCRIPT_TABLES_DIR / item["csv_file"]

        if not csv_path.exists():
            continue

        with open(csv_path, "r", encoding="utf-8") as f:
            reader = list(csv.reader(f))

        num_rows = len(reader) - 1
        num_cols = len(reader[0])
        dim_str = f"{num_rows} rows x {num_cols} cols"

        ws_toc.row_dimensions[toc_current_row].height = 20

        # Col 1: Table ID (Hyperlinked)
        c1 = ws_toc.cell(row=toc_current_row, column=1, value=t_id)
        c1.font = font_link
        c1.hyperlink = f"#'{short_name}'!A1"
        c1.alignment = Alignment(horizontal="center", vertical="center")
        c1.border = border_none

        # Col 2: Sheet Tab (Hyperlinked)
        c2 = ws_toc.cell(row=toc_current_row, column=2, value=short_name)
        c2.font = font_link
        c2.hyperlink = f"#'{short_name}'!A1"
        c2.alignment = Alignment(horizontal="left", vertical="center")
        c2.border = border_none

        # Col 3: Title
        c3 = ws_toc.cell(row=toc_current_row, column=3, value=item["title"])
        c3.font = font_data
        c3.alignment = Alignment(horizontal="left", vertical="center")
        c3.border = border_none

        # Col 4: Chapter
        c4 = ws_toc.cell(row=toc_current_row, column=4, value=item["chapter"])
        c4.font = font_data
        c4.alignment = Alignment(horizontal="center", vertical="center")
        c4.border = border_none

        # Col 5: Dimensions
        c5 = ws_toc.cell(row=toc_current_row, column=5, value=dim_str)
        c5.font = font_data
        c5.alignment = Alignment(horizontal="center", vertical="center")
        c5.border = border_none

        # Col 6: Focus
        c6 = ws_toc.cell(row=toc_current_row, column=6, value=item["focus"])
        c6.font = font_data
        c6.alignment = Alignment(horizontal="left", vertical="center")
        c6.border = border_none

        # Col 7: Dimension
        c7 = ws_toc.cell(row=toc_current_row, column=7, value=item["dimension"])
        c7.font = font_data
        c7.alignment = Alignment(horizontal="center", vertical="center")
        c7.border = border_none

        toc_current_row += 1

    # Bottom border on last row of TOC table
    last_toc_row = toc_current_row - 1
    for c in range(1, 8):
        ws_toc.cell(row=last_toc_row, column=c).border = border_last_row

    # Note below TOC table
    toc_note_row = last_toc_row + 2
    ws_toc.row_dimensions[toc_note_row].height = 22
    c_toc_note = ws_toc.cell(row=toc_note_row, column=1, value="Note. Master empirical table catalog conformed across Chapter IV (Results) and Chapter V (Discussion). Formatted according to APA Style (7th ed.) with horizontal boundary rules and no filter dropdowns.")
    c_toc_note.font = font_note

    # Auto-adjust TOC column widths
    for col in ws_toc.iter_cols(min_row=5, max_row=last_toc_row):
        col_letter = get_column_letter(col[0].column)
        max_len = 0
        for cell in col:
            val_s = str(cell.value or "")
            if len(val_s) > max_len:
                max_len = len(val_s)
        ws_toc.column_dimensions[col_letter].width = max(min(max_len + 4, 60), 12)

    # =========================================================================
    # 2. CREATE / PRESERVE 'table-format' REFERENCE SHEET
    # =========================================================================
    ws_fmt = wb.create_sheet(title="table-format")
    ws_fmt.views.sheetView[0].showGridLines = True

    # Row 1: Return link
    ws_fmt.row_dimensions[1].height = 20
    c_back_fmt = ws_fmt.cell(row=1, column=1, value="⬅ Return to Table of Contents")
    c_back_fmt.font = font_link
    c_back_fmt.hyperlink = "#'Contents'!A1"

    if existing_table_format_cells:
        # Replicate existing table-format cells
        for r_idx, r_data in enumerate(existing_table_format_cells, 1):
            if r_idx in existing_table_format_heights:
                ws_fmt.row_dimensions[r_idx].height = existing_table_format_heights[r_idx]
            for c_idx, c_info in enumerate(r_data, 1):
                if r_idx == 1:
                    continue  # preserve Return link
                target_cell = ws_fmt.cell(row=r_idx, column=c_idx, value=c_info["val"])
                if c_info["font"]:
                    target_cell.font = Font(
                        name=c_info["font"].name, size=c_info["font"].size,
                        bold=c_info["font"].bold, italic=c_info["font"].italic,
                        color=c_info["font"].color
                    )
                if c_info["border"]:
                    target_cell.border = Border(
                        top=c_info["border"].top, bottom=c_info["border"].bottom,
                        left=c_info["border"].left, right=c_info["border"].right
                    )
                if c_info["align"]:
                    target_cell.alignment = Alignment(
                        horizontal=c_info["align"].horizontal,
                        vertical=c_info["align"].vertical
                    )
        for col_let, w in existing_table_format_widths.items():
            ws_fmt.column_dimensions[col_let].width = w
    else:
        # Default fallback sample table
        ws_fmt.row_dimensions[2].height = 28
        sample_headers = ["Baseline characteristic", "Guided self-help", "Unguided self-help", "Wait-list control"]
        for c_idx, h in enumerate(sample_headers, 1):
            cell = ws_fmt.cell(row=2, column=c_idx, value=h)
            cell.font = font_header
            cell.border = border_header
        
        sample_rows = [
            ["\u2003Female", 25, 50, 20],
            ["\u2003Male", 25, 50, 30],
            ["\u2003Single", 13, 26, 11],
            ["\u2003Married/partnered", 35, 70, 38],
            ["\u2003Divorced/widowed", 1, 2, 1],
            ["\u2003Other", 1, 1, 0],
            ["Cohabitating", 37, 74, 36]
        ]
        for r_offset, r_vals in enumerate(sample_rows, 3):
            ws_fmt.row_dimensions[r_offset].height = 20
            is_last = (r_offset == 2 + len(sample_rows))
            for c_idx, v in enumerate(r_vals, 1):
                cell = ws_fmt.cell(row=r_offset, column=c_idx, value=v)
                cell.font = font_data
                cell.border = border_last_row if is_last else border_none
                cell.alignment = Alignment(horizontal="left" if c_idx == 1 else "center", vertical="center")
        for col_c in range(1, 5):
            ws_fmt.column_dimensions[get_column_letter(col_c)].width = 22.0

    # =========================================================================
    # 3. CREATE INDIVIDUAL TABLE WORKSHEETS (APA 7th Format, No Filters)
    # =========================================================================
    for item in TABLE_CATALOG:
        short_name = item["short_name"]
        t_id = item["table_id"]
        csv_path = MANUSCRIPT_TABLES_DIR / item["csv_file"]

        if not csv_path.exists():
            continue

        with open(csv_path, "r", encoding="utf-8") as f:
            reader = list(csv.reader(f))

        headers = reader[0]
        data_rows = reader[1:]
        num_rows = len(data_rows)
        num_cols = len(headers)

        ws_t = wb.create_sheet(title=short_name)
        ws_t.views.sheetView[0].showGridLines = True
        ws_t.freeze_panes = "A6"

        # Explicitly ensure NO Table objects and NO auto-filter
        ws_t.tables.clear()
        ws_t.auto_filter.ref = None

        # Row 1: Back link to Table of Contents
        ws_t.row_dimensions[1].height = 20
        c_back = ws_t.cell(row=1, column=1, value="⬅ Return to Table of Contents")
        c_back.font = font_link
        c_back.hyperlink = "#'Contents'!A1"
        c_back.alignment = Alignment(horizontal="left", vertical="center")

        # Row 2: Table ID (APA 7th: Line 1 in Bold)
        ws_t.row_dimensions[2].height = 22
        c_tid = ws_t.cell(row=2, column=1, value=t_id)
        c_tid.font = font_table_id
        c_tid.alignment = Alignment(horizontal="left", vertical="center")

        # Row 3: Table Title (APA 7th: Line 2 in Italic)
        ws_t.row_dimensions[3].height = 22
        c_ttitle = ws_t.cell(row=3, column=1, value=item["title"])
        c_ttitle.font = font_table_title
        c_ttitle.alignment = Alignment(horizontal="left", vertical="center")

        ws_t.row_dimensions[4].height = 10  # Blank spacing buffer

        # Row 5: Column Headers (APA 7th: Thin border top and bottom, no fill)
        ws_t.row_dimensions[5].height = 28
        for c_idx, h_text in enumerate(headers, 1):
            cell = ws_t.cell(row=5, column=c_idx, value=h_text)
            cell.font = font_header
            cell.border = border_header
            # Col 1 left-aligned; all other columns centered
            align_h = "left" if c_idx == 1 else "center"
            cell.alignment = Alignment(horizontal=align_h, vertical="center", wrap_text=True)

        # Rows 6+: Data Rows (APA 7th: No internal horizontal rules, no vertical rules, no fill)
        for r_offset, r_vals in enumerate(data_rows, 0):
            current_row = 6 + r_offset
            ws_t.row_dimensions[current_row].height = 20
            is_last_data_row = (r_offset == num_rows - 1)

            for c_idx, raw_val in enumerate(r_vals, 1):
                val, num_fmt, align_h = parse_cell_value(raw_val)
                cell = ws_t.cell(row=current_row, column=c_idx, value=val)
                cell.font = font_data
                cell.alignment = Alignment(horizontal=align_h, vertical="center")

                # Boundary rule on last data row only
                if is_last_data_row:
                    cell.border = border_last_row
                else:
                    cell.border = border_none

                if num_fmt:
                    cell.number_format = num_fmt

        # Row (6 + num_rows + 1): APA Note (Below table, italic, no border)
        note_row_idx = 6 + num_rows + 1
        ws_t.row_dimensions[note_row_idx].height = 24
        c_note = ws_t.cell(row=note_row_idx, column=1, value=item["note"])
        c_note.font = font_note
        c_note.alignment = Alignment(horizontal="left", vertical="center")

        # Auto-adjust column widths
        for col in ws_t.iter_cols(min_row=5, max_row=5 + num_rows):
            col_letter = get_column_letter(col[0].column)
            max_len = 0
            for cell in col:
                val_s = str(cell.value or "")
                if len(val_s) > max_len:
                    max_len = len(val_s)
            ws_t.column_dimensions[col_letter].width = max(min(max_len + 4, 60), 14)

    # =========================================================================
    # 4. SAVE WORKBOOK TO TARGET DIRECTORIES
    # =========================================================================
    out_paths = [
        RESULTS_DIR / "thesis_tables.xlsx",
        MANUSCRIPT_TABLES_DIR / "thesis_tables.xlsx",
        TABLES_DIR / "thesis_tables.xlsx"
    ]

    for p in out_paths:
        p.parent.mkdir(parents=True, exist_ok=True)
        wb.save(p)
        print(f"  -> Successfully saved APA formatted workbook: {p}")

    print(f"[COMPLETE] Master thesis_tables.xlsx formatted with {len(TABLE_CATALOG)} tables + template (no filters, APA boundary rules).")
    return out_paths


if __name__ == "__main__":
    build_thesis_tables_workbook()
