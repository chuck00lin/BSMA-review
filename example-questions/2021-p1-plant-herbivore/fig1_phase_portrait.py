"""Phase portrait of the dimensionless plant-herbivore model.

This figure illustrates the qualitative behaviour of the system

    du/dτ = β − γ u (v − 1)
    dv/dτ = v (1 − v/u)

with u ≡ q / (K4·I0)  (rescaled plant quality)
     v ≡ I / I0       (rescaled herbivore density)
     τ ≡ K3·t         (rescaled time)
     β = K1 / (K3·K4·I0)
     γ = K2·I0 / K3

What we draw on the phase plane (u on x, v on y):
  - The two v-nullclines:  v = 0  and  v = u  (the 45° line).
  - The u-nullcline: u·(v−1) = β/γ,   i.e.  v = 1 + (β/γ)/u
    (only defined for u > 0; it asymptotes to v = 1 as u → ∞).
  - The equilibrium point (u*, v*) with v* = u* and γu² − γu − β = 0.
  - A vector field of the flow, plus a couple of integrated trajectories
    so the reader can see them spiral / settle onto the fixed point.

Output: fig1_phase_portrait.png next to this file.
"""
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import font_manager
from scipy.integrate import solve_ivp

OUTDIR = Path(__file__).parent
plt.rcParams["axes.unicode_minus"] = False

# CJK font (so Chinese annotations render if needed) ---------------------------
cjk_candidates = ["Noto Sans CJK TC", "Noto Sans CJK SC", "Noto Sans CJK JP"]
available = {f.name for f in font_manager.fontManager.ttflist}
cjk_font = next((c for c in cjk_candidates if c in available), None)
if cjk_font:
    plt.rcParams["font.family"] = cjk_font


# Model -----------------------------------------------------------------------
def rhs(_t, y, beta, gamma):
    """Right-hand side of the dimensionless plant-herbivore ODEs."""
    u, v = y
    du = beta - gamma * u * (v - 1.0)
    dv = v * (1.0 - v / u) if u > 0 else 0.0
    return [du, dv]


# Pick a representative (β, γ). Choose something that gives a clear focus.
BETA, GAMMA = 2.0, 1.0

# Equilibrium: γ u² − γ u − β = 0 → u* = (1 + sqrt(1 + 4β/γ))/2
u_star = 0.5 * (1.0 + np.sqrt(1.0 + 4.0 * BETA / GAMMA))
v_star = u_star

# Grid for vector field --------------------------------------------------------
u_max = 4.0
v_max = 4.0
U, V = np.meshgrid(np.linspace(0.05, u_max, 22), np.linspace(0.05, v_max, 22))
DU = BETA - GAMMA * U * (V - 1.0)
DV = V * (1.0 - V / U)
# Normalise arrow lengths so direction is visible.
M = np.sqrt(DU**2 + DV**2)
M[M == 0] = 1.0
DUn, DVn = DU / M, DV / M

fig, ax = plt.subplots(figsize=(7.5, 6.5))

# Vector field
ax.quiver(U, V, DUn, DVn, M, cmap="Greys", scale=30, width=0.0035, alpha=0.7)

# Nullclines -------------------------------------------------------------------
u_line = np.linspace(0.05, u_max, 400)

# v-nullcline: v = u  (the diagonal)
ax.plot(u_line, u_line, lw=2.2, color="#1f77b4",
        label=r"$v$-nullcline: $v=u$")

# v-nullcline: v = 0 (x-axis); we just mark the axis
ax.axhline(0.0, lw=1.2, ls=":", color="#1f77b4", alpha=0.6)

# u-nullcline: v = 1 + (β/γ)/u
v_unull = 1.0 + (BETA / GAMMA) / u_line
ax.plot(u_line, v_unull, lw=2.2, color="#d62728",
        label=r"$u$-nullcline: $v=1+\frac{\beta/\gamma}{u}$")

# Equilibrium point
ax.plot(u_star, v_star, "o", ms=12, mec="black", mfc="gold", zorder=5,
        label=fr"equilibrium $(u^*,v^*)=({u_star:.2f},{v_star:.2f})$")

# A few trajectories integrated forward in τ
trajectory_ICs = [(0.3, 0.3), (3.5, 0.5), (0.5, 3.5), (3.5, 3.5)]
colors = ["#2ca02c", "#9467bd", "#ff7f0e", "#17becf"]
for ic, c in zip(trajectory_ICs, colors):
    sol = solve_ivp(rhs, (0, 30), ic, args=(BETA, GAMMA),
                    dense_output=True, rtol=1e-7, atol=1e-9, max_step=0.1)
    ax.plot(sol.y[0], sol.y[1], lw=1.6, color=c, alpha=0.9)
    ax.plot(ic[0], ic[1], "s", ms=6, color=c)

ax.set_xlabel(r"$u = q/(K_4 I_0)$  (無因次植物品質)")
ax.set_ylabel(r"$v = I/I_0$  (無因次食草者密度)")
ax.set_title(fr"Phase portrait  (β = {BETA}, γ = {GAMMA})")
ax.set_xlim(0, u_max)
ax.set_ylim(0, v_max)
ax.grid(True, alpha=0.3)
ax.legend(loc="upper right", fontsize=9, framealpha=0.92)

# Annotation explaining the layout
ax.annotate("induced defence\n($v<1$ → 提升 $q$)",
            xy=(2.5, 0.6), fontsize=9, color="#444",
            bbox=dict(boxstyle="round,pad=0.3", fc="#eef", ec="#88a"))
ax.annotate("overgrazing\n($v>1$ → 拉低 $q$)",
            xy=(2.5, 3.0), fontsize=9, color="#444",
            bbox=dict(boxstyle="round,pad=0.3", fc="#fee", ec="#a88"))

fig.tight_layout()
fig.savefig(OUTDIR / "fig1_phase_portrait.png", dpi=150, bbox_inches="tight")
print(f"Wrote {OUTDIR / 'fig1_phase_portrait.png'}")
