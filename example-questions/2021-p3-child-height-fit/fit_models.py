"""Fit Model A (logistic) and Model B (sqrt) to the child-height data,
extrapolate to ages 15 and 30, and produce a comparison figure.

Model A:  H = a / (1 + b * exp(-c*t))     —  nonlinear LSQ via curve_fit
Model B:  H = sqrt(a + b*t)                —  linearize as H^2 = a + b*t,
                                              then ordinary least squares

The figure:
  - Data points (the 6 measurements).
  - Both fits drawn over the in-sample range [0, 18] and extrapolated to t=35.
  - Vertical dashed lines at t=15 and t=30 with each model's prediction.
  - Annotation of Model B's runaway behaviour and Model A's asymptote a.

Prints fitted parameters and predictions to stdout, and writes
fig1_model_compare.png next to this file.
"""
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import font_manager
from scipy.optimize import curve_fit

OUTDIR = Path(__file__).parent
plt.rcParams["axes.unicode_minus"] = False

cjk_candidates = ["Noto Sans CJK TC", "Noto Sans CJK SC", "Noto Sans CJK JP"]
available = {f.name for f in font_manager.fontManager.ttflist}
cjk_font = next((c for c in cjk_candidates if c in available), None)
if cjk_font:
    plt.rcParams["font.family"] = cjk_font


# Data ------------------------------------------------------------------------
t_data = np.array([0.0, 5.0, 8.0, 12.0, 16.0, 18.0])
H_data = np.array([20.0, 36.2, 52.0, 60.0, 69.2, 70.0])


# -------- Model A: logistic, nonlinear LSQ -----------------------------------
def model_A(t, a, b, c):
    return a / (1.0 + b * np.exp(-c * t))


# Reasonable initial guesses:
#   a ~ slightly above max(H) (the asymptote)
#   b from H(0) = a/(1+b) -> b = a/H(0) - 1
#   c ~ 0.25 from the inflection-region spacing
a0 = 75.0
b0 = a0 / H_data[0] - 1.0
c0 = 0.25
pA, _ = curve_fit(model_A, t_data, H_data, p0=[a0, b0, c0], maxfev=10000)
a_A, b_A, c_A = pA

# -------- Model B: H^2 = a + b*t  (closed-form OLS) --------------------------
H2 = H_data ** 2
# Fit y = a + b*t with x = t_data.  Use polyfit(deg=1).
b_B, a_B = np.polyfit(t_data, H2, 1)   # polyfit returns highest-degree first


def model_B(t, a, b):
    val = a + b * t
    return np.sqrt(np.maximum(val, 0))   # guard for negative-arg in pathological t


# -------- Goodness of fit (RMSE on data) -------------------------------------
def rmse(y, yhat):
    return float(np.sqrt(np.mean((y - yhat) ** 2)))


rmse_A = rmse(H_data, model_A(t_data, *pA))
rmse_B = rmse(H_data, model_B(t_data, a_B, b_B))

# -------- Predictions --------------------------------------------------------
predict_at = [15.0, 30.0]
A_preds = {t: float(model_A(t, *pA)) for t in predict_at}
B_preds = {t: float(model_B(t, a_B, b_B)) for t in predict_at}

print("=" * 60)
print("Model A (logistic):  H = a / (1 + b·exp(-c·t))")
print(f"  a = {a_A:.4f}  (asymptotic height, inch)")
print(f"  b = {b_A:.4f}")
print(f"  c = {c_A:.4f}")
print(f"  RMSE on data = {rmse_A:.3f} inch")
print(f"  H(15) = {A_preds[15.0]:.2f} inch")
print(f"  H(30) = {A_preds[30.0]:.2f} inch")
print()
print("Model B (sqrt):  H = sqrt(a + b·t)")
print(f"  a = {a_B:.4f}")
print(f"  b = {b_B:.4f}")
print(f"  RMSE on data = {rmse_B:.3f} inch")
print(f"  H(15) = {B_preds[15.0]:.2f} inch")
print(f"  H(30) = {B_preds[30.0]:.2f} inch    <-- 注意:不合理")
print("=" * 60)

# -------- Plot ---------------------------------------------------------------
t_smooth = np.linspace(0, 35, 400)
fig, ax = plt.subplots(figsize=(9.5, 6.5))

# Shade the in-sample range
ax.axvspan(0, 18, color="#eee", alpha=0.6, zorder=0,
           label="資料範圍 (0–18 歲)")

# Data points
ax.plot(t_data, H_data, "o", ms=10, mec="black", mfc="white",
        label="量測資料", zorder=5)

# Model A curve
ax.plot(t_smooth, model_A(t_smooth, *pA), lw=2.2, color="#1f77b4",
        label=fr"Model A:  $a/(1+b e^{{-c t}})$  (RMSE={rmse_A:.2f})")
# Model A asymptote
ax.axhline(a_A, ls=":", color="#1f77b4", alpha=0.6,
           label=fr"$a_A = {a_A:.2f}$  (logistic 漸近線)")

# Model B curve
ax.plot(t_smooth, model_B(t_smooth, a_B, b_B), lw=2.2, color="#d62728",
        label=fr"Model B:  $\sqrt{{a + b t}}$  (RMSE={rmse_B:.2f})")

# Predictions at t=15 and t=30
for t in predict_at:
    ax.axvline(t, ls="--", color="#888", alpha=0.5)
    ax.plot(t, A_preds[t], "^", ms=12, color="#1f77b4", zorder=6)
    ax.plot(t, B_preds[t], "v", ms=12, color="#d62728", zorder=6)
    ax.annotate(fr"$H_A({t:.0f}) = {A_preds[t]:.1f}$",
                (t, A_preds[t]), xytext=(8, 8), textcoords="offset points",
                color="#1f77b4", fontsize=9, fontweight="bold")
    ax.annotate(fr"$H_B({t:.0f}) = {B_preds[t]:.1f}$",
                (t, B_preds[t]), xytext=(8, -16), textcoords="offset points",
                color="#d62728", fontsize=9, fontweight="bold")

ax.set_xlabel("Age (years)")
ax.set_ylabel("Height (inch)")
ax.set_title("兒童身高擬合:logistic vs sqrt\n(在 0–18 歲擬合,外推到 15、30 歲)")
ax.set_xlim(0, 35)
ax.set_ylim(15, 100)
ax.grid(True, alpha=0.3)
ax.legend(loc="lower right", fontsize=9, framealpha=0.92)

# Highlight the divergence: shade the region where the two predictions diverge.
ax.fill_between(t_smooth, model_A(t_smooth, *pA), model_B(t_smooth, a_B, b_B),
                where=t_smooth >= 18, alpha=0.12, color="#d62728")
ax.text(28, 82, "外推區:Model B\n還在飛漲(無上限)",
        fontsize=10, color="#a00", ha="center",
        bbox=dict(boxstyle="round,pad=0.4", fc="#fff", ec="#c66", alpha=0.9))

fig.tight_layout()
fig.savefig(OUTDIR / "fig1_model_compare.png", dpi=150, bbox_inches="tight")
print(f"\nWrote {OUTDIR / 'fig1_model_compare.png'}")
