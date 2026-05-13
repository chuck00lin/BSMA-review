"""Time evolution of the dimensionless plant-herbivore model.

We integrate

    du/dτ = β − γ u (v − 1)
    dv/dτ = v (1 − v/u)

forward in dimensionless time τ from a few initial conditions, and plot
u(τ) and v(τ) on a shared time axis (two stacked panels).

The point is to make the convergence to (u*, v*) visible — and to show
the characteristic damped oscillation (focus-type fixed point) when β/γ
is moderately large.

Output: fig2_time_series.png next to this file.
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


def rhs(_t, y, beta, gamma):
    u, v = y
    du = beta - gamma * u * (v - 1.0)
    dv = v * (1.0 - v / u) if u > 0 else 0.0
    return [du, dv]


BETA, GAMMA = 2.0, 1.0
u_star = 0.5 * (1.0 + np.sqrt(1.0 + 4.0 * BETA / GAMMA))
v_star = u_star

t_end = 30.0
t_eval = np.linspace(0, t_end, 1500)

# Three initial conditions: low/high quality, low/high herbivore density.
ICs = [
    (0.5, 0.5, "起點:低 q、低 I"),
    (3.5, 0.5, "起點:高 q、低 I"),
    (0.5, 3.5, "起點:低 q、高 I"),
]
colors = ["#2ca02c", "#ff7f0e", "#9467bd"]

fig, axes = plt.subplots(2, 1, figsize=(8.5, 6.0), sharex=True)

for ic, color, label in zip(ICs, colors, [t[2] for t in ICs]):
    sol = solve_ivp(rhs, (0, t_end), ic[:2], args=(BETA, GAMMA),
                    t_eval=t_eval, rtol=1e-8, atol=1e-10, max_step=0.05)
    axes[0].plot(sol.t, sol.y[0], lw=1.8, color=color, label=label)
    axes[1].plot(sol.t, sol.y[1], lw=1.8, color=color)

# Equilibrium reference lines
for ax, eq, name in zip(axes, (u_star, v_star), ("u^*", "v^*")):
    ax.axhline(eq, ls="--", color="black", alpha=0.4,
               label=fr"${name}={eq:.2f}$")
    ax.grid(True, alpha=0.3)

axes[0].set_ylabel(r"$u(\tau) = q/(K_4 I_0)$")
axes[0].set_title(fr"Dimensionless time evolution  (β={BETA}, γ={GAMMA})")
axes[0].legend(fontsize=9, ncol=2, loc="upper right")

axes[1].set_ylabel(r"$v(\tau) = I/I_0$")
axes[1].set_xlabel(r"$\tau = K_3\, t$")
axes[1].legend(fontsize=9, loc="upper right")

fig.tight_layout()
fig.savefig(OUTDIR / "fig2_time_series.png", dpi=150, bbox_inches="tight")
print(f"Wrote {OUTDIR / 'fig2_time_series.png'}")
