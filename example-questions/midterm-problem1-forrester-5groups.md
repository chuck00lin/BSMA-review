# 期中 Problem 1 — 5 群體 Forrester 圖(15%)

> **題目**:Draw a Forrester diagram for the population dynamics of these five groups for a model that simulates a period of 20 years at one-month intervals. Assume that both plant types produce seeds in the fall, but that there is a seed pool available to granivores during other months.
> **參考**:Gause 兩物種競爭方程(式 9.13、9.14)。眉批寫了「食肉動物」。

---

## 1. 先把「five groups」拆清楚

題目沒明寫五個是誰,但從前後文(Gause 兩個 plant types + 種子 + 食種子者 + 食肉者)可以推得:

| # | State Variable | 中文 | 單位 | 對應符號 |
|---|---|---|---|---|
| 1 | $n_1$ | Plant 1(植物 1) | g / m² 或 # | □ |
| 2 | $n_2$ | Plant 2(植物 2) | g / m² 或 # | □ |
| 3 | $S$ | Seed Pool(種子庫) | # seeds | □ |
| 4 | $G$ | Granivores(食種子動物) | # | □ |
| 5 | $C$ | Carnivores(食肉動物) | # | □ |

> **單位一致性檢查**(§3.4 第 9 條):五個方框其實有兩種「貨幣」——
> - 植物與種子是「植物生物量/數量」(g 或 # seeds)
> - granivore/carnivore 是「動物數量」(# individuals)
>
> 不同單位**不能直接物質流互通**,所以「granivore 吃種子」這條連接用**「種子被消費」+「granivore 出生」兩條分開的流**,中間靠「食物轉換效率」這個輔助變數轉換。這就是 §3.3.4 教的「畫多個平行的 Forrester 圖,用資訊流互相影響」。

---

## 2. 質性建模 4 步驟(§3.6)

### 步驟 1:識別 state variables

已列在表 1。

### 步驟 2:識別源(source)與匯(sink)

- **Source**:大氣 CO₂ / 太陽能 / 土壤養分(→ 植物生長);granivore 與 carnivore 的「出生來源」(雲)。
- **Sink**:大氣 CO₂(植物與動物呼吸/分解);廢物;granivore/carnivore 自然死亡。

題目沒有要求把這些當 state variable(我們不建模空氣中 CO₂),所以畫**雲狀符號**。

### 步驟 3:識別物質流

| # | 流名稱 | From | To | 何時發生 | 機制 |
|---|---|---|---|---|---|
| F1 | Plant 1 growth | source(CO₂) | $n_1$ | 全年 | Gause unrestricted + competition(式 9.13) |
| F2 | Plant 2 growth | source(CO₂) | $n_2$ | 全年 | Gause(式 9.14) |
| F3 | Plant 1 mortality | $n_1$ | sink | 全年 | Gause intra- + inter-specific competition |
| F4 | Plant 2 mortality | $n_2$ | sink | 全年 | 同上 |
| F5 | Seed production (Plant 1) | source | $S$ | **只在秋天** | $\propto n_1$,但用驅動變數開關 |
| F6 | Seed production (Plant 2) | source | $S$ | **只在秋天** | $\propto n_2$ |
| F7 | Seed loss (decay/germination 非秋季 outflow) | $S$ | sink | 非秋季 | 自然耗損 / 萌發(可選) |
| F8 | Granivory(吃種子) | $S$ | sink | **非秋季** | mass action ∝ $S \cdot G$ |
| F9 | Granivore birth(吃種子轉換) | source | $G$ | 非秋季 | $\propto S \cdot G$,效率 $\varepsilon_G$ |
| F10 | Predation(吃 granivore) | $G$ | sink | 全年 | mass action ∝ $G \cdot C$ |
| F11 | Carnivore birth | source | $C$ | 全年 | $\propto G \cdot C$,效率 $\varepsilon_C$ |
| F12 | Granivore natural death | $G$ | sink | 全年 | $d_G \cdot G$ |
| F13 | Carnivore natural death | $C$ | sink | 全年 | $d_C \cdot C$ |

> **關鍵設計**:F5/F6 與 F8/F9 都被一個**驅動變數「Season」(月份)**控制——這是 §3.2 的 ◇ 驅動變數符號,題目「fall vs other months」的開關就靠它。

### 步驟 4:識別輔助變數與驅動變數

| 種類 | 名稱 | 說明 |
|---|---|---|
| 驅動變數 ◇ | **Month / Season** | 月份索引,1~12;用來判斷「是不是秋天」 |
| 輔助變數 ○ | $\mathbb{1}_{\text{fall}}(t)$ | 秋季指示函數(秋季=1,其他=0) |
| 輔助變數 ○ | $\mathbb{1}_{\text{non-fall}}(t) = 1 - \mathbb{1}_{\text{fall}}(t)$ | 非秋季指示 |
| 輔助變數 ○ | $R_1 = 1 - (n_1 + \alpha n_2)/K_1$ | Plant 1 的縮減因子(類似 §3.3.2 的 $R$) |
| 輔助變數 ○ | $R_2 = 1 - (n_2 + \beta n_1)/K_2$ | Plant 2 縮減因子 |
| 參數 ○─ | $r_1, r_2, K_1, K_2, \alpha, \beta$ | Gause 參數 |
| 參數 ○─ | $\sigma_1, \sigma_2$ | 每株植物秋季產種子率 |
| 參數 ○─ | $a_G, \varepsilon_G, d_G$ | granivore 搜尋速率 / 轉換效率 / 死亡率 |
| 參數 ○─ | $a_C, \varepsilon_C, d_C$ | carnivore 對應參數 |
| 參數 ○─ | $\mu_S$ | 種子自然耗損率 |

---

## 3. Forrester 圖(文字版)

以下用 §3.2 的符號慣例:
- `□` = 狀態變數
- `⋈` = 速率閥
- `─→` = 物質流(實線)
- `⇢` = 資訊流(虛線)
- `☁` = 源/匯
- `○` = 輔助變數 / 參數
- `◇` = 驅動變數

```
                              ◇ Season (month, 1-12)
                              │
                              ├─⇢ 𝟙_fall ─⇢ ⋈ F5,F6 (秋季開)
                              └─⇢ 𝟙_non-fall ─⇢ ⋈ F8 (非秋季開)

         ☁ CO₂              ☁ CO₂
         │                   │
         ⋈ F1 (Plant 1 growth)   ⋈ F2 (Plant 2 growth)
         │   ⇡ R₁⇠ K₁,α,n₂        │   ⇡ R₂⇠ K₂,β,n₁
         ▼                   ▼
       ┌────┐  Gause coupling ┌────┐
       │ n₁ │ ⇠⇢ α,β ⇠⇢       │ n₂ │
       └────┘                 └────┘
         │ ⇢ σ₁              │ ⇢ σ₂
         ⋈ F5 (秋季: 產種子)    ⋈ F6 (秋季: 產種子)
         │                   │
         └────────┬──────────┘
                  ▼
                ┌────┐
                │ S  │ Seed Pool
                └────┘
                  │ ⇢ a_G
                  ⋈ F8 (非秋季: granivory)    ⋈ F7 (種子自然耗損, μ_S) ─→ ☁
                  │
                  ▼ (mass action with G)
                  ☁ ───⋈ F9 (轉換 ε_G)───→ ┌────┐
                                          │ G  │ Granivores
                                          └────┘
                                            │ ⇢ d_G
                                            ⋈ F10 (predation, a_C·G·C) ⋈ F12 (natural death)
                                            │              │
                                            ▼              ▼
                                            ☁               ☁
                                            ⋈ F11 (轉換 ε_C)
                                            │
                                            ▼
                                          ┌────┐
                                          │ C  │ Carnivores
                                          └────┘
                                            │ ⇢ d_C
                                            ⋈ F13 (natural death) ─→ ☁
```

> 圖中所有「秋季 / 非秋季開關」都是**從同一個 ◇ Season 驅動變數**透過 𝟙_fall、𝟙_non-fall 兩個輔助變數送出的資訊流——這是 §3.2 圖 3.2 標準畫法。

---

## 4. 對應方程式(把圖讀成數學)

設時間步長 $\Delta t = 1$ month,總期 $20 \times 12 = 240$ steps。

### Plant 1(式 9.13 + 種子流調整)

$$
\frac{dn_1}{dt} \;=\; \underbrace{r_1 n_1}_{\text{unrestricted}} \;-\; \underbrace{\frac{r_1 n_1^2}{K_1}}_{\text{intra}} \;-\; \underbrace{\frac{r_1 n_1 (\alpha n_2)}{K_1}}_{\text{inter}}
$$

(若採「種子產出消耗植物資源」的嚴格版本,可再扣 $-\sigma_1 n_1 \mathbb{1}_{\text{fall}}$;若把 Gause 的 $r_1 n_1$ 視為「已內含繁殖機制」,則種子產出走平行的源流,不從 $n_1$ 扣——這是質性建模的設計選擇,§3.3.3 提過。)

### Plant 2(式 9.14)

$$
\frac{dn_2}{dt} \;=\; r_2 n_2 \;-\; \frac{r_2 n_2^2}{K_2} \;-\; \frac{r_2 n_2 (\beta n_1)}{K_2}
$$

### Seed Pool

$$
\frac{dS}{dt} \;=\; \underbrace{\bigl(\sigma_1 n_1 + \sigma_2 n_2\bigr) \mathbb{1}_{\text{fall}}}_{F5+F6\,(秋季產種子)} \;-\; \underbrace{a_G\, S\, G\, \mathbb{1}_{\text{non-fall}}}_{F8\,(granivory)} \;-\; \underbrace{\mu_S S}_{F7\,(耗損)}
$$

### Granivores(用 mass action,§4.3.9)

$$
\frac{dG}{dt} \;=\; \underbrace{\varepsilon_G\, a_G\, S\, G\, \mathbb{1}_{\text{non-fall}}}_{F9\,(從種子轉換)} \;-\; \underbrace{a_C\, G\, C}_{F10\,(被捕食)} \;-\; \underbrace{d_G G}_{F12\,(自然死亡)}
$$

### Carnivores(同 §4.3.9 / 式 4.23-4.24)

$$
\frac{dC}{dt} \;=\; \underbrace{\varepsilon_C\, a_C\, G\, C}_{F11\,(從 granivore 轉換)} \;-\; \underbrace{d_C C}_{F13\,(自然死亡)}
$$

> 這正是 Lotka–Volterra(式 4.23/4.24)的形式,只是這裡的「prey」是 granivore。

---

## 5. 對照講義(我用了哪些章節)

| 題目要素 | 講義來源 |
|---|---|
| 5 個方框(state variables)+ 物質/資訊流符號 | [03-質性建模與Forrester圖.md §3.2](../redesigned/03-質性建模與Forrester圖.md) |
| 多狀態 / 多單位流動(§3.3.3, §3.3.4) | 同上 §3.3.3-§3.3.4 |
| Gause 競爭(式 9.13/9.14) | [09-模型分析.md §9.3.3](../redesigned/09-模型分析.md) |
| Lotka–Volterra(F10/F11 與 F8/F9 用的 mass action 形式) | [04-量化建模I.md §4.3.9](../redesigned/04-量化建模I.md) |
| 驅動變數 ◇(用於 fall 開關) | [03-質性建模與Forrester圖.md §3.2 符號表](../redesigned/03-質性建模與Forrester圖.md) |
| Δt = 1 month、20 yr 模擬(數值積分) | [06-數值技巧.md](../redesigned/06-數值技巧.md) |

---

## 6. 自我檢查清單(§3.4 十條規則)

| # | 規則 | 我這張圖是否合規? |
|---|---|---|
| 1 | 只用 §3.2 定義的符號 | ✅ |
| 2 | 每個方框/變數/參數都標**名稱與單位** | ✅(見表 1、表 4) |
| 3 | 源/匯不能影響速率 | ✅(雲只當源/匯) |
| 4 | 速率不直接連到方框,要透過閥 | ✅ |
| 5 | 狀態只能透過速率改變(資訊流不能進方框) | ✅ |
| 6 | 物質流只連狀態變數或源/匯 | ✅ |
| 7 | 參數不能被影響 | ✅ |
| 8 | 兩個狀態變數不能用資訊流直接相連(中間要過閥) | ✅ — Gause 的 $\alpha n_2$ 是進入「Plant 1 的成長閥」,不是直接打到 $n_1$ 方框 |
| 9 | 單位相容(g N 不能流進 g C) | ⚠️ **要注意**:F8(seed 被吃)與 F9(granivore 出生)是**兩條獨立的流**,中間靠 $\varepsilon_G$ 換單位——不是同一條物質流橫跨單位 |
| 10 | 圖上有的狀態變數要出現在方程式裡(反之亦然) | ✅(5 個方框 ↔ 5 條 ODE) |

---

## 7. 課堂答題建議

1. **先畫骨架**:5 個方框、源匯雲、必要的閥。**不要一開始就糾結資訊流**,等所有實線畫完再補虛線。
2. **明確標「秋季開關」**:用 ◇ Season 驅動變數連 F5、F6、F8——這是題目唯一的「時間相依」線索,評分點會落在這。
3. **不要把 granivore 直接畫一條流到 plant**:granivore 吃的是**種子**(S),不是直接吃植物。題目寫得很清楚。
4. **carnivore 的食物是 granivore**(眉批的「食肉動物」)——這條 predator-prey 是標準 Lotka–Volterra,參考 §3.3.4 圖 3.10。
5. **單位不一致時**(植物 g vs 動物 #),記得 §3.3.4:**平行畫,資訊流連接**,別偷懶把克的流進「個體數」的方框(規則 9)。

---

## 附錄:若要實際模擬(Δt = 1 month, 20 yr)

用 conda env `data__env`:

```bash
conda activate data__env
python simulate_5group.py
```

`simulate_5group.py` 骨架(這份還沒寫,等你說要就補):
- Euler 法,Δt = 1/12 yr
- 秋季 = month ∈ {9, 10, 11}(可調)
- 初始值與參數可從 §9.3.4 Gause 例子的 $(r_1, K_1, \alpha) = (0.05, 200, 0.2)$ 起手,granivore/carnivore 用 §4.3.9 例值
- 輸出五條曲線 + 相空間圖
