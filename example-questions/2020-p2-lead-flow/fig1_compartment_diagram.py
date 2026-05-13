"""Compartment diagram for the 3-compartment lead-flow model.

This is a hand-drawn schematic produced with matplotlib patches.  It
shows three boxes (blood, tissues, bones), the input I1, the four
outflow routes, and the six inter-compartment fluxes with their
rate-constant labels.  No simulation here — just the structural picture
that the simulation in fig2 follows.

Layout (roughly):

         I1 (input)
              │
              ▼
     ┌─────────────┐
     │ x3 bones    │  k31·x1 ───►
     │             │  ◄─── k13·x3       k01·x1
     └──────▲──────┘        ┌─────────┐  → urine
            │               │ x1 blood│  k21·x1
            └───────────────┤         ├──────────►  ┌──────────┐
                            └─────────┘             │ x2 tiss  │
                                  ▲    k12·x2       │          │
                                  └─────────────────┤          │
                                                    └────┬─────┘
                                                         │ k02·x2
                                                         ▼  hair/nails/sweat

Output: fig1_compartment_diagram.png next to this file.
"""
from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyArrowPatch
from matplotlib import font_manager

OUTDIR = Path(__file__).parent
plt.rcParams["axes.unicode_minus"] = False

cjk_candidates = ["Noto Sans CJK TC", "Noto Sans CJK SC", "Noto Sans CJK JP"]
available = {f.name for f in font_manager.fontManager.ttflist}
cjk_font = next((c for c in cjk_candidates if c in available), None)
if cjk_font:
    plt.rcParams["font.family"] = cjk_font


fig, ax = plt.subplots(figsize=(11, 6.5))
ax.set_xlim(0, 12)
ax.set_ylim(0, 8)
ax.axis("off")

# Boxes ----------------------------------------------------------------------
def draw_box(x, y, w, h, label_top, label_bottom, color):
    box = mpatches.FancyBboxPatch((x, y), w, h,
                                  boxstyle="round,pad=0.08,rounding_size=0.2",
                                  fc=color, ec="black", lw=2)
    ax.add_patch(box)
    ax.text(x + w / 2, y + h * 0.65, label_top, ha="center", va="center",
            fontsize=14, fontweight="bold")
    ax.text(x + w / 2, y + h * 0.30, label_bottom, ha="center", va="center",
            fontsize=12, style="italic")


# x3 bones (top-left)
draw_box(0.5, 5.3, 2.5, 1.6, r"$x_3$", "Bones", "#f5deb3")
# x1 blood (center)
draw_box(4.6, 3.4, 2.8, 1.8, r"$x_1$", "Blood", "#ffcccc")
# x2 tissues (right)
draw_box(8.6, 3.4, 2.8, 1.8, r"$x_2$", "Tissues", "#cce5ff")


# Arrow helper ---------------------------------------------------------------
def arrow(xy1, xy2, label, label_xy, color="black", style="-|>",
          lw=1.8, label_color=None):
    ar = FancyArrowPatch(xy1, xy2, arrowstyle=style, mutation_scale=18,
                         lw=lw, color=color)
    ax.add_patch(ar)
    ax.text(label_xy[0], label_xy[1], label, fontsize=11,
            color=label_color or color, ha="center", va="center",
            bbox=dict(boxstyle="round,pad=0.15", fc="white", ec="none",
                      alpha=0.85))


# I1 inflow (top, into blood)
ax.text(6.0, 7.4, r"$I_1 = 49.3\,\mu\mathrm{g/day}$", ha="center", va="center",
        fontsize=12, fontweight="bold",
        bbox=dict(boxstyle="round,pad=0.3", fc="#dfd", ec="green"))
arrow((6.0, 7.0), (6.0, 5.2), "", (0, 0), color="green", lw=2.2)

# Blood <-> Tissues  (two arrows)
arrow((7.4, 4.5), (8.6, 4.5), r"$k_{21}\,x_1$", (8.0, 4.85),
      color="#a44", lw=2.0)
arrow((8.6, 3.9), (7.4, 3.9), r"$k_{12}\,x_2$", (8.0, 3.55),
      color="#44a", lw=2.0)

# Blood -> Bones / Bones -> Blood
arrow((4.6, 4.8), (3.0, 5.8), r"$k_{31}\,x_1$", (3.6, 5.55),
      color="#a44", lw=2.0)
arrow((3.0, 6.2), (4.6, 4.4),
      r"$k_{13}\,x_3$" + "\n" + r"(極慢)",
      (3.6, 4.95), color="#44a", lw=2.0)

# Urinary outflow from blood
arrow((6.0, 3.4), (6.0, 1.6), r"$k_{01}\,x_1$" + "\n尿液", (6.0, 1.0),
      color="#c80", lw=2.0)

# Hair/nails/sweat outflow from tissues
arrow((10.0, 3.4), (10.0, 1.6), r"$k_{02}\,x_2$" + "\n毛髮/指甲/汗",
      (10.0, 1.0), color="#c80", lw=2.0)

# Title and rate table
fig.suptitle("鉛代謝三隔室模型", fontsize=15, fontweight="bold", y=0.97)

# Annotate the slow rate
ax.annotate("關鍵:$k_{13}=3.5\\times10^{-5}\\,\\mathrm{day}^{-1}$\n"
            "(半衰期 ≈ 54 年!)\n"
            "→ 骨骼像個鉛的「黑洞」",
            xy=(0.6, 4.3), fontsize=10, color="#444",
            bbox=dict(boxstyle="round,pad=0.4", fc="#fff7d0", ec="#aa7"))

fig.tight_layout()
fig.savefig(OUTDIR / "fig1_compartment_diagram.png", dpi=150,
            bbox_inches="tight")
print(f"Wrote {OUTDIR / 'fig1_compartment_diagram.png'}")
