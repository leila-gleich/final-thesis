"""
src/analysis/generate_radar_chart.py
------------------------------------
Generates Figure 5.1: The Asymmetric Trade-Off Evaluation Triangle (H1)
Visualizes multi-dimensional performance trade-offs across candidate models
(Robustness, Resilience, Generalizability) adhering strictly to AGENTS.md.
"""

from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
FIGURES_DIR = PROJECT_ROOT / "figures"
DEFAULT_OUTPUT_PATH = FIGURES_DIR / "ch05_discussion" / "Figure_5_1_Asymmetric_Trade_Off_Triangle.png"


def create_radar_chart(output_path: Path = DEFAULT_OUTPUT_PATH):
    """Generates Figure 5.1: The Asymmetric Trade-Off Triangle radar chart."""
    categories = ['Robustness\n(Routine Accuracy)', 'Resilience\n(Shock Recovery)', 'Generalizability\n(Spatial Transfer)']
    N = len(categories)
    angles = [n / float(N) * 2 * np.pi for n in range(N)]
    angles += angles[:1]

    # Performance indices scaled from 0.0 (unacceptable) to 1.0 (optimal)
    # Grounded in empirical metrics from Table 5.4:
    # Robustness: Target MASE < 0.70. Model 3 = 0.662 (0.95), Model 2 = 0.690 (0.90), Model 1 = 0.945 (0.45), Baseline = 1.000 (0.30)
    # Resilience: Target R_MASE ≈ 1.00, TTR < 4.0h. Model 3 (R=1.05, TTR=2.8h -> 0.95), Model 2 (R=2.14, TTR=5.4h -> 0.35), Model 1 (R=1.32, TTR=7.8h -> 0.50), Baseline (0.40)
    # Generalizability: Target RTR ≈ 1.00, Delta MASE <= 10%. Model 1 (RTR=1.04, +4.0% -> 0.95), Model 2 (RTR=1.08, +8.3% -> 0.80), Model 3 (RTR=1.19, +21.5% -> 0.30), Baseline (0.40)
    scores = {
        'Baseline Control (Daily Persistence)': [0.30, 0.40, 0.40],
        'Model 1 (Deterministic Flight Schedule)': [0.45, 0.50, 0.95],
        'Model 2 (Supervised Machine Learning)': [0.90, 0.35, 0.80],
        'Model 3 (Dynamic Two-Stage Hybrid)': [0.95, 0.95, 0.30],
    }

    colors = {
        'Baseline Control (Daily Persistence)': '#7f7f7f',
        'Model 1 (Deterministic Flight Schedule)': '#1f77b4',
        'Model 2 (Supervised Machine Learning)': '#ff7f0e',
        'Model 3 (Dynamic Two-Stage Hybrid)': '#2ca02c',
    }

    linestyles = {
        'Baseline Control (Daily Persistence)': ':',
        'Model 1 (Deterministic Flight Schedule)': '--',
        'Model 2 (Supervised Machine Learning)': '-.',
        'Model 3 (Dynamic Two-Stage Hybrid)': '-',
    }

    fig, ax = plt.subplots(figsize=(8, 7), subplot_kw=dict(polar=True), dpi=300)
    ax.set_theta_offset(np.pi / 2)
    ax.set_theta_direction(-1)

    plt.xticks(angles[:-1], categories, size=11, weight='bold', color='#222222')
    ax.set_rlabel_position(0)
    plt.yticks([0.2, 0.4, 0.6, 0.8, 1.0], ["0.2", "0.4", "0.6", "0.8", "1.0 (Optimal)"], color="#555555", size=9)
    plt.ylim(0, 1.05)

    for model_name, values in scores.items():
        vals = values + values[:1]
        ax.plot(angles, vals, linewidth=2.2, linestyle=linestyles[model_name], label=model_name, color=colors[model_name])
        ax.fill(angles, vals, color=colors[model_name], alpha=0.10)

    plt.title("Figure 5.1: The Asymmetric Trade-Off Evaluation Triangle (H1)\nMulti-Dimensional Performance Trade-Offs Across Candidate Models",
              size=12, weight='bold', pad=25, color='#111111')
    plt.legend(loc='upper right', bbox_to_anchor=(1.35, 1.15), frameon=True, fontsize=9.5)
    plt.tight_layout()
    output_path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close(fig)
    print(f"  + Generated radar chart: {output_path}")


if __name__ == "__main__":
    create_radar_chart()
