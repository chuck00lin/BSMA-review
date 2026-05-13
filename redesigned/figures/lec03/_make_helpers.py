"""Helper illustrations for Lecture 03 of the BSMA redesign.

Helpers:
  1. Forrester symbol cheat-sheet (Chinese labels)
  2. Step-by-step build of the grass-deer Forrester diagram (4 panels)
  3. Diagram → equation mapping for the density-independent model (Eq 3.1)
  4. Diagram → equation mapping for the density-dependent model (Eq 3.2)
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
# Forrester-symbol drawing primitives
# ----------------------------------------------------------------------------
def draw_state_box(ax, x, y, w=0.9, h=0.6, label="N", units="#"):
    rect = mpatches.Rectangle((x, y), w, h, linewidth=1.8,
                               edgecolor="black", facecolor="white")
    ax.add_patch(rect)
    ax.text(x + w / 2, y + h * 0.62, label, fontsize=11,
            ha="center", va="center", fontweight="bold")
    ax.text(x + w / 2, y + h * 0.22, units, fontsize=8,
            ha="center", va="center", color="#4a5568")


def draw_cloud(ax, x, y, scale=0.18):
    # Stylised cloud (source/sink)
    for dx, dy, r in [(-1, 0, 1), (-0.4, 0.7, 0.8), (0.4, 0.7, 0.9),
                       (1.0, 0.3, 0.85), (0.2, -0.2, 0.8)]:
        c = mpatches.Circle((x + dx * scale, y + dy * scale), r * scale,
                             linewidth=1.4, edgecolor="black", facecolor="white")
        ax.add_patch(c)


def draw_valve(ax, x, y, size=0.14, label=""):
    # Hourglass valve symbol
    pts = [(x - size, y + size), (x + size, y + size),
           (x - size, y - size), (x + size, y - size), (x - size, y + size)]
    xs, ys = zip(*pts)
    ax.plot(xs, ys, "-", color="black", linewidth=1.6)
    # cross line
    ax.plot([x - size, x + size], [y - size, y + size], "-",
            color="black", linewidth=1.6)
    if label:
        ax.text(x, y - size - 0.1, label, fontsize=9,
                ha="center", va="top")


def draw_material_arrow(ax, x1, y1, x2, y2, with_valve=True, label=""):
    if with_valve:
        mx, my = (x1 + x2) / 2, (y1 + y2) / 2
        ax.annotate("", xy=(mx - 0.18, my), xytext=(x1, y1),
                    arrowprops=dict(arrowstyle="-", linewidth=1.6, color="black"))
        draw_valve(ax, mx, my, label=label)
        ax.annotate("", xy=(x2, y2), xytext=(mx + 0.18, my),
                    arrowprops=dict(arrowstyle="->", linewidth=1.6, color="black"))
    else:
        ax.annotate("", xy=(x2, y2), xytext=(x1, y1),
                    arrowprops=dict(arrowstyle="->", linewidth=1.6, color="black"))


def draw_info_arrow(ax, x1, y1, x2, y2, color="#2b6cb0"):
    ax.annotate("", xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle="->", linewidth=1.4,
                                color=color, linestyle="dashed"))


def draw_param(ax, x, y, label):
    c = mpatches.Circle((x, y), 0.10, linewidth=1.4,
                         edgecolor="black", facecolor="white")
    ax.add_patch(c)
    ax.plot([x - 0.10, x + 0.10], [y, y], "-", color="black", linewidth=1.0)
    ax.text(x, y + 0.20, label, fontsize=10, ha="center")


def draw_aux(ax, x, y, label, w=0.7):
    e = mpatches.Ellipse((x, y), w, 0.35, linewidth=1.4,
                          edgecolor="black", facecolor="white")
    ax.add_patch(e)
    ax.text(x, y, label, fontsize=9, ha="center", va="center")


# ----------------------------------------------------------------------------
# Helper 1: Forrester symbol cheat-sheet (Chinese) — single column, roomy
# ----------------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(13, 13))
ax.set_xlim(0, 13)
ax.set_ylim(0, 16)
ax.axis("off")

rows = [
    ("狀態變數", "state variable / level",
     "我們關心、想預測其隨時間變化的「量」。畫成一個方框,標上名稱與單位。"
     "這是模型的主角——我們寫方程式的對象。",
     lambda a, y: draw_state_box(a, 1.0, y - 0.3, w=1.4, h=0.7, label="N", units="單位")),
    ("物質流", "material flow",
     "實線箭頭 + 中間的閥(類似砂漏的符號),代表「實際的物質、能量在流動」。"
     "中間的「閥」象徵這個流動是受「速率方程式」控制的——後面 §3.3 會看到。",
     lambda a, y: draw_material_arrow(a, 0.8, y, 2.6, y)),
    ("資訊流(影響)", "information flow / influence",
     "虛線箭頭。代表「一個變數的『值』影響到另一個地方的『流動率』」。"
     "**沒有實際物質在動,只有資訊**。常用來表達「人口越多,死亡速率也越高」這種影響關係。",
     lambda a, y: draw_info_arrow(a, 0.8, y, 2.6, y, color="black")),
    ("源 / 匯", "source / sink",
     "雲狀符號。「源」是系統之外、提供流入的東西;「匯」是系統之外、接收流出的東西。"
     "我們不為它寫方程式——它「沒有狀態」。大氣 CO2、太陽、地下水都是常見的源或匯。",
     lambda a, y: draw_cloud(a, 1.5, y, scale=0.25)),
    ("參數", "parameter",
     "圓圈 + 一橫,代表「方程式中的常數」(例如成長率 b、死亡率 d、承載量 K)。"
     "參數在模擬時保持不變,但會影響「閥」的開合大小。",
     lambda a, y: draw_param(a, 1.5, y, "k")),
    ("速率方程式", "rate equation (valve)",
     "閥的符號。當我們把物質流箭頭具體畫出時,閥就代表「這個流的速率公式」。"
     "閥被「參數」和「狀態變數」(透過資訊流)所控制。",
     lambda a, y: draw_valve(a, 1.5, y, label="")),
    ("輔助變數", "auxiliary variable",
     "圓形或橢圓 + 名稱。代表「由其他變數計算出來的中間量」"
     "(例如 logistic 模型裡的 reduction factor R = 1 − N/K)。它幫助我們把複雜公式拆成幾步。",
     lambda a, y: draw_aux(a, 1.5, y, "f(N)")),
    ("驅動變數", "driving variable",
     "菱形 + 名稱。「來自系統外」、會隨時間變化的輸入(例如季節、溫度、降雨)。"
     "它不是狀態變數(我們不為它寫方程式),但又會變動——所以單獨給一個符號。",
     lambda a, y: a.add_patch(mpatches.Polygon(
         [(1.1, y), (1.5, y - 0.3), (1.9, y), (1.5, y + 0.3)],
         linewidth=1.4, edgecolor="black", facecolor="white"))),
]

y0 = 15.0
dy = 1.75
for i, (zh, en, desc, draw_fn) in enumerate(rows):
    y = y0 - i * dy
    draw_fn(ax, y)
    ax.text(3.5, y + 0.55, f"{zh}", fontsize=15,
            color="#2b6cb0", fontweight="bold")
    ax.text(3.5, y + 0.15, f"({en})", fontsize=11,
            color="#4a5568", style="italic")
    ax.text(3.5, y - 0.4, desc, fontsize=11, color="#1a202c",
            verticalalignment="top", wrap=True)

fig.suptitle("Forrester 圖的 8 個基本符號", fontsize=17, y=0.995,
             color="#2b6cb0")
plt.savefig(OUTDIR / "helper-1-forrester-symbols.png",
            dpi=160, bbox_inches="tight", facecolor="white")
plt.close()


# ----------------------------------------------------------------------------
# Helper 2: Step-by-step build of grass-deer (4 panels)
# ----------------------------------------------------------------------------
fig, axes = plt.subplots(2, 2, figsize=(13, 8.5))
panel_titles = [
    "步驟 1:辨識「狀態變數」",
    "步驟 2:加上「源」與「匯」",
    "步驟 3:加上「物質流」",
    "步驟 4:加上「資訊流」(影響)",
]
panel_subtitles = [
    "我們關心 grass 與 deer 兩個量(以「碳含量,g C」計)。",
    "外面的大氣 CO₂ 既是源也是匯;固液廢物也是匯。",
    "三條 C 流:植物吸收 CO₂ → grass → 鹿吃 → deer → 排泄/呼吸 → 大氣/廢物。",
    "影響:grass 自己影響 plant uptake 速率;grass 與 deer 共同影響 consumption 速率;deer 影響自己的死亡速率。",
]

for k, (ax, title, sub) in enumerate(zip(axes.flat, panel_titles, panel_subtitles)):
    ax.set_xlim(0, 9)
    ax.set_ylim(0, 5)
    ax.axis("off")
    ax.set_title(f"{title}\n", fontsize=12, color="#2b6cb0", loc="left", pad=6)
    ax.text(0.1, 4.6, sub, fontsize=9.5, color="#4a5568", style="italic")

    grass = (3.2, 2.8)
    deer = (5.6, 2.8)

    # Panel 1: just state variables
    if k >= 0:
        draw_state_box(ax, grass[0] - 0.45, grass[1] - 0.3,
                       label="grass", units="g C")
        draw_state_box(ax, deer[0] - 0.45, deer[1] - 0.3,
                       label="deer", units="g C")

    # Panel 2: add sources/sinks
    if k >= 1:
        draw_cloud(ax, 1.5, 2.8, scale=0.22)
        ax.text(1.5, 2.0, "大氣 CO₂", fontsize=9, ha="center", color="#4a5568")
        draw_cloud(ax, 7.8, 2.8, scale=0.22)
        ax.text(7.8, 2.0, "大氣 CO₂\n+ 廢物", fontsize=9, ha="center", color="#4a5568")
        # consumption sink (atmospheric CO2 above)
        draw_cloud(ax, 4.4, 4.2, scale=0.18)
        ax.text(4.4, 4.65, "大氣 CO₂", fontsize=8, ha="center", color="#4a5568")

    # Panel 3: add material flows
    if k >= 2:
        draw_material_arrow(ax, 1.95, 2.8, 2.65, 2.8,
                             with_valve=True, label="uptake")
        draw_material_arrow(ax, 3.85, 2.8, 5.15, 2.8,
                             with_valve=True, label="consumption")
        draw_material_arrow(ax, 6.05, 2.8, 7.35, 2.8,
                             with_valve=True, label="death/excrete")

    # Panel 4: add information flows (dotted)
    if k >= 3:
        # grass affects own uptake rate (loop back)
        draw_info_arrow(ax, grass[0], grass[1] - 0.25,
                         2.3, 2.65)
        # grass affects consumption rate
        draw_info_arrow(ax, grass[0] + 0.45, grass[1] - 0.25,
                         4.45, 2.6)
        # deer affects consumption rate
        draw_info_arrow(ax, deer[0] - 0.45, deer[1] - 0.25,
                         4.55, 2.5)
        # deer affects own death rate
        draw_info_arrow(ax, deer[0], deer[1] - 0.25,
                         6.7, 2.65)

fig.suptitle("如何用 4 步畫出「草—鹿」生態系的 Forrester 圖",
             fontsize=15, y=0.99)
plt.tight_layout()
plt.savefig(OUTDIR / "helper-2-grass-deer-buildup.png",
            dpi=160, bbox_inches="tight", facecolor="white")
plt.close()


# ----------------------------------------------------------------------------
# Helper 3: Diagram → Equation mapping (density-independent, Eq 3.1)
# ----------------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(12, 5.5))
ax.set_xlim(0, 12)
ax.set_ylim(0, 5.5)
ax.axis("off")

# Left side: diagram
draw_cloud(ax, 0.8, 3.0, scale=0.20)
draw_state_box(ax, 3.0, 2.7, w=1.2, h=0.7, label="N", units="#")
draw_cloud(ax, 6.0, 3.0, scale=0.20)
draw_material_arrow(ax, 1.4, 3.05, 2.9, 3.05, with_valve=True, label="birth")
draw_material_arrow(ax, 4.3, 3.05, 5.65, 3.05, with_valve=True, label="death")
draw_param(ax, 1.9, 4.2, "b")
draw_info_arrow(ax, 1.9, 4.05, 2.05, 3.25)
draw_param(ax, 5.0, 4.2, "d")
draw_info_arrow(ax, 5.0, 4.05, 4.95, 3.25)
# N affects both rates (self-loops)
draw_info_arrow(ax, 3.35, 2.7, 2.15, 2.95)
draw_info_arrow(ax, 3.85, 2.7, 4.85, 2.95)

ax.text(3.6, 1.7, "圖 3.4 的 Forrester 圖", fontsize=11, ha="center",
        color="#2b6cb0", fontweight="bold")

# Right side: equation breakdown
eq_x = 8.5
ax.text(eq_x, 4.7, "對應的差分方程式(式 3.1):", fontsize=12,
        color="#22543d", fontweight="bold")
ax.text(eq_x, 3.9,
        r"$N_{t+1} \;=\; N_t \;+\; b\,N_t \;-\; d\,N_t$",
        fontsize=15)
ax.text(eq_x + 2.05, 3.55, "↑ birth 流入", fontsize=9, color="#2b6cb0", ha="center")
ax.text(eq_x + 3.4, 3.55, "↑ death 流出", fontsize=9, color="#c53030", ha="center")

ax.text(eq_x, 2.9, "每一項對應圖上一個元件:", fontsize=10, color="#22543d")
mapping = [
    (r"$N_t$"          , "圖中的「方框」(狀態變數)"),
    (r"$+ b\,N_t$"     , "左邊的閥(birth 速率方程式),由參數 b 與狀態 N 控制"),
    (r"$- d\,N_t$"     , "右邊的閥(death 速率方程式),由參數 d 與狀態 N 控制"),
]
for i, (sym, desc) in enumerate(mapping):
    y = 2.4 - i * 0.5
    ax.text(eq_x + 0.0, y, sym, fontsize=12, color="#22543d")
    ax.text(eq_x + 1.2, y, desc, fontsize=10, color="#1a202c")

fig.suptitle("從 Forrester 圖讀出方程式:Density-Independent 模型(式 3.1)",
             fontsize=14, y=0.99)
plt.savefig(OUTDIR / "helper-3-eq3-1-mapping.png",
            dpi=160, bbox_inches="tight", facecolor="white")
plt.close()


# ----------------------------------------------------------------------------
# Helper 4: Diagram → Equation mapping (density-dependent, Eq 3.2)
# ----------------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(12, 6))
ax.set_xlim(0, 12)
ax.set_ylim(0, 6)
ax.axis("off")

# Diagram
draw_cloud(ax, 0.8, 3.5, scale=0.20)
draw_state_box(ax, 3.0, 3.2, w=1.2, h=0.7, label="N", units="#")
draw_cloud(ax, 6.0, 3.5, scale=0.20)
draw_material_arrow(ax, 1.4, 3.55, 2.9, 3.55, with_valve=True, label="birth")
draw_material_arrow(ax, 4.3, 3.55, 5.65, 3.55, with_valve=True, label="death")
draw_param(ax, 1.9, 4.8, "b")
draw_info_arrow(ax, 1.9, 4.65, 2.05, 3.75)
draw_param(ax, 5.0, 4.8, "d")
draw_info_arrow(ax, 5.0, 4.65, 4.95, 3.75)
# N → death rate (self-loop on death)
draw_info_arrow(ax, 3.85, 3.2, 4.85, 3.45)

# Reduction Factor R aux variable (the new piece)
draw_aux(ax, 2.0, 1.7, "R = 1 − N/K", w=1.2)
draw_param(ax, 1.0, 1.7, "K")
draw_info_arrow(ax, 1.2, 1.7, 1.5, 1.7)
draw_info_arrow(ax, 3.5, 3.2, 2.2, 1.95)   # N influences R
draw_info_arrow(ax, 2.0, 1.95, 2.05, 3.4)   # R influences birth rate

ax.text(3.6, 0.6, "圖 3.5 的 Forrester 圖", fontsize=11, ha="center",
        color="#2b6cb0", fontweight="bold")

# Equation
eq_x = 7.6
ax.text(eq_x, 5.4, "對應的差分方程式(式 3.2):", fontsize=12,
        color="#22543d", fontweight="bold")
ax.text(eq_x, 4.5,
        r"$N_{t+1} \;=\; N_t \;+\; b\,N_t \!\left(1 - \dfrac{N_t}{K}\right) \;-\; d\,N_t$",
        fontsize=12.5)
ax.text(eq_x + 1.95, 4.05, "↑ birth (受 R 縮減)", fontsize=8.5, color="#2b6cb0")
ax.text(eq_x + 3.55, 4.05, "↑ death", fontsize=8.5, color="#c53030")

ax.text(eq_x, 3.5, "和式 3.1 比,只多出一個 reduction factor:", fontsize=10,
        color="#22543d")
ax.text(eq_x + 0.0, 3.0, r"$R \;=\; 1 - \dfrac{N_t}{K}$",
        fontsize=13, color="#22543d")
ax.text(eq_x + 0.0, 2.2,
        "• 當 $N=0$:$R=1$,birth 全速進行 ↔ 跟式 3.1 一樣\n"
        "• 當 $N=K$:$R=0$,birth 完全停止 ↔ 人口不再增加\n"
        "• 中間線性過渡:擁擠越大,出生效率越低",
        fontsize=10, color="#1a202c", verticalalignment="top")

fig.suptitle("從 Forrester 圖讀出方程式:Density-Dependent 模型(式 3.2)\n"
             "加一個 R 就把指數模型變成 logistic 模型",
             fontsize=13.5, y=0.99)
plt.savefig(OUTDIR / "helper-4-eq3-2-mapping.png",
            dpi=160, bbox_inches="tight", facecolor="white")
plt.close()


print("Done. Wrote:")
for p in sorted(OUTDIR.glob("helper-*.png")):
    print(" ", p.name, f"({p.stat().st_size} bytes)")
