# 2021 期中 Problem 2 — 賀爾蒙適應模型 (15%)

## 原題(完整)

> **Problem 2: (15%) – In-Class Problem**
>
> Many biological systems need to be able to respond to **changes** in the level of some signal (like a hormone) without responding to the **actual level**. For example, a cell might have no response to a low level of hormone. If the hormone level rapidly increases, the cell responds. But if the hormone level then remains constant at the higher level, the cell again stops responding. The process is sometimes called **adaptation**.
>
> One mechanism for this process is summarized in the following model. Internal response is a function of the fraction, $p$, of cell surface receptors that are bound by the hormone. This fraction increases when the hormone level, $H$, is high. However, the hormone also dissociates from bound receptors. Assume this happens at a rate $A$ but that this rate is **controlled by the cell**. One possible set of equations is
>
> $$
> \frac{dp}{dt} = k_1\,H\,(1 - p) - A\,p
> $$
>
> $$
> \frac{dA}{dt} = e\,(H - A)
> $$
>
> Suppose that $k_1 = 0.5$ and $e = 0.1$, use your computer to simulate the response of the cell.
>
> 1. Find the **equilibrium state** of this model assuming that $H = 1$.
> 2. Simulate the response when the level of $H$ jumps quickly from $H = 1$ to $H = 10$. Draw graphs of $p$ and $A$ in the **phase plane** (a plot of state variables $p$ vs. $A$) as functions of time. Explain what is happening.

---

## 1. 先用「人話」讀方程式

### 1.1 第一條:結合受器比例 $p$ 的動態

$$
\underbrace{\frac{dp}{dt}}_{\text{結合率變動}} = \underbrace{k_1 H (1 - p)}_{\text{結合(進)}} \;-\; \underbrace{A p}_{\text{解離(出)}}
$$

- $k_1 H (1-p)$:**質量作用律**——空閒受器($1-p$ 比例)與荷爾蒙($H$)兩兩相遇結合。$k_1$ 是親和力常數。
- $A p$:已結合受器($p$ 比例)以「速率 $A$」解離掉。**關鍵設計**:$A$ **不是常數**,而是會被細胞自己調控。
- 這條方程的型態跟 [04-量化建模I §4.3.3](../../redesigned/04-量化建模I.md) 講的「**dose-response / receptor occupancy**」一樣——一進一出。

### 1.2 第二條:解離率 $A$ 自身的動態

$$
\frac{dA}{dt} = e (H - A)
$$

這是一條**一階追蹤方程**(first-order tracking / leaky integrator):
- $H > A$ → $A$ 上升;$H < A$ → $A$ 下降。
- 換句話說 **$A$ 慢慢「跟上」$H$**,但有時間常數 $1/e$。
- 在這題 $e = 0.1$,**時間常數 $\tau_A = 10$**——比 $p$ 動得慢得多。**這個尺度分離是「適應」現象的根源**。

> **整體故事**(用一句話總結):**$H$ 一升高,$p$ 因「快速結合」先暴衝;然後 $A$ 慢慢爬上來,把 $p$ 重新拉回原本的水平**——這就是 adaptation。

---

## 2. 第 1 小題:$H = 1$ 時的平衡點

平衡 = $\dfrac{dp}{dt} = \dfrac{dA}{dt} = 0$ 同時成立。

**先用 $A$ 那條**(較簡單):

$$
0 = e (H - A) \;\Rightarrow\; A^* = H = 1
$$

**代回 $p$ 那條**:

$$
0 = k_1 H (1 - p^*) - A^* p^* = 0.5 \cdot 1 \cdot (1 - p^*) - 1 \cdot p^*
$$

$$
0.5 - 0.5 p^* - p^* = 0 \;\Rightarrow\; 0.5 = 1.5 p^* \;\Rightarrow\; p^* = \tfrac{1}{3}
$$

$$
\boxed{\;(p^*, A^*) = (1/3,\; 1)\;}
$$

---

## 3. 一個漂亮的觀察:**完美適應(perfect adaptation)**

把上面的步驟**重做一次,但用任意 $H$**:

$$
A^* = H,\qquad k_1 H (1 - p^*) = H\, p^* \;\Rightarrow\; p^* = \frac{k_1}{1 + k_1}
$$

**$p^*$ 跟 $H$ 完全無關**!

- $H = 1$: $p^* = 1/3$。
- $H = 10$: $p^* = 1/3$ 一樣!
- $H = 100$:還是 $1/3$。

**這就是「適應」**:不管荷爾蒙水平最終停在多少,長期反應 $p^*$ 都會回到同一個值。生物學上稱為 **perfect adaptation**(完全適應)或 **exact adaptation**。

> **背後機制**(進階):$A$ 跟蹤的是 $H$ 本身,而 $p$ 的平衡條件可以重排為 $A/H = k_1 (1-p)/p$ ——只要 $A \propto H$, $p^*$ 就被釘住。這在控制理論裡叫 **integral feedback**(積分回饋,因為 $A$ 是 $H$ 的「累積追蹤」)。

---

## 4. 第 2 小題:$H$ 從 1 階躍到 10

### 4.1 初值與終值

- **初始(穩定在 $H=1$)**:$(p, A) = (1/3,\,1)$。
- **$t = 0$ 時 $H$ 突然跳到 10,之後保持 $H = 10$**。
- **新平衡**:$(p^*, A^*) = (1/3,\,10)$。**$p^*$ 沒變,只有 $A^*$ 變了**——但路上不平靜。

### 4.2 兩個時間尺度

| 變數 | 時間常數(粗估) | 行為 |
|---|---|---|
| $p$ | $1/(k_1 H + A) \approx 1/(0.5\cdot 10 + 1) = 1/6 \approx 0.17$(剛跳完那一瞬) | **快**——幾乎瞬間響應 |
| $A$ | $1/e = 10$ | **慢**——要 $\sim 30$–$50$ 個時間單位才能達到新平衡 |

**尺度分離**:$\tau_p \ll \tau_A$。所以系統的反應會分兩段:

### 4.3 兩階段反應

1. **快階段($t \lesssim 1$)**:$H$ 跳到 10,但 $A$ 還困在 1。**$p$ 暫時看到一個「強結合、弱解離」的世界**,衝上來。把 $A=1$ 凍結,$p$ 的偽平衡是:
   $$
   p_{\text{peak}} \;\approx\; \frac{k_1 H}{k_1 H + A} = \frac{0.5 \cdot 10}{0.5 \cdot 10 + 1} = \frac{5}{6} \approx 0.833
   $$
   也就是 $p$ 會衝到接近 $0.83$。

2. **慢階段($t \in [1, 50]$)**:$A$ 慢慢往 10 爬,於是「強解離」開始作用,把 $p$ 從 $0.83$ 拉回 $0.33$。最終 $(p,A) \to (1/3,\,10)$。

![Time series of p and A after the H: 1 → 10 step](fig1_time_series_clean.png)

### 4.4 在 phase plane 上發生什麼?

把 $p$ 放橫軸,$A$ 放縱軸,觀察 $(p(t), A(t))$ 的軌跡:

- 一開始在 $(1/3,\,1)$。
- **第一段**:$p$ 衝向右(因為 $A$ 還小,$p$ 快速上升),$A$ 幾乎不動 → 軌跡幾乎水平向右,到 $p \approx 0.83$。
- **第二段**:$A$ 慢慢往上爬,$p$ 同時被拉回左邊 → 軌跡沿一條「拋物線狀」曲線爬升並左移,最後落到 $(1/3,\,10)$。

![Phase plane: trajectory tracks the slow manifold](fig2_phase_plane_clean.png)

> 這條軌跡之所以彎彎的,就是因為兩個變數的時間尺度差很多——它是**slow manifold** 的經典樣貌(見 [09-模型分析.md](../../redesigned/09-模型分析.md) 慢流形討論)。圖中虛線就是 slow manifold $A = k_1 H (1-p)/p$:當 $p$ 已經追上 $A$(即 $dp/dt \approx 0$),系統就會沿著這條 1D 曲線慢慢移動。

> 圖由 [`simulate_edu.py`](./simulate_edu.py) 產出(英文乾淨版,附詳細教學註解);中文版由 [`fig1_time_series.py`](./fig1_time_series.py) 與 [`fig2_phase_plane.py`](./fig2_phase_plane.py) 產出。

---

## 5. 對照講義

| 題目要素 | 講義來源 |
|---|---|
| 質量作用律 / receptor binding | [04-量化建模I.md §4.3.3](../../redesigned/04-量化建模I.md) |
| 一階追蹤 / leaky integrator 形式 | [04-量化建模I.md §4.3.2](../../redesigned/04-量化建模I.md) |
| 平衡點計算 | [09-模型分析.md §9.3.1](../../redesigned/09-模型分析.md) |
| Phase plane / 慢-快尺度分離 | [09-模型分析.md §9.3.3](../../redesigned/09-模型分析.md) |
| 「適應 / integral feedback」 | 跨章節主題,本題的生物學動機 |

---

## 6. 課堂答題建議

1. **第 1 題先做 $A^* = H$,因為簡單**——不要從 $p$ 那條開始解,會被 $p$ 跟 $H$ 雙變數絆住。
2. **第 2 題的關鍵不是模擬數字,而是說對故事**:**fast spike → slow recovery → 回到原 $p$**。閱卷者要看你抓不抓得到「適應」這個現象。
3. **如果有空,順手算 $p^* = k_1/(1+k_1)$ 跟 $H$ 無關**——這是這題的「亮點」,寫上去會加分。
4. **Phase plane 圖畫的時候**:
   - 終點 $(1/3, 10)$ 要標出來。
   - 軌跡分兩段(快段水平、慢段斜上)——分段標出來。
   - 加箭頭指明時間方向。

---

## 附錄:重現圖檔

```bash
conda activate bsma-pdf
cd example-questions/2021-p2-hormone-adaptation

# 原始版(中文標籤)
python fig1_time_series.py     # → fig1_time_series.png
python fig2_phase_plane.py     # → fig2_phase_plane.png

# 教育版(英文乾淨圖,時序 + phase plane;逐行教學註解)
python simulate_edu.py         # → fig1_time_series_clean.png
                               # → fig2_phase_plane_clean.png
```

**何時用哪一個**:
- **原始版** — 中文標籤,最簡可用程式碼參考。
- **`simulate_edu.py`** — 想了解「**為什麼**這樣寫」(為何 `max_step=0.05` 才抓得到 spike、slow manifold 的代數推導、為何「perfect adaptation」是 integral feedback 的特例)。**初值的關鍵教學**:**從平衡點 (1/3, 1) 起步 + H 階躍** 才能凸顯 adaptation,從隨機初值看不出來這個現象。
