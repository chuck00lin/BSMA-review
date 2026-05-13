"""Generate fresh helper illustrations for Lecture 01 of the BSMA redesign.

These complement (don't replace) the original PDF figures. Designed for clarity
at the kid-accessible-but-not-childish level — labelled axes, equilibrium point
explicitly marked, no clutter.

Run from within the bsma-pdf conda env so matplotlib + a CJK-capable font are
available.
"""
from pathlib import Path

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib import font_manager
import numpy as np

OUTDIR = Path(__file__).parent
plt.rcParams["axes.unicode_minus"] = False

# Find a CJK font for Chinese labels.
cjk_candidates = [
    "Noto Sans CJK TC",
    "Noto Sans CJK SC",
    "Noto Sans CJK JP",
    "WenQuanYi Zen Hei",
    "AR PL UMing CN",
    "Source Han Sans",
]
available = {f.name for f in font_manager.fontManager.ttflist}
cjk_font = next((c for c in cjk_candidates if c in available), None)
if cjk_font:
    plt.rcParams["font.family"] = cjk_font
    print(f"Using CJK font: {cjk_font}")
else:
    print("⚠️  No CJK font found — Chinese labels will show as boxes.")
    print("   Install one with:  sudo apt install fonts-noto-cjk")


# ----------------------------------------------------------------------------
# Helper 1: System / Model relationship + the four basic concepts
# ----------------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(10, 5.2))
ax.set_xlim(0, 10)
ax.set_ylim(0, 5.2)
ax.axis("off")

# System box (left)
sys_box = mpatches.FancyBboxPatch(
    (0.4, 1.0), 3.6, 3.2, boxstyle="round,pad=0.1",
    linewidth=2, edgecolor="#2c5282", facecolor="#ebf4ff",
)
ax.add_patch(sys_box)
ax.text(2.2, 3.85, "系統 (System)", fontsize=16, fontweight="bold",
        ha="center", color="#2c5282")
ax.text(2.2, 3.3, "真實世界中複雜的整體", fontsize=11, ha="center", color="#2c5282")
# Object icons inside system
for cx, cy, label in [(1.2, 2.4, "物件 A"), (2.6, 2.4, "物件 B"),
                       (1.5, 1.5, "物件 C"), (2.8, 1.6, "物件 D")]:
    obj = mpatches.Circle((cx, cy), 0.32, facecolor="#90cdf4",
                          edgecolor="#2c5282", linewidth=1.2)
    ax.add_patch(obj)
    ax.text(cx, cy, label, fontsize=8, ha="center", va="center", color="#1a365d")
# Lines between objects (relations)
for (x1, y1), (x2, y2) in [((1.2, 2.4), (2.6, 2.4)), ((2.6, 2.4), (2.8, 1.6)),
                             ((1.5, 1.5), (2.8, 1.6)), ((1.2, 2.4), (1.5, 1.5))]:
    ax.plot([x1, x2], [y1, y2], "-", color="#4a5568", linewidth=0.8, alpha=0.6)

# Arrow: 描述、簡化
ax.annotate("", xy=(6.2, 2.6), xytext=(4.2, 2.6),
            arrowprops=dict(arrowstyle="->", linewidth=2.5, color="#2d3748"))
ax.text(5.2, 3.1, "描述、簡化", fontsize=12, ha="center", color="#2d3748",
        fontweight="bold")
ax.text(5.2, 2.15, "(只保留我們關心的)", fontsize=9, ha="center", color="#718096")

# Model box (right)
mdl_box = mpatches.FancyBboxPatch(
    (6.3, 1.0), 3.5, 3.2, boxstyle="round,pad=0.1",
    linewidth=2, edgecolor="#9b2c2c", facecolor="#fff5f5",
)
ax.add_patch(mdl_box)
ax.text(8.05, 3.85, "模型 (Model)", fontsize=16, fontweight="bold",
        ha="center", color="#9b2c2c")
ax.text(8.05, 3.3, "對系統的描述", fontsize=11, ha="center", color="#9b2c2c")
# Stylised representations of the model (formula, diagram, words)
ax.text(8.05, 2.5, r"$R_{t+1} = R_t + I_t - E_t$",
        fontsize=12, ha="center", color="#9b2c2c")
ax.text(8.05, 1.95, "「青蛙吃蜻蜓」", fontsize=10, ha="center", color="#9b2c2c")
ax.text(8.05, 1.5, "(描述,可以是文字、圖、公式)",
        fontsize=8, ha="center", color="#a0aec0", style="italic")

# Caption
ax.text(5.0, 0.45, "系統與模型的關係:模型只是描述,不是系統本身。",
        fontsize=10, ha="center", color="#4a5568", style="italic")
ax.text(5.0, 0.1, "同一個系統可以有「許多」模型,每個模型看到的角度不同。",
        fontsize=10, ha="center", color="#4a5568", style="italic")

plt.savefig(OUTDIR / "helper-1-system-vs-model.png",
            dpi=160, bbox_inches="tight", facecolor="white")
plt.close()


# ----------------------------------------------------------------------------
# Helper 2: I and E vs R — clean redraw with equilibrium and 4 stages marked
# ----------------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(9, 6))

P = 100.0
Ix = 8.0
Ex = 4.0
R = np.linspace(0, P, 200)
I = Ix - (Ix / P) * R
E = (Ex / P) * R

ax.plot(R, I, color="#2b6cb0", linewidth=2.5, label=r"遷入率 $I = I_x - (I_x/P)\,R$")
ax.plot(R, E, color="#c53030", linewidth=2.5, label=r"滅絕率 $E = (E_x/P)\,R$")

# Equilibrium point
R_eq = Ix * P / (Ix + Ex)
y_eq = (Ex / P) * R_eq
ax.plot(R_eq, y_eq, "o", color="black", markersize=11, zorder=5)
ax.axvline(R_eq, color="gray", linestyle=":", linewidth=1, alpha=0.7)
ax.annotate(rf"平衡點 $\hat R = \dfrac{{I_x\,P}}{{I_x+E_x}}$",
            xy=(R_eq, y_eq), xytext=(R_eq + 8, y_eq + 1.5),
            fontsize=12, ha="left", color="black",
            arrowprops=dict(arrowstyle="->", color="black", linewidth=1.2))

# Endpoints
ax.plot(0, Ix, "s", color="#2b6cb0", markersize=8)
ax.text(-3, Ix, r"$I_x$", fontsize=14, ha="right", va="center", color="#2b6cb0")
ax.plot(P, Ex, "s", color="#c53030", markersize=8)
ax.text(P + 2, Ex, r"$E_x$", fontsize=14, ha="left", va="center", color="#c53030")

# Stage shading
ax.axvspan(0, R_eq, alpha=0.06, color="#48bb78")
ax.axvspan(R_eq, P, alpha=0.06, color="#ed8936")
ax.text(R_eq / 2, 8.5, "$I > E$:物種數會「增加」", fontsize=11,
        ha="center", color="#22543d")
ax.text((R_eq + P) / 2, 8.5, "$I < E$:物種數會「減少」", fontsize=11,
        ha="center", color="#7b341e")

ax.set_xlabel("島上物種數 $R$", fontsize=13)
ax.set_ylabel("速率(每單位時間多少種)", fontsize=13)
ax.set_xlim(0, P)
ax.set_ylim(0, 9.5)
ax.set_title("遷入與滅絕的拉鋸:平衡點在哪裡?", fontsize=14, pad=14)
ax.legend(loc="lower right", fontsize=11)
ax.grid(alpha=0.25, linestyle="--")

plt.tight_layout()
plt.savefig(OUTDIR / "helper-2-immigration-extinction-balance.png",
            dpi=160, bbox_inches="tight", facecolor="white")
plt.close()


# ----------------------------------------------------------------------------
# Helper 3: Realism / Precision / Generality trade-off triangle
# ----------------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(8, 7.5))
ax.set_xlim(-1, 9)
ax.set_ylim(-1.5, 8.5)
ax.axis("off")

# Triangle vertices
A = (4, 7)        # Realism (top)
B = (0.5, 1)      # Precision (bottom-left)
C = (7.5, 1)      # Generality (bottom-right)

triangle = mpatches.Polygon([A, B, C], closed=True,
                            facecolor="#fefcbf", edgecolor="#744210",
                            linewidth=2.5)
ax.add_patch(triangle)

# Vertex labels
ax.plot(*A, "o", color="#744210", markersize=14, zorder=5)
ax.text(A[0], A[1] + 0.6, "真實性\n(Realism)", fontsize=14, fontweight="bold",
        ha="center", color="#744210")
ax.text(A[0], A[1] - 0.5, "結構像不像真的", fontsize=10,
        ha="center", color="#744210", style="italic")

ax.plot(*B, "o", color="#744210", markersize=14, zorder=5)
ax.text(B[0] - 0.4, B[1] - 0.5, "精確性\n(Precision)", fontsize=14, fontweight="bold",
        ha="center", color="#744210")
ax.text(B[0] - 0.4, B[1] - 1.3, "輸出值準不準", fontsize=10,
        ha="center", color="#744210", style="italic")

ax.plot(*C, "o", color="#744210", markersize=14, zorder=5)
ax.text(C[0] + 0.4, C[1] - 0.5, "普遍性\n(Generality)", fontsize=14, fontweight="bold",
        ha="center", color="#744210")
ax.text(C[0] + 0.4, C[1] - 1.3, "可以套用幾個系統", fontsize=10,
        ha="center", color="#744210", style="italic")

# Example points (you can pick any two, not all three)
example_points = [
    ((3.9, 5.0), "縮小飛機模型\n(真實 + 精確)", "#2b6cb0"),
    ((5.6, 4.0), "全球氣候模型\n(真實 + 普遍)", "#2b6cb0"),
    ((4.0, 1.6), "線性回歸 $y=mx+b$\n(精確 + 普遍)", "#2b6cb0"),
]
for (x, y), label, color in example_points:
    ax.plot(x, y, "*", color=color, markersize=18, zorder=4)
    ax.text(x, y - 0.5, label, fontsize=9, ha="center", color=color,
            fontweight="bold")

# Central caption
ax.text(4, -0.7, "好模型最多只能「靠近兩個角」——\n不可能同時三項都最強。",
        fontsize=11.5, ha="center", color="#744210",
        bbox=dict(facecolor="#fffaf0", edgecolor="#744210",
                  boxstyle="round,pad=0.4"))

ax.set_title("模型的三方取捨", fontsize=15, pad=18, color="#744210")

plt.savefig(OUTDIR / "helper-3-realism-precision-generality.png",
            dpi=160, bbox_inches="tight", facecolor="white")
plt.close()


print("Done. Wrote:")
for p in sorted(OUTDIR.glob("helper-*.png")):
    print(" ", p.name, f"({p.stat().st_size} bytes)")
