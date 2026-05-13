"""
================================================================================
教育版:藻類生物量曲線擬合(2020 期中 P3)
================================================================================

這份程式碼是 `fit_models.py` 的「教學版」——產出的圖片是純英文乾淨版,
而程式碼本身有大量註解,解釋**為什麼這樣寫**,而不只是「寫了什麼」。

對應的觀念來自:
  - [07-參數估計.md §7.2 線性化]、§7.3 非線性 LSQ + 初值選擇
  - [08-模型驗證.md §8.3 配適度指標]、§8.4 nested 模型比較

讀這份程式碼的時候,**把每一段註解當成一個小教學單元**——它解釋的是
「在做非線性擬合時,你會踩到的坑,以及為什麼這樣繞過去」。
================================================================================
"""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy.stats import f as f_dist

OUTDIR = Path(__file__).parent


# ==============================================================================
# 第 0 步:資料
# ==============================================================================
# 原題給的 Adriatic Sea 藻類生物量隨時間的觀測。t 是天,B 是 mm²。
# 注意 B 的範圍跨了三個數量級(0.005 → 5.1)——這一點等下挑初值會用到。
t_data = np.array([11.0, 15.0, 18.0, 23.0, 26.0, 31.0,
                   39.0, 44.0, 54.0, 64.0, 74.0])
B_data = np.array([0.00476, 0.0105, 0.0207, 0.0619, 0.337, 0.74,
                   1.7, 2.45, 3.5, 4.5, 5.09])
n = len(t_data)  # n = 11


# ==============================================================================
# 第 1 步:把三個模型寫成 Python 函式
# ==============================================================================
# curve_fit 要求第一個引數是「自變數」,後面才是參數。
# 所以函式簽名都是 f(t, p1, p2, ...) 這個固定格式。

def model_A(t, a, b, c):
    """Standard logistic (3 parameters).

    B(t) = a / (1 + b · exp(-c·t))

    形狀:S 形飽和。t → ∞ 時 B → a,t = 0 時 B = a/(1+b)。
    """
    return a / (1.0 + b * np.exp(-c * t))


def model_B(t, a, b, c):
    """Power + offset (3 parameters).

    B(t) = a + b · t^c

    形狀:t → ∞ 時 B → ∞(若 b, c > 0),沒有飽和上限。
    `np.clip(t, 1e-9, ...)` 是怕 t=0 在某些 c 下會出現 0^c 數值問題。
    """
    return a + b * np.power(np.clip(t, 1e-9, None), c)


def model_C(t, a, b, c, d):
    """Richards / generalized logistic (4 parameters).

    B(t) = a / (1 + b · exp(-c·t))^(1/d)

    當 d = 1 時退化成 Model A。d 控制 S 形的「對稱性」:
      d > 1:右偏 S(早期慢、後期飽和快)
      d < 1:左偏 S(早期加速快、後期慢慢趨近上限)

    `np.maximum(..., 1e-12)` 是防呆——萬一參數讓 base 變很小或負值,
    避免 power(負數, 非整數)爆掉。實務上 b > 0、c > 0 不會發生,但
    LM 中間迭代可能瞬間飄到不好的點,加 floor 比較安全。
    """
    base = np.maximum(1.0 + b * np.exp(-c * t), 1e-12)
    return a / np.power(base, 1.0 / d)


# ==============================================================================
# 第 2 步:挑初值——非線性擬合的勝負手
# ==============================================================================
# scipy.optimize.curve_fit 預設用 Levenberg-Marquardt(LM)演算法。
# LM 是「局部優化器」——只會往附近找最低點。所以初值不好就會卡在
# 不好的局部極小,甚至不收斂。
#
# 怎麼挑?三招:
#   (a) 從模型的「漸近行為」反推
#   (b) 從「特殊點」反推(t=0 的值、反曲點位置)
#   (c) 線性化(把模型取 log 後變線性,先用 OLS 找粗估)
# ------------------------------------------------------------------------------

# Model A 的初值 ------------------------------------------------------
# (a) a:漸近線,略高於 max(B)。觀測最大 5.09,猜 a ≈ 6。
# (b) b:B(0) = a/(1+b) 應該接近 0,所以 b 應該很大。猜 b ≈ 1000。
# (c) c:反曲點 t* = ln(b)/c。從資料看 t=26 附近 B 還在快速上升,
#        中期反曲點大概落在 t ≈ 25 → c ≈ ln(1000)/25 ≈ 0.28。
pA0 = [6.0, 1000.0, 0.25]

# Model B 的初值 ------------------------------------------------------
# Model B 比較刁鑽——沒有飽和、沒有反曲,光看資料形狀挑初值容易飄。
# 訣竅:**線性化**(§7.2)。先假設 a ≈ 0(因為 t=11 的值已經很小),
# 那麼 B ≈ b·t^c,兩邊取 log:
#     log(B) = log(b) + c · log(t)
# 這是一條「log(B) 對 log(t)」的直線,可以用 np.polyfit 一行解。
logt = np.log(t_data)
logB = np.log(np.clip(B_data, 1e-9, None))   # clip 防 log(0)
c0, logb0 = np.polyfit(logt, logB, 1)         # 一階多項式 = 直線
pB0 = [0.0, float(np.exp(logb0)), float(c0)]

# Model C 的初值 ------------------------------------------------------
# (a) 既然 Model A 是 Model C 在 d=1 的特例,**最自然的初值就是
#     「先用 A 的擬合結果 + d=1」**。等下會跑這部分。
# (b) 同時要設 bounds:不設的話,優化器會把 d → 0(Gompertz 極限),
#     這時模型行為跟其他參數退耦,$b$ 和 $d$ 變不可辨識(unidentifiable)。
#     把 d 限在 [0.2, 5] 是保守做法,既給足彈性又避免退化。
bounds_C = ([0.1,  1.0,  0.01, 0.2],   # 下界:a, b, c, d
            [50.0, 1e6,  2.0,  5.0])   # 上界


# ==============================================================================
# 第 3 步:擬合
# ==============================================================================
# `maxfev = 50000` 給足夠的函式評估次數,避免「函數呼叫太多次」終止。
# `curve_fit` 回傳 (popt, pcov)。popt 是最佳參數,pcov 是參數共變
# 矩陣(可以拿來算參數不確定度,本練習不需要)。

pA, _ = curve_fit(model_A, t_data, B_data, p0=pA0, maxfev=50000)
pB, _ = curve_fit(model_B, t_data, B_data, p0=pB0, maxfev=50000)

# Model C 的初值用剛才 A 擬合好的 (a, b, c) + d=1
pC0 = [pA[0], pA[1], pA[2], 1.0]
pC, _ = curve_fit(model_C, t_data, B_data, p0=pC0,
                  bounds=bounds_C, maxfev=50000)


# ==============================================================================
# 第 4 步:配適度指標
# ==============================================================================
# 三個指標:
#   - RSS:殘差平方和。是後面所有指標的基礎。
#   - RMSE:平均誤差的「平方根」,跟資料單位相同(這裡是 mm²)。
#   - AIC:把 RSS 跟參數數量綁在一起。AIC 越小越好。
#
# AIC 的公式(假設殘差為常態):
#   AIC = n · ln(RSS/n) + 2K
# 其中 K = 參數數 + 1(算 σ²)。Burnham–Anderson 經驗法則:
#   ΔAIC < 2:兩個模型支持度相當
#   ΔAIC ∈ [4, 7]:支持度顯著下降
#   ΔAIC > 10:幾乎沒有支持
# ------------------------------------------------------------------------------

def rss(y, yhat):
    return float(np.sum((y - yhat) ** 2))

def rmse_from_rss(r, n_):
    return float(np.sqrt(r / n_))

def aic(rss_value, n_, k_params):
    # k_params 是擬合的參數數(a, b, c, ...),AIC 還要 +1 算 σ²。
    K = k_params + 1
    return n_ * np.log(rss_value / n_) + 2 * K

RSS_A = rss(B_data, model_A(t_data, *pA))
RSS_B = rss(B_data, model_B(t_data, *pB))
RSS_C = rss(B_data, model_C(t_data, *pC))

RMSE_A = rmse_from_rss(RSS_A, n)
RMSE_B = rmse_from_rss(RSS_B, n)
RMSE_C = rmse_from_rss(RSS_C, n)

AIC_A = aic(RSS_A, n, k_params=3)
AIC_B = aic(RSS_B, n, k_params=3)
AIC_C = aic(RSS_C, n, k_params=4)
AIC_min = min(AIC_A, AIC_B, AIC_C)


# ==============================================================================
# 第 5 步:F-test for nested models (Model A vs Model C)
# ==============================================================================
# Model A 是 Model C 的特例(d = 1)——所以兩個模型「嵌套」(nested)。
# nested 模型可以用 F-test 嚴格回答「多一個參數值不值得」:
#
#   F = [(RSS_A - RSS_C) / (p_C - p_A)] / [RSS_C / (n - p_C)]
#
# 在虛無假設「Model A 已足夠(d = 1)」下,F ~ F(p_C - p_A, n - p_C)。
# 拒絕 H_0 → Model C 顯著比 A 好。
# ------------------------------------------------------------------------------
p_A_count = 3
p_C_count = 4
df1 = p_C_count - p_A_count   # = 1
df2 = n - p_C_count           # = 7
F_stat = ((RSS_A - RSS_C) / df1) / (RSS_C / df2)
F_crit_05 = f_dist.ppf(0.95, df1, df2)
p_value = 1.0 - f_dist.cdf(F_stat, df1, df2)


# ==============================================================================
# 第 6 步:外推到 t = 150
# ==============================================================================
t_target = 150.0
predA = float(model_A(t_target, *pA))
predB = float(model_B(t_target, *pB))
predC = float(model_C(t_target, *pC))


# ==============================================================================
# 第 7 步:Console 報告
# ==============================================================================
def banner(s):
    print("\n" + "=" * 72)
    print(s)
    print("=" * 72)

banner("Fitted parameters")
print(f"Model A (3 params):  a = {pA[0]:.4f},  b = {pA[1]:.4f},  "
      f"c = {pA[2]:.4f}")
print(f"Model B (3 params):  a = {pB[0]:.4e},  b = {pB[1]:.4e},  "
      f"c = {pB[2]:.4f}")
print(f"Model C (4 params):  a = {pC[0]:.4f},  b = {pC[1]:.4f},  "
      f"c = {pC[2]:.4f},  d = {pC[3]:.4f}")

banner("Goodness of fit")
print(f"{'Model':<10}{'RSS':>12}{'RMSE':>12}{'AIC':>12}{'ΔAIC':>12}")
print(f"{'A':<10}{RSS_A:>12.5f}{RMSE_A:>12.5f}{AIC_A:>12.3f}"
      f"{AIC_A - AIC_min:>12.3f}")
print(f"{'B':<10}{RSS_B:>12.5f}{RMSE_B:>12.5f}{AIC_B:>12.3f}"
      f"{AIC_B - AIC_min:>12.3f}")
print(f"{'C':<10}{RSS_C:>12.5f}{RMSE_C:>12.5f}{AIC_C:>12.3f}"
      f"{AIC_C - AIC_min:>12.3f}")

banner("F-test: Model A vs Model C  (nested, H0: d = 1)")
print(f"F({df1}, {df2}) = {F_stat:.3f}")
print(f"F_crit(0.05)  = {F_crit_05:.3f}")
print(f"p-value       = {p_value:.5f}")
if F_stat > F_crit_05:
    print("→ Reject H0. Model C is significantly better than Model A.")
else:
    print("→ Fail to reject H0. Model A is sufficient.")

banner("Extrapolation to t = 150 days")
print(f"  Model A:  B(150) = {predA:.3f} mm²")
print(f"  Model B:  B(150) = {predB:.3f} mm²   (no saturation — beware!)")
print(f"  Model C:  B(150) = {predC:.3f} mm²")


# ==============================================================================
# 第 8 步:畫圖(乾淨英文版)
# ==============================================================================
# 設計原則:
#   - 全英文,不用 CJK 字型(避免依賴 Noto Sans CJK)
#   - 左圖:in-sample fit
#   - 右圖:extrapolation 到 150
#   - 用對比鮮明的線型與顏色,讓三條曲線一眼分辨
# ------------------------------------------------------------------------------
plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "axes.unicode_minus": False,
    "axes.spines.top": False,
    "axes.spines.right": False,
})

t_smooth = np.linspace(1, 160, 500)

fig, axes = plt.subplots(1, 2, figsize=(13.5, 5.5),
                         gridspec_kw={"width_ratios": [1, 1]})

# ---- Left panel: in-sample ---------------------------------------------------
ax = axes[0]
ax.plot(t_data, B_data, "o", ms=9, mec="black", mfc="white",
        mew=1.5, label="Observed", zorder=5)
ax.plot(t_smooth, model_A(t_smooth, *pA), "-", lw=2.2,
        color="#1f77b4", label=f"A  logistic   (RMSE = {RMSE_A:.3f})")
ax.plot(t_smooth, model_B(t_smooth, *pB), "--", lw=2.2,
        color="#d62728", label=f"B  power       (RMSE = {RMSE_B:.3f})")
ax.plot(t_smooth, model_C(t_smooth, *pC), "-.", lw=2.2,
        color="#2ca02c", label=f"C  Richards   (RMSE = {RMSE_C:.3f})")
ax.axvspan(t_data.min(), t_data.max(), color="#ddd", alpha=0.4)

ax.set_xlim(0, 80)
ax.set_ylim(-0.3, 6.5)
ax.set_xlabel("Time (days)")
ax.set_ylabel(r"Biomass (mm$^2$)")
ax.set_title("(a)  In-sample fit", loc="left", fontweight="bold")
ax.grid(True, alpha=0.3)
ax.legend(loc="upper left", fontsize=9, frameon=False)

# ---- Right panel: extrapolation to 150 ---------------------------------------
ax = axes[1]
ax.plot(t_data, B_data, "o", ms=9, mec="black", mfc="white",
        mew=1.5, label="Observed", zorder=5)
ax.plot(t_smooth, model_A(t_smooth, *pA), "-",  lw=2.2,
        color="#1f77b4", label="A  logistic")
ax.plot(t_smooth, model_B(t_smooth, *pB), "--", lw=2.2,
        color="#d62728", label="B  power")
ax.plot(t_smooth, model_C(t_smooth, *pC), "-.", lw=2.2,
        color="#2ca02c", label="C  Richards")
ax.axvspan(t_data.min(), t_data.max(), color="#ddd", alpha=0.4,
           label="data range")
ax.axvline(t_target, ls=":", color="#444", lw=1.2)

ax.plot(t_target, predA, "^", ms=11, color="#1f77b4", zorder=6)
ax.plot(t_target, predB, "s", ms=11, color="#d62728", zorder=6)
ax.plot(t_target, predC, "v", ms=11, color="#2ca02c", zorder=6)

# Predictions as annotations
ax.annotate(f"A: B(150) = {predA:.2f}",
            xy=(t_target, predA), xytext=(-105, 6),
            textcoords="offset points",
            color="#1f77b4", fontsize=9, fontweight="bold")
ax.annotate(f"B: B(150) = {predB:.2f}",
            xy=(t_target, predB), xytext=(-105, 8),
            textcoords="offset points",
            color="#d62728", fontsize=9, fontweight="bold")
ax.annotate(f"C: B(150) = {predC:.2f}",
            xy=(t_target, predC), xytext=(-105, -14),
            textcoords="offset points",
            color="#2ca02c", fontsize=9, fontweight="bold")

y_top = max(predA, predB, predC) * 1.12
y_top = max(y_top, 7.0)
ax.set_xlim(0, 165)
ax.set_ylim(-0.5, y_top)
ax.set_xlabel("Time (days)")
ax.set_ylabel(r"Biomass (mm$^2$)")
ax.set_title("(b)  Extrapolation to t = 150 days",
             loc="left", fontweight="bold")
ax.grid(True, alpha=0.3)
ax.legend(loc="upper left", fontsize=9, frameon=False)

fig.suptitle("Algal biomass: three models, in-sample vs extrapolation",
             fontsize=13, fontweight="bold", y=1.02)
fig.tight_layout()

outpath = OUTDIR / "fig1_model_compare_clean.png"
fig.savefig(outpath, dpi=150, bbox_inches="tight")
print(f"\nFigure written to: {outpath}")
