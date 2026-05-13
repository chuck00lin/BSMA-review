"""Numerical simulations of the 3-compartment lead-flow model.

Model:
    dx1/dt = -(k01 + k21 + k31)*x1 + k12*x2 + k13*x3 + I1
    dx2/dt =  k21*x1            - (k02 + k12)*x2
    dx3/dt =  k31*x1            -  k13*x3

Parameters (μg/day for I1, day^-1 for k's):
    I1 = 49.3
    k01 = 0.0211,  k21 = 0.0111,  k31 = 0.0039
    k02 = 0.0162,  k12 = 0.0124,  k13 = 0.000035

We integrate for both initial conditions, on two time horizons,
and lay out a 2×2 panel:

         ┌── 800 days ────┬── 8000 days ───┐
    IC1  │  fast plateau  │  bones climb   │
         ├────────────────┼────────────────┤
    IC2  │  tissue decays │  bones climb   │
         └────────────────┴────────────────┘

Linear y-axis is fine for the 800-day panels (blood/tissue range).
The 8000-day panels need log y (bones go from 0 to ≈100,000 μg
in 8000 days, well beyond the blood/tissue scale).

We also print the analytic equilibrium for reference.

Output: fig2_simulations.png next to this file.
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


# Parameters
I1 = 49.3
k01, k21, k31 = 0.0211, 0.0111, 0.0039
k02, k12, k13 = 0.0162, 0.0124, 0.000035


def rhs(_t, x):
    x1, x2, x3 = x
    return [
        -(k01 + k21 + k31) * x1 + k12 * x2 + k13 * x3 + I1,
        k21 * x1 - (k02 + k12) * x2,
        k31 * x1 - k13 * x3,
    ]


# Analytic equilibrium --------------------------------------------------------
x1_eq = I1 / (k01 + k21 * k02 / (k02 + k12))
x2_eq = k21 * x1_eq / (k02 + k12)
x3_eq = k31 * x1_eq / k13
print(f"Equilibrium:  x1*={x1_eq:.1f}  x2*={x2_eq:.1f}  x3*={x3_eq:.1f}")

# Simulations -----------------------------------------------------------------
ICs = [("IC1: 全部 = 0", [0.0, 0.0, 0.0]),
       ("IC2: 全部 = 1800", [1800.0, 1800.0, 1800.0])]
horizons = [800, 8000]

colors = {"x1": "#d62728", "x2": "#1f77b4", "x3": "#8c564b"}
labels_cn = {"x1": r"$x_1$ blood", "x2": r"$x_2$ tissues",
             "x3": r"$x_3$ bones"}

fig, axes = plt.subplots(2, 2, figsize=(13, 8.0))

for row, (ic_name, ic) in enumerate(ICs):
    for col, T in enumerate(horizons):
        ax = axes[row, col]
        t_eval = np.linspace(0, T, 2000)
        sol = solve_ivp(rhs, (0, T), ic, t_eval=t_eval,
                        rtol=1e-9, atol=1e-12, max_step=2.0)
        for i, key in enumerate(["x1", "x2", "x3"]):
            ax.plot(sol.t, sol.y[i], lw=2.0, color=colors[key],
                    label=labels_cn[key])
        # Equilibrium horizontal lines
        for eq, key in zip([x1_eq, x2_eq, x3_eq], ["x1", "x2", "x3"]):
            ax.axhline(eq, ls=":", color=colors[key], alpha=0.5, lw=1.2)

        ax.set_title(f"{ic_name}  ·  {T} days", fontsize=11)
        ax.set_xlabel("time (days)")
        ax.set_ylabel(r"lead amount ($\mu$g)")
        ax.grid(True, alpha=0.3)

        if T == 8000:
            ax.set_yscale("log")
            ax.set_ylim(0.5, 5e5)
        else:
            ax.set_ylim(-100, 3200)

        ax.legend(loc="lower right", fontsize=9, framealpha=0.9)

# Annotate the equilibrium asymptote on the long-horizon panels
for col_T, ax in zip([800, 8000], [axes[1, 0], axes[1, 1]]):
    if col_T == 8000:
        ax.annotate(fr"$x_3^* \approx {x3_eq:.0f}\,\mu$g"
                    + "\n(54 年才能達到)",
                    xy=(7500, x3_eq), xytext=(4000, x3_eq * 0.4),
                    color="#8c564b", fontsize=10,
                    arrowprops=dict(arrowstyle="->", color="#8c564b"))

fig.suptitle("鉛三隔室模型:兩個初值、兩個時間尺度",
             fontsize=14, fontweight="bold", y=1.01)
fig.tight_layout()
fig.savefig(OUTDIR / "fig2_simulations.png", dpi=150, bbox_inches="tight")
print(f"Wrote {OUTDIR / 'fig2_simulations.png'}")
