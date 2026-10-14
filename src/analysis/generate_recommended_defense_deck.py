"""
generate_recommended_defense_deck.py
Author: Leila Gleich
Degree: Master of Science in Aeronautics (MSAA / Gleich 700B)
Institution: Embry-Riddle Aeronautical University

Generates Recommended-Thesis-Defense-Deck.pptx strictly adhering to:
- Executive design philosophy: Clean, visual, spacious, high contrast (like thesis-defense-outline)
- Real rendered mathematical formulas (Matplotlib 300 DPI LaTeX typography)
- Prominent research figures from figures/
- Concise, high-impact bullet points (no wall-of-text boxes)
- 16:9 Widescreen (13.333" x 7.5")
- Exact 32-slide alignment with DEFENSE_PRESENTATION_SCRIPT_25MIN.md
"""

import os
import shutil
from PIL import Image
import matplotlib.pyplot as plt

from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE

BASE_DIR = "/Users/leilagleich/Library/CloudStorage/OneDrive-Embry-RiddleAeronauticalUniversity/final-thesis"
OUTPUT_PATH = os.path.join(BASE_DIR, "Recommended-Thesis-Defense-Deck.pptx")
MIRROR_PATH = os.path.join(BASE_DIR, "master-docs", "Recommended-Thesis-Defense-Deck.pptx")
PKG_MIRROR_PATH = os.path.join(BASE_DIR, "thesis_final_package", "defense", "Recommended-Thesis-Defense-Deck.pptx")

# Palette
NAVY = RGBColor(10, 34, 64)          # Primary ERAU Navy (#0A2240)
BLUE_ACCENT = RGBColor(37, 99, 235)  # Aviation Blue (#2563EB)
SLATE = RGBColor(71, 85, 105)        # Slate Grey (#475569)
DARK_TEXT = RGBColor(15, 23, 42)     # Body Charcoal (#0F172A)
MUTED_TEXT = RGBColor(100, 116, 139) # Secondary Muted Grey (#64748B)
SOFT_BG = RGBColor(248, 250, 252)    # Subtle Card Fill (#F8FAFC)
LINE_BORDER = RGBColor(226, 232, 240)# Hairline Border (#E2E8F0)
WHITE = RGBColor(255, 255, 255)      # Pure White
GREEN = RGBColor(22, 101, 52)        # Dark Green (#166534)
AMBER = RGBColor(180, 83, 9)         # Dark Amber (#B45309)


def render_all_formulas():
    """Renders all required mathematical formulas into high-DPI LaTeX formula PNGs."""
    formula_dir = os.path.join(BASE_DIR, "figures", "rendered_formulas")
    os.makedirs(formula_dir, exist_ok=True)

    formulas = {
        'formula_kingman.png': r'\bar{W}_q \approx \left(\frac{\rho}{1 - \rho}\right) \cdot \left(\frac{C_a^2 + C_s^2}{2}\right) \cdot \left(\frac{1}{\mu}\right)',
        'formula_cv_tsa.png': r'CV_{\mathrm{TSA}} = \frac{\sigma_{\mathrm{TSA}}}{\mu_{\mathrm{TSA}}}',
        'formula_showup_convolution.png': r'\hat{Y}_t = \sum_{i} \left[ \mathrm{Seats}_i \cdot (1 - S_{\mathrm{connect}}) \cdot P(t - \mathrm{DEP}_i) \right]',
        'formula_two_stage_hybrid.png': r'\hat{Y}_t = M_{\mathrm{base}}(\mathrm{Schedule}_t, \mathbf{X}_t) + \alpha \cdot (Y_{t-1} - \hat{Y}_{t-1})',
        'formula_baseline_persistence.png': r'\hat{Y}_t = Y_{t-24} \quad (\mathrm{MASE} \equiv 1.000)',
        'formula_lead_lag.png': r'R^2(t+2) = 0.5347 \quad \text{vs.} \quad R^2(t) = 0.1982',
        'formula_r_mase.png': r'R_{\mathrm{MASE}} = \frac{\mathrm{MASE}_{\mathrm{shock}}}{\mathrm{MASE}_{\mathrm{routine}}}',
        'formula_rtr.png': r'\mathrm{RTR} = \frac{\mathrm{RMSE}_{\mathrm{transfer}}}{\mathrm{RMSE}_{\mathrm{in\text{-}sample}}}'
    }

    rendered_paths = {}
    for fname, eq in formulas.items():
        fig, ax = plt.subplots(figsize=(6.5, 1.1), dpi=300)
        ax.text(0.5, 0.5, f"${eq}$", fontsize=17, ha='center', va='center', color='#0A2240')
        ax.axis('off')
        path = os.path.join(formula_dir, fname)
        fig.savefig(path, bbox_inches='tight', transparent=True, pad_inches=0.04)
        plt.close(fig)
        rendered_paths[fname] = path
    return rendered_paths


def create_deck():
    rendered_formulas = render_all_formulas()

    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    def add_header(slide, tracker, title, subtitle=None):
        """Standard slide header: tracker kicker, title, and optional subtitle."""
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
        p1.font.size = Pt(24)
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

    def add_fitted_image(slide, rel_or_abs_path, left, top, max_w, max_h):
        """Adds an image preserving aspect ratio centered inside bounding box (left, top, max_w, max_h)."""
        full_path = rel_or_abs_path if os.path.isabs(rel_or_abs_path) else os.path.join(BASE_DIR, rel_or_abs_path)
        if not os.path.exists(full_path):
            print(f"Warning: image not found: {full_path}")
            return None
        with Image.open(full_path) as im:
            orig_w, orig_h = im.size

        aspect = orig_w / orig_h
        target_aspect = max_w / max_h

        if aspect > target_aspect:
            # Width limited
            fit_w = max_w
            fit_h = max_w / aspect
            fit_left = left
            fit_top = top + (max_h - fit_h) / 2
        else:
            # Height limited
            fit_h = max_h
            fit_w = max_h * aspect
            fit_top = top
            fit_left = left + (max_w - fit_w) / 2

        return slide.shapes.add_picture(full_path, fit_left, fit_top, width=fit_w, height=fit_h)

    def add_bullet_list(slide, left, top, width, height, bullet_items):
        """Adds clean, spacious bullet points with bold title and regular text."""
        tb = slide.shapes.add_textbox(left, top, width, height)
        tf = tb.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0

        for i, (title, text) in enumerate(bullet_items):
            p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
            p.text = f"•  {title}: "
            p.font.name = "Calibri"
            p.font.size = Pt(13.5)
            p.font.bold = True
            p.font.color.rgb = NAVY
            if i > 0:
                p.space_before = Pt(10)

            run = p.add_run()
            run.text = text
            run.font.name = "Calibri"
            run.font.size = Pt(13)
            run.font.bold = False
            run.font.color.rgb = DARK_TEXT

    def add_card(slide, left, top, width, height, bg_color=SOFT_BG, border_color=LINE_BORDER):
        """Clean card with hairline border."""
        shape = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, left, top, width, height)
        shape.fill.solid()
        shape.fill.fore_color.rgb = bg_color
        shape.line.color.rgb = border_color
        shape.line.width = Pt(1)
        return shape

    # ==========================================================================
    # SLIDE 1: TITLE SLIDE
    # ==========================================================================
    s1 = prs.slides.add_slide(blank_layout)
    top_band = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(0.25))
    top_band.fill.solid()
    top_band.fill.fore_color.rgb = NAVY
    top_band.line.fill.background()

    tb = s1.shapes.add_textbox(Inches(1.0), Inches(1.8), Inches(11.333), Inches(4.8))
    tf = tb.text_frame
    tf.word_wrap = True

    p = tf.paragraphs[0]
    p.text = "EMBRY-RIDDLE AERONAUTICAL UNIVERSITY  |  GRADUATE THESIS DEFENSE"
    p.font.name = "Calibri"
    p.font.size = Pt(12)
    p.font.bold = True
    p.font.color.rgb = BLUE_ACCENT

    p = tf.add_paragraph()
    p.text = "Evaluating Predictive Techniques to Model\nStochastic Airport Passenger Flow"
    p.font.name = "Calibri"
    p.font.size = Pt(38)
    p.font.bold = True
    p.font.color.rgb = NAVY
    p.space_before = Pt(16)
    p.space_after = Pt(16)

    p = tf.add_paragraph()
    p.text = "An Evaluation of Multi-Pillar Performance Measures for TSA Throughput Volatility"
    p.font.name = "Calibri"
    p.font.size = Pt(16)
    p.font.color.rgb = SLATE

    p = tf.add_paragraph()
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

    roadmap_items = [
        ("01. Research Problem & Queuing Friction", "Kingman's heavy-traffic queuing formula, arrival burstiness (Ca²), and terminal capacity limits."),
        ("02. Evolution of Literature", "From static flight bank convolutions to micro-simulation, machine learning fragility, and dynamic hybrids."),
        ("03. Econometric Data Pipeline", "Star schema conformed data, 4-tier filtering, carrier isolation, and 168-hour purge buffer."),
        ("04. Empirical Volatility Regimes", "The Values vs. Volatility decoupling, macro seasonality, and diurnal asynchrony."),
        ("05. Holdout Benchmarks & Testing", "Certified 2025 out-of-time evaluation across Robustness, Resilience, and Generalizability."),
        ("06. Operational Playbook & Synthesis", "Dynamic checkpoint rostering, connecting deflator, and regime-switched gated inference engine.")
    ]
    add_bullet_list(s2, Inches(1.2), Inches(1.85), Inches(10.9), Inches(5.0), roadmap_items)

    # ==========================================================================
    # SLIDE 3: THE TERMINAL QUEUING PROBLEM (KINGMAN'S APPROXIMATION)
    # ==========================================================================
    s3 = prs.slides.add_slide(blank_layout)
    add_header(s3, "Theoretical Foundation", "The Terminal Queuing Problem", "Why Heavy-Traffic Checkpoints Fail Under Static Capacity Assumptions")

    # Rendered Formula above left bullets
    add_fitted_image(s3, rendered_formulas['formula_kingman.png'], Inches(0.8), Inches(1.8), Inches(5.2), Inches(1.0))

    kingman_bullets = [
        ("Inflexible Physical Capacity", "AIT screening lanes and certified TSO shifts cannot expand dynamically in real-time."),
        ("Quadratic Delay Scaling", "Under Kingman's formula, passenger waiting times scale quadratically with arrival volatility (Ca²) as utilization approaches saturation (ρ → 1.0)."),
        ("Static Staffing Fragility", "Historical headcount volume tables fail during airside delay cascades and convective ground stops."),
        ("Core Objective", "Airport screening checkpoints require volatility-aware stochastic forecasting.")
    ]
    add_bullet_list(s3, Inches(0.8), Inches(3.0), Inches(5.2), Inches(3.9), kingman_bullets)

    # Right figure: Terminal Queuing Friction
    add_fitted_image(s3, "figures/terminal_queuing_friction.jpg", Inches(6.3), Inches(1.8), Inches(6.2), Inches(5.0))

    # ==========================================================================
    # SLIDE 4: RESEARCH PURPOSE & OBJECTIVES
    # ==========================================================================
    s4 = prs.slides.add_slide(blank_layout)
    add_header(s4, "Research Formulation", "Research Purpose & Operational Objectives", "Pivoting from Static Headcounts to Stochastic Volatility Dynamics")

    obj_cards = [
        ("OBJECTIVE 01", "PIVOT TO VOLATILITY",
         "Shift the modeling target away from static hourly headcounts to throughput volatility: standard deviation (σ_TSA) and scale-free arrival burstiness (CV_TSA). Queuing theory dictates that arrival variance governs delay cascades."),
        ("OBJECTIVE 02", "MULTI-PARADIGM BENCHMARK",
         "Conduct a rigorous out-of-time evaluation benchmarking 3 candidate paradigms—Deterministic Schedules, Supervised Machine Learning, and Dynamic Hybrids—against an empirical daily persistence control."),
        ("OBJECTIVE 03", "CONTEXT-AWARE OPTIMALITY",
         "Prove that model superiority is strictly contingent upon operational priorities: routine accuracy (Robustness), storm shock recovery (Resilience), or zero-shot spatial transfer (Generalizability).")
    ]
    card_w = Inches(3.75)
    for i, (kicker, title, body) in enumerate(obj_cards):
        x = Inches(0.8) + i * Inches(3.99)
        c = add_card(s4, x, Inches(1.85), card_w, Inches(5.0), WHITE, LINE_BORDER)
        tf = c.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_right = Inches(0.3)
        tf.margin_top = Inches(0.35)

        p = tf.paragraphs[0]
        p.text = kicker
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

    # Top Quote Banner
    q_card = add_card(s5, Inches(0.8), Inches(1.85), Inches(11.733), Inches(1.8), SOFT_BG, LINE_BORDER)
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
    p.font.size = Pt(12.5)
    p.font.italic = True
    p.font.color.rgb = NAVY
    p.space_before = Pt(4)

    # Bottom 3 Priority Cards
    triad = [
        ("PRIORITY 1", "ROBUSTNESS", "Routine Daily Operations", "Delays < 15 min, 0 cancellations (FAA A14 reference benchmark). Focus is minimizing daily error (MASE < 0.700) with zero compute latency."),
        ("PRIORITY 2", "RESILIENCE", "Irregular Operations (IROPS)", "Convective storms, ground stops, delays ≥ 45 min, cancellations ≥ 5. Focus is shock recovery multiplier (R_MASE ≈ 1.00) and TTR < 4.0h."),
        ("PRIORITY 3", "GENERALIZABILITY", "Zero-Shot Spatial Transfer", "Concourse portability without local retraining (EWR → LGA). Focus is transfer ratio (RTR ≤ 1.05) and ΔMASE ≤ 10.0%.")
    ]
    for i, (kicker, title, sub, desc) in enumerate(triad):
        x = Inches(0.8) + i * Inches(3.99)
        c = add_card(s5, x, Inches(3.95), card_w, Inches(2.9), WHITE, LINE_BORDER)
        tf = c.text_frame
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
        p.font.size = Pt(10.5)
        p.font.color.rgb = DARK_TEXT
        p.space_before = Pt(6)

    # ==========================================================================
    # SLIDE 6: MASTER HYPOTHESIS: THE ASYMMETRIC TRADE-OFF (H1)
    # ==========================================================================
    s6 = prs.slides.add_slide(blank_layout)
    add_header(s6, "Theoretical Formulation", "Hypothesis: The Asymmetric Trade-Off (H₁)", "Proving that Model Superiority is Inherently Context-Dependent")

    h1_card = add_card(s6, Inches(0.8), Inches(1.85), Inches(11.733), Inches(1.15), NAVY, NAVY)
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
    p.font.size = Pt(13.5)
    p.font.color.rgb = WHITE
    p.space_before = Pt(2)

    subs = [
        ("H1a", "ROBUSTNESS HYPOTHESIS", "Machine Learning & Hybrids Win Routine Flow",
         "Under nominal conditions (delays < 15m), Supervised ML (Model 2) and Dynamic Hybrid (Model 3) achieve MASE < 0.700. Deterministic flight schedules fail to meet the target due to rigid capacity assumptions."),
        ("H1b", "RESILIENCE HYPOTHESIS", "Dynamic Hybrid is Sole Resilient Winner",
         "Under convective IROPS shocks (delays ≥ 45m), Dynamic Hybrid (Model 3) maintains shock stability (R_MASE ≈ 1.05). Supervised ML collapses (R = 2.14) due to the Empty Checkpoint Fallacy."),
        ("H1c", "GENERALIZABILITY HYPOTHESIS", "Deterministic Schedules Win Spatial Transfer",
         "Under zero-shot concourse transfer (EWR → LGA), Deterministic Schedule (Model 1) achieves ΔMASE ≤ 10%. Dynamic Hybrids fail (ΔMASE = +21.5%) due to decision tree terminal geometry overfitting.")
    ]
    for i, (tag, title, sub, desc) in enumerate(subs):
        x = Inches(0.8) + i * Inches(3.99)
        c = add_card(s6, x, Inches(3.3), card_w, Inches(3.55), WHITE, LINE_BORDER)
        tf = c.text_frame
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

    p7_bullets = [
        ("The Aggregate Error Trap", "Standard evaluations pool all 8,760 hours of the year into a single RMSE. Aggregate error is 90% dominated by calm, routine hours."),
        ("Robustness Pillar", "Target: MASE < 0.700. Evaluates accuracy under calm conditions (delays < 15m) with zero feedback latency."),
        ("Resilience Pillar", "Target: R_MASE ≈ 1.00 & TTR < 4.0h. Evaluates stability under severe convective storm ground stops."),
        ("Generalizability Pillar", "Target: RTR ≤ 1.05 & ΔMASE ≤ 10.0%. Evaluates zero-shot concourse transferability without local retraining.")
    ]
    add_bullet_list(s7, Inches(0.8), Inches(1.85), Inches(5.2), Inches(5.0), p7_bullets)
    add_fitted_image(s7, "figures/figure_5_1_asymmetric_trade_off_triangle.png", Inches(6.3), Inches(1.85), Inches(6.2), Inches(5.0))

    # ==========================================================================
    # SLIDE 8: EVOLUTION OF TERMINAL FLOW LITERATURE
    # ==========================================================================
    s8 = prs.slides.add_slide(blank_layout)
    add_header(s8, "Theoretical Evolution", "Evolution of Terminal Flow Literature", "From Static Flight Bank Convolutions to Dynamic Error Feedback")

    p8_bullets = [
        ("1990s Deterministic Schedules", "Convolving flight banks across empirical show-up curves (ACRP Report 40). Transparent, but blind to flight delays."),
        ("2000s Micro-Simulation", "Agent-based simulation (Simio, CAST). High spatial detail, but 20–45 minute runtimes prohibit tactical lane dispatch."),
        ("2015+ Supervised ML", "Gradient-boosted decision trees. Outstanding routine accuracy, but collapses during convective IROPS shocks."),
        ("Today Dynamic Hybrids", "Two-stage sequential models coupling macro flight schedules with live screening floor error innovation feedback.")
    ]
    add_bullet_list(s8, Inches(0.8), Inches(1.85), Inches(5.2), Inches(5.0), p8_bullets)
    add_fitted_image(s8, "figures/models and tests.png", Inches(6.3), Inches(1.85), Inches(6.2), Inches(5.0))

    # ==========================================================================
    # SLIDE 9: LITERATURE GAP: VOLATILITY VS. VOLUME
    # ==========================================================================
    s9 = prs.slides.add_slide(blank_layout)
    add_header(s9, "Literature Gap", "The Static Fallacy in Terminal Modeling", "Why Static Passenger Volumes Fail to Explain Checkpoint Delays")

    # Rendered Formula
    add_fitted_image(s9, rendered_formulas['formula_cv_tsa.png'], Inches(0.8), Inches(1.8), Inches(5.2), Inches(1.0))

    p9_bullets = [
        ("Scale-Free Burstiness", "CV_TSA normalizes arrival dispersion across small vs. mega checkpoints, capturing queue-generating surges."),
        ("Static Volume Fails", "Passenger Headcount vs. Flight Delays: r = -0.062, p = 0.77 (R² = 2.5%). Complete failure to correlate!"),
        ("Volatility Couplings", "Throughput Volatility vs. Delay Volatility: r = +0.4373, p < 0.05 (R² = 19.1%). Strong operational coupling!"),
        ("Queuing Theory Rule", "Kingman's approximation dictates that arrival variance, not static volume, causes checkpoint queue buildup.")
    ]
    add_bullet_list(s9, Inches(0.8), Inches(3.0), Inches(5.2), Inches(3.9), p9_bullets)
    add_fitted_image(s9, "figures/OTP volatility.png", Inches(6.3), Inches(1.85), Inches(6.2), Inches(5.0))

    # ==========================================================================
    # SLIDE 10: DETERMINISTIC FLIGHT SCHEDULES (MODEL 1)
    # ==========================================================================
    s10 = prs.slides.add_slide(blank_layout)
    add_header(s10, "Literature Breakdown", "Deterministic Flight Schedules & Classical Queueing", "Model 1: Convolving Scheduled Airline Banks Across Empirical Show-Up Curves")

    add_fitted_image(s10, rendered_formulas['formula_showup_convolution.png'], Inches(0.8), Inches(1.8), Inches(5.2), Inches(1.0))

    p10_bullets = [
        ("Empirical Show-Up Convolution", "Convolves scheduled flight seats deflated by connecting share (1 - S_connect) over ACRP Report 40 curves."),
        ("Zero-Shot Concourse Invariance", "Human passenger arrival psychology transfers across airports without requiring local model training."),
        ("Complete Transparency", "100% interpretable; airport operators can trace every forecast directly to airline flight schedules."),
        ("Blindness to Delays (Fatal Flaw)", "Fails to incorporate real-time airside telemetry; forecasts passengers that cleared screening hours earlier.")
    ]
    add_bullet_list(s10, Inches(0.8), Inches(3.0), Inches(5.2), Inches(3.9), p10_bullets)
    add_fitted_image(s10, "figures/pax stochastic arrival.png", Inches(6.3), Inches(1.85), Inches(6.2), Inches(5.0))

    # ==========================================================================
    # SLIDE 11: SHIFT TO MICRO-SIMULATION MODELING
    # ==========================================================================
    s11 = prs.slides.add_slide(blank_layout)
    add_header(s11, "Literature Breakdown", "The Shift to Micro-Simulation Modeling", "High Spatial Resolution vs. Severe Real-Time Operational Latency")

    c11_pro = add_card(s11, Inches(0.8), Inches(1.85), Inches(5.7), Inches(5.0), WHITE, LINE_BORDER)
    tf = c11_pro.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_right = Inches(0.3)
    tf.margin_top = Inches(0.3)
    p = tf.paragraphs[0]
    p.text = "HIGH SPATIAL FIDELITY (ADVANTAGES)"
    p.font.bold = True
    p.font.size = Pt(11)
    p.font.color.rgb = GREEN

    sim_pros = [
        ("Granular Physical Paths", "Resolves individual passenger walking corridors, PreCheck vs. standard screening, and bag divestment."),
        ("Concourse Layout Sizing", "Accurately maps stanchion serpentine queues and bottleneck merging (Simio, CAST, ArcSTAR)."),
        ("Capital Planning Standard", "Indispensable for multi-million dollar terminal concourse expansions and checkpoint lane sizing.")
    ]
    for title, text in sim_pros:
        p = tf.add_paragraph()
        p.text = f"•  {title}: "
        p.font.bold = True
        p.font.size = Pt(11)
        p.font.color.rgb = NAVY
        p.space_before = Pt(10)
        run = p.add_run()
        run.text = text
        run.font.size = Pt(10.5)
        run.font.color.rgb = DARK_TEXT

    c11_con = add_card(s11, Inches(6.8), Inches(1.85), Inches(5.733), Inches(5.0), WHITE, LINE_BORDER)
    tf = c11_con.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_right = Inches(0.3)
    tf.margin_top = Inches(0.3)
    p = tf.paragraphs[0]
    p.text = "THE DISPATCH LATENCY BARRIER (DISADVANTAGES)"
    p.font.bold = True
    p.font.size = Pt(11)
    p.font.color.rgb = AMBER

    sim_cons = [
        ("20–45 Minute Compute Runtimes", "Full terminal simulations are far too slow for dynamic, tactical lane rebalancing within the operating hour."),
        ("Heavy Calibration Overhead", "Hundreds of micro-parameters (walking speeds, divestment rates) become obsolete during convective storms."),
        ("Unsuitable for Live Dispatch", "Cannot dynamically ingest real-time airside telemetry to adjust screening capacity during ground stops.")
    ]
    for title, text in sim_cons:
        p = tf.add_paragraph()
        p.text = f"•  {title}: "
        p.font.bold = True
        p.font.size = Pt(11)
        p.font.color.rgb = NAVY
        p.space_before = Pt(10)
        run = p.add_run()
        run.text = text
        run.font.size = Pt(10.5)
        run.font.color.rgb = DARK_TEXT

    # ==========================================================================
    # SLIDE 12: SUPERVISED MACHINE LEARNING (MODEL 2)
    # ==========================================================================
    s12 = prs.slides.add_slide(blank_layout)
    add_header(s12, "Literature Breakdown", "Supervised Machine Learning (Model 2)", "High Routine Accuracy Coupled with Fragility Under Severe Shock")

    p12_bullets = [
        ("24 BTS OTP Operational Features", "Ingests arrival/departure delays, cancellations, taxi queues, flight bank dispersion, and aircraft gauge."),
        ("Routine Pareto Frontier Winner", "Delivers outstanding routine accuracy (MASE = 0.680–0.700) with zero feedback latency under nominal operations."),
        ("The Empty Checkpoint Fallacy", "During convective storms, flights cancel from airline feeds. The decision tree predicts zero volume, but lobbies are packed with stranded travelers."),
        ("Acute Disruption Fragility", "Pure ML suffers catastrophic collapse during convective IROPS shocks (Recovery Multiplier R_MASE = 2.14, TTR > 8.0h).")
    ]
    add_bullet_list(s12, Inches(0.8), Inches(1.85), Inches(5.2), Inches(5.0), p12_bullets)

    # Right: High-impact KPI Card & Summary
    c12_right = add_card(s12, Inches(6.3), Inches(1.85), Inches(6.2), Inches(5.0), WHITE, LINE_BORDER)
    tf = c12_right.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_right = Inches(0.35)
    tf.margin_top = Inches(0.4)

    p = tf.paragraphs[0]
    p.text = "24"
    p.font.size = Pt(48)
    p.font.bold = True
    p.font.color.rgb = NAVY
    p.alignment = PP_ALIGN.CENTER

    p = tf.add_paragraph()
    p.text = "BTS OTP & OPERATIONAL FEATURES"
    p.font.size = Pt(12)
    p.font.bold = True
    p.font.color.rgb = BLUE_ACCENT
    p.alignment = PP_ALIGN.CENTER
    p.space_before = Pt(4)

    p = tf.add_paragraph()
    p.text = "Dual Operational Regime Split:"
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = NAVY
    p.space_before = Pt(20)

    p = tf.add_paragraph()
    p.text = "• Routine Nominal Flow (Delays < 15m): Model 2 wins Pareto efficiency with instantaneous inference and no sensor feedback requirement."
    p.font.size = Pt(11)
    p.font.color.rgb = DARK_TEXT
    p.space_before = Pt(6)

    p = tf.add_paragraph()
    p.text = "• Severe Convective Shocks (Delays ≥ 45m): Algorithmic blind spot causes severe under-staffing during terminal crisis."
    p.font.size = Pt(11)
    p.font.color.rgb = AMBER
    p.space_before = Pt(6)

    # ==========================================================================
    # SLIDE 13: SEQUENTIAL TWO-STAGE HYBRIDS (MODEL 3)
    # ==========================================================================
    s13 = prs.slides.add_slide(blank_layout)
    add_header(s13, "Literature Breakdown", "Sequential Two-Stage Hybrid Architectures (Model 3)", "Coupling Macro Flight Schedule Cycles with Real-Time Floor Innovation Feedback")

    # Rendered Formula
    add_fitted_image(s13, rendered_formulas['formula_two_stage_hybrid.png'], Inches(0.8), Inches(1.8), Inches(5.2), Inches(1.1))

    p13_bullets = [
        ("Two-Stage Architecture", "Couples an operational flight schedule baseline M_base with real-time floor error feedback α · (Y_{t-1} - Ŷ_{t-1})."),
        ("Stage 1 (Operational Base)", "Captures macro flight banks, aircraft seat capacity, day-of-week rhythms, and connecting deflators."),
        ("Stage 2 (Real-Time Feedback)", "Injects live prior-hour screening floor innovation (e_{t-1}), immediately correcting stale schedules when severe storms ground departures."),
        ("Defeats the Fallacy", "Prevents the Empty Checkpoint Fallacy: stranded passengers in lobbies are detected instantly by live checkpoint sensors.")
    ]
    add_bullet_list(s13, Inches(0.8), Inches(3.1), Inches(5.2), Inches(3.8), p13_bullets)

    # Right Diagram
    add_fitted_image(s13, "figures/Model walk through.png", Inches(6.3), Inches(1.85), Inches(6.2), Inches(5.0))

    # ==========================================================================
    # SLIDE 14: COVID-19 DEMARCATION & SAMPLE STABILITY
    # ==========================================================================
    s14 = prs.slides.add_slide(blank_layout)
    add_header(s14, "Empirical Demarcation", "The Structural Impact of COVID-19 Demarcation", "Purging Pandemic Distortions to Establish Time-Series Stability")

    p14_bullets = [
        ("May 1, 2022 Cutoff", "Federal transit mask mandate dissolved; commercial air travel patterns normalized across U.S. airports."),
        ("Chow Break Test", "F = 1.42, p = 0.18. Fails to reject null hypothesis; confirms structural parameter stability across 44 months."),
        ("84.7% Load Factor Recovery", "Systemwide load factors fully recovered to historical pre-pandemic baselines."),
        ("Purging 2020–2021 Data", "Recursive CUSUM residuals prove that training models on 2020–2021 induces severe non-stationary bias.")
    ]
    add_bullet_list(s14, Inches(0.8), Inches(1.85), Inches(5.2), Inches(5.0), p14_bullets)
    add_fitted_image(s14, "figures/post-pandemic justification.png", Inches(6.3), Inches(1.85), Inches(6.2), Inches(5.0))

    # ==========================================================================
    # SLIDE 15: WHY AVIATION DEMANDS DYNAMIC PERFORMANCE MEASURES
    # ==========================================================================
    s15 = prs.slides.add_slide(blank_layout)
    add_header(s15, "Evaluative Synthesis", "Why Aviation Demands Dynamic Performance Measures", "The Danger of Relying on Global Annual Error Metrics")

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
        c = add_card(s15, Inches(0.8), y, Inches(11.733), Inches(1.55), WHITE, LINE_BORDER)
        tf = c.text_frame
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

    p16_bullets = [
        ("3.1 Research Approach", "Comparative out-of-time evaluation of 4 paradigms across 3 operational pillars."),
        ("3.2 Sample Cohort", "4-tier filtering isolating 9 airports & 12 carrier-exclusive complexes."),
        ("3.3 Data Sources & ETL", "67.2M raw federal records conformed to 42.1M Star Schema rows."),
        ("3.4 Validity Safeguards", "DB1B connecting deflator, carrier isolation, and 168-h purge buffer."),
        ("3.5 Treatment & Testing", "Out-of-time 2025 holdout and Diebold-Mariano statistical tests.")
    ]
    add_bullet_list(s16, Inches(0.8), Inches(1.85), Inches(5.2), Inches(5.0), p16_bullets)
    add_fitted_image(s16, "figures/Combined_Data_Pipeline_and_Funnel_Lifecycle.png", Inches(6.3), Inches(1.85), Inches(6.2), Inches(5.0))

    # ==========================================================================
    # SLIDE 17: FORECASTING MODEL FAMILIES & BASELINE CONTROL
    # ==========================================================================
    s17 = prs.slides.add_slide(blank_layout)
    add_header(s17, "Methodology Approach", "Forecasting Model Families & Baseline Control", "Four Candidate Paradigms Representing Distinct Operational Philosophies")

    # Top summary strip
    c17_strip = add_card(s17, Inches(0.8), Inches(1.8), Inches(11.733), Inches(0.9), WHITE, LINE_BORDER)
    tf = c17_strip.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_right = Inches(0.2)
    tf.margin_top = Inches(0.12)
    p = tf.paragraphs[0]
    p.text = "• Baseline Control: Daily Persistence (t-24, MASE ≡ 1.000)   • Model 1: Deterministic Flight Schedule (ACRP 40 Convolution)\n• Model 2: Supervised ML (LightGBM + 24 OTP Features)   • Model 3: Dynamic Two-Stage Hybrid (Schedule Base + Floor Feedback)"
    p.font.size = Pt(10.5)
    p.font.color.rgb = DARK_TEXT

    add_fitted_image(s17, "figures/figure_3_1_forecasting_model_families.png", Inches(0.8), Inches(2.85), Inches(11.733), Inches(4.3))

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
    for i, (tag, name, body) in enumerate(phases):
        x = Inches(0.8) + i * Inches(2.98)
        c = add_card(s18, x, Inches(1.85), Inches(2.78), Inches(5.0), WHITE, LINE_BORDER)
        tf = c.text_frame
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
    for i, (tag, name, body) in enumerate(results_flow):
        x = Inches(0.8) + i * Inches(2.98)
        card = add_card(s20, x, Inches(1.85), Inches(2.78), Inches(5.0), WHITE, LINE_BORDER)
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

    p21_bullets = [
        ("Flight Movement Density", "+16.9% higher flight volume (224,576 annual flights vs. 192,160 top-25 mean)."),
        ("Cancellation Churn", "+14.1% higher cancellation rate (1.63% vs. 1.43% top-25 mean)."),
        ("True Originating Volume", "+25.0% higher local originating demand (16.4M vs. 13.1M pax)."),
        ("Elevated Volatility", "CV_TSA = 0.8728 vs. 0.8250 top-25 mean (+5.8% arrival burstiness)."),
        ("Statistical Stress Testing", "The 9-airport cohort represents genuine high-congestion pressure fronts, providing robust power for resilience testing.")
    ]
    add_bullet_list(s21, Inches(0.8), Inches(1.85), Inches(5.2), Inches(5.0), p21_bullets)
    add_fitted_image(s21, "figures/Power of 9 airports.png", Inches(6.3), Inches(1.85), Inches(6.2), Inches(5.0))

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
    for i, (tag, name, sub, body) in enumerate(tiers):
        x = Inches(0.8) + i * Inches(2.98)
        card = add_card(s22, x, Inches(1.85), Inches(2.78), Inches(5.0), WHITE, LINE_BORDER)
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

    p23_bullets = [
        ("Balanced Legacy Representation", "12 carrier-exclusive complexes spanning American (5), Delta (5), and United (4)."),
        ("Delta Air Lines Complexes", "ATL (Domestic South), BOS (Terminal A), DTW (McNamara Terminal), LAX (Terminal 3), LGA (Terminal C)."),
        ("American Airlines Complexes", "DFW (Terminals A, B, C), BOS (Terminal B), LAX (Terminal 4), ORD (Terminal 3), PHL (Terminals B/C)."),
        ("United Airlines Complexes", "EWR (Terminal C), LAX (Terminal 7), ORD (Terminal 1)."),
        ("Econometric Identification", "Single-carrier exclusive checkpoints eliminate inter-airline passenger mixing.")
    ]
    add_bullet_list(s23, Inches(0.8), Inches(1.85), Inches(5.2), Inches(5.0), p23_bullets)
    add_fitted_image(s23, "figures/airport clusters.png", Inches(6.3), Inches(1.85), Inches(6.2), Inches(5.0))

    # ==========================================================================
    # SLIDE 24: ANNUAL SEASONAL VOLATILITY REGIMES
    # ==========================================================================
    s24 = prs.slides.add_slide(blank_layout)
    add_header(s24, "Macro Regimes", "Annual Seasonal Volatility Regimes", "Macro Travel Fluctuations and Convective Weather Disruptions (Table 4.3b)")

    c24_strip = add_card(s24, Inches(0.8), Inches(1.8), Inches(11.733), Inches(0.9), WHITE, LINE_BORDER)
    tf = c24_strip.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_right = Inches(0.2)
    tf.margin_top = Inches(0.12)
    p = tf.paragraphs[0]
    p.text = "• Off-Peak Winter (Wk 1–8, 45–46): Low volume, calm operations   • Mid-Peak Spring (Wk 9–21, 36–44): Business travel\n• Summer Convective Peak (Wk 22–35): Maximum delay dispersion (σ = 68.4m)   • Holiday Travel Peaks (Wk 47–52): Leisure surges"
    p.font.size = Pt(10.5)
    p.font.color.rgb = DARK_TEXT

    add_fitted_image(s24, "figures/figure_4_2_annual_volatility_clusters.png", Inches(0.8), Inches(2.85), Inches(11.733), Inches(4.3))

    # ==========================================================================
    # SLIDE 25: DAY-OF-WEEK VOLATILITY & BIMODAL DIURNAL PEAKS
    # ==========================================================================
    s25 = prs.slides.add_slide(blank_layout)
    add_header(s25, "Diurnal & DOW Cycles", "Day-of-Week Volatility & Bimodal Diurnal Peaks", "Temporal Asynchrony Between Passenger Screening and Aircraft Delays")

    p25_bullets = [
        ("Monday Morning Surge", "Peak early morning screening (05:00–08:00); flight departures operate on-time (on-time rate > 88%)."),
        ("Sunday Evening Cascades", "Airside delay cascades ripple into evening banks; departure delay dispersion expands by +35%."),
        ("Bimodal Diurnal Waves", "Morning peak (05:00–08:00) reaches 11,380 pax/hr; evening peak (14:00–22:00) sees flight delays exceed 63 minutes."),
        ("Airside-Landside Asynchrony", "Checkpoint queuing friction is decoupled from contemporaneous flight departures.")
    ]
    add_bullet_list(s25, Inches(0.8), Inches(1.85), Inches(5.2), Inches(5.0), p25_bullets)
    add_fitted_image(s25, "figures/figure_4_3_day_of_week_volatility_dynamics.png", Inches(6.3), Inches(1.85), Inches(6.2), Inches(2.45))
    add_fitted_image(s25, "figures/figure_4_4_diurnal_hourly_volatility_clusters.png", Inches(6.3), Inches(4.45), Inches(6.2), Inches(2.45))

    # ==========================================================================
    # SLIDE 26: EMPIRICAL PASSENGER SHOW-UP DYNAMICS (LEAD-LAG)
    # ==========================================================================
    s26 = prs.slides.add_slide(blank_layout)
    add_header(s26, "Lead-Lag Dynamics", "Empirical Passenger Show-Up Curve Convolution", "Resolving the Optimal Lead Time for Checkpoint Arrival Forecasting")

    add_fitted_image(s26, rendered_formulas['formula_lead_lag.png'], Inches(0.8), Inches(1.8), Inches(5.2), Inches(1.0))

    p26_bullets = [
        ("Contemporaneous Fails", "Flight schedules at departure hour t explain under 20% of passenger screening arrivals (R² = 0.1982)."),
        ("2-Hour Lead Optimum", "Correlation peaks at a 2-hour lead (t+2), explaining 53.5% of variance (F = 142.80, p < 0.001)."),
        ("ACRP Report 40 Validation", "Empirically validates lognormal passenger arrival curves: median lead time is 105 min domestic, 135 min leisure."),
        ("Actionable TSA Staffing", "Checkpoint supervisors must convolve flight banks at t+2 to set screening lane capacity.")
    ]
    add_bullet_list(s26, Inches(0.8), Inches(3.0), Inches(5.2), Inches(3.9), p26_bullets)
    add_fitted_image(s26, "figures/figure_4_5_lead_lag_convolution_curves.png", Inches(6.3), Inches(1.85), Inches(6.2), Inches(5.0))

    # ==========================================================================
    # SLIDE 27: CERTIFIED 2025 OUT-OF-TIME HOLDOUT BENCHMARKS (TABLE 4.10)
    # ==========================================================================
    s27 = prs.slides.add_slide(blank_layout)
    add_header(s27, "Model Benchmarks", "Certified 2025 Out-of-Time Holdout Benchmarks", "Rigorous Evaluation Across Full Holdout Period (Table 4.10)")

    c27_strip = add_card(s27, Inches(0.8), Inches(1.8), Inches(11.733), Inches(0.85), WHITE, LINE_BORDER)
    tf = c27_strip.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_right = Inches(0.2)
    tf.margin_top = Inches(0.1)
    p = tf.paragraphs[0]
    p.text = "• Model 3 (Dynamic Hybrid) DECISIVE WINNER: Lowest RMSE (222.1 pax/h), Lowest MASE (0.662), beating persistence by 33.8% (DM = -4.82, p < 0.001).\n• Model 2 (Supervised ML) wins Routine Pareto Efficiency: MASE = 0.779.   • Model 1 (Deterministic): MASE = 0.945."
    p.font.size = Pt(10.5)
    p.font.color.rgb = DARK_TEXT

    add_fitted_image(s27, "figures/figure_4_6_master_model_benchmark_matrix.png", Inches(0.8), Inches(2.8), Inches(11.733), Inches(4.35))

    # ==========================================================================
    # SLIDE 28: MULTI-PILLAR HYPOTHESIS TESTING (TABLE 4.11 / TABLE 5.4)
    # ==========================================================================
    s28 = prs.slides.add_slide(blank_layout)
    add_header(s28, "Hypothesis Testing", "Multi-Pillar Hypothesis Testing: The Asymmetric Trade-Off", "Full Evaluation Across Table 4.11 and Master Hypothesis H₁")

    c28_strip = add_card(s28, Inches(0.8), Inches(1.8), Inches(11.733), Inches(0.85), WHITE, LINE_BORDER)
    tf = c28_strip.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_right = Inches(0.2)
    tf.margin_top = Inches(0.1)
    p = tf.paragraphs[0]
    p.text = "• Dimension 1 (Robustness): Model 3 lowest RMSE (222.1); Model 2 wins Routine Pareto Efficiency. Confirms H1a.\n• Dimension 2 (Resilience): Model 3 DECISIVE WINNER (R = 1.05, TTR = 2.8h). ML collapses (R = 2.14). Confirms H1b.\n• Dimension 3 (Generalizability): Model 1 DECISIVE WINNER (RTR = 1.04). Model 3 fails (RTR = 1.19). Confirms H1c."
    p.font.size = Pt(10)
    p.font.color.rgb = DARK_TEXT

    add_fitted_image(s28, "figures/figure_5_4_master_hypothesis_trade_off_dashboard.png", Inches(0.8), Inches(2.8), Inches(11.733), Inches(4.35))

    # ==========================================================================
    # SLIDE 29: DEEP-DIVE RESILIENCE & THE EMPTY CHECKPOINT FALLACY
    # ==========================================================================
    s29 = prs.slides.add_slide(blank_layout)
    add_header(s29, "Deep-Dive Resilience", "Dimension 2: Disruption Resilience & Shock Recovery", "Convective Weather Ground Stops and the Empty Checkpoint Fallacy")

    add_fitted_image(s29, rendered_formulas['formula_r_mase.png'], Inches(0.8), Inches(1.8), Inches(5.2), Inches(1.0))

    p29_bullets = [
        ("The Empty Checkpoint Fallacy", "Convective storms trigger cancellations. Decision trees infer passenger demand vanished, predicting near-zero arrivals (R = 2.14)."),
        ("Terminal Lobby Crowding", "Passengers remain packed in ticket lobbies seeking rebooking and security access; pure ML leaves lanes unstaffed."),
        ("Hybrid Sensor Feedback Rescue", "Model 3 ingests live screening counts (e_{t-1}), instantly overriding stale schedules and restoring accuracy within 2.8 hours (R = 1.05)."),
        ("Operational Outcome", "Dynamic error feedback prevents checkpoint queuing crises during severe convective ground stops.")
    ]
    add_bullet_list(s29, Inches(0.8), Inches(3.0), Inches(5.2), Inches(3.9), p29_bullets)
    add_fitted_image(s29, "figures/figure_5_2_disruption_resilience_and_shock_recovery.png", Inches(6.3), Inches(1.85), Inches(6.2), Inches(5.0))

    # ==========================================================================
    # SLIDE 30: DEEP-DIVE GENERALIZABILITY & SPATIAL TRANSFER
    # ==========================================================================
    s30 = prs.slides.add_slide(blank_layout)
    add_header(s30, "Deep-Dive Generalizability", "Dimension 3: Generalizability & Spatial Transfer", "Zero-Shot Spatial Transfer from Newark (EWR) to LaGuardia (LGA)")

    add_fitted_image(s30, rendered_formulas['formula_rtr.png'], Inches(0.8), Inches(1.8), Inches(5.2), Inches(1.0))

    p30_bullets = [
        ("Model 1 Wins Transfer (Physics)", "RTR = 1.04, ΔMASE = +4.0%. Passenger arrival psychology (ACRP 40) is invariant across airports, transferring seamlessly."),
        ("Model 3 Decisively Fails (Overfitting)", "RTR = 1.19, ΔMASE = +21.5%. Decision tree splits overfit to Newark Terminal C's unique taxiway delays and concourse geometry."),
        ("Feedback Distortion", "When transferred without retraining, distorted predictions cause error feedback to amplify rather than correct errors."),
        ("Strategic Rule", "Deploy deterministic schedule physics for new concourses until 6–12 months of local checkpoint history is accumulated.")
    ]
    add_bullet_list(s30, Inches(0.8), Inches(3.0), Inches(5.2), Inches(3.9), p30_bullets)
    add_fitted_image(s30, "figures/figure_5_3_generalizability_and_spatial_transfer.png", Inches(6.3), Inches(1.85), Inches(6.2), Inches(5.0))

    # ==========================================================================
    # SLIDE 31: REAL-WORLD AVIATION APPLICATION: THE OPERATOR'S PLAYBOOK
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

    c32_banner = add_card(s32, Inches(0.8), Inches(1.85), Inches(11.733), Inches(1.1), NAVY, NAVY)
    tf = c32_banner.text_frame
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

    c32_takeaways = add_card(s32, Inches(0.8), Inches(3.1), Inches(11.733), Inches(3.75), WHITE, LINE_BORDER)
    tf = c32_takeaways.text_frame
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
    for i, (title, desc) in enumerate(bullets):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.text = f"•  {title}: "
        p.font.bold = True
        p.font.size = Pt(11)
        p.font.color.rgb = NAVY
        if i > 0:
            p.space_before = Pt(8)

        run = p.add_run()
        run.text = desc
        run.font.size = Pt(10.5)
        run.font.bold = False
        run.font.color.rgb = DARK_TEXT

    p_close = tf.add_paragraph()
    p_close.text = "Thank you for your guidance, mentorship, and support. Questions & Discussion."
    p_close.font.name = "Georgia"
    p_close.font.bold = True
    p_close.font.italic = True
    p_close.font.size = Pt(12)
    p_close.font.color.rgb = BLUE_ACCENT
    p_close.space_before = Pt(14)
    p_close.alignment = PP_ALIGN.CENTER

    # Save presentation
    prs.save(OUTPUT_PATH)
    print(f"Successfully generated clean presentation: {OUTPUT_PATH}")

    # Mirror to master-docs
    os.makedirs(os.path.dirname(MIRROR_PATH), exist_ok=True)
    shutil.copyfile(OUTPUT_PATH, MIRROR_PATH)
    print(f"Successfully mirrored presentation to: {MIRROR_PATH}")

    # Mirror to thesis_final_package/defense
    os.makedirs(os.path.dirname(PKG_MIRROR_PATH), exist_ok=True)
    shutil.copyfile(OUTPUT_PATH, PKG_MIRROR_PATH)
    print(f"Successfully mirrored presentation to: {PKG_MIRROR_PATH}")


if __name__ == "__main__":
    create_deck()
