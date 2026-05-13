"""Helper figures for Ch 03 — 該不該介入?(SIR + R₀).

Helpers:
  1. Compartment diagram — three boxes S→I→R, with flow labels and a
     legend explaining β, γ.
  2. Three scenarios time series — same initial condition (1 infected
     in a 1000-person population) under R₀ = 0.8, 1.2, 3.0.  Each panel
     plots S(t), I(t), R(t) so the student can see "qualitatively
     different outcomes" emerging just from changing β.
  3. Final-size curve — z = R(∞)/N as a function of R₀, solved
     numerically from 1 - z = exp(-R₀·z).  Marks five named diseases.
  4. Intervention diagram — final size as a function of vaccination
     coverage v, for several R₀.  Each curve plummets to 0 once v
     crosses the herd-immunity threshold v_c = 1 - 1/R₀.

All four are written next to this script as PNGs at 150 dpi.
"""
from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyArrowPatch
from matplotlib import font_manager
import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import brentq

OUTDIR = Path(__file__).parent
plt.rcParams["axes.unicode_minus"] = False

cjk_candidates = ["Noto Sans CJK TC", "Noto Sans CJK SC", "Noto Sans CJK JP"]
available = {f.name for f in font_manager.fontManager.ttflist}
cjk_font = next((c for c in cjk_candidates if c in available), None)
if cjk_font:
    plt.rcParams["font.family"] = cjk_font


# ----------------------------------------------------------------------------
# Helper 1: SIR compartment diagram
# ----------------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(11, 4.6))
ax.set_xlim(0, 12)
ax.set_ylim(0, 5)
ax.axis("off")


def draw_box(x, y, w, h, top, sub, color):
    box = mpatches.FancyBboxPatch((x, y), w, h,
                                  boxstyle="round,pad=0.08,rounding_size=0.25",
                                  fc=color, ec="black", lw=2.0)
    ax.add_patch(box)
    ax.text(x + w / 2, y + h * 0.62, top, ha="center", va="center",
            fontsize=22, fontweight="bold")
    ax.text(x + w / 2, y + h * 0.28, sub, ha="center", va="center",
            fontsize=11, style="italic")


draw_box(0.6, 1.5, 2.6, 2.0, "S", "可感受 Susceptible", "#cfe2ff")
draw_box(4.7, 1.5, 2.6, 2.0, "I", "感染中 Infectious",  "#ffd4d4")
draw_box(8.8, 1.5, 2.6, 2.0, "R", "已恢復 Recovered",   "#d4f4d4")


def arrow(xy1, xy2, label, label_xy, color="black"):
    ar = FancyArrowPatch(xy1, xy2, arrowstyle="-|>",
                         mutation_scale=22, lw=2.5, color=color)
    ax.add_patch(ar)
    ax.text(label_xy[0], label_xy[1], label, fontsize=13, color=color,
            ha="center", va="center", fontweight="bold",
            bbox=dict(boxstyle="round,pad=0.25", fc="white", ec="none",
                      alpha=0.9))


arrow((3.2, 2.5), (4.7, 2.5), r"$\beta\,S\,I/N$", (3.95, 2.95), "#a44")
arrow((7.3, 2.5), (8.8, 2.5), r"$\gamma\,I$",     (8.05, 2.95), "#444")

ax.text(6.0, 4.55, "SIR compartment model", ha="center", va="center",
        fontsize=15, fontweight="bold")
ax.text(6.0, 0.5,
        r"$\beta$ = transmission rate (mass action with $S \cdot I$)  ·  "
        r"$\gamma$ = recovery rate (per capita)  ·  "
        r"$N = S+I+R$ 守恆",
        ha="center", va="center", fontsize=10,
        bbox=dict(boxstyle="round,pad=0.4", fc="#fafafa", ec="#aaa"))

fig.tight_layout()
fig.savefig(OUTDIR / "fig1_compartment.png", dpi=150, bbox_inches="tight")
plt.close(fig)
print("Wrote fig1_compartment.png")


# ----------------------------------------------------------------------------
# Helper 2: three scenarios time series
# ----------------------------------------------------------------------------
def sir(t, y, beta, gamma, N):
    S, I, R = y
    dS = -beta * S * I / N
    dI =  beta * S * I / N - gamma * I
    dR =  gamma * I
    return [dS, dI, dR]


N = 1000.0
I0 = 1.0
y0 = [N - I0, I0, 0.0]
gamma = 0.25

scenarios = [
    ("A. 自熄  $R_0 = 0.8$", 0.20, "#4477aa"),
    ("B. 小流行 $R_0 = 1.2$", 0.30, "#cc8800"),
    ("C. 大爆發 $R_0 = 3.0$", 0.75, "#bb3322"),
]

fig, axes = plt.subplots(1, 3, figsize=(15, 4.6), sharey=True)
for ax, (title, beta, accent) in zip(axes, scenarios):
    t_eval = np.linspace(0, 120, 1500)
    sol = solve_ivp(sir, (0, 120), y0, args=(beta, gamma, N),
                    t_eval=t_eval, rtol=1e-9, atol=1e-12, max_step=0.2)
    ax.plot(sol.t, sol.y[0], lw=2.0, color="#1f77b4", label="S")
    ax.plot(sol.t, sol.y[1], lw=2.4, color="#d62728", label="I")
    ax.plot(sol.t, sol.y[2], lw=2.0, color="#2ca02c", label="R")

    R0 = beta / gamma
    # If R0>1, mark the peak.
    if R0 > 1:
        i_peak = int(np.argmax(sol.y[1]))
        ax.plot(sol.t[i_peak], sol.y[1][i_peak], "o", ms=11,
                mec="black", mfc="white", zorder=5)
        ax.annotate(fr"peak: $S={sol.y[0][i_peak]:.0f}$"
                    + fr", $I={sol.y[1][i_peak]:.0f}$",
                    (sol.t[i_peak], sol.y[1][i_peak]),
                    xytext=(8, 14), textcoords="offset points",
                    fontsize=9, color=accent,
                    arrowprops=dict(arrowstyle="->", color=accent))
    # Final size annotation
    z = sol.y[2][-1] / N
    ax.axhline(N * z, ls=":", color="#666", alpha=0.5)
    ax.text(115, N * z + 25, f"final R/N = {z*100:.0f}%",
            ha="right", fontsize=9, color="#444")

    ax.set_title(title, fontsize=11)
    ax.set_xlabel("時間 (day)")
    ax.grid(True, alpha=0.3)
    ax.set_xlim(0, 120)
    ax.set_ylim(0, 1050)
    ax.legend(loc="center right", fontsize=9)

axes[0].set_ylabel("人數")
fig.suptitle(r"相同初值 ($N=1000,\; I_0=1$),不同 $R_0$ → 結果天差地別",
             fontsize=13, y=1.02, fontweight="bold")
fig.tight_layout()
fig.savefig(OUTDIR / "fig2_three_scenarios.png", dpi=150,
            bbox_inches="tight")
plt.close(fig)
print("Wrote fig2_three_scenarios.png")


# ----------------------------------------------------------------------------
# Helper 3: final size curve  1 - z = exp(-R0 · z)
# ----------------------------------------------------------------------------
def final_size(R0):
    # R0 ≤ 1: only the z=0 root (no epidemic); below tiny threshold the
    # nontrivial root is in the floating-point noise floor — treat as 0.
    if R0 <= 1.0 + 1e-4:
        return 0.0
    f = lambda z: 1.0 - z - np.exp(-R0 * z)
    return brentq(f, 1e-4, 1.0 - 1e-9)


R0_grid = np.linspace(0.01, 18, 600)
z_grid = np.array([final_size(R) for R in R0_grid])

fig, ax = plt.subplots(figsize=(9.0, 5.6))
ax.fill_between(R0_grid, 0, z_grid, color="#ffcccc", alpha=0.55)
ax.plot(R0_grid, z_grid, lw=2.6, color="#bb3322")

# Vertical threshold line at R0 = 1
ax.axvline(1.0, ls="--", color="black", alpha=0.7)
ax.text(1.05, 0.05, r"$R_0 = 1$ 門檻",
        fontsize=11, fontweight="bold", color="black")

# Marker for named diseases
diseases = [
    ("流感", 1.5),
    ("COVID Wuhan", 2.5),
    ("COVID Omicron", 8.0),
    ("天花", 6.0),
    ("麻疹", 15.0),
]
for name, R in diseases:
    z = final_size(R)
    ax.plot(R, z, "o", ms=10, mec="black", mfc="white", zorder=5)
    ax.annotate(name + fr" ($R_0={R}$)" + "\n"
                + f"final = {z*100:.0f}%",
                (R, z), xytext=(6, -22), textcoords="offset points",
                fontsize=9, color="#333")

ax.set_xlim(0, 18)
ax.set_ylim(0, 1.05)
ax.set_xlabel(r"$R_0$")
ax.set_ylabel(r"終局感染比例 $z = R(\infty)/N$")
ax.set_title(r"終局規模:$R_0$ 一過 1 就橫掃大半")
ax.grid(True, alpha=0.3)
ax.text(13, 0.35,
        r"final size equation:" + "\n"
        + r"$1 - z = e^{-R_0\, z}$",
        fontsize=12, color="#444",
        bbox=dict(boxstyle="round,pad=0.4", fc="#fff", ec="#aaa"))

fig.tight_layout()
fig.savefig(OUTDIR / "fig3_final_size.png", dpi=150, bbox_inches="tight")
plt.close(fig)
print("Wrote fig3_final_size.png")


# ----------------------------------------------------------------------------
# Helper 4: vaccination coverage vs final epidemic size
# ----------------------------------------------------------------------------
v_grid = np.linspace(0.0, 1.0, 400)
R0_show = [1.5, 2.5, 3.5, 5.0]
colors = ["#4477aa", "#bb3322", "#229922", "#aa44aa"]

fig, ax = plt.subplots(figsize=(9.0, 5.6))
for R0, c in zip(R0_show, colors):
    # Effective R0 after fraction v vaccinated.
    R_eff = R0 * (1.0 - v_grid)
    # Final size: among the unvaccinated only.
    z_unvac = np.array([final_size(R) for R in R_eff])
    # Convert to fraction of total population infected.
    z_total = (1.0 - v_grid) * z_unvac
    ax.plot(v_grid, z_total, lw=2.4, color=c, label=fr"$R_0 = {R0}$")
    # Mark herd-immunity threshold v_c = 1 - 1/R0
    v_c = 1.0 - 1.0 / R0
    ax.axvline(v_c, ls=":", color=c, alpha=0.7)
    ax.text(v_c, 1.02, fr"$v_c={v_c:.2f}$",
            ha="center", va="bottom", fontsize=9, color=c)

ax.set_xlim(0, 1.02)
ax.set_ylim(0, 1.1)
ax.set_xlabel("疫苗覆蓋率 $v$")
ax.set_ylabel("終局感染比例(占全人口)")
ax.set_title("介入:每個 $R_0$ 都有自己的 herd-immunity 門檻")
ax.grid(True, alpha=0.3)
ax.legend(loc="upper right", fontsize=10)
ax.text(0.04, 0.92,
        r"$v_c = 1 - \dfrac{1}{R_0}$" + "\n"
        + r"門檻越右,代表 $R_0$ 越大、需要的疫苗覆蓋率越高",
        fontsize=10, color="#444",
        bbox=dict(boxstyle="round,pad=0.4", fc="#fff", ec="#aaa"))

fig.tight_layout()
fig.savefig(OUTDIR / "fig4_intervention.png", dpi=150, bbox_inches="tight")
plt.close(fig)
print("Wrote fig4_intervention.png")
