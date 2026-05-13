"""Fit three biomass-vs-time models to the Adriatic algae data and
extrapolate to t = 150 days.

Models:
    A:  B = a / (1 + b·exp(-c·t))            (standard logistic, 3 params)
    B:  B = a + b·t^c                        (power + offset, 3 params)
    C:  B = a / (1 + b·exp(-c·t))^(1/d)      (Richards / generalized
                                              logistic, 4 params)

All three are fit with scipy.optimize.curve_fit (Levenberg-Marquardt).
We seed the optimizer with hand-picked initial guesses so the solver
doesn't drift into bad local minima:

  - Model A: a ≈ 6 (slightly above max(B));  b large (≈1000) since
             B(0) ≈ a/(1+b) must be near zero;  c ≈ ln(b)/t_inflection
             ≈ 0.25.
  - Model B: take log of both sides — log(B − a) = log(b) + c·log(t).
             For our initial guess we set a=0 and use log-log regression
             on the data to get rough b, c.
  - Model C: start from Model A's fit with d = 1 (so C reduces to A).

The figure shows the data, the three fits over [0, 160] days, and the
predictions at t = 150 days for each.

Output: prints parameters, RMSE, and B(150) for each model;
        writes fig1_model_compare.png next to this file.
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
t_data = np.array([11.0, 15.0, 18.0, 23.0, 26.0, 31.0, 39.0,
                   44.0, 54.0, 64.0, 74.0])
B_data = np.array([0.00476, 0.0105, 0.0207, 0.0619, 0.337, 0.74, 1.7,
                   2.45, 3.5, 4.5, 5.09])


# Models ----------------------------------------------------------------------
def model_A(t, a, b, c):
    return a / (1.0 + b * np.exp(-c * t))


def model_B(t, a, b, c):
    return a + b * np.power(np.clip(t, 1e-9, None), c)


def model_C(t, a, b, c, d):
    # (1 + b·e^{-ct})^{1/d}: clamp base ≥ 1e-12 to avoid invalid power
    base = np.maximum(1.0 + b * np.exp(-c * t), 1e-12)
    return a / np.power(base, 1.0 / d)


def rmse(y, yhat):
    return float(np.sqrt(np.mean((y - yhat) ** 2)))


# Fit Model A -----------------------------------------------------------------
pA0 = [6.0, 1000.0, 0.25]
pA, _ = curve_fit(model_A, t_data, B_data, p0=pA0, maxfev=50000)
rmseA = rmse(B_data, model_A(t_data, *pA))

# Fit Model B -----------------------------------------------------------------
# Initial guess via log-log: assume a≈0, then log(B) = log(b) + c·log(t)
logt = np.log(t_data)
logB = np.log(np.clip(B_data, 1e-9, None))
c0, logb0 = np.polyfit(logt, logB, 1)
pB0 = [0.0, float(np.exp(logb0)), float(c0)]
pB, _ = curve_fit(model_B, t_data, B_data, p0=pB0, maxfev=50000)
rmseB = rmse(B_data, model_B(t_data, *pB))

# Fit Model C -----------------------------------------------------------------
# Constrain d ∈ [0.2, 5] to keep it in a meaningful Richards regime —
# without this, the optimizer drifts to d → 0 (the Gompertz limit) which
# is degenerate with respect to b.
pC0 = [pA[0], pA[1], pA[2], 1.0]
bounds_C = ([0.1,  1.0,  0.01, 0.2],
            [50.0, 1e6,  2.0,  5.0])
pC, _ = curve_fit(model_C, t_data, B_data, p0=pC0,
                  bounds=bounds_C, maxfev=50000)
rmseC = rmse(B_data, model_C(t_data, *pC))


# Predict at t = 150 ----------------------------------------------------------
t_target = 150.0
predA = float(model_A(t_target, *pA))
predB = float(model_B(t_target, *pB))
predC = float(model_C(t_target, *pC))


# Report ----------------------------------------------------------------------
print("=" * 70)
print(f"Model A (logistic):  B = a/(1 + b·e^(-c·t))")
print(f"  a = {pA[0]:.4f}   b = {pA[1]:.4f}   c = {pA[2]:.4f}")
print(f"  RMSE = {rmseA:.4f}  ·  B(150) = {predA:.3f} mm²")
print()
print(f"Model B (power):  B = a + b·t^c")
print(f"  a = {pB[0]:.4e}   b = {pB[1]:.4e}   c = {pB[2]:.4f}")
print(f"  RMSE = {rmseB:.4f}  ·  B(150) = {predB:.3f} mm²")
print()
print(f"Model C (Richards):  B = a / (1 + b·e^(-c·t))^(1/d)")
print(f"  a = {pC[0]:.4f}   b = {pC[1]:.4f}   c = {pC[2]:.4f}   d = {pC[3]:.4f}")
print(f"  RMSE = {rmseC:.4f}  ·  B(150) = {predC:.3f} mm²")
print("=" * 70)


# Plot ------------------------------------------------------------------------
t_smooth = np.linspace(1, 160, 500)
fig, axes = plt.subplots(1, 2, figsize=(14, 6.0),
                          gridspec_kw={"width_ratios": [1, 1]})

# Left panel: in-sample
ax = axes[0]
ax.plot(t_data, B_data, "o", ms=10, mec="black", mfc="white",
        label="量測資料", zorder=5)
ax.plot(t_smooth, model_A(t_smooth, *pA), lw=2.2, color="#1f77b4",
        label=fr"Model A (logistic)  RMSE={rmseA:.3f}")
ax.plot(t_smooth, model_B(t_smooth, *pB), lw=2.2, color="#d62728",
        label=fr"Model B (power)    RMSE={rmseB:.3f}")
ax.plot(t_smooth, model_C(t_smooth, *pC), lw=2.2, color="#2ca02c",
        label=fr"Model C (Richards) RMSE={rmseC:.3f}")
ax.axvspan(t_data.min(), t_data.max(), color="#eee", alpha=0.5,
           label="資料範圍")
ax.set_xlim(0, 80)
ax.set_ylim(-0.3, 7)
ax.set_xlabel("Time (days)")
ax.set_ylabel(r"Biomass (mm²)")
ax.set_title("資料範圍內擬合")
ax.grid(True, alpha=0.3)
ax.legend(loc="upper left", fontsize=9)

# Right panel: extrapolation to 150
ax = axes[1]
ax.plot(t_data, B_data, "o", ms=10, mec="black", mfc="white",
        label="量測資料", zorder=5)
ax.plot(t_smooth, model_A(t_smooth, *pA), lw=2.2, color="#1f77b4",
        label="Model A")
ax.plot(t_smooth, model_B(t_smooth, *pB), lw=2.2, color="#d62728",
        label="Model B")
ax.plot(t_smooth, model_C(t_smooth, *pC), lw=2.2, color="#2ca02c",
        label="Model C")
ax.axvspan(t_data.min(), t_data.max(), color="#eee", alpha=0.5)
ax.axvline(t_target, ls="--", color="#888", alpha=0.6, lw=1.5)
ax.plot(t_target, predA, "^", ms=11, color="#1f77b4", zorder=6)
ax.plot(t_target, predB, "s", ms=11, color="#d62728", zorder=6)
ax.plot(t_target, predC, "v", ms=11, color="#2ca02c", zorder=6)

ax.annotate(fr"$B_A(150)={predA:.2f}$",
            (t_target, predA), xytext=(-95, 5), textcoords="offset points",
            color="#1f77b4", fontsize=10, fontweight="bold")
ax.annotate(fr"$B_B(150)={predB:.2f}$",
            (t_target, predB), xytext=(-95, -2), textcoords="offset points",
            color="#d62728", fontsize=10, fontweight="bold")
ax.annotate(fr"$B_C(150)={predC:.2f}$",
            (t_target, predC), xytext=(-95, -10), textcoords="offset points",
            color="#2ca02c", fontsize=10, fontweight="bold")

# Auto y-limit based on max prediction
y_top = max(predA, predB, predC) * 1.1
y_top = max(y_top, 7.0)
ax.set_xlim(0, 165)
ax.set_ylim(-0.5, y_top)
ax.set_xlabel("Time (days)")
ax.set_ylabel(r"Biomass (mm²)")
ax.set_title("外推到 t=150:Model B 起飛,A、C 平穩")
ax.grid(True, alpha=0.3)
ax.legend(loc="upper left", fontsize=9)

fig.suptitle("藻類生物量曲線:三個模型的擬合與外推",
             fontsize=14, fontweight="bold", y=1.01)
fig.tight_layout()
fig.savefig(OUTDIR / "fig1_model_compare.png", dpi=150, bbox_inches="tight")
print(f"\nWrote {OUTDIR / 'fig1_model_compare.png'}")
