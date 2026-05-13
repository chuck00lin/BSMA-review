"""Helper illustrations for Lecture 07 — Parameter Estimation.

Helpers:
  1. Least squares with residuals — same data, two candidate lines, with
     vertical residual sticks and an SSE bar comparison.
  2. Linearizing transformation — Michaelis-Menten curve vs Lineweaver-Burk
     straight line, with the (1/S, 1/v) mapping annotated.
  3. Error surface + descent paths — steepest descent (zig-zag) vs
     Newton/LM (curvature-corrected step) on the same elongated valley.
  4. Nelder-Mead simplex operations — reflection, expansion, contraction,
     shrinkage on a single 2D error contour, each triangle labeled.
"""
from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib import font_manager
from matplotlib.patches import FancyArrowPatch, Polygon
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
# Helper 1: Least squares with residuals (two candidate fits + SSE bars)
# ----------------------------------------------------------------------------
fig, axes = plt.subplots(1, 3, figsize=(15, 5.2),
                          gridspec_kw={"width_ratios": [1, 1, 0.45]})

rng = np.random.default_rng(7)
x = np.array([1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0])
true_m, true_b = 0.85, 0.6
y = true_m * x + true_b + rng.normal(0, 0.35, size=x.size)

# fitted line via least squares
m_hat, b_hat = np.polyfit(x, y, 1)
y_hat = m_hat * x + b_hat
sse_good = np.sum((y - y_hat) ** 2)

# bad candidate line (offset & slope off)
m_bad, b_bad = 0.45, 2.2
y_bad = m_bad * x + b_bad
sse_bad = np.sum((y - y_bad) ** 2)

xs = np.linspace(0.3, 7.5, 100)

for ax, (m_, b_, ys, sse, color, title) in zip(
    axes[:2],
    [(m_bad, b_bad, y_bad, sse_bad, "#dc2626", "候選 A:不好的擬合"),
     (m_hat, b_hat, y_hat, sse_good, "#1d4ed8", "候選 B:最小平方擬合")],
):
    ax.plot(xs, m_ * xs + b_, color=color, lw=2.2, label=f"y = {m_:.2f}x + {b_:.2f}")
    for xi, yi, yhi in zip(x, y, ys):
        ax.plot([xi, xi], [yi, yhi], color="#9ca3af", lw=1.4, zorder=1)
    ax.scatter(x, y, s=58, c="#111827", zorder=3, label="實驗資料")
    ax.scatter(x, ys, s=42, marker="x", c=color, zorder=3, label="模型預測")
    ax.set_xlim(0, 8)
    ax.set_ylim(0, 8)
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_title(f"{title}\nSSE = {sse:.2f}")
    ax.legend(loc="upper left", fontsize=9)
    ax.grid(alpha=0.3)

# SSE comparison bar
ax3 = axes[2]
ax3.bar(["A", "B"], [sse_bad, sse_good], color=["#dc2626", "#1d4ed8"])
ax3.set_title("殘差平方和 SSE")
ax3.set_ylabel("SSE = Σ(y_i − y_hat_i)²")
for i, v in enumerate([sse_bad, sse_good]):
    ax3.text(i, v + 0.6, f"{v:.2f}", ha="center", fontsize=11, fontweight="bold")
ax3.set_ylim(0, max(sse_bad, sse_good) * 1.25)
ax3.grid(axis="y", alpha=0.3)

fig.suptitle("Helper 1:最小平方法挑出讓「垂直殘差平方和」最小的那條線",
             fontsize=13, y=1.02)
fig.tight_layout()
fig.savefig(OUTDIR / "helper-1-least-squares-residuals.png", dpi=140,
            bbox_inches="tight")
plt.close(fig)


# ----------------------------------------------------------------------------
# Helper 2: Linearizing transformation — Michaelis-Menten ↔ Lineweaver-Burk
# ----------------------------------------------------------------------------
fig, axes = plt.subplots(1, 2, figsize=(13, 5.2))

V_max = 2.0
K_m = 1.5
S = np.linspace(0.05, 12, 200)
v = V_max * S / (K_m + S)

# noisy "data" points
S_pts = np.array([0.5, 1.0, 1.5, 2.5, 4.0, 6.0, 9.0])
rng = np.random.default_rng(11)
v_pts = V_max * S_pts / (K_m + S_pts) + rng.normal(0, 0.04, size=S_pts.size)

ax = axes[0]
ax.plot(S, v, color="#1d4ed8", lw=2.2, label="v = Vmax S / (Km + S)")
ax.scatter(S_pts, v_pts, s=58, c="#111827", zorder=3, label="實驗資料")
ax.axhline(V_max, ls=":", color="#6b7280")
ax.text(10.5, V_max + 0.05, f"Vmax = {V_max}", color="#6b7280", fontsize=10)
ax.set_xlabel("受質濃度 S")
ax.set_ylabel("反應速率 v")
ax.set_title("(a) 原始 Michaelis–Menten 曲線\n參數 (Vmax, Km) 在分子分母都出現,不能直接線性回歸")
ax.set_xlim(0, 12)
ax.set_ylim(0, V_max * 1.2)
ax.legend(loc="lower right")
ax.grid(alpha=0.3)

# transformed: 1/v = (Km/Vmax)*(1/S) + 1/Vmax
inv_S_pts = 1 / S_pts
inv_v_pts = 1 / v_pts
slope = K_m / V_max
intercept = 1 / V_max
inv_S_line = np.linspace(0, 2.2, 50)
inv_v_line = slope * inv_S_line + intercept

ax = axes[1]
ax.plot(inv_S_line, inv_v_line, color="#dc2626", lw=2.2,
        label=f"1/v = (Km/Vmax)(1/S) + 1/Vmax")
ax.scatter(inv_S_pts, inv_v_pts, s=58, c="#111827", zorder=3, label="變換後資料")
ax.axhline(intercept, ls=":", color="#6b7280")
ax.text(1.7, intercept + 0.05, f"截距 = 1/Vmax = {intercept:.2f}",
        color="#6b7280", fontsize=10)
ax.annotate("", xy=(1.4, slope * 1.4 + intercept),
            xytext=(0.4, slope * 0.4 + intercept),
            arrowprops=dict(arrowstyle="->", color="#059669", lw=2))
ax.text(0.9, slope * 0.9 + intercept + 0.15,
        f"斜率 = Km/Vmax = {slope:.2f}", color="#059669", fontsize=10,
        fontweight="bold")
ax.set_xlabel("1/S")
ax.set_ylabel("1/v")
ax.set_title("(b) Lineweaver–Burk 變換後\n令 X=1/S、Y=1/v,變成 Y=mX+b,可直接用最小平方法")
ax.set_xlim(-0.1, 2.2)
ax.set_ylim(0, max(inv_v_pts) * 1.2)
ax.legend(loc="upper left")
ax.grid(alpha=0.3)

# arrow between panels
fig.text(0.5, 0.5, "兩邊取倒數\n非線性 → 線性", ha="center", va="center",
         fontsize=11, fontweight="bold", color="#059669",
         bbox=dict(boxstyle="round,pad=0.4", fc="#ecfdf5", ec="#059669"))

fig.suptitle("Helper 2:對參數非線性的方程式,先用「變換」把它變成 y = mx + b 的形狀",
             fontsize=13, y=1.02)
fig.tight_layout(rect=[0, 0, 1, 0.97])
fig.savefig(OUTDIR / "helper-2-linearizing-transformation.png", dpi=140,
            bbox_inches="tight")
plt.close(fig)


# ----------------------------------------------------------------------------
# Helper 3: Error surface + descent paths (steepest descent vs Newton/LM)
# ----------------------------------------------------------------------------
fig, axes = plt.subplots(1, 2, figsize=(13.5, 5.6))

# elongated quadratic error: ε(p1, p2) = 0.1*(p1-5)^2 + 1.5*(p2-3)^2
def err(p1, p2):
    return 0.1 * (p1 - 5) ** 2 + 1.5 * (p2 - 3) ** 2

def grad(p1, p2):
    return np.array([0.2 * (p1 - 5), 3.0 * (p2 - 3)])

# Hessian (constant for this quadratic)
H = np.array([[0.2, 0.0], [0.0, 3.0]])
H_inv = np.linalg.inv(H)

p1_grid = np.linspace(-2, 12, 200)
p2_grid = np.linspace(-1, 7, 200)
P1, P2 = np.meshgrid(p1_grid, p2_grid)
E = err(P1, P2)
levels = [0.5, 2, 5, 10, 18, 28, 42, 60]

# steepest descent (fixed λ = 0.4): zig-zags down the long valley
start = np.array([-1.0, 6.5])
lam = 0.4
path_sd = [start.copy()]
pt = start.copy()
for _ in range(18):
    g = grad(*pt)
    pt = pt - lam * g
    path_sd.append(pt.copy())
path_sd = np.array(path_sd)

# Newton/LM: one step jumps to minimum for quadratic
path_lm = [start.copy()]
pt = start.copy()
for _ in range(2):
    g = grad(*pt)
    pt = pt - H_inv @ g
    path_lm.append(pt.copy())
path_lm = np.array(path_lm)

for ax, path, color, title, sub in zip(
    axes,
    [path_sd, path_lm],
    ["#dc2626", "#1d4ed8"],
    ["(a) 最陡下降法 Steepest Descent", "(b) Newton-Raphson / LM"],
    ["只用斜率(梯度)\n固定步長 λ,容易在狹長谷地 Z 字前進",
     "用斜率 + 曲率(Hessian)\n步長自動依曲率調整,一步逼近最低點"],
):
    cs = ax.contour(P1, P2, E, levels=levels, colors="#6b7280", linewidths=0.9,
                     alpha=0.7)
    ax.clabel(cs, fontsize=7, fmt="%.0f")
    ax.plot(path[:, 0], path[:, 1], "o-", color=color, lw=2, ms=6,
             label="迭代軌跡")
    ax.plot(path[0, 0], path[0, 1], "s", color="#111827", ms=12,
             label="起點")
    ax.plot(5, 3, "*", color="#059669", ms=20, label="真最小值")
    ax.set_xlabel("參數 p1")
    ax.set_ylabel("參數 p2")
    ax.set_title(f"{title}\n{sub}", fontsize=10.5)
    ax.legend(loc="upper right", fontsize=9)
    ax.set_xlim(-2, 12)
    ax.set_ylim(-1, 7)
    ax.set_aspect("equal")

fig.suptitle(
    "Helper 3:同一個誤差曲面、同一個起點,兩種策略的差別在於「有沒有用曲率」",
    fontsize=13, y=1.02)
fig.tight_layout()
fig.savefig(OUTDIR / "helper-3-gradient-vs-newton.png", dpi=140,
            bbox_inches="tight")
plt.close(fig)


# ----------------------------------------------------------------------------
# Helper 4: Nelder-Mead simplex operations on a 2D contour
# ----------------------------------------------------------------------------
fig, axes = plt.subplots(2, 2, figsize=(13, 11))

def err2(p1, p2):
    return 0.6 * (p1 - 4) ** 2 + 1.2 * (p2 - 3) ** 2

p1_grid = np.linspace(-1, 8, 200)
p2_grid = np.linspace(-1, 7, 200)
P1, P2 = np.meshgrid(p1_grid, p2_grid)
E = err2(P1, P2)
levels = [0.5, 2, 5, 10, 18, 28, 42]


def draw_triangle(ax, pts, color, alpha=0.25, lw=2, ls="-"):
    poly = Polygon(pts, closed=True, facecolor=color, alpha=alpha,
                    edgecolor=color, lw=lw, ls=ls)
    ax.add_patch(poly)


def label_vertices(ax, pts, labels, offsets):
    for pt, lab, off in zip(pts, labels, offsets):
        ax.plot(pt[0], pt[1], "o", color="#111827", ms=8, zorder=5)
        ax.annotate(lab, xy=pt, xytext=(pt[0] + off[0], pt[1] + off[1]),
                     fontsize=11, fontweight="bold")


# Common simplex: B (best) low error, O (intermediate), W (worst) far from min
B = np.array([3.0, 2.5])
O = np.array([5.0, 2.0])
W = np.array([6.0, 5.5])
mid_BO = (B + O) / 2
d_vec = mid_BO - W


def base_contour(ax, title):
    cs = ax.contour(P1, P2, E, levels=levels, colors="#6b7280",
                      linewidths=0.8, alpha=0.7)
    ax.plot(4, 3, "*", color="#059669", ms=18, zorder=4)
    ax.text(4.15, 3.1, "min", color="#059669", fontsize=10)
    ax.set_xlabel("p1"); ax.set_ylabel("p2")
    ax.set_title(title, fontsize=11.5)
    ax.set_xlim(-1, 8); ax.set_ylim(-1, 7)
    ax.set_aspect("equal")


# (a) Reflection
ax = axes[0, 0]
base_contour(ax, "(a) Reflection 反射\nW 越過 B–O 中點 m,翻到對面變成 W′")
W_new = W + 2 * d_vec  # length 2d
draw_triangle(ax, [B, O, W], "#9ca3af", alpha=0.18)
draw_triangle(ax, [B, O, W_new], "#1d4ed8", alpha=0.28)
ax.plot(*mid_BO, "x", color="#dc2626", ms=10, mew=2)
label_vertices(ax, [B, O, W, W_new, mid_BO],
                 ["B", "O", "W", "W′", "m"],
                 [(0.15, 0.1), (0.15, 0.1), (0.15, 0.1), (0.15, 0.1),
                  (0.1, -0.35)])
ax.annotate("", xy=W_new, xytext=W,
              arrowprops=dict(arrowstyle="->", color="#1d4ed8", lw=1.6,
                              connectionstyle="arc3,rad=0"))

# (b) Expansion
ax = axes[0, 1]
base_contour(ax, "(b) Expansion 擴張\n若 W′ 更好,順勢再延伸 d 變成 W″")
W_exp = W + 3 * d_vec
draw_triangle(ax, [B, O, W], "#9ca3af", alpha=0.18)
draw_triangle(ax, [B, O, W_new], "#1d4ed8", alpha=0.18)
draw_triangle(ax, [B, O, W_exp], "#059669", alpha=0.30)
label_vertices(ax, [B, O, W, W_new, W_exp],
                 ["B", "O", "W", "W′", "W″"],
                 [(0.15, 0.1), (0.15, 0.1), (0.15, 0.1), (0.15, 0.1),
                  (0.15, 0.1)])
ax.annotate("", xy=W_exp, xytext=W_new,
              arrowprops=dict(arrowstyle="->", color="#059669", lw=1.6))

# (c) Contraction
ax = axes[1, 0]
base_contour(ax, "(c) Contraction 收縮\n若反射沒改善,只走一半 (d/2) 變成 W′")
W_con = W + 0.5 * d_vec
draw_triangle(ax, [B, O, W], "#9ca3af", alpha=0.18)
draw_triangle(ax, [B, O, W_con], "#f59e0b", alpha=0.30)
label_vertices(ax, [B, O, W, W_con],
                 ["B", "O", "W", "W′"],
                 [(0.15, 0.1), (0.15, 0.1), (0.15, 0.1), (0.15, 0.1)])
ax.annotate("", xy=W_con, xytext=W,
              arrowprops=dict(arrowstyle="->", color="#f59e0b", lw=1.6))

# (d) Shrinkage
ax = axes[1, 1]
base_contour(ax, "(d) Shrinkage 縮小\n上面都失敗:O 和 W 都往 B 靠近一半")
O_new = (B + O) / 2
W_new_shrink = (B + W) / 2
draw_triangle(ax, [B, O, W], "#9ca3af", alpha=0.18)
draw_triangle(ax, [B, O_new, W_new_shrink], "#a21caf", alpha=0.30)
label_vertices(ax, [B, O, W, O_new, W_new_shrink],
                 ["B", "O", "W", "O′", "W′"],
                 [(0.15, 0.1), (0.15, 0.1), (0.15, 0.1), (0.15, 0.1),
                  (0.15, 0.1)])
ax.annotate("", xy=O_new, xytext=O,
              arrowprops=dict(arrowstyle="->", color="#a21caf", lw=1.4))
ax.annotate("", xy=W_new_shrink, xytext=W,
              arrowprops=dict(arrowstyle="->", color="#a21caf", lw=1.4))

fig.suptitle(
    "Helper 4:Nelder-Mead 單體法的四種變形 — 用三角形「爬」過誤差等高線",
    fontsize=13, y=1.0)
fig.tight_layout()
fig.savefig(OUTDIR / "helper-4-simplex-operations.png", dpi=140,
            bbox_inches="tight")
plt.close(fig)


print("All 4 helpers written to", OUTDIR)
