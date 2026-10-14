"""
build_unified_manuscripts.py
============================
Automated pipeline to construct the conformed, authoritative manuscript suite for:
"Evaluating Predictive Techniques to Model Stochastic Airport Passenger Flow"
(Leila Gleich, MSAA / Gleich 700B, Embry-Riddle Aeronautical University).

Outputs in thesis_docs/manuscripts/:
1. Gleich-FinalThesis.docx (Preserved untouched)
2. Master_Appendix_Glossary_Acronyms.docx (Unified Master Appendix, Glossary, and Acronyms Word doc)
3. Chapter_I_Introduction.md
4. Chapter_II_Literature_Review.md
5. Chapter_III_Methodology.md
6. Chapter_IV_Findings_Discussion_Conclusions.md
7. Gleich-FinalThesis.md (Unified APA 7th Edition Markdown Master of the complete thesis)
"""

import os
import sys
import re
import subprocess
from pathlib import Path
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import qn, nsdecls

BASE_DIR = Path(__file__).resolve().parent.parent.parent
MANUSCRIPTS_DIR = BASE_DIR / "thesis_docs" / "manuscripts"
TEMPLATES_DIR = BASE_DIR / "thesis_docs" / "templates"
FIGURES_DIR = BASE_DIR / "thesis_docs" / "figures"

# Import acronyms and categories from generate_acronyms_docx
sys.path.insert(0, str(BASE_DIR / "src" / "manuscripts"))
from generate_acronyms_docx import ACRONYM_DATA, CATEGORIES, set_cell_margins, apply_apa_table_borders, sort_key


def get_git_content(ref_path):
    cmd = ["git", "show", ref_path]
    res = subprocess.run(cmd, cwd=str(BASE_DIR), capture_output=True, text=True, check=True)
    return res.stdout


def build_unified_master_word_doc():
    out_unified_path = MANUSCRIPTS_DIR / "Master_Appendix_Glossary_Acronyms.docx"
    if out_unified_path.exists():
        print(f"Master_Appendix_Glossary_Acronyms.docx already exists ({out_unified_path.stat().st_size} bytes), skipping regeneration.")
        return

    print("Loading base Master Appendix.docx...")
    src_appendix_path = MANUSCRIPTS_DIR / "Master Appendix.docx"
    doc = docx.Document(str(src_appendix_path))

    # Update top heading / metadata paragraphs
    for p in doc.paragraphs[:10]:
        if "MASTER DISSERTATION APPENDIX" in p.text:
            p.text = "MASTER DISSERTATION APPENDIX, GLOSSARY, AND ACRONYM REGISTRY"
            p.runs[0].font.bold = True
            p.runs[0].font.name = "Times New Roman"
        elif "MANUSCRIPT COMPILATION:" in p.text:
            p.text = "MANUSCRIPT COMPILATION: Master Merged Empirical & Methodological Appendices, Technical Glossary, and Acronym Registry"
            p.runs[0].font.name = "Times New Roman"

    # -------------------------------------------------------------
    # PART II: COMPREHENSIVE TECHNICAL GLOSSARY
    # -------------------------------------------------------------
    print("Appending Part II: Technical Glossary...")
    doc.add_page_break()
    p_sec2 = doc.add_paragraph()
    p_sec2.paragraph_format.space_before = Pt(24)
    p_sec2.paragraph_format.space_after = Pt(12)
    p_sec2.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_sec2 = p_sec2.add_run("PART II: COMPREHENSIVE GLOSSARY OF OPERATIONAL AND TECHNICAL TERMS")
    r_sec2.font.name = "Times New Roman"
    r_sec2.font.size = Pt(14)
    r_sec2.font.bold = True

    p_intro = doc.add_paragraph()
    p_intro.paragraph_format.line_spacing = 1.15
    p_intro.paragraph_format.space_after = Pt(8)
    r_intro = p_intro.add_run(
        "This technical glossary defines the commercial aviation operations concepts, federal data systems, "
        "statistical metrics, and predictive modeling methods used across Chapters I through V of this thesis. "
        "In accordance with APA 7th Edition guidelines, entries are grounded in authentic commercial aviation operations, "
        "airline flight scheduling banks, and airport passenger flow dynamics."
    )
    r_intro.font.name = "Times New Roman"
    r_intro.font.size = Pt(11)

    # Fetch glossary entries from local canonical markdown file
    glossary_path = MANUSCRIPTS_DIR / "glossary.md"
    if glossary_path.exists():
        with open(glossary_path, "r", encoding="utf-8") as f:
            glossary_raw = f.read()
    else:
        glossary_raw = get_git_content("5118e9bb:thesis_docs/manuscripts/glossary.md")
    parts = re.split(r"\n(?=### )", glossary_raw)
    raw_entries = parts[1:]
    table_split = re.split(r"\n(?=## Thematic Cross-Reference Matrix)", raw_entries[-1])
    raw_entries[-1] = table_split[0]

    entry_dict = {}
    for e in raw_entries:
        m = re.match(r"### (.*?)\n", e)
        if m:
            entry_dict[m.group(1).strip()] = e.strip()

    # Import category definitions
    from generate_categorized_glossary import main as _  # ensure loadable
    cat_definitions = [
        {
            "title": "Category 1: Aviation Infrastructure, Federal Agencies, and Programs",
            "desc": "Defines physical airport terminal zones, federal regulatory bodies, operational coordination command centers, and traveler security programs governing commercial aviation across the National Airspace System.",
            "terms": [
                "Air Traffic Control (ATC)", "Airport Operations Center (AOC)", "Airside",
                "Credential Authentication Technology (CAT)", "Federal Aviation Administration (FAA)",
                "Federal Security Director (FSD)", "Freedom of Information Act (FOIA)",
                "Ground Delay Program (GDP)", "Landside", "National Airspace System (NAS)",
                "Terminal Radar Approach Control (TRACON)", "Transportation Security Administration (TSA)",
                "Transportation Security Officer (TSO)", "TSA PreCheck", "Ultra-Low-Cost Carrier (ULCC)"
            ]
        },
        {
            "title": "Category 2: Federal Aviation Datasets, Data Hygiene, and Conformance",
            "desc": "Covers official federal aviation data sources, data hygiene protocols, timeline integrity standards, and relational warehouse conformance rules used across the 2019–2025 multi-source study baseline.",
            "terms": [
                "Advance Flight Cancellation", "Airborne Flight Duration", "Available Seats per Route-Month",
                "Bureau of Transportation Statistics (BTS)", "BTS DB1B / DB1C Origin-Destination Ticket Surveys",
                "BTS Form 41 Schedule T-100 Domestic Segment Data", "BTS Form 234 (On-Time Performance / OTP)",
                "Candidate B Demarcation", "Checkpoint Fingerprinting Algorithm", "Flight Departure Delay ($\\text{DepDelay}$)",
                "Lookahead Bias", "Operational Separation Buffer", "Overnight Structural Zero",
                "Runway Taxi-Out Queue Time", "Tactical Flight Cancellation"
            ]
        },
        {
            "title": "Category 3: Terminal Queuing Dynamics and Passenger Arrival Behavior",
            "desc": "Details physical, temporal, and behavioral dynamics of passenger movement through airport terminals, including passenger arrival show-up curves, airline flight bank waves, connecting passenger transfers, and queuing bottlenecks.",
            "terms": [
                "Airport Cooperative Research Program (ACRP) Report 40", "Batch Arrival Dynamics",
                "Bimodal Arrival Mixture", "Checkpoint Lane Throughput ($y_{k,l,t}$)",
                "Connecting Passenger Deflator", "Connecting Passenger Ratio", "Convolved Passenger Show-Up Curve",
                "Dedicated Terminal Screening Complex", "Divestiture", "Empty Checkpoint Fallacy",
                "Flight Bank (Departure Wave)", "Hub Disconnect", "Hub-and-Spoke Network",
                "Lead-Lag Asynchrony", "Level of Service (LOS)", "Multi-Carrier Schedule Collinearity",
                "Origin and Destination (O&D)", "Originating Passenger (Local Originating Demand)",
                "Queuing Theory", "Show-Up Curve", "Traffic Intensity ($\\rho(t)$)"
            ]
        },
        {
            "title": "Category 4: Operational Volatility, Seasonality, and Experimental Filtering",
            "desc": "Encompasses mathematical indices, cyclical volatility metrics, and purposive sampling funnels used to quantify airport operational turbulence and isolate unconfounded research cohorts.",
            "terms": [
                "84-Cell Operational Condition Matrix ($\\mathcal{G} = \\mathcal{S} \\times \\mathcal{D} \\times \\mathcal{H}$)",
                "Coefficient of Variation ($CV_{\\text{TSA}}$)", "Consensus Factor Weight ($W_j$)",
                "Coupled Volatility Index ($\\text{CVI}_d$)", "Diurnal Turbulence Shock Index ($\\text{TSI}_t$)",
                "Factorial Experimental Design ($4 \\times 4$)", "Four-Tier Purposive Filtering Pipeline",
                "High-Volatility Convective Season", "Intraday Scale-Free Volatility ($CV_{\\text{TSA, hr}}$)",
                "Multi-Day Rolling Volatility ($\\sigma_{\\text{TSA, 7d}}$)", "Nine-Airport Experimental Cohort",
                "Nominal On-Time Baseline", "Relative Volatility Elasticity ($\\eta_{\\text{vol}}$)",
                "Routine Daily Operations", "Throughput Volatility ($\\sigma_{\\text{TSA}}$)",
                "Top 25 Commercial Airport Network", "Values versus Volatility Paradigm"
            ]
        },
        {
            "title": "Category 5: Predictive Modeling Paradigms and Algorithmic Architectures",
            "desc": "Covers forecasting model families, machine learning regressors, and hybrid frameworks evaluated across the 2025 out-of-time holdout partition.",
            "terms": [
                "4-Model Canonical Evaluation Suite", "Autoregressive Integrated Moving Average (ARIMA / SARIMA / SARIMAX)",
                "Baseline Control Benchmark (Daily Persistence)", "Deterministic Fixed-Lead Operational Baseline (Model 1)",
                "Dynamic Two-Stage Hybrid Model (Model 3)", "Feature Engineering Pipeline",
                "Gradient-Boosted Decision Trees (LightGBM)", "Negative Binomial Regressor",
                "Poisson Regression", "Random Forest Regressor",
                "Regime-Switched Gated Inference Engine", "Supervised Machine Learning Model (Model 2)",
                "Tweedie Compound Poisson Gradient-Boosted Regressor"
            ]
        },
        {
            "title": "Category 6: Econometric Evaluation Metrics, Hypothesis Testing, and Statistics",
            "desc": "Encompasses formal mathematical error criteria, asymptotic hypothesis tests, and operational performance metrics defining the multi-pillar evaluation triad (Robustness, Resilience, Generalizability).",
            "terms": [
                "Absolute Percentage Error (APE)", "Change in MASE on Transfer ($\\Delta\\text{MASE}$)",
                "Coefficient of Determination ($R^2$)", "Conformal Quantile Prediction Bounds",
                "Diebold-Mariano (DM) Forecast Accuracy Test", "Disruption Error Multiplier ($R_{\\text{MASE}}$)",
                "Empirical Coverage Rate", "Heavy-Traffic Queuing Approximation (Kingman / Allen-Cunneen)",
                "Heteroskedasticity and Autocorrelation Consistent (HAC) Variance", "Mean Absolute Error (MAE)",
                "Mean Absolute Scaled Error (MASE)", "Normalized Root Mean Squared Error (NRMSE)",
                "Relative Transfer Ratio (RTR)", "Root Mean Squared Error (RMSE)",
                "Time-to-Recovery (TTR)", "Uncalibrated Cross-Airport Deployment (Zero-Shot Portability)"
            ]
        }
    ]

    for cat in cat_definitions:
        p_c = doc.add_paragraph()
        p_c.paragraph_format.space_before = Pt(14)
        p_c.paragraph_format.space_after = Pt(4)
        r_c = p_c.add_run(cat["title"])
        r_c.font.name = "Times New Roman"
        r_c.font.size = Pt(12)
        r_c.font.bold = True

        p_cd = doc.add_paragraph()
        p_cd.paragraph_format.space_before = Pt(0)
        p_cd.paragraph_format.space_after = Pt(6)
        r_cd = p_cd.add_run(cat["desc"])
        r_cd.font.name = "Times New Roman"
        r_cd.font.size = Pt(10)
        r_cd.font.italic = True

        for t in cat["terms"]:
            raw_entry = entry_dict.get(t)
            if not raw_entry:
                for k, v in entry_dict.items():
                    if t.split("(")[0].strip().lower() in k.lower():
                        raw_entry = v
                        break
            if not raw_entry:
                continue

            lines = raw_entry.splitlines()
            title_line = lines[0].replace("### ", "").strip()
            body_text = " ".join([l.strip() for l in lines[1:] if l.strip()])

            p_t = doc.add_paragraph()
            p_t.paragraph_format.space_before = Pt(4)
            p_t.paragraph_format.space_after = Pt(4)
            p_t.paragraph_format.line_spacing = 1.15

            r_title = p_t.add_run(f"{title_line}: ")
            r_title.font.name = "Times New Roman"
            r_title.font.size = Pt(10.5)
            r_title.font.bold = True

            r_body = p_t.add_run(body_text)
            r_body.font.name = "Times New Roman"
            r_body.font.size = Pt(10.5)

    # -------------------------------------------------------------
    # PART III: MASTER ACRONYM REGISTRY
    # -------------------------------------------------------------
    print("Appending Part III: Master Acronym Registry...")
    doc.add_page_break()
    p_sec3 = doc.add_paragraph()
    p_sec3.paragraph_format.space_before = Pt(24)
    p_sec3.paragraph_format.space_after = Pt(12)
    p_sec3.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_sec3 = p_sec3.add_run("PART III: MASTER INDEX OF ACRONYMS AND ABBREVIATIONS")
    r_sec3.font.name = "Times New Roman"
    r_sec3.font.size = Pt(14)
    r_sec3.font.bold = True

    p_t1 = doc.add_paragraph()
    p_t1.paragraph_format.space_before = Pt(12)
    p_t1.paragraph_format.space_after = Pt(2)
    r_t1 = p_t1.add_run("Table 1")
    r_t1.font.name = "Times New Roman"
    r_t1.font.size = Pt(11)
    r_t1.font.bold = True

    p_t1_title = doc.add_paragraph()
    p_t1_title.paragraph_format.space_before = Pt(0)
    p_t1_title.paragraph_format.space_after = Pt(8)
    r_t1_title = p_t1_title.add_run("Master Index of Acronyms, Operational Expansions, and Thesis Applications")
    r_t1_title.font.name = "Times New Roman"
    r_t1_title.font.size = Pt(11)
    r_t1_title.font.italic = True

    # Build Table
    table = doc.add_table(rows=1, cols=4)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.autofit = False

    col_widths = [Inches(1.2), Inches(2.2), Inches(1.8), Inches(4.3)]
    for j, w in enumerate(col_widths):
        table.columns[j].width = w

    headers = [
        "Acronym / Abbreviation",
        "Full Expansion / Stand-For Term",
        "Operational Category",
        "Primary Thesis Application"
    ]
    hdr_cells = table.rows[0].cells
    for j, h in enumerate(headers):
        hdr_cells[j].text = h
        hdr_cells[j].width = col_widths[j]
        set_cell_margins(hdr_cells[j], top=100, bottom=100, left=120, right=120)
        p = hdr_cells[j].paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.LEFT
        for r in p.runs:
            r.font.name = "Times New Roman"
            r.font.size = Pt(10)
            r.font.bold = True

    for it in ACRONYM_DATA:
        row_cells = table.add_row().cells
        for j, w in enumerate(col_widths):
            row_cells[j].width = w

        row_cells[0].text = it["acronym"]
        row_cells[1].text = it["full_term"]
        row_cells[2].text = it["category"]
        row_cells[3].text = it["definition"]

        for j in range(4):
            set_cell_margins(row_cells[j], top=70, bottom=70, left=120, right=120)
            p = row_cells[j].paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.LEFT
            for r in p.runs:
                r.font.name = "Times New Roman"
                r.font.size = Pt(9.5)
                if j == 0:
                    r.font.bold = True

    apply_apa_table_borders(table)

    p_note = doc.add_paragraph()
    p_note.paragraph_format.space_before = Pt(6)
    p_note.paragraph_format.space_after = Pt(14)
    r_note = p_note.add_run(
        "Note. All terms and acronyms are grounded in authentic aviation operations, queuing theory, and empirical econometric "
        "modeling across Chapters I through V of this thesis. Primary evaluation models include Baseline Control (Diurnal Persistence), "
        "Model 1 (Deterministic Flight Schedule Model), Model 2 (Supervised Machine Learning Model), and Model 3 (Dynamic Two-Stage "
        "Hybrid Model). Internal variable tags (M0, M1*, M3, M5) are excluded in compliance with repository governance rules."
    )
    r_note.font.name = "Times New Roman"
    r_note.font.size = Pt(9.5)
    r_note.font.italic = True

    out_unified_path = MANUSCRIPTS_DIR / "Master_Appendix_Glossary_Acronyms.docx"
    doc.save(str(out_unified_path))
    print(f"[SUCCESS] Unified Master Word document generated: {out_unified_path}")


def build_markdown_chapters():
    print("Generating the 4 section Markdown files and master Gleich-FinalThesis.md...")

    # 1. Target section files in MANUSCRIPTS_DIR
    ch1_out = MANUSCRIPTS_DIR / "Chapter_I_Introduction.md"
    ch2_out = MANUSCRIPTS_DIR / "Chapter_II_Literature_Review.md"
    ch3_out = MANUSCRIPTS_DIR / "Chapter_III_Methodology.md"
    ch4_out = MANUSCRIPTS_DIR / "Chapter_IV_Findings_Discussion_Conclusions.md"

    if ch1_out.exists() and ch2_out.exists() and ch3_out.exists() and ch4_out.exists():
        print("Loading chapter text directly from existing canonical Markdown manuscripts...")
        with open(ch1_out, "r", encoding="utf-8") as f:
            ch1_text = f.read()
        with open(ch2_out, "r", encoding="utf-8") as f:
            ch2_text = f.read()
        with open(ch3_out, "r", encoding="utf-8") as f:
            ch3_text = f.read()
        with open(ch4_out, "r", encoding="utf-8") as f:
            ch4_5_text = f.read()
    else:
        missing = [str(p.name) for p in [ch1_out, ch2_out, ch3_out, ch4_out] if not p.exists()]
        raise FileNotFoundError(
            f"Canonical markdown manuscript chapters missing in {MANUSCRIPTS_DIR}: {', '.join(missing)}. "
            f"Expected Chapter_I_Introduction.md through Chapter_IV_Findings_Discussion_Conclusions.md."
        )

    # 5. Gleich-FinalThesis.md (The complete manuscript)
    front_matter = """# AN EVALUATION OF PERFORMANCE MEASURES FOR PREDICTIVE APPROACHES TO MODEL TSA THROUGHPUT VOLATILITY

by  
**Leila Gleich**

A Graduate Capstone Project Submitted to the College of Aviation,  
Department of Aeronautics, in Partial Fulfillment  
of the Requirements for the Degree of  
**Master of Science in Aeronautics**  
Embry-Riddle Aeronautical University  
Worldwide Campus  
October 2026

---

### Graduate Capstone Project Approval

This Graduate Capstone Project was prepared under the direction of the candidate’s Graduate Capstone Project Chair, **Mark Miller**, Worldwide Campus and has been approved. It was submitted to the Department of Graduate Studies in partial fulfillment of the requirements for the degree of Master of Science in Aeronautics.

Graduate Capstone Project Chair: Mark Miller  
Date: October 2026

---

### Acknowledgements

I would like to express my sincere appreciation for the opportunities I have had to understand the extent to which airport operations can be improved and to support both local and global aviation communities. I am deeply grateful to my capstone committee and faculty for their guidance, critical review, and encouragement throughout this investigation.

---

### Abstract

**Scholar**: Leila Gleich  
**Title**: An Evaluation of Performance Measures for Predictive Approaches to Model TSA Throughput Volatility  
**Institution**: Embry-Riddle Aeronautical University  
**Degree**: Master of Science in Aeronautics / Aviation Data Analytics  
**Year**: 2026  

This study investigates predictive modeling frameworks to forecast passenger screening throughput volatility at commercial airport security checkpoints. Operating under Kingman's heavy-traffic queuing formula, checkpoint congestion and traveler delays scale quadratically with arrival volatility as checkpoint lane utilization approaches capacity. Using a longitudinal conformed dataset spanning 2019 through 2025 across the Top 25 U.S. commercial airfields, this research isolates 12 carrier-exclusive terminal complexes across a 9-airport experimental cohort to evaluate three candidate operational modeling paradigms (Deterministic Flight Schedule Convolution, Supervised Machine Learning, and Dynamic Two-Stage Hybrid) against an empirical diurnal persistence Baseline Control. The findings decisively demonstrate asymmetric performance trade-offs: while the Two-Stage Hybrid achieves superior routine precision and shock resilience during severe irregular operations, deterministic operational schedules exhibit unmatched cross-facility spatial portability.

---
"""

    full_thesis_text = "\n\n".join([
        front_matter,
        ch1_text,
        "\n---\n",
        ch2_text,
        "\n---\n",
        ch3_text,
        "\n---\n",
        ch4_5_text
    ])

    full_out = MANUSCRIPTS_DIR / "Gleich-FinalThesis.md"
    with open(full_out, "w", encoding="utf-8") as f:
        f.write(full_thesis_text)

    print(f"[SUCCESS] All 4 section MD files and Gleich-FinalThesis.md generated cleanly.")


def cleanup_manuscripts_folder():
    print("Enforcing strict directory purity: only specified files in thesis_docs/manuscripts/...")

    # Relocate templates to thesis_docs/templates/ if present
    if (MANUSCRIPTS_DIR / "templates").exists():
        TEMPLATES_DIR.mkdir(parents=True, exist_ok=True)
        for item in (MANUSCRIPTS_DIR / "templates").iterdir():
            target = TEMPLATES_DIR / item.name
            if not target.exists():
                item.rename(target)
        if (MANUSCRIPTS_DIR / "templates").exists():
            subprocess.run(["rm", "-rf", str(MANUSCRIPTS_DIR / "templates")])

    # Relocate figures to thesis_docs/figures/ if present
    if (MANUSCRIPTS_DIR / "figures").exists():
        FIGURES_DIR.mkdir(parents=True, exist_ok=True)
        for item in (MANUSCRIPTS_DIR / "figures").iterdir():
            target = FIGURES_DIR / item.name
            if not target.exists():
                item.rename(target)
        if (MANUSCRIPTS_DIR / "figures").exists():
            subprocess.run(["rm", "-rf", str(MANUSCRIPTS_DIR / "figures")])

    # Remove precursor / intermediate files
    for extraneous in [
        "Master Appendix.docx",
        "gleich700B_chpIV_chpV_combined.md",
        ".DS_Store"
    ]:
        p = MANUSCRIPTS_DIR / extraneous
        if p.exists():
            if p.is_dir():
                subprocess.run(["rm", "-rf", str(p)])
            else:
                p.unlink()

    # List final contents
    final_files = sorted([f.name for f in MANUSCRIPTS_DIR.iterdir()])
    print("Final contents of thesis_docs/manuscripts/:")
    for f in final_files:
        print(f" - {f}")


if __name__ == "__main__":
    build_unified_master_word_doc()
    build_markdown_chapters()
    cleanup_manuscripts_folder()
