"""Build the paper and slide figures from the Assignment 2 results.

All values are copied from the executed outputs of experiment.ipynb
(Sections 6-8). Rerunning the notebook reproduces them (SEED = 42).
Run: python make_figures.py  -> writes PNGs to figures/
"""
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

OUT = Path("figures")
OUT.mkdir(exist_ok=True)
sns.set_theme(style="whitegrid", context="talk", font_scale=0.8)
PALETTE = {"Raw features": "#BBBBBB", "Engineered features": "#4C72B0"}

# Table 1 source: test-set results on 86 held-out mixtures (notebook Section 7)
test = pd.DataFrame({
    "Model": ["Linear Regression", "Random Forest", "Gradient Boosting"] * 2,
    "Features": ["Raw features"] * 3 + ["Engineered features"] * 3,
    "RMSE": [9.592, 5.682, 5.189, 6.561, 4.857, 4.404],
    "MAE": [7.519, 4.377, 3.679, 5.294, 3.570, 3.148],
    "R2": [0.647, 0.876, 0.897, 0.835, 0.910, 0.926],
})

# Figure 1: test RMSE by model and feature set
fig, ax = plt.subplots(figsize=(8, 4.8))
sns.barplot(data=test, x="Model", y="RMSE", hue="Features", palette=PALETTE, ax=ax)
for c in ax.containers:
    ax.bar_label(c, fmt="%.2f", fontsize=10, padding=2)
ax.set_xlabel("")
ax.set_ylabel("Test RMSE (MPa)")
ax.set_title("Figure 1. Test RMSE on unseen mixtures (lower is better)")
ax.set_ylim(0, 11)
ax.legend(title="", loc="upper right")
fig.tight_layout()
fig.savefig(OUT / "fig1_test_rmse.png", dpi=200)
plt.close(fig)

# Figure 2: grouped vs random split, 10 seeds (notebook Section 8)
split = pd.DataFrame({
    "Split": ["Grouped by mixture\n(unseen mixtures)", "Random rows\n(mixtures shared)"],
    "Mean RMSE": [5.12, 3.89],
    "SD": [0.38, 0.40],
})
fig, ax = plt.subplots(figsize=(6.5, 4.8))
bars = ax.bar(split["Split"], split["Mean RMSE"], yerr=split["SD"], capsize=8,
              color=["#4C72B0", "#DD8452"], width=0.55)
ax.bar_label(bars, labels=[f"{m:.2f} ± {s:.2f}" for m, s in zip(split["Mean RMSE"], split["SD"])],
             padding=14, fontsize=11)
ax.set_ylabel("Test RMSE (MPa), mean of 10 seeds")
ax.set_ylim(0, 7)
ax.set_title("Figure 2. Random splitting understates error")
fig.tight_layout()
fig.savefig(OUT / "fig2_split_leakage.png", dpi=200)
plt.close(fig)

# Figure 3: permutation importance of the best model (notebook Section 7)
imp = pd.DataFrame({
    "Feature": ["log(age)", "water/binder", "water/cement", "binder", "water",
                "fly ash", "aggregate/binder", "coarse aggregate"],
    "Importance": [9.327, 5.862, 3.119, 1.274, 0.470, 0.460, 0.305, 0.245],
    "SD": [0.306, 0.412, 0.257, 0.116, 0.084, 0.104, 0.124, 0.076],
})
fig, ax = plt.subplots(figsize=(8, 4.8))
ax.barh(imp["Feature"][::-1], imp["Importance"][::-1], xerr=imp["SD"][::-1],
        color="#4C72B0", capsize=3)
ax.set_xlabel("Increase in test RMSE when shuffled (MPa)")
ax.set_title("Figure 3. Permutation importance, Gradient Boosting")
fig.tight_layout()
fig.savefig(OUT / "fig3_importance.png", dpi=200)
plt.close(fig)

print("Figures written to", OUT.resolve())
