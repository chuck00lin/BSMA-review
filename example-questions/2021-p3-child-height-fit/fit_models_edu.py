"""
================================================================================
教育版:兒童身高曲線擬合(2021 期中 P3)
================================================================================

這份程式碼是 `fit_models.py` 的「教學版」——產出的圖片是純英文乾淨版,
而程式碼本身有大量註解,解釋**為什麼這樣寫**。

對應的觀念來自:
  - [07-參數估計.md §7.2 線性化(closed-form OLS)]、§7.3 非線性 LSQ + 初值選擇
  - [08-模型驗證.md §8.6 結構驗證(Model B 沒有飽和)]

讀這份程式碼時,把每一段註解當成一個小教學單元。**核心訊息**:
  Model A(logistic):非線性 → 必須挑初值 → curve_fit (LM)
  Model B(sqrt):平方後線性 → 不需挑初值 → np.polyfit (closed-form OLS)

================================================================================
"""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

OUTDIR = Path(__file__).parent


# ==============================================================================
# 第 0 步:資料
# ==============================================================================
# 6 個觀測點。注意:
#   - t = 0 時 H = 20(嬰兒身高)
#   - t = 18 時 H = 70(青少年接近終身高)
#   - 中間區段 5–12 歲增長最快(這是青春期前的加速)
t_data = np.array([0.0, 5.0, 8.0, 12.0, 16.0, 18.0])
H_data = np.array([20.0, 36.2, 52.0, 60.0, 69.2, 70.0])
n = len(t_data)


# ==============================================================================
# 第 1 步:把兩個模型寫成 Python 函式
# ==============================================================================
def model_A(t, a, b, c):
    """Logistic (3 parameters).

    H(t) = a / (1 + b · exp(-c·t))

    形狀:S 形,t → ∞ 時 H → a (有飽和上限)
    """
    return a / (1.0 + b * np.exp(-c * t))


def model_B(t, a, b):
    """Square root (2 parameters).

    H(t) = sqrt(a + b·t)

    形狀:類似 t^{1/2}增長,t → ∞ 時 H → ∞(沒有飽和)。
    `np.maximum(.., 0)` 防止對負數開根號(t 太負時可能發生)。
    """
    val = a + b * t
    return np.sqrt(np.maximum(val, 0))


# ==============================================================================
# 第 2 步:Model B —— 「線性化」的勝利
# ==============================================================================
# Model B 的關鍵觀察:
#       H² = a + b·t       (兩邊平方,a, b 變成線性參數!)
# 這就是 [07-參數估計.md §7.2] 講的「線性化技巧」。
#
# 好處:
#   - 不用挑初值
#   - 不用迭代優化器
#   - 有「閉式解」(closed-form OLS)——一行 np.polyfit 解決
#   - 解出來的就是「最小平方意義下的全局最佳」(沒有局部最佳的問題)
#
# 注意:這個「線性化」是把模型參數變線性,**不是**把資料變線性。
# 我們對 H² vs t 做最小平方;這跟「對 H vs t 做最小平方」不同!
# 哪個比較對?要看雜訊假設——如果 H 的雜訊是「常數變異數」,
# 那原始 H 的擬合才正確;但 H² 線性化用於得 a, b 的「**初值**」很方便。
# 因為這題 H 跨度不大,線性化的結果已經很接近最佳。
H2 = H_data ** 2
b_B, a_B = np.polyfit(t_data, H2, 1)   # 一階多項式:回傳「[斜率, 截距]」


# ==============================================================================
# 第 3 步:Model A —— 非線性擬合,挑初值是勝負手
# ==============================================================================
# Model A 沒有閉式解,只能用迭代優化(Levenberg-Marquardt)。
# **LM 是局部優化器**——只會往附近找最低點。初值不好就會收斂到怪地方,
# 或不收斂。
#
# 挑初值的三招(全部用在 Model A 上):
#   (a) 從漸近行為:a 是漸近線,略高於 max(H)。max(H) = 70 → 猜 a = 75。
#       為什麼略高?因為 18 歲還沒完全飽和,真正的終身高應該再高一點。
#   (b) 從 t = 0 的值:H(0) = a/(1+b) = 20。
#       已知 a ≈ 75,解出 b = a/H(0) - 1 = 75/20 - 1 = 2.75。
#   (c) 從反曲點位置:logistic 的反曲點在 t* = ln(b)/c。
#       資料看起來中段(t ≈ 8)變化最快,粗估反曲點在 t ≈ 10。
#       → c ≈ ln(2.75) / 10 ≈ 0.10。實務上試 c = 0.25 也 OK,LM 會收斂。
a0 = 75.0
b0 = a0 / H_data[0] - 1.0   # ≈ 2.75
c0 = 0.25
pA, _ = curve_fit(model_A, t_data, H_data, p0=[a0, b0, c0], maxfev=10000)
a_A, b_A, c_A = pA


# ==============================================================================
# 第 4 步:配適度與預測
# ==============================================================================
def rmse(y, yhat):
    return float(np.sqrt(np.mean((y - yhat) ** 2)))

rmse_A = rmse(H_data, model_A(t_data, *pA))
rmse_B = rmse(H_data, model_B(t_data, a_B, b_B))

# 外推到題目要求的兩個年齡
predict_at = [15.0, 30.0]
A_preds = {t: float(model_A(t, *pA)) for t in predict_at}
B_preds = {t: float(model_B(t, a_B, b_B)) for t in predict_at}


# ==============================================================================
# 第 5 步:Console 報告
# ==============================================================================
def banner(s):
    print("\n" + "=" * 72)
    print(s)
    print("=" * 72)

banner("Initial guesses (Model A only — Model B has closed-form OLS)")
print(f"  a0 = {a0:.2f}   (slightly above max(H) = {H_data.max():.1f})")
print(f"  b0 = {b0:.4f}   (from H(0) = a/(1+b) = 20)")
print(f"  c0 = {c0:.4f}   (rough guess from inflection region)")

banner("Fitted parameters")
print(f"Model A (logistic, 3 params):  a = {a_A:.4f},  b = {b_A:.4f},  "
      f"c = {c_A:.4f}")
print(f"Model B (sqrt,     2 params):  a = {a_B:.4f},  b = {b_B:.4f}")

banner("Goodness of fit & predictions")
print(f"{'Model':<10}{'RMSE (in)':>12}{'H(15) (in)':>14}{'H(30) (in)':>14}")
print(f"{'A':<10}{rmse_A:>12.3f}{A_preds[15.0]:>14.2f}{A_preds[30.0]:>14.2f}")
print(f"{'B':<10}{rmse_B:>12.3f}{B_preds[15.0]:>14.2f}{B_preds[30.0]:>14.2f}"
      "   <-- 91 in = 231 cm,結構上不合理")

banner("Why no F-test here?")
print("  Model A (logistic) 和 Model B (sqrt) **不是** nested models—")
print("  Model A 沒有任何參數值可以讓它退化成 Model B。")
print("  所以 F-test for nested 在這題不適用。")
print("  在這種情境下用 AIC 比較更合適(或直接看 RMSE + 結構驗證)。")


# ==============================================================================
# 第 6 步:畫圖(乾淨英文版)
# ==============================================================================
plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "axes.unicode_minus": False,
    "axes.spines.top": False,
    "axes.spines.right": False,
})

t_smooth = np.linspace(0, 35, 400)

fig, ax = plt.subplots(figsize=(10, 6.5))

# In-sample range shading
ax.axvspan(0, 18, color="#ddd", alpha=0.4, zorder=0, label="data range (0–18 yr)")

# Data
ax.plot(t_data, H_data, "o", ms=10, mec="black", mfc="white", mew=1.5,
        label="Observed", zorder=5)

# Model A
ax.plot(t_smooth, model_A(t_smooth, *pA), "-", lw=2.2, color="#1f77b4",
        label=f"A  logistic (RMSE = {rmse_A:.2f})")
ax.axhline(a_A, ls=":", color="#1f77b4", alpha=0.5,
           label=f"$a_A$ = {a_A:.2f} (asymptote)")

# Model B
ax.plot(t_smooth, model_B(t_smooth, a_B, b_B), "--", lw=2.2, color="#d62728",
        label=f"B  sqrt (RMSE = {rmse_B:.2f})")

# Prediction markers
for t in predict_at:
    ax.axvline(t, ls=":", color="#444", alpha=0.5, lw=1.2)
    ax.plot(t, A_preds[t], "^", ms=12, color="#1f77b4", zorder=6)
    ax.plot(t, B_preds[t], "v", ms=12, color="#d62728", zorder=6)
    ax.annotate(f"A: H({t:.0f}) = {A_preds[t]:.1f}",
                xy=(t, A_preds[t]), xytext=(8, 8),
                textcoords="offset points",
                color="#1f77b4", fontsize=9, fontweight="bold")
    ax.annotate(f"B: H({t:.0f}) = {B_preds[t]:.1f}",
                xy=(t, B_preds[t]), xytext=(8, -16),
                textcoords="offset points",
                color="#d62728", fontsize=9, fontweight="bold")

# Highlight the runaway region
ax.fill_between(t_smooth, model_A(t_smooth, *pA), model_B(t_smooth, a_B, b_B),
                where=t_smooth >= 18, alpha=0.12, color="#d62728")
ax.text(28, 82,
        "Extrapolation:\nModel B has no asymptote\n→ keeps growing",
        fontsize=9, color="#a00", ha="center",
        bbox=dict(boxstyle="round,pad=0.4", fc="#fff", ec="#c66", alpha=0.9))

ax.set_xlabel("Age (years)")
ax.set_ylabel("Height (inch)")
ax.set_title("Child height fit:  logistic vs sqrt\n"
             "(in-sample 0–18 yr;  extrapolate to 15, 30)",
             loc="left", fontweight="bold")
ax.set_xlim(0, 35)
ax.set_ylim(15, 100)
ax.grid(True, alpha=0.3)
ax.legend(loc="lower right", fontsize=9, frameon=False)

fig.tight_layout()
outpath = OUTDIR / "fig1_model_compare_clean.png"
fig.savefig(outpath, dpi=150, bbox_inches="tight")
print(f"\nFigure written to: {outpath}")
