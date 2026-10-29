
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

V = 23


def box(ax, lim=(-3, 3)):
    """Однакові межі та підписи осей."""
    ax.set_xlim(lim)
    ax.set_ylim(lim)
    ax.set_zlim(lim)
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")


# ---------- Завдання 1: шість фігур ----------
fig = plt.figure(figsize=(9, 8))
ax = fig.add_subplot(projection="3d")

# півсфера
u, v = np.meshgrid(np.linspace(0, 2 * np.pi, 40), np.linspace(0, np.pi / 2, 20))
ax.plot_surface(
    np.cos(u) * np.sin(v),
    np.sin(u) * np.sin(v),
    np.cos(v),
    color="tab:blue",
    alpha=0.8,
)

# тривимірна стрілка
ax.quiver(2, 0, 0, 0, 0, 2, color="red", arrow_length_ratio=0.25, linewidth=3)

# піраміда
pyramid = [
    [(-3, -3, 0), (-1, -3, 0), (-1, -1, 0), (-3, -1, 0)],
    [(-3, -3, 0), (-1, -3, 0), (-2, -2, 2)],
    [(-1, -3, 0), (-1, -1, 0), (-2, -2, 2)],
    [(-1, -1, 0), (-3, -1, 0), (-2, -2, 2)],
    [(-3, -1, 0), (-3, -3, 0), (-2, -2, 2)],
]
ax.add_collection3d(Poly3DCollection(pyramid, facecolors="gold", edgecolor="k", alpha=0.9))

# еліпс (еліпсоїд)
a, b, c = 1.2, 0.6, 1
u, v = np.meshgrid(np.linspace(0, 2 * np.pi, 40), np.linspace(0, np.pi, 20))
ax.plot_surface(
    -2 + a * np.cos(u) * np.sin(v),
    2.2 + b * np.sin(u) * np.sin(v),
    1 + c * np.cos(v),
    color="tab:green",
    alpha=0.85,
)


# паралелепіпед
box_faces = [
    [(1.2, -3, 0), (2.8, -3, 0), (2.8, -1.8, 0), (1.2, -1.8, 0)],  # низ
    [(1.2, -3, 1.2), (2.8, -3, 1.2), (2.8, -1.8, 1.2), (1.2, -1.8, 1.2)],  # верх
    [(1.2, -3, 0), (2.8, -3, 0), (2.8, -3, 1.2), (1.2, -3, 1.2)],  # передня (y = -3)
    [(1.2, -1.8, 0), (2.8, -1.8, 0), (2.8, -1.8, 1.2), (1.2, -1.8, 1.2)],  # задня (y = -1.8)
    [(1.2, -3, 0), (1.2, -1.8, 0), (1.2, -1.8, 1.2), (1.2, -3, 1.2)],  # ліва (x = 1.2)
    [(2.8, -3, 0), (2.8, -1.8, 0), (2.8, -1.8, 1.2), (2.8, -3, 1.2)],  # права (x = 2.8)
]
ax.add_collection3d(Poly3DCollection(box_faces, facecolors="tab:purple", edgecolor="k", alpha=0.9))

# конус
u, h = np.meshgrid(np.linspace(0, 2 * np.pi, 40), np.linspace(0, 1, 10))
ax.plot_surface(
    1.8 + (1 - h) * np.cos(u),
    2 + (1 - h) * np.sin(u),
    2.2 * h,
    color="tab:orange",
    alpha=0.9,
)

ax.set_title("Завдання 1. Півсфера, стрілка, піраміда, еліпсоїд, паралелепіпед, конус")
box(ax)


# ---------- Завдання 2: призма зі стрілками-ребрами ----------
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(projection="3d")
 
# вершини: нижня основа (z = 0) і верхня основа (z = 2.5)
bottom = [(1.5, 0, 0), (0.75, 1.3, 0), (-0.75, 1.3, 0), (-1.5, 0, 0), (-0.75, -1.3, 0), (0.75, -1.3, 0)]
top = [(1.5, 0, 2.5), (0.75, 1.3, 2.5), (-0.75, 1.3, 2.5), (-1.5, 0, 2.5), (-0.75, -1.3, 2.5), (0.75, -1.3, 2.5)]
 
# грані: дві основи та шість бічних прямокутників
faces = [
    bottom,
    top,
    [bottom[0], bottom[1], top[1], top[0]],
    [bottom[1], bottom[2], top[2], top[1]],
    [bottom[2], bottom[3], top[3], top[2]],
    [bottom[3], bottom[4], top[4], top[3]],
    [bottom[4], bottom[5], top[5], top[4]],
    [bottom[5], bottom[0], top[0], top[5]],
]
ax.add_collection3d(Poly3DCollection(faces, facecolors="skyblue", alpha=0.5))
 
for i in range(6):
    x, y, z = bottom[i]
    x2, y2, z2 = bottom[(i + 1) % 6]  # наступна вершина (після останньої знову перша)
    ax.quiver(x, y, 0, x2 - x, y2 - y, 0, color="black", arrow_length_ratio=0.12, linewidth=2)  # нижнє ребро
    ax.quiver(x, y, 2.5, x2 - x, y2 - y, 0, color="black", arrow_length_ratio=0.12, linewidth=2)  # верхнє ребро
    ax.quiver(x, y, 0, 0, 0, 2.5, color="crimson", arrow_length_ratio=0.12, linewidth=2)  # вертикальне ребро 


ax.text(0, 0, 1.25, "Шестикутна\nпризма", ha="center", va="center", fontsize=13)
ax.set_title("Завдання 2. Призма з ребрами-стрілками")
ax.set_xlim(-2.2, 2.2)
ax.set_ylim(-2.2, 2.2)
ax.set_zlim(0, 3)
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")


# ---------- Завдання 3: сторінка 23 альбому, обертання експоненти навколо Oz ----------
# r = e^w, z = w  =>  x = e^w cos u, y = e^w sin u, z = w
fig = plt.figure(figsize=(8, 7))
ax = fig.add_subplot(projection="3d")

u, w = np.meshgrid(np.linspace(0, 2 * np.pi, 120), np.linspace(-3, 1.2, 80))
surf = ax.plot_surface(
    np.exp(w) * np.cos(u), 
    np.exp(w) * np.sin(u), 
    w, 
    cmap="viridis", linewidth=0)

ax.set_xlim(-3, 3)
ax.set_ylim(-3, 3)
ax.set_zlim(-3, 1.2)
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.set_title("Завдання 3. Обертання експоненти r = e^z навколо осі Oz\nx=e^v cos u, y=e^v sin u, z=v")
fig.colorbar(surf, shrink=0.6, label="z")


# ---------- Завдання 4: z = x^2 - 2xy + 5/2 y^2 - 2x, D = [0,2]x[0,2] ----------
def f(x, y):
    return x**2 - 2 * x * y + 2.5 * y**2 - 2 * x


x, y = np.meshgrid(np.linspace(0, 2, 80), np.linspace(0, 2, 80))
fig = plt.figure(figsize=(8, 7))
ax = fig.add_subplot(projection="3d")

surf = ax.plot_surface(x, y, f(x, y), cmap="plasma")
fig.colorbar(surf, shrink=0.6, label="z")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.set_title("Завдання 4. z = x² − 2xy + 5/2·y² − 2x,  D: 0≤x≤2, 0≤y≤2")


# ---------- Завдання 5: три просторові діаграми, N = 23 + 4 = 27 стовпчиків ----------
N = V + 4
fig = plt.figure(figsize=(18, 6))

# діаграма 1: усі стовпчики в площині x = 1
ax = fig.add_subplot(1, 3, 1, projection="3d")
ax.bar3d(1, np.arange(N), 0, 0.4, 0.6, np.random.uniform(1, 5, N), color="tab:blue")
ax.set_xlim(0, 3)
ax.set_title("Діаграма 1: площина x = 1")

# діаграма 2: усі стовпчики в площині x = 2
ax = fig.add_subplot(1, 3, 2, projection="3d")
ax.bar3d(2, np.arange(N), 0, 0.4, 0.6, np.random.uniform(1, 5, N), color="tab:green")
ax.set_xlim(0, 3)
ax.set_title("Діаграма 2: площина x = 2")

# діаграма 3: кожен стовпчик у своїй площині y від 0.05 до 1
ax = fig.add_subplot(1, 3, 3, projection="3d")
ax.bar3d(np.arange(N), np.linspace(0.05, 1, N), 0, 0.6, 0.03, np.random.uniform(1, 5, N), color="tab:red")
ax.set_title("Діаграма 3: площини y від 0.05 до 1")

# підписи осей для всіх трьох діаграм
for ax in fig.axes:
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")


# ---------- Завдання 6: власна поверхня ----------
r, th = np.meshgrid(np.linspace(0, 3, 150), np.linspace(0, 2 * np.pi, 150))
X = r * np.cos(th)
Y = r * np.sin(th)
Z = np.sin(2 * r) * np.exp(-r / 3) * np.cos(3 * th / 2) ** 2

fig = plt.figure(figsize=(8, 7))
ax = fig.add_subplot(projection="3d")
ax.plot_surface(X, Y, Z, color="mediumseagreen", edgecolor="darkgreen", linewidth=0.15, alpha=0.9)
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.set_title("Завдання 6. z = sin(2r)·e^(−r/3)·cos²(3φ/2)")


# ---------- Завдання 7: мозаїка з трьох областей ----------
fig = plt.figure(figsize=(14, 9))
gs = fig.add_gridspec(2, 2)

# 1) каркасний графік
xg, yg = np.meshgrid(np.linspace(0, 2, 25), np.linspace(0, 2, 25))
ax1 = fig.add_subplot(gs[0, 0], projection="3d")
ax1.plot_wireframe(xg, yg, f(xg, yg), color="tab:blue", linewidth=0.6)
ax1.set_title("1) Каркасний графік z = x² − 2xy + 5/2·y² − 2x")

# 2) розсіяний графік
ax2 = fig.add_subplot(gs[1, 0], projection="3d")
xr = np.random.uniform(0, 2, 600)
yr = np.random.uniform(0, 2, 600)
ax2.scatter(xr, yr, f(xr, yr), c=f(xr, yr), cmap="plasma", s=8)
ax2.set_title("2) Розсіяний графік тієї ж поверхні")

for a in (ax1, ax2):
    a.set_xlabel("X")
    a.set_ylabel("Y")
    a.set_zlabel("Z")

# 3) полярний контурний графік на залитому контурному графіку
# крива ρ = a / (1 + b·cos φ), a = 1, b = -1/3  <=>  ρ·(1 - cos φ / 3) = 1
ax3 = fig.add_subplot(gs[:, 1], projection="polar")
phi, r = np.meshgrid(np.linspace(0, 2 * np.pi, 200), np.linspace(0, 3, 100))
Z = r * (1 - np.cos(phi) / 3)  # Z = 1 саме на кривій ρ = 1 / (1 − cos φ / 3)
ax3.contourf(phi, r, Z, levels=20, cmap="YlGnBu")  # залитий контурний графік
ax3.contour(phi, r, Z, levels=8, colors="black", linewidths=0.6)  # контурні лінії
ax3.contour(phi, r, Z, levels=[1], colors="red", linewidths=2.5)  # наша крива (рівень Z = 1)
ax3.set_title("3) Контурний графік у полярних координатах\nкрива ρ = 1 / (1 − cos φ / 3)")

fig.suptitle("Завдання 7. Мозаїка графічних областей")

plt.show()