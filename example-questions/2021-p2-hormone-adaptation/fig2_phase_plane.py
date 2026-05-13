"""Phase-plane trajectory of (p, A) after the step H: 1 → 10.

Model:
    dp/dt = k1 H (1 − p) − A p
    dA/dt = e (H − A)
with k1 = 0.5, e = 0.1, H = 10 after the step.

Trajectory starts at the old equilibrium (1/3, 1) and ends at the new
equilibrium (1/3, 10).  Because e ≪ k1·H, the trajectory has a clear
"L" shape: nearly horizontal first (fast spike in p), then almost
vertical (slow climb of A while p drifts back to 1/3).

We overlay:
  - the p-nullcline (dp/dt = 0): A = k1 H (1−p)/p
  - the A-nullcline (dA/dt = 0): A = H = 10  (a horizontal line)
  - the equilibrium intersection at (1/3, 10)
  - markers at t = 0, t = 1, t = 5, t = 20 to make the speed change explicit

Output: fig2_phase_plane.png next to this file.
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


def rhs(_t, y):
    p, A = y
    return [K1 * H_NEW * (1 - p) - A * p,
            E * (H_NEW - A)]


t_end = 80.0
sol = solve_ivp(rhs, (0, t_end), [1/3, 1.0],
                t_eval=np.linspace(0, t_end, 5000),
                rtol=1e-10, atol=1e-13, max_step=0.02)

p_traj = sol.y[0]
A_traj = sol.y[1]

fig, ax = plt.subplots(figsize=(8.0, 6.5))

# Nullclines -----------------------------------------------------------------
p_grid = np.linspace(0.02, 0.99, 400)
p_nullcline_A = K1 * H_NEW * (1 - p_grid) / p_grid  # dp/dt=0
ax.plot(p_grid, p_nullcline_A, lw=2.0, color="#d62728",
        label=r"$p$-nullcline: $A = k_1 H (1-p)/p$")
ax.axhline(H_NEW, lw=2.0, color="#1f77b4",
           label=fr"$A$-nullcline: $A = H = {H_NEW:.0f}$")

# Trajectory
ax.plot(p_traj, A_traj, lw=2.4, color="#2ca02c", alpha=0.95,
        label="軌跡 $(p(t), A(t))$")

# Time markers
mark_times = [0.0, 1.0, 5.0, 15.0, 40.0]
for tmk in mark_times:
    idx = np.argmin(np.abs(sol.t - tmk))
    ax.plot(p_traj[idx], A_traj[idx], "o", ms=9,
            mec="black", mfc="white", zorder=5)
    ax.annotate(f"t={tmk:g}", (p_traj[idx], A_traj[idx]),
                xytext=(7, 6), textcoords="offset points",
                fontsize=9, color="black")

# Equilibria
ax.plot(1/3, 1, "s", ms=11, mec="black", mfc="#aaa", zorder=6,
        label=r"舊平衡 $(1/3, 1)$")
ax.plot(1/3, H_NEW, "o", ms=13, mec="black", mfc="gold", zorder=6,
        label=r"新平衡 $(1/3, 10)$")

# Arrows along trajectory to show time direction
for tmk in [0.3, 3.0, 25.0]:
    idx = np.argmin(np.abs(sol.t - tmk))
    if idx < len(sol.t) - 5:
        dp = p_traj[idx + 5] - p_traj[idx]
        dA = A_traj[idx + 5] - A_traj[idx]
        ax.annotate("", xy=(p_traj[idx] + dp, A_traj[idx] + dA),
                    xytext=(p_traj[idx], A_traj[idx]),
                    arrowprops=dict(arrowstyle="->", lw=2.4, color="#2ca02c"))

ax.set_xlabel(r"$p$  (受器結合比例)")
ax.set_ylabel(r"$A$  (受器解離率)")
ax.set_xlim(0, 1)
ax.set_ylim(0, 12)
ax.grid(True, alpha=0.3)
ax.legend(loc="upper right", fontsize=9, framealpha=0.92)
ax.set_title("Phase plane:H 階躍後的「快結合 → 慢適應」L 形軌跡")

# Phase highlights
ax.annotate("快階段:p 快速衝右\n($A$ 還來不及動)",
            xy=(0.65, 1.5), fontsize=9, color="#444",
            bbox=dict(boxstyle="round,pad=0.3", fc="#efe", ec="#888"))
ax.annotate("慢階段:$A$ 爬升,\n把 $p$ 拉回 $1/3$",
            xy=(0.55, 7.0), fontsize=9, color="#444",
            bbox=dict(boxstyle="round,pad=0.3", fc="#eef", ec="#888"))

fig.tight_layout()
fig.savefig(OUTDIR / "fig2_phase_plane.png", dpi=150, bbox_inches="tight")
print(f"Wrote {OUTDIR / 'fig2_phase_plane.png'}")
