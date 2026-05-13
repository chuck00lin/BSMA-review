"""Helper illustrations for Lecture 04.

Helpers:
  1. Derivative as the limit of a secant slope (tangent line)
  2. Integration as a Riemann sum (area under curve)
  3. Three types of negative feedback side-by-side (self-inhibition,
     extrinsic, saturation) — same axes, different shapes
  4. Multi-factor combination methods compared (Liebig min vs multiplicative
     vs harmonic mean vs arithmetic mean) — same C, N, P, different μ
"""
from pathlib import Path

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib import font_manager
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
# Helper 1: Derivative — secant slope approaching tangent
# ----------------------------------------------------------------------------
fig, axes = plt.subplots(1, 3, figsize=(15, 5), sharey=True)

x = np.linspace(0, 4, 400)
y = x**2

x0 = 2.0
y0 = x0**2

dxs = [1.5, 0.6, 0.1]
panel_titles = [
    "Δx = 1.5(粗略)",
    "Δx = 0.6(較準)",
    "Δx → 0(極限:切線斜率)",
]

for ax, dx, title in zip(axes, dxs, panel_titles):
    ax.plot(x, y, color="#2b6cb0", linewidth=2, label=r"$y = x^2$")
    ax.plot(x0, y0, "o", color="black", markersize=8)
    if dx > 0.01:
        x1 = x0 + dx
        y1 = x1**2
        ax.plot(x1, y1, "o", color="#c53030", markersize=8)
        # secant
        slope = (y1 - y0) / dx
        xs = np.array([x0 - 0.4, x1 + 0.4])
        ys = y0 + slope * (xs - x0)
        ax.plot(xs, ys, "--", color="#c53030", linewidth=1.5,
                label=f"割線斜率 = {slope:.2f}")
        # vertical drop / horizontal rise
        ax.plot([x0, x1], [y0, y0], "-", color="#718096", linewidth=1)
        ax.plot([x1, x1], [y0, y1], "-", color="#718096", linewidth=1)
        ax.text((x0 + x1) / 2, y0 - 0.7, f"Δx={dx}", fontsize=10,
                ha="center", color="#718096")
        ax.text(x1 + 0.1, (y0 + y1) / 2, f"Δy={y1-y0:.2f}",
                fontsize=10, color="#718096")
    # tangent (true slope = 2x0 = 4)
    slope_true = 2 * x0
    xs = np.array([x0 - 0.7, x0 + 0.7])
    ys = y0 + slope_true * (xs - x0)
    ax.plot(xs, ys, "-", color="#22543d", linewidth=2,
            label=f"切線斜率 = {slope_true:.2f}")

    ax.set_xlim(0, 4)
    ax.set_ylim(-1, 16)
    ax.set_xlabel("x", fontsize=12)
    if ax is axes[0]:
        ax.set_ylabel("y", fontsize=12)
    ax.set_title(title, fontsize=12, pad=8)
    ax.grid(alpha=0.25, linestyle="--")
    ax.legend(loc="upper left", fontsize=9.5)

fig.suptitle("導數(derivative)的直覺:Δx 越小,割線就越接近切線",
             fontsize=14, y=1.02)
plt.tight_layout()
plt.savefig(OUTDIR / "helper-1-derivative-secant.png",
            dpi=160, bbox_inches="tight", facecolor="white")
plt.close()


# ----------------------------------------------------------------------------
# Helper 2: Integration as Riemann sum — area under curve
# ----------------------------------------------------------------------------
fig, axes = plt.subplots(1, 3, figsize=(15, 5), sharey=True)

x = np.linspace(0, 4, 400)
y = x**2 / 2 + 1   # arbitrary positive function

# True integral on [0, 3]
xtrue = np.linspace(0, 3, 200)
ytrue = xtrue**2 / 2 + 1
true_area = np.trapezoid(ytrue, xtrue)

panel_n = [4, 12, 60]
panel_titles = [
    "n = 4 個矩形(粗略)",
    "n = 12 個矩形(較準)",
    "n → ∞(極限:積分的真值)",
]

for ax, n, title in zip(axes, panel_n, panel_titles):
    # plot curve
    ax.plot(x, y, color="#2b6cb0", linewidth=2)
    # Riemann rectangles
    xs = np.linspace(0, 3, n + 1)
    widths = np.diff(xs)
    heights = (xs[:-1])**2 / 2 + 1   # left-Riemann
    approx_area = np.sum(widths * heights)
    for xi, w, h in zip(xs[:-1], widths, heights):
        rect = mpatches.Rectangle((xi, 0), w, h,
                                   linewidth=0.7, edgecolor="#c53030",
                                   facecolor="#fed7d7", alpha=0.65)
        ax.add_patch(rect)
    # caption
    ax.text(0.15, 7.4, f"矩形和 ≈ {approx_area:.3f}", fontsize=11,
            color="#c53030")
    ax.text(0.15, 6.8, f"真實積分 = {true_area:.3f}", fontsize=11,
            color="#22543d")

    ax.set_xlim(0, 4)
    ax.set_ylim(0, 8)
    ax.set_xlabel("x", fontsize=12)
    if ax is axes[0]:
        ax.set_ylabel("f(x)", fontsize=12)
    ax.set_title(title, fontsize=12, pad=8)
    ax.grid(alpha=0.25, linestyle="--")
    ax.axvline(3, color="black", linewidth=0.8, alpha=0.6)
    ax.text(3.1, 0.3, "x = 3", fontsize=9, color="black")

fig.suptitle("積分(integral)的直覺:把曲線下面切成小矩形再加起來;n 越大越準",
             fontsize=14, y=1.02)
plt.tight_layout()
plt.savefig(OUTDIR / "helper-2-integration-riemann.png",
            dpi=160, bbox_inches="tight", facecolor="white")
plt.close()


# ----------------------------------------------------------------------------
# Helper 3: Three types of negative feedback — side-by-side
# ----------------------------------------------------------------------------
fig, axes = plt.subplots(1, 3, figsize=(15, 5))

# (a) Self-inhibition — logistic
ax = axes[0]
N = np.linspace(0, 100, 400)
r = 0.1
K = 80
dN = r * N * (1 - N / K)
ax.plot(N, dN, color="#c53030", linewidth=2.5, label=r"$\frac{dN}{dt}=rN(1-N/K)$")
ax.axhline(0, color="black", linewidth=0.8)
ax.axvline(K, color="#22543d", linestyle="--", linewidth=1.3)
ax.text(K + 1, 0.3, "K(承載量)", fontsize=10, color="#22543d")
ax.set_xlim(0, 100)
ax.set_xlabel("N(狀態變數)", fontsize=11)
ax.set_ylabel("變化率 dN/dt", fontsize=11)
ax.set_title("(a) 自我抑制 Self-Inhibition\n(logistic 模型)", fontsize=12)
ax.grid(alpha=0.25, linestyle="--")
ax.legend(loc="upper right", fontsize=10)

# (b) Extrinsic — Newton's cooling
ax = axes[1]
T = np.linspace(0, 100, 400)
Ta = 25
k = 0.5
dT = k * (Ta - T)
ax.plot(T, dT, color="#2b6cb0", linewidth=2.5,
        label=r"$\frac{dT}{dt}=k(T_a-T)$")
ax.axhline(0, color="black", linewidth=0.8)
ax.axvline(Ta, color="#22543d", linestyle="--", linewidth=1.3)
ax.text(Ta + 1, -3, r"$T_a$(環境溫度)", fontsize=10, color="#22543d")
ax.set_xlim(0, 100)
ax.set_xlabel("T(溫度)", fontsize=11)
ax.set_ylabel("變化率 dT/dt", fontsize=11)
ax.set_title("(b) 外部因素 Extrinsic\n(牛頓冷卻定律)", fontsize=12)
ax.grid(alpha=0.25, linestyle="--")
ax.legend(loc="upper right", fontsize=10)

# (c) Saturation — Michaelis-Menten
ax = axes[2]
S = np.linspace(0, 20, 400)
Vmax = 2.0
Km = 2.5
V = Vmax * S / (Km + S)
ax.plot(S, V, color="#7b341e", linewidth=2.5,
        label=r"$V=V_{max}\,\dfrac{S}{K_m+S}$")
ax.axhline(Vmax, color="#22543d", linestyle="--", linewidth=1.3)
ax.text(15, Vmax + 0.05, r"$V_{max}$(上限)", fontsize=10, color="#22543d")
ax.axvline(Km, color="#718096", linestyle=":", linewidth=1)
ax.axhline(Vmax / 2, color="#718096", linestyle=":", linewidth=1)
ax.plot(Km, Vmax / 2, "o", color="black", markersize=7)
ax.text(Km + 0.3, Vmax / 2 - 0.15, "S=K_m 時 V=Vmax/2",
        fontsize=9, color="black")
ax.set_xlim(0, 20)
ax.set_ylim(0, 2.5)
ax.set_xlabel("S(受質濃度)", fontsize=11)
ax.set_ylabel("速率 V", fontsize=11)
ax.set_title("(c) 飽和 Saturation\n(Michaelis-Menten 酵素動力學)", fontsize=12)
ax.grid(alpha=0.25, linestyle="--")
ax.legend(loc="lower right", fontsize=10)

fig.suptitle("負反饋的三種數學形式:行為大不相同,但都能限制速率",
             fontsize=14, y=1.02)
plt.tight_layout()
plt.savefig(OUTDIR / "helper-3-three-negative-feedback.png",
            dpi=160, bbox_inches="tight", facecolor="white")
plt.close()


# ----------------------------------------------------------------------------
# Helper 4: Multi-factor combinations compared
# ----------------------------------------------------------------------------
# Fix C, N, P scenarios; show μ/μ* under 4 methods
fig, ax = plt.subplots(figsize=(11, 6))

scenarios = [
    ("情境 A\n養分充足", 1.0, 1.0, 1.0),
    ("情境 B\nC 偏低", 0.4, 1.0, 1.0),
    ("情境 C\n3 種都中等", 0.6, 0.6, 0.6),
    ("情境 D\n只有 N 不足", 1.0, 0.2, 1.0),
]


def m_min(c, n, p):
    return min(c, n, p)


def m_mult(c, n, p):
    return c * n * p


def m_arith(c, n, p):
    return (c + n + p) / 3


def m_harm(c, n, p):
    if c == 0 or n == 0 or p == 0:
        return 0
    return 3 / (1 / c + 1 / n + 1 / p)


methods = [
    ("Liebig 最小值", m_min, "#c53030"),
    ("乘法", m_mult, "#2b6cb0"),
    ("算術平均", m_arith, "#7b341e"),
    ("調和平均", m_harm, "#22543d"),
]

n_scen = len(scenarios)
n_meth = len(methods)
bar_w = 0.18
x_pos = np.arange(n_scen)

for i, (name, fn, color) in enumerate(methods):
    vals = [fn(c, n, p) for (_, c, n, p) in scenarios]
    ax.bar(x_pos + i * bar_w - bar_w * (n_meth - 1) / 2, vals, bar_w,
           label=name, color=color, edgecolor="black", linewidth=0.6)
    for xi, v in zip(x_pos + i * bar_w - bar_w * (n_meth - 1) / 2, vals):
        ax.text(xi, v + 0.015, f"{v:.2f}", fontsize=8, ha="center")

ax.set_xticks(x_pos)
ax.set_xticklabels([f"{s[0]}\n(C={s[1]}, N={s[2]}, P={s[3]})"
                    for s in scenarios], fontsize=10)
ax.set_ylim(0, 1.1)
ax.set_ylabel(r"相對速率 $\mu/\mu^*$", fontsize=12)
ax.set_title("同樣的 C、N、P 輸入,四種「組合方法」給出截然不同的答案",
             fontsize=14, pad=12)
ax.legend(loc="upper right", fontsize=10.5, ncol=2)
ax.grid(alpha=0.25, axis="y", linestyle="--")
ax.set_axisbelow(True)

plt.tight_layout()
plt.savefig(OUTDIR / "helper-4-multi-factor-methods.png",
            dpi=160, bbox_inches="tight", facecolor="white")
plt.close()


print("Done. Wrote:")
for p in sorted(OUTDIR.glob("helper-*.png")):
    print(" ", p.name, f"({p.stat().st_size} bytes)")
