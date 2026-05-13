"""Helper illustrations for Lecture 06 — Numerical Techniques.

Helpers:
  1. Slope field + Euler walking: shows the slope field, the true solution,
     and the broken-line Euler trajectory walking step-by-step.
  2. Euler vs RK-2 vs RK-4 on dy/dt = 0.5 y: at Δt = 1.0, true vs numerical,
     plus the error magnitude chart.
  3. Stiff equation breakdown: Euler with big Δt explodes; small Δt works.
  4. Method of Lines: 1D space discretized into nodes, each node a stack of
     two boxes (p, b) — visualizing PDE → ODE system.
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
# Helper 1: Slope field + Euler walking
# ----------------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(11, 7))

# ODE: dy/dt = 0.3 y  (exponential growth, easy to visualize)
a = 0.3

# Slope field
t_grid = np.linspace(0, 6, 14)
y_grid = np.linspace(0, 12, 12)
T_g, Y_g = np.meshgrid(t_grid, y_grid)
dT = np.ones_like(T_g)
dY = a * Y_g
# normalise arrows
mag = np.hypot(dT, dY)
dT /= mag
dY /= mag
ax.quiver(T_g, Y_g, dT, dY, color="#9ca3af", alpha=0.7, scale=30, width=0.0035)

# True solution
t_true = np.linspace(0, 6, 200)
y0 = 2.0
y_true = y0 * np.exp(a * t_true)
ax.plot(t_true, y_true, color="#22543d", linewidth=2.5,
        label=f"真實解 $y = y_0 e^{{at}}$")

# Euler steps Δt = 1.0
dt = 1.0
ts = [0]
ys = [y0]
while ts[-1] < 6:
    y_new = ys[-1] + dt * a * ys[-1]
    ts.append(ts[-1] + dt)
    ys.append(y_new)
ax.plot(ts, ys, "o-", color="#c53030", linewidth=2.2, markersize=9,
        label=f"Euler 法 (Δt = {dt})")

# Annotate the Euler step at t=0 → t=1
for i in range(len(ts) - 1):
    t0, y0_pt = ts[i], ys[i]
    slope = a * y0_pt
    # short tangent line
    arrow_len = 0.95
    ax.annotate("", xy=(t0 + arrow_len, y0_pt + slope * arrow_len),
                xytext=(t0, y0_pt),
                arrowprops=dict(arrowstyle="->", color="#c53030",
                                linewidth=1.5, alpha=0.5))

# Annotate first step explicitly
ax.annotate(
    "在 $t_0$ 取斜率 $f(y_0) = a y_0$,\n"
    "走 Δt 步:$y_1 = y_0 + a y_0 \\cdot \\Delta t$",
    xy=(0.5, 2.5), xytext=(0.4, 5.8),
    fontsize=10, color="#c53030",
    arrowprops=dict(arrowstyle="->", color="#c53030", linewidth=1))

# Annotate the error growing
ax.annotate(
    "誤差累積:每步少看了「之後的曲率」",
    xy=(5.0, 7.0), xytext=(2.5, 10.5),
    fontsize=11, color="#c53030", fontweight="bold",
    arrowprops=dict(arrowstyle="->", color="#c53030", linewidth=1.3))

ax.set_xlabel("時間 $t$", fontsize=12)
ax.set_ylabel("$y$", fontsize=12)
ax.set_xlim(0, 6)
ax.set_ylim(0, 13)
ax.set_title("斜率場(灰箭頭)+ Euler 法(紅折線)在每一步「跟斜率走」",
             fontsize=14, pad=10)
ax.grid(alpha=0.25, linestyle="--")
ax.legend(loc="upper left", fontsize=11)

plt.tight_layout()
plt.savefig(OUTDIR / "helper-1-slope-field-euler.png",
            dpi=160, bbox_inches="tight", facecolor="white")
plt.close()


# ----------------------------------------------------------------------------
# Helper 2: Euler vs RK-2 vs RK-4 accuracy
# ----------------------------------------------------------------------------
fig, axes = plt.subplots(1, 2, figsize=(14, 5.5))

# ODE: dy/dt = 0.5 y, y0 = 10, t from 0 to 4
def f(t, y): return 0.5 * y
y0 = 10.0
t_end = 4.0
dt = 1.0
t_steps = np.arange(0, t_end + dt/2, dt)
n = len(t_steps)

# True solution
t_true = np.linspace(0, t_end, 300)
y_true = y0 * np.exp(0.5 * t_true)

# Euler
y_euler = [y0]
for i in range(n - 1):
    y_euler.append(y_euler[-1] + dt * f(t_steps[i], y_euler[-1]))

# RK-2 (midpoint)
y_rk2 = [y0]
for i in range(n - 1):
    y = y_rk2[-1]; t = t_steps[i]
    k1 = f(t, y) * dt
    k2 = f(t + dt/2, y + k1/2) * dt
    y_rk2.append(y + k2)

# RK-4
y_rk4 = [y0]
for i in range(n - 1):
    y = y_rk4[-1]; t = t_steps[i]
    k1 = f(t, y) * dt
    k2 = f(t + dt/2, y + k1/2) * dt
    k3 = f(t + dt/2, y + k2/2) * dt
    k4 = f(t + dt, y + k3) * dt
    y_rk4.append(y + (k1 + 2*k2 + 2*k3 + k4) / 6)

# Panel (a): trajectories
ax = axes[0]
ax.plot(t_true, y_true, color="#22543d", linewidth=2.5, label="真實解")
ax.plot(t_steps, y_euler, "o-", color="#c53030", linewidth=2, markersize=9,
        label="Euler  (Δt=1)")
ax.plot(t_steps, y_rk2, "s-", color="#dd6b20", linewidth=2, markersize=9,
        label="RK-2  (Δt=1)")
ax.plot(t_steps, y_rk4, "^-", color="#2b6cb0", linewidth=2, markersize=9,
        label="RK-4  (Δt=1)")

ax.set_xlabel("時間 $t$", fontsize=12)
ax.set_ylabel("$y$", fontsize=12)
ax.set_title("$\\dfrac{dy}{dt} = 0.5 y$,$y_0=10$,Δt=1 下三種方法的軌跡",
             fontsize=13, pad=8)
ax.legend(loc="upper left", fontsize=10.5)
ax.grid(alpha=0.25, linestyle="--")

# Panel (b): final error bar chart (at t=4)
ax = axes[1]
t_check = 4.0
y_exact = y0 * np.exp(0.5 * t_check)

methods = ["Euler\nΔt=1.0", "Euler\nΔt=0.5", "Euler\nΔt=0.25",
           "RK-2\nΔt=1.0", "RK-4\nΔt=1.0"]
errors = []

# Euler Δt=1
y = y0
for _ in range(int(t_check / 1.0)):
    y = y + 1.0 * f(0, y)
errors.append(abs(y - y_exact))

# Euler Δt=0.5
y = y0
for _ in range(int(t_check / 0.5)):
    y = y + 0.5 * f(0, y)
errors.append(abs(y - y_exact))

# Euler Δt=0.25
y = y0
for _ in range(int(t_check / 0.25)):
    y = y + 0.25 * f(0, y)
errors.append(abs(y - y_exact))

# RK-2 Δt=1
y = y0
for _ in range(int(t_check / 1.0)):
    t = 0; dt_ = 1.0
    k1 = f(t, y) * dt_
    k2 = f(t + dt_/2, y + k1/2) * dt_
    y = y + k2
errors.append(abs(y - y_exact))

# RK-4 Δt=1
y = y0
for _ in range(int(t_check / 1.0)):
    t = 0; dt_ = 1.0
    k1 = f(t, y) * dt_
    k2 = f(t + dt_/2, y + k1/2) * dt_
    k3 = f(t + dt_/2, y + k2/2) * dt_
    k4 = f(t + dt_, y + k3) * dt_
    y = y + (k1 + 2*k2 + 2*k3 + k4) / 6
errors.append(abs(y - y_exact))

colors = ["#c53030", "#dd6b20", "#ed8936", "#d69e2e", "#2b6cb0"]
bars = ax.bar(methods, errors, color=colors, edgecolor="black", linewidth=0.6)
for b, e in zip(bars, errors):
    ax.text(b.get_x() + b.get_width()/2, b.get_height() + 0.1,
            f"{e:.3f}", ha="center", fontsize=10)
ax.set_ylabel(f"$t = {t_check}$ 時的絕對誤差", fontsize=12)
ax.set_yscale("log")
ax.set_title(f"絕對誤差 (對數軸):真實值 $y(4) = {y_exact:.3f}$",
             fontsize=13, pad=8)
ax.grid(alpha=0.3, axis="y", linestyle="--", which="both")
ax.set_axisbelow(True)

fig.suptitle("Euler 用一半步長,還是輸給 RK-4 用整步長",
             fontsize=14, y=1.02, fontweight="bold")
plt.tight_layout()
plt.savefig(OUTDIR / "helper-2-euler-vs-rk-accuracy.png",
            dpi=160, bbox_inches="tight", facecolor="white")
plt.close()


# ----------------------------------------------------------------------------
# Helper 3: Stiff equation — Euler explodes with big Δt, works with small Δt
# ----------------------------------------------------------------------------
fig, axes = plt.subplots(1, 2, figsize=(13, 5.5))

# Simple stiff-ish system: dy/dt = -k y,  k = 50 (very fast decay)
# True solution: y = y0 * exp(-k t)
k = 50.0
y0_s = 1.0
t_end_s = 0.5

t_true_s = np.linspace(0, t_end_s, 400)
y_true_s = y0_s * np.exp(-k * t_true_s)

# (a) Big Δt = 0.05 → Euler:  y_{n+1} = y_n (1 - k Δt) = y_n (1 - 2.5)
ax = axes[0]
dt_big = 0.05
t_b = np.arange(0, t_end_s + dt_big/2, dt_big)
y_b = [y0_s]
for _ in range(len(t_b) - 1):
    y_b.append(y_b[-1] + dt_big * (-k) * y_b[-1])
ax.plot(t_true_s, y_true_s, color="#22543d", linewidth=2.5,
        label="真實解 $y = e^{-50t}$")
ax.plot(t_b, y_b, "o-", color="#c53030", linewidth=2, markersize=8,
        label=f"Euler  Δt={dt_big} (= 2/k)")
ax.axhline(0, color="black", linewidth=0.7)
ax.set_xlabel("時間 $t$", fontsize=12)
ax.set_ylabel("$y$", fontsize=12)
ax.set_xlim(0, t_end_s)
ax.set_ylim(-3, 3)
ax.set_title("Δt 太大 → Euler **爆炸**(數值不穩定)", fontsize=12, pad=6)
ax.legend(loc="upper right", fontsize=10)
ax.grid(alpha=0.25, linestyle="--")

# (b) Small Δt = 0.005 → Euler:  works fine
ax = axes[1]
dt_small = 0.005
t_s = np.arange(0, t_end_s + dt_small/2, dt_small)
y_s = [y0_s]
for _ in range(len(t_s) - 1):
    y_s.append(y_s[-1] + dt_small * (-k) * y_s[-1])
ax.plot(t_true_s, y_true_s, color="#22543d", linewidth=2.5,
        label="真實解")
ax.plot(t_s[::5], y_s[::5], "o-", color="#2b6cb0", linewidth=1.5,
        markersize=4,
        label=f"Euler  Δt={dt_small}")
ax.axhline(0, color="black", linewidth=0.7)
ax.set_xlabel("時間 $t$", fontsize=12)
ax.set_ylabel("$y$", fontsize=12)
ax.set_xlim(0, t_end_s)
ax.set_ylim(-0.1, 1.1)
ax.set_title("Δt 夠小 → Euler 沒問題,但 **要算 100 倍多步**",
             fontsize=12, pad=6)
ax.legend(loc="upper right", fontsize=10)
ax.grid(alpha=0.25, linestyle="--")

fig.suptitle(
    "stiff(僵硬)方程式:快速衰減 $\\dot y = -50 y$,Δt 必須遠小於 $1/k$",
    fontsize=14, y=1.02, fontweight="bold")
plt.tight_layout()
plt.savefig(OUTDIR / "helper-3-stiff-equation-breakdown.png",
            dpi=160, bbox_inches="tight", facecolor="white")
plt.close()


# ----------------------------------------------------------------------------
# Helper 4: Method of Lines — PDE → ODE system
# ----------------------------------------------------------------------------
fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# Left panel: spatial discretization
ax = axes[0]
ax.set_xlim(-0.5, 10.5)
ax.set_ylim(-0.5, 5)
ax.axis("off")

# Show the continuous PDE on top
ax.text(5, 4.5,
        r"$\dfrac{\partial p}{\partial t} = -U \dfrac{\partial p}{\partial x} + D \dfrac{\partial^2 p}{\partial x^2}$",
        fontsize=14, ha="center", color="#2b6cb0")
ax.text(5, 4.0, "(連續的 PDE,空間 $x$ 是連續的)",
        fontsize=10, ha="center", color="#4a5568", style="italic")

# Continuous curve representing p(x, t=固定)
xs = np.linspace(0.5, 9.5, 200)
ys = 2.5 + 0.6 * np.sin(0.7 * xs) * np.exp(-0.06 * (xs - 5)**2)
ax.plot(xs, ys, color="#22543d", linewidth=2)
ax.text(0.5, 3.4, "$p(x, t)$", fontsize=11, color="#22543d")

# Discrete nodes
n_nodes = 9
node_xs = np.linspace(1.0, 9.0, n_nodes)
node_ys = 2.5 + 0.6 * np.sin(0.7 * node_xs) * np.exp(-0.06 * (node_xs - 5)**2)
for nx, ny in zip(node_xs, node_ys):
    ax.plot([nx, nx], [0.3, ny], "--", color="#9ca3af", linewidth=0.8)
    ax.plot(nx, ny, "o", color="#c53030", markersize=11, zorder=5)
    ax.plot(nx, 0.3, "v", color="black", markersize=8, zorder=5)
ax.axhline(0.3, color="black", linewidth=0.8)
for nx, label in zip(node_xs, ["$i-3$", "$i-2$", "$i-1$", "$i$", "", "", "", "", ""]):
    pass
# Label a few nodes
labels = ["$x_1$", "$x_2$", "$x_3$", "$x_4$", "$x_i$",
          "$x_{i+1}$", "$x_{N-2}$", "$x_{N-1}$", "$x_N$"]
for nx, label in zip(node_xs[:5], labels[:5]):
    ax.text(nx, 0.05, label, fontsize=9, ha="center")
for nx, label in zip(node_xs[-3:], labels[-3:]):
    ax.text(nx, 0.05, label, fontsize=9, ha="center")

ax.set_title("(a) 空間離散化:把連續的 $x$ 切成 N 個格點",
             fontsize=12, pad=4, color="#2b6cb0")

# Right panel: each node becomes an ODE
ax = axes[1]
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.axis("off")

ax.text(5, 9.5,
        "每一個格點 $i$,變成一條 ODE:",
        fontsize=13, ha="center", color="#22543d", fontweight="bold")

ax.text(5, 8.0,
        r"$\dfrac{dp_i}{dt} = -U \dfrac{p_{i+1} - p_{i-1}}{2\Delta x}"
        r" + D \dfrac{p_{i+1} - 2 p_i + p_{i-1}}{(\Delta x)^2}$",
        fontsize=13.5, ha="center")

ax.text(5, 7.0, "(連續的偏導數 → 用差分近似)",
        fontsize=10, ha="center", color="#4a5568", style="italic")

# Show stack of ODEs
y_starts = np.linspace(5.5, 1.0, 6)
labels_eq = [r"$\dot p_1 = -U \dfrac{p_2 - p_0}{2\Delta x} + D \dfrac{p_2 - 2p_1 + p_0}{\Delta x^2}$",
             r"$\dot p_2 = -U \dfrac{p_3 - p_1}{2\Delta x} + D \dfrac{p_3 - 2p_2 + p_1}{\Delta x^2}$",
             r"$\vdots$",
             r"$\dot p_i = -U \dfrac{p_{i+1} - p_{i-1}}{2\Delta x} + D \dfrac{p_{i+1} - 2p_i + p_{i-1}}{\Delta x^2}$",
             r"$\vdots$",
             r"$\dot p_N = $ (邊界條件決定)"]

for y, lbl in zip(y_starts, labels_eq):
    ax.text(0.5, y, lbl, fontsize=10.5, va="center")

ax.text(5, -0.4,
        "**結論**:1 條 PDE → $N$ 條互相耦合的 ODE → 用 RK-4 一起解",
        fontsize=11, ha="center", color="#c53030", fontweight="bold")

ax.set_title("(b) 每一條空間「線」上的 ODE,沿時間軸求解",
             fontsize=12, pad=4, color="#2b6cb0")

fig.suptitle("Method of Lines:把 PDE 變成 N 個耦合 ODE",
             fontsize=14, y=1.01, fontweight="bold")
plt.tight_layout()
plt.savefig(OUTDIR / "helper-4-method-of-lines.png",
            dpi=160, bbox_inches="tight", facecolor="white")
plt.close()


print("Done. Wrote:")
for p in sorted(OUTDIR.glob("helper-*.png")):
    print(" ", p.name, f"({p.stat().st_size} bytes)")
