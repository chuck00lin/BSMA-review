"""Time series of p(t) and A(t) after the hormone step H: 1 → 10.

Model:
    dp/dt = k1 * H * (1 - p)  -  A * p
    dA/dt = e * (H - A)
with k1 = 0.5, e = 0.1.

Initial condition is the equilibrium at H=1:  (p, A) = (1/3, 1).
At t=0 we step H from 1 to 10 and integrate forward.

What the figure shows:
  Two stacked panels:
    Top  — p(t):  sharp spike from 1/3 up to ~5/6, then slow decay back to 1/3.
    Bot  — A(t):  slow first-order tracking of the new H=10 set point.
  We annotate the spike height (k1·H/(k1·H + A_initial)) and the new equilibrium.

Output: fig1_time_series.png next to this file.
"""
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import font_manager
from scipy.integrate import solve_ivp

OUTDIR = Path(__file__).parent
plt.rcParams["axes.unicode_minus"] = False

cjk_candidates = ["Noto Sans CJK TC", "Noto Sans CJK SC", "Noto Sans CJK JP"]
available = {f.name for f in font_manager.fontManager.ttflist}
cjk_font = next((c for c in cjk_candidates if c in available), None)
if cjk_font:
    plt.rcParams["font.family"] = cjk_font


K1 = 0.5
E = 0.1
H_NEW = 10.0
H_OLD = 1.0


def rhs(_t, y):
    p, A = y
    return [K1 * H_NEW * (1 - p) - A * p,
            E * (H_NEW - A)]


# Equilibrium under H_OLD = 1
p0 = 1.0 / 3.0
A0 = H_OLD  # = 1

t_end = 80.0
t_eval = np.linspace(0, t_end, 4000)
sol = solve_ivp(rhs, (0, t_end), [p0, A0], t_eval=t_eval,
                rtol=1e-9, atol=1e-12, max_step=0.05)

p_traj = sol.y[0]
A_traj = sol.y[1]

# Peak height (instantaneous quasi-steady estimate while A ~ A0)
p_peak_estimate = K1 * H_NEW / (K1 * H_NEW + A0)
p_eq_new = K1 / (1 + K1)
A_eq_new = H_NEW

fig, axes = plt.subplots(2, 1, figsize=(8.5, 6.2), sharex=True)

# Panel 1: p(t)
ax = axes[0]
ax.plot(sol.t, p_traj, lw=2.2, color="#d62728", label=r"$p(t)$")
ax.axhline(p_eq_new, ls="--", color="black", alpha=0.5,
           label=fr"$p^* = k_1/(1+k_1) = {p_eq_new:.3f}$")
ax.axhline(p_peak_estimate, ls=":", color="#888", alpha=0.7,
           label=fr"快速階段預估峰值 $\approx {p_peak_estimate:.3f}$")
ax.set_ylabel(r"$p$  (受器結合比例)")
ax.legend(fontsize=9, loc="center right")
ax.grid(True, alpha=0.3)
ax.set_title(r"H 從 1 階躍到 10:p 暴衝 → 適應 → 回到原平衡")

# Panel 2: A(t)
ax = axes[1]
ax.plot(sol.t, A_traj, lw=2.2, color="#1f77b4", label=r"$A(t)$")
ax.axhline(A_eq_new, ls="--", color="black", alpha=0.5,
           label=fr"$A^* = H = {A_eq_new:.0f}$")
ax.axhline(A0, ls=":", color="#888", alpha=0.7,
           label=fr"初始 $A_0 = {A0:.0f}$")

# Mark the e-folding (1/e of remaining gap) at t = 1/e = 10
target_efold = A0 + (A_eq_new - A0) * (1 - np.exp(-1))
ax.plot(1.0 / E, target_efold, "o", ms=8, color="#1f77b4")
ax.annotate(fr"$t = 1/e = {1/E:.0f}$ (走完一個時間常數)",
            xy=(1.0 / E, target_efold), xytext=(20, 5),
            fontsize=9, color="#1f77b4",
            arrowprops=dict(arrowstyle="->", color="#1f77b4", alpha=0.6))

ax.set_ylabel(r"$A$  (受器解離率)")
ax.set_xlabel(r"$t$")
ax.legend(fontsize=9, loc="center right")
ax.grid(True, alpha=0.3)

fig.tight_layout()
fig.savefig(OUTDIR / "fig1_time_series.png", dpi=150, bbox_inches="tight")
print(f"Wrote {OUTDIR / 'fig1_time_series.png'}")
