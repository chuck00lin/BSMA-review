# 2021 期中 Problem 3 — 兒童身高曲線擬合 (20%)

## 原題(完整)

> **Problem 3: (20%) – In-Class Problem**
>
> The height ($H$) of a child is measured at different ages as follows.
>
> | age (years) | 0 | 5 | 8 | 12 | 16 | 18 |
> |---:|---:|---:|---:|---:|---:|---:|
> | H (inch) | 20.0 | 36.2 | 52.0 | 60.0 | 69.2 | 70.0 |
>
> Estimate the height of the child as an adult of **15** and **30 years of age**, using the following two models. You may use MATLAB or python programs to find the parameters of each model. **Compare and discuss** the two models. Which model do you think is more appropriate to **describe the data**? Which model is more reasonable for the **estimation of the height of an adult of 30 years of age**?
>
> $$
> \text{Model A:}\quad H = \frac{a}{1 + b\,e^{-ct}}
> $$
>
> $$
> \text{Model B:}\quad H = \sqrt{a + b\,t}
> $$

---

## 1. 兩個模型在「形狀」上的差異(verbal first)

在動工算之前,先**看一眼兩個模型長什麼樣**——這比急著程式跑擬合重要。

### 1.1 Model A:logistic 飽和曲線

$$
H(t) = \frac{a}{1 + b\,e^{-ct}}
$$

- 當 $t \to \infty$:$e^{-ct} \to 0$,所以 $H \to a$。**有上限 $a$**(漸近線)。
- 當 $t = 0$:$H(0) = a/(1+b)$。
- 當 $t \to -\infty$:$H \to 0$。
- 中間有一個**反曲點(inflection point)**,長相是 **S 形**。
- 參數意義:$a$ = 終身高(漸近),$b$ = 跟初始狀態有關(基本上控制「S 從哪裡開始」),$c$ = 成長速率(S 形的「斜度」)。

**這就是 logistic 曲線**——跟 [04-量化建模I §4.3.7](../../redesigned/04-量化建模I.md) 講的 logistic 種群成長同一條,只是現在用來擬合身高。生物學上很合理:小孩會長到一個極限就停。

### 1.2 Model B:平方根曲線

$$
H(t) = \sqrt{a + b t}
$$

- 當 $t \to \infty$:$H \to \infty$,**沒有上限**。
- 當 $t = 0$:$H(0) = \sqrt{a}$。
- 等價變形:$H^2 = a + b t$ ——**$H^2$ 對 $t$ 是直線**。這也是我們等下擬合的時候要用的小技巧。
- 形狀:成長率隨時間下降,但**永遠沒有飽和**。

> **這個分析告訴你結論已經出來一半了**:Model B 沒有極限,30 歲的身高估計不可能合理(會繼續長)。但**在資料範圍內(0–18 歲)它可能擬合得不錯**,因為 0–18 歲還在快速長高。所以這題在考你「**好擬合 ≠ 好外推**」的概念。

---

## 2. 動手擬合

### 2.1 Model B 的小技巧——線性化(§7.2)

把 $H^2$ 對 $t$ 做線性回歸,參數就有閉式解:

$$
\underbrace{H^2}_{\text{新的 } y} \;=\; \underbrace{a}_{\text{截距}} \;+\; \underbrace{b}_{\text{斜率}} \cdot t
$$

把資料的 $H^2$ 算出來:

| $t$ | 0 | 5 | 8 | 12 | 16 | 18 |
|---:|---:|---:|---:|---:|---:|---:|
| $H$ | 20.0 | 36.2 | 52.0 | 60.0 | 69.2 | 70.0 |
| $H^2$ | 400 | 1310 | 2704 | 3600 | 4789 | 4900 |

對 $(t, H^2)$ 做 OLS,得到 $a, b$。**程式碼**見 `fit_models.py`。

實際擬合得到(`fit_models.py` 跑出來):
$$
\widehat{a} \approx 326.9,\quad \widehat{b} \approx 266.8
$$

→ 預測 $H(15) = \sqrt{326.9 + 266.8\cdot 15} \approx \sqrt{4328.9} \approx 65.8$ inch
→ 預測 $H(30) = \sqrt{326.9 + 266.8\cdot 30} \approx \sqrt{8330.9} \approx 91.3$ inch ⚠️

**91 吋(231 cm)的成人?不合理**。

### 2.2 Model A 的非線性擬合(§7.3)

對 $H = a/(1+b e^{-ct})$ 沒有閉式解,**得用非線性最小平方法**(`scipy.optimize.curve_fit`,本質上是 Levenberg-Marquardt——見 [07-參數估計.md §7.3](../../redesigned/07-參數估計.md))。

初值很重要:
- $a \approx$ 最大資料值 $\approx 75$(略高於 70,因為 18 歲還沒完全飽和)。
- $b$:$H(0) = a/(1+b) = 20 \Rightarrow b \approx a/20 - 1 \approx 2.75$。
- $c$:從反曲點位置估;粗估 $c \approx 0.25$(中間段大概每 4 年顯著變化)。

擬合得到:
$$
\widehat{a} \approx 74.32,\quad \widehat{b} \approx 2.82,\quad \widehat{c} \approx 0.217
$$

→ 預測 $H(15) \approx 67.0$ inch
→ 預測 $H(30) \approx 74.0$ inch ✓(終身高 $\approx 74.3$ 吋 / 189 cm,合理)

> **(實際數值會被 `fit_models.py` 寫到圖上,以上是大致數量級。)**

---

## 3. 兩個模型的比較

| 指標 | Model A (logistic) | Model B (sqrt) |
|---|---|---|
| 自由度(參數數) | 3 | 2 |
| 資料範圍內 RMSE | $\approx 1.44$ inch | $\approx 2.42$ inch(略大) |
| 預測 $H(15)$ | $\approx 67.0$ inch | $\approx 65.8$ inch(類似) |
| 預測 $H(30)$ | $\approx 74.0$ inch ✓ | $\approx 91.3$ inch ✗ |
| 漸近極限 | $a \approx 74.3$(合理終身高) | $\infty$(無上限) |
| 生物合理性 | ✓ 反映「長到一個天花板就停」 | ✗ 預測身高無止盡增長 |
| 用途 | 適合**外推到成人** | 只適合**內插**或短期外推 |

### 模型選擇:in-sample 與 structural validity 都站在 A 這邊

這題雖然 Model B 少一個參數(可能因此被 Occam's razor 偏好),但實際上:

- **In-sample**:Model A 的 RMSE($\approx 1.44$ inch)還是比 Model B($\approx 2.42$ inch)小。Model A 多出的一個參數**買到了顯著更好的擬合**。
- **Out-of-sample(外推到 30 歲)**:Model B 給 91 吋,**結構上就不合理**——身高不該無止盡增長。
- 這正是 [08-模型驗證.md §8.6 結構驗證](../../redesigned/08-模型驗證.md) 強調的:模型不只要「fit data」,還要**結構上合理**(structurally validated)。logistic 的「有飽和」這個結構性質,讓它在外推時不會發狂。
- **如果 Model B 在 in-sample 反而比 A 更好**——那才會是真正的 Occam vs structural validity 的兩難。這題裡 A 全面勝出,**不要選錯**。

> 圖見 `fit_models.py` 輸出的 `fig1_model_compare.png`。

---

## 4. 答題建議

1. **不要急著跑程式**——先把兩個模型的「形狀」寫一下:Model A 有上限、Model B 沒有。
2. **線性化擬合 Model B**:這是送分點。$H^2$ vs $t$ 線性回歸,用普通最小平方法。
3. **Model A 一定要寫初值**:閱卷者要看你會挑 $a \approx \max H$、$b$ 從 $t=0$ 值反推等等。
4. **「30 歲」這題的答案不是只有數字**:你要清楚講「Model B 給出 91 吋這個明顯不合理的值,因為它沒有飽和上限」——這是這題真正在考的觀念。
5. **選擇結論**:用 Model A(logistic)做外推 / 估計成人身高。Model B 在 18 歲內當作描述工具還可以。

---

## 5. 對照講義

| 題目要素 | 講義來源 |
|---|---|
| 線性化(transformations / linear least squares) | [07-參數估計.md §7.2](../../redesigned/07-參數估計.md) |
| 非線性 LSQ(LM、Newton 等) | [07-參數估計.md §7.3](../../redesigned/07-參數估計.md) |
| Logistic 模型本身 | [04-量化建模I.md §4.3.7](../../redesigned/04-量化建模I.md) |
| Parsimony vs structural validity | [08-模型驗證.md §8.6](../../redesigned/08-模型驗證.md) |

---

## 附錄:跑擬合

```bash
conda activate bsma-pdf
cd example-questions/2021-p3-child-height-fit
python fit_models.py
```
