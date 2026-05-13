"""Helper illustrations for Lecture 08 — Model Validation.

Helpers:
  1. Geometry of validation (Mankin et al. 1977) — single S/M/Q Venn plus
     a 5-panel grid of the canonical relations (disjoint / partial / Q=S /
     M-subset-S / S-subset-M), each annotated with reliability/adequacy.
  2. The high-correlation trap — three scatter panels (slope error / bias
     error / both) with the 1:1 line and the regression line overlaid, so
     the reader can see why r alone is not enough.
  3. MSEP decomposition into MC + SC + RC — four hypothetical models
     compared on a stacked bar chart so the components are visible at a
     glance, with a brief verbal label for each model.
  4. Likelihood + AIC discrimination — left: the binomial likelihood
     L(theta) for the die example, MLE marked at theta=0.4 versus fair
     theta=1/6; right: RSS, ln L, and AIC for the four nested models on
     Fig. 8.7's data, illustrating how AIC trades fit against complexity.
"""
from pathlib import Path
import matplotlib.pyplot as plt
from matplotlib import font_manager
from matplotlib.patches import Ellipse, Circle, FancyArrowPatch
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
# Helper 1: Geometry of Validation (Mankin sets)
# ----------------------------------------------------------------------------
fig = plt.figure(figsize=(14, 6.2))
gs = fig.add_gridspec(2, 4, width_ratios=[1.5, 1, 1, 1], hspace=0.35, wspace=0.3)

# Big panel on left: canonical S/M/Q overlap
axL = fig.add_subplot(gs[:, 0])
axL.set_xlim(-2, 2.5)
axL.set_ylim(-2, 2.5)
axL.set_aspect("equal")
axL.axis("off")
# Universe P
axL.add_patch(plt.Rectangle((-1.95, -1.95), 4.4, 4.4, fill=False, edgecolor="0.5", linewidth=1.2))
axL.text(2.35, 2.25, "P 全部可測量的集合", ha="right", va="top", fontsize=10, color="0.4")
# S and M
axL.add_patch(Ellipse((-0.4, 0.35), width=2.6, height=2.2, angle=20,
                       fill=False, edgecolor="C0", linewidth=2.4))
axL.add_patch(Ellipse((0.7, -0.25), width=2.4, height=2.4, angle=-20,
                       fill=False, edgecolor="C3", linewidth=2.4))
axL.text(-1.35, 1.25, "S 系統的觀測", color="C0", fontsize=13, fontweight="bold")
axL.text(1.45, -1.35, "M 模型的預測", color="C3", fontsize=13, fontweight="bold")
axL.text(0.18, 0.05, "Q\n正確預測", ha="center", va="center",
         color="0.15", fontsize=11, fontweight="bold")
axL.text(0, 2.05, "圖 8.1 的幾何重畫",
         ha="center", va="center", fontsize=11, color="0.3")
# Annotations: reliability/adequacy ratios
axL.text(-1.85, -1.75,
         "可靠度 (reliability) = |Q| / |M|\n適切度 (adequacy)   = |Q| / |S|",
         fontsize=10, color="0.2",
         bbox=dict(boxstyle="round,pad=0.4", facecolor="0.97", edgecolor="0.7"))


def draw_pair(ax, S_xy, M_xy, S_r, M_r, label, sub):
    ax.set_xlim(-2, 2)
    ax.set_ylim(-2, 2)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.add_patch(plt.Rectangle((-1.95, -1.95), 3.9, 3.9, fill=False,
                               edgecolor="0.7", linewidth=0.8))
    ax.add_patch(Circle(S_xy, S_r, fill=False, edgecolor="C0", linewidth=1.8))
    ax.add_patch(Circle(M_xy, M_r, fill=False, edgecolor="C3", linewidth=1.8))
    ax.text(S_xy[0], S_xy[1] + S_r + 0.15, "S", color="C0",
            fontsize=12, fontweight="bold", ha="center")
    ax.text(M_xy[0], M_xy[1] - M_r - 0.25, "M", color="C3",
            fontsize=12, fontweight="bold", ha="center")
    ax.text(0, 1.78, label, fontsize=11, fontweight="bold", ha="center")
    ax.text(0, -1.78, sub, fontsize=9.5, color="0.3", ha="center")


# Panel (a): disjoint — no Q
ax_a = fig.add_subplot(gs[0, 1])
draw_pair(ax_a, (-0.85, 0.4), (0.85, -0.4), 0.85, 0.85,
          "(a) Q = ∅", "模型無用:M 與 S 完全沒交集")
# Panel (b): partial overlap — model useful but only partly adequate
ax_b = fig.add_subplot(gs[0, 2])
draw_pair(ax_b, (-0.55, 0.15), (0.7, 0.0), 1.0, 0.95,
          "(b) Q ⊂ M ∩ S", "模型有用,但只覆蓋部分觀測")
# Panel (c): Q = S, model is a superset — high adequacy, low reliability
ax_c = fig.add_subplot(gs[0, 3])
draw_pair(ax_c, (-0.05, 0.0), (0.0, 0.0), 0.7, 1.4,
          "(c) S ⊂ M, Q = S", "適切度 100%,可靠度低 (M 太大)")
# Panel (d): M ⊂ S, M = Q — high reliability, low adequacy
ax_d = fig.add_subplot(gs[1, 2])
draw_pair(ax_d, (0.0, 0.0), (0.0, 0.0), 1.4, 0.6,
          "(d) M ⊂ S, Q = M", "可靠度 100%,但只說明 S 一小塊")
# Panel (e): hardest — S and M nearly coincide
ax_e = fig.add_subplot(gs[1, 1])
draw_pair(ax_e, (0.0, 0.0), (0.05, 0.0), 1.0, 0.95,
          "(e) Q ≈ M ≈ S", "可靠度與適切度都接近 1(理想)")
# Bottom right cell: legend
ax_leg = fig.add_subplot(gs[1, 3])
ax_leg.axis("off")
ax_leg.text(0.5, 0.85, "五種 S / M / Q 關係", ha="center", fontsize=12, fontweight="bold")
ax_leg.text(0.05, 0.55,
            "• S = 系統可觀測量集合\n"
            "• M = 模型可預測量集合\n"
            "• Q = M ∩ S 中與資料一致者\n"
            "• |·| 表示集合大小(或機率質量)",
            fontsize=10, color="0.2", va="top")

fig.suptitle("圖 8-A:驗證的幾何 — Mankin 等人 (1977) 的集合觀點",
             fontsize=14, fontweight="bold", y=0.985)
fig.savefig(OUTDIR / "helper1-set-geometry.png", dpi=150, bbox_inches="tight")
plt.close(fig)
print("Wrote helper1-set-geometry.png")


# ----------------------------------------------------------------------------
# Helper 2: The high-correlation trap — three scatter pitfalls
# ----------------------------------------------------------------------------
fig, axes = plt.subplots(1, 3, figsize=(14.5, 4.8))

rng = np.random.default_rng(8)
x = np.linspace(0.5, 9.5, 14)


def fit_line(xs, ys):
    a, b = np.polyfit(xs, ys, 1)
    return a, b


def panel(ax, model_vals, obs_vals, title, diagnosis):
    ax.scatter(model_vals, obs_vals, s=46, color="C0",
               edgecolor="white", linewidth=0.7, zorder=4, label="觀測 vs 模型")
    grid = np.array([0, 10])
    ax.plot(grid, grid, "k-", linewidth=2, label="1:1 線(完美)")
    a, b = fit_line(model_vals, obs_vals)
    ax.plot(grid, a * grid + b, "--", color="C3", linewidth=2,
            label=f"最小平方回歸線 y = {a:.2f}x + {b:.2f}")
    r = np.corrcoef(model_vals, obs_vals)[0, 1]
    ax.set_xlim(0, 10); ax.set_ylim(0, 10)
    ax.set_xlabel("模型預測"); ax.set_ylabel("觀測值")
    ax.set_title(f"{title}\nr = {r:.3f}", fontsize=11)
    ax.text(0.04, 0.96, diagnosis, transform=ax.transAxes,
            va="top", ha="left", fontsize=9.5,
            bbox=dict(boxstyle="round,pad=0.4",
                      facecolor="#fff7d6", edgecolor="0.5"))
    ax.legend(loc="lower right", fontsize=8.5, framealpha=0.95)
    ax.grid(alpha=0.25)


# A: slope error — model under-predicts small, over-predicts large
obs_A = 0.6 * x + 1.5 + rng.normal(0, 0.3, x.size)
panel(axes[0], x, obs_A, "A:斜率錯誤(變異尺度錯)",
      "雖然 r ≈ 0.98,\n但回歸線斜率 ≠ 1,\n模型把小值高估、大值低估。")

# B: bias error — model consistently underestimates
obs_B = x - 2.0 + rng.normal(0, 0.3, x.size)
panel(axes[1], x, obs_B, "B:偏差錯誤(常數位移)",
      "r 一樣很高,\n但截距 ≠ 0:模型整體向下偏移,\n所有預測都被系統性低估。")

# C: bias + slope error
obs_C = 0.7 * x - 1.0 + rng.normal(0, 0.25, x.size)
panel(axes[2], x, obs_C, "C:偏差 + 斜率都錯",
      "截距 ≠ 0 且 斜率 ≠ 1,\n但相關係數仍 ≈ 0.99。\n\n結論:r 高 ≠ 模型對。")

fig.suptitle("圖 8-B:高相關的陷阱 — 為什麼只看 r 會被騙",
             fontsize=14, fontweight="bold", y=1.02)
fig.tight_layout()
fig.savefig(OUTDIR / "helper2-correlation-trap.png", dpi=150, bbox_inches="tight")
plt.close(fig)
print("Wrote helper2-correlation-trap.png")


# ----------------------------------------------------------------------------
# Helper 3: MSEP decomposition into MC + SC + RC
# ----------------------------------------------------------------------------
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5.2),
                                gridspec_kw={"width_ratios": [1.1, 1]})

# Construct four hypothetical model/obs pairs to give clearly different
# (MC, SC, RC) decompositions. We design X (model) and Y (obs) so that:
#   - case 1: pure bias  (mean shift, same slope, low noise)  -> MC dominant
#   - case 2: pure slope (mean equal, slope != 1, low noise)  -> SC dominant
#   - case 3: pure noise (mean equal, slope ~1, large noise)  -> RC dominant
#   - case 4: balanced mix
rng = np.random.default_rng(11)
n = 60
x_true = np.linspace(1, 9, n)

cases = []
# 1: bias
X1 = x_true.copy()
Y1 = X1 + 1.8 + rng.normal(0, 0.25, n)
cases.append(("僅偏差\n(MC 大)", X1, Y1))
# 2: slope
X2 = x_true.copy()
Y2 = 0.55 * X2 + (1 - 0.55) * X2.mean() + rng.normal(0, 0.25, n)
cases.append(("僅斜率\n(SC 大)", X2, Y2))
# 3: random
X3 = x_true.copy()
Y3 = X3 + rng.normal(0, 1.4, n)
cases.append(("僅雜訊\n(RC 大)", X3, Y3))
# 4: mix
X4 = x_true.copy()
Y4 = 0.75 * X4 + 0.9 + rng.normal(0, 0.7, n)
cases.append(("混合誤差", X4, Y4))


def decomp(X, Y):
    Xm, Ym = X.mean(), Y.mean()
    Sx, Sy = X.std(ddof=0), Y.std(ddof=0)
    r = np.corrcoef(X, Y)[0, 1]
    MSEP = np.mean((X - Y) ** 2)
    MC = (Xm - Ym) ** 2 / MSEP
    SC = (Sx - r * Sy) ** 2 / MSEP
    RC = (1 - r * r) * Sy * Sy / MSEP
    return MSEP, MC, SC, RC


# Left: stacked bar of fractional decomposition
labels = [c[0] for c in cases]
MSEPs, MCs, SCs, RCs = [], [], [], []
for _, X, Y in cases:
    msep, mc, sc, rc = decomp(X, Y)
    MSEPs.append(msep); MCs.append(mc); SCs.append(sc); RCs.append(rc)

xpos = np.arange(len(cases))
ax1.bar(xpos, MCs, label="MC(均值偏差)", color="#d97757")
ax1.bar(xpos, SCs, bottom=MCs, label="SC(斜率偏差)", color="#f0c674")
ax1.bar(xpos, RCs, bottom=np.array(MCs) + np.array(SCs),
        label="RC(隨機誤差)", color="#7da9c4")
for i, m in enumerate(MSEPs):
    ax1.text(i, 1.04, f"MSEP={m:.2f}", ha="center", fontsize=10, color="0.2")
ax1.set_xticks(xpos)
ax1.set_xticklabels(labels, fontsize=10)
ax1.set_ylim(0, 1.18)
ax1.set_ylabel("佔 MSEP 的比例")
ax1.set_title("MSEP = MC + SC + RC(分數和恆為 1)", fontsize=12, fontweight="bold")
ax1.legend(loc="upper right", fontsize=9.5)
ax1.grid(axis="y", alpha=0.25)
ax1.axhline(1.0, color="0.4", linestyle=":", linewidth=0.8)

# Right: scatter for case 4 with annotation of what each component captures
X, Y = cases[3][1], cases[3][2]
ax2.scatter(X, Y, s=30, color="C0", edgecolor="white", linewidth=0.5, zorder=4)
grid = np.array([0, 11])
ax2.plot(grid, grid, "k-", linewidth=1.8, label="1:1 線")
a, b = np.polyfit(X, Y, 1)
ax2.plot(grid, a * grid + b, "--", color="C3", linewidth=1.8,
         label=f"資料對模型的回歸 (斜率={a:.2f})")
ax2.axhline(Y.mean(), color="C0", linestyle=":", linewidth=1, alpha=0.7)
ax2.axvline(X.mean(), color="C3", linestyle=":", linewidth=1, alpha=0.7)
ax2.annotate("均值差 → MC\n(mean Y − mean X)²",
             xy=(X.mean(), Y.mean()),
             xytext=(X.mean() + 1.5, Y.mean() - 2.4),
             fontsize=9.5,
             arrowprops=dict(arrowstyle="->", color="0.4"))
ax2.annotate("斜率偏離 1 → SC",
             xy=(8, a * 8 + b),
             xytext=(2.5, 8.5),
             fontsize=9.5,
             arrowprops=dict(arrowstyle="->", color="0.4"))
ax2.annotate("殘餘散佈 → RC",
             xy=(X[5], Y[5]),
             xytext=(0.5, 5.5),
             fontsize=9.5,
             arrowprops=dict(arrowstyle="->", color="0.4"))
ax2.set_xlim(0, 11); ax2.set_ylim(0, 11)
ax2.set_xlabel("模型預測 X"); ax2.set_ylabel("觀測值 Y")
ax2.set_title("混合誤差案例:三種成份在資料中的位置", fontsize=12, fontweight="bold")
ax2.legend(loc="lower right", fontsize=9.5)
ax2.grid(alpha=0.25)

fig.suptitle("圖 8-C:把 MSEP 拆成三塊 — 偏差(MC)+ 斜率(SC)+ 隨機(RC)",
             fontsize=14, fontweight="bold", y=1.02)
fig.tight_layout()
fig.savefig(OUTDIR / "helper3-msep-decomp.png", dpi=150, bbox_inches="tight")
plt.close(fig)
print("Wrote helper3-msep-decomp.png")


# ----------------------------------------------------------------------------
# Helper 4: Likelihood curve + AIC complexity-vs-fit trade-off
# ----------------------------------------------------------------------------
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13.5, 5.2))

# Left panel: binomial likelihood for n=5, x=2 (the "is the die fair?" case)
theta = np.linspace(1e-3, 1 - 1e-3, 400)
from math import comb
L = comb(5, 2) * theta ** 2 * (1 - theta) ** 3
mle = theta[np.argmax(L)]
true_fair = 1 / 6

ax1.plot(theta, L, color="C0", linewidth=2.2, label="L(θ | n=5, x=2)")
ax1.axvline(mle, color="C3", linestyle="--", linewidth=1.6,
            label=f"MLE θ_hat = {mle:.2f}(最有可能的 θ)")
ax1.axvline(true_fair, color="0.3", linestyle=":", linewidth=1.6,
            label=f"公正骰子 θ = 1/6 ≈ {true_fair:.3f}")
# Mark L(MLE) and L(1/6) as horizontal sticks to show ratio
L_mle = L.max()
L_fair = comb(5, 2) * true_fair ** 2 * (1 - true_fair) ** 3
ax1.plot([mle, mle], [0, L_mle], color="C3", linewidth=1.4, alpha=0.5)
ax1.plot([true_fair, true_fair], [0, L_fair], color="0.3", linewidth=1.4, alpha=0.6)
ratio = L_mle / L_fair
ax1.annotate(f"似然比 R = L(0.4) / L(1/6) ≈ {ratio:.2f}",
             xy=(0.42, L_mle * 0.96),
             xytext=(0.55, 0.31),
             fontsize=10.5,
             arrowprops=dict(arrowstyle="->", color="0.3"),
             bbox=dict(boxstyle="round,pad=0.35",
                       facecolor="#fff7d6", edgecolor="0.5"))
ax1.set_xlabel("骰子出某一面的機率 θ")
ax1.set_ylabel("Likelihood L(θ)")
ax1.set_title("似然函數:把 θ 當變數,資料當已知\n"
              "(擲 5 次出現 2 次 3 點 — 骰子公正嗎?)", fontsize=11)
ax1.set_xlim(0, 1)
ax1.set_ylim(0, max(L) * 1.15)
ax1.legend(loc="upper right", fontsize=9.5)
ax1.grid(alpha=0.25)

# Right panel: AIC trade-off for the 4 models on Fig 8.7 data
# Reproduce Table 8.5 figures approximately
models = ["M1\ny=a1·x", "M2\ny=a0+a1·x", "M3\ny=a0+a1·x+a2·x²", "M4\ny=a3·exp(a4·x)"]
K_params = [2, 3, 4, 3]  # number of estimated params incl sigma^2
RSS = [28.465, 22.473, 12.773, 11.854]
n_data = 4
neg2lnL = [n_data * np.log(r / n_data) + n_data * (np.log(2 * np.pi) + 1) for r in RSS]
AIC = [a + 2 * k for a, k in zip(neg2lnL, K_params)]
AIC_min = min(AIC)
Delta = [a - AIC_min for a in AIC]

xpos = np.arange(len(models))
w = 0.35
ax2.bar(xpos - w/2, neg2lnL, width=w, color="#7da9c4", label="−2 ln L (失配懲罰)")
ax2.bar(xpos + w/2, [2 * k for k in K_params], width=w, color="#d97757",
        label="2K (複雜度懲罰)")
# Plot AIC line on top
ax2_t = ax2.twinx()
ax2_t.plot(xpos, AIC, "o-", color="0.15", linewidth=2.2, markersize=9,
           label="AIC = −2 ln L + 2K")
for i, (a, d) in enumerate(zip(AIC, Delta)):
    ax2_t.annotate(f"AIC={a:.1f}\nΔ={d:.1f}", (xpos[i], a),
                   textcoords="offset points", xytext=(0, 12),
                   ha="center", fontsize=9, color="0.15")
ax2.set_xticks(xpos)
ax2.set_xticklabels(models, fontsize=9.5)
ax2.set_ylabel("懲罰大小")
ax2_t.set_ylabel("AIC(越小越好)", color="0.15")
ax2.set_title("AIC 是兩種懲罰的加總:配適得越好越省 −2 ln L,\n"
              "但每多用一個參數要再付 2 點", fontsize=11)
ax2.legend(loc="upper left", fontsize=9)
ax2_t.legend(loc="upper right", fontsize=9)
ax2.grid(axis="y", alpha=0.25)
ax2_t.set_ylim(min(AIC) - 5, max(AIC) + 5)

fig.suptitle("圖 8-D:從似然函數到 AIC — 模型辨別的兩條路徑",
             fontsize=14, fontweight="bold", y=1.02)
fig.tight_layout()
fig.savefig(OUTDIR / "helper4-likelihood-aic.png", dpi=150, bbox_inches="tight")
plt.close(fig)
print("Wrote helper4-likelihood-aic.png")

print("\nAll Lec 08 helpers rendered.")
