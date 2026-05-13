"""Generate fresh helper illustrations for Lecture 02 of the BSMA redesign.

Helpers:
  1. Classical View 6-stage pipeline
  2. Polya 4 steps ↔ modeling 6 stages correspondence
  3. Exponential vs logistic trajectories (the two competing models in §2.3)
  4. Doubling time: density-independent (constant) vs density-dependent
     (grows then becomes impossible)
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
# Helper 1: Classical View — 6-stage pipeline with feedback arrow
# ----------------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(13, 4.3))
ax.set_xlim(0, 13)
ax.set_ylim(-0.2, 3.5)
ax.axis("off")

stages = [
    ("1. Objectives\n目標", "#ed8936"),
    ("2. Hypotheses\n假設", "#dd6b20"),
    ("3. Mathematical\nFormulation\n數學公式化", "#c05621"),
    ("4. Verification\n驗證(程式對嗎?)", "#9c4221"),
    ("5. Calibration\n校正(參數估計)", "#7b341e"),
    ("6. Analysis &\nEvaluation\n分析與評估", "#652b19"),
]

n = len(stages)
x_centers = np.linspace(1, 12, n)
for i, ((label, color), x) in enumerate(zip(stages, x_centers)):
    box = mpatches.FancyBboxPatch(
        (x - 0.85, 1.5), 1.7, 1.6, boxstyle="round,pad=0.06",
        linewidth=1.8, edgecolor=color, facecolor="white",
    )
    ax.add_patch(box)
    ax.text(x, 2.3, label, fontsize=9.5, ha="center", va="center",
            color=color, fontweight="bold")
    if i < n - 1:
        ax.annotate("", xy=(x_centers[i+1] - 0.85, 2.3),
                    xytext=(x + 0.85, 2.3),
                    arrowprops=dict(arrowstyle="->", linewidth=2,
                                    color="#4a5568"))

# Feedback arrow (Analysis fails → back to Hypotheses)
ax.annotate(
    "", xy=(x_centers[1], 1.4), xytext=(x_centers[-1], 1.4),
    arrowprops=dict(arrowstyle="->", linewidth=1.8, color="#c53030",
                    connectionstyle="arc3,rad=0.3", linestyle="--"),
)
ax.text((x_centers[1] + x_centers[-1]) / 2, 0.55,
        "若驗收失敗 → 修正假設或公式,重做一遍",
        fontsize=10.5, ha="center", color="#c53030", style="italic")

ax.set_title("經典觀點 (Classical View):建模的 6 個循序階段",
             fontsize=14, pad=12, color="#7b341e")
plt.savefig(OUTDIR / "helper-1-classical-view-pipeline.png",
            dpi=160, bbox_inches="tight", facecolor="white")
plt.close()


# ----------------------------------------------------------------------------
# Helper 2: Polya 4 steps ↔ Modeling stages
# ----------------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(11, 5.8))
ax.set_xlim(0, 11)
ax.set_ylim(-0.2, 5.5)
ax.axis("off")

polya = [
    ("Polya 第 1 步\n理解問題", "建模:\n寫 Objectives + Hypotheses"),
    ("Polya 第 2 步\n擬定計畫", "建模:\nMathematical Formulation"),
    ("Polya 第 3 步\n執行計畫", "建模:\nVerification + Calibration\n→ 跑模型得答案"),
    ("Polya 第 4 步\n檢查答案", "建模:\nAnalysis & Evaluation\n→ 模型是否合理?"),
]

for i, (left, right) in enumerate(polya):
    y = 4.5 - i * 1.15
    # left box (Polya)
    lbox = mpatches.FancyBboxPatch(
        (0.3, y - 0.45), 3.6, 0.9, boxstyle="round,pad=0.06",
        linewidth=1.8, edgecolor="#2b6cb0", facecolor="#ebf8ff",
    )
    ax.add_patch(lbox)
    ax.text(2.1, y, left, fontsize=10.5, ha="center", va="center",
            color="#2b6cb0", fontweight="bold")

    # arrow
    ax.annotate("", xy=(6.4, y), xytext=(4.0, y),
                arrowprops=dict(arrowstyle="->", linewidth=2,
                                color="#4a5568"))
    ax.text(5.2, y + 0.32, "對應到", fontsize=9.5, ha="center", color="#4a5568")

    # right box (modeling)
    rbox = mpatches.FancyBboxPatch(
        (6.5, y - 0.55), 4.2, 1.1, boxstyle="round,pad=0.06",
        linewidth=1.8, edgecolor="#22543d", facecolor="#f0fff4",
    )
    ax.add_patch(rbox)
    ax.text(8.6, y, right, fontsize=10, ha="center", va="center",
            color="#22543d")

ax.set_title("Polya 的 4 步解題 ↔ 建模的 6 個階段",
             fontsize=14, pad=14, color="#2d3748")
plt.savefig(OUTDIR / "helper-2-polya-vs-modeling.png",
            dpi=160, bbox_inches="tight", facecolor="white")
plt.close()


# ----------------------------------------------------------------------------
# Helper 3: Exponential vs logistic trajectories
# ----------------------------------------------------------------------------
fig, axes = plt.subplots(1, 2, figsize=(12, 5), sharey=False)

r = 0.10
K = 1000.0
N0 = 50.0
T = 60

# Density-independent (exponential): N_{t+1} = (1+r) N_t
N_exp = [N0]
for _ in range(T):
    N_exp.append(N_exp[-1] * (1 + r))

# Density-dependent (logistic):  N_{t+1} = N_t + r N_t (1 - N_t/K)
N_log = [N0]
for _ in range(T):
    n = N_log[-1]
    N_log.append(n + r * n * (1 - n / K))

t = np.arange(T + 1)

ax = axes[0]
ax.plot(t, N_exp, color="#2b6cb0", linewidth=2.5,
        label=r"密度無關(指數):$N_{t+1} = (1+r)\,N_t$")
ax.axhline(2 * N0, color="#718096", linestyle=":", linewidth=1)
ax.text(T * 0.85, 2 * N0 + 60, "$2 N_0$", fontsize=10, color="#718096")
ax.set_xlim(0, T)
ax.set_ylim(0, max(N_exp) * 1.05)
ax.set_xlabel("時間 $t$", fontsize=12)
ax.set_ylabel("族群數 $N_t$", fontsize=12)
ax.set_title("第一模型:指數成長(無上限)", fontsize=13)
ax.grid(alpha=0.25, linestyle="--")
ax.legend(loc="upper left", fontsize=10)

ax = axes[1]
ax.plot(t, N_log, color="#c53030", linewidth=2.5,
        label=r"密度有關(logistic):$N_{t+1} = N_t + r N_t (1 - N_t/K)$")
ax.axhline(K, color="#22543d", linestyle="--", linewidth=1.3, alpha=0.8)
ax.text(T * 0.05, K - 70, "承載量 $K$", fontsize=11, color="#22543d")
ax.axhline(2 * N0, color="#718096", linestyle=":", linewidth=1)
ax.text(T * 0.85, 2 * N0 + 30, "$2 N_0$", fontsize=10, color="#718096")
ax.set_xlim(0, T)
ax.set_ylim(0, K * 1.12)
ax.set_xlabel("時間 $t$", fontsize=12)
ax.set_ylabel("族群數 $N_t$", fontsize=12)
ax.set_title("第二模型:Logistic 成長(趨於 $K$)", fontsize=13)
ax.grid(alpha=0.25, linestyle="--")
ax.legend(loc="lower right", fontsize=10)

fig.suptitle(f"同一個 $r = {r}$、$N_0 = {int(N0)}$ ,兩個模型給出截然不同的軌跡",
             fontsize=14, y=1.02)
plt.tight_layout()
plt.savefig(OUTDIR / "helper-3-exponential-vs-logistic.png",
            dpi=160, bbox_inches="tight", facecolor="white")
plt.close()


# ----------------------------------------------------------------------------
# Helper 4: Doubling time comparison (constant vs N_0-dependent)
# ----------------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(11, 5.5))

r = 0.10
K = 1000.0

# First model: doubling time t_d = ln(2)/ln(1+r) — constant in N_0
t_d_exp = np.log(2) / np.log(1 + r)

# Second model: simulate doubling time numerically as a function of N_0
N0_values = np.linspace(10, 0.99 * K, 200)
t_d_log = []
for N0 in N0_values:
    target = 2 * N0
    if target >= K:
        t_d_log.append(np.nan)
        continue
    n = N0
    t = 0
    while n < target and t < 1000:
        n = n + r * n * (1 - n / K)
        t += 1
    t_d_log.append(t if n >= target else np.nan)

ax.axhline(t_d_exp, color="#2b6cb0", linewidth=2.5, linestyle="-",
           label=fr"第一模型 (density-independent):$t_d = \frac{{\ln 2}}{{\ln(1+r)}} \approx {t_d_exp:.2f}$ (不依賴 $N_0$)")
ax.plot(N0_values, t_d_log, color="#c53030", linewidth=2.5,
        label="第二模型 (logistic):$t_d$ 隨 $N_0$ 變大而急速上升,在 $N_0 = K/2$ 之後翻倍不可能")

# Mark K/2
ax.axvline(K / 2, color="#22543d", linestyle="--", linewidth=1.2, alpha=0.7)
ax.text(K / 2 + 10, 80, "$N_0 = K/2$:\n再翻一倍會超過 $K$\n→ 永遠不會翻倍", fontsize=10,
        color="#22543d")

ax.set_xlabel("起始族群 $N_0$", fontsize=12)
ax.set_ylabel("翻倍時間 $t_d$", fontsize=12)
ax.set_xlim(0, K)
ax.set_ylim(0, 120)
ax.set_title(f"翻倍時間:兩個模型給出完全不同的答案(同樣 $r = {r}$、$K = {int(K)}$)",
             fontsize=13)
ax.grid(alpha=0.25, linestyle="--")
ax.legend(loc="upper left", fontsize=10.5)

plt.tight_layout()
plt.savefig(OUTDIR / "helper-4-doubling-time-comparison.png",
            dpi=160, bbox_inches="tight", facecolor="white")
plt.close()


print("Done. Wrote:")
for p in sorted(OUTDIR.glob("helper-*.png")):
    print(" ", p.name, f"({p.stat().st_size} bytes)")
