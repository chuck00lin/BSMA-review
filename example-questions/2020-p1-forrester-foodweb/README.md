# 2020 期中 Problem 1 — 5 群體 Forrester 圖(15%)

## 原題(完整)

> **Problem 1: (15%) – In-Class Problem**
>
> In the SW deserts of North America, **ants, birds, small mammals, and plants** interact to create a complex foodweb. The primary interactions are as follows.
>
> - Ants and small mammals **compete for seeds** produced by two kinds of plants: **small-seeded** and **large-seeded** plants.
> - Within limits, both granivores can consume both sizes of seeds, but, understandably, **ants favor small seeds** and **mammals prefer large seeds**.
> - Consumption of seeds **reduces the population growth rates of the plants**.
> - Birds also consume **large seeds**, but are **more effective at times when the amount of bare ground is high** (or, the amount of plants is low).
> - **Neither birds nor small mammals eat ants.**
> - The two types of plants **compete for space**.
>
> Draw a **Forrester diagram** for the population dynamics of these **five groups** for a model that simulates a period of **20 years at one-month intervals**. Assume that **both plant types produce seeds in the fall**, but that there is a **seed pool available to granivores during other months**.

---

## 0. 先把「five groups」釘清楚(這題的第一個地雷)

原題明說五個 **groups(族群)** 是:

| # | State Variable | 中文 | 單位 |
|---|---|---|---|
| 1 | $P_S$ | Small-seeded plants(小種子植物) | g/m² 或 # |
| 2 | $P_L$ | Large-seeded plants(大種子植物) | g/m² 或 # |
| 3 | $A$ | Ants(螞蟻) | # individuals |
| 4 | $M$ | Small mammals(小型哺乳類) | # individuals |
| 5 | $B$ | Birds(鳥) | # individuals |

> **常見錯誤**:把鳥當「carnivore(食肉動物)」自成一層。原題講得很清楚——**沒有任何一群會吃 ants**(neither birds nor small mammals eat ants),也沒有任何一群吃 birds 或 mammals。**這不是一個三層 food chain,是一個「植物→種子→兩種 granivore + 鳥」的競爭結構**。

### 兩個 seed pool 算不算 group?

原題的 seed pool 是**輔助 stock**,不是 group:
- 「Draw a Forrester diagram for the population dynamics of **these five groups**」——五個 group 是植物與動物族群。
- 「a seed pool available to granivores during other months」——這句話建議我們需要一個 stock 來儲存秋天產的種子,讓動物在非秋季也能吃到。但**它不是「群體」**。

所以圖上會有 **5 個 group 方框 + 2 個 seed pool 輔助方框($S_S, S_L$)**,總共 7 個 stock。group 數還是 5。

---

## 1. 質性建模 4 步驟(§3.6)

### 步驟 1:識別 state variables

主 state(5 groups):$P_S, P_L, A, M, B$。
輔助 stock(seed pools):$S_S$(small seeds),$S_L$(large seeds)。

### 步驟 2:識別源與匯

- **Source**(雲 ☁):大氣 CO₂ / 太陽能(→ 植物);動物的「出生」(由吃進來的食物轉換)。
- **Sink**(雲 ☁):植物的呼吸/枯死;動物的自然死亡;種子的自然耗損(發芽未存活、腐爛)。

### 步驟 3:識別物質流

| # | 流名稱 | From | To | 季節 | 機制 |
|---|---|---|---|---|---|
| F1 | 小種子植物成長 | ☁ | $P_S$ | 全年 | logistic + 競爭 |
| F2 | 大種子植物成長 | ☁ | $P_L$ | 全年 | logistic + 競爭 |
| F3 | 小種子植物枯死 | $P_S$ | ☁ | 全年 | 含於 logistic |
| F4 | 大種子植物枯死 | $P_L$ | ☁ | 全年 | 含於 logistic |
| F5 | 小種子產出 | ☁ | $S_S$ | **僅秋季** | $\sigma_S P_S$,由 ◇ Season 開關 |
| F6 | 大種子產出 | ☁ | $S_L$ | **僅秋季** | $\sigma_L P_L$,同上 |
| F7 | 小種子耗損(發芽/腐爛) | $S_S$ | ☁ | 全年 | $\mu_S S_S$ |
| F8 | 大種子耗損 | $S_L$ | ☁ | 全年 | $\mu_L S_L$ |
| F9 | 螞蟻吃小種子(主食) | $S_S$ | ☁ | **非秋季** | $a_{AS} S_S A$, $a_{AS}$ 大 |
| F10 | 螞蟻吃大種子(次選) | $S_L$ | ☁ | 非秋季 | $a_{AL} S_L A$, $a_{AL} \ll a_{AS}$ |
| F11 | 哺乳類吃大種子(主食) | $S_L$ | ☁ | 非秋季 | $m_{ML} S_L M$, $m_{ML}$ 大 |
| F12 | 哺乳類吃小種子(次選) | $S_S$ | ☁ | 非秋季 | $m_{MS} S_S M$, $m_{MS} \ll m_{ML}$ |
| F13 | 鳥吃大種子 | $S_L$ | ☁ | **全年但受 bare ground 調節** | $b_L S_L B \cdot \phi(P_S+P_L)$ |
| F14 | 螞蟻出生 | ☁ | $A$ | 全年 | $\varepsilon_A \cdot (\text{F9+F10})$ |
| F15 | 哺乳類出生 | ☁ | $M$ | 全年 | $\varepsilon_M \cdot (\text{F11+F12})$ |
| F16 | 鳥出生 | ☁ | $B$ | 全年 | $\varepsilon_B \cdot \text{F13}$ |
| F17 | 螞蟻自然死亡 | $A$ | ☁ | 全年 | $d_A A$ |
| F18 | 哺乳類自然死亡 | $M$ | ☁ | 全年 | $d_M M$ |
| F19 | 鳥自然死亡 | $B$ | ☁ | 全年 | $d_B B$ |

> **單位問題**(§3.4 第 9 條):植物與種子是「生物量 / 數量」,動物是「個體數」——**兩種單位不能直接物質流互通**。所以 F9/F14、F10–F12、F13/F16 都各自畫**兩條獨立的流**(seed 端進 sink、動物端從 source 出生),中間靠「轉換效率 $\varepsilon$」這個輔助參數做橋。這是 §3.3.4 的標準「多單位 Forrester 圖」處理。

### 步驟 4:識別輔助變數與驅動變數

| 種類 | 名稱 | 說明 |
|---|---|---|
| 驅動變數 ◇ | Month / Season | 月份索引 1–12 |
| 輔助 ○ | $\mathbf{1}_{\text{fall}}(t)$ | 秋季指示;F5、F6 用 |
| 輔助 ○ | $\mathbf{1}_{\text{non-fall}}(t)$ | 非秋季指示;F9–F12 用 |
| 輔助 ○ | $G = P_S + P_L$ | 總植被量(資訊流) |
| 輔助 ○ | $\phi(G) = 1/(1 + G/G_0)$ | bare-ground 增益因子,$G$ 低時 $\phi \to 1$, $G$ 高時 $\phi \to 0$;F13 用 |
| 參數 ○─ | $r_S, K_S, \alpha_{SL}$ | 小種子植物 logistic |
| 參數 ○─ | $r_L, K_L, \alpha_{LS}$ | 大種子植物 logistic |
| 參數 ○─ | $\sigma_S, \sigma_L$ | 秋季產種子率 |
| 參數 ○─ | $\mu_S, \mu_L$ | 種子自然耗損率 |
| 參數 ○─ | $a_{AS}, a_{AL}, \varepsilon_A, d_A$ | 螞蟻參數 |
| 參數 ○─ | $m_{ML}, m_{MS}, \varepsilon_M, d_M$ | 哺乳類參數 |
| 參數 ○─ | $b_L, G_0, \varepsilon_B, d_B$ | 鳥參數 |

---

## 2. Forrester 圖(文字版)

符號慣例(§3.2):`□` = 狀態方框,`⋈` = 速率閥,`─→` = 物質流,`⇢` = 資訊流,`☁` = source/sink,`○` = 輔助/參數,`◇` = 驅動變數。

```
                              ◇ Season (1-12)
                                ├─⇢ 𝟙_fall      ─⇢ F5, F6           (秋季開)
                                └─⇢ 𝟙_non-fall  ─⇢ F9, F10, F11, F12 (非秋季開)

        ☁ CO₂                          ☁ CO₂
         │                              │
         ⋈ F1 (P_S 成長)                  ⋈ F2 (P_L 成長)
         │  ⇡ R_S ⇠ K_S, α_SL, P_L        │  ⇡ R_L ⇠ K_L, α_LS, P_S
         ▼                              ▼
       ┌─────┐  ─── 競爭(α_SL, α_LS) ─── ┌─────┐
       │ P_S │ ⇠⇢⇠⇢⇠⇢⇠⇢⇠⇢⇠⇢⇠⇢⇠⇢⇠⇢⇠⇢⇠⇢ │ P_L │
       └─┬───┘                          └───┬─┘
         ⋈ F3 (枯死) ─→ ☁                    ⋈ F4 (枯死) ─→ ☁
         │ ⇢ σ_S                            │ ⇢ σ_L
         ⋈ F5 (秋季:小種子產出) ☁           ⋈ F6 (秋季:大種子產出) ☁
         │                                  │
         ▼                                  ▼
       ┌─────┐                           ┌─────┐
       │ S_S │ ─⋈ F7 (μ_S) ─→ ☁          │ S_L │ ─⋈ F8 (μ_L) ─→ ☁
       └──┬──┘                           └──┬──┘
          │                                 │
          │── ⋈ F9 (a_AS, 非秋季) ─→ ☁      │── ⋈ F11 (m_ML, 非秋季) ─→ ☁
          │   ⇡ A                           │   ⇡ M
          │── ⋈ F12 (m_MS, 非秋季) ─→ ☁     │── ⋈ F10 (a_AL, 非秋季) ─→ ☁
              ⇡ M                               ⇡ A
                                            │── ⋈ F13 (b_L · φ(G)) ─→ ☁
                                                ⇡ B          ⇡ φ ⇠ G = P_S + P_L

        Ant 出生(轉換 ε_A)                Mammal 出生(轉換 ε_M)         Bird 出生(轉換 ε_B)
        ☁ ─⋈ F14─→ ┌───┐                 ☁ ─⋈ F15─→ ┌───┐               ☁ ─⋈ F16─→ ┌───┐
                   │ A │                              │ M │                            │ B │
                   └─┬─┘                              └─┬─┘                            └─┬─┘
                     ⋈ F17 (d_A) ─→ ☁                    ⋈ F18 (d_M) ─→ ☁                ⋈ F19 (d_B) ─→ ☁
```

**重點**:
- 所有「fall / non-fall 開關」都從同一個 ◇ Season 經 $\mathbf{1}_{\text{fall}}$、 $\mathbf{1}_{\text{non-fall}}$ 兩個輔助變數送資訊流出去(§3.2 圖 3.2 標準畫法)。
- $\phi(G) = 1/(1+G/G_0)$ 是「**bare-ground 增益**」——資訊流從兩個植物 stock $P_S, P_L$ 加總後算出,送進 F13 的閥。這對應原題「birds are more effective when bare ground is high」。
- **沒有 carnivore**——沒有任何流從 $A$、 $M$、 $B$ 進到另一個動物 stock。

---

## 3. 對應方程式(把圖讀成數學)

設時間步 $\Delta t = 1$ 月,總期 $20 \times 12 = 240$ 步。

### 3.1 兩種植物(Gause 競爭,§4.3.9 / 9.3.3)

$$
\frac{dP_S}{dt} = r_S\,P_S\left(1 - \frac{P_S + \alpha_{SL} P_L}{K_S}\right)
$$

$$
\frac{dP_L}{dt} = r_L\,P_L\left(1 - \frac{P_L + \alpha_{LS} P_S}{K_L}\right)
$$

> 「Consumption of seeds reduces plant growth rates」可以**用一個額外負項**(直接從 $r_S, r_L$ 減去 $\sigma_S, \sigma_L \mathbf{1}_{\text{fall}}$ 抽走的部分),也可以**設計成 $r$ 已內含繁殖代價**——兩種都對,寫答案時要說明你的選擇(§3.3.3 的「設計選擇」)。

### 3.2 兩個 seed pool

$$
\frac{dS_S}{dt} = \underbrace{\sigma_S P_S \cdot \mathbf{1}_{\text{fall}}}_{\text{F5: 秋季產出}} - \underbrace{(a_{AS} A + m_{MS} M)\,S_S \cdot \mathbf{1}_{\text{non-fall}}}_{\text{F9 + F12: 被吃}} - \underbrace{\mu_S\,S_S}_{\text{F7: 耗損}}
$$

$$
\frac{dS_L}{dt} = \underbrace{\sigma_L P_L \cdot \mathbf{1}_{\text{fall}}}_{\text{F6: 秋季產出}} - \underbrace{(a_{AL} A + m_{ML} M)\,S_L \cdot \mathbf{1}_{\text{non-fall}}}_{\text{F10 + F11: ant/mammal 吃}} - \underbrace{b_L B\,\phi(G)\,S_L}_{\text{F13: 鳥吃}} - \underbrace{\mu_L\,S_L}_{\text{F8: 耗損}}
$$

> **注意 F13 不被 $\mathbf{1}_{\text{non-fall}}$ 限制**——鳥可以全年吃,但效率被 $\phi(G)$ 調節。原題「more effective when bare ground is high」就是 $\phi(G)$ 在 $G$ 低時放大。

### 3.3 螞蟻

$$
\frac{dA}{dt} = \underbrace{\varepsilon_A\,(a_{AS} S_S + a_{AL} S_L)\,A\,\mathbf{1}_{\text{non-fall}}}_{\text{F14: 從吃進的種子轉換為個體}} - \underbrace{d_A\,A}_{\text{F17: 自然死亡}}
$$

### 3.4 小型哺乳類

$$
\frac{dM}{dt} = \underbrace{\varepsilon_M\,(m_{ML} S_L + m_{MS} S_S)\,M\,\mathbf{1}_{\text{non-fall}}}_{\text{F15: 從吃進的種子轉換}} - \underbrace{d_M\,M}_{\text{F18: 自然死亡}}
$$

### 3.5 鳥

$$
\frac{dB}{dt} = \underbrace{\varepsilon_B\,b_L\,B\,\phi(G)\,S_L}_{\text{F16: 從吃進的大種子轉換}} - \underbrace{d_B\,B}_{\text{F19: 自然死亡}}
$$

### 3.6 輔助關係

$$
\mathbf{1}_{\text{fall}}(t) = \begin{cases} 1 & \text{若 month}(t) \in \{9,10,11\} \\ 0 & \text{其他} \end{cases}, \qquad \mathbf{1}_{\text{non-fall}} = 1 - \mathbf{1}_{\text{fall}}
$$

$$
G(t) = P_S(t) + P_L(t), \qquad \phi(G) = \frac{1}{1 + G/G_0}
$$

---

## 4. 為什麼這個結構抓得到「題目所有要求」

逐條對照原題:

| 原題要求 | 模型對應 |
|---|---|
| Ants 和 mammals 競爭種子 | F9–F12 都從 $S_S, S_L$ 流出,共享同一個種子池 |
| Ants 偏好小種子 | $a_{AS} \gg a_{AL}$ |
| Mammals 偏好大種子 | $m_{ML} \gg m_{MS}$ |
| 吃種子會降低植物成長率 | F5/F6 把種子搬出植物的「繁殖預算」(或寫為 $r_S, r_L$ 已扣) |
| Birds 吃大種子 | F13:只從 $S_L$ 流出 |
| Birds 效率隨 bare ground 升高 | $\phi(G) = 1/(1+G/G_0)$:植被多時 $\phi$ 小,植被少時 $\phi$ 大 |
| 鳥和哺乳類**都不吃螞蟻** | **圖上沒有 $A \to B$ 或 $A \to M$ 的物質流** |
| 兩種植物競爭空間 | Gause $\alpha_{SL}, \alpha_{LS}$ 交互項 |
| 秋季產種子,其他月份種子被吃 | F5/F6 由 $\mathbf{1}_{\text{fall}}$ 開;F9–F12 由 $\mathbf{1}_{\text{non-fall}}$ 開 |
| 20 yr, $\Delta t = 1$ 月 | 240 個積分步 |

---

## 5. 對照講義

| 題目要素 | 講義來源 |
|---|---|
| 5 個方框、物質/資訊流符號 | [03-質性建模與Forrester圖.md §3.2](../../redesigned/03-質性建模與Forrester圖.md) |
| 多狀態、多單位流動(植物 g vs 動物 #) | 同上 §3.3.3-§3.3.4 |
| Gause 兩物種競爭(§4.3.9 / 9.3.3) | [04-量化建模I.md §4.3.9](../../redesigned/04-量化建模I.md) [09-模型分析.md §9.3.3](../../redesigned/09-模型分析.md) |
| Mass-action 形式($A \cdot S_S$ 等) | [04-量化建模I.md §4.3.9](../../redesigned/04-量化建模I.md) |
| 驅動變數 ◇(用於 fall 開關) | [03-質性建模與Forrester圖.md §3.2 符號表](../../redesigned/03-質性建模與Forrester圖.md) |
| Functional response 修飾($\phi(G)$ for birds) | [04-量化建模I.md §4.3.4](../../redesigned/04-量化建模I.md) |
| 20 yr, $\Delta t = 1$ 月 數值積分 | [06-數值技巧.md](../../redesigned/06-數值技巧.md) |

---

## 6. 自我檢查(§3.4 十條規則)

| # | 規則 | 我這張圖是否合規? |
|---|---|---|
| 1 | 只用 §3.2 定義的符號 | ✅ |
| 2 | 每個方框/變數/參數都標**名稱與單位** | ✅(見表 1 與輔助/參數表) |
| 3 | 源/匯不能影響速率 | ✅(雲只當 source/sink) |
| 4 | 速率不直接連到方框,要透過閥 | ✅ |
| 5 | 狀態只能透過速率改變 | ✅(資訊流不進方框) |
| 6 | 物質流只連狀態變數或源/匯 | ✅ |
| 7 | 參數不能被影響 | ✅ |
| 8 | 兩個狀態變數不能用資訊流直接相連 | ✅(Gause 的 $\alpha P_L$ 進的是 $P_S$ 的成長閥,不是直接打到 $P_S$ 方框) |
| 9 | 單位相容(g 不能流進 #) | ⚠️ **要注意**:F9–F13 是「種子被吃」的物質流(g);動物個體增加用平行的 F14–F16(#),中間靠 $\varepsilon$ 轉單位 |
| 10 | 圖上有的狀態變數要出現在方程式裡(反之亦然) | ✅(5 個 group + 2 個 seed pool ↔ 7 條 ODE) |

---

## 7. 課堂答題建議

1. **先寫清楚「五個 group」是誰**——很多人會把鳥誤當 carnivore,在這題會直接失分。原題明寫 "Neither birds nor small mammals eat ants",白紙黑字。
2. **seed pool 不算 group,但圖要畫**——「a seed pool available to granivores during other months」這句話強迫你加 $S_S, S_L$ 兩個輔助 stock。**沒畫種子池會少很多評分點**。
3. **季節開關用 ◇ Season → 𝟙_fall, 𝟙_non-fall 兩個輔助**——這是 §3.2 圖 3.2 的標準畫法,別用其他符號。
4. **bare-ground 機制**——鳥的覓食效率隨植被密度反向變化。寫一個 $\phi(G) = 1/(1+G/G_0)$ 或類似的形式就好。
5. **沒有 predator-prey** ——這題的競爭/捕食結構是「植物 → 種子 → 兩種 granivore + 鳥」的扇形,**不是 Lotka–Volterra 食物鏈**。不要把它寫成 LV。

---

## 附錄:若要實際模擬(Δt = 1 月, 20 yr)

```bash
conda activate data__env
python simulate_5group.py     # (尚未實作,要的話再寫)
```

`simulate_5group.py` 骨架:
- Euler 或 RK4,$\Delta t = 1/12$ yr。
- 秋季 = month ∈ {9, 10, 11}。
- 初始值與參數可從 [09-模型分析.md §9.3.4](../../redesigned/09-模型分析.md) Gause 例子的 $(r_1, K_1, \alpha) = (0.05, 200, 0.2)$ 起手;granivore 用 [04-量化建模I.md §4.3.9](../../redesigned/04-量化建模I.md) 例值;$\phi(G)$ 的 $G_0$ 取總承載力的 1/10 量級。
- 輸出 5 條族群曲線 + 2 條 seed pool 曲線 + 相空間圖。
