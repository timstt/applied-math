from sympy import *
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

x, y = symbols('x y')
a, b, c, e = symbols('a b c e', positive=True)

# 1.43. Гіпербола x^2/a^2 - y^2/b^2 = 1, точки перетину директрис і асимптот: (±4, ±2)
px, py = 4, 2                                    # дані з умови

# Рівняння директрис і асимптот у вигляді "ліва частина - права частина = 0"
dir1 = x - a/e           # x = a/e
dir2 = x + a/e           # x = -a/e
as1 = y - b/a*x          # y = (b/a)x
as2 = y + b/a*x          # y = -(b/a)x

# Підставляємо всі 4 точки: кожна лежить на одній директрисі й одній асимптоті
system = [dir1.subs(x, px), as1.subs({x: px, y: py}),
          dir1.subs(x, px), as2.subs({x: px, y: -py}),
          dir2.subs(x, -px), as2.subs({x: -px, y: py}),
          dir2.subs(x, -px), as1.subs({x: -px, y: -py}),
          c**2 - a**2 - b**2,
          e - c/a]
print('Система:')
for eq in system:
    print('   ', eq, '= 0')

A, B, C, E = solve(system, [a, b, c, e])[0]
D = A/E                                          # директриси x = ±D
K = B/A                                          # асимптоти y = ±Kx
hyp = x**2/A**2 - y**2/B**2
print('a =', A, ', b =', B, ', c =', C, ', e =', E)
print('Рівняння гіперболи:', Eq(hyp, 1))

a1, b1, c1, d1, k1 = float(A), float(B), float(C), float(D), float(K)

# ---------------- Зображення ----------------
xmax = 2.5*c1                                    # межі вікна: з запасом за фокусами
ymax = 1.2*k1*xmax                               # асимптоти виходять з вікна збоку
h = xmax/30                                      # зсув підписів від точок

fig = plt.figure(figsize=(10, 6.5), facecolor='#f4f1ea')
ax = plt.axes(xlim=(-xmax, xmax), ylim=(-ymax, ymax))
ax.set_aspect('equal')
ax.grid(True, alpha=0.3)

X, Y = np.meshgrid(np.linspace(-xmax, xmax, 400), np.linspace(-ymax, ymax, 400))
Z = X**2/a1**2 - Y**2/b1**2
ax.contourf(X, Y, Z, [1, Z.max()], colors=['#cfe3f7'])
ax.contour(X, Y, Z, [1], colors=['b'], linewidths=2.5)
ax.plot([], [], 'b', lw=2.5, label='гіпербола $' + latex(hyp) + '=1$')

ax.plot([-xmax, xmax], [0, 0], 'k', lw=0.8)
ax.plot([0, 0], [-ymax, ymax], 'k', lw=0.8)
ax.plot([-xmax, xmax], [-k1*xmax, k1*xmax], 'g--', label='асимптоти $y=\\pm' + latex(K) + 'x$')
ax.plot([-xmax, xmax], [k1*xmax, -k1*xmax], 'g--')
ax.plot([d1, d1], [-ymax, ymax], 'm:', lw=2, label='директриси $x=\\pm' + latex(D) + '$')
ax.plot([-d1, -d1], [-ymax, ymax], 'm:', lw=2)
ax.plot([c1, -c1], [0, 0], 'r*', ms=15, label='фокуси $(\\pm' + latex(C) + ', 0)$')
ax.text(c1, -2*h, '$F_2$', color='r', fontsize=12)
ax.text(-c1 - h, -2*h, '$F_1$', color='r', fontsize=12)

for qx, qy in [(px, py), (px, -py), (-px, py), (-px, -py)]:
    ax.plot(qx, qy, 'ko', ms=8)
    ax.text(qx - 2*h, qy + h, '(' + str(qx) + ', ' + str(qy) + ')')

ax.text(-xmax + h, ymax - 7*h,
        '$' + latex(hyp) + '=1$\n$a=' + latex(A) + ',\\ b=' + latex(B) + ',\\ c=' + latex(C) +
        '$\n$e=' + latex(E) + '$',
        fontsize=11, bbox=dict(boxstyle='round', fc='white', ec='b'))
ax.legend(loc='upper center', fontsize=9)

# ---------------- Анімація ----------------
# Точка M рухається по правій гілці, потім по лівій; |r1 - r2| = 2a весь час стале
N = 100                                          # кадрів на одну гілку
ym_max = b1*np.sqrt(xmax**2/a1**2 - 1)           # до якого y гілка лишається у вікні
line_r1, = ax.plot([], [], color='orange', lw=2)
line_r2, = ax.plot([], [], color='purple', lw=2)
pc = plt.Circle((a1, 0), h/1.5, fc='orange', ec='k', zorder=5)
ax.add_patch(pc)


def redraw(i):
    ym = -ym_max + 2*ym_max*(i % N)/N
    xm = a1*np.sqrt(1 + ym**2/b1**2)
    if i >= N:
        xm = -xm                                  # ліва гілка
    pc.center = (xm, ym)
    line_r1.set_data([-c1, xm], [0, ym])
    line_r2.set_data([c1, xm], [0, ym])
    r1 = np.sqrt((xm + c1)**2 + ym**2)
    r2 = np.sqrt((xm - c1)**2 + ym**2)
    ax.set_title('r1 = {0:.2f},  r2 = {1:.2f},  |r1 - r2| = {2:.2f} = 2a = {3:.2f}'
                 .format(r1, r2, abs(r1 - r2), 2*a1))


anim = animation.FuncAnimation(fig, redraw, frames=2*N, interval=40)
plt.show()
