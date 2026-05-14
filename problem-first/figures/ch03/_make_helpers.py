"""Helper figures for Ch 03 — Q1 穩定還是失控?

Helpers:
  1. Phase line — two panels showing a stable fp (f' < 0) and an unstable
     fp (f' > 0), with flow arrows on the x-axis to make the basin
     structure visible.
  2. Logistic vs Allee — side-by-side phase lines.  Logistic has 2 fps
     (one stable, one unstable).  Allee has 3 fps with a separatrix —
     the "history matters" structure.
  3. SIR threshold — three time series of I(t) on a log scale, for
     R0 = 0.7, 1.0, 1.3.  Visually demonstrates that λ flips sign at
     R0 = 1 — the same I0 → fundamentally different fates.
  4. 2D fixed-point zoo — six small phase portraits showing the
     archetypal 2D fixed-point types: stable/unstable node, saddle,
     stable/unstable spiral, center.

Each helper writes a PNG into the same directory at 150 dpi.
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


# ============================================================================
# Helper 1: phase line for stable vs unstable 1D fp
# ============================================================================
def draw_phase_line(ax, f, x_grid, fp, fp_type, title, xlim):
    y = f(x_grid)
    ax.axhline(0, color="black", lw=0.8)
    ax.plot(x_grid, y, lw=2.2, color="#1f77b4")
    # Mark fp
    color = "#2ca02c" if fp_type == "stable" else "#d62728"
    ax.plot(fp, 0, "o", ms=14, mec="black", mfc=color, zorder=5)
    ax.annotate(fr"$x^\ast={fp}$" + "\n" + f"({fp_type})",
                (fp, 0), xytext=(8, 30 if fp_type == "stable" else -45),
                textcoords="offset points",
                fontsize=11, color=color, fontweight="bold",
                ha="left")

    # Flow arrows on a shifted "x-axis" line below the plot
    y_arrow = ax.get_ylim()[0] * 0.85
    arrow_xs = np.linspace(xlim[0] + 0.1, xlim[1] - 0.1, 9)
    for ax_x in arrow_xs:
        sign = np.sign(f(ax_x))
        if abs(sign) < 1e-6 or abs(ax_x - fp) < 0.05:
            continue
        ax.annotate("", xy=(ax_x + 0.18 * sign, y_arrow),
                    xytext=(ax_x, y_arrow),
                    arrowprops=dict(arrowstyle="->", color="#444", lw=2.0))

    ax.set_xlim(*xlim)
    ax.set_xlabel("$x$")
    ax.set_ylabel(r"$f(x) = \dot{x}$")
    ax.set_title(title)
    ax.grid(True, alpha=0.3)
    ax.text(0.02, 0.95, fr"$f'(x^\ast) = {('-' if fp_type=='stable' else '+')}|f'|$",
            transform=ax.transAxes, fontsize=11, color=color,
            verticalalignment="top",
            bbox=dict(boxstyle="round,pad=0.3", fc="white", ec=color))


fig, axes = plt.subplots(1, 2, figsize=(12, 4.8))

# Stable: f(x) = -2(x - 1)
draw_phase_line(axes[0], lambda x: -2 * (x - 1), np.linspace(-1, 3, 200),
                fp=1.0, fp_type="stable",
                title="Stable fp:箭頭兩邊都指向 $x^\\ast$",
                xlim=(-1, 3))

# Unstable: f(x) = 2(x - 1)
draw_phase_line(axes[1], lambda x: 2 * (x - 1), np.linspace(-1, 3, 200),
                fp=1.0, fp_type="unstable",
                title="Unstable fp:箭頭兩邊都背離 $x^\\ast$",
                xlim=(-1, 3))

fig.suptitle("1D 相線:$f'(x^\\ast)$ 的號數決定穩定性",
             fontsize=13, fontweight="bold", y=1.03)
fig.tight_layout()
fig.savefig(OUTDIR / "fig1_phase_line.png", dpi=150, bbox_inches="tight")
plt.close(fig)
print("Wrote fig1_phase_line.png")


# ============================================================================
# Helper 2: logistic (2 fps) vs Allee (3 fps)
# ============================================================================
fig, axes = plt.subplots(1, 2, figsize=(13, 5.4))

# ---- Logistic ----
N = np.linspace(-0.15, 1.3, 400)
r, K = 1.0, 1.0
f_log = r * N * (1 - N / K)

ax = axes[0]
ax.axhline(0, color="black", lw=0.8)
ax.plot(N, f_log, lw=2.3, color="#1f77b4", label=r"$f(N)=rN(1-N/K)$")
ax.plot(0.0, 0, "o", ms=14, mec="black", mfc="#d62728", zorder=5)
ax.plot(1.0, 0, "o", ms=14, mec="black", mfc="#2ca02c", zorder=5)
ax.annotate("$N^\\ast=0$\n(unstable)", (0, 0), xytext=(15, 30),
            textcoords="offset points", color="#d62728", fontsize=11,
            fontweight="bold")
ax.annotate("$N^\\ast=K$\n(stable)", (1, 0), xytext=(-25, 30),
            textcoords="offset points", color="#2ca02c", fontsize=11,
            fontweight="bold", ha="right")

# Flow arrows
y_arrow = -0.12
for nx in np.linspace(-0.05, 1.25, 11):
    sign = np.sign(r * nx * (1 - nx / K))
    if abs(sign) < 1e-6 or min(abs(nx), abs(nx - 1)) < 0.05:
        continue
    ax.annotate("", xy=(nx + 0.06 * sign, y_arrow), xytext=(nx, y_arrow),
                arrowprops=dict(arrowstyle="->", color="#444", lw=1.8))

ax.set_xlim(-0.15, 1.3)
ax.set_ylim(-0.18, 0.32)
ax.set_xlabel("$N$")
ax.set_ylabel(r"$\dot N$")
ax.set_title("Logistic:2 fp,任何種子都會長")
ax.grid(True, alpha=0.3)

# ---- Allee ----
A_thresh = 0.3
f_allee = r * N * (N / A_thresh - 1) * (1 - N / K)

ax = axes[1]
ax.axhline(0, color="black", lw=0.8)
ax.plot(N, f_allee, lw=2.3, color="#1f77b4",
        label=r"$f(N)=rN(N/A-1)(1-N/K)$")
ax.plot(0.0, 0, "o", ms=14, mec="black", mfc="#2ca02c", zorder=5)
ax.plot(A_thresh, 0, "o", ms=14, mec="black", mfc="#d62728", zorder=5)
ax.plot(1.0, 0, "o", ms=14, mec="black", mfc="#2ca02c", zorder=5)
ax.annotate("$N^\\ast=0$\n(stable)\n滅絕", (0, 0),
            xytext=(15, -55), textcoords="offset points",
            color="#2ca02c", fontsize=10, fontweight="bold")
ax.annotate(f"$N^\\ast=A={A_thresh}$\n(unstable)\nseparatrix",
            (A_thresh, 0), xytext=(15, 30),
            textcoords="offset points", color="#d62728",
            fontsize=10, fontweight="bold")
ax.annotate("$N^\\ast=K$\n(stable)\n殖民", (1, 0),
            xytext=(-25, -55), textcoords="offset points",
            color="#2ca02c", fontsize=10, fontweight="bold", ha="right")

# Flow arrows for Allee
y_arrow = -0.12
for nx in np.linspace(-0.05, 1.25, 13):
    val = r * nx * (nx / A_thresh - 1) * (1 - nx / K)
    sign = np.sign(val)
    if abs(sign) < 1e-6 or min(abs(nx), abs(nx - A_thresh),
                               abs(nx - 1)) < 0.05:
        continue
    ax.annotate("", xy=(nx + 0.06 * sign, y_arrow), xytext=(nx, y_arrow),
                arrowprops=dict(arrowstyle="->", color="#444", lw=1.8))

ax.set_xlim(-0.15, 1.3)
ax.set_ylim(-0.18, 0.32)
ax.set_xlabel("$N$")
ax.set_ylabel(r"$\dot N$")
ax.set_title("Allee:3 fp,初值決定命運")
ax.grid(True, alpha=0.3)

fig.suptitle("從 2 fp 到 3 fp:多平衡點 → 系統有歷史性",
             fontsize=13, fontweight="bold", y=1.02)
fig.tight_layout()
fig.savefig(OUTDIR / "fig2_logistic_vs_allee.png", dpi=150,
            bbox_inches="tight")
plt.close(fig)
print("Wrote fig2_logistic_vs_allee.png")


# ============================================================================
# Helper 3: SIR threshold — log-scale I(t) for three R0 values
# ============================================================================
def sir(t, y, beta, gamma, N):
    S, I, R = y
    return [-beta * S * I / N,
            beta * S * I / N - gamma * I,
            gamma * I]


N_pop = 1000.0
I0 = 1.0
gamma = 0.25
y0 = [N_pop - I0, I0, 0.0]

R0_list = [0.7, 1.0, 1.3]
colors = ["#1f77b4", "#888888", "#d62728"]

fig, ax = plt.subplots(figsize=(9, 5.6))

for R0, c in zip(R0_list, colors):
    beta = R0 * gamma
    t_eval = np.linspace(0, 60, 800)
    sol = solve_ivp(sir, (0, 60), y0, args=(beta, gamma, N_pop),
                    t_eval=t_eval, rtol=1e-10, atol=1e-13, max_step=0.1)
    lam = beta - gamma
    label = (fr"$R_0={R0}$  →  $\lambda=\beta-\gamma={lam:+.3f}$/day")
    ax.semilogy(sol.t, sol.y[1], lw=2.3, color=c, label=label)

# Reference exponential lines (early dynamics)
t_ref = np.linspace(0, 30, 50)
for R0, c in zip(R0_list, colors):
    beta = R0 * gamma
    lam = beta - gamma
    if abs(lam) > 0.01:
        ax.semilogy(t_ref, I0 * np.exp(lam * t_ref), ls=":", color=c,
                    alpha=0.6, lw=1.3)

ax.axhline(I0, color="black", ls="--", alpha=0.4, lw=1)
ax.set_xlabel("時間 (day)")
ax.set_ylabel(r"$I(t)$  (log scale)")
ax.set_title(r"SIR 早期:$R_0$ 跨過 1 → $\lambda$ 號數翻轉 → 命運質變"
             + "\n虛線 = 線性化預測 $I_0\, e^{\lambda t}$")
ax.set_xlim(0, 60)
ax.set_ylim(0.1, 1100)
ax.grid(True, alpha=0.3, which="both")
ax.legend(loc="upper left", fontsize=10)

fig.tight_layout()
fig.savefig(OUTDIR / "fig3_sir_threshold.png", dpi=150,
            bbox_inches="tight")
plt.close(fig)
print("Wrote fig3_sir_threshold.png")


# ============================================================================
# Helper 4: 2D fixed-point zoo
# ============================================================================
fig, axes = plt.subplots(2, 3, figsize=(13.5, 8.5))

# Each entry: (title, J matrix, sample IC list)
zoo = [
    ("Stable node\n(eigvals 實數,皆 < 0)",
     np.array([[-2, 0], [0, -1]]),
     "stable"),
    ("Unstable node\n(eigvals 實數,皆 > 0)",
     np.array([[2, 0], [0, 1]]),
     "unstable"),
    ("Saddle\n(eigvals 實數,一正一負)",
     np.array([[1, 0], [0, -1]]),
     "saddle"),
    ("Stable spiral\n(eigvals 複數,實部 < 0)",
     np.array([[-0.5, -1], [1, -0.5]]),
     "stable"),
    ("Unstable spiral\n(eigvals 複數,實部 > 0)",
     np.array([[0.5, -1], [1, 0.5]]),
     "unstable"),
    ("Center\n(eigvals 純虛 → marginal)",
     np.array([[0, -1], [1, 0]]),
     "center"),
]

for ax, (title, J, kind) in zip(axes.flat, zoo):
    # Stream plot of the linear system  dy/dt = J·y
    xs = np.linspace(-2, 2, 25)
    ys = np.linspace(-2, 2, 25)
    X, Y = np.meshgrid(xs, ys)
    U = J[0, 0] * X + J[0, 1] * Y
    V = J[1, 0] * X + J[1, 1] * Y
    ax.streamplot(X, Y, U, V, color="#888", density=1.0, linewidth=0.9,
                  arrowsize=1.0)

    # A few sample trajectories starting from the periphery
    for theta in np.linspace(0, 2 * np.pi, 8, endpoint=False):
        ic = 1.5 * np.array([np.cos(theta), np.sin(theta)])
        # Integrate forward; for unstable we need short time, for
        # stable longer time so trajectories visibly converge.
        t_end = 8 if kind == "stable" else 4
        sol = solve_ivp(lambda t, z: J @ z, (0, t_end), ic,
                        dense_output=True, rtol=1e-7, atol=1e-9,
                        max_step=0.05)
        ax.plot(sol.y[0], sol.y[1], lw=1.4,
                color="#2ca02c" if kind == "stable"
                else ("#d62728" if kind == "unstable" else "#9467bd"),
                alpha=0.85)

    # Mark fp
    fp_color = ("#2ca02c" if kind == "stable"
                else ("#d62728" if kind == "unstable" else "#9467bd"))
    ax.plot(0, 0, "o", ms=12, mec="black", mfc=fp_color, zorder=5)

    ax.set_xlim(-2, 2)
    ax.set_ylim(-2, 2)
    ax.set_aspect("equal")
    ax.set_title(title, fontsize=10.5)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.grid(False)

fig.suptitle("2D 線性系統 fp 動物園 — 由 Jacobian 特徵值決定類型",
             fontsize=13, fontweight="bold", y=0.99)
fig.tight_layout()
fig.savefig(OUTDIR / "fig4_2d_zoo.png", dpi=150, bbox_inches="tight")
plt.close(fig)
print("Wrote fig4_2d_zoo.png")
