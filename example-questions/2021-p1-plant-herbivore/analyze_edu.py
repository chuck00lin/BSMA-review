"""
================================================================================
教育版:植物–食草者無因次模型分析(2021 期中 P1)
================================================================================

這份程式碼是 `fig1_phase_portrait.py` + `fig2_time_series.py` 的「教學版」
——產出乾淨英文 phase portrait + 時序圖,程式碼有大量註解。

無因次模型:
    du/dτ = β − γ u (v − 1)
    dv/dτ = v (1 − v/u)

對應的觀念:
  - [05-量化建模II.md §5.2.3 無因次化]
  - [09-模型分析.md §9.3.1 平衡點 / §9.3.3 Nullclines / phase plane]
  - [06-數值技巧.md §6.1 ODE 數值積分]

**「初值很重要」在這題的意義**:
  (a) 模型的「參數初值」 β, γ —— 挑(2, 1)是為了讓 phase portrait 結構**清晰**:
      - β/γ = 2 讓 u-nullcline 跟 v-nullcline 在合理位置交會
      - γ 不太大也不太小,讓向量場有適度傾斜
  (b) 軌跡的「狀態初值」(u₀, v₀) —— 我們挑四個角落點,讓讀者一眼看出
      所有軌跡都收斂到同一個 (u*, v*) 焦點。

================================================================================
"""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

OUTDIR = Path(__file__).parent


# ==============================================================================
# 第 0 步:挑參數
# ==============================================================================
# (β, γ) 的選擇邏輯:
#   - β 大 → 品質基線補充強 → 平衡值 u* 大(植物常保高品質)
#   - γ 大 → 食草壓力對品質反應快 → 系統反應劇烈,振盪更明顯
# 挑 β=2, γ=1 的理由:
#   1) 平衡點落在 (u*, v*) ≈ (2, 2),圖內可見、可標注
#   2) Jacobian 的判別式恰好讓我們看到「穩定 spiral」(複根),
#      軌跡會繞著平衡點旋進來——是教學上最戲劇化的情況
#   3) 不挑太極端的值,讓 nullcline 在 (0, 4)×(0, 4) 範圍內都看得到
BETA, GAMMA = 2.0, 1.0


# ==============================================================================
# 第 1 步:ODE 與平衡點(代數解)
# ==============================================================================
def rhs(_t, y, beta, gamma):
    u, v = y
    du = beta - gamma * u * (v - 1.0)
    dv = v * (1.0 - v / u) if u > 0 else 0.0
    return [du, dv]


# 平衡點:v = u(取非零解),代入 dv = 0 後 → γu² - γu - β = 0
# 解二次方程取正根:u* = (1 + sqrt(1 + 4β/γ))/2
u_star = 0.5 * (1.0 + np.sqrt(1.0 + 4.0 * BETA / GAMMA))
v_star = u_star

print(f"Equilibrium at (β, γ) = ({BETA}, {GAMMA}):")
print(f"  u* = v* = {u_star:.4f}")
print(f"  meaning: 食草者密度等於 {u_star:.2f} 倍 I_0,品質維持在這個對應水平")


# ==============================================================================
# 第 2 步:向量場(quiver)
# ==============================================================================
# 用 meshgrid 在 (u, v) 平面上佈點。**為什麼要正規化箭頭?**
# 因為原始 du/dt 在不同區域大小差很多 —— 不正規化的話只有靠近平衡的地方
# 看得到箭頭,遠處箭頭會「衝出畫面」。
# 正規化後**用顏色(M)**編碼速度大小(深=快、淺=慢)。
u_max, v_max = 4.0, 4.0
N_GRID = 22
U, V = np.meshgrid(np.linspace(0.05, u_max, N_GRID),
                   np.linspace(0.05, v_max, N_GRID))
DU = BETA - GAMMA * U * (V - 1.0)
DV = V * (1.0 - V / U)
M = np.sqrt(DU**2 + DV**2)
M[M == 0] = 1.0
DUn, DVn = DU / M, DV / M


# ==============================================================================
# 第 3 步:Nullclines(代數線)
# ==============================================================================
# 兩條 v-nullcline:v = 0(x 軸)和 v = u(45° 線)
# 一條 u-nullcline:u(v-1) = β/γ → v = 1 + (β/γ)/u
u_line = np.linspace(0.05, u_max, 400)
v_unull = 1.0 + (BETA / GAMMA) / u_line


# ==============================================================================
# 第 4 步:幾條代表性軌跡
# ==============================================================================
# **挑 IC 的策略**:四個「角落」起點,確保軌跡覆蓋四個象限。
# 這樣讀者一眼能看出「不管從哪裡出發都收斂到同一個 (u*, v*)」。
TRAJ_ICs = [(0.3, 0.3), (3.5, 0.5), (0.5, 3.5), (3.5, 3.5)]
T_END = 30.0  # 跑夠長以確保看到收斂

# **為什麼 max_step = 0.1?** 軌跡在 spiral 時局部曲率大,
# 預設步長可能跳得太遠導致曲線「卡角」。0.1 讓繪圖平滑。
INTEGRATOR_KW = dict(rtol=1e-7, atol=1e-9, max_step=0.1)


def trace(ic, t_end=T_END):
    sol = solve_ivp(rhs, (0, t_end), ic, args=(BETA, GAMMA),
                    dense_output=True, **INTEGRATOR_KW)
    return sol.y


# ==============================================================================
# 第 5 步:畫圖
# ==============================================================================
plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "axes.unicode_minus": False,
    "axes.spines.top": False,
    "axes.spines.right": False,
})

fig, axes = plt.subplots(1, 2, figsize=(14, 6.5))

# -----  左圖:Phase portrait  ----------------------------------
ax = axes[0]

# 向量場(灰階,深=快)
ax.quiver(U, V, DUn, DVn, M, cmap="Greys", scale=30, width=0.0035, alpha=0.7)

# Nullclines
ax.plot(u_line, u_line, lw=2.2, color="#1f77b4",
        label=r"$v$-nullcline:  $v = u$")
ax.axhline(0.0, lw=1.2, ls=":", color="#1f77b4", alpha=0.6)
ax.plot(u_line, v_unull, lw=2.2, color="#d62728",
        label=r"$u$-nullcline:  $v = 1 + (\beta/\gamma)/u$")

# 軌跡
traj_colors = ["#2ca02c", "#9467bd", "#ff7f0e", "#17becf"]
for ic, c in zip(TRAJ_ICs, traj_colors):
    y = trace(ic)
    ax.plot(y[0], y[1], lw=1.6, color=c, alpha=0.9)
    ax.plot(ic[0], ic[1], "s", ms=6, color=c)

# 平衡點
ax.plot(u_star, v_star, "o", ms=12, mec="black", mfc="gold", zorder=5,
        label=fr"equilibrium  $(u^*, v^*) = ({u_star:.2f}, {v_star:.2f})$")

# 區域標注:induced vs overgrazing
ax.text(2.7, 0.6, "induced defence\n($v < 1$ → boost $q$)",
        fontsize=9, color="#444",
        bbox=dict(boxstyle="round,pad=0.3", fc="#eef", ec="#88a"))
ax.text(2.7, 3.0, "overgrazing\n($v > 1$ → reduce $q$)",
        fontsize=9, color="#444",
        bbox=dict(boxstyle="round,pad=0.3", fc="#fee", ec="#a88"))

ax.set_xlabel(r"$u = q/(K_4 I_0)$   (dimensionless quality)")
ax.set_ylabel(r"$v = I/I_0$   (dimensionless herbivore density)")
ax.set_title(fr"(a)  Phase portrait  ($\beta = {BETA}$, $\gamma = {GAMMA}$)",
             fontweight="bold", loc="left")
ax.set_xlim(0, u_max)
ax.set_ylim(0, v_max)
ax.grid(True, alpha=0.3)
ax.legend(loc="upper right", fontsize=9, frameon=False)

# -----  右圖:Time series  --------------------------------------
# 從 (0.3, 0.3) 跑一條長軌跡,把 u(τ), v(τ) 隨時間畫出來
ax = axes[1]
T_LONG = 40.0
sol = solve_ivp(rhs, (0, T_LONG), (0.3, 0.3), args=(BETA, GAMMA),
                t_eval=np.linspace(0, T_LONG, 2000), **INTEGRATOR_KW)
ax.plot(sol.t, sol.y[0], lw=2.0, color="#1f77b4", label=r"$u(\tau)$")
ax.plot(sol.t, sol.y[1], lw=2.0, color="#d62728", label=r"$v(\tau)$")
ax.axhline(u_star, ls=":", color="#888", alpha=0.7,
           label=fr"$u^* = v^* = {u_star:.2f}$")
ax.set_xlabel(r"dimensionless time  $\tau$")
ax.set_ylabel(r"$u, v$")
ax.set_title(r"(b)  Trajectory from $(u_0, v_0) = (0.3, 0.3)$",
             fontweight="bold", loc="left")
ax.legend(loc="center right", fontsize=10, frameon=False)
ax.grid(True, alpha=0.3)

fig.suptitle("Dimensionless plant–herbivore model",
             fontsize=13, fontweight="bold", y=1.02)
fig.tight_layout()

outpath = OUTDIR / "fig1_phase_portrait_clean.png"
fig.savefig(outpath, dpi=150, bbox_inches="tight")
print(f"\nFigure written to: {outpath}")
