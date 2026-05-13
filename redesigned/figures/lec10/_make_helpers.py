"""Helper illustrations for Lecture 10 — Stochastic Models.

Helpers:
  1. Linear congruential generator + lattice test — a bad LCG (small
     modulus) shows clear stripes in the consecutive-pair scatter; a
     good LCG looks uniformly scattered. Side-by-side comparison so
     the reader sees why lattice tests matter.
  2. Inverse cumulative method walkthrough — empirical CDF on top,
     uniform draw on the y-axis, horizontal arrow over to the CDF,
     then vertical drop to the x-axis showing the sampled deviate.
     Multiple draws produce a histogram matching the original PDF.
  3. Stochastic logistic — three noise levels (sigma = 0.1, 0.44, 1.44
     on K) with five trajectories each, plus deterministic equilibrium
     overlaid. Right panel: histogram of populations after t=30 for
     each noise level so we can see distribution spreads.
  4. Markov chain deer example — the 3-state transition diagram on
     the left (water / grass / sleeping) with arrows weighted by
     probability; on the right, evolution of state probability
     vector p_t for n=1,2,4,16,32 converging to the fixed point.
"""
from pathlib import Path
import matplotlib.pyplot as plt
from matplotlib import font_manager
from matplotlib.patches import FancyArrowPatch, Circle
import numpy as np

OUTDIR = Path(__file__).parent
plt.rcParams["axes.unicode_minus"] = False

cjk_candidates = ["Noto Sans CJK TC", "Noto Sans CJK SC", "Noto Sans CJK JP"]
available = {f.name for f in font_manager.fontManager.ttflist}
cjk_font = next((c for c in cjk_candidates if c in available), None)
if cjk_font:
    plt.rcParams["font.family"] = cjk_font
    print(f"Using CJK font: {cjk_font}")


# ----------------------------------------------------------------------------
# Helper 1: LCG + lattice test (good vs bad generator)
# ----------------------------------------------------------------------------
fig, axes = plt.subplots(1, 3, figsize=(15, 5.0))


def lcg(a, c, m, x0, n):
    out = np.empty(n)
    x = x0
    for i in range(n):
        x = (a * x + c) % m
        out[i] = x / m
    return out


# Bad LCG (RANDU-like): a=65539, c=0, m=2^31 — has notorious 3D structure
# but here we use even worse small-modulus for visible stripes
N = 2000
bad = lcg(a=23, c=0, m=10**5, x0=37, n=N + 1)
good = lcg(a=1103515245, c=12345, m=2**31, x0=42, n=N + 1)

# Left panel: time-series view of a few terms
ax = axes[0]
ax.plot(good[:60], "o-", color="C2", markersize=5, linewidth=1, label="好 LCG")
ax.plot(bad[:60], "s-", color="C3", markersize=5, linewidth=1, label="差 LCG", alpha=0.7)
ax.set_xlabel("序號 i")
ax.set_ylabel("U_i")
ax.set_title("LCG 產生的序列前 60 項\n(看起來都很 uniform)", fontsize=11)
ax.legend(loc="upper right", fontsize=10)
ax.grid(alpha=0.25)

# Middle panel: bad LCG lattice
ax = axes[1]
ax.scatter(bad[:-1], bad[1:], s=3, color="C3", alpha=0.6)
ax.set_xlim(0, 1); ax.set_ylim(0, 1)
ax.set_xlabel("U_i"); ax.set_ylabel("U_{i+1}")
ax.set_title("差 LCG 的 lattice test\n→ 點落在規則的條紋,不是真隨機!",
             fontsize=11)
ax.set_aspect("equal")
ax.grid(alpha=0.25)

# Right panel: good LCG lattice
ax = axes[2]
ax.scatter(good[:-1], good[1:], s=3, color="C2", alpha=0.6)
ax.set_xlim(0, 1); ax.set_ylim(0, 1)
ax.set_xlabel("U_i"); ax.set_ylabel("U_{i+1}")
ax.set_title("好 LCG 的 lattice test\n→ 點均勻散布,合格", fontsize=11)
ax.set_aspect("equal")
ax.grid(alpha=0.25)

fig.suptitle("圖 10-A:線性同餘法 (LCG) 與 lattice test — \n"
             "「序列看起來隨機」不夠,要把(U_i, U_{i+1}) 畫成散點才看得到陷阱",
             fontsize=13, fontweight="bold", y=1.05)
fig.tight_layout()
fig.savefig(OUTDIR / "helper1-lcg-lattice.png", dpi=150, bbox_inches="tight")
plt.close(fig)
print("Wrote helper1-lcg-lattice.png")


# ----------------------------------------------------------------------------
# Helper 2: Inverse cumulative method walkthrough
# ----------------------------------------------------------------------------
fig, axes = plt.subplots(2, 2, figsize=(13, 9.8),
                          gridspec_kw={"height_ratios": [1, 1]})

# Use an asymmetric "lifetime" pdf: gamma(2, 1)
x = np.linspace(0, 8, 500)
from math import factorial
pdf = x * np.exp(-x)  # gamma(2,1)
cdf = 1 - (1 + x) * np.exp(-x)

# Top-left: PDF
ax = axes[0, 0]
ax.fill_between(x, pdf, alpha=0.4, color="C0")
ax.plot(x, pdf, color="C0", linewidth=2)
ax.set_xlabel("x"); ax.set_ylabel("f(x)")
ax.set_title("(a) 我們想抽樣的 pdf f(x) — gamma(2, 1) 為例", fontsize=11)
ax.set_xlim(0, 8); ax.set_ylim(0, 0.42)
ax.grid(alpha=0.25)

# Top-right: CDF with one example draw
ax = axes[0, 1]
ax.plot(x, cdf, color="C0", linewidth=2.4, label="F(x)")
# Pick three uniform draws and project to x
np.random.seed(1)
us = [0.25, 0.55, 0.85]
colors = ["C2", "C3", "C4"]
for u, c in zip(us, colors):
    x_inv = x[np.searchsorted(cdf, u)]
    ax.plot([0, x_inv], [u, u], color=c, linewidth=1.4, linestyle="--")
    ax.plot([x_inv, x_inv], [u, 0], color=c, linewidth=1.4, linestyle="--")
    ax.scatter([0], [u], s=70, color=c, zorder=5)
    ax.scatter([x_inv], [0], s=70, color=c, marker="v", zorder=5)
    ax.text(-0.4, u, f"U={u:.2f}", color=c, fontsize=10, va="center", ha="right")
    ax.text(x_inv, -0.06, f"x={x_inv:.2f}", color=c, fontsize=10,
            ha="center", va="top")
ax.set_xlabel("x"); ax.set_ylabel("F(x) = P(X ≤ x)")
ax.set_title("(b) 逆累積方法 — \n"
             "從 U(0,1) 抽一個 U,水平打到 F,垂直落到 x", fontsize=11)
ax.set_xlim(-0.8, 8); ax.set_ylim(-0.1, 1.05)
ax.grid(alpha=0.25)

# Bottom-left: histogram of many draws
ax = axes[1, 0]
rng = np.random.default_rng(2)
draws_u = rng.uniform(0, 1, 4000)
draws_x = -np.log(rng.uniform(0, 1, 4000)) - np.log(rng.uniform(0, 1, 4000))
# gamma(2,1) = sum of two exp(1) — closed-form inverse via exp
ax.hist(draws_x, bins=60, density=True, color="C0", alpha=0.55,
        label="4000 個抽樣")
ax.plot(x, pdf, color="C3", linewidth=2.2, label="目標 pdf gamma(2,1)")
ax.set_xlabel("x"); ax.set_ylabel("密度")
ax.set_title("(c) 大量重複抽樣後,直方圖貼回原始 pdf", fontsize=11)
ax.set_xlim(0, 10); ax.set_ylim(0, 0.42)
ax.legend(loc="upper right", fontsize=10)
ax.grid(alpha=0.25)

# Bottom-right: algorithm steps
ax = axes[1, 1]
ax.axis("off")
ax.text(0.5, 0.97, "(d) 逆累積方法的 5 個步驟", ha="center", fontsize=13, fontweight="bold")
steps = [
    "1. 寫出你要的 pdf f(x)。",
    "2. 對 f 積分求 cdf:\n     F(x) = ∫ f(t) dt(從 −∞ 到 x)",
    "3. 用 F(−∞) = 0、F(+∞) = 1 定積分常數。",
    "4. 抽一個 U ~ Uniform(0, 1)。",
    "5. 求 x = F^(-1)(U) — 把 F(x) = U 反解出 x。",
]
for i, s in enumerate(steps):
    ax.text(0.05, 0.83 - i * 0.16, s, fontsize=11, va="top")
ax.text(0.5, 0.04,
        "適用:cdf 可以反解時(指數、Cauchy、Weibull、...)\n"
        "對 Normal 一般用 Box–Muller 而不是 F^(-1)",
        ha="center", fontsize=10, color="0.3",
        bbox=dict(boxstyle="round,pad=0.5", facecolor="#fff7d6", edgecolor="0.5"))

fig.suptitle("圖 10-B:Inverse Cumulative Method — 從 uniform 抽樣造出任何分布",
             fontsize=14, fontweight="bold", y=1.0)
fig.tight_layout()
fig.savefig(OUTDIR / "helper2-inverse-cdf.png", dpi=150, bbox_inches="tight")
plt.close(fig)
print("Wrote helper2-inverse-cdf.png")


# ----------------------------------------------------------------------------
# Helper 3: Stochastic logistic — three noise levels
# ----------------------------------------------------------------------------
fig, axes = plt.subplots(1, 4, figsize=(17, 4.6),
                          gridspec_kw={"width_ratios": [1, 1, 1, 0.95]})

dt = 0.05
T = 50
n_steps = int(T / dt)
t = np.arange(n_steps) * dt
K0 = 1.0
V0 = 0.1
n_realizations = 5


def stoch_logistic(sigma, rng):
    V = np.empty(n_steps)
    V[0] = V0
    for i in range(1, n_steps):
        K_now = K0 + rng.normal(0, sigma)
        dV = V[i-1] * (K_now - V[i-1]) * dt
        V[i] = max(0, V[i-1] + dV)
    return V


sigmas = [0.10, 0.44, 1.44]
titles = ["σ = 0.1\n(輕微擾動)", "σ = 0.44\n(中等擾動)", "σ = 1.44\n(強擾動,常造成滅絕)"]
colors_by_sigma = ["C2", "C0", "C3"]

# Collect final distributions for the right panel
final_pops_by_sigma = []
rng_master = np.random.default_rng(11)
for k, (sigma, title, c) in enumerate(zip(sigmas, titles, colors_by_sigma)):
    ax = axes[k]
    finals = []
    for r in range(40):
        traj = stoch_logistic(sigma, rng_master)
        if r < n_realizations:
            ax.plot(t, traj, color=c, linewidth=1.0, alpha=0.55)
        finals.append(traj[-1])
    ax.axhline(K0, color="0.2", linestyle="--", linewidth=1.5, label="K = 1.0 (確定式)")
    ax.set_xlim(0, T); ax.set_ylim(0, 2.4)
    ax.set_xlabel("時間 τ"); ax.set_ylabel("族群 V" if k == 0 else "")
    ax.set_title(title, fontsize=11)
    ax.legend(loc="upper right", fontsize=8.5)
    ax.grid(alpha=0.25)
    final_pops_by_sigma.append(finals)

# Right panel: stacked histogram of final populations
ax = axes[3]
for finals, c, sigma in zip(final_pops_by_sigma, colors_by_sigma, sigmas):
    ax.hist(finals, bins=15, alpha=0.55, color=c,
            label=f"σ={sigma}", edgecolor="0.4", density=True)
ax.axvline(K0, color="0.2", linestyle="--", linewidth=1.5)
ax.set_xlabel("t = 50 時的族群 V")
ax.set_ylabel("出現密度")
ax.set_title("三種雜訊下的長期分布\n(每組 40 次模擬)", fontsize=11)
ax.legend(loc="upper right", fontsize=9.5)
ax.grid(alpha=0.25)
ax.set_xlim(0, 2.5)

fig.suptitle("圖 10-C:隨機 logistic 方程 dV/dτ = V·(K + N(0,σ²) − V) — \n"
             "三種噪聲下,個別軌跡 + 長期分布",
             fontsize=13, fontweight="bold", y=1.05)
fig.tight_layout()
fig.savefig(OUTDIR / "helper3-stochastic-logistic.png", dpi=150, bbox_inches="tight")
plt.close(fig)
print("Wrote helper3-stochastic-logistic.png")


# ----------------------------------------------------------------------------
# Helper 4: Markov chain deer example
# ----------------------------------------------------------------------------
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14.5, 5.6),
                                gridspec_kw={"width_ratios": [1, 1.1]})

# Transition matrix from Table 10.1
P = np.array([
    [0.6, 0.2, 0.2],   # from water
    [0.25, 0.5, 0.25],  # from grass
    [0.25, 0.25, 0.5],  # from sleeping
])
state_names = ["水域", "草地", "睡覺區"]
state_colors = ["#7da9c4", "#a8c97f", "#d3a9c4"]

# Left panel: state transition diagram
ax1.set_xlim(-1.5, 1.5); ax1.set_ylim(-1.3, 1.5)
ax1.set_aspect("equal")
ax1.axis("off")
positions = [(-1.0, 0.7), (1.0, 0.7), (0.0, -0.7)]
radius = 0.32
for (x, y), name, c in zip(positions, state_names, state_colors):
    circ = Circle((x, y), radius, facecolor=c, edgecolor="0.2", linewidth=2)
    ax1.add_patch(circ)
    ax1.text(x, y, name, ha="center", va="center", fontsize=11, fontweight="bold")

# Draw arrows for transitions
def draw_arrow(ax, p1, p2, label, offset=(0, 0), curve=0.2):
    # Self-loops handled separately
    if p1 == p2:
        x, y = positions[p1]
        ax.add_patch(Circle((x, y + radius + 0.18), 0.10,
                             fill=False, edgecolor="0.3", linewidth=1.5))
        ax.text(x, y + radius + 0.36, label, ha="center", fontsize=9, color="0.2")
        return
    x1, y1 = positions[p1]
    x2, y2 = positions[p2]
    arrow = FancyArrowPatch((x1, y1), (x2, y2),
                            connectionstyle=f"arc3,rad={curve}",
                            arrowstyle="->", mutation_scale=18,
                            color="0.4", linewidth=1.2)
    ax1.add_patch(arrow)
    mx, my = (x1 + x2) / 2 + offset[0], (y1 + y2) / 2 + offset[1]
    ax1.text(mx, my, label, fontsize=9, color="0.15",
             bbox=dict(boxstyle="round,pad=0.18", facecolor="white",
                       edgecolor="none", alpha=0.85))


# Self-loops
for i, p in enumerate(P):
    draw_arrow(ax1, i, i, f"{P[i,i]:.2f}")

# Off-diagonals
edges = [
    (0, 1, (0.0, 0.18), 0.25),
    (1, 0, (0.0, -0.18), 0.25),
    (0, 2, (-0.30, 0.0), 0.25),
    (2, 0, (0.30, -0.05), 0.25),
    (1, 2, (0.32, 0.0), 0.25),
    (2, 1, (-0.32, -0.05), 0.25),
]
for i, j, off, curve in edges:
    draw_arrow(ax1, i, j, f"{P[i,j]:.2f}", offset=off, curve=curve)

ax1.set_title("(左)鹿在 3 個狀態間的轉移矩陣 P\n"
              "(箭頭旁的數字 = 一步轉移機率)", fontsize=12)

# Right panel: evolution of p_t for n=1,2,4,16,32
p0 = np.array([1.0, 0.0, 0.0])  # start in water
ns = [1, 2, 4, 16, 32]
ps = []
P_pow = np.eye(3)
seq = [p0.copy()]
for n in range(1, max(ns) + 1):
    P_pow = P_pow @ P
    if n in ns:
        ps.append(p0 @ P_pow)

# Build bar groups
x = np.arange(len(state_names))
width = 0.13
positions_offsets = np.arange(len(ns) + 1) * width - width * (len(ns)) / 2
labels = ["t=0"] + [f"t={n}" for n in ns]
for i, vec in enumerate([p0] + ps):
    color = plt.cm.viridis(i / (len(ns) + 1))
    ax2.bar(x + positions_offsets[i], vec, width, color=color,
            edgecolor="0.4", linewidth=0.6, label=labels[i])

# Fixed distribution (analytic): solve t P = t with sum = 1
# Eigenvector of P^T with eigenvalue 1
w, v = np.linalg.eig(P.T)
fixed_idx = np.argmin(abs(w - 1.0))
fixed = np.real(v[:, fixed_idx])
fixed /= fixed.sum()
ax2.axhline(0, color="0.5", linewidth=0.6)
for i, val in enumerate(fixed):
    ax2.axhline(val, color="0.5", linestyle=":", linewidth=0.8,
                xmin=i/3, xmax=(i+1)/3)
ax2.set_xticks(x)
ax2.set_xticklabels(state_names, fontsize=10)
ax2.set_ylabel("狀態機率 p_t(i)")
ax2.set_ylim(0, 1.05)
ax2.set_title("(右)起始 p_0 = (1, 0, 0)(從水域出發),\n"
              "p_t 隨 t 收斂到固定機率分布 ≈ (0.385, 0.308, 0.308)",
              fontsize=12)
ax2.legend(loc="upper right", fontsize=8.5, ncol=2)
ax2.grid(axis="y", alpha=0.25)

fig.suptitle("圖 10-D:Markov 鏈 — 鹿在水、草、睡覺三狀態的長期分布",
             fontsize=14, fontweight="bold", y=1.02)
fig.tight_layout()
fig.savefig(OUTDIR / "helper4-markov-deer.png", dpi=150, bbox_inches="tight")
plt.close(fig)
print("Wrote helper4-markov-deer.png")

print("\nAll Lec 10 helpers rendered.")
