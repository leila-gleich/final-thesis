"""
generate_recommended_defense_deck.py
Author: Leila Gleich
Degree: Master of Science in Aeronautics (MSAA / Gleich 700B)
Institution: Embry-Riddle Aeronautical University

Generates Recommended-Thesis-Defense-Deck.pptx adhering strictly to
RECOMMENDED_SLIDE_VISUALIZATIONS.md and executive design principles:
- 16:9 Widescreen (13.333" x 7.5")
- ZERO raster screenshot dumps / images
- Centered mathematical display equations using clean typography
- Native PowerPoint tables (APA 7 styling)
- SmartArt-style process flows, metric KPI blocks, and multi-column comparison cards
- High contrast, ample whitespace, uncluttered executive presentation
"""

import os
import shutil
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE

BASE_DIR = "/Users/leilagleich/Library/CloudStorage/OneDrive-Embry-RiddleAeronauticalUniversity/final-thesis"
OUTPUT_PATH = os.path.join(BASE_DIR, "Recommended-Thesis-Defense-Deck.pptx")
MIRROR_PATH = os.path.join(BASE_DIR, "master-docs", "Recommended-Thesis-Defense-Deck.pptx")

# ==============================================================================
# COLOR PALETTE (ERAU Executive Theme)
# ==============================================================================
NAVY = RGBColor(10, 34, 64)          # ERAU Deep Navy (#0A2240) - Primary
BLUE_ACCENT = RGBColor(37, 99, 235)  # Aviation Blue (#2563EB) - Active / Kicker
SLATE = RGBColor(71, 85, 105)        # Slate Grey (#475569) - Subtitles / Labels
DARK_TEXT = RGBColor(15, 23, 42)     # Charcoal Body Text (#0F172A)
MUTED_TEXT = RGBColor(100, 116, 139) # Secondary Muted Grey (#64748B)
SOFT_BG = RGBColor(248, 250, 252)    # Subtle Card Fill (#F8FAFC)
WHITE = RGBColor(255, 255, 255)      # Pure White
LINE_BORDER = RGBColor(226, 232, 240)# Hairline Border (#E2E8F0)
GREEN = RGBColor(22, 101, 52)        # Dark Forest Green (#166534) - Passed / Success
AMBER = RGBColor(180, 83, 9)         # Dark Amber (#B45309) - Fragility / Alert
LIGHT_BLUE = RGBColor(239, 246, 255) # Light Blue Accent Fill (#EFF6FF)
LIGHT_GREEN = RGBColor(240, 253, 244)# Light Green Accent Fill (#F0FDF4)
LIGHT_AMBER = RGBColor(254, 243, 199)# Light Amber Accent Fill (#FEF3C7)


def create_deck():
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    # ==========================================================================
    # HELPER FUNCTIONS
    # ==========================================================================
    def add_header(slide, tracker, title, subtitle=None):
        """Header with tracker kicker, title, and optional subtitle."""
        box = slide.shapes.add_textbox(Inches(0.8), Inches(0.4), Inches(11.733), Inches(1.15))
        tf = box.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0

        p0 = tf.paragraphs[0]
        p0.text = tracker.upper()
        p0.font.name = "Calibri"
        p0.font.size = Pt(10)
        p0.font.bold = True
        p0.font.color.rgb = BLUE_ACCENT

        p1 = tf.add_paragraph()
        p1.text = title
        p1.font.name = "Calibri"
        p1.font.size = Pt(22)
        p1.font.bold = True
        p1.font.color.rgb = NAVY
        p1.space_before = Pt(3)

        if subtitle:
            p2 = tf.add_paragraph()
            p2.text = subtitle
            p2.font.name = "Calibri"
            p2.font.size = Pt(12)
            p2.font.color.rgb = SLATE
            p2.space_before = Pt(2)

    def add_card(slide, left, top, width, height, bg_color=SOFT_BG, border_color=LINE_BORDER):
        """Clean rectangular card with hairline border."""
        shape = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, left, top, width, height)
        shape.fill.solid()
        shape.fill.fore_color.rgb = bg_color
        shape.line.color.rgb = border_color
        shape.line.width = Pt(1)
        return shape

    def add_kpi_card(slide, left, top, width, height, stat_value, stat_label, subtext=None, border_color=LINE_BORDER, bg_color=WHITE):
        """High-impact KPI callout block."""
        card = add_card(slide, left, top, width, height, bg_color, border_color)
        tf = card.text_frame
        tf.word_wrap = True
        tf.vertical_anchor = MSO_ANCHOR.MIDDLE
        tf.margin_left = tf.margin_right = Inches(0.2)
        tf.margin_top = tf.margin_bottom = Inches(0.15)

        p0 = tf.paragraphs[0]
        p0.text = stat_value
        p0.font.name = "Calibri"
        p0.font.size = Pt(28)
        p0.font.bold = True
        p0.font.color.rgb = NAVY
        p0.alignment = PP_ALIGN.CENTER

        p1 = tf.add_paragraph()
        p1.text = stat_label.upper()
        p1.font.name = "Calibri"
        p1.font.size = Pt(10)
        p1.font.bold = True
        p1.font.color.rgb = BLUE_ACCENT
        p1.alignment = PP_ALIGN.CENTER
        p1.space_before = Pt(4)

        if subtext:
            p2 = tf.add_paragraph()
            p2.text = subtext
            p2.font.name = "Calibri"
            p2.font.size = Pt(9.5)
            p2.font.color.rgb = SLATE
            p2.alignment = PP_ALIGN.CENTER
            p2.space_before = Pt(4)
        return card

    def add_centered_equation(slide, left, top, width, height, title, formula, subtext_lines=None, bg_color=WHITE):
        """Centered display mathematical formula card."""
        card = add_card(slide, left, top, width, height, bg_color, LINE_BORDER)
        tf = card.text_frame
        tf.word_wrap = True
        tf.vertical_anchor = MSO_ANCHOR.MIDDLE
        tf.margin_left = tf.margin_right = Inches(0.3)
        tf.margin_top = tf.margin_bottom = Inches(0.15)

        p0 = tf.paragraphs[0]
        p0.text = title.upper()
        p0.font.name = "Calibri"
        p0.font.size = Pt(10)
        p0.font.bold = True
        p0.font.color.rgb = BLUE_ACCENT
        p0.alignment = PP_ALIGN.CENTER

        p1 = tf.add_paragraph()
        p1.text = formula
        p1.font.name = "Georgia"
        p1.font.size = Pt(18)
        p1.font.bold = True
        p1.font.color.rgb = NAVY
        p1.alignment = PP_ALIGN.CENTER
        p1.space_before = Pt(6)
        p1.space_after = Pt(6)

        if subtext_lines:
            for line in subtext_lines:
                p = tf.add_paragraph()
                p.text = line
                p.font.name = "Calibri"
                p.font.size = Pt(10.5)
                p.font.color.rgb = SLATE
                p.alignment = PP_ALIGN.CENTER
                p.space_before = Pt(2)
        return card

    def add_process_steps(slide, top_y, steps, width=Inches(11.733), height=Inches(1.15)):
        """Horizontal connected process flow."""
        n = len(steps)
        gap = Inches(0.18)
        step_w = (width - gap * (n - 1)) / n
        left_start = Inches(0.8)

        for i, (num, title, sub) in enumerate(steps):
            x = left_start + i * (step_w + gap)
            shape = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, x, top_y, step_w, height)
            shape.fill.solid()
            shape.fill.fore_color.rgb = NAVY if i == n-1 else SOFT_BG
            shape.line.color.rgb = NAVY if i == n-1 else LINE_BORDER
            shape.line.width = Pt(1)

            tf = shape.text_frame
            tf.word_wrap = True
            tf.vertical_anchor = MSO_ANCHOR.MIDDLE
            tf.margin_left = tf.margin_right = Inches(0.12)

            p0 = tf.paragraphs[0]
            p0.text = f"{num}  ·  {title}"
            p0.font.name = "Calibri"
            p0.font.size = Pt(11)
            p0.font.bold = True
            p0.font.color.rgb = WHITE if i == n-1 else NAVY

            p1 = tf.add_paragraph()
            p1.text = sub
            p1.font.name = "Calibri"
            p1.font.size = Pt(9.5)
            p1.font.color.rgb = MUTED_TEXT if i == n-1 else SLATE
            p1.space_before = Pt(3)

    # ==========================================================================
    # SLIDE 1: TITLE SLIDE
    # ==========================================================================
    s1 = prs.slides.add_slide(blank_layout)
    top_band = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(0.25))
    top_band.fill.solid()
    top_band.fill.fore_color.rgb = NAVY
    top_band.line.fill.background()

    tb = s1.shapes.add_textbox(Inches(1.0), Inches(1.8), Inches(11.333), Inches(4.8))
    tf1 = tb.text_frame
    tf1.word_wrap = True

    p = tf1.paragraphs[0]
    p.text = "EMBRY-RIDDLE AERONAUTICAL UNIVERSITY  |  GRADUATE THESIS DEFENSE"
    p.font.name = "Calibri"
    p.font.size = Pt(12)
    p.font.bold = True
    p.font.color.rgb = BLUE_ACCENT

    p = tf1.add_paragraph()
    p.text = "Evaluating Predictive Techniques to Model\nStochastic Airport Passenger Flow"
    p.font.name = "Calibri"
    p.font.size = Pt(38)
    p.font.bold = True
    p.font.color.rgb = NAVY
    p.space_before = Pt(16)
    p.space_after = Pt(16)

    p = tf1.add_paragraph()
    p.text = "An Evaluation of Multi-Pillar Performance Measures for TSA Throughput Volatility"
    p.font.name = "Calibri"
    p.font.size = Pt(16)
    p.font.color.rgb = SLATE

    p = tf1.add_paragraph()
    p.text = "Candidate: Leila Gleich  ·  Master of Science in Aeronautics (MSAA / Gleich 700B)  ·  October 2026"
    p.font.name = "Calibri"
    p.font.size = Pt(13)
    p.font.color.rgb = MUTED_TEXT
    p.space_before = Pt(38)

    # ==========================================================================
    # SLIDE 2: PRESENTATION OUTLINE / ROADMAP
    # ==========================================================================
    s2 = prs.slides.add_slide(blank_layout)
    add_header(s2, "Executive Roadmap", "Defense Presentation Roadmap", "25-Minute Structured Oral Examination across Six Operational Phases")

    roadmap_steps = [
        ("01", "The Research Problem", "Queuing Friction, Kingman's heavy-traffic law & terminal capacity limits"),
        ("02", "Evolution of Literature", "Schedules, micro-simulation, ML fragility & dynamic two-stage hybrids"),
        ("03", "Econometric Data Pipeline", "Star schema, 4-tier filtering, carrier isolation & leakage purge buffer"),
        ("04", "Empirical Volatility Regimes", "Values vs. volatility discovery, macro seasonality & diurnal asynchrony"),
        ("05", "Holdout & Hypothesis Testing", "2025 out-of-time evaluation across Robustness, Resilience & Generalizability"),
        ("06", "Operational Playbook", "Dynamic checkpoint rostering, connecting deflator & regime-switched engine")
    ]

    # Render as a 2x3 matrix of structured process cards
    col_w = Inches(3.75)
    row_h = Inches(2.2)
    gap_x = Inches(0.24)
    gap_y = Inches(0.25)

    for idx, (num, title, desc) in enumerate(roadmap_steps):
        r = idx // 3
        c = idx % 3
        x = Inches(0.8) + c * (col_w + gap_x)
        y = Inches(1.85) + r * (row_h + gap_y)

        card = add_card(s2, x, y, col_w, row_h, bg_color=WHITE, border_color=LINE_BORDER)
        tf = card.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_right = Inches(0.25)
        tf.margin_top = tf.margin_bottom = Inches(0.2)

        p = tf.paragraphs[0]
        p.text = f"SECTION {num}"
        p.font.name = "Calibri"
        p.font.size = Pt(10)
        p.font.bold = True
        p.font.color.rgb = BLUE_ACCENT

        p = tf.add_paragraph()
        p.text = title
        p.font.name = "Calibri"
        p.font.size = Pt(14)
        p.font.bold = True
        p.font.color.rgb = NAVY
        p.space_before = Pt(3)

        p = tf.add_paragraph()
        p.text = desc
        p.font.name = "Calibri"
        p.font.size = Pt(10.5)
        p.font.color.rgb = SLATE
        p.space_before = Pt(6)

    # ==========================================================================
    # SLIDE 3: THE TERMINAL QUEUING PROBLEM (KINGMAN'S FRICTION)
    # ==========================================================================
    s3 = prs.slides.add_slide(blank_layout)
    add_header(s3, "Theoretical Foundation", "The Terminal Queuing Problem", "Why Heavy-Traffic Checkpoints Fail Under Static Capacity Assumptions")

    # Left: Centered Kingman Math Equation Card
    add_centered_equation(
        s3, Inches(0.8), Inches(1.85), Inches(5.7), Inches(5.0),
        title="Kingman's Heavy-Traffic Approximation",
        formula="W̄q  ≈  ( ρ / (1 - ρ) ) · [ ( Ca² + Cs² ) / 2 ] · ( 1 / μ )",
        subtext_lines=[
            "ρ → 1.0 : Checkpoint lane utilization approaching saturation capacity",
            "Ca² : Arrival burstiness. Queuing delay scales QUADRATICALLY with arrival volatility!",
            "Cs² : Screening inspection variability across passenger streams",
            "μ : Sustainable service throughput per active AIT lane",
            "",
            "Core Takeaway: Under peak flight banks, arrival volatility",
            "drives catastrophic queuing surges even when mean volume is stable."
        ]
    )

    # Right: Operational Friction Mechanism (2 Cards)
    c1 = add_card(s3, Inches(6.8), Inches(1.85), Inches(5.733), Inches(2.35), WHITE, LINE_BORDER)
    tf = c1.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_right = Inches(0.25)
    tf.margin_top = Inches(0.2)
    p = tf.paragraphs[0]
    p.text = "INFLEXIBLE PHYSICAL CAPACITY"
    p.font.bold = True
    p.font.size = Pt(11)
    p.font.color.rgb = AMBER
    p = tf.add_paragraph()
    p.text = "Physical AIT screening lanes and certified TSO shifts cannot flex instantaneously to meet sudden passenger spikes. Rosters are locked weeks in advance, leaving checkpoints vulnerable to demand shocks."
    p.font.size = Pt(11)
    p.font.color.rgb = DARK_TEXT
    p.space_before = Pt(6)

    c2 = add_card(s3, Inches(6.8), Inches(4.5), Inches(5.733), Inches(2.35), WHITE, LINE_BORDER)
    tf = c2.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_right = Inches(0.25)
    tf.margin_top = Inches(0.2)
    p = tf.paragraphs[0]
    p.text = "TEMPORAL ASYNCHRONY & LEAD TIME"
    p.font.bold = True
    p.font.size = Pt(11)
    p.font.color.rgb = BLUE_ACCENT
    p = tf.add_paragraph()
    p.text = "Passenger screening arrivals precede flight departures by 2 hours (t-2). Flight delays cascade into late afternoon and evening banks, decoupling flight schedules from checkpoint demand and creating severe operational friction."
    p.font.size = Pt(11)
    p.font.color.rgb = DARK_TEXT
    p.space_before = Pt(6)

    # ==========================================================================
    # SLIDE 4: RESEARCH PURPOSE & OBJECTIVES
    # ==========================================================================
    s4 = prs.slides.add_slide(blank_layout)
    add_header(s4, "Research Formulation", "Research Purpose & Operational Objectives", "Pivoting from Static Headcounts to Stochastic Volatility Dynamics")

    obj_cards = [
        ("01", "PIVOT TO VOLATILITY",
         "Shift the modeling target away from static hourly headcounts to throughput volatility: standard deviation (σ_TSA) and scale-free burstiness (CV_TSA). Queuing theory dictates that arrival variance governs delay cascades."),
        ("02", "MULTI-PARADIGM BENCHMARK",
         "Conduct a rigorous out-of-time evaluation benchmarking 3 distinct candidate paradigms—Deterministic Schedules, Supervised Machine Learning, and Dynamic Hybrids—against a non-parametric persistence control."),
        ("03", "CONTEXT-AWARE OPTIMALITY",
         "Prove that model superiority is strictly contingent upon the operational priority: routine accuracy (Robustness), storm shock recovery (Resilience), or zero-shot spatial transfer (Generalizability).")
    ]

    card_w = Inches(3.75)
    for i, (num, title, body) in enumerate(obj_cards):
        x = Inches(0.8) + i * Inches(3.99)
        card = add_card(s4, x, Inches(1.85), card_w, Inches(5.0), WHITE, LINE_BORDER)
        tf = card.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_right = Inches(0.3)
        tf.margin_top = Inches(0.35)

        p = tf.paragraphs[0]
        p.text = f"OBJECTIVE {num}"
        p.font.bold = True
        p.font.size = Pt(10)
        p.font.color.rgb = BLUE_ACCENT

        p = tf.add_paragraph()
        p.text = title
        p.font.bold = True
        p.font.size = Pt(14)
        p.font.color.rgb = NAVY
        p.space_before = Pt(4)

        p = tf.add_paragraph()
        p.text = body
        p.font.size = Pt(11)
        p.font.color.rgb = DARK_TEXT
        p.space_before = Pt(12)

    # ==========================================================================
    # SLIDE 5: PRIMARY RESEARCH QUESTION (RQ1)
    # ==========================================================================
    s5 = prs.slides.add_slide(blank_layout)
    add_header(s5, "Core Inquiry", "Primary Research Question", "Formalizing Model Selection Across Three Disparate Operational Dimensions")

    # Top Quote Card
    q_card = add_card(s5, Inches(0.8), Inches(1.85), Inches(11.733), Inches(2.0), SOFT_BG, LINE_BORDER)
    tf = q_card.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_right = Inches(0.35)
    tf.margin_top = Inches(0.2)
    p = tf.paragraphs[0]
    p.text = "PRIMARY RESEARCH QUESTION (RQ₁)"
    p.font.bold = True
    p.font.size = Pt(10)
    p.font.color.rgb = BLUE_ACCENT

    p = tf.add_paragraph()
    p.text = "“Which predictive modeling frameworks—spanning deterministic persistence controls, deterministic schedule baselines, supervised machine learning, and dynamic two-stage hybrids—are most effective for forecasting airport passenger security screening throughput volatility when prioritizing Robustness, Resilience, or Generalizability as the primary operational evaluation metric?”"
    p.font.name = "Georgia"
    p.font.size = Pt(13)
    p.font.italic = True
    p.font.color.rgb = NAVY
    p.space_before = Pt(6)

    # Bottom Triad of Operational Prioritizations
    triad = [
        ("PRIORITY 1", "ROBUSTNESS", "Routine Daily Operations", "Delays < 15 min, 0 cancellations (FAA A14 reference). Focus is minimizing daily error (MASE < 0.700) and compute latency."),
        ("PRIORITY 2", "RESILIENCE", "Irregular Operations (IROPS)", "Convective storms, ground stops, delays ≥ 45 min, cancellations ≥ 5. Focus is shock recovery multiplier (R_MASE ≈ 1.00) and TTR < 4.0h."),
        ("PRIORITY 3", "GENERALIZABILITY", "Zero-Shot Spatial Transfer", "Concourse portability without local retraining (EWR → LGA). Focus is transfer ratio (RTR ≤ 1.05) and ΔMASE ≤ 10.0%.")
    ]

    card_w = Inches(3.75)
    for i, (kicker, title, sub, desc) in enumerate(triad):
        x = Inches(0.8) + i * Inches(3.99)
        card = add_card(s5, x, Inches(4.15), card_w, Inches(2.7), WHITE, LINE_BORDER)
        tf = card.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_right = Inches(0.25)
        tf.margin_top = Inches(0.2)

        p = tf.paragraphs[0]
        p.text = kicker
        p.font.bold = True
        p.font.size = Pt(9.5)
        p.font.color.rgb = BLUE_ACCENT

        p = tf.add_paragraph()
        p.text = title
        p.font.bold = True
        p.font.size = Pt(13)
        p.font.color.rgb = NAVY
        p.space_before = Pt(2)

        p = tf.add_paragraph()
        p.text = sub
        p.font.size = Pt(10)
        p.font.bold = True
        p.font.color.rgb = SLATE
        p.space_before = Pt(2)

        p = tf.add_paragraph()
        p.text = desc
        p.font.size = Pt(10)
        p.font.color.rgb = DARK_TEXT
        p.space_before = Pt(6)

    # ==========================================================================
    # SLIDE 6: MASTER HYPOTHESIS: THE ASYMMETRIC TRADE-OFF (H1)
    # ==========================================================================
    s6 = prs.slides.add_slide(blank_layout)
    add_header(s6, "Theoretical Formulation", "Hypothesis: The Asymmetric Trade-Off (H₁)", "Proving that Model Superiority is Inherently Context-Dependent")

    # Top Anchor Banner
    h1_card = add_card(s6, Inches(0.8), Inches(1.85), Inches(11.733), Inches(1.2), NAVY, NAVY)
    tf = h1_card.text_frame
    tf.word_wrap = True
    tf.vertical_anchor = MSO_ANCHOR.MIDDLE
    tf.margin_left = tf.margin_right = Inches(0.3)
    p = tf.paragraphs[0]
    p.text = "MASTER HYPOTHESIS (H₁)"
    p.font.bold = True
    p.font.size = Pt(10)
    p.font.color.rgb = WHITE
    p = tf.add_paragraph()
    p.text = "Across candidate paradigms, no individual model is universally dominant across all three performance measures."
    p.font.name = "Georgia"
    p.font.bold = True
    p.font.size = Pt(14)
    p.font.color.rgb = WHITE
    p.space_before = Pt(2)

    # 3 Comparative Sub-Hypothesis Cards
    subs = [
        ("H1a", "ROBUSTNESS HYPOTHESIS", "Machine Learning & Hybrids Satisfy Target",
         "Under nominal conditions (delays < 15m), Supervised ML (Model 2) and Dynamic Hybrid (Model 3) achieve MASE < 0.700. Deterministic flight schedules fail to meet the target due to rigid capacity assumptions.",
         GREEN),
        ("H1b", "RESILIENCE HYPOTHESIS", "Dynamic Hybrid is Sole Resilient Winner",
         "Under convective IROPS shocks (delays ≥ 45m), Dynamic Hybrid (Model 3) maintains shock stability (R_MASE ≈ 1.05). Supervised ML collapses (R = 2.14) due to the Empty Checkpoint Fallacy.",
         GREEN),
        ("H1c", "GENERALIZABILITY HYPOTHESIS", "Deterministic Schedules Win Spatial Transfer",
         "Under zero-shot concourse transfer (EWR → LGA), Deterministic Schedule (Model 1) achieves ΔMASE ≤ 10%. Dynamic Hybrids fail (ΔMASE = +21.5%) due to decision tree terminal geometry overfitting.",
         GREEN)
    ]

    card_w = Inches(3.75)
    for i, (tag, title, sub, desc, border) in enumerate(subs):
        x = Inches(0.8) + i * Inches(3.99)
        card = add_card(s6, x, Inches(3.3), card_w, Inches(3.55), WHITE, LINE_BORDER)
        tf = card.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_right = Inches(0.25)
        tf.margin_top = Inches(0.25)

        p = tf.paragraphs[0]
        p.text = tag
        p.font.bold = True
        p.font.size = Pt(10)
        p.font.color.rgb = BLUE_ACCENT

        p = tf.add_paragraph()
        p.text = title
        p.font.bold = True
        p.font.size = Pt(12)
        p.font.color.rgb = NAVY
        p.space_before = Pt(2)

        p = tf.add_paragraph()
        p.text = sub
        p.font.bold = True
        p.font.size = Pt(10)
        p.font.color.rgb = SLATE
        p.space_before = Pt(4)

        p = tf.add_paragraph()
        p.text = desc
        p.font.size = Pt(10.5)
        p.font.color.rgb = DARK_TEXT
        p.space_before = Pt(10)

    # ==========================================================================
    # SLIDE 7: MULTI-PILLAR PERFORMANCE FRAMEWORK
    # ==========================================================================
    s7 = prs.slides.add_slide(blank_layout)
    add_header(s7, "Evaluative Trio", "The Multi-Pillar Performance Framework", "Why Single Global Metrics Fail Operational Decision-Makers")

    # Left: The Trade-off Dilemma
    c_left = add_card(s7, Inches(0.8), Inches(1.85), Inches(5.6), Inches(5.0), WHITE, LINE_BORDER)
    tf = c_left.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_right = Inches(0.3)
    tf.margin_top = Inches(0.3)

    p = tf.paragraphs[0]
    p.text = "THE ASYMMETRIC TRADE-OFF SPACE"
    p.font.bold = True
    p.font.size = Pt(11)
    p.font.color.rgb = BLUE_ACCENT

    p = tf.add_paragraph()
    p.text = "Operational Reality vs. Algorithmic Specialization"
    p.font.bold = True
    p.font.size = Pt(14)
    p.font.color.rgb = NAVY
    p.space_before = Pt(4)

    bullets = [
        "Traditional evaluations rely on annual aggregate RMSE, pooling all 8,760 hours of the year into a single metric.",
        "Aggregate error is 90% dominated by routine, calm hours. A model can boast excellent annual RMSE while completely collapsing during severe afternoon storms.",
        "Airport directors cannot manage checkpoints with a single metric: morning peak staffing requires low latency, convective storms demand shock resilience, and terminal expansion requires zero-shot spatial transfer.",
        "Conclusion: Model selection must be formulated across three mutually non-collinear operational pillars."
    ]
    for b in bullets:
        p = tf.add_paragraph()
        p.text = f"•  {b}"
        p.font.size = Pt(10.5)
        p.font.color.rgb = DARK_TEXT
        p.space_before = Pt(8)

    # Right: 3 Specification Strips
    strips = [
        ("PILLAR 1: ROBUSTNESS", "Routine Daily Operations (Nominal)",
         "Evaluates accuracy under calm conditions (delays < 15m, 0 cancels).\n• Stated Target: MASE < 0.700\n• Focus: Lowest routine RMSE and zero-latency inference dispatch."),
        ("PILLAR 2: RESILIENCE", "Disruption Shock Stability (IROPS)",
         "Evaluates model stability under convective storms (delays ≥ 45m, cancels ≥ 5).\n• Stated Target: R_MASE ≈ 1.00 & TTR < 4.0h\n• Focus: Overcoming the Empty Checkpoint Fallacy."),
        ("PILLAR 3: GENERALIZABILITY", "Zero-Shot Spatial Transferability",
         "Evaluates model transfer from EWR to LGA without concourse retraining.\n• Stated Target: Relative Transfer Ratio RTR ≤ 1.05 & ΔMASE ≤ 10.0%\n• Focus: Invariance to physical checkpoint terminal layouts.")
    ]

    for i, (title, sub, text) in enumerate(strips):
        y = Inches(1.85) + i * Inches(1.72)
        card = add_card(s7, Inches(6.7), y, Inches(5.833), Inches(1.55), SOFT_BG, LINE_BORDER)
        tf = card.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_right = Inches(0.25)
        tf.margin_top = Inches(0.15)

        p = tf.paragraphs[0]
        p.text = title
        p.font.bold = True
        p.font.size = Pt(10.5)
        p.font.color.rgb = NAVY

        p = tf.add_paragraph()
        p.text = sub
        p.font.bold = True
        p.font.size = Pt(9.5)
        p.font.color.rgb = BLUE_ACCENT
        p.space_before = Pt(2)

        p = tf.add_paragraph()
        p.text = text
        p.font.size = Pt(9.5)
        p.font.color.rgb = DARK_TEXT
        p.space_before = Pt(3)

    # ==========================================================================
    # SLIDE 8: EVOLUTION OF TERMINAL FLOW LITERATURE
    # ==========================================================================
    s8 = prs.slides.add_slide(blank_layout)
    add_header(s8, "Theoretical Evolution", "Evolution of Terminal Flow Literature", "From Static Flight Bank Convolutions to Dynamic Error Feedback")

    # Top Timeline Process
    lit_steps = [
        ("1990s", "Deterministic Schedules", "Flight bank show-up curves (ACRP Report 40). Transparent, but blind to delay cascades."),
        ("2000s", "Micro-Simulation", "Agent-based models (Simio, CAST). High spatial fidelity, but severe 45m compute latency."),
        ("2015+", "Supervised Machine Learning", "Tree ensembles (GBRT, Random Forest). High routine accuracy; fragile during severe IROPS."),
        ("Today", "Two-Stage Dynamic Hybrids", "Couples recurring flight schedules with live floor error feedback (e_t-1).")
    ]
    add_process_steps(s8, Inches(1.85), lit_steps, Inches(11.733), Inches(1.3))

    # Bottom 2 Comparative Cards: Strengths vs. Operational Shortcomings
    c_str = add_card(s8, Inches(0.8), Inches(3.45), Inches(5.7), Inches(3.4), WHITE, LINE_BORDER)
    tf = c_str.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_right = Inches(0.25)
    tf.margin_top = Inches(0.2)
    p = tf.paragraphs[0]
    p.text = "THEORETICAL ADVANCEMENTS (STRENGTHS)"
    p.font.bold = True
    p.font.size = Pt(11)
    p.font.color.rgb = GREEN

    pts = [
        "Deterministic Physics: Captures flight bank periodicity and aircraft seat gauge without requiring historical training data.",
        "Micro-Simulation: Accurately maps physical walking corridors, PreCheck lane splits, and baggage screening bottlenecks.",
        "Supervised ML: Efficiently processes complex non-linear interactions across 24 BTS OTP delay metrics and taxi times."
    ]
    for pt in pts:
        p = tf.add_paragraph()
        p.text = f"•  {pt}"
        p.font.size = Pt(10.5)
        p.font.color.rgb = DARK_TEXT
        p.space_before = Pt(6)

    c_lim = add_card(s8, Inches(6.8), Inches(3.45), Inches(5.733), Inches(3.4), WHITE, LINE_BORDER)
    tf = c_lim.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_right = Inches(0.25)
    tf.margin_top = Inches(0.2)
    p = tf.paragraphs[0]
    p.text = "OPERATIONAL SHORTCOMINGS (THE GAPS)"
    p.font.bold = True
    p.font.size = Pt(11)
    p.font.color.rgb = AMBER

    pts_lim = [
        "The Static Volume Fallacy: Prior literature targets raw hourly headcounts, completely ignoring arrival burstiness (Kingman's Ca²).",
        "The Dispatch Latency Barrier: 45-minute simulation runs cannot support real-time tactical lane opening during flight ground stops.",
        "The Empty Checkpoint Fallacy: ML algorithms predict zero passengers when flights cancel, leaving airports blind to stranded crowds."
    ]
    for pt in pts_lim:
        p = tf.add_paragraph()
        p.text = f"•  {pt}"
        p.font.size = Pt(10.5)
        p.font.color.rgb = DARK_TEXT
        p.space_before = Pt(6)

    # ==========================================================================
    # SLIDE 9: LITERATURE GAP: VOLATILITY VS. VOLUME
    # ==========================================================================
    s9 = prs.slides.add_slide(blank_layout)
    add_header(s9, "Literature Gap", "The Static Fallacy in Terminal Modeling", "Why Static Passenger Volumes Fail to Explain Checkpoint Delays")

    # Left: CV_TSA Definition Card
    add_centered_equation(
        s9, Inches(0.8), Inches(1.85), Inches(5.7), Inches(5.0),
        title="Scale-Free Relative Volatility Metric",
        formula="CV_TSA  =  σ_TSA  /  μ_TSA",
        subtext_lines=[
            "σ_TSA : Standard deviation of passenger screening arrivals across the day",
            "μ_TSA : Mean hourly screening volume across active operating hours",
            "",
            "Why Volatility Governs Heavy-Traffic Queuing:",
            "• Dimensionless metric normalizing burstiness across small vs. mega hubs",
            "• Kingman's formula proves waiting time is proportional to Ca²",
            "• Volume headcounts hide intra-hour peaking that overwhelms lanes."
        ]
    )

    # Right: Empirical Decoupling Contrast Card
    c_emp = add_card(s9, Inches(6.8), Inches(1.85), Inches(5.733), Inches(5.0), WHITE, LINE_BORDER)
    tf = c_emp.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_right = Inches(0.3)
    tf.margin_top = Inches(0.3)

    p = tf.paragraphs[0]
    p.text = "THE VALUES VERSUS VOLATILITY DISCOVERY"
    p.font.bold = True
    p.font.size = Pt(11)
    p.font.color.rgb = NAVY

    p = tf.add_paragraph()
    p.text = "Empirical Correlation Analysis Across 9-Airport Cohort"
    p.font.bold = True
    p.font.size = Pt(13)
    p.font.color.rgb = BLUE_ACCENT
    p.space_before = Pt(4)

    p = tf.add_paragraph()
    p.text = "1. Static Passenger Volume (y_t) vs. Flight Delays:"
    p.font.bold = True
    p.font.size = Pt(11)
    p.font.color.rgb = AMBER
    p.space_before = Pt(12)

    p = tf.add_paragraph()
    p.text = "r = -0.062,  p = 0.77  ⟹  R² = 2.5%  (Complete Failure!)"
    p.font.name = "Georgia"
    p.font.bold = True
    p.font.size = Pt(12)
    p.font.color.rgb = DARK_TEXT
    p.space_before = Pt(2)

    p = tf.add_paragraph()
    p.text = "Raw volume displays zero statistically significant relationship with airline departure delays. Staffing for volume leaves checkpoints blind."
    p.font.size = Pt(10)
    p.font.color.rgb = SLATE
    p.space_before = Pt(2)

    p = tf.add_paragraph()
    p.text = "2. Throughput Volatility (CV_TSA) vs. Delay Volatility (CV_delay):"
    p.font.bold = True
    p.font.size = Pt(11)
    p.font.color.rgb = GREEN
    p.space_before = Pt(14)

    p = tf.add_paragraph()
    p.text = "r = +0.4373,  p < 0.05  ⟹  R² = 19.1%  (Strong Coupling!)"
    p.font.name = "Georgia"
    p.font.bold = True
    p.font.size = Pt(12)
    p.font.color.rgb = DARK_TEXT
    p.space_before = Pt(2)

    p = tf.add_paragraph()
    p.text = "Checkpoint arrival volatility is directly coupled with flight departure delay dispersion, confirming that volatility modeling is the correct target."
    p.font.size = Pt(10)
    p.font.color.rgb = SLATE
    p.space_before = Pt(2)

    # ==========================================================================
    # SLIDE 10: DETERMINISTIC FLIGHT SCHEDULES (MODEL 1)
    # ==========================================================================
    s10 = prs.slides.add_slide(blank_layout)
    add_header(s10, "Literature Breakdown", "Deterministic Flight Schedules & Classical Queueing", "Model 1: Convolving Scheduled Airline Banks Across Empirical Show-Up Curves")

    add_centered_equation(
        s10, Inches(0.8), Inches(1.85), Inches(5.7), Inches(5.0),
        title="Passenger Show-Up Curve Convolution",
        formula="Ŷ_t  =  ∑ [ Seats_i · (1 - S_connect) · P(t - DEP_i) ]",
        subtext_lines=[
            "Seats_i : Total available seats on scheduled departing flight i",
            "S_connect : Connecting passenger share (deflated via BTS DB1B)",
            "P(τ) : Empirical lognormal show-up probability density (ACRP Report 40)",
            "DEP_i : Scheduled flight departure timestamp",
            "",
            "Operational Philosophy:",
            "Transparent, physics-based baseline. Zero historical training",
            "required; captures macro scheduled bank rhythms directly."
        ]
    )

    c_right = add_card(s10, Inches(6.8), Inches(1.85), Inches(5.733), Inches(5.0), WHITE, LINE_BORDER)
    tf = c_right.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_right = Inches(0.3)
    tf.margin_top = Inches(0.3)

    p = tf.paragraphs[0]
    p.text = "OPERATIONAL APPRAISAL: MODEL 1"
    p.font.bold = True
    p.font.size = Pt(11)
    p.font.color.rgb = BLUE_ACCENT

    p = tf.add_paragraph()
    p.text = "Strengths & Structural Vulnerabilities"
    p.font.bold = True
    p.font.size = Pt(14)
    p.font.color.rgb = NAVY
    p.space_before = Pt(4)

    items = [
        ("Zero-Shot Spatial Invariance (Major Strength)",
         "Because passenger arrival psychology is governed by human show-up behavior rather than local concourse geometry, Model 1 transfers seamlessly to new airports without calibration."),
        ("Complete Transparency",
         "100% interpretable. Airport operators and airlines can trace every passenger forecast back to explicit flight numbers and aircraft seat configurations."),
        ("Blindness to Delays (Fatal Flaw)",
         "Fails to incorporate real-time airside telemetry. When afternoon storms cause 2-hour departure delays, Model 1 predicts passenger arrivals that have already cleared screening hours earlier.")
    ]
    for title, desc in items:
        p = tf.add_paragraph()
        p.text = f"•  {title}"
        p.font.bold = True
        p.font.size = Pt(11)
        p.font.color.rgb = DARK_TEXT
        p.space_before = Pt(10)

        p = tf.add_paragraph()
        p.text = desc
        p.font.size = Pt(10)
        p.font.color.rgb = SLATE
        p.space_before = Pt(2)

    # ==========================================================================
    # SLIDE 11: SHIFT TO MICRO-SIMULATION MODELING
    # ==========================================================================
    s11 = prs.slides.add_slide(blank_layout)
    add_header(s11, "Literature Breakdown", "The Shift to Micro-Simulation Modeling", "High Spatial Resolution vs. Severe Real-Time Operational Latency")

    c_sim_pro = add_card(s11, Inches(0.8), Inches(1.85), Inches(5.7), Inches(5.0), WHITE, LINE_BORDER)
    tf = c_sim_pro.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_right = Inches(0.3)
    tf.margin_top = Inches(0.3)

    p = tf.paragraphs[0]
    p.text = "HIGH SPATIAL FIDELITY (ADVANTAGES)"
    p.font.bold = True
    p.font.size = Pt(11)
    p.font.color.rgb = GREEN

    p = tf.add_paragraph()
    p.text = "Discrete-Event Agent-Based Micro-Simulation"
    p.font.bold = True
    p.font.size = Pt(14)
    p.font.color.rgb = NAVY
    p.space_before = Pt(4)

    sim_pts = [
        "Resolves individual passenger walking corridors, PreCheck vs. standard lane splits, and carry-on divestment times.",
        "Captures physical layout constraints: stanchion queuing serpentine geometry and lane merging bottlenecks.",
        "Gold standard for capital infrastructure planning: sizing future terminal concourses and evaluating multi-million dollar checkpoint expansions.",
        "Platforms: Simio, CAST, ArcSTAR, and Arena airport simulation suites."
    ]
    for pt in sim_pts:
        p = tf.add_paragraph()
        p.text = f"•  {pt}"
        p.font.size = Pt(10.5)
        p.font.color.rgb = DARK_TEXT
        p.space_before = Pt(10)

    c_sim_con = add_card(s11, Inches(6.8), Inches(1.85), Inches(5.733), Inches(5.0), WHITE, LINE_BORDER)
    tf = c_sim_con.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_right = Inches(0.3)
    tf.margin_top = Inches(0.3)

    p = tf.paragraphs[0]
    p.text = "THE DISPATCH LATENCY BARRIER (DISADVANTAGES)"
    p.font.bold = True
    p.font.size = Pt(11)
    p.font.color.rgb = AMBER

    p = tf.add_paragraph()
    p.text = "Why Micro-Simulation Fails in Real-Time Operations"
    p.font.bold = True
    p.font.size = Pt(14)
    p.font.color.rgb = NAVY
    p.space_before = Pt(4)

    sim_cons = [
        "20–45 Minute Computation Time: A 24-hour terminal simulation requires up to 45 minutes to execute—far too slow for tactical within-hour lane adjustments.",
        "High Calibration Overhead: Requires hundreds of micro-parameters (walking speeds, divest rates, escorts) that become obsolete during weather shocks.",
        "Inflexible to Shock Cascades: When a ground stop hits, stochastic simulation cannot dynamically ingest live sensor telemetry to rebalance queues.",
        "Operational Verdict: Excellent for multi-year capital planning, but unsuitable for automated intraday lane dispatch."
    ]
    for pt in sim_cons:
        p = tf.add_paragraph()
        p.text = f"•  {pt}"
        p.font.size = Pt(10.5)
        p.font.color.rgb = DARK_TEXT
        p.space_before = Pt(10)

    # ==========================================================================
    # SLIDE 12: SUPERVISED MACHINE LEARNING (MODEL 2)
    # ==========================================================================
    s12 = prs.slides.add_slide(blank_layout)
    add_header(s12, "Literature Breakdown", "Supervised Machine Learning (Model 2)", "High Routine Accuracy Coupled with Fragility Under Severe Shock")

    # Left: Big KPI Stat Box
    add_kpi_card(
        s12, Inches(0.8), Inches(1.85), Inches(3.6), Inches(5.0),
        stat_value="24",
        stat_label="Operational Features",
        subtext="BTS OTP Delay Attributes,\nFlight Bank Dispersion,\nTaxi-out Queues & Weather"
    )

    # Right: Dual Operational Regime Breakdown
    c_ml = add_card(s12, Inches(4.7), Inches(1.85), Inches(7.833), Inches(5.0), WHITE, LINE_BORDER)
    tf = c_ml.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_right = Inches(0.35)
    tf.margin_top = Inches(0.3)

    p = tf.paragraphs[0]
    p.text = "OPERATIONAL REGIME SPLIT: SUPERVISED ML"
    p.font.bold = True
    p.font.size = Pt(11)
    p.font.color.rgb = BLUE_ACCENT

    p = tf.add_paragraph()
    p.text = "Routine Efficiency vs. The Empty Checkpoint Fallacy"
    p.font.bold = True
    p.font.size = Pt(14)
    p.font.color.rgb = NAVY
    p.space_before = Pt(4)

    p = tf.add_paragraph()
    p.text = "1. Routine Daily Operations (Pareto Frontier Winner):"
    p.font.bold = True
    p.font.size = Pt(11.5)
    p.font.color.rgb = GREEN
    p.space_before = Pt(12)

    p = tf.add_paragraph()
    p.text = "• Delivers outstanding routine accuracy (MASE = 0.680–0.700) under calm conditions.\n• Zero feedback latency: generates multi-hour forecasts instantly without requiring live sensor streams.\n• Captures complex non-linear delay interactions across airline carriers."
    p.font.size = Pt(10.5)
    p.font.color.rgb = DARK_TEXT
    p.space_before = Pt(3)

    p = tf.add_paragraph()
    p.text = "2. Convective Storm Shocks (The Empty Checkpoint Fallacy):"
    p.font.bold = True
    p.font.size = Pt(11.5)
    p.font.color.rgb = AMBER
    p.space_before = Pt(14)

    p = tf.add_paragraph()
    p.text = "• When convective weather grounds departures, flights are cancelled from airline feeds.\n• The decision tree sees cancelled flights and predicts near-zero passenger throughput.\n• In reality, thousands of stranded passengers flood terminal lobbies seeking rebooking.\n• Result: Pure ML suffers catastrophic collapse during IROPS (Recovery Multiplier R = 2.14)."
    p.font.size = Pt(10.5)
    p.font.color.rgb = DARK_TEXT
    p.space_before = Pt(3)

    # ==========================================================================
    # SLIDE 13: SEQUENTIAL TWO-STAGE HYBRIDS (MODEL 3)
    # ==========================================================================
    s13 = prs.slides.add_slide(blank_layout)
    add_header(s13, "Literature Breakdown", "Sequential Two-Stage Hybrid Architectures (Model 3)", "Coupling Macro Flight Schedule Cycles with Real-Time Floor Innovation Feedback")

    # Top: Centered Formula
    add_centered_equation(
        s13, Inches(0.8), Inches(1.85), Inches(11.733), Inches(1.7),
        title="Two-Stage Hybrid Formulation",
        formula="Ŷ_t  =  M_base(Schedule_t, X_t)  +  α · ( Y_{t-1} - Ŷ_{t-1} )",
        subtext_lines=["where α is the empirical feedback gain calibrating live prior-hour floor residual innovation."]
    )

    # Bottom: 2 Architectural Blocks
    c_stg1 = add_card(s13, Inches(0.8), Inches(3.75), Inches(5.7), Inches(3.1), WHITE, LINE_BORDER)
    tf = c_stg1.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_right = Inches(0.25)
    tf.margin_top = Inches(0.2)
    p = tf.paragraphs[0]
    p.text = "STAGE 1: OPERATIONAL SCHEDULE BASELINE"
    p.font.bold = True
    p.font.size = Pt(11)
    p.font.color.rgb = BLUE_ACCENT
    p = tf.add_paragraph()
    p.text = "Captures the deterministic diurnal heartbeat of the airport: published flight banks, aircraft gauge, day-of-week demand patterns, and connecting deflators. Establishes the macro capacity anchor."
    p.font.size = Pt(10.5)
    p.font.color.rgb = DARK_TEXT
    p.space_before = Pt(8)

    c_stg2 = add_card(s13, Inches(6.8), Inches(3.75), Inches(5.733), Inches(3.1), WHITE, LINE_BORDER)
    tf = c_stg2.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_right = Inches(0.25)
    tf.margin_top = Inches(0.2)
    p = tf.paragraphs[0]
    p.text = "STAGE 2: REAL-TIME FLOOR INNOVATION FEEDBACK"
    p.font.bold = True
    p.font.size = Pt(11)
    p.font.color.rgb = GREEN
    p = tf.add_paragraph()
    p.text = "Injects the prior-hour screening floor innovation: e_{t-1} = Y_{t-1} - Ŷ_{t-1}. When storm ground stops leave passengers stranded in concourses, live checkpoint counts immediately pull forecasts back to reality, preventing the Empty Checkpoint Fallacy."
    p.font.size = Pt(10.5)
    p.font.color.rgb = DARK_TEXT
    p.space_before = Pt(8)

    # ==========================================================================
    # SLIDE 14: COVID-19 DEMARCATION & SAMPLE STABILITY
    # ==========================================================================
    s14 = prs.slides.add_slide(blank_layout)
    add_header(s14, "Empirical Demarcation", "The Structural Impact of COVID-19 Demarcation", "Purging Pandemic Distortions to Establish Time-Series Stability")

    # 3 Stat KPI Blocks
    kpis = [
        ("May 1, 2022", "Demarcation Cutoff", "Federal mask mandate dissolved; commercial traffic patterns normalized."),
        ("F = 1.42", "Chow Break Test", "p = 0.18. Fails to reject null; confirms structural stability across 44 months."),
        ("84.7%", "Load Factor Recovery", "Systemwide load factors fully recovered to historical baseline.")
    ]
    for i, (val, lbl, sub) in enumerate(kpis):
        x = Inches(0.8) + i * Inches(3.99)
        add_kpi_card(s14, x, Inches(1.85), Inches(3.75), Inches(2.2), val, lbl, sub)

    # Bottom Summary Card
    c_bot = add_card(s14, Inches(0.8), Inches(4.3), Inches(11.733), Inches(2.55), WHITE, LINE_BORDER)
    tf = c_bot.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_right = Inches(0.3)
    tf.margin_top = Inches(0.2)

    p = tf.paragraphs[0]
    p.text = "ECONOMETRIC JUSTIFICATION FOR DATA PURGING (2020–2021)"
    p.font.bold = True
    p.font.size = Pt(11)
    p.font.color.rgb = NAVY

    just_pts = [
        "Recursive CUSUM Residual Analysis: Structural instability persists through early 2022. Training models on 2020–2021 induces severe non-stationary bias.",
        "Zero Operational Value: Pandemic air travel reflected government travel restrictions and quarantine orders rather than stochastic passenger arrival psychology.",
        "44-Month Post-Pandemic Evaluation Window: Provides 42.1 million conformed records across 2022–2025, ensuring overwhelming statistical power without pandemic distortion."
    ]
    for pt in just_pts:
        p = tf.add_paragraph()
        p.text = f"•  {pt}"
        p.font.size = Pt(10.5)
        p.font.color.rgb = DARK_TEXT
        p.space_before = Pt(6)

    # ==========================================================================
    # SLIDE 15: WHY AVIATION DEMANDS DYNAMIC PERFORMANCE MEASURES
    # ==========================================================================
    s15 = prs.slides.add_slide(blank_layout)
    add_header(s15, "Evaluative Synthesis", "Why Aviation Demands Dynamic Performance Measures", "The Danger of Relying on Global Annual Error Metrics")

    # 3 Horizontal Dimension Cards
    dim_cards = [
        ("DIMENSION 1: NOMINAL ON-TIME FLOW (ROBUSTNESS)",
         "FAA A14 Reference Case (Delays < 15m, 0 Cancels)",
         "In routine operations, airport security checkpoints experience predictable morning and evening flight banks. Small residual errors are easily absorbed by standard lane buffers. The operational goal is low computational latency, zero feedback overhead, and reliable baseline staffing."),
        ("DIMENSION 2: CONVECTIVE STORM SHOCKS (RESILIENCE)",
         "Irregular Operations / IROPS (Delays ≥ 45m, Cancels ≥ 5)",
         "Terminal crises occur during severe weather ground stops. Airport directors face massive queue surges as flight schedules desynchronize. A model with excellent annual RMSE that fails during storms is operationally hazardous. The goal is shock recovery and rapid time-to-recovery (TTR < 4h)."),
        ("DIMENSION 3: CONCOURSE SPATIAL PORTABILITY (GENERALIZABILITY)",
         "Zero-Shot Concourse Transfer (EWR → LGA Without Retraining)",
         "Airport authorities regularly open new terminal concourses or reassign airline carriers. Training complex machine learning models requires 12 months of local checkpoint history. The operational goal is zero-shot transferability across unfamiliar physical checkpoint layouts.")
    ]

    for i, (title, sub, text) in enumerate(dim_cards):
        y = Inches(1.85) + i * Inches(1.72)
        card = add_card(s15, Inches(0.8), y, Inches(11.733), Inches(1.55), WHITE, LINE_BORDER)
        tf = card.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_right = Inches(0.3)
        tf.margin_top = Inches(0.15)

        p = tf.paragraphs[0]
        p.text = title
        p.font.bold = True
        p.font.size = Pt(11)
        p.font.color.rgb = NAVY

        p = tf.add_paragraph()
        p.text = sub
        p.font.bold = True
        p.font.size = Pt(9.5)
        p.font.color.rgb = BLUE_ACCENT
        p.space_before = Pt(2)

        p = tf.add_paragraph()
        p.text = text
        p.font.size = Pt(9.5)
        p.font.color.rgb = DARK_TEXT
        p.space_before = Pt(3)

    # ==========================================================================
    # SLIDE 16: RESEARCH METHODOLOGY OVERVIEW
    # ==========================================================================
    s16 = prs.slides.add_slide(blank_layout)
    add_header(s16, "Methodological Architecture", "Research Methodology Overview", "Five-Stage Scientific Architecture Grounded in Federal Aviation Assets")

    method_steps = [
        ("3.1", "Research Approach", "Comparative out-of-time evaluation across 3 operational pillars."),
        ("3.2", "Cohort Sampling", "4-tier filtering isolating 9 airports & 12 carrier-exclusive complexes."),
        ("3.3", "Data Assets & ETL", "67.2M raw federal records conformed to 42.1M Star Schema rows."),
        ("3.4", "Validity Safeguards", "DB1B connecting deflator, carrier isolation & 168-h purge buffer."),
        ("3.5", "Treatment & Testing", "2025 out-of-time holdout & Diebold-Mariano statistical tests.")
    ]
    add_process_steps(s16, Inches(1.85), method_steps, Inches(11.733), Inches(1.3))

    # Bottom Card with Detailed Flowchart Details
    c_m_bot = add_card(s16, Inches(0.8), Inches(3.45), Inches(11.733), Inches(3.4), WHITE, LINE_BORDER)
    tf = c_m_bot.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_right = Inches(0.3)
    tf.margin_top = Inches(0.2)

    p = tf.paragraphs[0]
    p.text = "RIGOROUS METHODOLOGICAL EXECUTION"
    p.font.bold = True
    p.font.size = Pt(11)
    p.font.color.rgb = NAVY

    m_pts = [
        "Econometric Rigor: Standardized multi-source data merging across TSA FOIA throughput, BTS On-Time Performance (OTP), BTS T-100 Segment data, and BTS DB1B Ticket Surveys.",
        "Zero-Data Contamination: Strict information availability boundaries ensure models only ingest telemetry realized prior to the prediction hour (t-1).",
        "Out-of-Time Verification: Evaluated on an untouched 2025 holdout dataset (January 1 – December 31, 2025), preventing synthetic random split leakage.",
        "Formal Statistical Testing: Model differences validated using Diebold-Mariano tests and paired t-tests across operational regimes."
    ]
    for pt in m_pts:
        p = tf.add_paragraph()
        p.text = f"•  {pt}"
        p.font.size = Pt(10.5)
        p.font.color.rgb = DARK_TEXT
        p.space_before = Pt(8)

    # ==========================================================================
    # SLIDE 17: FORECASTING MODEL FAMILIES & BASELINE CONTROL
    # ==========================================================================
    s17 = prs.slides.add_slide(blank_layout)
    add_header(s17, "Methodology Approach", "Forecasting Model Families & Baseline Control", "Four Candidate Paradigms Representing Distinct Operational Philosophies")

    models = [
        ("CONTROL", "BASELINE CONTROL", "Diurnal Persistence Benchmark",
         "Ŷ_t = Y_{t-24}\n\n• Non-parametric persistence\n• Benchmark MASE ≡ 1.000\n• Assumes yesterday's pattern repeats exactly today\n• Captures basic diurnal cycle"),
        ("MODEL 1", "DETERMINISTIC SCHEDULE", "Airline Flight Bank Convolution",
         "ACRP Report 40 curves\n\n• Convolves seats over lognormal passenger show-up curves\n• 100% interpretable\n• Zero historical training needed\n• Highly portable across concourses"),
        ("MODEL 2", "SUPERVISED ML", "Gradient-Boosted Decision Trees",
         "LightGBM + 24 Features\n\n• Tweedie deviance objective\n• Ingests 24 BTS OTP attributes\n• Captures non-linear delay interactions\n• Highly accurate in routine flow"),
        ("MODEL 3", "DYNAMIC HYBRID", "Two-Stage Error Innovation",
         "Schedule Base + Floor Feedback\n\n• Stage 1: Flight schedule base\n• Stage 2: e_{t-1} floor innovation\n• Rebalances dynamically during storms\n• Decisive holdout winner")
    ]

    card_w = Inches(2.78)
    for i, (tag, name, sub, desc) in enumerate(models):
        x = Inches(0.8) + i * Inches(2.98)
        card = add_card(s17, x, Inches(1.85), card_w, Inches(5.0), WHITE, LINE_BORDER)
        tf = card.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_right = Inches(0.2)
        tf.margin_top = Inches(0.25)

        p = tf.paragraphs[0]
        p.text = tag
        p.font.bold = True
        p.font.size = Pt(9.5)
        p.font.color.rgb = BLUE_ACCENT

        p = tf.add_paragraph()
        p.text = name
        p.font.bold = True
        p.font.size = Pt(12)
        p.font.color.rgb = NAVY
        p.space_before = Pt(2)

        p = tf.add_paragraph()
        p.text = sub
        p.font.bold = True
        p.font.size = Pt(9.5)
        p.font.color.rgb = SLATE
        p.space_before = Pt(2)

        p = tf.add_paragraph()
        p.text = desc
        p.font.size = Pt(10)
        p.font.color.rgb = DARK_TEXT
        p.space_before = Pt(10)

    # ==========================================================================
    # SLIDE 18: FOUR-PHASE RESEARCH LIFECYCLE
    # ==========================================================================
    s18 = prs.slides.add_slide(blank_layout)
    add_header(s18, "Design & Procedure", "Four-Phase Research Execution Lifecycle", "From Raw Federal Asset Ingestion to Out-of-Time Holdout Verification")

    phases = [
        ("PHASE 1", "DATA FOUNDATION & ETL",
         "Conformed 67.2M raw records from TSA FOIA, BTS OTP, T-100, and DB1B into an optimized Star Schema database, harmonizing carrier codes and airport IATA identifiers across 44 months."),
        ("PHASE 2", "ECONOMETRIC FILTERING",
         "Executed the 4-tier filtering pipeline, screening 450+ airports to isolate the 9-airport experimental cohort across 12 carrier-exclusive screening complexes."),
        ("PHASE 3", "CALIBRATION & ENGINEERING",
         "Engineered 24 operational features, constructed an 84-cell interaction grid, and calibrated hyperparameter bounds (N_train ≥ 50 in 98.8% of feature cells)."),
        ("PHASE 4", "MULTI-PILLAR TESTING",
         "Executed out-of-time evaluation across the full 2025 holdout period, testing hypotheses H1a (Robustness), H1b (Resilience), and H1c (Generalizability).")
    ]

    card_w = Inches(2.78)
    for i, (tag, name, body) in enumerate(phases):
        x = Inches(0.8) + i * Inches(2.98)
        card = add_card(s18, x, Inches(1.85), card_w, Inches(5.0), WHITE, LINE_BORDER)
        tf = card.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_right = Inches(0.2)
        tf.margin_top = Inches(0.3)

        p = tf.paragraphs[0]
        p.text = tag
        p.font.bold = True
        p.font.size = Pt(10)
        p.font.color.rgb = BLUE_ACCENT

        p = tf.add_paragraph()
        p.text = name
        p.font.bold = True
        p.font.size = Pt(12)
        p.font.color.rgb = NAVY
        p.space_before = Pt(3)

        p = tf.add_paragraph()
        p.text = body
        p.font.size = Pt(10.5)
        p.font.color.rgb = DARK_TEXT
        p.space_before = Pt(10)

    # ==========================================================================
    # SLIDE 19: METHODOLOGICAL SAFEGUARDS & DATA INTEGRITY
    # ==========================================================================
    s19 = prs.slides.add_slide(blank_layout)
    add_header(s19, "Validity Safeguards", "Methodological Safeguards & Data Integrity", "Eliminating Leakage, Spatial Contamination, and Information Lookahead")

    safeguards = [
        ("168-HOUR PURGE BUFFER",
         "Strict 7-day temporal gap between training and test holdout. Eliminates autoregressive memory leakage that artificially inflates machine learning performance in time-series evaluation."),
        ("CONNECTING PASSENGER DEFLATOR",
         "Applies BTS DB1B originating passenger ratios to scheduled seats. Resolves 'The Hub Disconnect' by stripping out connecting passengers who never cross the TSA checkpoint floor."),
        ("CARRIER SCREENING ISOLATION",
         "Restricts cohort to single-carrier terminals (e.g., EWR Terminal C, ATL South). Eliminates multi-carrier passenger mixing, establishing clean econometric identification."),
        ("STRICT INFORMATION AVAILABILITY (t-1)",
         "Eliminates lookahead bias. Models ingest only operational data realized prior to the prediction hour. No future departure delays or cancelled flights are used at prediction time.")
    ]

    col_w = Inches(5.7)
    row_h = Inches(2.35)
    for idx, (title, desc) in enumerate(safeguards):
        r = idx // 2
        c = idx % 2
        x = Inches(0.8) + c * Inches(6.0)
        y = Inches(1.85) + r * Inches(2.65)

        card = add_card(s19, x, y, col_w, row_h, WHITE, LINE_BORDER)
        tf = card.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_right = Inches(0.25)
        tf.margin_top = Inches(0.2)

        p = tf.paragraphs[0]
        p.text = title
        p.font.bold = True
        p.font.size = Pt(11)
        p.font.color.rgb = BLUE_ACCENT

        p = tf.add_paragraph()
        p.text = desc
        p.font.size = Pt(10.5)
        p.font.color.rgb = DARK_TEXT
        p.space_before = Pt(6)

    # ==========================================================================
    # SLIDE 20: CHAPTER IV EMPIRICAL RESULTS ARCHITECTURE
    # ==========================================================================
    s20 = prs.slides.add_slide(blank_layout)
    add_header(s20, "Results Roadmap", "Chapter IV Empirical Results Architecture", "Structured Progression from Exploratory Volatility to Certified Holdout Tests")

    results_flow = [
        ("SECTION 4.1", "EXPLORATORY DATA ANALYSIS",
         "Discovery of the Values vs. Volatility decoupling (r = +0.4373 vs. r = -0.062). Establishes arrival burstiness as the primary modeling target."),
        ("SECTION 4.2", "FOUR-TIER FILTERING COHORT",
         "Execution of the 4-tier filtering pipeline. Isolates the 9-airport experimental cohort across 12 carrier-exclusive complexes with balanced representation."),
        ("SECTION 4.3", "MODEL DEVELOPMENT & 2025 HOLDOUT",
         "Feature engineering across 24 attributes and execution of the out-of-time 2025 holdout benchmark suite (Table 4.10)."),
        ("SECTION 4.4", "MULTI-PILLAR HYPOTHESIS TESTING",
         "Formal testing of H1a (Robustness), H1b (Resilience), and H1c (Generalizability) proving the Master Asymmetric Trade-Off (Table 4.11).")
    ]

    card_w = Inches(2.78)
    for i, (tag, name, body) in enumerate(results_flow):
        x = Inches(0.8) + i * Inches(2.98)
        card = add_card(s20, x, Inches(1.85), card_w, Inches(5.0), WHITE, LINE_BORDER)
        tf = card.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_right = Inches(0.2)
        tf.margin_top = Inches(0.3)

        p = tf.paragraphs[0]
        p.text = tag
        p.font.bold = True
        p.font.size = Pt(10)
        p.font.color.rgb = BLUE_ACCENT

        p = tf.add_paragraph()
        p.text = name
        p.font.bold = True
        p.font.size = Pt(12)
        p.font.color.rgb = NAVY
        p.space_before = Pt(3)

        p = tf.add_paragraph()
        p.text = body
        p.font.size = Pt(10.5)
        p.font.color.rgb = DARK_TEXT
        p.space_before = Pt(10)

    # ==========================================================================
    # SLIDE 21: DESCRIPTIVE STATISTICS: 9-AIRPORT COHORT VS. TOP 25
    # ==========================================================================
    s21 = prs.slides.add_slide(blank_layout)
    add_header(s21, "Descriptive Statistics", "Empirical Baseline: 9-Airport Cohort vs. Top 25", "Isolating High-Stress Operational Hubs Across U.S. Commercial Aviation")

    # 4 Big-Number KPI Stat Blocks
    cohort_stats = [
        ("+16.9%", "Flight Density", "224,576 annual flights vs. 192,160 top-25 mean"),
        ("+14.1%", "Cancellation Churn", "1.63% annual cancel rate vs. 1.43% top-25 mean"),
        ("+25.0%", "Originating Demand", "16.4M originating pax vs. 13.1M top-25 mean"),
        ("+5.8%", "Arrival Volatility", "CV_TSA = 0.8728 vs. 0.8250 top-25 mean")
    ]
    for i, (val, lbl, sub) in enumerate(cohort_stats):
        x = Inches(0.8) + i * Inches(2.98)
        add_kpi_card(s21, x, Inches(1.85), Inches(2.78), Inches(2.2), val, lbl, sub)

    # Bottom Explanatory Card
    c_desc_bot = add_card(s21, Inches(0.8), Inches(4.3), Inches(11.733), Inches(2.55), WHITE, LINE_BORDER)
    tf = c_desc_bot.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_right = Inches(0.3)
    tf.margin_top = Inches(0.2)

    p = tf.paragraphs[0]
    p.text = "OPERATIONAL SIGNIFICANCE OF THE 9-AIRPORT COHORT"
    p.font.bold = True
    p.font.size = Pt(11)
    p.font.color.rgb = NAVY

    c_pts = [
        "Deliberate High-Congestion Fronts: The 9 selected airports represent genuine operational pressure points in the National Airspace System, rather than tranquil regional stations.",
        "Statistical Stress Testing: High flight density and elevated cancellation rates ensure sufficient sample sizes of convective IROPS shocks for robust resilience testing.",
        "Originating Passenger Dominance: Higher originating passenger headcounts mean that checkpoint queuing dynamics directly drive terminal crowding.",
        "Factorial Carrier Balance: Equal representation across American (5), Delta (5), and United (4) complexes prevents airline-specific procedural bias."
    ]
    for pt in c_pts:
        p = tf.add_paragraph()
        p.text = f"•  {pt}"
        p.font.size = Pt(10.5)
        p.font.color.rgb = DARK_TEXT
        p.space_before = Pt(6)

    # ==========================================================================
    # SLIDE 22: THE FOUR-TIER PURPOSIVE FILTERING FUNNEL
    # ==========================================================================
    s22 = prs.slides.add_slide(blank_layout)
    add_header(s22, "Cohort Selection", "The Four-Tier Purposive Filtering Pipeline", "Methodological Funnel from 450+ Commercial Airports to 12 Carrier Complexes")

    tiers = [
        ("TIER 1", "MACRO SCALE", "Commercial Hub Volume",
         "Filtered 450+ commercial airports to the Top 25 large hubs. Captures 68% of total U.S. commercial passenger traffic."),
        ("TIER 2", "MESO CARRIER", "Legacy Carrier Presence",
         "Screened for continuous, dominant mainline presence of American, Delta, or United. Eliminated JFK due to terminal fragmentation."),
        ("TIER 3", "MICRO GEOMETRY", "Physical Carrier Isolation",
         "Filtered out consolidated, multi-carrier checkpoints. Eliminated SLC due to unified common-use checkpoint floor."),
        ("TIER 4", "COHORT BALANCE", "Factorial Representation",
         "Finalized 9 airports across 12 carrier-exclusive complexes, balancing 4 operational clusters across the major airline alliances.")
    ]

    card_w = Inches(2.78)
    for i, (tag, name, sub, body) in enumerate(tiers):
        x = Inches(0.8) + i * Inches(2.98)
        card = add_card(s22, x, Inches(1.85), card_w, Inches(5.0), WHITE, LINE_BORDER)
        tf = card.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_right = Inches(0.2)
        tf.margin_top = Inches(0.3)

        p = tf.paragraphs[0]
        p.text = tag
        p.font.bold = True
        p.font.size = Pt(10)
        p.font.color.rgb = BLUE_ACCENT

        p = tf.add_paragraph()
        p.text = name
        p.font.bold = True
        p.font.size = Pt(12)
        p.font.color.rgb = NAVY
        p.space_before = Pt(2)

        p = tf.add_paragraph()
        p.text = sub
        p.font.bold = True
        p.font.size = Pt(9.5)
        p.font.color.rgb = SLATE
        p.space_before = Pt(2)

        p = tf.add_paragraph()
        p.text = body
        p.font.size = Pt(10)
        p.font.color.rgb = DARK_TEXT
        p.space_before = Pt(10)

    # ==========================================================================
    # SLIDE 23: 9-AIRPORT EXPERIMENTAL COHORT SPECIFICATION
    # ==========================================================================
    s23 = prs.slides.add_slide(blank_layout)
    add_header(s23, "Cohort Specification", "The 9-Airport Experimental Cohort Specification", "12 Carrier-Exclusive Terminal Complexes Across Major Commercial Alliances")

    # Clean 3x3 Grid of Airport Badges (Table 4.6)
    airports_grid = [
        ("ATL", "Atlanta Hartsfield-Jackson", "Delta Domestic South", "Mega Connecting Hub"),
        ("BOS", "Boston Logan", "Delta A  ·  American B", "Northeast Business Origin"),
        ("DFW", "Dallas/Fort Worth", "American A, B, C", "Mega Network Fortress"),
        ("DTW", "Detroit Metropolitan", "Delta McNamara Terminal", "Midwest Mega Transfer"),
        ("EWR", "Newark Liberty", "United Terminal C", "Congested Metro Hub"),
        ("LAX", "Los Angeles International", "Delta 3 · AA 4 · United 7", "West Coast Gateway"),
        ("LGA", "New York LaGuardia", "Delta Terminal C", "High-Frequency Business"),
        ("ORD", "Chicago O'Hare", "United T1  ·  American T3", "Dual-Hub Pressure Center"),
        ("PHL", "Philadelphia International", "American Terminals B/C", "Mid-Atlantic Hub")
    ]

    col_w = Inches(3.75)
    row_h = Inches(1.5)
    gap_x = Inches(0.24)
    gap_y = Inches(0.2)

    for idx, (code, name, complex_str, archetype) in enumerate(airports_grid):
        r = idx // 3
        c = idx % 3
        x = Inches(0.8) + c * (col_w + gap_x)
        y = Inches(1.85) + r * (row_h + gap_y)

        card = add_card(s23, x, y, col_w, row_h, WHITE, LINE_BORDER)
        tf = card.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_right = Inches(0.2)
        tf.margin_top = Inches(0.12)

        p = tf.paragraphs[0]
        p.text = f"{code}  ·  {name}"
        p.font.bold = True
        p.font.size = Pt(11)
        p.font.color.rgb = NAVY

        p = tf.add_paragraph()
        p.text = complex_str
        p.font.bold = True
        p.font.size = Pt(10)
        p.font.color.rgb = BLUE_ACCENT
        p.space_before = Pt(2)

        p = tf.add_paragraph()
        p.text = f"Cluster Archetype: {archetype}"
        p.font.size = Pt(9.5)
        p.font.color.rgb = SLATE
        p.space_before = Pt(2)

    # ==========================================================================
    # SLIDE 24: ANNUAL SEASONAL VOLATILITY REGIMES
    # ==========================================================================
    s24 = prs.slides.add_slide(blank_layout)
    add_header(s24, "Macro Regimes", "Annual Seasonal Volatility Regimes", "Macro Travel Fluctuations and Convective Weather Disruptions (Table 4.3b)")

    seasons = [
        ("OFF-PEAK WINTER", "Weeks 1–8, 45–46",
         "Lowest passenger throughput and baseline delay dispersion. High schedule adherence; ideal for baseline model calibration."),
        ("MID-PEAK SPRING", "Weeks 9–21, 36–44",
         "Elevated business travel with tight morning and evening flight banks. Moderate delays; balanced operational tempo."),
        ("SUMMER CONVECTIVE", "Weeks 22–35 (PEAK SHOCK)",
         "Highest delay dispersion (σ_delay = 68.4m) and peak arrival volatility (CV_TSA). Severe thunderstorms induce major ground stops and delay cascades."),
        ("HOLIDAY TRAVEL PEAKS", "Weeks 47–52",
         "Maximum passenger headcounts driven by leisure and family travelers. Heavy luggage divestment and non-consecutive passenger volume surges.")
    ]

    card_w = Inches(2.78)
    for i, (title, weeks, desc) in enumerate(seasons):
        x = Inches(0.8) + i * Inches(2.98)
        card = add_card(s24, x, Inches(1.85), card_w, Inches(5.0), WHITE, LINE_BORDER)
        tf = card.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_right = Inches(0.2)
        tf.margin_top = Inches(0.3)

        p = tf.paragraphs[0]
        p.text = title
        p.font.bold = True
        p.font.size = Pt(11)
        p.font.color.rgb = AMBER if "PEAK SHOCK" in title else NAVY

        p = tf.add_paragraph()
        p.text = weeks
        p.font.bold = True
        p.font.size = Pt(9.5)
        p.font.color.rgb = BLUE_ACCENT
        p.space_before = Pt(2)

        p = tf.add_paragraph()
        p.text = desc
        p.font.size = Pt(10)
        p.font.color.rgb = DARK_TEXT
        p.space_before = Pt(10)

    # ==========================================================================
    # SLIDE 25: DAY-OF-WEEK VOLATILITY & BIMODAL DIURNAL PEAKS
    # ==========================================================================
    s25 = prs.slides.add_slide(blank_layout)
    add_header(s25, "Diurnal & DOW Cycles", "Day-of-Week Volatility & Bimodal Diurnal Peaks", "Temporal Asynchrony Between Passenger Screening and Aircraft Delays")

    c_dow = add_card(s25, Inches(0.8), Inches(1.85), Inches(5.7), Inches(5.0), WHITE, LINE_BORDER)
    tf = c_dow.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_right = Inches(0.3)
    tf.margin_top = Inches(0.3)

    p = tf.paragraphs[0]
    p.text = "DAY-OF-WEEK OPERATIONAL ARCHETYPES"
    p.font.bold = True
    p.font.size = Pt(11)
    p.font.color.rgb = BLUE_ACCENT

    p = tf.add_paragraph()
    p.text = "Contrasting Monday vs. Sunday Rhythms"
    p.font.bold = True
    p.font.size = Pt(14)
    p.font.color.rgb = NAVY
    p.space_before = Pt(4)

    dow_pts = [
        ("Monday Morning (Outbound Business Surge)",
         "Screening checkpoints experience peak weekly throughput between 05:00 and 08:00. High business traveler PreCheck adoption; flight departure delays remain minimal (on-time rate > 88%)."),
        ("Sunday Evening (Inbound Leisure & Turnaround Cascades)",
         "Screening volume peaks between 15:00 and 19:00. Cumulative air traffic delay ripples expand departure delay standard deviation by +35% compared to weekday mornings."),
        ("Mid-Week Equilibrium (Tuesday–Thursday)",
         "Predictable corporate travel rhythm with highly stable diurnal arrival waves; serves as the baseline calibration control.")
    ]
    for title, desc in dow_pts:
        p = tf.add_paragraph()
        p.text = f"•  {title}"
        p.font.bold = True
        p.font.size = Pt(10.5)
        p.font.color.rgb = DARK_TEXT
        p.space_before = Pt(8)

        p = tf.add_paragraph()
        p.text = desc
        p.font.size = Pt(9.5)
        p.font.color.rgb = SLATE
        p.space_before = Pt(2)

    c_diu = add_card(s25, Inches(6.8), Inches(1.85), Inches(5.733), Inches(5.0), WHITE, LINE_BORDER)
    tf = c_diu.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_right = Inches(0.3)
    tf.margin_top = Inches(0.3)

    p = tf.paragraphs[0]
    p.text = "BIMODAL DIURNAL ASYNCHRONY"
    p.font.bold = True
    p.font.size = Pt(11)
    p.font.color.rgb = GREEN

    p = tf.add_paragraph()
    p.text = "The Airside-Landside Operational Disconnect"
    p.font.bold = True
    p.font.size = Pt(14)
    p.font.color.rgb = NAVY
    p.space_before = Pt(4)

    diu_pts = [
        ("Morning Wave (05:00 – 08:00)",
         "Peak screening surge: throughput reaches 11,380 pax/hr across major complexes. Flight departures operate on-time; airport queuing friction is purely driven by passenger arrival burstiness."),
        ("Midday Lull (10:00 – 13:00)",
         "Checkpoint throughput declines by 40–55%. Screening lanes are under-utilized while aircraft turnarounds take place on the airside."),
        ("Afternoon/Evening Wave (14:00 – 22:00)",
         "Secondary passenger screening surge coupled with peak airside flight delays. Convective weather cascades create severe mismatch between scheduled departures and physical checkpoint arrivals.")
    ]
    for title, desc in diu_pts:
        p = tf.add_paragraph()
        p.text = f"•  {title}"
        p.font.bold = True
        p.font.size = Pt(10.5)
        p.font.color.rgb = DARK_TEXT
        p.space_before = Pt(8)

        p = tf.add_paragraph()
        p.text = desc
        p.font.size = Pt(9.5)
        p.font.color.rgb = SLATE
        p.space_before = Pt(2)

    # ==========================================================================
    # SLIDE 26: EMPIRICAL PASSENGER SHOW-UP DYNAMICS (LEAD-LAG)
    # ==========================================================================
    s26 = prs.slides.add_slide(blank_layout)
    add_header(s26, "Lead-Lag Dynamics", "Empirical Passenger Show-Up Curve Convolution", "Resolving the Optimal Lead Time for Checkpoint Arrival Forecasting")

    add_centered_equation(
        s26, Inches(0.8), Inches(1.85), Inches(5.7), Inches(5.0),
        title="Contemporaneous vs. 2-Hour Lead Correlation",
        formula="R²( t+2 ) = 0.5347    vs.    R²( t ) = 0.1982",
        subtext_lines=[
            "Contemporaneous flight schedules (t) fail completely (R² < 20%).",
            "Checkpoint arrivals peak at a 2-hour lead time (t+2),",
            "explaining 53.5% of variance (F = 142.80, p < 0.001).",
            "",
            "Validates ACRP Report 40 lognormal show-up curves:",
            "Passengers arrive at security 1.5 to 2.5 hours prior to gate pushback.",
            "Forecasting models must convolve flight banks at t+2."
        ]
    )

    c_lag_right = add_card(s26, Inches(6.8), Inches(1.85), Inches(5.733), Inches(5.0), WHITE, LINE_BORDER)
    tf = c_lag_right.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_right = Inches(0.3)
    tf.margin_top = Inches(0.3)

    p = tf.paragraphs[0]
    p.text = "EMPIRICAL FINDINGS: LEAD-LAG DECONVOLUTION"
    p.font.bold = True
    p.font.size = Pt(11)
    p.font.color.rgb = BLUE_ACCENT

    p = tf.add_paragraph()
    p.text = "Core Takeaways for Operational Planning"
    p.font.bold = True
    p.font.size = Pt(14)
    p.font.color.rgb = NAVY
    p.space_before = Pt(4)

    ll_pts = [
        ("The 2-Hour Operational Window",
         "The correlation between scheduled aircraft seats and TSA checkpoint arrivals follows a steep bell curve: R²(t) = 0.1982, R²(t+1) = 0.4410, R²(t+2) = 0.5347, R²(t+3) = 0.3120."),
        ("ACRP Report 40 Empirical Validation",
         "Confirms the lognormal parameterization of passenger show-up curves: domestic travelers show up with median arrival lead time of 105 minutes, leisure travelers at 135 minutes."),
        ("Actionable TSA Checkpoint Staffing",
         "TSA shift supervisors must evaluate flight banks 2 hours ahead of departure. Convolving flight schedules at t+2 provides the optimal planning window for opening screening lanes.")
    ]
    for title, desc in ll_pts:
        p = tf.add_paragraph()
        p.text = f"•  {title}"
        p.font.bold = True
        p.font.size = Pt(10.5)
        p.font.color.rgb = DARK_TEXT
        p.space_before = Pt(8)

        p = tf.add_paragraph()
        p.text = desc
        p.font.size = Pt(9.5)
        p.font.color.rgb = SLATE
        p.space_before = Pt(2)

    # ==========================================================================
    # SLIDE 27: CERTIFIED 2025 HOLDOUT BENCHMARKS (TABLE 4.10)
    # ==========================================================================
    s27 = prs.slides.add_slide(blank_layout)
    add_header(s27, "Model Benchmarks", "Certified 2025 Out-of-Time Holdout Benchmarks", "Rigorous Evaluation Across Full Holdout Period (Table 4.10)")

    # Native PowerPoint Table for Table 4.10
    rows = 5
    cols = 8
    t_shape = s27.shapes.add_table(rows, cols, Inches(0.8), Inches(1.85), Inches(11.733), Inches(3.6))
    table = t_shape.table

    # Column widths
    col_widths = [Inches(1.8), Inches(2.3), Inches(1.1), Inches(1.3), Inches(1.3), Inches(1.1), Inches(1.2), Inches(1.633)]
    for i, w in enumerate(col_widths):
        table.columns[i].width = w

    headers = ["Paradigm", "Model Name", "Test R²", "RMSE (pax/h)", "MAE (pax/h)", "Test MASE", "Bias", "Target Status"]
    table_data = [
        ["Baseline Control", "Daily Persistence (t-24)", "0.6719", "253.6", "179.3", "1.000", "-0.7", "Empirical Baseline"],
        ["Model 1", "Deterministic Schedule", "0.4980", "313.4", "215.9", "0.945", "-42.1", "Passed (MASE < 1.0)"],
        ["Model 2", "Supervised ML (LightGBM)", "0.6178", "273.5", "178.0", "0.779", "-18.4", "Passed (MASE < 0.850)"],
        ["Model 3", "Dynamic Two-Stage Hybrid", "0.7483", "222.1", "142.8", "0.662", "-8.5", "Decisive Winner"]
    ]

    for col_idx, h in enumerate(headers):
        cell = table.cell(0, col_idx)
        cell.fill.solid()
        cell.fill.fore_color.rgb = NAVY
        cell.text_frame.margin_left = cell.text_frame.margin_right = Inches(0.1)
        p = cell.text_frame.paragraphs[0]
        p.text = h
        p.font.name = "Calibri"
        p.font.size = Pt(11)
        p.font.bold = True
        p.font.color.rgb = WHITE
        p.alignment = PP_ALIGN.CENTER if col_idx >= 2 else PP_ALIGN.LEFT

    for row_idx, r_data in enumerate(table_data):
        is_winner = (row_idx == 3)
        for col_idx, val in enumerate(r_data):
            cell = table.cell(row_idx + 1, col_idx)
            cell.fill.solid()
            cell.fill.fore_color.rgb = LIGHT_BLUE if is_winner else (WHITE if row_idx % 2 == 0 else SOFT_BG)
            cell.text_frame.margin_left = cell.text_frame.margin_right = Inches(0.1)
            p = cell.text_frame.paragraphs[0]
            p.text = val
            p.font.name = "Calibri"
            p.font.size = Pt(10.5)
            p.font.bold = is_winner or (col_idx == 0)
            p.font.color.rgb = NAVY if is_winner else DARK_TEXT
            p.alignment = PP_ALIGN.CENTER if col_idx >= 2 else PP_ALIGN.LEFT

    # Bottom Note Box
    tb_note = s27.shapes.add_textbox(Inches(0.8), Inches(5.7), Inches(11.733), Inches(1.2))
    tf = tb_note.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "*Note.* Out-of-time test holdout period: January 1, 2025 – December 31, 2025. N = 8,760 hours across the 9-airport experimental cohort. Model 3 achieves the lowest RMSE (222.1 pax/hr) and lowest MASE (0.662), outperforming Daily Persistence by 33.8% and Supervised ML by 18.8% (Diebold-Mariano test DM = -4.82, p < 0.001)."
    p.font.name = "Calibri"
    p.font.size = Pt(10)
    p.font.italic = True
    p.font.color.rgb = SLATE

    # ==========================================================================
    # SLIDE 28: MULTI-PILLAR HYPOTHESIS TESTING (TABLE 4.11 / TABLE 5.4)
    # ==========================================================================
    s28 = prs.slides.add_slide(blank_layout)
    add_header(s28, "Hypothesis Testing", "Multi-Pillar Hypothesis Testing: The Asymmetric Trade-Off", "Full Evaluation Across Table 4.11 and Master Hypothesis H₁")

    pillar_cards = [
        ("DIMENSION 1: ROBUSTNESS", "Routine Daily Operations (Nominal Flow)",
         "Evaluated on calm hours (delays < 15m, 0 cancels).\n\n"
         "• Stated Target: MASE < 0.700\n"
         "• Model 3: MASE = 0.662, RMSE = 222.1 (Lowest Error)\n"
         "• Model 2: MASE = 0.680–0.700 (Pareto Efficient, 0-Latency)\n"
         "• Model 1: MASE = 0.945 (Fails Target)\n\n"
         "Verdict: CONFIRMS H1a. Machine learning & dynamic hybrids win routine accuracy; deterministic schedules fail.",
         GREEN),
        ("DIMENSION 2: RESILIENCE", "Disruption Shock Stability (Convective IROPS)",
         "Evaluated on severe storms (delays ≥ 45m, cancels ≥ 5).\n\n"
         "• Stated Target: R_MASE ≈ 1.00 & TTR < 4.0h\n"
         "• Model 3: R_MASE = 1.05, TTR = 2.8h (DECISIVE WINNER)\n"
         "• Model 2: R_MASE = 2.14, TTR > 8.0h (COLLAPSES)\n"
         "• Model 1: R_MASE = 1.48 (Moderate Degradation)\n\n"
         "Verdict: CONFIRMS H1b. Dynamic hybrid is the sole resilient architecture; pure ML fragilely fails.",
         GREEN),
        ("DIMENSION 3: GENERALIZABILITY", "Zero-Shot Spatial Transfer (EWR → LGA)",
         "Evaluated on spatial transfer without local retraining.\n\n"
         "• Stated Target: RTR ≤ 1.05 & ΔMASE ≤ 10.0%\n"
         "• Model 1: RTR = 1.04, ΔMASE = +4.0% (DECISIVE WINNER)\n"
         "• Model 3: RTR = 1.19, ΔMASE = +21.5% (DECISIVELY FAILS)\n"
         "• Model 2: RTR = 1.28, ΔMASE = +32.0% (FAILS)\n\n"
         "Verdict: CONFIRMS H1c. Deterministic schedule wins zero-shot transfer; complex hybrids overfit concourse geometry.",
         GREEN)
    ]

    card_w = Inches(3.75)
    for i, (title, sub, body, border) in enumerate(pillar_cards):
        x = Inches(0.8) + i * Inches(3.99)
        card = add_card(s28, x, Inches(1.85), card_w, Inches(5.0), WHITE, LINE_BORDER)
        tf = card.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_right = Inches(0.25)
        tf.margin_top = Inches(0.25)

        p = tf.paragraphs[0]
        p.text = title
        p.font.bold = True
        p.font.size = Pt(11)
        p.font.color.rgb = NAVY

        p = tf.add_paragraph()
        p.text = sub
        p.font.bold = True
        p.font.size = Pt(9.5)
        p.font.color.rgb = BLUE_ACCENT
        p.space_before = Pt(2)

        p = tf.add_paragraph()
        p.text = body
        p.font.size = Pt(10)
        p.font.color.rgb = DARK_TEXT
        p.space_before = Pt(8)

    # ==========================================================================
    # SLIDE 29: DEEP-DIVE RESILIENCE & THE EMPTY CHECKPOINT FALLACY
    # ==========================================================================
    s29 = prs.slides.add_slide(blank_layout)
    add_header(s29, "Deep-Dive Resilience", "Dimension 2: Disruption Resilience & Shock Recovery", "Convective Weather Ground Stops and the Empty Checkpoint Fallacy")

    # Top Formula
    add_centered_equation(
        s29, Inches(0.8), Inches(1.85), Inches(11.733), Inches(1.4),
        title="Disruption Shock Recovery Multiplier",
        formula="R_MASE  =  MASE_shock  /  MASE_routine",
        subtext_lines=["Target: R_MASE ≈ 1.00 (Perfect Invariance). Values >> 1.0 indicate acute shock fragility."]
    )

    # Left: Empty Checkpoint Fallacy (Model 2 Collapse)
    c_fallacy = add_card(s29, Inches(0.8), Inches(3.45), Inches(5.7), Inches(3.4), WHITE, LINE_BORDER)
    tf = c_fallacy.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_right = Inches(0.25)
    tf.margin_top = Inches(0.2)
    p = tf.paragraphs[0]
    p.text = "THE EMPTY CHECKPOINT FALLACY (MODEL 2 COLLAPSE)"
    p.font.bold = True
    p.font.size = Pt(11)
    p.font.color.rgb = AMBER

    p = tf.add_paragraph()
    p.text = "R_MASE = 2.14  (Shock Degradation > 114%)"
    p.font.bold = True
    p.font.size = Pt(12)
    p.font.color.rgb = NAVY
    p.space_before = Pt(2)

    pts = [
        "Causal Failure Mechanism: Thunderstorms ground flight banks. Airlines cancel flights in automated telemetry feeds.",
        "Algorithmic Misinterpretation: Decision trees observe cancelled flights and infer that passenger demand has vanished, forecasting near-zero throughput.",
        "The Terminal Reality: Passengers remain packed in concourses and ticket lobbies seeking customer service, rebooking, and security access.",
        "Result: TTR > 8.0 hours. Checkpoint lanes are closed right when crowding is at its worst."
    ]
    for pt in pts:
        p = tf.add_paragraph()
        p.text = f"•  {pt}"
        p.font.size = Pt(10)
        p.font.color.rgb = DARK_TEXT
        p.space_before = Pt(5)

    # Right: Hybrid Error Innovation Rescue (Model 3)
    c_rescue = add_card(s29, Inches(6.8), Inches(3.45), Inches(5.733), Inches(3.4), WHITE, LINE_BORDER)
    tf = c_rescue.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_right = Inches(0.25)
    tf.margin_top = Inches(0.2)
    p = tf.paragraphs[0]
    p.text = "HYBRID ERROR INNOVATION RESCUE (MODEL 3)"
    p.font.bold = True
    p.font.size = Pt(11)
    p.font.color.rgb = GREEN

    p = tf.add_paragraph()
    p.text = "R_MASE = 1.05  ·  TTR = 2.8 Hours (Decisive Winner)"
    p.font.bold = True
    p.font.size = Pt(12)
    p.font.color.rgb = NAVY
    p.space_before = Pt(2)

    pts = [
        "Sensor Feedback Correction: Ingests live screening count from t-1: e_{t-1} = Y_{t-1} - Ŷ_{t-1}.",
        "Immediate Disruption Detection: When hundreds of stranded passengers pass through screening despite flight cancellations, the positive innovation instantly overrides the stale schedule base.",
        "Rapid Convergence: Restores forecast accuracy within 2.8 hours, well below the 4.0-hour FAA operational window.",
        "Operational Outcome: Checkpoint lanes stay appropriately staffed throughout convective weather disruptions."
    ]
    for pt in pts:
        p = tf.add_paragraph()
        p.text = f"•  {pt}"
        p.font.size = Pt(10)
        p.font.color.rgb = DARK_TEXT
        p.space_before = Pt(5)

    # ==========================================================================
    # SLIDE 30: DEEP-DIVE GENERALIZABILITY & SPATIAL TRANSFER
    # ==========================================================================
    s30 = prs.slides.add_slide(blank_layout)
    add_header(s30, "Deep-Dive Generalizability", "Dimension 3: Generalizability & Spatial Transfer", "Zero-Shot Spatial Transfer from Newark (EWR) to LaGuardia (LGA)")

    # Top Formula
    add_centered_equation(
        s30, Inches(0.8), Inches(1.85), Inches(11.733), Inches(1.4),
        title="Relative Spatial Transfer Ratio",
        formula="RTR  =  RMSE_transfer  /  RMSE_in-sample",
        subtext_lines=["Target: RTR ≤ 1.05 & ΔMASE ≤ 10.0%. Evaluates zero-shot transferability without local retraining."]
    )

    # Left: Model 1 Deterministic Winner
    c_m1_win = add_card(s30, Inches(0.8), Inches(3.45), Inches(5.7), Inches(3.4), WHITE, LINE_BORDER)
    tf = c_m1_win.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_right = Inches(0.25)
    tf.margin_top = Inches(0.2)
    p = tf.paragraphs[0]
    p.text = "MODEL 1: DETERMINISTIC SCHEDULE (DECISIVE WINNER)"
    p.font.bold = True
    p.font.size = Pt(11)
    p.font.color.rgb = GREEN

    p = tf.add_paragraph()
    p.text = "RTR = 1.04  ·  ΔMASE = +4.0%  (Passes Target)"
    p.font.bold = True
    p.font.size = Pt(12)
    p.font.color.rgb = NAVY
    p.space_before = Pt(2)

    pts = [
        "Invariance of Human Arrival Psychology: Passenger show-up curves (ACRP Report 40) reflect universal traveler behavior rather than specific airport terminal layout quirks.",
        "Physics-Based Schedule Mapping: Scheduled flight banks and aircraft gauge transfer seamlessly between airports without requiring historical calibration.",
        "Immediate Deployment: Can be applied instantly to new airport concourses, terminal redevelopments, or airline terminal reassignments.",
        "Conclusion: Deterministic physics wins zero-shot spatial transferability."
    ]
    for pt in pts:
        p = tf.add_paragraph()
        p.text = f"•  {pt}"
        p.font.size = Pt(10)
        p.font.color.rgb = DARK_TEXT
        p.space_before = Pt(5)

    # Right: Model 3 Dynamic Hybrid Overfitting Failure
    c_m3_fail = add_card(s30, Inches(6.8), Inches(3.45), Inches(5.733), Inches(3.4), WHITE, LINE_BORDER)
    tf = c_m3_fail.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_right = Inches(0.25)
    tf.margin_top = Inches(0.2)
    p = tf.paragraphs[0]
    p.text = "MODEL 3: DYNAMIC HYBRID (DECISIVELY FAILS)"
    p.font.bold = True
    p.font.size = Pt(11)
    p.font.color.rgb = AMBER

    p = tf.add_paragraph()
    p.text = "RTR = 1.19  ·  ΔMASE = +21.5%  (Decisively Fails Target)"
    p.font.bold = True
    p.font.size = Pt(12)
    p.font.color.rgb = NAVY
    p.space_before = Pt(2)

    pts = [
        "Concourse Geometry Overfitting: Decision trees overfit to Newark Terminal C's unique taxiway delays, concourse corridors, and connecting patterns.",
        "Transfer Distortion: When transferred to LaGuardia Terminal C without retraining, decision splits on delay attributes misfire, producing erratic forecast errors.",
        "Feedback Instability: If the base model generates distorted predictions, the 1-step error innovation feedback amplifies errors rather than correcting them.",
        "Strategic Reality: Complex hybrid models require 6–12 months of local data before they can be safely deployed."
    ]
    for pt in pts:
        p = tf.add_paragraph()
        p.text = f"•  {pt}"
        p.font.size = Pt(10)
        p.font.color.rgb = DARK_TEXT
        p.space_before = Pt(5)

    # ==========================================================================
    # SLIDE 31: OPERATOR'S PLAYBOOK & REAL-WORLD IMPLEMENTATION
    # ==========================================================================
    s31 = prs.slides.add_slide(blank_layout)
    add_header(s31, "Operational Implementation", "Real-World Aviation Application: The Operator's Playbook", "Translating Empirical Findings into Actionable TSA Screening Policy")

    playbook_cards = [
        ("01", "DYNAMIC CHECKPOINT ROSTERING",
         "Abandon static historical volume tables.\n\n"
         "• Roster checkpoint screening lanes based on t+2 flight bank convolutions convolved with empirical show-up curves.\n"
         "• Apply conformal quantile (q85) safety buffers (+1.2 lanes during peak banks) to absorb heavy-traffic arrival burstiness without creating catastrophic queue surges."),
        ("02", "CONNECTING PASSENGER DEFLATION",
         "Stop over-staffing connecting mega-hubs.\n\n"
         "• Ingest BTS DB1B ticket survey originating ratios directly into checkpoint capacity planning algorithms.\n"
         "• Deflating flight seat capacity by local originating share (1 - S_connect) prevents the costly misallocation of TSA security personnel to passengers who never enter landside terminals."),
        ("03", "REGIME-SWITCHED GATED ENGINE",
         "Deploy the hybrid operational policy.\n\n"
         "• Nominal Operations (Delays < 15m): Execute pure Supervised ML (Model 2) for zero-latency, low-compute Pareto efficiency.\n"
         "• Severe Convective Storms (Delays ≥ 45m): Automatically switch to Dynamic Hybrid (Model 3) with floor feedback to eliminate the Empty Checkpoint Fallacy.")
    ]

    card_w = Inches(3.75)
    for i, (num, title, body) in enumerate(playbook_cards):
        x = Inches(0.8) + i * Inches(3.99)
        card = add_card(s31, x, Inches(1.85), card_w, Inches(5.0), WHITE, LINE_BORDER)
        tf = card.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_right = Inches(0.25)
        tf.margin_top = Inches(0.3)

        p = tf.paragraphs[0]
        p.text = f"STRATEGY {num}"
        p.font.bold = True
        p.font.size = Pt(10)
        p.font.color.rgb = BLUE_ACCENT

        p = tf.add_paragraph()
        p.text = title
        p.font.bold = True
        p.font.size = Pt(13)
        p.font.color.rgb = NAVY
        p.space_before = Pt(3)

        p = tf.add_paragraph()
        p.text = body
        p.font.size = Pt(10.5)
        p.font.color.rgb = DARK_TEXT
        p.space_before = Pt(10)

    # ==========================================================================
    # SLIDE 32: RESEARCH SYNTHESIS & FINAL CONCLUSION
    # ==========================================================================
    s32 = prs.slides.add_slide(blank_layout)
    add_header(s32, "Research Synthesis", "Research Synthesis & Concluding Takeaway", "Transforming Airport Security Screening from Reactive Firefighting to Resilient Synchronization")

    # Center Headline Banner
    c_banner = add_card(s32, Inches(0.8), Inches(1.85), Inches(11.733), Inches(1.1), NAVY, NAVY)
    tf = c_banner.text_frame
    tf.word_wrap = True
    tf.vertical_anchor = MSO_ANCHOR.MIDDLE
    tf.margin_left = tf.margin_right = Inches(0.3)
    p = tf.paragraphs[0]
    p.text = "CORE RESEARCH SYNTHESIS"
    p.font.bold = True
    p.font.size = Pt(10)
    p.font.color.rgb = WHITE
    p = tf.add_paragraph()
    p.text = "Transforming Airport Security Screening from Reactive Firefighting to Resilient Stochastic Synchronization"
    p.font.name = "Georgia"
    p.font.bold = True
    p.font.size = Pt(13.5)
    p.font.color.rgb = WHITE
    p.space_before = Pt(2)

    # 4 Key Strategic Bullets Card
    c_takeaways = add_card(s32, Inches(0.8), Inches(3.1), Inches(11.733), Inches(3.75), WHITE, LINE_BORDER)
    tf = c_takeaways.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_right = Inches(0.3)
    tf.margin_top = Inches(0.25)

    bullets = [
        ("The Values vs. Volatility Imperative",
         "Arrival volatility (σ_TSA, CV_TSA), not static passenger headcounts, dictates checkpoint queue formation under Kingman's heavy-traffic formula. Terminal planning must model stochastic arrival variance."),
        ("Proof of the Master Hypothesis (H₁)",
         "Proved the Asymmetric Trade-Off: No single predictive model is universally superior. Model 3 wins Robustness (RMSE) and Resilience; Model 2 wins Routine Pareto Efficiency; Model 1 wins Zero-Shot Spatial Portability."),
        ("Eliminating the Empty Checkpoint Fallacy",
         "Real-time prior-hour screening floor innovation feedback (e_{t-1}) rescues forecasting during severe convective storms, cutting recovery time to 2.8 hours."),
        ("The Regime-Switched Gated Engine",
         "A practical, context-aware operational framework that bridges airside flight schedules and landside passenger screening, delivering operational resilience without unnecessary computational overhead.")
    ]
    for title, desc in bullets:
        p = tf.add_paragraph() if tf.paragraphs[0].text else tf.paragraphs[0]
        p.text = f"•  {title}:"
        p.font.bold = True
        p.font.size = Pt(11)
        p.font.color.rgb = NAVY
        p.space_before = Pt(6)

        p = tf.add_paragraph()
        p.text = f"   {desc}"
        p.font.size = Pt(10)
        p.font.color.rgb = DARK_TEXT
        p.space_before = Pt(2)

    p_close = tf.add_paragraph()
    p_close.text = "Thank you for your guidance, mentorship, and support. Questions & Discussion."
    p_close.font.name = "Georgia"
    p_close.font.bold = True
    p_close.font.italic = True
    p_close.font.size = Pt(12)
    p_close.font.color.rgb = BLUE_ACCENT
    p_close.space_before = Pt(12)
    p_close.alignment = PP_ALIGN.CENTER

    # Save presentation
    prs.save(OUTPUT_PATH)
    print(f"Successfully generated clean presentation: {OUTPUT_PATH}")

    # Mirror to master-docs
    os.makedirs(os.path.dirname(MIRROR_PATH), exist_ok=True)
    shutil.copyfile(OUTPUT_PATH, MIRROR_PATH)
    print(f"Successfully mirrored presentation to: {MIRROR_PATH}")


if __name__ == "__main__":
    create_deck()
