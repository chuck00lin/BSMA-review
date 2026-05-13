"""
================================================================================
教育版:鉛三隔室模型模擬(2020 期中 P2)
================================================================================

這份程式碼是 `fig2_simulations.py` 的「教學版」——產出的圖是純英文乾淨版,
程式碼有大量註解,解釋**為什麼這樣寫**。

對應的觀念:
  - [03-質性建模與Forrester圖.md §3.3.4 隔室模型]
  - [04-量化建模I.md §4.3.5 線性 ODE 系統]
  - [05-量化建模II.md §5.2.2 守恆檢查]
  - [06-數值技巧.md §6.1–§6.3 RK / solve_ivp / stiff 系統]
  - [09-模型分析.md 多時間尺度 / slow manifold]

**初值很重要**——這題給了兩組 IC,**揭露的是「不同時間尺度的故事」**:
  IC1: x = (0, 0, 0)        — 健康人剛開始接觸鉛,看「累積過程」
  IC2: x = (1800, 1800, 1800) — 已暴露的人,看「短期重分布」 vs 「長期歸宿」

================================================================================
"""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

OUTDIR = Path(__file__).parent


# ==============================================================================
# 第 0 步:參數
# ==============================================================================
# 單位:I1 為 μg/day,k 為 day^{-1}
#
# **關鍵觀察**:k13 = 0.000035 day⁻¹,半衰期 = ln(2)/k13 ≈ 19,805 day ≈ 54 yr。
# 其他 k 都在 0.01 量級,半衰期約 30–60 天。
# **三個數量級的尺度差** → 多時間尺度系統 → 短期 (800 day) 跟長期 (8000 day)
# 看到完全不一樣的故事。
I1 = 49.3
k01, k21, k31 = 0.0211, 0.0111, 0.0039
k02, k12, k13 = 0.0162, 0.0124, 0.000035


# ==============================================================================
# 第 1 步:把 ODE 寫成 Python 函式
# ==============================================================================
# scipy.integrate.solve_ivp 要求 rhs(t, y) 簽名:
#   - 第一個參數是時間(這題 ODE 不直接依賴 t,但介面仍要)
#   - 第二個參數是狀態向量
# 我們用 `_t` 做底線命名,表示「拿到但不會用」。
def rhs(_t, x):
    """三個隔室的時間導數."""
    x1, x2, x3 = x
    return [
        -(k01 + k21 + k31) * x1 + k12 * x2 + k13 * x3 + I1,   # blood
        k21 * x1 - (k02 + k12) * x2,                          # tissues
        k31 * x1 - k13 * x3,                                  # bones
    ]


# ==============================================================================
# 第 2 步:用代數解平衡點(sanity check)
# ==============================================================================
# 平衡時 dx/dt = 0。從最簡單的兩條解起:
#   - x2 方程式:k21·x1 = (k02+k12)·x2  →  x2* = k21/(k02+k12) · x1*
#   - x3 方程式:k31·x1 = k13·x3        →  x3* = k31/k13 · x1*
# 把這兩個代回 x1 方程式整理,得到 x1* 的閉式:
#   x1* = I1 / (k01 + k21·k02/(k02+k12))
x1_eq = I1 / (k01 + k21 * k02 / (k02 + k12))
x2_eq = k21 * x1_eq / (k02 + k12)
x3_eq = k31 * x1_eq / k13

# 守恆檢查:平衡時流入 = 流出,即 I1 = k01·x1* + k02·x2*
flux_in = I1
flux_out_eq = k01 * x1_eq + k02 * x2_eq

print(f"Analytic equilibrium:")
print(f"  x1* (blood)   = {x1_eq:>10.2f}  μg")
print(f"  x2* (tissues) = {x2_eq:>10.2f}  μg")
print(f"  x3* (bones)   = {x3_eq:>10.2f}  μg")
print(f"Conservation check at equilibrium:")
print(f"  I1            = {flux_in:>10.2f}  μg/day")
print(f"  k01·x1*+k02·x2*= {flux_out_eq:>10.2f}  μg/day   (應該等於 I1)")


# ==============================================================================
# 第 3 步:挑數值積分器
# ==============================================================================
# **為什麼用 `solve_ivp` 而不是 Euler?**
#   - Euler 法是 explicit、一階,誤差累積快。
#   - 這題 8000 天的時程,若用 Δt=1 的 Euler,誤差會堆得很可觀。
#   - `solve_ivp` 預設 'RK45'(Dormand-Prince),自適應步長 + 五階精度,
#     對「中等 stiff」的線性 ODE 既快又準。
#   - 我們用嚴格的 `rtol=1e-9, atol=1e-12` 確保精度高(這是線性問題,
#     不會難收斂),這樣 8000 天的長期積分才不會偏離理論平衡。
#   - `max_step=2.0` (天) 限制最大步長:對短期 800 天積分,避免步長
#     大到「跳過」前 30 天的快速上升。
#
# **如果這個系統 stiff 怎麼辦?** 用 method='BDF' 或 'LSODA'(隱式)。
# 這題的特徵值差三個數量級——其實邊緣 stiff,但 RK45 還能應付。
# 若擴展到更病態的系統,要切換到 stiff solver(§6.3.2)。
INTEGRATOR_KW = dict(rtol=1e-9, atol=1e-12, max_step=2.0)


def simulate(ic, t_end, n_points=2000):
    """跑一次模擬,回傳 (t, x1, x2, x3)."""
    t_eval = np.linspace(0, t_end, n_points)
    sol = solve_ivp(rhs, (0, t_end), ic, t_eval=t_eval, **INTEGRATOR_KW)
    return sol.t, sol.y


# ==============================================================================
# 第 4 步:跑模擬 —— 兩組 IC × 兩個時間尺度
# ==============================================================================
# **為什麼是 2×2 panel?**
#   - 行 = 兩組 IC(分別代表「沒接觸過」與「已暴露」的人)
#   - 列 = 兩個時間尺度(短期 800 天看 blood/tissues 的快動力,
#                        長期 8000 天看 bones 的慢累積)
# 這是「multiple time-scale sysetm」最自然的呈現方式。
ICs = [
    ("IC1: x = (0, 0, 0)",       [0.0,    0.0,    0.0]),
    ("IC2: x = (1800, 1800, 1800)", [1800.0, 1800.0, 1800.0]),
]
horizons = [800, 8000]


# ==============================================================================
# 第 5 步:畫 2×2 panel(英文乾淨版)
# ==============================================================================
plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "axes.unicode_minus": False,
    "axes.spines.top": False,
    "axes.spines.right": False,
})

colors = {"x1": "#d62728", "x2": "#1f77b4", "x3": "#8c564b"}
labels = {"x1": r"$x_1$  blood",
          "x2": r"$x_2$  tissues",
          "x3": r"$x_3$  bones"}

fig, axes = plt.subplots(2, 2, figsize=(13, 8.0))

for row, (ic_name, ic) in enumerate(ICs):
    for col, T in enumerate(horizons):
        ax = axes[row, col]
        t, y = simulate(ic, T)
        for i, key in enumerate(["x1", "x2", "x3"]):
            ax.plot(t, y[i], lw=2.0, color=colors[key], label=labels[key])
        # Equilibrium horizontal lines (dotted)
        for eq, key in zip([x1_eq, x2_eq, x3_eq], ["x1", "x2", "x3"]):
            ax.axhline(eq, ls=":", color=colors[key], alpha=0.5, lw=1.2)

        ax.set_title(f"{ic_name}   ·   T = {T} days",
                     fontsize=11, loc="left")
        ax.set_xlabel("time (days)")
        ax.set_ylabel(r"lead amount ($\mu$g)")
        ax.grid(True, alpha=0.3)

        # 長期 panel 用 log y 才看得到 bones 慢慢爬升的全貌
        if T == 8000:
            ax.set_yscale("log")
            ax.set_ylim(0.5, 5e5)
        else:
            ax.set_ylim(-100, 3200)

        ax.legend(loc="lower right", fontsize=9, frameon=False)

# 在右下 panel 標出「54 年才能達到」的 bones 平衡
axes[1, 1].annotate(rf"$x_3^* \approx {x3_eq:.0f}\,\mu$g"
                    + "\n(reachable only after ~54 yr)",
                    xy=(7500, x3_eq), xytext=(3500, x3_eq * 0.35),
                    color="#8c564b", fontsize=10,
                    arrowprops=dict(arrowstyle="->", color="#8c564b"))

fig.suptitle("Lead 3-compartment model:  2 ICs × 2 time horizons",
             fontsize=13, fontweight="bold", y=1.00)
fig.tight_layout()

outpath = OUTDIR / "fig2_simulations_clean.png"
fig.savefig(outpath, dpi=150, bbox_inches="tight")
print(f"\nFigure written to: {outpath}")
