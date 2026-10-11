"""
convert_word_to_apa7_markdown.py
--------------------------------
Converts author Word manuscripts (ChpI v4.docx, ChpII v5.docx, ChpIII v4.docx,
ChpIV v5.docx, ChpV v1.docx) into standardized APA 7th Edition Markdown files.

Outputs:
- thesis_docs/manuscripts/final-thesis-v1/chp1-intro.md
- thesis_docs/manuscripts/final-thesis-v1/chp2-litreview.md
- thesis_docs/manuscripts/final-thesis-v1/chp3-methodology.md
- thesis_docs/manuscripts/final-thesis-v1/chp4-results.md
- thesis_docs/manuscripts/final-thesis-v1/chp5-discussion.md
- thesis_docs/manuscripts/final-thesis-v1/final-thesis-v1.md
- thesis_docs/manuscripts/final-thesis-v1.md
"""

import os
import re
from pathlib import Path
import docx
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent.parent
MANUSCRIPTS_DIR = BASE_DIR / "thesis_docs" / "manuscripts"
FINAL_V1_DIR = MANUSCRIPTS_DIR / "final-thesis-v1"
TABLES_DIR = BASE_DIR / "results" / "manuscript_tables"


def omml_to_latex(elem):
    tag = elem.tag.split('}')[-1]
    if tag == 't':
        return elem.text or ''
    elif tag == 'sSub':
        e = elem.find('{*}e')
        sub = elem.find('{*}sub')
        base_str = omml_to_latex(e) if e is not None else ''
        sub_str = omml_to_latex(sub) if sub is not None else ''
        return f"{base_str}_{{{sub_str}}}"
    elif tag == 'sSup':
        e = elem.find('{*}e')
        sup = elem.find('{*}sup')
        base_str = omml_to_latex(e) if e is not None else ''
        sup_str = omml_to_latex(sup) if sup is not None else ''
        return f"{base_str}^{{{sup_str}}}"
    elif tag == 'sSubSup':
        e = elem.find('{*}e')
        sub = elem.find('{*}sub')
        sup = elem.find('{*}sup')
        base_str = omml_to_latex(e) if e is not None else ''
        sub_str = omml_to_latex(sub) if sub is not None else ''
        sup_str = omml_to_latex(sup) if sup is not None else ''
        return f"{base_str}_{{{sub_str}}}^{{{sup_str}}}"
    elif tag == 'f':
        num = elem.find('{*}num')
        den = elem.find('{*}den')
        num_str = omml_to_latex(num) if num is not None else ''
        den_str = omml_to_latex(den) if den is not None else ''
        return f"\\frac{{{num_str}}}{{{den_str}}}"
    elif tag == 'rad':
        e = elem.find('{*}e')
        e_str = omml_to_latex(e) if e is not None else ''
        return f"\\sqrt{{{e_str}}}"
    elif tag == 'd':
        e = elem.find('{*}e')
        e_str = omml_to_latex(e) if e is not None else ''
        return f"({e_str})"
    else:
        return ''.join(omml_to_latex(c) for c in elem)


def extract_paragraph(p):
    runs_and_math = []
    for child in p._element:
        tag = child.tag.split('}')[-1]
        if tag == 'r':
            t_elems = child.findall('.//{*}t')
            t_text = ''.join([t.text for t in t_elems if t.text])
            if t_text:
                runs_and_math.append(t_text)
        elif tag in ('oMath', 'oMathPara'):
            m_latex = omml_to_latex(child).strip()
            if m_latex:
                m_latex = m_latex.replace('%', '\\%')
                runs_and_math.append(f" ${m_latex}$ ")
    
    text = ''.join(runs_and_math).strip()
    text = re.sub(r' +', ' ', text)
    text = text.replace('\xa0', ' ')
    style = p.style.name if p.style else 'Normal'
    is_bold = any(r.bold for r in p.runs if r.text and r.text.strip())
    is_italic = any(r.italic for r in p.runs if r.text and r.text.strip())
    return style, text, is_bold, is_italic


def format_apa7_table(csv_path, table_id, title, note=None):
    if not os.path.exists(csv_path):
        return f"\n{table_id}  \n*{title}*\n\n*(Table asset pending generation at {csv_path})*\n"
    df = pd.read_csv(csv_path)
    lines = [f"\n{table_id}  ", f"*{title}*", ""]
    header = "| " + " | ".join(str(c) for c in df.columns) + " |"
    sep = "| " + " | ".join([":---"] * len(df.columns)) + " |"
    lines.extend([header, sep])
    for _, row in df.iterrows():
        r_str = "| " + " | ".join(str(v).replace("\n", " ").strip() for v in row) + " |"
        lines.append(r_str)
    if note:
        lines.extend(["", f"*Note.* {note}"])
    lines.append("")
    return "\n".join(lines)


def convert_chp1(docx_path):
    doc = docx.Document(docx_path)
    lines = ["# Chapter I: Introduction\n"]
    for p in doc.paragraphs:
        style, text, is_bold, _ = extract_paragraph(p)
        if not text or text in ("Chapter I", "Introduction"):
            continue
        if style == "Heading 2" or (is_bold and len(text) < 60 and not text.endswith(".")):
            lines.append(f"\n## {text}\n")
        elif style == "List Paragraph" or text.startswith(("Robustness", "Resilience", "Generalizability")):
            lines.append(f"* {text}")
        else:
            lines.append(f"{text}\n")
    return "\n".join(lines)


def convert_chp2(docx_path):
    doc = docx.Document(docx_path)
    lines = ["# Chapter II: Review of the Relevant Literature\n"]
    level2_titles = [
        "Traditional Approaches and Operational Complexity",
        "From Analytical Queuing Models to Simulation Modeling and Real-Time Management",
        "Advanced Predictive Models and Machine Learning",
        "The Impact of Post-Pandemic Operational Volatility"
    ]
    for p in doc.paragraphs:
        style, text, is_bold, _ = extract_paragraph(p)
        if not text or text in ("Chapter II", "Review of the Relevant Literature"):
            continue
        is_heading = is_bold and len(text) < 100 and not text.endswith(".")
        if is_heading:
            if text in level2_titles:
                lines.append(f"\n## {text}\n")
            else:
                lines.append(f"\n### {text}\n")
        else:
            lines.append(f"{text}\n")
    return "\n".join(lines)


def convert_chp3(docx_path):
    doc = docx.Document(docx_path)
    lines = ["# Chapter III: Methodology\n"]
    level2_sections = [
        "Research Approach", "Sample", "Sources of Data", "Validity", "Treatment of the Data"
    ]
    for p in doc.paragraphs:
        style, text, is_bold, _ = extract_paragraph(p)
        if not text or text in ("Chapter III", "Methodology"):
            continue
        
        # Check for figure callout
        if text.startswith("Figure 3:") or text == "Design and Procedure Phases":
            if text.startswith("Figure 3:"):
                lines.append(f"\nFigure 3  \n*Design and Procedure Phases*\n")
                lines.append(f"![Figure 3: Design and Procedure Phases](../../figures/ch03_methodology/Combined_Data_Pipeline_and_Funnel_Lifecycle.png)\n")
                lines.append(f"*Note.* High-Performance Computing (HPC) sequential extract, transform, and load pipeline coupling TSA FOIA throughput records with BTS operational datasets.\n")
            continue
        
        is_heading = (style == "Normal" and is_bold and len(text) < 70 and not text.endswith(".")
                      and not text.startswith("Figure") and not text.startswith("Table"))
        
        if is_heading:
            if text in level2_sections or any(text.startswith(s) for s in level2_sections):
                lines.append(f"\n## {text}\n")
            else:
                lines.append(f"\n### {text}\n")
        elif style == "List Paragraph":
            lines.append(f"* {text}")
        else:
            lines.append(f"{text}\n")
    return "\n".join(lines)


def convert_chp4(docx_path):
    doc = docx.Document(docx_path)
    lines = ["# Chapter IV: Findings and Discussion\n"]
    
    # Table map
    tables = {
        "Table 4.1": (TABLES_DIR / "table_4_1.csv", "Table 4.1",
                      "Master Post-ETL Multi-Source Data Foundation Census",
                      "Full candidate commercial network across the Top 25 airfields (2019-2025)."),
        "Table 4.2": (TABLES_DIR / "table_4_2.csv", "Table 4.2",
                      "Post-ETL Master Summary Descriptive Statistics (Top 25 Cleaned Data Warehouse)",
                      "Parametric and non-parametric dispersion metrics across 42,062,039 conformed records."),
        "Table 4.6": (TABLES_DIR / "table_4_6.csv", "Table 4.6",
                      "The Nine-Airport Experimental Cohort Specification",
                      "Balanced 4x4 factorial design isolating 12 carrier-exclusive terminal complexes across 9 commercial airfields."),
        "Table 4.9": (TABLES_DIR / "table_4_9.csv", "Table 4.9",
                      "Empirical Lead-Lag Transfer Dynamics (Scheduled Flights Versus Checkpoint Volume)",
                      "Evaluated across 72,053 complex-hours on the 2025 holdout dataset."),
        "Table 4.8": (TABLES_DIR / "table_4_8.csv", "Table 4.8",
                      "Day-of-Week Mean Daily Passenger Throughput Across the Nine Cohort Airports",
                      "Average daily screened volume (pax/day) across dedicated carrier complexes."),
        "Table 4.10": (TABLES_DIR / "table_4_10.csv", "Table 4.10",
                       "Master Model Benchmark Matrix for TSA Throughput Volatility (2025 Full-Year Holdout)",
                       "Evaluated across 72,053 hourly complex observations in the 2025 holdout partition."),
        "Table 4.11": (TABLES_DIR / "table_4_11.csv", "Table 4.11",
                       "Master Multi-Pillar Hypothesis Evaluation Matrix Across the Four Models",
                       "Comprehensive evaluation across Robustness, Resilience, and Generalizability.")
    }

    skip_next = False
    for i, p in enumerate(doc.paragraphs):
        style, text, is_bold, _ = extract_paragraph(p)
        if not text or text in ("Chapter IV", "Findings and Discussion"):
            continue
        
        # Check Figure 4.1
        if text.startswith("Figure 4.1"):
            lines.append(f"\nFigure 4.1  \n*Chapter IV Architecture and Empirical Roadmap*\n")
            lines.append("```mermaid\ngraph TD\n    A[Section 4.1: Initial Exploratory Data Analysis] --> B[Section 4.2: Data Filtering & Subset Selection]\n    B --> C[Section 4.3: Model Development & Execution]\n    C --> D[Section 4.4: Model Results & Hypothesis Evaluation]\n```\n")
            lines.append("*Note.* Structural flow of empirical findings across the 4-phase analytical architecture.\n")
            continue
            
        # Check Table callouts
        matched_table = None
        for t_key in tables:
            if text.startswith(t_key):
                matched_table = t_key
                break
                
        if matched_table:
            csv_path, tid, title, note = tables[matched_table]
            tbl_md = format_apa7_table(csv_path, tid, title, note)
            lines.append(tbl_md)
            continue
            
        # Headings
        if style == "Heading 2":
            lines.append(f"\n## {text}\n")
        elif style == "Heading 3":
            lines.append(f"\n### {text}\n")
        elif is_bold and len(text) < 70 and not text.endswith(".") and not text.startswith("Table"):
            lines.append(f"\n### {text}\n")
        elif text.startswith(("Phase 1:", "Phase 2:", "Phase 3:", "Phase 4:", "Dimension 1:", "Dimension 2:", "Dimension 3:")):
            lines.append(f"\n#### {text}\n")
        elif text.startswith(("Initial Exploratory", "Data Filtering", "Model Development", "Model Results")):
            lines.append(f"* **{text}**")
        else:
            lines.append(f"{text}\n")
            
    return "\n".join(lines)


def convert_chp5(docx_path):
    doc = docx.Document(docx_path)
    lines = ["# Chapter V: Conclusions and Recommendations\n"]
    
    tables = {
        "Table 5.1": (TABLES_DIR / "table_5_1.csv", "Table 5.1",
                      "Evaluation Dimension 1: Routine Operational Accuracy Across the Candidate Models",
                      "Evaluated during nominal conditions (delays < 15 min, zero cancellations)."),
        "Table 5.2": (TABLES_DIR / "table_5_2.csv", "Table 5.2",
                      "Evaluation Dimension 2: Resilience and Shock Performance Under Severe Operational Disruption",
                      "Evaluated during severe IROPS disruptions (departure delays >= 45 min or cancellations >= 5)."),
        "Table 5.3": (TABLES_DIR / "table_5_3.csv", "Table 5.3",
                      "Evaluation Dimension 3: Generalizability and Cross-Airport Spatial Transfer",
                      "Evaluated under zero-shot transfer from EWR (Terminal C) to LGA (Terminal C)."),
        "Table 5.4": (TABLES_DIR / "table_5_4.csv", "Table 5.4",
                      "Master Multi-Dimensional Model Evaluation Trade-Offs (Hypothesis 1 Summary)",
                      "Summary of asymmetric trade-offs across all three operational performance dimensions.")
    }

    for p in doc.paragraphs:
        style, text, is_bold, _ = extract_paragraph(p)
        if not text or text in ("Chapter V", "Conclusions and Recommendations"):
            continue
            
        matched_table = None
        for t_key in tables:
            if text.startswith(t_key):
                matched_table = t_key
                break
                
        if matched_table:
            csv_path, tid, title, note = tables[matched_table]
            tbl_md = format_apa7_table(csv_path, tid, title, note)
            lines.append(tbl_md)
            continue
            
        if style == "Heading 2" or (is_bold and len(text) < 80 and not text.endswith(".")):
            lines.append(f"\n## {text}\n")
        elif style == "Heading 3":
            lines.append(f"\n### {text}\n")
        elif style == "List Paragraph":
            lines.append(f"* {text}")
        else:
            lines.append(f"{text}\n")
            
    return "\n".join(lines)


def main():
    FINAL_V1_DIR.mkdir(parents=True, exist_ok=True)
    
    print("Converting Chapter I...")
    ch1_md = convert_chp1(MANUSCRIPTS_DIR / "ChpI v4.docx")
    with open(FINAL_V1_DIR / "chp1-intro.md", "w", encoding="utf-8") as f:
        f.write(ch1_md)
        
    print("Converting Chapter II...")
    ch2_md = convert_chp2(MANUSCRIPTS_DIR / "ChpII v5.docx")
    with open(FINAL_V1_DIR / "chp2-litreview.md", "w", encoding="utf-8") as f:
        f.write(ch2_md)
        
    print("Converting Chapter III...")
    ch3_md = convert_chp3(MANUSCRIPTS_DIR / "ChpIII v4.docx")
    with open(FINAL_V1_DIR / "chp3-methodology.md", "w", encoding="utf-8") as f:
        f.write(ch3_md)
        
    print("Converting Chapter IV...")
    ch4_md = convert_chp4(MANUSCRIPTS_DIR / "ChpIV v5.docx")
    with open(FINAL_V1_DIR / "chp4-results.md", "w", encoding="utf-8") as f:
        f.write(ch4_md)
        
    print("Converting Chapter V...")
    ch5_md = convert_chp5(MANUSCRIPTS_DIR / "ChpV v1.docx")
    with open(FINAL_V1_DIR / "chp5-discussion.md", "w", encoding="utf-8") as f:
        f.write(ch5_md)
        
    # Compile full thesis
    full_thesis_lines = [
        "---",
        "title: \"Evaluating Predictive Techniques to Model Stochastic Airport Passenger Flow\"",
        "author: \"Leila Gleich\"",
        "institution: \"Embry-Riddle Aeronautical University\"",
        "degree: \"Master of Science in Aeronautics\"",
        "date: \"October 2026\"",
        "version: \"final-thesis-v1 (APA 7th Edition Conformed)\"",
        "---\n\n",
        ch1_md,
        "\n\n---\n\n",
        ch2_md,
        "\n\n---\n\n",
        ch3_md,
        "\n\n---\n\n",
        ch4_md,
        "\n\n---\n\n",
        ch5_md
    ]
    full_thesis_md = "\n".join(full_thesis_lines)
    
    with open(FINAL_V1_DIR / "final-thesis-v1.md", "w", encoding="utf-8") as f:
        f.write(full_thesis_md)
        
    with open(MANUSCRIPTS_DIR / "final-thesis-v1.md", "w", encoding="utf-8") as f:
        f.write(full_thesis_md)
        
    print("[SUCCESS] All APA 7th Edition Markdown files generated cleanly in final-thesis-v1!")


if __name__ == "__main__":
    main()
