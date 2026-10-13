"""
build_recommended_defense_deck.py
Redesigned: Clean, Minimalist, Visual Defense Presentation Deck.
Eliminates text box clutter, embeds certified figures/graphs, uses clean process diagrams,
and centers mathematical equations with minimal text and high visual impact.
"""

import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE

BASE_DIR = "/Users/leilagleich/Library/CloudStorage/OneDrive-Embry-RiddleAeronauticalUniversity/final-thesis"

def create_deck(output_path):
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    # Minimalist Professional Palette
    NAVY = RGBColor(10, 34, 64)          # Primary ERAU Navy
    LIGHT_NAVY = RGBColor(24, 52, 94)    # Accent Navy
    SLATE = RGBColor(71, 85, 105)        # Clean Muted Slate
    DARK_TEXT = RGBColor(15, 23, 42)     # Body Text
    MUTED_TEXT = RGBColor(148, 163, 184) # Muted Label Grey
    BLUE_ACCENT = RGBColor(37, 99, 235)  # Vivid Accent
    SOFT_BG = RGBColor(248, 250, 252)    # Subtle Card Fill
    LINE_BORDER = RGBColor(226, 232, 240)# Hairline Border
    WHITE = RGBColor(255, 255, 255)
    GREEN = RGBColor(22, 101, 52)        # Success Dark Green
    AMBER = RGBColor(180, 83, 9)         # Caution Dark Amber

    def add_header(slide, tracker, title, subtitle=None):
        header_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.4), Inches(11.733), Inches(1.1))
        tf = header_box.text_frame
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
        p1.space_before = Pt(2)

        if subtitle:
            p2 = tf.add_paragraph()
            p2.text = subtitle
            p2.font.name = "Calibri"
            p2.font.size = Pt(12)
            p2.font.color.rgb = SLATE
            p2.space_before = Pt(2)

    def add_card(slide, left, top, width, height, bg_color=SOFT_BG, border_color=LINE_BORDER):
        shape = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, left, top, width, height)
        shape.fill.solid()
        shape.fill.fore_color.rgb = bg_color
        shape.line.color.rgb = border_color
        shape.line.width = Pt(1)
        return shape

    def add_centered_equation(slide, left, top, width, height, title, formula, subtext=None):
        card = add_card(slide, left, top, width, height, WHITE, LINE_BORDER)
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

        if subtext:
            p2 = tf.add_paragraph()
            p2.text = subtext
            p2.font.name = "Calibri"
            p2.font.size = Pt(11)
            p2.font.color.rgb = SLATE
            p2.alignment = PP_ALIGN.CENTER

    def add_image_safe(slide, rel_path, left, top, width=None, height=None):
        full_path = os.path.join(BASE_DIR, rel_path)
        if os.path.exists(full_path):
            if width and height:
                return slide.shapes.add_picture(full_path, left, top, width=width, height=height)
            elif width:
                return slide.shapes.add_picture(full_path, left, top, width=width)
            elif height:
                return slide.shapes.add_picture(full_path, left, top, height=height)
            else:
                return slide.shapes.add_picture(full_path, left, top)
        print(f"Warning: Image not found: {full_path}")
        return None

    def add_smart_process(slide, top_y, steps, width=Inches(11.7), height=Inches(1.1)):
        n = len(steps)
        gap = Inches(0.2)
        step_w = (width - gap * (n - 1)) / n
        left_start = Inches(0.8)

        for i, (num, title, sub) in enumerate(steps):
            x = left_start + i * (step_w + gap)
            shape = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, x, top_y, step_w, height)
            shape.fill.solid()
            shape.fill.fore_color.rgb = SOFT_BG if i < n-1 else NAVY
            shape.line.color.rgb = LINE_BORDER if i < n-1 else NAVY
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
            p0.font.color.rgb = NAVY if i < n-1 else WHITE

            p1 = tf.add_paragraph()
            p1.text = sub
            p1.font.name = "Calibri"
            p1.font.size = Pt(9.5)
            p1.font.color.rgb = SLATE if i < n-1 else MUTED_TEXT
            p1.space_before = Pt(2)

    # ==========================================
    # SLIDE 1: TITLE SLIDE
    # ==========================================
    s1 = prs.slides.add_slide(blank_layout)
    bar = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(0.25))
    bar.fill.solid()
    bar.fill.fore_color.rgb = NAVY
    bar.line.fill.background()

    tb = s1.shapes.add_textbox(Inches(1.2), Inches(2.0), Inches(10.9), Inches(4.5))
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
    p.space_before = Pt(14)
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
    p.space_before = Pt(36)

    # ==========================================
    # SLIDE 2: PRESENTATION OUTLINE
    # ==========================================
    s2 = prs.slides.add_slide(blank_layout)
    add_header(s2, "Executive Roadmap", "Defense Presentation Roadmap", "25-Minute Structured Oral Examination across Six Operational Phases")

    steps_s2 = [
        ("01", "Research Problem & Hypotheses", "Kingman queuing friction, volatility targeting, and Asymmetric Trade-Offs (H1)"),
        ("02", "Literature & Theoretical Evolution", "Evolution from deterministic schedules and simulation to ML and dynamic 2-stage hybrids"),
        ("03", "Econometric Data Pipeline", "4-tier filtering funnel, DB1B connecting deflation, and carrier checkpoint isolation"),
        ("04", "Empirical Volatility Findings", "Values vs. Volatility coupling (R² = 19.1%), 4 annual seasons, and bimodal diurnal peaks"),
        ("05", "Model Execution & Benchmarks", "Certified 2025 holdouts: Robustness, Resilience (IROPS shocks), and Generalizability"),
        ("06", "Operational Implementation", "Regime-switched gated inference playbook and dynamic checkpoint allocation")
    ]
    for i, (num, title_txt, desc_txt) in enumerate(steps_s2):
        col = i % 3
        row = i // 3
        x = Inches(0.8 + col * 4.0)
        y = Inches(1.8 + row * 2.6)
        card = add_card(s2, x, y, Inches(3.7), Inches(2.3), WHITE, LINE_BORDER)
        tf = card.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_right = Inches(0.25)
        tf.margin_top = Inches(0.2)

        p = tf.paragraphs[0]
        p.text = num
        p.font.name = "Calibri"
        p.font.size = Pt(22)
        p.font.bold = True
        p.font.color.rgb = BLUE_ACCENT

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
    # SLIDE 3: RESEARCH PROBLEM (KINGMAN'S LAW & QUEUING FRICTION)
    # ==========================================
    s3 = prs.slides.add_slide(blank_layout)
    add_header(s3, "Theoretical Foundation", "The Terminal Queuing Problem", "Why Static Volume Staffing Fails Under Stochastic Arrival Burstiness")

    add_centered_equation(
        s3, Inches(0.8), Inches(1.8), Inches(5.6), Inches(5.0),
        "Kingman's Heavy-Traffic Queuing Approximation",
        "W_q  ≈  ( ρ / (1 - ρ) ) · ( (C_a² + C_s²) / 2 ) · ( 1 / μ )",
        "Key Operational Implications:\n\n"
        "1. Delay scales quadratically with arrival volatility (C_a²), not volume.\n\n"
        "2. As lane utilization ρ approaches 1.0, variance bursts cause exponential delay spikes.\n\n"
        "3. Static hourly passenger counts completely mask heavy-traffic queuing friction."
    )

    c_top = add_card(s3, Inches(6.8), Inches(1.8), Inches(5.7), Inches(2.35), SOFT_BG, LINE_BORDER)
    tf = c_top.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_right = Inches(0.3)
    tf.margin_top = Inches(0.2)
    p = tf.paragraphs[0]
    p.text = "THE OPERATIONAL REALITY"
    p.font.name = "Calibri"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = BLUE_ACCENT
    p = tf.add_paragraph()
    p.text = "Inflexible Security Infrastructure"
    p.font.name = "Calibri"
    p.font.size = Pt(16)
    p.font.bold = True
    p.font.color.rgb = NAVY
    p.space_before = Pt(3)
    p = tf.add_paragraph()
    p.text = "Physical screening lanes (AIT body scanners, baggage X-ray, TSO staffing) cannot expand dynamically in real time. Static historical tables leave checkpoints chronically mismatched to flight bank surges."
    p.font.name = "Calibri"
    p.font.size = Pt(11.5)
    p.font.color.rgb = SLATE
    p.space_before = Pt(6)

    c_bot = add_card(s3, Inches(6.8), Inches(4.45), Inches(5.7), Inches(2.35), WHITE, LINE_BORDER)
    tf = c_bot.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_right = Inches(0.3)
    tf.margin_top = Inches(0.2)
    p = tf.paragraphs[0]
    p.text = "THE STOCHASTIC MECHANISM"
    p.font.name = "Calibri"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = AMBER
    p = tf.add_paragraph()
    p.text = "Passenger Arrivals Lead, Flight Delays Lag"
    p.font.name = "Calibri"
    p.font.size = Pt(16)
    p.font.bold = True
    p.font.color.rgb = NAVY
    p.space_before = Pt(3)
    p = tf.add_paragraph()
    p.text = "Passengers show up 2 hours ahead of scheduled flight departures. Downline aircraft delays accumulate in late afternoon banks. Modeling this temporal asynchrony requires capturing variance, not static numbers."
    p.font.name = "Calibri"
    p.font.size = Pt(11.5)
    p.font.color.rgb = SLATE
    p.space_before = Pt(6)

    # ==========================================
    # SLIDE 4: RESEARCH PURPOSE
    # ==========================================
    s4 = prs.slides.add_slide(blank_layout)
    add_header(s4, "Research Formulation", "Research Purpose & Operational Objectives", "Transforming Terminal Security from Static Accounting to Stochastic Forecasting")

    purp_cards = [
        ("OBJECTIVE 1", "Target Throughput Volatility", "Pivot from static volume (y_t) to volatility targets: diurnal dispersion (σ_TSA) and scale-free burstiness (CV_TSA = σ/μ)."),
        ("OBJECTIVE 2", "Comparative Model Suite", "Empirically evaluate three distinct paradigms—deterministic schedules, supervised ML, and 2-stage dynamic hybrids—against a persistence control."),
        ("OBJECTIVE 3", "Context-Aware Optimization", "Prove that predictive superiority is contingent upon operational regime: routine flow vs. severe convective disruptions vs. spatial facility transfer.")
    ]
    for i, (tag, title, desc) in enumerate(purp_cards):
        x = Inches(0.8 + i * 4.0)
        card = add_card(s4, x, Inches(2.0), Inches(3.7), Inches(4.8), WHITE, LINE_BORDER)
        tf = card.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_right = Inches(0.3)
        tf.margin_top = Inches(0.3)

        p = tf.paragraphs[0]
        p.text = tag
        p.font.name = "Calibri"
        p.font.size = Pt(11)
        p.font.bold = True
        p.font.color.rgb = BLUE_ACCENT

        p = tf.add_paragraph()
        p.text = title
        p.font.name = "Calibri"
        p.font.size = Pt(18)
        p.font.bold = True
        p.font.color.rgb = NAVY
        p.space_before = Pt(8)

        p = tf.add_paragraph()
        p.text = desc
        p.font.name = "Calibri"
        p.font.size = Pt(12)
        p.font.color.rgb = SLATE
        p.space_before = Pt(14)

    # ==========================================
    # SLIDE 5: RESEARCH QUESTION
    # ==========================================
    s5 = prs.slides.add_slide(blank_layout)
    add_header(s5, "Core Inquiry", "Primary Research Question", "Evaluating Predictive Paradigms Across Competing Operational Trade-Offs")

    stmt_card = add_card(s5, Inches(1.2), Inches(1.8), Inches(10.9), Inches(2.2), WHITE, BLUE_ACCENT)
    tf = stmt_card.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_right = Inches(0.4)
    tf.margin_top = Inches(0.25)
    p = tf.paragraphs[0]
    p.text = "RESEARCH QUESTION (RQ₁)"
    p.font.name = "Calibri"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = BLUE_ACCENT
    p.alignment = PP_ALIGN.CENTER
    p = tf.add_paragraph()
    p.text = "“Which predictive modeling frameworks—spanning deterministic persistence controls, deterministic schedule baselines, machine learning, and dynamic two-stage hybrids—are most effective for forecasting airport passenger security screening throughput volatility when prioritizing robustness, resilience, or generalizability as the primary operational evaluation metric?”"
    p.font.name = "Georgia"
    p.font.size = Pt(15)
    p.font.color.rgb = NAVY
    p.alignment = PP_ALIGN.CENTER
    p.space_before = Pt(6)

    pills_s5 = [
        ("Robustness", "Routine Accuracy", "Lowest RMSE & MASE < 0.700 under nominal on-time operations (delay < 15m, 0 cancels)."),
        ("Resilience", "Disruption Stability", "Multiplier R_MASE ≈ 1.00 & recovery TTR < 4.0h during severe convective IROPS."),
        ("Generalizability", "Spatial Portability", "Zero-shot transfer error penalty ΔMASE ≤ 10% deployed to new terminal layouts.")
    ]
    for i, (dim, sub, desc) in enumerate(pills_s5):
        x = Inches(1.2 + i * 3.8)
        card = add_card(s5, x, Inches(4.3), Inches(3.3), Inches(2.5), SOFT_BG, LINE_BORDER)
        tf = card.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_right = Inches(0.2)
        tf.margin_top = Inches(0.2)
        p = tf.paragraphs[0]
        p.text = dim.upper()
        p.font.name = "Calibri"
        p.font.size = Pt(13)
        p.font.bold = True
        p.font.color.rgb = NAVY
        p = tf.add_paragraph()
        p.text = sub
        p.font.name = "Calibri"
        p.font.size = Pt(11)
        p.font.bold = True
        p.font.color.rgb = BLUE_ACCENT
        p.space_before = Pt(2)
        p = tf.add_paragraph()
        p.text = desc
        p.font.name = "Calibri"
        p.font.size = Pt(10.5)
        p.font.color.rgb = SLATE
        p.space_before = Pt(6)

    # ==========================================
    # SLIDE 6: HYPOTHESIS: THE ASYMMETRIC TRADE-OFF
    # ==========================================
    s6 = prs.slides.add_slide(blank_layout)
    add_header(s6, "Theoretical Formulation", "Hypothesis: The Asymmetric Trade-Off (H₁)", "No Single Predictive Technique is Universally Dominant Across All Operating Regimes")

    h1_ban = add_card(s6, Inches(0.8), Inches(1.8), Inches(11.7), Inches(1.1), SOFT_BG, LINE_BORDER)
    tf = h1_ban.text_frame
    tf.word_wrap = True
    tf.margin_left = Inches(0.3)
    tf.margin_top = Inches(0.12)
    p = tf.paragraphs[0]
    p.text = "MASTER HYPOTHESIS (H₁)"
    p.font.name = "Calibri"
    p.font.size = Pt(10)
    p.font.bold = True
    p.font.color.rgb = BLUE_ACCENT
    p = tf.add_paragraph()
    p.text = "Across the candidate modeling paradigms evaluated, no individual approach will prove superior across all three performance measures (robustness, resilience, and generalizability)."
    p.font.name = "Calibri"
    p.font.size = Pt(14)
    p.font.bold = True
    p.font.color.rgb = NAVY
    p.space_before = Pt(2)

    sub_h = [
        ("H₁ₐ  ·  Robustness", "Routine Accuracy Winner", "Model 2 (Machine Learning) & Model 3 (Hybrid) achieve MASE < 0.700 under nominal rhythms.\n\nDeterministic baselines fail due to schedule rigidity."),
        ("H₁ᵦ  ·  Resilience", "Disruption Shock Winner", "Model 3 (Dynamic Hybrid) is the sole model satisfying resilience (R_MASE ≈ 1.05).\n\nModel 2 collapses (R = 2.14) due to the Empty Checkpoint Fallacy."),
        ("H₁꜀  ·  Generalizability", "Zero-Shot Transfer Winner", "Model 1 (Deterministic) satisfies transfer targets (RTR = 1.04, ΔMASE = +4.0%).\n\nModel 3 fails (RTR = 1.19, ΔMASE = +21.5%) due to terminal layout overfitting.")
    ]
    for i, (tag, win, desc) in enumerate(sub_h):
        x = Inches(0.8 + i * 4.0)
        card = add_card(s6, x, Inches(3.2), Inches(3.7), Inches(3.6), WHITE, LINE_BORDER)
        tf = card.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_right = Inches(0.25)
        tf.margin_top = Inches(0.2)
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
        p.font.color.rgb = BLUE_ACCENT
        p.space_before = Pt(3)
        p = tf.add_paragraph()
        p.text = desc
        p.font.name = "Calibri"
        p.font.size = Pt(11)
        p.font.color.rgb = SLATE
        p.space_before = Pt(8)

    # ==========================================
    # SLIDE 7: DYNAMIC PERFORMANCE MEASURES (RADAR CHART EMBEDDED)
    # ==========================================
    s7 = prs.slides.add_slide(blank_layout)
    add_header(s7, "Evaluative Trio", "The Multi-Pillar Performance Framework", "Evaluating Models Beyond Single-Metric Annual Global Minimization")

    # Embed Figure 5.1 Radar Chart
    add_image_safe(s7, "figures/figure_5_1_asymmetric_trade_off_triangle.png", Inches(0.8), Inches(1.8), width=Inches(5.6))

    p_info = [
        ("Dimension 1: Robustness", "Nominal Accuracy", "Lowest RMSE & MASE < 0.700 under on-time baseline operations (delay < 15 min, 0 cancellations). Ensures reliable day-to-day base staffing rosters."),
        ("Dimension 2: Resilience", "Disruption Recovery", "Recovery multiplier R_MASE ≈ 1.00 & TTR < 4.0h during severe convective disruptions (delay ≥ 45 min, cancels ≥ 5). Prevents lobby gridlock."),
        ("Dimension 3: Generalizability", "Spatial Portability", "Zero-shot transfer ratio RTR ≤ 1.05 & error penalty ΔMASE ≤ 10% deployed to new airports without local retraining.")
    ]
    for i, (dim_title, dim_sub, dim_txt) in enumerate(p_info):
        y = Inches(1.8 + i * 1.7)
        card = add_card(s7, Inches(6.8), y, Inches(5.7), Inches(1.5), WHITE, LINE_BORDER)
        tf = card.text_frame
        tf.word_wrap = True
        tf.margin_left = Inches(0.25)
        tf.margin_top = Inches(0.12)
        p = tf.paragraphs[0]
        p.text = dim_title
        p.font.name = "Calibri"
        p.font.size = Pt(13)
        p.font.bold = True
        p.font.color.rgb = NAVY
        p = tf.add_paragraph()
        p.text = dim_sub.upper()
        p.font.name = "Calibri"
        p.font.size = Pt(10.5)
        p.font.bold = True
        p.font.color.rgb = BLUE_ACCENT
        p.space_before = Pt(2)
        p = tf.add_paragraph()
        p.text = dim_txt
        p.font.name = "Calibri"
        p.font.size = Pt(10.5)
        p.font.color.rgb = SLATE
        p.space_before = Pt(2)

    # ==========================================
    # SLIDE 8: EXISTING LITERATURE OVERVIEW (MODELS & TESTS DIAGRAM EMBEDDED)
    # ==========================================
    s8 = prs.slides.add_slide(blank_layout)
    add_header(s8, "Theoretical Evolution", "Evolution of Terminal Flow Literature", "Bridging the Historical Divide Between Airside Operations and Landside Security")

    lit_steps = [
        ("1990s", "Deterministic Schedules", "Flight bank seat convolution; assumes 100% on-time departures."),
        ("2000s", "Micro-Simulation", "Agent-based passenger paths; detailed layout but high latency."),
        ("2015+", "Supervised ML", "Decision trees with delay covariates; low routine error, brittle in shocks."),
        ("Today", "Two-Stage Hybrids", "Schedule baseline + live floor feedback; resilient to disruptions.")
    ]
    add_smart_process(s8, Inches(1.8), lit_steps, width=Inches(11.7), height=Inches(1.1))

    # Embed Models and Tests Figure
    add_image_safe(s8, "figures/models and tests.png", Inches(1.8), Inches(3.2), height=Inches(3.8))

    # ==========================================
    # SLIDE 9: LITERATURE GAP: VOLATILITY IS CRITICAL (OTP VOLATILITY EMBEDDED)
    # ==========================================
    s9 = prs.slides.add_slide(blank_layout)
    add_header(s9, "Literature Gap", "The Static Fallacy in Terminal Modeling", "Why Aggregate Passenger Headcounts Fail to Capture Heavy-Traffic Congestion")

    add_centered_equation(
        s9, Inches(0.8), Inches(1.8), Inches(5.6), Inches(5.0),
        "Scale-Free Volatility Metric",
        "CV_TSA  =  σ_TSA / μ_TSA",
        "Scale-Free Arrival Burstiness:\n\n"
        "• Normalizes arrival volatility across mega-hubs and regional terminals.\n\n"
        "• Static volume (y_t) correlates negligibly with flight delays (R² = 2.5%).\n\n"
        "• Volatility metrics correlate tightly with delay dispersion (R² = 19.1%, r = +0.4373)."
    )

    # Embed OTP Volatility Figure
    add_image_safe(s9, "figures/OTP volatility.png", Inches(6.8), Inches(1.8), width=Inches(5.7))

    # ==========================================
    # SLIDE 10: TRADITIONAL MODELS (PAX ARRIVAL CURVES EMBEDDED)
    # ==========================================
    s10 = prs.slides.add_slide(blank_layout)
    add_header(s10, "Literature Breakdown", "Deterministic Flight Schedules & Classical Queueing", "The Operational Baseline: Convolving Scheduled Flight Banks (Model 1)")

    add_centered_equation(
        s10, Inches(0.8), Inches(1.8), Inches(5.6), Inches(5.0),
        "Deterministic Schedule Convolution",
        "Ŷ_t  =  ∑ [Seats_i · (1 - S_connect) · P(t - DEP_i)]",
        "Empirical Passenger Show-Up Dynamics:\n\n"
        "• Convolves scheduled departure times DEP_i over empirical show-up curves P(τ).\n\n"
        "• Strengths: 100% transparent, zero calibration compute, highly interpretable.\n\n"
        "• Fatal Flaw: Rigid schedule assumptions leave models blind to downline delay ripples."
    )

    # Embed Pax Stochastic Arrival Figure
    add_image_safe(s10, "figures/pax stochastic arrival.png", Inches(6.8), Inches(2.0), width=Inches(5.7))

    # ==========================================
    # SLIDE 11: SHIFT TO MICRO-SIMULATION
    # ==========================================
    s11 = prs.slides.add_slide(blank_layout)
    add_header(s11, "Literature Breakdown", "The Shift to Micro-Simulation Modeling", "High Terminal Architectural Fidelity vs. Real-Time Operational Latency Barriers")

    c_pro = add_card(s11, Inches(0.8), Inches(1.8), Inches(5.6), Inches(5.0), SOFT_BG, LINE_BORDER)
    tf = c_pro.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_right = Inches(0.3)
    tf.margin_top = Inches(0.3)
    p = tf.paragraphs[0]
    p.text = "ADVANTAGES OF MICRO-SIMULATION"
    p.font.name = "Calibri"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = GREEN
    p = tf.add_paragraph()
    p.text = "Granular Physical Fidelity"
    p.font.name = "Calibri"
    p.font.size = Pt(18)
    p.font.bold = True
    p.font.color.rgb = NAVY
    p.space_before = Pt(4)
    p = tf.add_paragraph()
    p.text = "• Models individual passenger walking paths, baggage check, and screening queues.\n\n• Resolves complex multi-checkpoint concourse layouts (Simio, CAST, ARENA).\n\n• Captures split processing between TSA PreCheck, standard screening, and CLEAR biometric lanes."
    p.font.name = "Calibri"
    p.font.size = Pt(12)
    p.font.color.rgb = SLATE
    p.space_before = Pt(12)

    c_con = add_card(s11, Inches(6.8), Inches(1.8), Inches(5.7), Inches(5.0), WHITE, LINE_BORDER)
    tf = c_con.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_right = Inches(0.3)
    tf.margin_top = Inches(0.3)
    p = tf.paragraphs[0]
    p.text = "OPERATIONAL LIMITATIONS"
    p.font.name = "Calibri"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = AMBER
    p = tf.add_paragraph()
    p.text = "The Dispatch Latency Barrier"
    p.font.name = "Calibri"
    p.font.size = Pt(18)
    p.font.bold = True
    p.font.color.rgb = NAVY
    p.space_before = Pt(4)
    p = tf.add_paragraph()
    p.text = "• Heavy Calibration Overhead: Hundreds of micro-parameters become obsolete during severe weather.\n\n• Computational Latency: 20–45 minute runtimes prohibit real-time dynamic checkpoint lane rebalancing.\n\n• Airside Isolation: Fails to integrate live FAA air traffic management and taxiway queue buildup."
    p.font.name = "Calibri"
    p.font.size = Pt(12)
    p.font.color.rgb = SLATE
    p.space_before = Pt(12)

    # ==========================================
    # SLIDE 12: ADVANCED PREDICTIVE MODELS (MACHINE LEARNING)
    # ==========================================
    s12 = prs.slides.add_slide(blank_layout)
    add_header(s12, "Literature Breakdown", "Supervised Machine Learning (Model 2)", "Capturing Multi-Variable Operational Interactions vs. Regimes of Severe Brittleness")

    card_stat = add_card(s12, Inches(0.8), Inches(1.8), Inches(3.6), Inches(5.0), WHITE, LINE_BORDER)
    tf = card_stat.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_right = Inches(0.2)
    tf.margin_top = Inches(0.4)
    p = tf.paragraphs[0]
    p.text = "24"
    p.font.name = "Calibri"
    p.font.size = Pt(54)
    p.font.bold = True
    p.font.color.rgb = NAVY
    p.alignment = PP_ALIGN.CENTER
    p = tf.add_paragraph()
    p.text = "BTS OTP & Schedule Features"
    p.font.name = "Calibri"
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = BLUE_ACCENT
    p.alignment = PP_ALIGN.CENTER
    p.space_before = Pt(4)
    p = tf.add_paragraph()
    p.text = "Taxi-out duration, cancellations, cause decompositions, aircraft gauge tiers, and flight bank dispersion metrics."
    p.font.name = "Calibri"
    p.font.size = Pt(11)
    p.font.color.rgb = SLATE
    p.alignment = PP_ALIGN.CENTER
    p.space_before = Pt(8)

    c_r1 = add_card(s12, Inches(4.8), Inches(1.8), Inches(7.7), Inches(2.35), SOFT_BG, LINE_BORDER)
    tf = c_r1.text_frame
    tf.word_wrap = True
    tf.margin_left = Inches(0.3)
    tf.margin_top = Inches(0.18)
    p = tf.paragraphs[0]
    p.text = "ROUTINE OPERATIONS STRENGTH"
    p.font.name = "Calibri"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = GREEN
    p = tf.add_paragraph()
    p.text = "Pareto Optimal Nominal Accuracy"
    p.font.name = "Calibri"
    p.font.size = Pt(16)
    p.font.bold = True
    p.font.color.rgb = NAVY
    p.space_before = Pt(2)
    p = tf.add_paragraph()
    p.text = "Gradient-boosted decision trees capture complex airside-landside interactions, delivering exceptional routine accuracy (MASE = 0.680–0.700) with zero feedback compute latency."
    p.font.name = "Calibri"
    p.font.size = Pt(11.5)
    p.font.color.rgb = SLATE
    p.space_before = Pt(4)

    c_r2 = add_card(s12, Inches(4.8), Inches(4.45), Inches(7.7), Inches(2.35), WHITE, LINE_BORDER)
    tf = c_r2.text_frame
    tf.word_wrap = True
    tf.margin_left = Inches(0.3)
    tf.margin_top = Inches(0.18)
    p = tf.paragraphs[0]
    p.text = "DISRUPTION BRITTLENESS FLAW"
    p.font.name = "Calibri"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = AMBER
    p = tf.add_paragraph()
    p.text = "The Empty Checkpoint Fallacy"
    p.font.name = "Calibri"
    p.font.size = Pt(16)
    p.font.bold = True
    p.font.color.rgb = NAVY
    p.space_before = Pt(2)
    p = tf.add_paragraph()
    p.text = "During convective ground stops, scheduled flights vanish from electronic airline feeds. The ML model falsely predicts zero checkpoint demand, while thousands of passengers remain stranded in lobbies."
    p.font.name = "Calibri"
    p.font.size = Pt(11.5)
    p.font.color.rgb = SLATE
    p.space_before = Pt(4)

    # ==========================================
    # SLIDE 13: HYBRID ARCHITECTURES
    # ==========================================
    s13 = prs.slides.add_slide(blank_layout)
    add_header(s13, "Literature Breakdown", "Sequential Two-Stage Hybrid Architectures (Model 3)", "Coupling Base Flight Schedules with Real-Time Dynamic Error Innovation Feedback")

    add_centered_equation(
        s13, Inches(0.8), Inches(1.8), Inches(11.7), Inches(2.2),
        "Two-Stage Sequential Hybrid Formulation",
        "Ŷ_t  =  M_base(Schedule_t, Features_t)  +  α · ( Y_{t-1} - Ŷ_{t-1} )",
        "Stage 1: Base machine learning model captures cyclical flight schedules and operational covariates.\n"
        "Stage 2: Real-time 1-step error innovation feedback (e_{t-1}) injects live floor telemetry, dynamically correcting lobby backlog."
    )

    c13_1 = add_card(s13, Inches(0.8), Inches(4.3), Inches(5.6), Inches(2.5), SOFT_BG, LINE_BORDER)
    tf = c13_1.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_right = Inches(0.3)
    tf.margin_top = Inches(0.2)
    p = tf.paragraphs[0]
    p.text = "STAGE 2 SHOCK RESCUE"
    p.font.name = "Calibri"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = GREEN
    p = tf.add_paragraph()
    p.text = "Overcoming Schedule Blindness"
    p.font.name = "Calibri"
    p.font.size = Pt(16)
    p.font.bold = True
    p.font.color.rgb = NAVY
    p.space_before = Pt(3)
    p = tf.add_paragraph()
    p.text = "When storms ground flights, Stage 1 falsely predicts near-zero arrivals. The prior-hour floor observation Y_{t-1} detects massive queue backlogs, instantly lifting forecasts."
    p.font.name = "Calibri"
    p.font.size = Pt(11.5)
    p.font.color.rgb = SLATE
    p.space_before = Pt(6)

    c13_2 = add_card(s13, Inches(6.8), Inches(4.3), Inches(5.7), Inches(2.5), WHITE, LINE_BORDER)
    tf = c13_2.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_right = Inches(0.3)
    tf.margin_top = Inches(0.2)
    p = tf.paragraphs[0]
    p.text = "THE ASYMMETRIC TRADE-OFF PENALTY"
    p.font.name = "Calibri"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = AMBER
    p = tf.add_paragraph()
    p.text = "Spatial Overfitting Penalty"
    p.font.name = "Calibri"
    p.font.size = Pt(16)
    p.font.bold = True
    p.font.color.rgb = NAVY
    p.space_before = Pt(3)
    p = tf.add_paragraph()
    p.text = "Requires active, low-latency API floor feeds. Furthermore, decision trees overfit to specific source terminal geometry, causing Model 3 to fail spatial generalizability."
    p.font.name = "Calibri"
    p.font.size = Pt(11.5)
    p.font.color.rgb = SLATE
    p.space_before = Pt(6)

    # ==========================================
    # SLIDE 14: IMPACT OF COVID & VOLATILITY (FIGURE EMBEDDED)
    # ==========================================
    s14 = prs.slides.add_slide(blank_layout)
    add_header(s14, "Empirical Demarcation", "The Structural Impact of COVID-19 Demarcation", "Establishing Post-Pandemic Behavioral Stability (May 1, 2022 – December 31, 2025)")

    # Embed Post-Pandemic Justification Figure
    add_image_safe(s14, "figures/post-pandemic justification.png", Inches(0.8), Inches(1.8), width=Inches(6.2))

    covid_stats = [
        ("May 1, 2022", "Demarcation Cutoff", "Federal mask mandate dissolved; marks return to normal passenger behavior."),
        ("F = 1.42", "Chow Stability Test", "p = 0.18 (fails to reject null of structural stability across 44 months)."),
        ("84.7%", "Load Factor Recovery", "Systemwide passenger load factors fully recovered to pre-pandemic baselines.")
    ]
    for i, (num_s, lab_s, desc_s) in enumerate(covid_stats):
        y = Inches(1.8 + i * 1.7)
        card = add_card(s14, Inches(7.4), y, Inches(5.1), Inches(1.5), WHITE, LINE_BORDER)
        tf = card.text_frame
        tf.word_wrap = True
        tf.margin_left = Inches(0.25)
        tf.margin_top = Inches(0.12)
        p = tf.paragraphs[0]
        p.text = num_s
        p.font.name = "Calibri"
        p.font.size = Pt(20)
        p.font.bold = True
        p.font.color.rgb = NAVY
        p = tf.add_paragraph()
        p.text = lab_s.upper()
        p.font.name = "Calibri"
        p.font.size = Pt(10)
        p.font.bold = True
        p.font.color.rgb = BLUE_ACCENT
        p.space_before = Pt(2)
        p = tf.add_paragraph()
        p.text = desc_s
        p.font.name = "Calibri"
        p.font.size = Pt(10.5)
        p.font.color.rgb = SLATE
        p.space_before = Pt(2)

    # ==========================================
    # SLIDE 15: IMPORTANCE OF DYNAMIC PERFORMANCE MEASURES
    # ==========================================
    s15 = prs.slides.add_slide(blank_layout)
    add_header(s15, "Evaluative Synthesis", "Why Aviation Demands Dynamic Performance Measures", "The Fatal Pitfall of Single-Metric Global Minimization in Airport Operations")

    cards_15 = [
        ("Nominal Rhythms (Robustness)", "A model optimized purely for annual RMSE minimizes routine errors during sunny days. However, routine operations are computationally cheap and tolerant of minor variance.", BLUE_ACCENT),
        ("Disruption Shocks (Resilience)", "Airport crises occur during convective storm fronts. If a model collapses during IROPS (like Model 2's 2.14x error surge), it endangers terminal operations when accuracy matters most.", AMBER),
        ("Facility Transfer (Generalizability)", "Airports cannot afford 12 months of local calibration data for newly built concourses. Models must possess zero-shot transferability across physical terminal layouts.", GREEN)
    ]
    for i, (title_t, desc_t, col_acc) in enumerate(cards_15):
        x = Inches(0.8 + i * 4.0)
        card = add_card(s15, x, Inches(2.0), Inches(3.7), Inches(4.8), WHITE, LINE_BORDER)
        tf = card.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_right = Inches(0.3)
        tf.margin_top = Inches(0.3)

        p = tf.paragraphs[0]
        p.text = f"PILLAR {i+1}"
        p.font.name = "Calibri"
        p.font.size = Pt(11)
        p.font.bold = True
        p.font.color.rgb = col_acc

        p = tf.add_paragraph()
        p.text = title_t
        p.font.name = "Calibri"
        p.font.size = Pt(16)
        p.font.bold = True
        p.font.color.rgb = NAVY
        p.space_before = Pt(8)

        p = tf.add_paragraph()
        p.text = desc_t
        p.font.name = "Calibri"
        p.font.size = Pt(12)
        p.font.color.rgb = SLATE
        p.space_before = Pt(14)

    # ==========================================
    # SLIDE 16: METHODOLOGY OVERVIEW (FUNNEL LIFECYCLE EMBEDDED)
    # ==========================================
    s16 = prs.slides.add_slide(blank_layout)
    add_header(s16, "Methodological Architecture", "Research Methodology Overview", "Structured 5-Part Graduate Methodology Architecture (ERAU Standards)")

    flow_steps = [
        ("3.1", "Approach", "Comparative evaluation of 4 paradigms across 3 pillars."),
        ("3.2", "Sample", "4-tier filtering isolating 9 airports & 12 complexes."),
        ("3.3", "Data Sources", "67.2M raw → 42.1M conformed federal records."),
        ("3.4", "Validity", "DB1B connecting deflator & carrier lane isolation."),
        ("3.5", "Treatment", "Star Schema warehouse & 168-hr purge buffer.")
    ]
    add_smart_process(s16, Inches(1.8), flow_steps, width=Inches(11.7), height=Inches(1.1))

    # Embed Combined Data Pipeline & Funnel Figure
    add_image_safe(s16, "figures/Combined_Data_Pipeline_and_Funnel_Lifecycle.png", Inches(2.8), Inches(3.1), height=Inches(4.0))

    # ==========================================
    # SLIDE 17: METHODOLOGY APPROACH (FIGURE 3.1 EMBEDDED)
    # ==========================================
    s17 = prs.slides.add_slide(blank_layout)
    add_header(s17, "Methodology Approach", "Forecasting Model Families & Taxonomy", "Figure 3.1: Comparative Architectural Taxonomy of Evaluated Predictive Paradigms")

    add_image_safe(s17, "figures/figure_3_1_forecasting_model_families.png", Inches(1.0), Inches(1.8), width=Inches(11.333))

    for i, (m_id, m_name, m_role) in enumerate([
        ("Baseline Control", "Daily Persistence", "Non-parametric diurnal persistence control; establishes MASE ≡ 1.000."),
        ("Model 1", "Deterministic Schedule", "ACRP Report 40 lognormal show-up convolution across flight banks."),
        ("Model 2", "Supervised ML", "Gradient-boosted decision trees incorporating 24 BTS operational features."),
        ("Model 3", "Dynamic Two-Stage Hybrid", "Coupling flight schedules with live prior-hour error feedback (e_{t-1}).")
    ]):
        x = Inches(0.8 + i * 3.0)
        card = add_card(s17, x, Inches(5.4), Inches(2.8), Inches(1.5), WHITE, LINE_BORDER)
        tf = card.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_right = Inches(0.15)
        tf.margin_top = Inches(0.1)
        p = tf.paragraphs[0]
        p.text = m_id
        p.font.name = "Calibri"
        p.font.size = Pt(11)
        p.font.bold = True
        p.font.color.rgb = BLUE_ACCENT
        p = tf.add_paragraph()
        p.text = m_name
        p.font.name = "Calibri"
        p.font.size = Pt(13)
        p.font.bold = True
        p.font.color.rgb = NAVY
        p.space_before = Pt(2)
        p = tf.add_paragraph()
        p.text = m_role
        p.font.name = "Calibri"
        p.font.size = Pt(9.5)
        p.font.color.rgb = SLATE
        p.space_before = Pt(2)

    # ==========================================
    # SLIDE 18: METHODOLOGY DESIGN AND PROCEDURES
    # ==========================================
    s18 = prs.slides.add_slide(blank_layout)
    add_header(s18, "Design & Procedure", "Four-Phase Research Execution Lifecycle", "Table 3.1: Systematic Progression from Federal Ingestion to Hypothesis Testing")

    phases_s18 = [
        ("PHASE 1", "Multi-Source Data Ingestion & ETL", "TSA FOIA, BTS OTP, T-100, DB1B", "Extract 67.2M raw records; conform into Star Schema warehouse (42.1M records). Preserved structural night zeros."),
        ("PHASE 2", "Econometric Funnel & Cohort Isolation", "4-Tier Purposive Filtering Funnel", "Filtered 450+ airports to Top 25, screened legacy carrier presence, isolated dedicated carrier terminals (9 airfields, 12 complexes)."),
        ("PHASE 3", "Model Calibration & Feature Engineering", "Feature Pipeline & 84-Cell Grid", "Constructed 24 OTP features; convolved ACRP 40 curves; verified 98.8% sample sufficiency across 84-cell interaction grid."),
        ("PHASE 4", "Multi-Pillar Hypothesis Evaluation", "Out-of-Time 2025 Holdout Benchmark", "Tested models across Robustness (nominal), Resilience (convective storms), and Generalizability using Diebold-Mariano tests.")
    ]
    for i, (p_tag, p_name, p_sub, p_desc) in enumerate(phases_s18):
        x = Inches(0.8 + i * 3.0)
        card = add_card(s18, x, Inches(2.0), Inches(2.8), Inches(4.8), WHITE, LINE_BORDER)
        tf = card.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_right = Inches(0.2)
        tf.margin_top = Inches(0.25)
        p = tf.paragraphs[0]
        p.text = p_tag
        p.font.name = "Calibri"
        p.font.size = Pt(11)
        p.font.bold = True
        p.font.color.rgb = BLUE_ACCENT
        p = tf.add_paragraph()
        p.text = p_name
        p.font.name = "Calibri"
        p.font.size = Pt(15)
        p.font.bold = True
        p.font.color.rgb = NAVY
        p.space_before = Pt(4)
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
        p.font.size = Pt(11)
        p.font.color.rgb = SLATE
        p.space_before = Pt(8)

    # ==========================================
    # SLIDE 19: METHODOLOGY DETAILS (VALIDITY SAFEGUARDS)
    # ==========================================
    s19 = prs.slides.add_slide(blank_layout)
    add_header(s19, "Validity Safeguards", "Methodological Safeguards & Data Integrity", "Strict Prevention of Autoregressive Data Leakage and Unconfounded Isolation")

    safeguards_s19 = [
        ("The 7-Day Purge Buffer", "Table 4.8 / REC-06", "168-hour zero-training purge buffer established between training (2022–2024) and test holdout (2025). Completely prevents autoregressive memory leakage across dataset boundaries."),
        ("Connecting Passenger Deflator", "DB1B Coupon Deflation", "Deflates departing aircraft seats by true connecting ratios (S_connect up to 66.3% at DFW). Solves the Hub Disconnect where airside connections bypass TSA."),
        ("Carrier Checkpoint Isolation", "Dedicated Carrier Complexes", "Isolates screening checkpoints operated exclusively by American, Delta, or United, eliminating multi-carrier unidentifiable passenger mixing."),
        ("Strict Information Causality", "t-1 Realized Telemetry", "Models only ingest strictly prior-hour features (t-1) available in real-time operations, ensuring zero forward-looking lookahead bias.")
    ]
    for i, (title_t, sub_t, desc_t) in enumerate(safeguards_s19):
        col = i % 2
        row = i // 2
        x = Inches(0.8 + col * 6.0)
        y = Inches(2.0 + row * 2.5)
        card = add_card(s19, x, y, Inches(5.7), Inches(2.3), WHITE, LINE_BORDER)
        tf = card.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_right = Inches(0.3)
        tf.margin_top = Inches(0.2)
        p = tf.paragraphs[0]
        p.text = title_t
        p.font.name = "Calibri"
        p.font.size = Pt(15)
        p.font.bold = True
        p.font.color.rgb = NAVY
        p = tf.add_paragraph()
        p.text = sub_t.upper()
        p.font.name = "Calibri"
        p.font.size = Pt(11)
        p.font.bold = True
        p.font.color.rgb = BLUE_ACCENT
        p.space_before = Pt(2)
        p = tf.add_paragraph()
        p.text = desc_t
        p.font.name = "Calibri"
        p.font.size = Pt(11.5)
        p.font.color.rgb = SLATE
        p.space_before = Pt(4)

    # ==========================================
    # SLIDE 20: FINDINGS ROADMAP
    # ==========================================
    s20 = prs.slides.add_slide(blank_layout)
    add_header(s20, "Results Roadmap", "Chapter IV Empirical Results Architecture", "Four Sequential Analyses Supporting Multi-Pillar Hypothesis Testing")

    findings_s20 = [
        ("4.1 Exploratory Analysis", "Top 25 Census & The Values vs. Volatility Discovery", "Analyzing 42.1M records; proving static volumes mask queuing while volatility metrics correlate tightly with flight delays."),
        ("4.2 Data Filtering & Cohort", "Four-Tier Purposive Filtering Pipeline", "Progression from 450+ airports to the 9-airport factorial cohort across 12 carrier-exclusive screening environments."),
        ("4.3 Model Execution", "Holdout Benchmark Matrix Across 4 Paradigms", "2025 out-of-time evaluation across Baseline Control, Model 1, Model 2, and Model 3; certified RMSE, MASE, and Bias."),
        ("4.4 Multi-Pillar Hypothesis", "Testing H₁ Across Robustness, Resilience, Transfer", "Deep-dive evaluations under nominal operations, convective IROPS shocks, and zero-shot cross-facility portability.")
    ]
    for i, (step_t, title_t, desc_t) in enumerate(findings_s20):
        y = Inches(1.8 + i * 1.25)
        card = add_card(s20, Inches(0.8), y, Inches(11.7), Inches(1.1), WHITE, LINE_BORDER)
        tf = card.text_frame
        tf.word_wrap = True
        tf.margin_left = Inches(0.3)
        tf.margin_top = Inches(0.15)
        p = tf.paragraphs[0]
        p.text = step_t.upper()
        p.font.name = "Calibri"
        p.font.size = Pt(10)
        p.font.bold = True
        p.font.color.rgb = BLUE_ACCENT
        p = tf.add_paragraph()
        p.text = title_t
        p.font.name = "Calibri"
        p.font.size = Pt(14)
        p.font.bold = True
        p.font.color.rgb = NAVY
        p.space_before = Pt(2)
        p = tf.add_paragraph()
        p.text = desc_t
        p.font.name = "Calibri"
        p.font.size = Pt(11)
        p.font.color.rgb = SLATE
        p.space_before = Pt(2)

    # ==========================================
    # SLIDE 21: DESCRIPTIVE STATISTICS: TOP 25 VS 9-AIRPORT COHORT (POWER OF 9 AIRPORTS EMBEDDED)
    # ==========================================
    s21 = prs.slides.add_slide(blank_layout)
    add_header(s21, "Descriptive Statistics", "Empirical Baseline: 9-Airport Cohort vs. Top 25", "Table 4.7: Proving the Experimental Cohort Represents the Operational Stress Front")

    cohort_stats_s21 = [
        ("+16.9%", "Flight Movement Density", "224,576 annual flights vs. 192,160 national Top 25 average"),
        ("+14.1%", "Higher Cancellation Rate", "1.63% flight cancellation rate vs. 1.43% national Top 25 average"),
        ("+25.0%", "Local Originating Demand", "16.4M true originating passengers vs. 13.1M national Top 25 average"),
        ("+5.8%", "Elevated Arrival Volatility", "CV_TSA = 0.8728 vs. 0.8250 national Top 25 baseline average")
    ]
    for i, (num_s, lab_s, desc_s) in enumerate(cohort_stats_s21):
        x = Inches(0.8 + i * 3.0)
        card = add_card(s21, x, Inches(1.8), Inches(2.8), Inches(2.4), WHITE, LINE_BORDER)
        tf = card.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_right = Inches(0.2)
        tf.margin_top = Inches(0.2)
        p = tf.paragraphs[0]
        p.text = num_s
        p.font.name = "Calibri"
        p.font.size = Pt(28)
        p.font.bold = True
        p.font.color.rgb = NAVY
        p.alignment = PP_ALIGN.CENTER
        p = tf.add_paragraph()
        p.text = lab_s
        p.font.name = "Calibri"
        p.font.size = Pt(12)
        p.font.bold = True
        p.font.color.rgb = BLUE_ACCENT
        p.alignment = PP_ALIGN.CENTER
        p.space_before = Pt(4)
        p = tf.add_paragraph()
        p.text = desc_s
        p.font.name = "Calibri"
        p.font.size = Pt(10)
        p.font.color.rgb = SLATE
        p.alignment = PP_ALIGN.CENTER
        p.space_before = Pt(4)

    # Embed Power of 9 Airports Figure
    add_image_safe(s21, "figures/Power of 9 airports.png", Inches(3.2), Inches(4.4), height=Inches(2.6))

    # ==========================================
    # SLIDE 22: DATA FILTERING & 4-TIER PIPELINE
    # ==========================================
    s22 = prs.slides.add_slide(blank_layout)
    add_header(s22, "Cohort Selection", "The Four-Tier Purposive Filtering Pipeline", "Table 3.2: Progressive Filtering from 450+ Commercial Airfields to 9 Balanced Hubs")

    tiers_s22 = [
        ("Macro Tier", "Commercial Scale", "450+  →  Top 25 Hubs", "Filtered commercial airfields to the Top 25 large hubs representing 68% of commercial traffic."),
        ("Meso Tier", "Carrier Presence", "Top 25  →  14 Core Hubs", "Enforced continuous operations by American, Delta, United. Eliminated JFK due to United's exit."),
        ("Micro Tier", "Checkpoint Isolation", "14  →  10 Airfields", "Screened for dedicated carrier checkpoints. Eliminated consolidated checkpoints (e.g. Salt Lake City)."),
        ("Cohort Tier", "Operational Balance", "10  →  9 Final Airfields", "Balanced across 4 operational clusters and 12 dedicated carrier-exclusive screening complexes.")
    ]
    for i, (t_name, t_sub, t_flow, t_desc) in enumerate(tiers_s22):
        x = Inches(0.8 + i * 3.0)
        card = add_card(s22, x, Inches(2.0), Inches(2.8), Inches(4.8), WHITE, LINE_BORDER)
        tf = card.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_right = Inches(0.2)
        tf.margin_top = Inches(0.2)
        p = tf.paragraphs[0]
        p.text = t_name.upper()
        p.font.name = "Calibri"
        p.font.size = Pt(11)
        p.font.bold = True
        p.font.color.rgb = BLUE_ACCENT
        p = tf.add_paragraph()
        p.text = t_sub
        p.font.name = "Calibri"
        p.font.size = Pt(15)
        p.font.bold = True
        p.font.color.rgb = NAVY
        p.space_before = Pt(3)
        p = tf.add_paragraph()
        p.text = t_flow
        p.font.name = "Calibri"
        p.font.size = Pt(11)
        p.font.bold = True
        p.font.color.rgb = GREEN
        p.space_before = Pt(6)
        p = tf.add_paragraph()
        p.text = t_desc
        p.font.name = "Calibri"
        p.font.size = Pt(11)
        p.font.color.rgb = SLATE
        p.space_before = Pt(8)

    # ==========================================
    # SLIDE 23: PIPELINE RESULTS: 9 AIRPORTS & 12 COMPLEXES (AIRPORT CLUSTERS EMBEDDED)
    # ==========================================
    s23 = prs.slides.add_slide(blank_layout)
    add_header(s23, "Cohort Specification", "The 9-Airport Experimental Cohort Specification", "Table 4.6: Factorial Representation Across 12 Carrier-Exclusive Terminal Complexes")

    # Embed Airport Clusters Figure
    add_image_safe(s23, "figures/airport clusters.png", Inches(0.8), Inches(1.8), width=Inches(6.0))

    airports_list = [
        ("ATL", "Atlanta Hartsfield", "Delta Domestic South"),
        ("BOS", "Boston Logan", "Delta A / American B"),
        ("DFW", "Dallas/Fort Worth", "American A, B, C"),
        ("DTW", "Detroit Metro", "Delta McNamara"),
        ("EWR", "Newark Liberty", "United Terminal C"),
        ("LAX", "Los Angeles Intl", "Delta 3 / AA 4 / United 7"),
        ("LGA", "New York LaGuardia", "Delta Terminal C (New)"),
        ("ORD", "Chicago O'Hare", "United T1 / American T3"),
        ("PHL", "Philadelphia Intl", "American Terminals B/C")
    ]
    for i, (code, name, term) in enumerate(airports_list):
        col = i % 2
        row = i // 2
        x = Inches(7.1 + col * 2.8)
        y = Inches(1.8 + row * 1.0)
        card = add_card(s23, x, y, Inches(2.6), Inches(0.9), WHITE, LINE_BORDER)
        tf = card.text_frame
        tf.word_wrap = True
        tf.margin_left = Inches(0.15)
        tf.margin_top = Inches(0.08)
        p = tf.paragraphs[0]
        p.text = f"{code}  ·  {name}"
        p.font.name = "Calibri"
        p.font.size = Pt(11)
        p.font.bold = True
        p.font.color.rgb = NAVY
        p = tf.add_paragraph()
        p.text = term
        p.font.name = "Calibri"
        p.font.size = Pt(9.5)
        p.font.color.rgb = SLATE
        p.space_before = Pt(1)

    # ==========================================
    # SLIDE 24: ANNUAL SEASONS & VOLATILITY REGIMES (FIGURE 4.2 EMBEDDED)
    # ==========================================
    s24 = prs.slides.add_slide(blank_layout)
    add_header(s24, "Macro Regimes", "Annual Seasonal Volatility Regimes", "Figure 4.2: Macro Seasonality Clustering Across the 52 Calendar Weeks")

    add_image_safe(s24, "figures/figure_4_2_annual_volatility_clusters.png", Inches(0.8), Inches(1.8), width=Inches(11.7))

    # ==========================================
    # SLIDE 25: DAY-OF-WEEK & DIURNAL DYNAMICS (FIGURE 4.3 & 4.4 EMBEDDED)
    # ==========================================
    s25 = prs.slides.add_slide(blank_layout)
    add_header(s25, "Diurnal & DOW Cycles", "Day-of-Week Volatility & Bimodal Diurnal Peaks", "Figure 4.3 & 4.4: Monday Business Outbound vs. Sunday Inbound Delays")

    add_image_safe(s25, "figures/figure_4_3_day_of_week_volatility_dynamics.png", Inches(0.8), Inches(1.8), width=Inches(5.6))
    add_image_safe(s25, "figures/figure_4_4_diurnal_hourly_volatility_clusters.png", Inches(6.8), Inches(1.8), width=Inches(5.7))

    # ==========================================
    # SLIDE 26: EMPIRICAL PASSENGER SHOW-UP CONVOLUTION (FIGURE 4.5 EMBEDDED)
    # ==========================================
    s26 = prs.slides.add_slide(blank_layout)
    add_header(s26, "Lead-Lag Dynamics", "Empirical Passenger Show-Up Curve Convolution", "Figure 4.5: Why Lead-2 (t+2) Captures 53.5% of Arrival Variance vs. Contemporaneous Failure")

    add_image_safe(s26, "figures/figure_4_5_lead_lag_convolution_curves.png", Inches(0.8), Inches(1.8), width=Inches(6.2))

    add_centered_equation(
        s26, Inches(7.4), Inches(1.8), Inches(5.1), Inches(5.0),
        "Lead-Lag Asynchrony Proof",
        "R²(t+2) = 0.5347  vs.  R²(t) = 0.1982",
        "Key Empirical Findings:\n\n"
        "• Contemporaneous flight schedules (t) fail to predict screening arrivals (R² = 19.8%).\n\n"
        "• Passenger arrivals peak precisely at t+2 hours ahead of scheduled gate departure (R² = 53.5%).\n\n"
        "• Model 1 convolving empirical show-up curves over t+2 bridges this physical gap."
    )

    # ==========================================
    # SLIDE 27: 2025 HOLDOUT BENCHMARK MATRIX (FIGURE 4.6 EMBEDDED)
    # ==========================================
    s27 = prs.slides.add_slide(blank_layout)
    add_header(s27, "Model Benchmarks", "Certified 2025 Out-of-Time Holdout Benchmarks", "Table 4.10: Performance Hierarchy Across Candidate Modeling Paradigms")

    add_image_safe(s27, "figures/figure_4_6_master_model_benchmark_matrix.png", Inches(1.5), Inches(1.8), height=Inches(5.0))

    # ==========================================
    # SLIDE 28: MULTI-PILLAR HYPOTHESIS TESTING (FIGURE 5.4 DASHBOARD EMBEDDED)
    # ==========================================
    s28 = prs.slides.add_slide(blank_layout)
    add_header(s28, "Hypothesis Testing", "Multi-Pillar Hypothesis Evaluation: The Asymmetric Trade-Off", "Table 4.11: Proving H₁ Across Robustness, Resilience, and Generalizability")

    add_image_safe(s28, "figures/figure_5_4_master_hypothesis_trade_off_dashboard.png", Inches(1.5), Inches(1.8), height=Inches(5.0))

    # ==========================================
    # SLIDE 29: DIMENSION 2: RESILIENCE & SHOCK RECOVERY (FIGURE 5.2 EMBEDDED)
    # ==========================================
    s29 = prs.slides.add_slide(blank_layout)
    add_header(s29, "Deep-Dive Resilience", "Dimension 2: Disruption Resilience & Shock Recovery", "Figure 5.2: Overcoming the Empty Checkpoint Fallacy During Severe Convective Storms")

    add_image_safe(s29, "figures/figure_5_2_disruption_resilience_and_shock_recovery.png", Inches(0.8), Inches(1.8), width=Inches(6.2))

    add_centered_equation(
        s29, Inches(7.4), Inches(1.8), Inches(5.1), Inches(5.0),
        "Resilience Disruption Multiplier",
        "R_MASE  =  MASE_shock / MASE_routine",
        "Disruption Performance:\n\n"
        "• Model 3 (Dynamic Hybrid): R_MASE = 1.05 (Resilient Winner; TTR = 2.8 hours).\n\n"
        "• Model 2 (Supervised ML): R_MASE = 2.14 (Fragile Collapse due to Empty Checkpoint Fallacy).\n\n"
        "• Model 1 (Deterministic): R_MASE = 1.32 (Blind to delays; TTR = 7.8 hours)."
    )

    # ==========================================
    # SLIDE 30: DIMENSION 3: GENERALIZABILITY & SPATIAL TRANSFER (FIGURE 5.3 EMBEDDED)
    # ==========================================
    s30 = prs.slides.add_slide(blank_layout)
    add_header(s30, "Deep-Dive Generalizability", "Dimension 3: Generalizability & Spatial Transfer", "Figure 5.3: Zero-Shot Transferability from Newark (EWR) to LaGuardia (LGA)")

    add_image_safe(s30, "figures/figure_5_3_generalizability_and_spatial_transfer.png", Inches(0.8), Inches(1.8), width=Inches(6.2))

    add_centered_equation(
        s30, Inches(7.4), Inches(1.8), Inches(5.1), Inches(5.0),
        "Relative Transfer Ratio",
        "RTR  =  RMSE_transfer / RMSE_in-sample",
        "Spatial Transfer Performance:\n\n"
        "• Model 1 (Deterministic): RTR = 1.04, ΔMASE = +4.0% (Target Met; Transfer Winner).\n\n"
        "• Model 2 (Supervised ML): RTR = 1.08, ΔMASE = +8.3% (Passes Target).\n\n"
        "• Model 3 (Dynamic Hybrid): RTR = 1.19, ΔMASE = +21.5% (Fails Target due to layout overfitting)."
    )

    # ==========================================
    # SLIDE 31: OPERATIONAL IMPLEMENTATION (THE OPERATOR'S PLAYBOOK)
    # ==========================================
    s31 = prs.slides.add_slide(blank_layout)
    add_header(s31, "Operational Implementation", "Real-World Aviation Application: The Operator's Playbook", "Three Actionable Policy Recommendations for TSA and Airport Operations Centers")

    ops_s31 = [
        ("Dynamic Checkpoint Rostering", "Replace Static Tables with 2-Hr Lead Convolutions", "TSA Federal Security Directors should abandon static time-of-day tables. Deploy dynamic staffing rosters driven by t+2 scheduled flight bank convolutions convolved with conformal safety buffers."),
        ("Connecting Ratio Deflation", "Integrate Bureau of Transportation Statistics O&D Data", "Centralized security scheduling systems must dynamically deflate scheduled flight seats using airline O&D transfer ratios, preventing chronic over-staffing at connecting hub complexes."),
        ("The Regime-Switched Gated Engine", "Automated Operational Model Switching Architecture", "Deploy Model 2 (Supervised ML) during nominal on-time operations for zero-latency interpretable dispatch. Instantly switch to Model 3 (Dynamic Hybrid) when ground stop delays exceed 45 minutes.")
    ]
    for i, (title_t, sub_t, desc_t) in enumerate(ops_s31):
        y = Inches(1.8 + i * 1.65)
        card = add_card(s31, Inches(0.8), y, Inches(11.7), Inches(1.5), WHITE, LINE_BORDER)
        tf = card.text_frame
        tf.word_wrap = True
        tf.margin_left = Inches(0.3)
        tf.margin_top = Inches(0.15)
        p = tf.paragraphs[0]
        p.text = title_t
        p.font.name = "Calibri"
        p.font.size = Pt(14)
        p.font.bold = True
        p.font.color.rgb = NAVY
        p = tf.add_paragraph()
        p.text = sub_t.upper()
        p.font.name = "Calibri"
        p.font.size = Pt(11)
        p.font.bold = True
        p.font.color.rgb = BLUE_ACCENT
        p.space_before = Pt(2)
        p = tf.add_paragraph()
        p.text = desc_t
        p.font.name = "Calibri"
        p.font.size = Pt(11)
        p.font.color.rgb = SLATE
        p.space_before = Pt(3)

    # ==========================================
    # SLIDE 32: CONCLUSION
    # ==========================================
    s32 = prs.slides.add_slide(blank_layout)
    bar32 = s32.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(0.25))
    bar32.fill.solid()
    bar32.fill.fore_color.rgb = NAVY
    bar32.line.fill.background()

    card32 = add_card(s32, Inches(1.2), Inches(1.5), Inches(10.9), Inches(5.2), WHITE, LINE_BORDER)
    tf = card32.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_right = Inches(0.5)
    tf.margin_top = Inches(0.4)

    p = tf.paragraphs[0]
    p.text = "RESEARCH SYNTHESIS & CONCLUDING TAKEAWAY"
    p.font.name = "Calibri"
    p.font.size = Pt(12)
    p.font.bold = True
    p.font.color.rgb = BLUE_ACCENT
    p.alignment = PP_ALIGN.CENTER

    p = tf.add_paragraph()
    p.text = "Transforming Airport Security from Reactive Firefighting\nto Resilient Stochastic Synchronization"
    p.font.name = "Calibri"
    p.font.size = Pt(26)
    p.font.bold = True
    p.font.color.rgb = NAVY
    p.alignment = PP_ALIGN.CENTER
    p.space_before = Pt(8)
    p.space_after = Pt(14)

    concl_takeaways = [
        "1. Volatility Governs Heavy Traffic: Under Kingman's law, arrival burstiness (Ca²) causes queue delay explosions, proving static headcounts are fundamentally insufficient.",
        "2. The Asymmetric Trade-Off (H1): Model 1 wins zero-shot transferability; Model 2 wins routine Pareto efficiency; Model 3 wins shock resilience during severe convective storms.",
        "3. Defeating the Empty Checkpoint Fallacy: Dynamic error innovation feedback rescues machine learning from storm-induced lobby under-staffing.",
        "4. Operational Viability: Implementing the Regime-Switched Gated Engine delivers mathematically proven resilience without sacrificing routine operational efficiency."
    ]
    for t in concl_takeaways:
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
    p.font.color.rgb = BLUE_ACCENT
    p.alignment = PP_ALIGN.CENTER
    p.space_before = Pt(18)

    prs.save(output_path)
    print(f"Successfully generated visual minimalist deck at: {output_path}")

if __name__ == "__main__":
    out = "/Users/leilagleich/Library/CloudStorage/OneDrive-Embry-RiddleAeronauticalUniversity/final-thesis/Recommended-Thesis-Defense-Deck.pptx"
    create_deck(out)
