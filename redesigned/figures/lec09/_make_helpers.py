"""Helper illustrations for Lecture 09 — Model Analysis.

Helpers:
  1. Sensitivity strategies & index — two scanning strategies overlaid on a
     2D response contour (one-at-a-time vs multi-parameter grid), plus a
     bar chart of S = (delta R / R_n) / (delta P / P_n) for six fictitious
     parameters showing which ones drive the model.
  2. Error propagation amplified vs compensated — two functions (z = e^x
     and z = sqrt(x)) with the same input scatter sigma_x; show how the
     same uncertainty becomes a large/small spread in z depending on the
     local slope (df/dx) at the mean.
  3. Monte Carlo error analysis — 1000 MC replicates of the Pielou
     extinction model P = (d/b)^n with normally distributed d, b, n.
     Histogram + cumulative; mark deterministic estimate, MC mean, median
     so the reader sees that mean(f(X)) != f(mean(X)) for a nonlinear f.
  4. Eigenvalue dictionary for phase planes — 2x3 panel: stable node,
     unstable node, saddle, stable spiral, unstable spiral, center.
     Each panel has a streamplot of dx/dt = A x and shows lambda values.
"""
from pathlib import Path
import matplotlib.pyplot as plt
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
# Helper 1: Two sensitivity strategies + S bar chart
# ----------------------------------------------------------------------------
fig, axes = plt.subplots(1, 3, figsize=(15.5, 5.0),
                          gridspec_kw={"width_ratios": [1, 1, 1.05]})

# Build a 2D response surface (Gaussian-like bowl)
p1 = np.linspace(-1.5, 1.5, 120)
p2 = np.linspace(-1.5, 1.5, 120)
P1, P2 = np.meshgrid(p1, p2)
R = 1.6 * P1**2 + 1.0 * P2**2 + 0.6 * P1 * P2

# Strategy A: vary single parameter over wide range
ax = axes[0]
cs = ax.contour(P1, P2, R, levels=8, colors="0.55", linewidths=0.9)
ax.clabel(cs, inline=True, fontsize=7, fmt="%.1f")
# nominal "N" point
N = (0.0, 0.0)
ax.scatter(*N, marker="o", s=60, color="C2", zorder=5)
ax.annotate("N(標稱)", N, xytext=(0.1, 0.15), fontsize=9.5)
# horizontal scan (vary p1) and vertical scan (vary p2)
ax.plot([-1.4, 1.4], [0, 0], color="C0", linewidth=2, zorder=4)
ax.plot([0, 0], [-1.4, 1.4], color="C3", linewidth=2, zorder=4)
ax.scatter([-1.2, -0.6, 0.6, 1.2], [0, 0, 0, 0],
           s=55, color="C0", marker="o", edgecolor="white", zorder=5)
ax.scatter([0, 0, 0, 0], [-1.2, -0.6, 0.6, 1.2],
           s=55, color="C3", marker="s", edgecolor="white", zorder=5)
ax.set_xlim(-1.55, 1.55); ax.set_ylim(-1.55, 1.55)
ax.set_xlabel("參數 p1"); ax.set_ylabel("參數 p2")
ax.set_title("策略 A:一次動一個參數,範圍掃寬", fontsize=11)
ax.set_aspect("equal")
ax.text(0.04, 0.04, "p1→ p1 軸藍\np2→ p2 軸紅",
        transform=ax.transAxes, fontsize=9, va="bottom",
        bbox=dict(boxstyle="round,pad=0.3", facecolor="#fff7d6", edgecolor="0.5"))

# Strategy B: factorial design - small perturbation in many params at once
ax = axes[1]
cs = ax.contour(P1, P2, R, levels=8, colors="0.55", linewidths=0.9)
ax.clabel(cs, inline=True, fontsize=7, fmt="%.1f")
ax.scatter(*N, marker="o", s=60, color="C2", zorder=5)
ax.annotate("N", N, xytext=(0.08, 0.12), fontsize=10)
# 3x3 grid around N (small range)
grid = np.linspace(-0.5, 0.5, 3)
G1, G2 = np.meshgrid(grid, grid)
for x, y in zip(G1.ravel(), G2.ravel()):
    if x == 0 and y == 0:
        continue
    ax.scatter(x, y, s=55, color="C4", marker="P",
               edgecolor="white", zorder=5)
# annotate one point with +/-
ax.annotate("+,+", (0.5, 0.5), xytext=(0.55, 0.55), fontsize=8.5)
ax.annotate("−,−", (-0.5, -0.5), xytext=(-0.85, -0.7), fontsize=8.5)
ax.set_xlim(-1.55, 1.55); ax.set_ylim(-1.55, 1.55)
ax.set_xlabel("參數 p1"); ax.set_ylabel("參數 p2")
ax.set_title("策略 B:多參數同時擾動(分數階乘 / ANOVA)", fontsize=11)
ax.set_aspect("equal")
ax.text(0.04, 0.04, "小範圍多點同動,\n用 F 統計量當靈敏度指標。",
        transform=ax.transAxes, fontsize=9, va="bottom",
        bbox=dict(boxstyle="round,pad=0.3", facecolor="#fff7d6", edgecolor="0.5"))

# Right panel: S bar chart for six fictitious parameters
ax = axes[2]
params = ["r", "K", "α", "β", "μ", "γ"]
S_values = [1.15, 0.88, 0.42, -0.30, 0.08, -0.04]
colors = ["#d97757" if abs(s) > 0.5 else "#f0c674" if abs(s) > 0.1 else "#7da9c4"
          for s in S_values]
bars = ax.barh(params, S_values, color=colors, edgecolor="0.3")
for bar, s in zip(bars, S_values):
    ax.text(s + (0.04 if s >= 0 else -0.04), bar.get_y() + bar.get_height()/2,
            f"S={s:+.2f}", va="center", ha="left" if s >= 0 else "right",
            fontsize=10)
ax.axvline(0, color="0.3", linewidth=0.8)
ax.axvline(0.5, color="0.7", linestyle="--", linewidth=0.8)
ax.axvline(-0.5, color="0.7", linestyle="--", linewidth=0.8)
ax.set_xlabel("靈敏度指標 S = (ΔR/R_n) / (ΔP/P_n)")
ax.set_xlim(-0.8, 1.5)
ax.set_title("六個參數的 S 值 — 找出真正的「火車頭」", fontsize=11)
ax.text(0.03, 0.05, "|S| > 0.5:強烈依賴(紅)\n0.1–0.5:中等(黃)\n< 0.1:幾乎沒影響(藍)",
        transform=ax.transAxes, fontsize=9, va="bottom",
        bbox=dict(boxstyle="round,pad=0.3", facecolor="0.97", edgecolor="0.6"))
ax.grid(axis="x", alpha=0.25)

fig.suptitle("圖 9-A:靈敏度分析的兩個策略 + 靈敏度指標 S 的解讀",
             fontsize=14, fontweight="bold", y=1.02)
fig.tight_layout()
fig.savefig(OUTDIR / "helper1-sensitivity-strategies.png", dpi=150, bbox_inches="tight")
plt.close(fig)
print("Wrote helper1-sensitivity-strategies.png")


# ----------------------------------------------------------------------------
# Helper 2: Error propagation amplified vs compensated
# ----------------------------------------------------------------------------
fig, axes = plt.subplots(1, 2, figsize=(13, 5.2))

x_mean = 1.0
sigma_x = 0.35
xs = np.linspace(0.001, 2.4, 500)
x_samples = np.random.default_rng(42).normal(x_mean, sigma_x, 600)
x_samples = x_samples[(x_samples > 0.05) & (x_samples < 2.4)]

# Panel A: amplification (steep function — exponential)
ax = axes[0]
f = lambda x: np.exp(x)
ax.plot(xs, f(xs), color="0.2", linewidth=2.2, label="z = exp(x)(陡)")
z_samples = f(x_samples)
# Show distribution of x along bottom, distribution of z along left
ax.hist(x_samples, bins=22, bottom=0, weights=np.ones_like(x_samples)*0.7/len(x_samples)*30,
        color="C0", alpha=0.55, label="x 的分布(σ_x=0.35)")
# project to z on left axis using horizontal histogram
ax.hist(z_samples, bins=22, orientation="horizontal",
        weights=np.ones_like(z_samples)*0.10/len(z_samples)*30,
        color="C3", alpha=0.55, label="z 的分布(放大)")
ax.axvline(x_mean, color="0.2", linestyle=":", linewidth=1)
ax.axhline(f(x_mean), color="0.2", linestyle=":", linewidth=1)
ax.scatter([x_mean], [f(x_mean)], s=60, color="black", zorder=5)
ax.text(x_mean + 0.05, f(x_mean) + 0.4, f"(x̄, f(x̄))", fontsize=10)
# Slope annotation
slope = f(x_mean)
ax.annotate(f"局部斜率 ∂f/∂x = {slope:.2f}",
            xy=(x_mean, f(x_mean)),
            xytext=(0.18, 6.5),
            fontsize=10,
            arrowprops=dict(arrowstyle="->", color="0.4"),
            bbox=dict(boxstyle="round,pad=0.35", facecolor="#fff7d6", edgecolor="0.5"))
ax.set_xlim(0, 2.4); ax.set_ylim(0, 12)
ax.set_xlabel("x"); ax.set_ylabel("z")
ax.set_title("A:放大(amplified)\n陡函數 → 同樣 σ_x 變成大很多的 σ_z", fontsize=11)
ax.legend(loc="upper left", fontsize=8.5)
ax.grid(alpha=0.25)

# Panel B: compensation (saturating function — sqrt)
ax = axes[1]
f = lambda x: 3 * np.sqrt(x)
ax.plot(xs, f(xs), color="0.2", linewidth=2.2, label="z = 3√x(平緩)")
z_samples = f(x_samples)
ax.hist(x_samples, bins=22, bottom=0, weights=np.ones_like(x_samples)*0.7/len(x_samples)*30,
        color="C0", alpha=0.55, label="x 的分布(σ_x=0.35)")
ax.hist(z_samples, bins=22, orientation="horizontal",
        weights=np.ones_like(z_samples)*0.10/len(z_samples)*30,
        color="C3", alpha=0.55, label="z 的分布(壓縮)")
ax.axvline(x_mean, color="0.2", linestyle=":", linewidth=1)
ax.axhline(f(x_mean), color="0.2", linestyle=":", linewidth=1)
ax.scatter([x_mean], [f(x_mean)], s=60, color="black", zorder=5)
ax.text(x_mean + 0.05, f(x_mean) + 0.15, f"(x̄, f(x̄))", fontsize=10)
slope = 3 / (2 * np.sqrt(x_mean))
ax.annotate(f"局部斜率 ∂f/∂x = {slope:.2f}",
            xy=(x_mean, f(x_mean)),
            xytext=(1.0, 5.2),
            fontsize=10,
            arrowprops=dict(arrowstyle="->", color="0.4"),
            bbox=dict(boxstyle="round,pad=0.35", facecolor="#fff7d6", edgecolor="0.5"))
ax.set_xlim(0, 2.4); ax.set_ylim(0, 6)
ax.set_xlabel("x"); ax.set_ylabel("z")
ax.set_title("B:抵銷(compensated)\n平緩函數 → 同樣 σ_x 被壓縮成較小的 σ_z", fontsize=11)
ax.legend(loc="upper left", fontsize=8.5)
ax.grid(alpha=0.25)

fig.suptitle("圖 9-B:誤差傳播取決於「函數在哪個點」 — Var(z) ≈ (∂f/∂x)² · Var(x)",
             fontsize=13, fontweight="bold", y=1.02)
fig.tight_layout()
fig.savefig(OUTDIR / "helper2-error-amp-comp.png", dpi=150, bbox_inches="tight")
plt.close(fig)
print("Wrote helper2-error-amp-comp.png")


# ----------------------------------------------------------------------------
# Helper 3: Monte Carlo error analysis on Pielou's extinction model
# ----------------------------------------------------------------------------
fig, axes = plt.subplots(1, 2, figsize=(13.5, 5.0))
rng = np.random.default_rng(7)
N_mc = 1000

def mc_run(n0=10):
    d = rng.normal(0.8, 0.157, N_mc)
    b = rng.normal(0.9, 0.174, N_mc)
    n = rng.normal(n0, 0.69, N_mc)
    valid = (d > 0) & (b > 0) & (n > 0)
    P = (d[valid] / b[valid]) ** n[valid]
    P = np.clip(P, 0, 1)
    return P

P10 = mc_run(n0=10)
P5 = mc_run(n0=5)
P20 = mc_run(n0=20)

# Left: histogram for n0=10 with deterministic, MC mean, median
ax = axes[0]
ax.hist(P10, bins=40, color="#7da9c4", edgecolor="0.4", alpha=0.85)
det = (0.8 / 0.9) ** 10
ax.axvline(det, color="C3", linewidth=2,
           label=f"確定式估計 f(mean) = {det:.3f}")
ax.axvline(P10.mean(), color="C2", linewidth=2,
           label=f"MC 平均 mean(f) = {P10.mean():.3f}")
ax.axvline(np.median(P10), color="0.2", linestyle="--", linewidth=1.6,
           label=f"MC 中位數 = {np.median(P10):.3f}")
ax.set_xlabel("滅絕機率 P")
ax.set_ylabel("出現次數(共 1000 次模擬)")
ax.set_title("n0 = 10:1000 次 Monte Carlo,\n注意「確定式 ≠ MC 平均」(非線性偏差)",
             fontsize=11)
ax.legend(loc="upper right", fontsize=9.5)
ax.grid(alpha=0.25)
ax.set_xlim(0, 1)

# Right: how initial population size shifts the whole distribution
ax = axes[1]
ax.hist(P5, bins=40, color="C3", alpha=0.55, label="n0 = 5", edgecolor="0.4")
ax.hist(P10, bins=40, color="#7da9c4", alpha=0.65, label="n0 = 10", edgecolor="0.4")
ax.hist(P20, bins=40, color="C2", alpha=0.55, label="n0 = 20", edgecolor="0.4")
ax.axvline(P5.mean(), color="C3", linewidth=2)
ax.axvline(P10.mean(), color="#7da9c4", linewidth=2)
ax.axvline(P20.mean(), color="C2", linewidth=2)
ax.set_xlabel("滅絕機率 P")
ax.set_ylabel("出現次數")
ax.set_title("不同初始族群 n0 對滅絕機率分布的影響\n"
             "—— 大族群被擠到「機率幾乎為 0」", fontsize=11)
ax.legend(loc="upper right", fontsize=10)
ax.grid(alpha=0.25)
ax.set_xlim(0, 1)

fig.suptitle("圖 9-C:Monte Carlo 誤差分析 — Pielou 滅絕模型 P = (d/b)^n",
             fontsize=14, fontweight="bold", y=1.02)
fig.tight_layout()
fig.savefig(OUTDIR / "helper3-monte-carlo.png", dpi=150, bbox_inches="tight")
plt.close(fig)
print("Wrote helper3-monte-carlo.png")


# ----------------------------------------------------------------------------
# Helper 4: Eigenvalue dictionary for phase planes
# ----------------------------------------------------------------------------
fig, axes = plt.subplots(2, 3, figsize=(14.5, 8.8))


def stream_phase(ax, A, title, eigs_label, color="C0"):
    x = np.linspace(-2, 2, 30)
    y = np.linspace(-2, 2, 30)
    X, Y = np.meshgrid(x, y)
    DX = A[0, 0] * X + A[0, 1] * Y
    DY = A[1, 0] * X + A[1, 1] * Y
    ax.streamplot(X, Y, DX, DY, color=color, density=1.1, linewidth=0.9, arrowsize=1.1)
    ax.scatter([0], [0], s=80, color="black", zorder=5)
    ax.set_xlim(-2, 2); ax.set_ylim(-2, 2)
    ax.set_aspect("equal")
    ax.set_xlabel("x"); ax.set_ylabel("y")
    ax.set_title(title, fontsize=11)
    ax.text(0.02, 0.97, eigs_label, transform=ax.transAxes,
            fontsize=10, va="top",
            bbox=dict(boxstyle="round,pad=0.3", facecolor="#fff7d6", edgecolor="0.5"))
    ax.grid(alpha=0.2)


# (a) stable node: λ1, λ2 both negative
A1 = np.array([[-1.5, 0], [0, -0.5]])
stream_phase(axes[0, 0], A1, "(a) 穩定節點 (stable node)\n所有路徑直接收斂",
             "λ_1 = −1.5\nλ_2 = −0.5\n→ 真實負",
             color="C2")
# (b) unstable node
A2 = np.array([[1.2, 0], [0, 0.4]])
stream_phase(axes[0, 1], A2, "(b) 不穩定節點 (unstable node)\n所有路徑遠離",
             "λ_1 = +1.2\nλ_2 = +0.4\n→ 真實正",
             color="C3")
# (c) saddle
A3 = np.array([[1.0, 0], [0, -1.0]])
stream_phase(axes[0, 2], A3, "(c) 鞍點 (saddle)\n沿某方向穩定、其他方向逃逸",
             "λ_1 = +1.0\nλ_2 = −1.0\n→ 一正一負",
             color="C4")
# (d) stable spiral
A4 = np.array([[-0.4, 1.0], [-1.0, -0.4]])
stream_phase(axes[1, 0], A4, "(d) 穩定螺旋 (stable spiral)\n邊轉邊收斂",
             "λ = −0.4 ± 1.0i\n→ 複數,Re < 0",
             color="C0")
# (e) unstable spiral
A5 = np.array([[0.3, 1.0], [-1.0, 0.3]])
stream_phase(axes[1, 1], A5, "(e) 不穩定螺旋 (unstable spiral)\n邊轉邊發散",
             "λ = +0.3 ± 1.0i\n→ 複數,Re > 0",
             color="C1")
# (f) center (neutral)
A6 = np.array([[0.0, 1.0], [-1.0, 0.0]])
stream_phase(axes[1, 2], A6, "(f) 中心 (center)\n永遠繞圈,不收斂也不發散",
             "λ = ±1.0i\n→ 純虛數,Re = 0",
             color="C5")

fig.suptitle("圖 9-D:Jacobian 特徵值 λ 的符號決定相平面長相\n"
             "(這六種就是線性系統穩定性的「字典」)",
             fontsize=13, fontweight="bold", y=1.0)
fig.tight_layout()
fig.savefig(OUTDIR / "helper4-eigenvalue-dictionary.png", dpi=150, bbox_inches="tight")
plt.close(fig)
print("Wrote helper4-eigenvalue-dictionary.png")

print("\nAll Lec 09 helpers rendered.")
