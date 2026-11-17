from sympy import *
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.patches import Rectangle

x, y = symbols('x y')
a, b, c, e = symbols('a b c e', positive=True)


# ---------------- 1.43 ----------------
# Скласти рівняння гіперболи x^2/a^2 - y^2/b^2 = 1, знаючи чотири точки (±4, ±2)
# перетину її директрис і асимптот.
#
# Директриси:  x = a/e,  x = -a/e
# Асимптоти:   y = (b/a)x,  y = -(b/a)x
# Зв'язок:     c^2 = a^2 + b^2,  e = c/a
#
# Кожна точка лежить на одній директрисі й одній асимптоті:
#   (4, 2):   x = a/e,   y = (b/a)x
#   (4, -2):  x = a/e,   y = -(b/a)x
#   (-4, 2):  x = -a/e,  y = -(b/a)x
#   (-4, -2): x = -a/e,  y = (b/a)x
# Підставляємо всі 4 точки і отримуємо систему:
system = [Eq(4, a/e), Eq(2, b/a*4),
          Eq(4, a/e), Eq(-2, -b/a*4),
          Eq(-4, -a/e), Eq(2, -b/a*(-4)),
          Eq(-4, -a/e), Eq(-2, b/a*(-4)),
          Eq(c**2, a**2 + b**2),
          Eq(e, c/a)]
print('1.43    система:')
for eq in system:
    print('           ', eq)

sol = solve(system, [a, b, c, e])
A, B, C, E = sol[0]
print('        a =', A, ', b =', B, ', c =', C, ', e =', E)
print('        a^2 =', A**2, ', b^2 =', B**2)
print('        рівняння гіперболи:', Eq(x**2/A**2 - y**2/B**2, 1))
print('        директриси: x = ±', A/E, ',  асимптоти: y = ±', B/A, '* x')
print('        фокуси: (±', C, ', 0)')

# Перевірка: підставляємо знайдені a, b, e у праву частину рівнянь директрис і асимптот
print('        перевірка (4, 2):  x =', (A/E), ', y =', B/A*4)
print('        перевірка (-4, -2): x =', (-A/E), ', y =', B/A*(-4))


# ---------------- Зображення ----------------
a1 = float(A)
b1 = float(B)
c1 = float(C)
d1 = float(A/E)                                  # директриси x = ±4

fig = plt.figure(figsize=(10, 6.5), facecolor='#f4f1ea')
ax = plt.axes(xlim=(-13, 13), ylim=(-7.5, 7.5))
ax.set_aspect('equal')
ax.grid(True, alpha=0.3)

# Гіпербола як лінія рівня x^2/20 - y^2/5 = 1, внутрішня область залита
X, Y = np.meshgrid(np.linspace(-13, 13, 500), np.linspace(-7.5, 7.5, 400))
Z = X**2/a1**2 - Y**2/b1**2
ax.contourf(X, Y, Z, [1, 100], colors=['#cfe3f7'])
ax.contour(X, Y, Z, [1], colors=['#1f4e9c'], linewidths=2.5)
ax.plot([], [], color='#1f4e9c', lw=2.5, label='гіпербола $x^2/20-y^2/5=1$')

# Основний прямокутник 2a x 2b — його діагоналі лежать на асимптотах
rect = Rectangle((-a1, -b1), 2*a1, 2*b1, fill=False, ec='gray', ls='-.')
ax.add_patch(rect)

# Осі координат
ax.plot([-13, 13], [0, 0], 'k', lw=0.8)
ax.plot([0, 0], [-7.5, 7.5], 'k', lw=0.8)
ax.text(12.5, 0.3, 'x', fontsize=12)
ax.text(0.3, 7, 'y', fontsize=12)

# Асимптоти y = ±x/2
xa = np.linspace(-13, 13, 2)
ax.plot(xa, b1/a1*xa, 'g--', label='асимптоти $y=\\pm x/2$')
ax.plot(xa, -b1/a1*xa, 'g--')

# Директриси x = ±4
ax.plot([d1, d1], [-7.5, 7.5], 'm:', lw=2, label='директриси $x=\\pm4$')
ax.plot([-d1, -d1], [-7.5, 7.5], 'm:', lw=2)

# Задані точки (±4, ±2)
ax.plot([4, 4, -4, -4], [2, -2, 2, -2], 'ko', ms=8, label='точки $(\\pm4, \\pm2)$')
ax.text(4.3, 2.3, '(4, 2)')
ax.text(4.3, -2.7, '(4, -2)')
ax.text(-6.3, 2.3, '(-4, 2)')
ax.text(-6.6, -2.7, '(-4, -2)')

# Вершини і фокуси
ax.plot([a1, -a1], [0, 0], 'bs')
ax.text(a1 - 0.9, 0.3, '$A_2$', color='b')
ax.text(-a1 + 0.2, 0.3, '$A_1$', color='b')
ax.plot([c1, -c1], [0, 0], 'r*', ms=15, label='фокуси $(\\pm5, 0)$')
ax.text(c1, -0.8, '$F_2$', color='r', fontsize=12)
ax.text(-c1 - 0.6, -0.8, '$F_1$', color='r', fontsize=12)

# Півосі a і b
ax.annotate('', xy=(a1, -b1 - 0.6), xytext=(0, -b1 - 0.6), arrowprops=dict(arrowstyle='<->'))
ax.text(1.5, -b1 - 1.3, '$a=2\\sqrt{5}$')
ax.annotate('', xy=(-a1 - 0.6, b1), xytext=(-a1 - 0.6, 0), arrowprops=dict(arrowstyle='<->'))
ax.text(-a1 - 3.3, 0.9, '$b=\\sqrt{5}$')

# Рамка з відповіддю
bbox_properties = dict(boxstyle='round', fc='white', ec='#1f4e9c')
ax.text(-12.5, 4.6, '$x^2/20-y^2/5=1$\n$a=2\\sqrt{5},\\ b=\\sqrt{5},\\ c=5$\n$e=\\sqrt{5}/2$',
        fontsize=11, bbox=bbox_properties)
ax.legend(loc='lower right', fontsize=9)


# ---------------- Анімація ----------------
# Точка M рухається по правій гілці знизу вгору, потім по лівій згори вниз.
# Фокальні радіуси r1 = |F1M| і r2 = |F2M| змінюються, а |r1 - r2| = 2a лишається сталим.
N = 100                                          # кадрів на одну гілку
line_r1, = ax.plot([], [], color='orange', lw=2)
line_r2, = ax.plot([], [], color='purple', lw=2)
trail, = ax.plot([], [], color='orange', lw=4, alpha=0.4)
pc = plt.Circle((a1, 0), 0.25, fc='orange', ec='k', zorder=5)
ax.add_patch(pc)


def redraw(i):
    if i < N:                                    # права гілка: y від -6 до 6
        yy = np.linspace(-6, -6 + 12*i/(N - 1), i + 1)
        xx = a1*np.sqrt(1 + yy**2/b1**2)
    else:                                        # ліва гілка: y від 6 до -6
        yy = np.linspace(6, 6 - 12*(i - N)/(N - 1), i - N + 1)
        xx = -a1*np.sqrt(1 + yy**2/b1**2)
    xm = xx[-1]                                  # поточне положення точки M
    ym = yy[-1]
    trail.set_data(xx, yy)
    pc.center = (xm, ym)
    line_r1.set_data([-c1, xm], [0, ym])
    line_r2.set_data([c1, xm], [0, ym])
    r1 = np.sqrt((xm + c1)**2 + ym**2)
    r2 = np.sqrt((xm - c1)**2 + ym**2)
    ax.set_title('r1 = ' + str(round(r1, 3)) + ',   r2 = ' + str(round(r2, 3)) +
                 ',   |r1 - r2| = ' + str(round(abs(r1 - r2), 3)) +
                 ' = 2a = ' + str(round(2*a1, 3)))


anim = animation.FuncAnimation(fig, redraw, frames=2*N, interval=40)
plt.show()
