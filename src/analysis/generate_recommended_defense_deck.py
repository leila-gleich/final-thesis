"""
build_recommended_defense_deck.py
Generates a clean, minimalistic, modern 16:9 PowerPoint deck for Leila Gleich's Thesis Defense.
Adheres strictly to:
- ERAU Navy and Slate palette, clean whitespace, card layouts, stat callouts, comparison grids
- Centered mathematical equations in dedicated callout cards
- Balanced layout mixing (no bullet-point overload)
- 32 slides mirroring Thesis-Defense.pptx and DEFENSE_PRESENTATION_SCRIPT_25MIN.md
"""

import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE

def create_deck(output_path):
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    # Color Palette: Clean Minimalist ERAU Aviation theme
    NAVY = RGBColor(10, 34, 64)        # Deep ERAU Navy
    LIGHT_NAVY = RGBColor(24, 52, 94)  # Accent Navy
    SLATE = RGBColor(71, 85, 105)      # Cool Slate Body
    DARK_TEXT = RGBColor(15, 23, 42)   # Near Black
    MUTED_TEXT = RGBColor(100, 116, 139) # Light Muted Grey
    BG_CARD = RGBColor(248, 250, 252)  # Soft Off-white / light slate card
    BORDER_CARD = RGBColor(226, 232, 240) # Card Border
    ACCENT_BLUE = RGBColor(37, 99, 235) # Vivid Blue Accent
    AMBER_BG = RGBColor(254, 243, 199) # Warning card bg
    AMBER_TEXT = RGBColor(180, 83, 9)  # Warning text
    GREEN_BG = RGBColor(240, 253, 244) # Success card bg
    GREEN_TEXT = RGBColor(21, 128, 61) # Success text
    WHITE = RGBColor(255, 255, 255)

    def add_header(slide, tracker, title, subtitle=None):
        """Header with small uppercase category tracker and bold title"""
        header_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.5), Inches(11.733), Inches(1.1))
        tf = header_box.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0

        p0 = tf.paragraphs[0]
        p0.text = tracker.upper()
        p0.font.name = "Calibri"
        p0.font.size = Pt(11)
        p0.font.bold = True
        p0.font.color.rgb = ACCENT_BLUE

        p1 = tf.add_paragraph()
        p1.text = title
        p1.font.name = "Calibri"
        p1.font.size = Pt(24)
        p1.font.bold = True
        p1.font.color.rgb = NAVY
        p1.space_before = Pt(3)

        if subtitle:
            p2 = tf.add_paragraph()
            p2.text = subtitle
            p2.font.name = "Calibri"
            p2.font.size = Pt(13)
            p2.font.color.rgb = SLATE
            p2.space_before = Pt(3)

    def add_card(slide, left, top, width, height, bg_color=BG_CARD, border_color=BORDER_CARD):
        shape = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
        shape.fill.solid()
        shape.fill.fore_color.rgb = bg_color
        shape.line.color.rgb = border_color
        shape.line.width = Pt(1)
        return shape

    def add_equation_card(slide, left, top, width, height, eq_title, eq_formula, explanation):
        shape = add_card(slide, left, top, width, height, BG_CARD, BORDER_CARD)
        tf = shape.text_frame
        tf.word_wrap = True
        tf.margin_left = Inches(0.3)
        tf.margin_right = Inches(0.3)
        tf.margin_top = Inches(0.2)
        tf.margin_bottom = Inches(0.2)

        p0 = tf.paragraphs[0]
        p0.text = eq_title.upper()
        p0.font.name = "Calibri"
        p0.font.size = Pt(11)
        p0.font.bold = True
        p0.font.color.rgb = ACCENT_BLUE
        p0.alignment = PP_ALIGN.CENTER

        p1 = tf.add_paragraph()
        p1.text = eq_formula
        p1.font.name = "Georgia"
        p1.font.size = Pt(18)
        p1.font.bold = True
        p1.font.color.rgb = NAVY
        p1.alignment = PP_ALIGN.CENTER
        p1.space_before = Pt(8)
        p1.space_after = Pt(8)

        p2 = tf.add_paragraph()
        p2.text = explanation
        p2.font.name = "Calibri"
        p2.font.size = Pt(12)
        p2.font.color.rgb = SLATE
        p2.alignment = PP_ALIGN.CENTER

    def add_stat_box(slide, left, top, width, height, number_str, label_str, subtext_str=None, color=NAVY):
        shape = add_card(slide, left, top, width, height, WHITE, BORDER_CARD)
        tf = shape.text_frame
        tf.word_wrap = True
        tf.margin_left = Inches(0.2)
        tf.margin_right = Inches(0.2)
        tf.margin_top = Inches(0.2)

        p0 = tf.paragraphs[0]
        p0.text = number_str
        p0.font.name = "Calibri"
        p0.font.size = Pt(28)
        p0.font.bold = True
        p0.font.color.rgb = color
        p0.alignment = PP_ALIGN.CENTER

        p1 = tf.add_paragraph()
        p1.text = label_str
        p1.font.name = "Calibri"
        p1.font.size = Pt(12)
        p1.font.bold = True
        p1.font.color.rgb = DARK_TEXT
        p1.alignment = PP_ALIGN.CENTER
        p1.space_before = Pt(4)

        if subtext_str:
            p2 = tf.add_paragraph()
            p2.text = subtext_str
            p2.font.name = "Calibri"
            p2.font.size = Pt(10.5)
            p2.font.color.rgb = MUTED_TEXT
            p2.alignment = PP_ALIGN.CENTER
            p2.space_before = Pt(2)

    # ==========================================
    # SLIDE 1: TITLE SLIDE
    # ==========================================
    s1 = prs.slides.add_slide(blank_layout)
    # Background accent bar
    top_bar = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(0.35))
    top_bar.fill.solid()
    top_bar.fill.fore_color.rgb = NAVY
    top_bar.line.fill.background()

    tbox = s1.shapes.add_textbox(Inches(1.2), Inches(1.8), Inches(10.9), Inches(4.5))
    tf1 = tbox.text_frame
    tf1.word_wrap = True

    p = tf1.paragraphs[0]
    p.text = "GRADUATE THESIS DEFENSE  |  MSAA / GLEICH 700B"
    p.font.name = "Calibri"
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = ACCENT_BLUE

    p = tf1.add_paragraph()
    p.text = "Evaluating Predictive Techniques to Model\nStochastic Airport Passenger Flow"
    p.font.name = "Calibri"
    p.font.size = Pt(36)
    p.font.bold = True
    p.font.color.rgb = NAVY
    p.space_before = Pt(14)
    p.space_after = Pt(20)

    p = tf1.add_paragraph()
    p.text = "An Evaluation of Multi-Pillar Performance Measures for TSA Throughput Volatility"
    p.font.name = "Calibri"
    p.font.size = Pt(16)
    p.font.color.rgb = SLATE

    p = tf1.add_paragraph()
    p.text = "Candidate: Leila Gleich\nEmbry-Riddle Aeronautical University  ·  Worldwide Campus  ·  October 2026"
    p.font.name = "Calibri"
    p.font.size = Pt(13)
    p.font.color.rgb = MUTED_TEXT
    p.space_before = Pt(28)

    # ==========================================
    # SLIDE 2: PRESENTATION OUTLINE
    # ==========================================
    s2 = prs.slides.add_slide(blank_layout)
    add_header(s2, "Executive Roadmap", "Defense Presentation Structure", "Paced 25-Minute Defense Architecture across Six Operational Segments")

    steps = [
        ("01", "Research Problem & Hypotheses", "Stochastic arrivals, Kingman's heavy-traffic queuing law, and Asymmetric Trade-Offs (H1)"),
        ("02", "Literature & Theoretical Gaps", "Evolution from deterministic schedules and micro-simulation to ML and 2-stage dynamic hybrids"),
        ("03", "Econometric Data Pipeline", "4-phase pipeline, 4-tier filtering funnel, DB1B connecting deflation, and carrier isolation"),
        ("04", "Empirical Findings & Regimes", "Values vs. Volatility coupling (R² = 19.1%), 4 annual seasons, and bimodal diurnal peaks"),
        ("05", "Model Execution & Benchmarks", "Evaluating 4 paradigms across Robustness (nominal), Resilience (IROPS), and Generalizability"),
        ("06", "Operational Implementation", "Regime-switched gated inference engine, dynamic checkpoint rostering, and conclusion")
    ]
    for i, (num, title_txt, desc_txt) in enumerate(steps):
        col = i % 3
        row = i // 3
        left = Inches(0.8 + col * 4.0)
        top = Inches(2.1 + row * 2.5)
        card = add_card(s2, left, top, Inches(3.7), Inches(2.2))
        tf = card.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_right = Inches(0.25)
        tf.margin_top = Inches(0.2)

        p = tf.paragraphs[0]
        p.text = num
        p.font.name = "Calibri"
        p.font.size = Pt(20)
        p.font.bold = True
        p.font.color.rgb = ACCENT_BLUE

        p = tf.add_paragraph()
        p.text = title_txt
        p.font.name = "Calibri"
        p.font.size = Pt(14)
        p.font.bold = True
        p.font.color.rgb = NAVY
        p.space_before = Pt(4)

        p = tf.add_paragraph()
        p.text = desc_txt
        p.font.name = "Calibri"
        p.font.size = Pt(11)
        p.font.color.rgb = SLATE
        p.space_before = Pt(4)

    # ==========================================
    # SLIDE 3: THE RESEARCH PROBLEM
    # ==========================================
    s3 = prs.slides.add_slide(blank_layout)
    add_header(s3, "Theoretical Foundation", "The Terminal Queuing Friction Problem", "Why Static Volume Staffing Fails Under Arrival Burstiness")

    # Left Card: Core Operational Tension
    c_left = add_card(s3, Inches(0.8), Inches(2.1), Inches(5.6), Inches(4.7))
    tf = c_left.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_right = Inches(0.3)
    tf.margin_top = Inches(0.3)

    p = tf.paragraphs[0]
    p.text = "THE ASYMMETRIC QUEUING DILEMMA"
    p.font.name = "Calibri"
    p.font.size = Pt(12)
    p.font.bold = True
    p.font.color.rgb = ACCENT_BLUE

    p = tf.add_paragraph()
    p.text = "Commercial airport passenger flow is fundamentally stochastic, governed by independent upstream passenger show-up decisions and downstream flight bank delays."
    p.font.name = "Calibri"
    p.font.size = Pt(13)
    p.font.color.rgb = DARK_TEXT
    p.space_before = Pt(8)

    p = tf.add_paragraph()
    p.text = "Rigid Physical Infrastructure:"
    p.font.name = "Calibri"
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = NAVY
    p.space_before = Pt(12)

    p = tf.add_paragraph()
    p.text = "Security screening lanes (AIT scanners, baggage belts, TSO rosters) cannot expand dynamically in response to sudden surges. Checkpoint lane utilization approaches capacity (ρ → 1.0)."
    p.font.name = "Calibri"
    p.font.size = Pt(12)
    p.font.color.rgb = SLATE
    p.space_before = Pt(2)

    p = tf.add_paragraph()
    p.text = "The Operational Failure Mode:"
    p.font.name = "Calibri"
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = NAVY
    p.space_before = Pt(12)

    p = tf.add_paragraph()
    p.text = "Static historical staffing tables leave terminals either critically over-staffed during minimal volume or severely under-staffed during delay cascades."
    p.font.name = "Calibri"
    p.font.size = Pt(12)
    p.font.color.rgb = SLATE
    p.space_before = Pt(2)

    # Right Card: Kingman Heavy-Traffic Law Centered Equation
    add_equation_card(
        s3, Inches(6.8), Inches(2.1), Inches(5.7), Inches(4.7),
        "Mathematical Grounding: Kingman's Heavy-Traffic Law",
        "W_q  ≈  ( ρ / (1 - ρ) ) · ( (C_a² + C_s²) / 2 ) · ( 1 / μ )",
        "Key Operational Takeaway:\n\n"
        "1. Delay scales quadratically with arrival volatility (C_a²), NOT static passenger counts.\n\n"
        "2. As lane utilization ρ approaches 1.0, any marginal burst in passenger dispersion causes non-linear queue explosions.\n\n"
        "3. Accurately modeling and forecasting volatility (σ_TSA and CV_TSA) is paramount to preventing checkpoint gridlock."
    )

    # ==========================================
    # SLIDE 4: RESEARCH PURPOSE
    # ==========================================
    s4 = prs.slides.add_slide(blank_layout)
    add_header(s4, "Research Formulation", "Research Purpose & Operational Objectives", "Transforming Terminal Security from Static Accounting to Stochastic Forecasting")

    purposes = [
        ("Pivot from Volume to Volatility", "Shift the core predictive target from raw static passenger headcounts (y_t) to true throughput volatility (σ_TSA, CV_TSA), capturing the arrival burstiness that directly governs queuing delays under heavy utilization."),
        ("Multi-Paradigm Comparative Evaluation", "Empirically evaluate three candidate modeling families—deterministic flight schedules, supervised machine learning, and dynamic 2-stage hybrids—benchmarked against a non-parametric naive persistence control."),
        ("Circumstance-Conditioned Model Selection", "Formalize a multi-pillar evaluative architecture proving that model optimality is contingent upon operational priorities (routine accuracy vs. disruption resilience vs. zero-shot facility portability).")
    ]
    for i, (title_txt, desc_txt) in enumerate(purposes):
        left = Inches(0.8 + i * 4.0)
        card = add_card(s4, left, Inches(2.2), Inches(3.7), Inches(4.5))
        tf = card.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_right = Inches(0.3)
        tf.margin_top = Inches(0.3)

        p = tf.paragraphs[0]
        p.text = f"OBJECTIVE {i+1}"
        p.font.name = "Calibri"
        p.font.size = Pt(11)
        p.font.bold = True
        p.font.color.rgb = ACCENT_BLUE

        p = tf.add_paragraph()
        p.text = title_txt
        p.font.name = "Calibri"
        p.font.size = Pt(16)
        p.font.bold = True
        p.font.color.rgb = NAVY
        p.space_before = Pt(8)

        p = tf.add_paragraph()
        p.text = desc_txt
        p.font.name = "Calibri"
        p.font.size = Pt(12)
        p.font.color.rgb = SLATE
        p.space_before = Pt(12)

    # ==========================================
    # SLIDE 5: RESEARCH QUESTION
    # ==========================================
    s5 = prs.slides.add_slide(blank_layout)
    add_header(s5, "Core Inquiry", "Primary Research Question", "Evaluating Predictive Paradigms Across Competing Operational Trade-Offs")

    # Central Callout Card
    rq_card = add_card(s5, Inches(1.5), Inches(2.0), Inches(10.3), Inches(2.3), WHITE, ACCENT_BLUE)
    tf = rq_card.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_right = Inches(0.5)
    tf.margin_top = Inches(0.3)

    p = tf.paragraphs[0]
    p.text = "RESEARCH QUESTION (RQ₁)"
    p.font.name = "Calibri"
    p.font.size = Pt(12)
    p.font.bold = True
    p.font.color.rgb = ACCENT_BLUE
    p.alignment = PP_ALIGN.CENTER

    p = tf.add_paragraph()
    p.text = "“Which predictive modeling frameworks—spanning deterministic persistence controls, deterministic schedule baselines, machine learning, and dynamic two-stage hybrids—are most effective for forecasting airport passenger security screening throughput volatility when prioritizing robustness, resilience, or generalizability as the primary operational evaluation metric?”"
    p.font.name = "Georgia"
    p.font.size = Pt(15)
    p.font.color.rgb = NAVY
    p.alignment = PP_ALIGN.CENTER
    p.space_before = Pt(8)

    # 3 Pill Sub-cards
    pills = [
        ("Robustness", "Routine Operational Accuracy", "Lowest RMSE & MASE < 0.700 under nominal on-time operations (delay < 15m, 0 cancels)."),
        ("Resilience", "Disruption Shock Stability", "Disruption multiplier R_MASE ≈ 1.00, lowest shock error, and recovery time TTR < 4.0h during IROPS."),
        ("Generalizability", "Zero-Shot Facility Portability", "Relative transfer ratio RTR ≈ 1.00 and error penalty ΔMASE ≤ 10% deployed to new terminals without retraining.")
    ]
    for i, (dim, sub, desc) in enumerate(pills):
        left = Inches(1.5 + i * 3.6)
        card = add_card(s5, left, Inches(4.7), Inches(3.2), Inches(2.1))
        tf = card.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_right = Inches(0.2)
        tf.margin_top = Inches(0.18)

        p = tf.paragraphs[0]
        p.text = dim.upper()
        p.font.name = "Calibri"
        p.font.size = Pt(12)
        p.font.bold = True
        p.font.color.rgb = NAVY

        p = tf.add_paragraph()
        p.text = sub
        p.font.name = "Calibri"
        p.font.size = Pt(11)
        p.font.bold = True
        p.font.color.rgb = ACCENT_BLUE
        p.space_before = Pt(2)

        p = tf.add_paragraph()
        p.text = desc
        p.font.name = "Calibri"
        p.font.size = Pt(10.5)
        p.font.color.rgb = SLATE
        p.space_before = Pt(4)

    # ==========================================
    # SLIDE 6: HYPOTHESIS: THE ASYMMETRIC TRADE-OFF
    # ==========================================
    s6 = prs.slides.add_slide(blank_layout)
    add_header(s6, "Theoretical Formulation", "Hypothesis: The Asymmetric Trade-Off (H₁)", "No Single Predictive Technique is Universally Dominant Across All Operating Regimes")

    # Master H1 Banner
    h1_banner = add_card(s6, Inches(0.8), Inches(2.0), Inches(11.7), Inches(1.1), BG_CARD, BORDER_CARD)
    tf = h1_banner.text_frame
    tf.word_wrap = True
    tf.margin_left = Inches(0.4)
    tf.margin_top = Inches(0.15)
    p = tf.paragraphs[0]
    p.text = "MASTER HYPOTHESIS H₁:"
    p.font.name = "Calibri"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = ACCENT_BLUE
    p = tf.add_paragraph()
    p.text = "Across the candidate modeling paradigms evaluated, no individual approach will prove superior across all three performance measures (robustness, resilience, and generalizability)."
    p.font.name = "Calibri"
    p.font.size = Pt(14)
    p.font.bold = True
    p.font.color.rgb = NAVY
    p.space_before = Pt(2)

    # 3 Sub-Hypotheses Grid
    sub_hyps = [
        ("H₁ₐ  ·  Robustness", "Routine Accuracy Winner", "Model 2 (Machine Learning) & Model 3 (Hybrid) achieve MASE < 0.700 under nominal rhythms.\n\nDeterministic baselines fail due to schedule rigidity."),
        ("H₁ᵦ  ·  Resilience", "Disruption Shock Winner", "Model 3 (Dynamic Hybrid) is the sole model satisfying resilience (R_MASE ≈ 1.05).\n\nModel 2 collapses (R = 2.14) due to the Empty Checkpoint Fallacy."),
        ("H₁꜀  ·  Generalizability", "Zero-Shot Transfer Winner", "Model 1 (Deterministic) satisfies transfer targets (RTR = 1.04, ΔMASE = +4.0%).\n\nModel 3 fails (RTR = 1.19, ΔMASE = +21.5%) due to terminal geometry overfitting.")
    ]
    for i, (tag, win, txt) in enumerate(sub_hyps):
        left = Inches(0.8 + i * 4.0)
        card = add_card(s6, left, Inches(3.3), Inches(3.7), Inches(3.5))
        tf = card.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_right = Inches(0.3)
        tf.margin_top = Inches(0.25)

        p = tf.paragraphs[0]
        p.text = tag
        p.font.name = "Calibri"
        p.font.size = Pt(13)
        p.font.bold = True
        p.font.color.rgb = NAVY

        p = tf.add_paragraph()
        p.text = win.upper()
        p.font.name = "Calibri"
        p.font.size = Pt(11)
        p.font.bold = True
        p.font.color.rgb = ACCENT_BLUE
        p.space_before = Pt(3)

        p = tf.add_paragraph()
        p.text = txt
        p.font.name = "Calibri"
        p.font.size = Pt(11.5)
        p.font.color.rgb = SLATE
        p.space_before = Pt(8)

    # ==========================================
    # SLIDE 7: DYNAMIC PERFORMANCE MEASURES
    # ==========================================
    s7 = prs.slides.add_slide(blank_layout)
    add_header(s7, "Evaluative Trio", "The Multi-Pillar Performance Framework", "Replacing Single-Metric Bias with a Context-Aware Operational Evaluation Trio")

    dims = [
        ("DIMENSION 1", "ROBUSTNESS", "Routine Baseline Accuracy", "Target: Lowest RMSE & MASE < 0.700", "Measures forecasting accuracy under nominal, on-time baseline operations (delays < 15 min, 0 cancellations). Ensures reliable day-to-day base staffing rosters."),
        ("DIMENSION 2", "RESILIENCE", "Disruption Shock Recovery", "Target: R_MASE ≈ 1.00 & TTR < 4.0h", "Measures stability and recovery rate under acute convective flight ground stops and severe delays (≥ 45 min, cancels ≥ 5). Prevents checkpoint under-staffing during IROPS."),
        ("DIMENSION 3", "GENERALIZABILITY", "Zero-Shot Facility Transfer", "Target: RTR ≤ 1.05 & ΔMASE ≤ 10%", "Measures transferability of source-calibrated models (EWR) to unfamiliar target terminals (LGA) without local retraining. Tests structural independence from local physical geometry.")
    ]
    for i, (dim_tag, name, sub, target_txt, desc) in enumerate(dims):
        left = Inches(0.8 + i * 4.0)
        card = add_card(s7, left, Inches(2.2), Inches(3.7), Inches(4.5))
        tf = card.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_right = Inches(0.3)
        tf.margin_top = Inches(0.3)

        p = tf.paragraphs[0]
        p.text = dim_tag
        p.font.name = "Calibri"
        p.font.size = Pt(11)
        p.font.bold = True
        p.font.color.rgb = ACCENT_BLUE

        p = tf.add_paragraph()
        p.text = name
        p.font.name = "Calibri"
        p.font.size = Pt(20)
        p.font.bold = True
        p.font.color.rgb = NAVY
        p.space_before = Pt(2)

        p = tf.add_paragraph()
        p.text = sub
        p.font.name = "Calibri"
        p.font.size = Pt(12)
        p.font.color.rgb = DARK_TEXT
        p.space_before = Pt(4)

        # Target callout
        p = tf.add_paragraph()
        p.text = target_txt
        p.font.name = "Calibri"
        p.font.size = Pt(11)
        p.font.bold = True
        p.font.color.rgb = GREEN_TEXT
        p.space_before = Pt(12)

        p = tf.add_paragraph()
        p.text = desc
        p.font.name = "Calibri"
        p.font.size = Pt(11.5)
        p.font.color.rgb = SLATE
        p.space_before = Pt(8)

    # ==========================================
    # SLIDE 8: EXISTING LITERATURE OVERVIEW
    # ==========================================
    s8 = prs.slides.add_slide(blank_layout)
    add_header(s8, "Theoretical Evolution", "Chronological Evolution of Terminal Flow Literature", "Bridging the Historical Divide Between Airside Operations and Landside Security")

    # 4 Chronological milestone cards
    milestones = [
        ("Phase I: 1990s–2000s", "Deterministic Airline Scheduling", "Convolving flight seat banks across static ACRP Report 40 passenger arrival distributions.\n\nAssumes 100% on-time flight departures; blind to delay cascades."),
        ("Phase II: 2000s–2010s", "Discrete-Event Simulation", "Micro-simulation modeling individual passenger paths (Simio, CAST, ARENA).\n\nDetailed terminal layout fidelity, but extreme computational latency prohibits live dispatch."),
        ("Phase III: 2015–2020s", "Supervised Machine Learning", "Gradient-boosted decision trees incorporating flight delays and weather covariates.\n\nOptimizes routine nominal error, but exhibits severe brittleness during severe convective disruptions."),
        ("Phase IV: Contemporary", "Two-Stage Dynamic Hybrids", "Coupling deterministic schedule foundations with live checkpoint floor feedback (e_t-1).\n\nProvides real-time adaptability while preserving physical mass balance principles.")
    ]
    for i, (era, title_txt, desc_txt) in enumerate(milestones):
        left = Inches(0.8 + i * 3.0)
        card = add_card(s8, left, Inches(2.2), Inches(2.8), Inches(4.5))
        tf = card.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_right = Inches(0.25)
        tf.margin_top = Inches(0.25)

        p = tf.paragraphs[0]
        p.text = era
        p.font.name = "Calibri"
        p.font.size = Pt(11)
        p.font.bold = True
        p.font.color.rgb = ACCENT_BLUE

        p = tf.add_paragraph()
        p.text = title_txt
        p.font.name = "Calibri"
        p.font.size = Pt(15)
        p.font.bold = True
        p.font.color.rgb = NAVY
        p.space_before = Pt(4)

        p = tf.add_paragraph()
        p.text = desc_txt
        p.font.name = "Calibri"
        p.font.size = Pt(11)
        p.font.color.rgb = SLATE
        p.space_before = Pt(10)

    # ==========================================
    # SLIDE 9: LITERATURE GAP: VOLATILITY IS CRITICAL
    # ==========================================
    s9 = prs.slides.add_slide(blank_layout)
    add_header(s9, "Literature Gap", "The Static Fallacy in Existing Literature", "Why Historical Gravity and Static Headcount Models Fail Terminal Queuing")

    c1 = add_card(s9, Inches(0.8), Inches(2.1), Inches(5.6), Inches(4.6))
    tf1 = c1.text_frame
    tf1.word_wrap = True
    tf1.margin_left = tf1.margin_right = Inches(0.3)
    tf1.margin_top = Inches(0.3)

    p = tf1.paragraphs[0]
    p.text = "THE FLAW IN TRADITIONAL AIRPORT RESEARCH"
    p.font.name = "Calibri"
    p.font.size = Pt(12)
    p.font.bold = True
    p.font.color.rgb = ACCENT_BLUE

    p = tf1.add_paragraph()
    p.text = "Existing airport operations literature overwhelmingly evaluates forecasting success using static passenger headcounts (y_t) and aggregate daily totals."
    p.font.name = "Calibri"
    p.font.size = Pt(13)
    p.font.color.rgb = DARK_TEXT
    p.space_before = Pt(8)

    p = tf1.add_paragraph()
    p.text = "Why Static Aggregates Mislead:"
    p.font.name = "Calibri"
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = NAVY
    p.space_before = Pt(12)

    p = tf1.add_paragraph()
    p.text = "Two days with identical 50,000 daily passenger volumes can experience radically different queue delays: an evenly distributed flow produces zero delays, whereas clustered bank arrivals overwhelm checkpoint queues."
    p.font.name = "Calibri"
    p.font.size = Pt(12)
    p.font.color.rgb = SLATE
    p.space_before = Pt(4)

    # Right Card: The Volatility Paradigm
    c2 = add_card(s9, Inches(6.8), Inches(2.1), Inches(5.7), Inches(4.6), BG_CARD, BORDER_CARD)
    tf2 = c2.text_frame
    tf2.word_wrap = True
    tf2.margin_left = tf2.margin_right = Inches(0.3)
    tf2.margin_top = Inches(0.3)

    p = tf2.paragraphs[0]
    p.text = "THE VOLATILITY ADVANTAGE"
    p.font.name = "Calibri"
    p.font.size = Pt(12)
    p.font.bold = True
    p.font.color.rgb = GREEN_TEXT

    p = tf2.add_paragraph()
    p.text = "Arrival Burstiness Governs Heavy-Traffic Queues"
    p.font.name = "Calibri"
    p.font.size = Pt(16)
    p.font.bold = True
    p.font.color.rgb = NAVY
    p.space_before = Pt(6)

    p = tf2.add_paragraph()
    p.text = "Under heavy utilization (ρ → 1.0), variance mismatch is the primary source of operational friction. Forecasting the diurnal standard deviation (σ_TSA) and the scale-free coefficient of variation (CV_TSA = σ/μ) provides direct actionable intelligence for security lane dispatching."
    p.font.name = "Calibri"
    p.font.size = Pt(12.5)
    p.font.color.rgb = SLATE
    p.space_before = Pt(8)

    # Mini centered formula
    p = tf2.add_paragraph()
    p.text = "CV_TSA = σ_TSA / μ_TSA  (Dimensionless Arrival Burstiness)"
    p.font.name = "Georgia"
    p.font.size = Pt(14)
    p.font.bold = True
    p.font.color.rgb = NAVY
    p.alignment = PP_ALIGN.CENTER
    p.space_before = Pt(14)
    p.space_after = Pt(14)

    p = tf2.add_paragraph()
    p.text = "Normalizes arrival turbulence across mega hub terminals and medium hubs, establishing a scale-free benchmark for queuing risk."
    p.font.name = "Calibri"
    p.font.size = Pt(11.5)
    p.font.color.rgb = SLATE

    # ==========================================
    # SLIDE 10: TRADITIONAL MODELS
    # ==========================================
    s10 = prs.slides.add_slide(blank_layout)
    add_header(s10, "Literature Breakdown", "Deterministic Flight Schedules & Classical Queueing", "The Historical Foundation: Flight Bank Convolutions (Model 1 Baseline)")

    add_equation_card(
        s10, Inches(0.8), Inches(2.1), Inches(5.6), Inches(4.6),
        "Deterministic Schedule Convolution",
        "Ŷ_t  =  ∑ [Seats_i · (1 - S_connect) · P(t - DEP_i)]",
        "Convolving scheduled flight departures DEP_i with ACRP Report 40 lognormal passenger show-up curves P(τ).\n\n"
        "Strengths: 100% transparent, zero calibration compute, fully interpretable.\n\n"
        "Fatal Operational Defect: Completely blind to downstream flight delays, cancellations, and airside ground stops."
    )

    # Right Card: Classical M/M/s vs. Stochastic Reality
    c_right = add_card(s10, Inches(6.8), Inches(2.1), Inches(5.7), Inches(4.6))
    tf = c_right.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_right = Inches(0.3)
    tf.margin_top = Inches(0.3)

    p = tf.paragraphs[0]
    p.text = "CLASSICAL QUEUING FORMULATIONS"
    p.font.name = "Calibri"
    p.font.size = Pt(12)
    p.font.bold = True
    p.font.color.rgb = ACCENT_BLUE

    p = tf.add_paragraph()
    p.text = "Erlang-C & Poisson Arrival Limits"
    p.font.name = "Calibri"
    p.font.size = Pt(16)
    p.font.bold = True
    p.font.color.rgb = NAVY
    p.space_before = Pt(6)

    p = tf.add_paragraph()
    p.text = "Classical M/M/s and Erlang-C models assume memoryless Poisson arrivals (variance = mean, C_a² = 1.0). In real airport screening, arrival variance is significantly overdispersed (C_a² >> 1.0) due to flight bank synchronizations and party clustering."
    p.font.name = "Calibri"
    p.font.size = Pt(12)
    p.font.color.rgb = SLATE
    p.space_before = Pt(8)

    p = tf.add_paragraph()
    p.text = "Empirical Reality in 9-Airport Cohort:"
    p.font.name = "Calibri"
    p.font.size = Pt(12)
    p.font.bold = True
    p.font.color.rgb = DARK_TEXT
    p.space_before = Pt(10)

    p = tf.add_paragraph()
    p.text = "Average CV_TSA across our cohort is 0.8728, reaching 1.1240 at LGA. Treating passenger arrival rates as stationary Poisson processes underestimates checkpoint queues by up to 300%."
    p.font.name = "Calibri"
    p.font.size = Pt(11.5)
    p.font.color.rgb = SLATE
    p.space_before = Pt(4)

    # ==========================================
    # SLIDE 11: SHIFT TO MICRO-SIMULATION
    # ==========================================
    s11 = prs.slides.add_slide(blank_layout)
    add_header(s11, "Literature Breakdown", "The Shift to Micro-Simulation Modeling", "Granular Architectural Fidelity vs. Real-Time Operational Latency Barriers")

    c1 = add_card(s11, Inches(0.8), Inches(2.1), Inches(5.6), Inches(4.6), BG_CARD, BORDER_CARD)
    tf1 = c1.text_frame
    tf1.word_wrap = True
    tf1.margin_left = tf1.margin_right = Inches(0.3)
    tf1.margin_top = Inches(0.3)

    p = tf1.paragraphs[0]
    p.text = "ADVANTAGES OF MICRO-SIMULATION"
    p.font.name = "Calibri"
    p.font.size = Pt(12)
    p.font.bold = True
    p.font.color.rgb = GREEN_TEXT

    p = tf1.add_paragraph()
    p.text = "High Physical & Spatial Resolution"
    p.font.name = "Calibri"
    p.font.size = Pt(16)
    p.font.bold = True
    p.font.color.rgb = NAVY
    p.space_before = Pt(6)

    bullets_pro = [
        "Models discrete passenger trajectories, bag drop queuing, and individual screening lanes.",
        "Accurately maps complex terminal geometries, security lane layouts, and passenger walking paths.",
        "Captures interaction between TSA PreCheck, standard screening lanes, and CLEAR kiosks."
    ]
    for b in bullets_pro:
        p = tf1.add_paragraph()
        p.text = f"•  {b}"
        p.font.name = "Calibri"
        p.font.size = Pt(12)
        p.font.color.rgb = SLATE
        p.space_before = Pt(8)

    # Right Card: Shortcomings
    c2 = add_card(s11, Inches(6.8), Inches(2.1), Inches(5.7), Inches(4.6), BG_CARD, BORDER_CARD)
    tf2 = c2.text_frame
    tf2.word_wrap = True
    tf2.margin_left = tf2.margin_right = Inches(0.3)
    tf2.margin_top = Inches(0.3)

    p = tf2.paragraphs[0]
    p.text = "THREE OPERATIONAL SHORTCOMINGS"
    p.font.name = "Calibri"
    p.font.size = Pt(12)
    p.font.bold = True
    p.font.color.rgb = AMBER_TEXT

    p = tf2.add_paragraph()
    p.text = "Why Simulation Fails Live Tactical Dispatch"
    p.font.name = "Calibri"
    p.font.size = Pt(16)
    p.font.bold = True
    p.font.color.rgb = NAVY
    p.space_before = Pt(6)

    bullets_con = [
        "Calibration Overhead: Requires hundreds of manual parameters (boarding pass scanner times, bin loading rates) that become obsolete during weather shocks.",
        "Computational Latency: Re-running Monte Carlo iterations takes 20–45 minutes—far too slow for real-time TSA checkpoint lane rebalancing.",
        "Lack of Airside Coupling: Rarely incorporates live FAA air traffic management programs, taxiway queue buildup, or downline delay cascades."
    ]
    for b in bullets_con:
        p = tf2.add_paragraph()
        p.text = f"•  {b}"
        p.font.name = "Calibri"
        p.font.size = Pt(11.5)
        p.font.color.rgb = SLATE
        p.space_before = Pt(6)

    # ==========================================
    # SLIDE 12: ADVANCED PREDICTIVE MODELS (MACHINE LEARNING)
    # ==========================================
    s12 = prs.slides.add_slide(blank_layout)
    add_header(s12, "Literature Breakdown", "Supervised Machine Learning (Model 2)", "Nonlinear Feature Exploration vs. Regimes of Severe Brittleness")

    add_stat_box(s12, Inches(0.8), Inches(2.1), Inches(3.6), Inches(4.6), "24", "BTS OTP & Schedule Features", "Taxi-out, cancellations, delay causes, gauge tiers, and flight bank dispersion metrics", NAVY)

    c_center = add_card(s12, Inches(4.8), Inches(2.1), Inches(7.7), Inches(4.6))
    tf = c_center.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_right = Inches(0.3)
    tf.margin_top = Inches(0.3)

    p = tf.paragraphs[0]
    p.text = "STRENGTHS & FATAL BLIND SPOTS"
    p.font.name = "Calibri"
    p.font.size = Pt(12)
    p.font.bold = True
    p.font.color.rgb = ACCENT_BLUE

    p = tf.add_paragraph()
    p.text = "The Routine Advantage:"
    p.font.name = "Calibri"
    p.font.size = Pt(14)
    p.font.bold = True
    p.font.color.rgb = NAVY
    p.space_before = Pt(8)

    p = tf.add_paragraph()
    p.text = "Gradient-boosted decision trees effectively capture complex multi-variable interactions (e.g., taxi-out queue buildup and flight bank congestion). Delivers exceptional routine accuracy (MASE = 0.680–0.700) with zero feedback latency."
    p.font.name = "Calibri"
    p.font.size = Pt(12)
    p.font.color.rgb = SLATE
    p.space_before = Pt(3)

    p = tf.add_paragraph()
    p.text = "The Brittleness Flaw (The Empty Checkpoint Fallacy):"
    p.font.name = "Calibri"
    p.font.size = Pt(14)
    p.font.bold = True
    p.font.color.rgb = AMBER_TEXT
    p.space_before = Pt(12)

    p = tf.add_paragraph()
    p.text = "During irregular operations (convective ground stops, widespread cancellations), scheduled departures vanish from the electronic airline feed. The decision tree predicts zero demand, while thousands of passengers remain stranded in terminal concourses."
    p.font.name = "Calibri"
    p.font.size = Pt(12)
    p.font.color.rgb = SLATE
    p.space_before = Pt(3)

    # ==========================================
    # SLIDE 13: HYBRID ARCHITECTURES
    # ==========================================
    s13 = prs.slides.add_slide(blank_layout)
    add_header(s13, "Literature Breakdown", "Sequential Two-Stage Hybrid Architectures (Model 3)", "Coupling Base Flight Schedules with Real-Time Dynamic Error Innovation Feedback")

    add_equation_card(
        s13, Inches(0.8), Inches(2.1), Inches(11.7), Inches(2.4),
        "Two-Stage Sequential Hybrid Formulation",
        "Ŷ_t  =  M_base(Schedule_t, Features_t)  +  α · ( Y_{t-1} - Ŷ_{t-1} )",
        "Stage 1: Base machine learning model captures cyclical flight schedules and operational covariates.\n"
        "Stage 2: Real-time 1-step error innovation feedback (e_{t-1}) injects live floor telemetry, dynamically correcting lobby backlog."
    )

    # Bottom 2 cards
    c_b1 = add_card(s13, Inches(0.8), Inches(4.8), Inches(5.6), Inches(2.0))
    tf1 = c_b1.text_frame
    tf1.word_wrap = True
    tf1.margin_left = tf1.margin_right = Inches(0.25)
    tf1.margin_top = Inches(0.15)
    p = tf1.paragraphs[0]
    p.text = "WHY STAGE 2 RESCUES DISRUPTIONS"
    p.font.name = "Calibri"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = GREEN_TEXT
    p = tf1.add_paragraph()
    p.text = "When storms ground flights, Stage 1 falsely predicts zero volume. However, the prior-hour floor observation Y_{t-1} reveals hundreds of passengers still passing through screening, instantly lifting forecasts."
    p.font.name = "Calibri"
    p.font.size = Pt(11)
    p.font.color.rgb = SLATE
    p.space_before = Pt(3)

    c_b2 = add_card(s13, Inches(6.8), Inches(4.8), Inches(5.7), Inches(2.0))
    tf2 = c_b2.text_frame
    tf2.word_wrap = True
    tf2.margin_left = tf2.margin_right = Inches(0.25)
    tf2.margin_top = Inches(0.15)
    p = tf2.paragraphs[0]
    p.text = "THE ASYMMETRIC TRADE-OFF PENALTY"
    p.font.name = "Calibri"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = AMBER_TEXT
    p = tf2.add_paragraph()
    p.text = "Requires active, low-latency API telemetry from physical checkpoint floor lanes. Furthermore, because Stage 1 overfits to specific terminal geometries, Model 3 loses spatial generalizability."
    p.font.name = "Calibri"
    p.font.size = Pt(11)
    p.font.color.rgb = SLATE
    p.space_before = Pt(3)

    # ==========================================
    # SLIDE 14: IMPACT OF COVID & VOLATILITY
    # ==========================================
    s14 = prs.slides.add_slide(blank_layout)
    add_header(s14, "Empirical Demarcation", "The Structural Impact of COVID-19 Demarcation", "Establishing Post-Pandemic Behavioral Stability (May 1, 2022 – December 31, 2025)")

    stats = [
        ("May 1, 2022", "Demarcation Cutoff", "Federal mask mandate dissolved; marks return to normal passenger behavior"),
        ("F = 1.42", "Chow Stability Test", "p = 0.18 (fails to reject null of structural stability across 44 months)"),
        ("84.7%", "Load Factor Recovery", "Systemwide passenger load factors recovered to pre-pandemic baseline")
    ]
    for i, (num_str, label_str, sub_str) in enumerate(stats):
        left = Inches(0.8 + i * 4.0)
        add_stat_box(s14, left, Inches(2.1), Inches(3.7), Inches(2.2), num_str, label_str, sub_str, NAVY)

    c_bot = add_card(s14, Inches(0.8), Inches(4.6), Inches(11.7), Inches(2.1))
    tf = c_bot.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_right = Inches(0.4)
    tf.margin_top = Inches(0.2)

    p = tf.paragraphs[0]
    p.text = "WHY POST-PANDEMIC DEMARCATION WAS CRITICAL"
    p.font.name = "Calibri"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = ACCENT_BLUE

    p = tf.add_paragraph()
    p.text = "Training machine learning algorithms across 2020–2021 severely contaminates predictive models with artificial lockdowns and erratic airline schedule retrenchments. Our CUSUM recursive residual tests confirm that commercial aviation passenger arrival dynamics stabilized into a stationary post-pandemic regime starting May 1, 2022."
    p.font.name = "Calibri"
    p.font.size = Pt(12)
    p.font.color.rgb = SLATE
    p.space_before = Pt(4)

    # ==========================================
    # SLIDE 15: IMPORTANCE OF DYNAMIC PERFORMANCE MEASURES
    # ==========================================
    s15 = prs.slides.add_slide(blank_layout)
    add_header(s15, "Evaluative Synthesis", "Why Aviation Demands Dynamic Performance Measures", "The Fatal Pitfall of Single-Metric Global Minimization in Airport Operations")

    # 3 contrasting operational cards
    cards = [
        ("Nominal Rhythms (Robustness)", "A model optimized purely for annual RMSE minimizes routine errors during sunny days. However, routine operations are computationally cheap and tolerant of minor variance.", ACCENT_BLUE),
        ("Disruption Shocks (Resilience)", "Airport crises occur during convective storm fronts. If a model collapses during IROPS (like Model 2's 2.14x error surge), it endangers terminal operations when accuracy matters most.", AMBER_TEXT),
        ("Facility Transfer (Generalizability)", "Airports cannot afford 12 months of local calibration data for newly built concourses. Models must possess zero-shot transferability across physical terminal layouts.", GREEN_TEXT)
    ]
    for i, (title_txt, desc_txt, color_accent) in enumerate(cards):
        left = Inches(0.8 + i * 4.0)
        card = add_card(s15, left, Inches(2.2), Inches(3.7), Inches(4.5))
        tf = card.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_right = Inches(0.3)
        tf.margin_top = Inches(0.3)

        p = tf.paragraphs[0]
        p.text = f"PILLAR {i+1}"
        p.font.name = "Calibri"
        p.font.size = Pt(11)
        p.font.bold = True
        p.font.color.rgb = color_accent

        p = tf.add_paragraph()
        p.text = title_txt
        p.font.name = "Calibri"
        p.font.size = Pt(16)
        p.font.bold = True
        p.font.color.rgb = NAVY
        p.space_before = Pt(8)

        p = tf.add_paragraph()
        p.text = desc_txt
        p.font.name = "Calibri"
        p.font.size = Pt(12)
        p.font.color.rgb = SLATE
        p.space_before = Pt(12)

    # ==========================================
    # SLIDE 16: METHODOLOGY OVERVIEW
    # ==========================================
    s16 = prs.slides.add_slide(blank_layout)
    add_header(s16, "Methodological Architecture", "Research Methodology Overview", "Structured 5-Part Graduate Methodology Architecture (ERAU Standards)")

    headers_5 = [
        ("3.1 Research Approach", "Non-experimental quantitative comparative design; evaluating 4 modeling paradigms across 3 operational dimensions."),
        ("3.2 Sample & Funnel", "Purposive 4-tier filtering pipeline isolating 9 commercial hub airports representing 12 carrier-exclusive screening complexes."),
        ("3.3 Sources of Data", "Synthesizing 67.2M raw federal records down to 42.1M conformed records across TSA FOIA, BTS OTP, and BTS DB1B surveys."),
        ("3.4 Validity Safeguards", "Connecting passenger deflation (DB1B), carrier screening isolation, and strict 168-hour purge buffers."),
        ("3.5 Treatment of Data", "Multi-source star schema warehouse, Tweedie count models, and out-of-time holdout evaluations.")
    ]
    for i, (head, desc) in enumerate(headers_5):
        top = Inches(2.1 + i * 0.95)
        card = add_card(s16, Inches(0.8), top, Inches(11.7), Inches(0.85))
        tf = card.text_frame
        tf.word_wrap = True
        tf.margin_left = Inches(0.3)
        tf.margin_top = Inches(0.12)

        p = tf.paragraphs[0]
        p.text = head
        p.font.name = "Calibri"
        p.font.size = Pt(13)
        p.font.bold = True
        p.font.color.rgb = NAVY

        p = tf.add_paragraph()
        p.text = desc
        p.font.name = "Calibri"
        p.font.size = Pt(11)
        p.font.color.rgb = SLATE
        p.space_before = Pt(2)

    # ==========================================
    # SLIDE 17: METHODOLOGY APPROACH
    # ==========================================
    s17 = prs.slides.add_slide(blank_layout)
    add_header(s17, "Methodology Approach", "Candidate Models & Evaluation Matrix", "Benchmarking Four Paradigms Across the Operational Evaluative Trio")

    # Table layout
    card = add_card(s17, Inches(0.8), Inches(2.1), Inches(11.7), Inches(4.6))
    tf = card.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_right = Inches(0.3)
    tf.margin_top = Inches(0.2)

    # 4 model description cards inside
    models_info = [
        ("Baseline Control", "Diurnal Persistence Benchmark", "Ŷ_t = Y_{t-24}", "Non-parametric empirical control; establishes MASE ≡ 1.000 benchmark."),
        ("Model 1", "Deterministic Flight Schedule", "Ŷ_t = ∑ [Seats · (1-S) · P(τ)]", "Convolution of airline flight banks over ACRP Report 40 lognormal show-up curves."),
        ("Model 2", "Supervised Machine Learning", "Ŷ_t = Tree(Sched, OTP_24)", "Gradient-boosted decision trees incorporating 24 BTS operational features."),
        ("Model 3", "Dynamic Two-Stage Hybrid", "Ŷ_t = M_base + α·e_{t-1}", "Sequential two-stage coupling recurring schedules with live 1-step error innovation.")
    ]
    for i, (m_id, m_name, m_eq, m_desc) in enumerate(models_info):
        left = Inches(1.1 + i * 2.8)
        sub_card = add_card(s17, left, Inches(2.4), Inches(2.6), Inches(4.0), WHITE, BORDER_CARD)
        stf = sub_card.text_frame
        stf.word_wrap = True
        stf.margin_left = stf.margin_right = Inches(0.2)
        stf.margin_top = Inches(0.2)

        p = stf.paragraphs[0]
        p.text = m_id
        p.font.name = "Calibri"
        p.font.size = Pt(12)
        p.font.bold = True
        p.font.color.rgb = ACCENT_BLUE

        p = stf.add_paragraph()
        p.text = m_name
        p.font.name = "Calibri"
        p.font.size = Pt(14)
        p.font.bold = True
        p.font.color.rgb = NAVY
        p.space_before = Pt(3)

        p = stf.add_paragraph()
        p.text = m_eq
        p.font.name = "Georgia"
        p.font.size = Pt(11)
        p.font.bold = True
        p.font.color.rgb = SLATE
        p.space_before = Pt(8)

        p = stf.add_paragraph()
        p.text = m_desc
        p.font.name = "Calibri"
        p.font.size = Pt(10.5)
        p.font.color.rgb = SLATE
        p.space_before = Pt(8)

    # ==========================================
    # SLIDE 18: METHODOLOGY DESIGN AND PROCEDURES
    # ==========================================
    s18 = prs.slides.add_slide(blank_layout)
    add_header(s18, "Design & Procedure", "Four-Phase Research Lifecycle", "Table 3.1: Systematic Progression from Federal Ingestion to Hypothesis Testing")

    phases = [
        ("PHASE 1", "Multi-Source Data Ingestion & ETL", "TSA FOIA, BTS OTP, T-100, DB1B", "Extract 67.2M raw records; conform into Star Schema warehouse (42.1M records). Quarantined 35,809 missing keys; preserved structural night zeros."),
        ("PHASE 2", "Econometric Funnel & Cohort Isolation", "4-Tier Purposive Filtering Funnel", "Filtered 450+ airports to Top 25, screened legacy carrier presence, isolated dedicated carrier terminals, yielding 9 airfields across 12 complexes."),
        ("PHASE 3", "Model Calibration & Feature Engineering", "Feature Pipeline & 84-Cell Grid", "Constructed 24 OTP features; convolved ACRP 40 show-up curves; verified 98.8% training sample sufficiency across 84-cell seasonal interaction grid."),
        ("PHASE 4", "Multi-Pillar Hypothesis Evaluation", "Out-of-Time 2025 Holdout Benchmark", "Tested models across Robustness (nominal), Resilience (severe convective storms), and Generalizability (zero-shot transfer) using Diebold-Mariano tests.")
    ]
    for i, (p_tag, p_name, p_sub, p_desc) in enumerate(phases):
        left = Inches(0.8 + i * 3.0)
        card = add_card(s18, left, Inches(2.2), Inches(2.8), Inches(4.5))
        tf = card.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_right = Inches(0.2)
        tf.margin_top = Inches(0.25)

        p = tf.paragraphs[0]
        p.text = p_tag
        p.font.name = "Calibri"
        p.font.size = Pt(11)
        p.font.bold = True
        p.font.color.rgb = ACCENT_BLUE

        p = tf.add_paragraph()
        p.text = p_name
        p.font.name = "Calibri"
        p.font.size = Pt(15)
        p.font.bold = True
        p.font.color.rgb = NAVY
        p.space_before = Pt(3)

        p = tf.add_paragraph()
        p.text = p_sub
        p.font.name = "Calibri"
        p.font.size = Pt(11)
        p.font.bold = True
        p.font.color.rgb = DARK_TEXT
        p.space_before = Pt(6)

        p = tf.add_paragraph()
        p.text = p_desc
        p.font.name = "Calibri"
        p.font.size = Pt(10.5)
        p.font.color.rgb = SLATE
        p.space_before = Pt(8)

    # ==========================================
    # SLIDE 19: METHODOLOGY DETAILS (VALIDITY & LEAKAGE SAFEGUARDS)
    # ==========================================
    s19 = prs.slides.add_slide(blank_layout)
    add_header(s19, "Validity & Safeguards", "Methodological Safeguards & Data Integrity", "Strict Prevention of Autoregressive Data Leakage and Unconfounded Isolation")

    safeguards = [
        ("The 7-Day Purge Buffer", "Table 4.8 / REC-06", "168-hour zero-training purge embargo established between training (2022–2024) and test holdout (2025). Completely prevents autoregressive memory leakage across dataset boundaries."),
        ("Connecting Passenger Deflator", "DB1B Coupon Deflation", "Deflates departing aircraft seats by true connecting ratios (S_connect up to 66.3% at DFW). Solves the Hub Disconnect where airside connections bypass TSA."),
        ("Carrier Checkpoint Isolation", "Dedicated Carrier Complexes", "Isolates screening checkpoints operated exclusively by American, Delta, or United, eliminating multi-carrier unidentifiable passenger mixing."),
        ("Strict Information Causality", "t-1 Realized Telemetry", "Models only ingest strictly prior-hour features (t-1) available in real-time operations, ensuring zero forward-looking lookahead bias.")
    ]
    for i, (title_txt, sub_txt, desc_txt) in enumerate(safeguards):
        col = i % 2
        row = i // 2
        left = Inches(0.8 + col * 6.0)
        top = Inches(2.2 + row * 2.4)
        card = add_card(s19, left, top, Inches(5.7), Inches(2.2))
        tf = card.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_right = Inches(0.3)
        tf.margin_top = Inches(0.2)

        p = tf.paragraphs[0]
        p.text = title_txt
        p.font.name = "Calibri"
        p.font.size = Pt(15)
        p.font.bold = True
        p.font.color.rgb = NAVY

        p = tf.add_paragraph()
        p.text = sub_txt.upper()
        p.font.name = "Calibri"
        p.font.size = Pt(11)
        p.font.bold = True
        p.font.color.rgb = ACCENT_BLUE
        p.space_before = Pt(2)

        p = tf.add_paragraph()
        p.text = desc_txt
        p.font.name = "Calibri"
        p.font.size = Pt(11.5)
        p.font.color.rgb = SLATE
        p.space_before = Pt(4)

    # ==========================================
    # SLIDE 20: FINDINGS & DISCUSSION ROADMAP
    # ==========================================
    s20 = prs.slides.add_slide(blank_layout)
    add_header(s20, "Results Roadmap", "Chapter IV & V Empirical Architecture", "Four Sequential Empirical Analyses Supporting Master Hypothesis Testing")

    findings = [
        ("4.1 Exploratory Analysis", "Top 25 Census & The Values vs. Volatility Discovery", "Analyzing 42.1M records; proving static volumes mask queuing while volatility metrics correlate tightly with flight delays."),
        ("4.2 Data Filtering & Cohort", "Four-Tier Purposive Filtering Pipeline", "Progression from 450+ airports to the 9-airport factorial cohort across 12 carrier-exclusive screening environments."),
        ("4.3 Model Execution", "Holdout Benchmark Matrix Across 4 Paradigms", "2025 out-of-time evaluation across Baseline Control, Model 1, Model 2, and Model 3; certified RMSE, MASE, and Bias."),
        ("4.4 Multi-Pillar Hypothesis", "Testing H₁ Across Robustness, Resilience, Transfer", "Deep-dive evaluations under nominal operations, convective IROPS shocks, and zero-shot cross-facility portability.")
    ]
    for i, (step_txt, title_txt, desc_txt) in enumerate(findings):
        top = Inches(2.1 + i * 1.15)
        card = add_card(s20, Inches(0.8), top, Inches(11.7), Inches(1.05))
        tf = card.text_frame
        tf.word_wrap = True
        tf.margin_left = Inches(0.3)
        tf.margin_top = Inches(0.15)

        p = tf.paragraphs[0]
        p.text = step_txt.upper()
        p.font.name = "Calibri"
        p.font.size = Pt(11)
        p.font.bold = True
        p.font.color.rgb = ACCENT_BLUE

        p = tf.add_paragraph()
        p.text = title_txt
        p.font.name = "Calibri"
        p.font.size = Pt(14)
        p.font.bold = True
        p.font.color.rgb = NAVY
        p.space_before = Pt(2)

        p = tf.add_paragraph()
        p.text = desc_txt
        p.font.name = "Calibri"
        p.font.size = Pt(11)
        p.font.color.rgb = SLATE
        p.space_before = Pt(2)

    # ==========================================
    # SLIDE 21: DESCRIPTIVE STATISTICS: TOP 25 VS 9-AIRPORT COHORT
    # ==========================================
    s21 = prs.slides.add_slide(blank_layout)
    add_header(s21, "Descriptive Statistics", "Empirical Baseline: 9-Airport Cohort vs. Top 25", "Table 4.7: Proving the Experimental Cohort Represents the Operational Stress Front")

    cohort_stats = [
        ("+16.9%", "Flight Movement Density", "224,576 scheduled annual flights vs. 192,160 national Top 25 average"),
        ("+14.1%", "Higher Cancellation Rate", "1.63% flight cancellation rate vs. 1.43% national Top 25 average"),
        ("+25.0%", "Local Originating Demand", "16.4M true originating passengers vs. 13.1M national Top 25 average"),
        ("+5.8%", "Elevated Arrival Volatility", "CV_TSA = 0.8728 vs. 0.8250 national Top 25 baseline average")
    ]
    for i, (num_str, label_str, sub_str) in enumerate(cohort_stats):
        left = Inches(0.8 + i * 3.0)
        add_stat_box(s21, left, Inches(2.1), Inches(2.8), Inches(2.3), num_str, label_str, sub_str, NAVY)

    c_sum = add_card(s21, Inches(0.8), Inches(4.7), Inches(11.7), Inches(2.0))
    tf = c_sum.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_right = Inches(0.4)
    tf.margin_top = Inches(0.2)

    p = tf.paragraphs[0]
    p.text = "EMPIRICAL JUSTIFICATION OF COHORT REPRESENTATIVENESS"
    p.font.name = "Calibri"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = ACCENT_BLUE

    p = tf.add_paragraph()
    p.text = "The 9-airport cohort is not a convenience sample. It captures airports with significantly higher traffic density, greater disruption exposure, and heavier landside passenger show-up volumes than the broader Top 25. This ensures that models trained on this cohort are tested under genuine operational stress."
    p.font.name = "Calibri"
    p.font.size = Pt(12)
    p.font.color.rgb = SLATE
    p.space_before = Pt(4)

    # ==========================================
    # SLIDE 22: DATA FILTERING & 4-TIER PIPELINE
    # ==========================================
    s22 = prs.slides.add_slide(blank_layout)
    add_header(s22, "Cohort Selection", "The Four-Tier Purposive Filtering Pipeline", "Table 3.2: Progressive Filtering from 450+ Commercial Airfields to 9 Balanced Hubs")

    tiers = [
        ("Macro Tier", "Commercial Network Scale", "450+ Airfields  →  Top 25 Hubs", "Filtered commercial airfields to the Top 25 large hubs representing 68% of commercial traffic, eliminating regional airfields lacking continuous high-volume queues."),
        ("Meso Tier", "Carrier Presence & Continuity", "Top 25 Hubs  →  14 Core Hubs", "Enforced continuous operational presence by American, Delta, and United. Eliminated JFK due to United's permanent operational exit in October 2022."),
        ("Micro Tier", "Physical Checkpoint Isolation", "14 Core Hubs  →  10 Airfields", "Screened for dedicated carrier checkpoints. Eliminated consolidated central checkpoint terminals (e.g. Salt Lake City) where carrier passenger flows mix."),
        ("Cohort Tier", "Factorial Operational Balance", "10 Airfields  →  9 Final Airfields", "Balanced across 4 operational clusters (Mega-Hubs, Coastal International, High-Originating, Transfer Concentrated) and 12 dedicated screening complexes.")
    ]
    for i, (t_name, t_sub, t_flow, t_desc) in enumerate(tiers):
        left = Inches(0.8 + i * 3.0)
        card = add_card(s22, left, Inches(2.2), Inches(2.8), Inches(4.5))
        tf = card.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_right = Inches(0.2)
        tf.margin_top = Inches(0.2)

        p = tf.paragraphs[0]
        p.text = t_name.upper()
        p.font.name = "Calibri"
        p.font.size = Pt(11)
        p.font.bold = True
        p.font.color.rgb = ACCENT_BLUE

        p = tf.add_paragraph()
        p.text = t_sub
        p.font.name = "Calibri"
        p.font.size = Pt(14)
        p.font.bold = True
        p.font.color.rgb = NAVY
        p.space_before = Pt(3)

        p = tf.add_paragraph()
        p.text = t_flow
        p.font.name = "Calibri"
        p.font.size = Pt(10.5)
        p.font.bold = True
        p.font.color.rgb = GREEN_TEXT
        p.space_before = Pt(6)

        p = tf.add_paragraph()
        p.text = t_desc
        p.font.name = "Calibri"
        p.font.size = Pt(10.5)
        p.font.color.rgb = SLATE
        p.space_before = Pt(8)

    # ==========================================
    # SLIDE 23: PIPELINE RESULTS: 9 AIRPORTS & 12 COMPLEXES
    # ==========================================
    s23 = prs.slides.add_slide(blank_layout)
    add_header(s23, "Cohort Specification", "The 9-Airport Experimental Cohort Specification", "Table 4.6: Factorial Representation Across 12 Carrier-Exclusive Terminal Complexes")

    airports_grid = [
        ("ATL", "Atlanta Hartsfield", "Delta Air Lines", "Domestic South Terminal"),
        ("BOS", "Boston Logan", "Delta / American", "Terminal A & Terminal B"),
        ("DFW", "Dallas/Fort Worth", "American Airlines", "Terminals A, B, C complexes"),
        ("DTW", "Detroit Metro", "Delta Air Lines", "McNamara Terminal"),
        ("EWR", "Newark Liberty", "United Airlines", "Terminal C complex"),
        ("LAX", "Los Angeles Intl", "Delta / United / AA", "Terminals 3, 4, 7 complexes"),
        ("LGA", "New York LaGuardia", "Delta Air Lines", "Terminal C (New 2022 Concourse)"),
        ("ORD", "Chicago O'Hare", "United / American", "Terminal 1 & Terminal 3"),
        ("PHL", "Philadelphia Intl", "American Airlines", "Terminals B and C")
    ]
    for i, (code, name, carrier, term) in enumerate(airports_grid):
        col = i % 3
        row = i // 3
        left = Inches(0.8 + col * 4.0)
        top = Inches(2.1 + row * 1.5)
        card = add_card(s23, left, top, Inches(3.7), Inches(1.35))
        tf = card.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_right = Inches(0.2)
        tf.margin_top = Inches(0.12)

        p = tf.paragraphs[0]
        p.text = f"{code}  ·  {name}"
        p.font.name = "Calibri"
        p.font.size = Pt(13)
        p.font.bold = True
        p.font.color.rgb = NAVY

        p = tf.add_paragraph()
        p.text = carrier
        p.font.name = "Calibri"
        p.font.size = Pt(11)
        p.font.bold = True
        p.font.color.rgb = ACCENT_BLUE
        p.space_before = Pt(2)

        p = tf.add_paragraph()
        p.text = term
        p.font.name = "Calibri"
        p.font.size = Pt(10.5)
        p.font.color.rgb = SLATE
        p.space_before = Pt(2)

    # Bottom summary pill
    c_bot = add_card(s23, Inches(0.8), Inches(5.9), Inches(11.7), Inches(0.9), WHITE, BORDER_CARD)
    tf = c_bot.text_frame
    tf.margin_left = Inches(0.3)
    tf.margin_top = Inches(0.12)
    p = tf.paragraphs[0]
    p.text = "Complete balance across Big Three carriers: American (5 complexes), Delta (5 complexes), United (4 complexes)."
    p.font.name = "Calibri"
    p.font.size = Pt(11.5)
    p.font.bold = True
    p.font.color.rgb = DARK_TEXT

    # ==========================================
    # SLIDE 24: IMPLICATIONS FOR MODEL DEVELOPMENT
    # ==========================================
    s24 = prs.slides.add_slide(blank_layout)
    add_header(s24, "Model Development", "Methodological Implications for Model Architecture", "Four Non-Negotiable Operational Principles Governing Model Formulation")

    principles = [
        ("Principle 1: Single Carrier Screening Isolation", "Ensures passenger demand feeds map 1:1 to dedicated carrier flight banks without unobserved passenger contamination from foreign airlines."),
        ("Principle 2: Mandatory DB1B Connecting Deflation", "All scheduled flight capacities are deflated by quarterly local originating shares (S_local = 1 - S_connect) to eliminate the Hub Disconnect."),
        ("Principle 3: Strict Information Availability (t-1)", "Models are restricted to information physically available prior to prediction hour t, strictly eliminating forward lookahead bias."),
        ("Principle 4: Zero-Bounded Tweedie Formulations", "Throughput is non-negative and zero-inflated during overnight curfew hours; models use compound Poisson-Gamma (Tweedie p = 1.3) objective functions.")
    ]
    for i, (title_txt, desc_txt) in enumerate(principles):
        top = Inches(2.1 + i * 1.15)
        card = add_card(s24, Inches(0.8), top, Inches(11.7), Inches(1.05))
        tf = card.text_frame
        tf.word_wrap = True
        tf.margin_left = Inches(0.3)
        tf.margin_top = Inches(0.15)

        p = tf.paragraphs[0]
        p.text = title_txt
        p.font.name = "Calibri"
        p.font.size = Pt(14)
        p.font.bold = True
        p.font.color.rgb = NAVY

        p = tf.add_paragraph()
        p.text = desc_txt
        p.font.name = "Calibri"
        p.font.size = Pt(11.5)
        p.font.color.rgb = SLATE
        p.space_before = Pt(3)

    # ==========================================
    # SLIDE 25: MODEL EXECUTION & 2025 HOLDOUT
    # ==========================================
    s25 = prs.slides.add_slide(blank_layout)
    add_header(s25, "Holdout Benchmark", "2025 Holdout Execution Benchmarks", "Table 4.10: Empirical Out-of-Time Performance Across Candidate Modeling Paradigms")

    # Table layout for Table 4.10
    headers_410 = ["Paradigm", "Model Name", "Test R²", "RMSE (pax/hr)", "MAE (pax/hr)", "Test MASE", "Bias (pax/hr)"]
    rows_410 = [
        ["Baseline Control", "Daily Persistence (t-24)", "0.6719", "253.6", "179.3", "1.000", "-0.7"],
        ["Deterministic Schedule", "Model 1 (2-Hr Lead)", "0.4980", "313.4", "215.9", "0.945", "-42.1"],
        ["Machine Learning", "Model 2 (Decision Tree + OTP)", "0.6178", "273.5", "178.0", "0.779", "-18.4"],
        ["Dynamic Hybrid", "Model 3 (Two-Stage Hybrid)", "0.7483", "222.1", "142.8", "0.662", "-8.5"]
    ]

    t_card = add_card(s25, Inches(0.8), Inches(2.1), Inches(11.7), Inches(4.7))
    tf = t_card.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_right = Inches(0.3)
    tf.margin_top = Inches(0.2)

    p = tf.paragraphs[0]
    p.text = "CERTIFIED 2025 OUT-OF-TIME HOLDOUT BENCHMARK (N = 8,760 HOURLY PERIODS)"
    p.font.name = "Calibri"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = ACCENT_BLUE

    # Draw mini cards for each model
    for i, row in enumerate(rows_410):
        top_m = Inches(2.6 + i * 0.95)
        sub_c = add_card(s25, Inches(1.1), top_m, Inches(11.1), Inches(0.85), WHITE, BORDER_CARD)
        stf = sub_c.text_frame
        stf.word_wrap = True
        stf.margin_left = Inches(0.2)
        stf.margin_top = Inches(0.12)

        p = stf.paragraphs[0]
        p.text = f"{row[1]}  ({row[0]})"
        p.font.name = "Calibri"
        p.font.size = Pt(13)
        p.font.bold = True
        p.font.color.rgb = NAVY if i < 3 else GREEN_TEXT

        p = stf.add_paragraph()
        p.text = f"Test R²: {row[2]}   |   RMSE: {row[3]} pax/hr   |   MAE: {row[4]} pax/hr   |   MASE: {row[5]}   |   Bias: {row[6]} pax/hr"
        p.font.name = "Calibri"
        p.font.size = Pt(11)
        p.font.color.rgb = SLATE
        p.space_before = Pt(2)

    # ==========================================
    # SLIDE 26: HOW TO INTERPRET FINAL RESULTS
    # ==========================================
    s26 = prs.slides.add_slide(blank_layout)
    add_header(s26, "Results Interpretation", "Interpreting Statistical & Operational Metrics", "Translating Academic Error Metrics into Checkpoint Floor Staffing Implications")

    int_cards = [
        ("Dispersion Scale vs. Volume Scale", "Why RMSE Matters in Heavy Traffic", "RMSE penalizes large peak-hour errors quadratically. Because queuing wait times explode exponentially during peak bursts, minimizing peak error (RMSE) is far more operationally valuable than minimizing median error (MAE)."),
        ("MASE as Primary Benchmark", "Mean Absolute Scaled Error (MASE)", "MASE scales forecast error relative to non-parametric daily persistence (MASE ≡ 1.000). A MASE of 0.662 indicates Model 3 delivers a 33.8% error reduction over naive staffing tables."),
        ("Conformal Staffing Buffers", "Dynamic Safety Cushions (q85)", "Rather than staffing to point forecasts, operational dispatching convolving 85th percentile conformal prediction intervals protects against 99.2% of unpredicted surge delays with only +1.2 lanes.")
    ]
    for i, (title_txt, sub_txt, desc_txt) in enumerate(int_cards):
        left = Inches(0.8 + i * 4.0)
        card = add_card(s26, left, Inches(2.2), Inches(3.7), Inches(4.5))
        tf = card.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_right = Inches(0.3)
        tf.margin_top = Inches(0.3)

        p = tf.paragraphs[0]
        p.text = f"METRIC {i+1}"
        p.font.name = "Calibri"
        p.font.size = Pt(11)
        p.font.bold = True
        p.font.color.rgb = ACCENT_BLUE

        p = tf.add_paragraph()
        p.text = title_txt
        p.font.name = "Calibri"
        p.font.size = Pt(15)
        p.font.bold = True
        p.font.color.rgb = NAVY
        p.space_before = Pt(6)

        p = tf.add_paragraph()
        p.text = sub_txt
        p.font.name = "Calibri"
        p.font.size = Pt(11.5)
        p.font.bold = True
        p.font.color.rgb = DARK_TEXT
        p.space_before = Pt(6)

        p = tf.add_paragraph()
        p.text = desc_txt
        p.font.name = "Calibri"
        p.font.size = Pt(11)
        p.font.color.rgb = SLATE
        p.space_before = Pt(8)

    # ==========================================
    # SLIDE 27: MODEL PERFORMANCE PROGRESSION
    # ==========================================
    s27 = prs.slides.add_slide(blank_layout)
    add_header(s27, "Performance Progression", "Progression of Predictive Paradigms", "From Deterministic Schedules to Machine Learning and Dynamic Error Feedback")

    progs = [
        ("Model 1: Deterministic Baseline", "Starting Point: Flight Bank Physics", "Captures coarse flight schedules but suffers negative bias (-42.1 pax/hr) during delays.\n\nMASE = 0.945 | RMSE = 313.4 pax/hr", ACCENT_BLUE),
        ("Model 2: Supervised ML", "Intermediate: Operational Covariates", "Incorporates 24 OTP features (taxi queue, cancellations, weather delays). Cuts MASE to 0.779.\n\nMASE = 0.779 | RMSE = 273.5 pax/hr", NAVY),
        ("Model 3: Dynamic Hybrid", "State-of-the-Art: Live Floor Telemetry", "Sequential coupling of schedules with prior-hour error feedback (e_{t-1}). Slashes MASE to 0.662.\n\nMASE = 0.662 | RMSE = 222.1 pax/hr", GREEN_TEXT)
    ]
    for i, (m_tag, m_title, m_desc, color_acc) in enumerate(progs):
        left = Inches(0.8 + i * 4.0)
        card = add_card(s27, left, Inches(2.2), Inches(3.7), Inches(4.5))
        tf = card.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_right = Inches(0.3)
        tf.margin_top = Inches(0.3)

        p = tf.paragraphs[0]
        p.text = m_tag.upper()
        p.font.name = "Calibri"
        p.font.size = Pt(11)
        p.font.bold = True
        p.font.color.rgb = color_acc

        p = tf.add_paragraph()
        p.text = m_title
        p.font.name = "Calibri"
        p.font.size = Pt(15)
        p.font.bold = True
        p.font.color.rgb = NAVY
        p.space_before = Pt(6)

        p = tf.add_paragraph()
        p.text = m_desc
        p.font.name = "Calibri"
        p.font.size = Pt(11.5)
        p.font.color.rgb = SLATE
        p.space_before = Pt(12)

    # ==========================================
    # SLIDE 28: MASTER MULTI-PILLAR HYPOTHESIS TESTING
    # ==========================================
    s28 = prs.slides.add_slide(blank_layout)
    add_header(s28, "Hypothesis Testing", "Table 4.11 / Table 5.4: Master Asymmetric Trade-Off Matrix", "Conclusive Proof of Hypothesis H₁ Across All Three Evaluative Dimensions")

    # 3 Summary Cards representing the dimensions
    eval_cards = [
        ("Dimension 1: Robustness (Nominal Rhythms)", "Winner: Model 3 (Lowest RMSE) & Model 2 (Pareto)", "Model 3: RMSE = 222.1, MASE = 0.662 (Target Met)\nModel 2: RMSE = 273.5, MASE = 0.680–0.700 (Target Met)\nDM Test: DM = 48.72 (p < 0.0001) confirms genuine statistical superiority over deterministic schedules.", GREEN_TEXT),
        ("Dimension 2: Resilience (Convective IROPS)", "Decisive Winner: Model 3 (Dynamic Hybrid)", "Model 3: Disruption Multiplier R_MASE = 1.05, Shock MASE = 0.694, Recovery TTR = 2.8 hours.\nModel 2: Fragile collapse (R_MASE = 2.14) due to Empty Checkpoint Fallacy.\nModel 1: Blind to delays (R_MASE = 1.32, TTR = 7.8 hours).", ACCENT_BLUE),
        ("Dimension 3: Generalizability (Zero-Shot Transfer)", "Decisive Winner: Model 1 (Deterministic)", "Model 1: Relative Transfer Ratio RTR = 1.04, Error Shift ΔMASE = +4.0% (Target Met).\nModel 3 Decisively Fails: RTR = 1.19, ΔMASE = +21.5% due to terminal geometry overfitting.", AMBER_TEXT)
    ]
    for i, (title_txt, win_txt, desc_txt, col_acc) in enumerate(eval_cards):
        top = Inches(2.1 + i * 1.55)
        card = add_card(s28, Inches(0.8), top, Inches(11.7), Inches(1.4))
        tf = card.text_frame
        tf.word_wrap = True
        tf.margin_left = Inches(0.3)
        tf.margin_top = Inches(0.12)

        p = tf.paragraphs[0]
        p.text = title_txt
        p.font.name = "Calibri"
        p.font.size = Pt(13)
        p.font.bold = True
        p.font.color.rgb = NAVY

        p = tf.add_paragraph()
        p.text = win_txt.upper()
        p.font.name = "Calibri"
        p.font.size = Pt(11)
        p.font.bold = True
        p.font.color.rgb = col_acc
        p.space_before = Pt(2)

        p = tf.add_paragraph()
        p.text = desc_txt
        p.font.name = "Calibri"
        p.font.size = Pt(10.5)
        p.font.color.rgb = SLATE
        p.space_before = Pt(2)

    # ==========================================
    # SLIDE 29: DISCUSSION & ANALYSIS OF RESULTS
    # ==========================================
    s29 = prs.slides.add_slide(blank_layout)
    add_header(s29, "Results Discussion", "Spatial Architecture & Terminal Geometry Dynamics", "How Physical Airport Layouts and Passenger Psychology Dictate Model Efficacy")

    disc_cards = [
        ("Connecting Passenger Shielding", "Hubs with high connecting ratios (DFW 66.3%, ATL 60.1%) shield checkpoints from airside flight delay cascades. Terminal screening queues are insulated because transfer passengers remain airside."),
        ("High-Originating Facility Exposure", "Origin-heavy airports (EWR 66.4% local, LGA 62.1% local) exhibit acute coupling with surface highway traffic and weather delays. Checkpoints absorb 100% of flight schedule shocks."),
        ("Terminal Complex Aggregation", "Single-carrier screening lane isolation (e.g. Delta Terminal C at LGA) eliminates noise from unrelated airline operations, allowing precise 1-step error innovation convergence.")
    ]
    for i, (title_txt, desc_txt) in enumerate(disc_cards):
        left = Inches(0.8 + i * 4.0)
        card = add_card(s29, left, Inches(2.2), Inches(3.7), Inches(4.5))
        tf = card.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_right = Inches(0.3)
        tf.margin_top = Inches(0.3)

        p = tf.paragraphs[0]
        p.text = f"DYNAMIC {i+1}"
        p.font.name = "Calibri"
        p.font.size = Pt(11)
        p.font.bold = True
        p.font.color.rgb = ACCENT_BLUE

        p = tf.add_paragraph()
        p.text = title_txt
        p.font.name = "Calibri"
        p.font.size = Pt(16)
        p.font.bold = True
        p.font.color.rgb = NAVY
        p.space_before = Pt(6)

        p = tf.add_paragraph()
        p.text = desc_txt
        p.font.name = "Calibri"
        p.font.size = Pt(11.5)
        p.font.color.rgb = SLATE
        p.space_before = Pt(12)

    # ==========================================
    # SLIDE 30: REAL WORLD APPLICATION (THE OPERATOR'S PLAYBOOK)
    # ==========================================
    s30 = prs.slides.add_slide(blank_layout)
    add_header(s30, "Operational Implementation", "Real-World Aviation Application: The Operator's Playbook", "Three Actionable Policy Recommendations for TSA and Airport Operations Centers")

    ops = [
        ("Dynamic Checkpoint Rostering", "Replace Static Tables with 2-Hr Lead Convolutions", "TSA Federal Security Directors must abandon static time-of-day tables. Deploy dynamic staffing rosters driven by t+2 scheduled flight bank convolutions convolved with conformal safety buffers."),
        ("Connecting Ratio Deflation", "Integrate Bureau of Transportation Statistics O&D Data", "Centralized security scheduling systems must dynamically deflate scheduled flight seats using airline O&D transfer ratios, preventing chronic over-staffing at connecting hub complexes."),
        ("The Regime-Switched Gated Engine", "Automated Operational Model Switching Architecture", "Deploy Model 2 (Supervised ML) during nominal on-time operations for zero-latency interpretable dispatch. Instantly switch to Model 3 (Dynamic Hybrid) when ground stop delays exceed 45 minutes.")
    ]
    for i, (title_txt, sub_txt, desc_txt) in enumerate(ops):
        top = Inches(2.1 + i * 1.55)
        card = add_card(s30, Inches(0.8), top, Inches(11.7), Inches(1.4))
        tf = card.text_frame
        tf.word_wrap = True
        tf.margin_left = Inches(0.3)
        tf.margin_top = Inches(0.12)

        p = tf.paragraphs[0]
        p.text = title_txt
        p.font.name = "Calibri"
        p.font.size = Pt(14)
        p.font.bold = True
        p.font.color.rgb = NAVY

        p = tf.add_paragraph()
        p.text = sub_txt.upper()
        p.font.name = "Calibri"
        p.font.size = Pt(11)
        p.font.bold = True
        p.font.color.rgb = ACCENT_BLUE
        p.space_before = Pt(2)

        p = tf.add_paragraph()
        p.text = desc_txt
        p.font.name = "Calibri"
        p.font.size = Pt(11)
        p.font.color.rgb = SLATE
        p.space_before = Pt(3)

    # ==========================================
    # SLIDE 31: RECOMMENDATIONS FOR FUTURE RESEARCH
    # ==========================================
    s31 = prs.slides.add_slide(blank_layout)
    add_header(s31, "Future Directions", "Recommendations for Future Aviation Research", "Next Frontiers in Airport Queuing Analytics and Multi-Modal Telemetry")

    futures = [
        ("Granular Lane-Type Telemetry", "Disaggregating checkpoint counts by lane type—specifically isolating TSA PreCheck, standard screening, and CLEAR biometric lanes to model lane switching behaviors."),
        ("Multi-Modal Ground Telemetry", "Integrating highway traffic sensor feeds, parking shuttle tracking, and regional rail telemetry into landside arrival feature pipelines."),
        ("Multi-Step Ahead Recursive Hybrids", "Extending the 1-step error innovation feedback framework to multi-step recursive forecasting horizons (t+2 through t+6 hours) for tactical shift scheduling.")
    ]
    for i, (title_txt, desc_txt) in enumerate(futures):
        left = Inches(0.8 + i * 4.0)
        card = add_card(s31, left, Inches(2.2), Inches(3.7), Inches(4.5))
        tf = card.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_right = Inches(0.3)
        tf.margin_top = Inches(0.3)

        p = tf.paragraphs[0]
        p.text = f"OPPORTUNITY {i+1}"
        p.font.name = "Calibri"
        p.font.size = Pt(11)
        p.font.bold = True
        p.font.color.rgb = ACCENT_BLUE

        p = tf.add_paragraph()
        p.text = title_txt
        p.font.name = "Calibri"
        p.font.size = Pt(16)
        p.font.bold = True
        p.font.color.rgb = NAVY
        p.space_before = Pt(6)

        p = tf.add_paragraph()
        p.text = desc_txt
        p.font.name = "Calibri"
        p.font.size = Pt(11.5)
        p.font.color.rgb = SLATE
        p.space_before = Pt(12)

    # ==========================================
    # SLIDE 32: CONCLUSION
    # ==========================================
    s32 = prs.slides.add_slide(blank_layout)
    # Matching title aesthetic
    top_bar32 = s32.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(0.35))
    top_bar32.fill.solid()
    top_bar32.fill.fore_color.rgb = NAVY
    top_bar32.line.fill.background()

    c_concl = add_card(s32, Inches(1.2), Inches(1.5), Inches(10.9), Inches(5.2), WHITE, BORDER_CARD)
    tf = c_concl.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_right = Inches(0.5)
    tf.margin_top = Inches(0.4)

    p = tf.paragraphs[0]
    p.text = "RESEARCH SYNTHESIS & CONCLUDING TAKEAWAY"
    p.font.name = "Calibri"
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = ACCENT_BLUE
    p.alignment = PP_ALIGN.CENTER

    p = tf.add_paragraph()
    p.text = "Transforming Airport Security from Reactive Firefighting\nto Resilient Stochastic Synchronization"
    p.font.name = "Calibri"
    p.font.size = Pt(26)
    p.font.bold = True
    p.font.color.rgb = NAVY
    p.alignment = PP_ALIGN.CENTER
    p.space_before = Pt(10)
    p.space_after = Pt(16)

    takeaways = [
        "1. Volatility Governs Heavy Traffic: Under Kingman's law, arrival burstiness (Ca²) causes queue delay explosions, proving static headcounts are fundamentally insufficient.",
        "2. The Asymmetric Trade-Off (H1): Model 1 wins zero-shot transferability; Model 2 wins routine Pareto efficiency; Model 3 wins shock resilience during severe convective storms.",
        "3. Defeating the Empty Checkpoint Fallacy: Dynamic error innovation feedback rescues machine learning from storm-induced lobby under-staffing.",
        "4. Operational Viability: Implementing the Regime-Switched Gated Engine delivers mathematically proven resilience without sacrificing routine operational efficiency."
    ]
    for t in takeaways:
        p = tf.add_paragraph()
        p.text = t
        p.font.name = "Calibri"
        p.font.size = Pt(12)
        p.font.color.rgb = SLATE
        p.space_before = Pt(8)

    p = tf.add_paragraph()
    p.text = "Thank you for your guidance, mentorship, and support throughout this graduate thesis."
    p.font.name = "Calibri"
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = ACCENT_BLUE
    p.alignment = PP_ALIGN.CENTER
    p.space_before = Pt(18)

    prs.save(output_path)
    print(f"Successfully generated clean recommended presentation at: {output_path}")

if __name__ == "__main__":
    out = "/Users/leilagleich/Library/CloudStorage/OneDrive-Embry-RiddleAeronauticalUniversity/final-thesis/Recommended-Thesis-Defense-Deck.pptx"
    create_deck(out)
