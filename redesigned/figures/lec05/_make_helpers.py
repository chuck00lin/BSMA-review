"""Helper illustrations for Lecture 05.

Helpers:
  1. Partial derivative intuition — surface z = f(x, t), with slices showing
     ∂f/∂x (fix t) and ∂f/∂t (fix x)
  2. 1D conservation derivation — small segment with F_in / F_out and a
     box-with-mass cartoon
  3. Advection vs diffusion — animation-like before/after panels showing
     drift (mean moves) vs spread (width grows)
  4. Activator-inhibitor mechanism — pattern emergence from short-range
     activation + long-range inhibition
  5. Dimensionless logistic — original two-parameter equation vs the single
     "canonical" equation it collapses to
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
# Helper 1: Partial derivative — fix one variable, vary the other
# ----------------------------------------------------------------------------
fig, axes = plt.subplots(1, 3, figsize=(15, 5))

# Function f(x, t) — a 2D Gaussian-like bump moving with time
def f(x, t):
    return np.exp(-((x - 0.4 * t)**2) / 4) * np.exp(-0.05 * t)

xs = np.linspace(-5, 12, 200)
ts = np.linspace(0, 10, 200)
X, T = np.meshgrid(xs, ts)
Z = f(X, T)

# Panel (a): the full surface (heatmap)
ax = axes[0]
c = ax.contourf(X, T, Z, levels=15, cmap="viridis")
ax.set_xlabel("空間 $x$", fontsize=12)
ax.set_ylabel("時間 $t$", fontsize=12)
ax.set_title("函數 $f(x, t)$ 同時隨 $x$、$t$ 變", fontsize=12)
ax.axhline(5, color="red", linestyle="--", linewidth=2, label="固定 $t=5$")
ax.axvline(2, color="orange", linestyle="--", linewidth=2, label="固定 $x=2$")
ax.legend(loc="upper right", fontsize=10)
plt.colorbar(c, ax=ax, label="$f$")

# Panel (b): slice at fixed t=5 — varies along x → ∂f/∂x
ax = axes[1]
t_fixed = 5.0
x_slice = xs
y_slice = f(x_slice, t_fixed)
ax.plot(x_slice, y_slice, color="red", linewidth=2.5,
        label=f"$f(x, t=5)$")
# Tangent at x=2
x0 = 2.0
y0 = f(x0, t_fixed)
# numerical derivative
h = 0.001
slope = (f(x0 + h, t_fixed) - f(x0 - h, t_fixed)) / (2 * h)
xs_t = np.linspace(x0 - 1.5, x0 + 1.5, 10)
ax.plot(xs_t, y0 + slope * (xs_t - x0), color="black",
        linewidth=1.5, linestyle=":")
ax.plot(x0, y0, "o", color="black", markersize=8)
ax.annotate(rf"$\dfrac{{\partial f}}{{\partial x}}|_{{x=2,t=5}} \approx {slope:.2f}$",
            xy=(x0, y0), xytext=(x0 + 1.5, y0 + 0.25),
            fontsize=12,
            arrowprops=dict(arrowstyle="->", color="black"))
ax.set_xlabel("空間 $x$", fontsize=12)
ax.set_ylabel("$f(x, t=5)$", fontsize=12)
ax.set_title("固定 $t=5$,只看 $x$ 變 → $\\partial f / \\partial x$",
             fontsize=12)
ax.grid(alpha=0.25, linestyle="--")
ax.legend(loc="upper right", fontsize=10)

# Panel (c): slice at fixed x=2 — varies along t → ∂f/∂t
ax = axes[2]
x_fixed = 2.0
t_slice = ts
y_slice = f(x_fixed, t_slice)
ax.plot(t_slice, y_slice, color="orange", linewidth=2.5,
        label=f"$f(x=2, t)$")
# Tangent at t=5
t0 = 5.0
y0 = f(x_fixed, t0)
slope = (f(x_fixed, t0 + h) - f(x_fixed, t0 - h)) / (2 * h)
ts_t = np.linspace(t0 - 1.5, t0 + 1.5, 10)
ax.plot(ts_t, y0 + slope * (ts_t - t0), color="black",
        linewidth=1.5, linestyle=":")
ax.plot(t0, y0, "o", color="black", markersize=8)
ax.annotate(rf"$\dfrac{{\partial f}}{{\partial t}}|_{{x=2,t=5}} \approx {slope:.2f}$",
            xy=(t0, y0), xytext=(t0 + 1.0, y0 + 0.2),
            fontsize=12,
            arrowprops=dict(arrowstyle="->", color="black"))
ax.set_xlabel("時間 $t$", fontsize=12)
ax.set_ylabel("$f(x=2, t)$", fontsize=12)
ax.set_title("固定 $x=2$,只看 $t$ 變 → $\\partial f / \\partial t$",
             fontsize=12)
ax.grid(alpha=0.25, linestyle="--")
ax.legend(loc="upper right", fontsize=10)

fig.suptitle("偏導數的直覺:把其他變數「凍結」,只對一個變數求導",
             fontsize=14, y=1.02)
plt.tight_layout()
plt.savefig(OUTDIR / "helper-1-partial-derivative.png",
            dpi=160, bbox_inches="tight", facecolor="white")
plt.close()


# ----------------------------------------------------------------------------
# Helper 2: Advection vs diffusion intuition
# ----------------------------------------------------------------------------
fig, axes = plt.subplots(2, 3, figsize=(14, 7))

# Initial Gaussian
xs = np.linspace(-5, 25, 400)
mu0, sigma0 = 5.0, 0.8

# Time points
times = [0, 4, 8]

# Top row: ADVECTION (mean drifts, width fixed)
for i, t in enumerate(times):
    ax = axes[0, i]
    mu = mu0 + 1.5 * t
    sigma = sigma0
    y = np.exp(-((xs - mu)**2) / (2 * sigma**2)) / (sigma * np.sqrt(2*np.pi))
    ax.fill_between(xs, y, alpha=0.4, color="#2b6cb0")
    ax.plot(xs, y, color="#2b6cb0", linewidth=2)
    ax.set_xlim(-5, 25)
    ax.set_ylim(0, 0.6)
    ax.set_xlabel("位置 $x$", fontsize=10)
    if i == 0:
        ax.set_ylabel("濃度 $C$", fontsize=11)
    ax.set_title(f"$t = {t}$", fontsize=11)
    ax.grid(alpha=0.25, linestyle="--")
    # Mark center
    ax.axvline(mu, color="red", linestyle=":", linewidth=1)
    ax.text(mu + 0.3, 0.45, f"中心: $x={mu:.1f}$",
            fontsize=9, color="red")
fig.text(0.5, 0.97,
         "平流 (Advection):中心隨時間「漂走」,形狀不變",
         fontsize=13, ha="center", color="#2b6cb0", fontweight="bold")

# Bottom row: DIFFUSION (mean fixed, width grows)
for i, t in enumerate(times):
    ax = axes[1, i]
    mu = mu0
    sigma = sigma0 * np.sqrt(1 + t * 1.5)
    y = np.exp(-((xs - mu)**2) / (2 * sigma**2)) / (sigma * np.sqrt(2*np.pi))
    ax.fill_between(xs, y, alpha=0.4, color="#c53030")
    ax.plot(xs, y, color="#c53030", linewidth=2)
    ax.set_xlim(-5, 25)
    ax.set_ylim(0, 0.6)
    ax.set_xlabel("位置 $x$", fontsize=10)
    if i == 0:
        ax.set_ylabel("濃度 $C$", fontsize=11)
    ax.set_title(f"$t = {t}$", fontsize=11)
    ax.grid(alpha=0.25, linestyle="--")
    ax.axvline(mu, color="red", linestyle=":", linewidth=1)
    ax.text(mu + 0.3, 0.45, f"中心仍在 $x={mu:.1f}$\n寬度: $\\sigma={sigma:.2f}$",
            fontsize=9, color="red")

fig.text(0.5, 0.46,
         "擴散 (Diffusion):中心不動,但形狀越來越「胖」(隨機運動撒開)",
         fontsize=13, ha="center", color="#c53030", fontweight="bold")

plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.savefig(OUTDIR / "helper-2-advection-vs-diffusion.png",
            dpi=160, bbox_inches="tight", facecolor="white")
plt.close()


# ----------------------------------------------------------------------------
# Helper 3: Activator-inhibitor mechanism for Turing patterns
# ----------------------------------------------------------------------------
fig, axes = plt.subplots(1, 2, figsize=(14, 5.5))

# Left: mechanism diagram (boxes + arrows)
ax = axes[0]
ax.set_xlim(0, 10)
ax.set_ylim(0, 6)
ax.axis("off")

# Activator box
act = mpatches.FancyBboxPatch((1.5, 4.0), 2.5, 1.0,
                               boxstyle="round,pad=0.1",
                               linewidth=2, edgecolor="#22543d",
                               facecolor="#c6f6d5")
ax.add_patch(act)
ax.text(2.75, 4.5, "激活子 $u$\n(Activator)", fontsize=12,
        ha="center", va="center", color="#22543d", fontweight="bold")

# Inhibitor box
inh = mpatches.FancyBboxPatch((6.0, 4.0), 2.5, 1.0,
                               boxstyle="round,pad=0.1",
                               linewidth=2, edgecolor="#7b341e",
                               facecolor="#fed7c4")
ax.add_patch(inh)
ax.text(7.25, 4.5, "抑制子 $v$\n(Inhibitor)", fontsize=12,
        ha="center", va="center", color="#7b341e", fontweight="bold")

# Self-activation (autocatalysis) on activator
ax.annotate("", xy=(2.5, 5.05), xytext=(3.5, 5.4),
            arrowprops=dict(arrowstyle="->", linewidth=2, color="#22543d",
                            connectionstyle="arc3,rad=0.5"))
ax.text(3.7, 5.6, "自激活\n(autocatalysis)", fontsize=10,
        color="#22543d")

# u → v (activate)
ax.annotate("", xy=(6.0, 4.7), xytext=(4.0, 4.7),
            arrowprops=dict(arrowstyle="->", linewidth=2, color="#22543d"))
ax.text(5.0, 4.85, "激活", fontsize=10, ha="center", color="#22543d")

# v → u (inhibit) — with bar end
ax.annotate("", xy=(4.0, 4.3), xytext=(6.0, 4.3),
            arrowprops=dict(arrowstyle="-|>", linewidth=2, color="#c53030"))
ax.text(5.0, 4.05, "抑制", fontsize=10, ha="center", color="#c53030")

# Diffusion arrows
ax.annotate("", xy=(2.75, 3.2), xytext=(2.75, 4.0),
            arrowprops=dict(arrowstyle="->", linewidth=1.5, color="#4a5568"))
ax.text(2.0, 3.4, "慢擴散\n$D_u$ 小", fontsize=10, color="#22543d", ha="right")

ax.annotate("", xy=(7.25, 3.2), xytext=(7.25, 4.0),
            arrowprops=dict(arrowstyle="->", linewidth=2.5, color="#4a5568"))
ax.text(8.0, 3.4, "快擴散\n$D_v$ 大", fontsize=10, color="#7b341e")

# Key principle box
ax.text(5.0, 2.0,
        "**關鍵**:激活子擴散慢、抑制子擴散快\n"
        "→ 局部「自我加強」+ 遠處「抑制周圍」\n"
        "→ 自發形成「斑點」、「條紋」、「螺旋」等圖案",
        fontsize=11, ha="center", color="#1a202c",
        bbox=dict(facecolor="#fffaf0", edgecolor="#744210",
                  boxstyle="round,pad=0.6"))

ax.set_title("激活子—抑制子的相互作用",
             fontsize=13, color="#2b6cb0", pad=8)

# Right: spatial pattern emergence (sample 1D pattern)
ax = axes[1]
xs = np.linspace(0, 30, 400)
# Sample pattern: stripes
pattern = 1.0 + 0.5 * np.cos(2 * np.pi * xs / 4)
ax.fill_between(xs, pattern, color="#22543d", alpha=0.3,
                label="活化子 $u$ 濃度")
ax.plot(xs, pattern, color="#22543d", linewidth=2)

inhibitor = 1.0 + 0.5 * np.cos(2 * np.pi * (xs - 2) / 4) * 0.7
ax.plot(xs, inhibitor, color="#c53030", linewidth=2, linestyle="--",
        label="抑制子 $v$ 濃度")

ax.set_xlabel("空間位置 $x$", fontsize=12)
ax.set_ylabel("濃度", fontsize=12)
ax.set_xlim(0, 30)
ax.set_ylim(0, 2)
ax.set_title("結果:空間上自發形成週期性「條紋」", fontsize=13, pad=8)
ax.grid(alpha=0.25, linestyle="--")
ax.legend(loc="upper right", fontsize=10)

# Annotations
ax.text(15, 0.3,
        "(這就是斑馬魚的條紋、豹的斑點、貝殼紋路……的數學起源)",
        fontsize=10, ha="center", color="#4a5568", style="italic")

plt.tight_layout()
plt.savefig(OUTDIR / "helper-3-turing-mechanism.png",
            dpi=160, bbox_inches="tight", facecolor="white")
plt.close()


# ----------------------------------------------------------------------------
# Helper 4: Dimensionless scaling — same equation, fewer parameters
# ----------------------------------------------------------------------------
fig, axes = plt.subplots(1, 2, figsize=(13, 5.5), sharey=True)

# Original logistic — 4 different (r, K) parameter sets.
# Use same dimensionless n0 = 0.1 (so N0 = 0.1 K) — that way the dimensionless
# curves will perfectly collapse.
params = [
    (0.05, 100, "#2b6cb0", "$r=0.05$, $K=100$"),
    (0.10, 100, "#c53030", "$r=0.10$, $K=100$"),
    (0.05, 200, "#22543d", "$r=0.05$, $K=200$"),
    (0.10, 200, "#7b341e", "$r=0.10$, $K=200$"),
]
n0 = 0.1   # same dimensionless starting condition for all

t = np.linspace(0, 100, 300)

ax = axes[0]
Kmax = max(p[1] for p in params)
for r, K, color, label in params:
    N0 = n0 * K
    N = K / (1 + (K / N0 - 1) * np.exp(-r * t))
    ax.plot(t, N / Kmax, color=color, linewidth=2, label=label)

ax.set_xlabel("時間 $t$", fontsize=12)
ax.set_ylabel("$N \\,/\\, K_{\\max}$", fontsize=12)
ax.set_title("原版式子(每組參數不同曲線)\n$\\frac{dN}{dt}=rN(1-N/K)$",
             fontsize=12, pad=8)
ax.grid(alpha=0.25, linestyle="--")
ax.legend(loc="lower right", fontsize=10)
ax.set_xlim(0, 100)

# Dimensionless version: τ = rt, n = N/K
ax = axes[1]
tau = np.linspace(0, 6, 300)
n_canonical = 1 / (1 + (1 / n0 - 1) * np.exp(-tau))
# Black dashed underlay
ax.plot(tau, n_canonical, color="black",
        linewidth=5, linestyle="-", alpha=0.18,
        label="所有曲線完全重合 ↓")
for r, K, color, label in params:
    n = 1 / (1 + (1 / n0 - 1) * np.exp(-tau))
    ax.plot(tau, n, color=color, linewidth=1.7, label=label, alpha=0.85)

ax.set_xlabel("無因次時間 $\\tau = rt$", fontsize=12)
ax.set_ylabel("$n = N/K$", fontsize=12)
ax.set_title("無因次化後(同一條曲線!)\n$\\frac{dn}{d\\tau}=n(1-n)$",
             fontsize=12, pad=8)
ax.grid(alpha=0.25, linestyle="--")
ax.legend(loc="lower right", fontsize=10)
ax.set_xlim(0, 6)
ax.set_ylim(0, 1.1)

fig.suptitle("無因次化(non-dimensionalization)的威力:\n"
             "把「兩個參數」的家族,壓縮成「一條曲線」",
             fontsize=14, y=1.04)
plt.tight_layout()
plt.savefig(OUTDIR / "helper-4-dimensionless-collapse.png",
            dpi=160, bbox_inches="tight", facecolor="white")
plt.close()


print("Done. Wrote:")
for p in sorted(OUTDIR.glob("helper-*.png")):
    print(" ", p.name, f"({p.stat().st_size} bytes)")
