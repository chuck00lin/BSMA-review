"""Helper figures for MAP.md — the two-layer (problems × tools) overview.

Helpers:
  1. Direction comparison — traditional textbook (math → application) vs
     problem-first (real problem → Q-classification → tools).
  2. Toolbox grouping — 12 underlying math tools organized in 3 families:
     A) structure (how to write the ODE), B) behavior (how to analyze
     it), C) data+compute (numerical integration + parameter fitting).
  3. Force-multiplier bar chart — number of Q's each tool serves;
     shows that a few tools (numerical integration, linearization,
     phase plane) carry most of the load.
  4. Q × Tool matrix — heatmap of which tools serve which problems,
     with the named real cases overlaid in the cells they exemplify.
     This IS the map.

All four are written into problem-first/figures/MAP/ at 150 dpi.
"""
from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch
from matplotlib import font_manager
import numpy as np

OUTDIR = Path(__file__).parent
plt.rcParams["axes.unicode_minus"] = False

cjk_candidates = ["Noto Sans CJK TC", "Noto Sans CJK SC", "Noto Sans CJK JP"]
available = {f.name for f in font_manager.fontManager.ttflist}
cjk_font = next((c for c in cjk_candidates if c in available), None)
if cjk_font:
    plt.rcParams["font.family"] = cjk_font


# ============================================================================
# Helper 1: Direction comparison (traditional vs problem-first)
# ============================================================================
fig, axes = plt.subplots(1, 2, figsize=(14, 7.5))


def draw_chain(ax, items, color, title, arrow_color):
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 12)
    ax.axis("off")
    ax.set_title(title, fontsize=14, fontweight="bold", pad=15)
    n = len(items)
    y_positions = np.linspace(11, 1, n)
    for i, (txt, y) in enumerate(zip(items, y_positions)):
        box = FancyBboxPatch((1.5, y - 0.55), 7, 1.1,
                             boxstyle="round,pad=0.1,rounding_size=0.2",
                             fc=color, ec="black", lw=1.5)
        ax.add_patch(box)
        ax.text(5, y, txt, ha="center", va="center", fontsize=11,
                fontweight="bold")
        if i < n - 1:
            ax.annotate("", xy=(5, y_positions[i + 1] + 0.65),
                        xytext=(5, y - 0.65),
                        arrowprops=dict(arrowstyle="->", color=arrow_color,
                                        lw=2.5))


# Traditional path
trad = [
    "微積分、線代",
    "ODE 理論",
    "動力系統 / phase plane",
    "PDE / 特殊函數",
    "  (滿屋子工具)  ",
    "「找個應用題練練吧」",
    "[X]  讀者結業:多認識方法,不太會建模",
]
draw_chain(axes[0], trad, "#dde", "傳統教科書(由下往上)", "#446")

# Problem-first path
pf = [
    "真實生物問題(COVID、藥動、生態…)",
    "「我**到底**要回答什麼?」",
    "歸類成 5 類問題之一(Q1–Q5)",
    "「這類問題該用什麼工具?」",
    "展開 2–3 個底層工具",
    "建模 → 分析 → 回答原問題",
    "[O]  讀者結業:能對任何問題說「Q? + T?」",
]
draw_chain(axes[1], pf, "#dfd", "本書(由上往下)", "#363")

fig.suptitle("方向反轉:傳統「方法→應用」 vs 本書「問題→方法」",
             fontsize=15, fontweight="bold", y=0.99)
fig.tight_layout()
fig.savefig(OUTDIR / "fig1_directions.png", dpi=150, bbox_inches="tight")
plt.close(fig)
print("Wrote fig1_directions.png")


# ============================================================================
# Helper 2: Toolbox grouping (12 tools in 3 families)
# ============================================================================
fig, ax = plt.subplots(figsize=(14, 8.5))
ax.set_xlim(0, 18)
ax.set_ylim(0, 11)
ax.axis("off")

groups = [
    {
        "title": "A. 結構工具\n(寫 ODE 用)",
        "color": "#ffe4d2",
        "x_left": 0.5,
        "x_right": 5.7,
        "tools": [
            ("T1", "per capita 速率", r"$\dot N = a\,N$"),
            ("T2", "質量作用律", r"$\dot N = a\,N\,M$"),
            ("T3", "logistic / 飽和", r"$\dot N = rN(1-N/K)$"),
            ("T4", "守恆律", r"$\sum \dot{x}_i = 0$"),
            ("T5", "多時間尺度", r"slow / fast 分離"),
        ],
    },
    {
        "title": "B. 行為工具\n(分析用)",
        "color": "#d4e9ff",
        "x_left": 6.2,
        "x_right": 11.4,
        "tools": [
            ("T6", "平衡點 + 線性化", r"$\dot \varepsilon = f'(x^\ast)\,\varepsilon$"),
            ("T7", "Jacobian / 特徵值", r"$\det(J - \lambda I) = 0$"),
            ("T8", "Phase plane / nullclines", r"2D 幾何"),
            ("T9", "Bifurcation", r"參數跨越臨界值"),
            ("T10", "敏感度分析", r"$\partial(\text{out})/\partial(\text{param})$"),
        ],
    },
    {
        "title": "C. 資料 + 計算工具",
        "color": "#dcf4d2",
        "x_left": 11.9,
        "x_right": 17.5,
        "tools": [
            ("T11", "數值積分", r"Euler / RK / solve_ivp"),
            ("T12", "參數擬合", r"LSQ / Levenberg-Marquardt"),
        ],
    },
]

for g in groups:
    # Group container
    height = 0.5 + 1.4 * len(g["tools"]) + 0.7
    cont = FancyBboxPatch((g["x_left"], 9.5 - height),
                          g["x_right"] - g["x_left"], height,
                          boxstyle="round,pad=0.15,rounding_size=0.4",
                          fc=g["color"], ec="black", lw=2.2)
    ax.add_patch(cont)
    ax.text((g["x_left"] + g["x_right"]) / 2, 9.5 - 0.45,
            g["title"], ha="center", va="top",
            fontsize=12, fontweight="bold")

    # Each tool
    for i, (tid, name, formula) in enumerate(g["tools"]):
        y = 9.5 - 1.2 - 1.4 * i
        ax.text(g["x_left"] + 0.3, y, tid, ha="left", va="center",
                fontsize=11, fontweight="bold", color="#333",
                bbox=dict(boxstyle="circle,pad=0.18", fc="white",
                          ec=g["color"].replace("4", "0").replace("d", "9"),
                          lw=1.5))
        ax.text(g["x_left"] + 1.2, y + 0.18, name, ha="left", va="center",
                fontsize=11)
        ax.text(g["x_left"] + 1.2, y - 0.32, formula, ha="left", va="center",
                fontsize=10, style="italic", color="#444")

ax.set_title("12 個底層工具 = 結構 + 行為 + 資料",
             fontsize=15, fontweight="bold", pad=10)

fig.tight_layout()
fig.savefig(OUTDIR / "fig2_toolbox.png", dpi=150, bbox_inches="tight")
plt.close(fig)
print("Wrote fig2_toolbox.png")


# ============================================================================
# Helper 3: Force-multiplier bar chart
# ============================================================================
tool_names = [
    "T11 數值積分",
    "T6 線性化",
    "T7 Jacobian/特徵值",
    "T8 Phase plane",
    "T3 logistic / 飽和",
    "T2 質量作用",
    "T9 Bifurcation",
    "T10 敏感度",
    "T1 per capita",
    "T4 守恆",
    "T5 多時間尺度",
    "T12 擬合",
]
qs_served = [5, 4, 4, 4, 3, 2, 2, 2, 2, 1, 1, 1]

# Color by ROI tier
def color_for(n):
    if n >= 5:
        return "#d4af37"   # gold
    if n == 4:
        return "#c0c0c0"   # silver
    if n == 3:
        return "#cd7f32"   # bronze
    return "#7c9bbf"


colors = [color_for(n) for n in qs_served]

fig, ax = plt.subplots(figsize=(11, 7))
y_pos = np.arange(len(tool_names))[::-1]   # so largest at top
bars = ax.barh(y_pos, qs_served, color=colors, edgecolor="black", lw=1.0)

for bar, n in zip(bars, qs_served):
    ax.text(bar.get_width() + 0.1, bar.get_y() + bar.get_height() / 2,
            f"{n} / 5 個 Q",
            va="center", fontsize=11)

ax.set_yticks(y_pos)
ax.set_yticklabels(tool_names, fontsize=11)
ax.set_xticks([0, 1, 2, 3, 4, 5])
ax.set_xlabel("該工具服務的 Q 數量")
ax.set_xlim(0, 6)
ax.set_title("Force multipliers:服務最多 Q 的工具",
             fontsize=14, fontweight="bold", pad=12)

# Legend tier
legend_handles = [
    mpatches.Patch(color="#d4af37", label="[1st] 5/5 — 必學的第一順位"),
    mpatches.Patch(color="#c0c0c0", label="[2nd] 4/5 — 學完一次解三類問題"),
    mpatches.Patch(color="#cd7f32", label="[3rd] 3/5 — 跨多個 Q"),
    mpatches.Patch(color="#7c9bbf", label="場景特定 — 1–2 個 Q"),
]
ax.legend(handles=legend_handles, loc="lower right", fontsize=9.5)
ax.grid(True, alpha=0.3, axis="x")

fig.tight_layout()
fig.savefig(OUTDIR / "fig3_force_multipliers.png", dpi=150,
            bbox_inches="tight")
plt.close(fig)
print("Wrote fig3_force_multipliers.png")


# ============================================================================
# Helper 4: Q × Tool matrix (the map itself), with named cases overlaid
# ============================================================================
tools_short = ["T1", "T2", "T3", "T4", "T5",
               "T6", "T7", "T8", "T9", "T10", "T11", "T12"]
tools_full = [
    "per capita", "mass action", "logistic", "守恆", "多時間尺度",
    "線性化", "Jacobian", "phase plane", "bifurcation", "敏感度",
    "數值積分", "擬合"
]

# Matrix: rows = Q, cols = tools
# values: 0=none, 1=used, 2=core
M = np.array([
    # T1 T2 T3 T4 T5 T6 T7 T8 T9 T10 T11 T12
    [0, 1, 1, 0, 0, 2, 2, 1, 1, 0, 1, 0],   # Q1
    [1, 1, 1, 1, 0, 0, 1, 2, 0, 0, 1, 0],   # Q2
    [1, 0, 0, 0, 2, 1, 1, 1, 0, 0, 1, 0],   # Q3
    [0, 0, 1, 0, 0, 1, 1, 1, 2, 2, 1, 1],   # Q4
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 2],   # Q5
])

q_labels = ["Q1\n穩定/失控", "Q2\n長期", "Q3\n時間尺度",
            "Q4\n敏感度", "Q5\n反推"]

# Cases anchored on a (Q, tool) cell — drawn as small text overlays
case_anchors = [
    (r"SIR ($R_0$)",     0, 6),   # Q1 × T7 (Jacobian)
    ("Allee bistab.",    0, 5),   # Q1 × T6
    ("Chemostat",        0, 5),   # Q1 × T6  (same cell as Allee — combine)
    ("Lead 3-cmpt",      1, 7),   # Q2 × T8
    ("Drug PK steady",   1, 0),   # Q2 × T1
    ("Hormone adapt.",   2, 4),   # Q3 × T5
    ("Drug PK transient",2, 0),   # Q3 × T1
    ("Spruce budworm",   3, 8),   # Q4 × T9
    ("Fishery MSY",      3, 8),   # Q4 × T9
    ("Algae fit",        4, 11),  # Q5 × T12
    ("Height growth",    4, 11),  # Q5 × T12
    ("HIV params",       4, 11),  # Q5 × T12
]

fig, ax = plt.subplots(figsize=(14, 6.5))

# Heatmap base
im = ax.imshow(M, cmap="Greens", vmin=0, vmax=2.5, aspect="auto")

ax.set_xticks(range(len(tools_short)))
ax.set_xticklabels([f"{s}\n{f}" for s, f in zip(tools_short, tools_full)],
                   fontsize=10)
ax.set_yticks(range(5))
ax.set_yticklabels(q_labels, fontsize=11, fontweight="bold")

# Cell symbols for "used" (★) and "core" (★★)
for i in range(M.shape[0]):
    for j in range(M.shape[1]):
        v = M[i, j]
        if v == 1:
            ax.text(j, i, "★", ha="center", va="center", fontsize=14,
                    color="#444")
        elif v == 2:
            ax.text(j, i, "★★", ha="center", va="center", fontsize=12,
                    color="white", fontweight="bold")

# Group case names by (i, j)
case_groups = {}
for name, i, j in case_anchors:
    case_groups.setdefault((i, j), []).append(name)

for (i, j), names in case_groups.items():
    txt = " · ".join(names)
    # Annotate below cell with small italic case name
    ax.annotate(txt, xy=(j, i + 0.32), ha="center", va="top",
                fontsize=7.5, color="#a44", style="italic")

ax.set_title("Q × Tool 矩陣:每個 Q 用到哪些工具(★ 用到,★★ 核心) "
             "+ 紅字 = 真實 case",
             fontsize=13, fontweight="bold", pad=12)
ax.set_xlabel("12 個底層工具")
ax.set_ylabel("5 類問題")

fig.tight_layout()
fig.savefig(OUTDIR / "fig4_real_problems.png", dpi=150, bbox_inches="tight")
plt.close(fig)
print("Wrote fig4_real_problems.png")

