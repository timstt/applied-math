from sympy import *
from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import numpy as np

x, y = symbols('x y', real=True)
a, b, c, e = symbols('a b c e', positive=True)


# ---------------- 1.43 ----------------
# Скласти рівняння гіперболи x^2/a^2 - y^2/b^2 = 1, знаючи чотири точки (±4, ±2)
# перетину її директрис і асимптот.
#
# 1) Рівняння директрис і асимптот гіперболи:
#    директриси  x = a/e,  x = -a/e
#    асимптоти   y = (b/a)x,  y = -(b/a)x
#    і зв'язок   c^2 = a^2 + b^2,  e = c/a
dir1 = Eq(x, a/e)
dir2 = Eq(x, -a/e)
as1 = Eq(y, b/a*x)
as2 = Eq(y, -b/a*x)
print('1.43    директриси:', dir1, ',', dir2)
print('        асимптоти: ', as1, ',', as2)

# 2) Кожна точка перетину лежить на одній директрисі й одній асимптоті:
#    (4, 2):   x = a/e,  y = (b/a)x       (4, -2):  x = a/e,  y = -(b/a)x
#    (-4, 2):  x = -a/e, y = -(b/a)x      (-4, -2): x = -a/e, y = (b/a)x
points = {(4, 2): (dir1, as1), (4, -2): (dir1, as2),
          (-4, 2): (dir2, as2), (-4, -2): (dir2, as1)}

# 3) Підставляємо всі 4 точки — отримуємо систему
system = []
for (px, py), (dr, asy) in points.items():
    for eq in (dr, asy):
        eq_p = eq.subs({x: px, y: py})
        if eq_p not in system:                      # однакові рівняння беремо один раз
            system.append(eq_p)
system += [Eq(c**2, a**2 + b**2), Eq(e, c/a)]
print('        система:')
for eq in system:
    print('           ', eq)

# 4) Розв'язуємо систему
sol = solve(system, [a, b, c, e], dict=True)[0]
A, B, C, E = sol[a], sol[b], sol[c], sol[e]
hyperbola = Eq(x**2/A**2 - y**2/B**2, 1)
print('        розв\'язок: a =', A, ', b =', B, ', c =', C, ', e =', E)
print('        a^2 =', A**2, ', b^2 =', B**2)
print('        рівняння гіперболи:', hyperbola)
print('        фокуси: (±', C, ', 0)')

# Перевірка: всі 4 точки задовольняють знайдені рівняння директрис і асимптот
ok = all(dr.subs({a: A, e: E, x: px}) == True and asy.subs({a: A, b: B, x: px, y: py}) == True
         for (px, py), (dr, asy) in points.items())
print('        перевірка, всі 4 точки на директрисах і асимптотах:', ok)
e = E


# ---------------- Зображення ----------------
af, bf, cf, ef = float(A), float(B), float(C), float(e)
d = af**2/cf                                         # директриси x = ±d
L = 13                                               # межа вікна по x

fig, ax = plt.subplots(figsize=(10, 6.5))
fig.patch.set_facecolor('#f4f1ea')
ax.set_facecolor('#fbfaf6')

# Внутрішня область гіперболи x^2/20 - y^2/5 >= 1 (там, де фокуси)
Xg, Yg = np.meshgrid(np.linspace(-L, L, 600), np.linspace(-7.5, 7.5, 400))
ax.contourf(Xg, Yg, Xg**2/af**2 - Yg**2/bf**2, levels=[1, 1e9], colors=['#cfe3f7'], alpha=0.6)

# Основний прямокутник 2a x 2b, діагоналі якого лежать на асимптотах
ax.add_patch(plt.Rectangle((-af, -bf), 2*af, 2*bf, fill=False, ec='#999', ls='-.', lw=1))
ax.annotate('', xy=(af, -bf - 0.6), xytext=(0, -bf - 0.6), arrowprops=dict(arrowstyle='<->', color='#555'))
ax.text(af/2, -bf - 1.2, r'$a=2\sqrt{5}$', ha='center', color='#555')
ax.annotate('', xy=(-af - 0.6, bf), xytext=(-af - 0.6, 0), arrowprops=dict(arrowstyle='<->', color='#555'))
ax.text(-af - 0.8, bf/2, r'$b=\sqrt{5}$', ha='right', va='center', color='#555')

# Гіпербола (дві гілки)
T = np.linspace(-2.5, 2.5, 500)
ax.plot(af*np.cosh(T), bf*np.sinh(T), color='#1f4e9c', lw=2.5,
        label=r'$\dfrac{x^2}{20}-\dfrac{y^2}{5}=1$')
ax.plot(-af*np.cosh(T), bf*np.sinh(T), color='#1f4e9c', lw=2.5)

# Асимптоти та директриси
Xa = np.array([-L, L])
ax.plot(Xa, bf/af*Xa, color='#2e8b57', ls='--', lw=1.3, label=r'асимптоти $y=\pm\frac{1}{2}x$')
ax.plot(Xa, -bf/af*Xa, color='#2e8b57', ls='--', lw=1.3)
ax.axvline(d, color='#b03aa8', ls=':', lw=1.8, label=r'директриси $x=\pm4$')
ax.axvline(-d, color='#b03aa8', ls=':', lw=1.8)

# Задані точки перетину (±4, ±2)
for px in (4, -4):
    for py in (2, -2):
        ax.plot(px, py, 'o', ms=8, color='#222', zorder=5)
        ax.text(px + (0.3 if px > 0 else -0.3), py + (0.35 if py > 0 else -0.6),
                f'({px}, {py})', ha='left' if px > 0 else 'right', fontsize=9)

# Вершини і фокуси
ax.plot([af, -af], [0, 0], 's', ms=7, color='#1f4e9c', zorder=5)
ax.text(af - 0.2, 0.35, '$A_2$', ha='right', color='#1f4e9c')
ax.text(-af + 0.2, 0.35, '$A_1$', color='#1f4e9c')
ax.plot([cf, -cf], [0, 0], '*', ms=15, color='#d62728', zorder=5, label=r'фокуси $F_{1,2}(\pm5, 0)$')
ax.text(cf + 0.2, -0.7, '$F_2$', color='#d62728', fontsize=12)
ax.text(-cf - 0.7, -0.7, '$F_1$', color='#d62728', fontsize=12)

# Осі та підписи
ax.axhline(0, color='k', lw=0.8)
ax.axvline(0, color='k', lw=0.8)
ax.text(L - 0.3, 0.3, 'x', fontsize=12)
ax.text(0.3, 7.0, 'y', fontsize=12)
ax.text(0.15, -0.6, 'O')
ax.set_xlim(-L, L)
ax.set_ylim(-7.5, 7.5)
ax.set_aspect('equal')
ax.grid(alpha=0.3)
ax.set_title('1.43. Гіпербола за точками перетину директрис і асимптот', fontsize=13, weight='bold')

info = '\n'.join([r'$\dfrac{x^2}{20}-\dfrac{y^2}{5}=1$',
                  r'$a=2\sqrt{5},\ b=\sqrt{5},\ c=5$',
                  r'$e=\dfrac{\sqrt{5}}{2}\approx$' + f'{ef:.3f}'])
ax.text(-L + 0.4, 7.1, info, va='top', fontsize=11,
        bbox=dict(boxstyle='round,pad=0.5', fc='white', ec='#1f4e9c'))
ax.legend(loc='lower right', fontsize=9, framealpha=0.95)


# ---------------- Анімація ----------------
# Точка M рухається по правій гілці, потім по лівій. Фокальні радіуси r1 = |F1M|, r2 = |F2M|
# змінюються, а їх різниця |r1 - r2| = 2a лишається сталою — це і є означення гіперболи.
N = 120                                              # кадрів на одну гілку
Tm = np.concatenate([np.linspace(-2.2, 2.2, N), np.linspace(2.2, -2.2, N)])
Sm = np.concatenate([np.ones(N), -np.ones(N)])       # 1 — права гілка, -1 — ліва

r1_line, = ax.plot([], [], color='#ff7f0e', lw=2)
r2_line, = ax.plot([], [], color='#9467bd', lw=2)
trail, = ax.plot([], [], color='#ff7f0e', lw=4, alpha=0.35)
point, = ax.plot([], [], 'o', ms=11, color='#ff7f0e', mec='k', zorder=6)
label_M = ax.text(0, 0, '', fontsize=12, weight='bold')
readout = ax.text(L - 0.4, 7.1, '', ha='right', va='top', fontsize=10, family='monospace',
                  bbox=dict(boxstyle='round,pad=0.5', fc='#fff7e6', ec='#ff7f0e'))
hist = []


def update(k):
    s, tt = Sm[k], Tm[k]
    mx, my = s*af*np.cosh(tt), bf*np.sinh(tt)
    if k % N == 0:
        hist.clear()                                 # нова гілка — новий слід
    hist.append((mx, my))
    r1 = np.hypot(mx + cf, my)
    r2 = np.hypot(mx - cf, my)
    r1_line.set_data([-cf, mx], [0, my])
    r2_line.set_data([cf, mx], [0, my])
    trail.set_data(*zip(*hist))
    point.set_data([mx], [my])
    label_M.set_position((mx + 0.3, my + 0.3))
    label_M.set_text('M')
    point.set_color(plt.cm.plasma(k / len(Tm)))
    readout.set_text(f'M = ({mx:6.2f}, {my:6.2f})\n'
                     f'r1 = |F1M| = {r1:6.3f}\n'
                     f'r2 = |F2M| = {r2:6.3f}\n'
                     f'|r1 - r2| = {abs(r1 - r2):6.3f}\n'
                     f'2a        = {2*af:6.3f}')
    return r1_line, r2_line, trail, point, label_M, readout


anim = FuncAnimation(fig, update, frames=len(Tm), interval=40, blit=False)
plt.tight_layout()
plt.show()
