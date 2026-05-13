"""
================================================================================
教育版:賀爾蒙適應模型(2021 期中 P2)
================================================================================

這份程式碼是 `fig1_time_series.py` + `fig2_phase_plane.py` 的「教學版」——
產出兩張英文乾淨圖,程式碼有大量註解。

模型(已給 k1 = 0.5, e = 0.1):
    dp/dt = k1 · H · (1 - p) - A · p
    dA/dt = e · (H - A)

對應的觀念:
  - [04-量化建模I.md §4.3.3 mass-action / receptor binding]
  - [04-量化建模I.md §4.3.2 一階追蹤 / leaky integrator]
  - [09-模型分析.md §9.3.1 equilibria / §9.3.3 phase plane / slow manifold]

**「初值很重要」在這題的意義**:
  初值是「H = 1 時的平衡」(p, A) = (1/3, 1)。**這個選擇關鍵**——
  從非平衡的點起步看不到「適應」現象,只會看到一般的暫態。
  從平衡點起步 + H 階躍才能凸顯「快暴衝 → 慢適應 → 回到原 p」這個故事。

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
K1 = 0.5
E = 0.1
H_OLD = 1.0
H_NEW = 10.0

# **尺度分離**(這題的核心):
#   τ_p = 1 / (k1·H + A) ≈ 1/6 ≈ 0.17  (剛跳完 H=10、A=1 時)
#   τ_A = 1 / e          = 10
# τ_p 比 τ_A 快約 60 倍 → p 「秒回應」,A 「慢追上」 → adaptation
tau_p_initial = 1.0 / (K1 * H_NEW + 1.0)
tau_A = 1.0 / E
print(f"Time scales at the moment of the step:")
print(f"  tau_p ≈ {tau_p_initial:.3f}  (p responds fast)")
print(f"  tau_A = {tau_A:.1f}    (A tracks slowly)")
print(f"  ratio = {tau_A/tau_p_initial:.1f}x  → strong scale separation")


# ==============================================================================
# 第 1 步:平衡點(代數)
# ==============================================================================
# H = H_OLD = 1 時的初始平衡:
#   dA/dt = 0 → A* = H = 1
#   dp/dt = 0 → k1·H·(1-p) = A·p → p* = k1·H/(k1·H + A) = k1/(1 + k1) = 1/3
p_eq_old = K1 / (1.0 + K1)
A_eq_old = H_OLD

# H = H_NEW = 10 時的新平衡:
#   一樣的代數推導 → A* = 10,p* = k1/(1+k1) = 1/3 (**跟 H 無關!**)
p_eq_new = K1 / (1.0 + K1)
A_eq_new = H_NEW

# 「快階段」p 的偽平衡(暫時凍結 A = 1):
p_peak = K1 * H_NEW / (K1 * H_NEW + A_eq_old)

print(f"\nEquilibria:")
print(f"  H = 1:  (p*, A*) = ({p_eq_old:.4f}, {A_eq_old:.0f})")
print(f"  H = 10: (p*, A*) = ({p_eq_new:.4f}, {A_eq_new:.0f})")
print(f"  p_peak (fast quasi-eq when A still = 1) = {p_peak:.4f}")
print(f"  ** Perfect adaptation: p* is the same for both H **")


# ==============================================================================
# 第 2 步:ODE 與模擬
# ==============================================================================
def rhs(_t, y):
    p, A = y
    return [K1 * H_NEW * (1.0 - p) - A * p,
            E * (H_NEW - A)]


# **為什麼 t_end = 80?**
#   A 的時間常數 τ_A = 10,要 3-4 個 τ 才接近平衡 → ≥ 30
#   留到 80 是為了讓圖上有清楚的「平穩段」,讀者一眼看到收斂
# **為什麼 max_step = 0.05?**
#   快階段 t < 1 時 p 變化劇烈,步長太大會跳過尖峰。
T_END = 80.0
INTEGRATOR_KW = dict(rtol=1e-9, atol=1e-12, max_step=0.05)

t_eval = np.linspace(0, T_END, 4000)
sol = solve_ivp(rhs, (0, T_END), [p_eq_old, A_eq_old],
                t_eval=t_eval, **INTEGRATOR_KW)
p_traj = sol.y[0]
A_traj = sol.y[1]


# ==============================================================================
# 第 3 步:畫圖 1 —— 時序圖(兩個 panel)
# ==============================================================================
plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "axes.unicode_minus": False,
    "axes.spines.top": False,
    "axes.spines.right": False,
})

fig1, axes = plt.subplots(2, 1, figsize=(9, 6.5), sharex=True)

# ----- 上 panel:p(t)
ax = axes[0]
ax.plot(sol.t, p_traj, lw=2.2, color="#d62728", label="$p(t)$")
ax.axhline(p_eq_new, ls="--", color="black", alpha=0.5,
           label=f"$p^* = k_1/(1+k_1) = {p_eq_new:.3f}$")
ax.axhline(p_peak, ls=":", color="#888", alpha=0.7,
           label=f"fast-phase peak $\\approx {p_peak:.3f}$")
ax.set_ylabel("$p$  (bound fraction)")
ax.legend(fontsize=9, loc="center right", frameon=False)
ax.grid(True, alpha=0.3)
ax.set_title("(a)  $H$: 1 → 10 step.  $p$ spikes, then 'adapts' back to 1/3",
             fontweight="bold", loc="left")

# ----- 下 panel:A(t)
ax = axes[1]
ax.plot(sol.t, A_traj, lw=2.2, color="#1f77b4", label="$A(t)$")
ax.axhline(A_eq_new, ls="--", color="black", alpha=0.5,
           label=f"$A^* = H = {A_eq_new:.0f}$")
ax.axhline(A_eq_old, ls=":", color="#888", alpha=0.7,
           label=f"initial $A_0 = {A_eq_old:.0f}$")

# 標出 1 個時間常數 t = τ_A
target_efold = A_eq_old + (A_eq_new - A_eq_old) * (1 - np.exp(-1))
ax.plot(tau_A, target_efold, "o", ms=8, color="#1f77b4")
ax.annotate(f"$t = 1/e = {tau_A:.0f}$\n(one time constant)",
            xy=(tau_A, target_efold), xytext=(20, 5),
            fontsize=9, color="#1f77b4",
            arrowprops=dict(arrowstyle="->", color="#1f77b4", alpha=0.6))

ax.set_ylabel("$A$  (dissociation rate)")
ax.set_xlabel("$t$")
ax.legend(fontsize=9, loc="center right", frameon=False)
ax.grid(True, alpha=0.3)

fig1.tight_layout()
outpath1 = OUTDIR / "fig1_time_series_clean.png"
fig1.savefig(outpath1, dpi=150, bbox_inches="tight")
print(f"\nFigure 1 written to: {outpath1}")


# ==============================================================================
# 第 4 步:畫圖 2 —— Phase plane (p 對 A)
# ==============================================================================
# Phase plane 是「拿掉時間」的另一種視角:橫軸 p、縱軸 A。
# 兩個時間尺度差很多 → 軌跡是「先水平衝右,再斜上爬升」的 L 形。
# **這條斜上的曲線本身就是 slow manifold** —— 在它上面,p 與 A 之間
# 滿足 dp/dt ≈ 0(p 已經追上當前的 A),系統在這條 1D 流形上慢慢爬。

fig2, ax = plt.subplots(figsize=(8, 7))

# 軌跡
ax.plot(p_traj, A_traj, lw=2.0, color="#9467bd", label="trajectory")

# 標起點與終點
ax.plot(p_traj[0], A_traj[0], "o", ms=12, mec="black", mfc="#2ca02c",
        zorder=5, label=f"start  $({p_traj[0]:.2f}, {A_traj[0]:.0f})$")
ax.plot(p_traj[-1], A_traj[-1], "s", ms=12, mec="black", mfc="#d62728",
        zorder=5, label=f"end  $\\approx({p_traj[-1]:.2f}, {A_traj[-1]:.1f})$")

# 標 peak(p 最大的點)
i_peak = int(np.argmax(p_traj))
ax.plot(p_traj[i_peak], A_traj[i_peak], "^", ms=12, mec="black",
        mfc="#ff7f0e", zorder=5,
        label=f"peak  $({p_traj[i_peak]:.2f}, {A_traj[i_peak]:.2f})$")

# slow manifold:dp/dt ≈ 0 給 A = k1·H·(1-p)/p
p_grid = np.linspace(0.05, 0.95, 200)
A_slow = K1 * H_NEW * (1.0 - p_grid) / p_grid
mask = (A_slow >= 0.5) & (A_slow <= 11)
ax.plot(p_grid[mask], A_slow[mask], "--", lw=1.6, color="#888",
        label=r"slow manifold:  $A = k_1 H (1-p)/p$")

# 箭頭標方向
for idx in (50, 250, 800, 1500, 3000):
    if idx < len(p_traj) - 1:
        dx = p_traj[idx + 1] - p_traj[idx]
        dy = A_traj[idx + 1] - A_traj[idx]
        norm = np.hypot(dx, dy)
        if norm > 0:
            ax.annotate("", xytext=(p_traj[idx], A_traj[idx]),
                        xy=(p_traj[idx] + dx * 0.5 / norm,
                            A_traj[idx] + dy * 0.5 / norm),
                        arrowprops=dict(arrowstyle="->",
                                        color="#9467bd", lw=1.4))

ax.set_xlabel("$p$  (bound fraction)")
ax.set_ylabel("$A$  (dissociation rate)")
ax.set_title("(b)  Phase plane: trajectory tracks a slow manifold",
             fontweight="bold", loc="left")
ax.set_xlim(0, 1)
ax.set_ylim(0, 11)
ax.grid(True, alpha=0.3)
ax.legend(loc="upper left", fontsize=9, frameon=False)

fig2.tight_layout()
outpath2 = OUTDIR / "fig2_phase_plane_clean.png"
fig2.savefig(outpath2, dpi=150, bbox_inches="tight")
print(f"Figure 2 written to: {outpath2}")
