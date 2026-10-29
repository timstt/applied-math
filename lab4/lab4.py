# Лабораторна 4. Анімація (matplotlib). Варіант 23
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# ---------------------------------------------------------------
# Завдання 1. Крива їздить вправо-вліво і змінює колір
# y = arccos(1/sqrt(1+t^2)),  x = arcsin(t/(1+t^2))
# ---------------------------------------------------------------
t = np.linspace(-30, 30, 2000)
x1 = np.arcsin(t / (1 + t**2))
y1 = np.arccos(1 / np.sqrt(1 + t**2))

fig1, ax1 = plt.subplots()
ax1.set_xlim(-3.2, 3.2)
ax1.set_ylim(-0.3, 1.9)
ax1.axvline(-3, color="gray")   # ліва межа
ax1.axvline(3, color="gray")    # права межа
ax1.set_title("Завдання 1: крива рухається і змінює колір")
ax1.grid(True)
line1, = ax1.plot([], [], lw=3)

colors = ["blue", "red", "green", "orange", "purple"]
left = -3 - x1.min()    # зсув, коли крива торкається лівої межі
right = 3 - x1.max()    # зсув, коли крива торкається правої межі


start = -3.3 - x1.max()   # зсув, коли крива ще повністю за лівим краєм вікна


def update1(frame):
    if frame < 60:
        # спочатку крива виїжджає з-за лівого краю до лівої межі
        shift = start + (left - start) * frame / 60
        line1.set_color(colors[0])
    else:
        # k: 0..199 - вправо, 200..399 - назад (і так по колу)
        k = frame - 60
        f = k % 400
        s = f / 200 if f < 200 else 2 - f / 200     # від 0 до 1 і назад до 0
        shift = left + (right - left) * s
        line1.set_color(colors[(k // 200) % len(colors)])  # новий колір на кожній межі
    line1.set_data(x1 + shift, y1)


ani1 = FuncAnimation(fig1, update1, frames=2060, interval=20)

# ---------------------------------------------------------------
# Завдання 2. Поверхня обертання експоненти навколо осі Oz: r = e^z
# Поверхня "виростає", потім обертається камера і змінюється колір
# ---------------------------------------------------------------
z = np.linspace(-3, 1.5, 50)

fig2 = plt.figure()
ax2 = fig2.add_subplot(projection="3d")
cmaps = ["viridis", "plasma", "autumn", "cool"]


def update2(frame):
    ax2.clear()
    if frame < 60:                                  # фаза 1: поверхня будується
        angle_max = 2 * np.pi * (frame + 1) / 60
        azim = 35
        cmap = cmaps[0]
    else:                                           # фаза 2: обертання камери
        angle_max = 2 * np.pi
        azim = 35 + (frame - 60) * 3
        cmap = cmaps[((frame - 60) // 40) % len(cmaps)]
    th = np.linspace(0, angle_max, 50)
    Z, TH = np.meshgrid(z, th)
    R = np.exp(Z)
    ax2.plot_surface(R * np.cos(TH), R * np.sin(TH), Z, cmap=cmap)
    ax2.set_xlim(-4.5, 4.5)
    ax2.set_ylim(-4.5, 4.5)
    ax2.set_zlim(-3, 1.5)
    ax2.set_title("Завдання 2: r = e^z (обертання експоненти навколо Oz)")
    ax2.view_init(elev=25, azim=azim)


ani2 = FuncAnimation(fig2, update2, frames=2000, interval=40)

# ---------------------------------------------------------------
# Завдання 3. Полярна крива rho = 1 / (1 - cos(phi)/3)
# Спочатку промальовується, потім обертається навколо полюса
# ---------------------------------------------------------------
a, b = 1, -1 / 3
phi = np.linspace(0, 2 * np.pi, 400)
rho = a / (1 + b * np.cos(phi))

fig3 = plt.figure()
ax3 = fig3.add_subplot(projection="polar")
ax3.set_ylim(0, 1.8)
ax3.set_title("Завдання 3: ρ = 1 / (1 - cos φ / 3)")
line3, = ax3.plot([], [], lw=3)


def update3(frame):
    if frame < 100:                                 # фаза 1: промальовування
        n = 4 * (frame + 1)
        line3.set_data(phi[:n], rho[:n])
        line3.set_color("blue")
    else:                                           # фаза 2: обертання
        angle = (frame - 100) * 0.05
        line3.set_data(phi + angle, rho)
        line3.set_color(plt.cm.hsv(((frame - 100) % 120) / 120))


ani3 = FuncAnimation(fig3, update3, frames=2000, interval=30)

plt.show()