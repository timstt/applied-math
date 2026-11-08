# STEM-проєкт. Криві другого порядку та поверхні обертання (sympy, matplotlib). Варіант 23
from sympy import *
import matplotlib.pyplot as plt
import numpy as np

x, y, z = symbols('x y z', real=True)
a2, b2 = symbols('a2 b2', positive=True)


# ---------------- 1.23 ----------------
# Еліпс x^2/a^2 + y^2/b^2 = 1, фокуси (1, 0), (-1, 0), точка (sqrt(3), sqrt(3)/2) належить еліпсу
c = 1
Mx, My = sqrt(3), sqrt(3)/2
sol = solve([Eq(a2 - b2, c**2),
             Eq(Mx**2/a2 + My**2/b2, 1)], [a2, b2], dict=True)[0]
A2, B2 = sol[a2], sol[b2]
a, b = sqrt(A2), sqrt(B2)
e = c/a
ellipse = Eq(x**2/A2 + y**2/B2, 1)
print('1.23    a^2 =', A2, ', b^2 =', B2)
print('        рівняння еліпса:', ellipse)
print('        ексцентриситет e =', e, ', директриси x = ±', a/e)
print('        перевірка: точка M на еліпсі ->', simplify(ellipse.lhs.subs({x: Mx, y: My})) == 1)

t = np.linspace(0, 2*np.pi, 400)
af, bf = float(a), float(b)
plt.figure()
plt.plot(af*np.cos(t), bf*np.sin(t), 'b', label=f'$x^2/{A2}+y^2/{B2}=1$')
plt.plot([-c, c], [0, 0], 'ro', label='фокуси $F_{1,2}(\\pm1, 0)$')
plt.plot(float(Mx), float(My), 'go', label='$M(\\sqrt{3}, \\sqrt{3}/2)$')
plt.plot([-c, float(Mx), c], [0, float(My), 0], 'g--', lw=0.8)
for d in (-float(a/e), float(a/e)):
    plt.axvline(d, color='m', ls=':')
plt.plot([], [], 'm:', label='директриси $x=\\pm4$')
plt.axhline(0, color='k', lw=0.5)
plt.axvline(0, color='k', lw=0.5)
plt.gca().set_aspect('equal')
plt.xlim(-5, 5)
plt.ylim(-4, 3)
plt.legend(loc='lower center', ncol=2, fontsize=8)
plt.title('1.23')


# ---------------- 2.1.23 ----------------
# Поверхня обертання лінії y - z - 5 = 0, x = 0 навколо осі Oz
# При обертанні навколо Oz: y -> ±sqrt(x^2 + y^2), z без змін
line = y - z - 5
r = symbols('r', nonnegative=True)
surf = expand(line.subs(y, r) * line.subs(y, -r))   # добуток двох гілок y = ±r
surf = surf.subs(r**2, x**2 + y**2)
print('2.1.23  поверхня:', Eq(surf, 0))
print('        тобто x^2 + y^2 - (z + 5)^2 = 0 — круговий конус з вершиною (0, 0, -5)')

# Перевірка: будь-яка точка твірної, повернута навколо Oz, лежить на поверхні
s, phi = symbols('s phi', real=True)
P = (s*cos(phi), s*sin(phi), s - 5)                  # точка (0, s, s-5) твірної, повернута на кут phi
print('        перевірка:', simplify(surf.subs({x: P[0], y: P[1], z: P[2]})) == 0)

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
Z, PHI = np.meshgrid(np.linspace(-10, 0, 60), np.linspace(0, 2*np.pi, 80))
R = np.abs(Z + 5)
ax.plot_surface(R*np.cos(PHI), R*np.sin(PHI), Z, cmap='viridis', alpha=0.6)
zl = np.linspace(-10, 0, 2)
ax.plot(0*zl, zl + 5, zl, 'r', lw=3, label='твірна $y-z-5=0,\\ x=0$')
ax.plot([0, 0], [0, 0], [-11, 1], 'k--', label='вісь $Oz$')
ax.scatter(0, 0, -5, color='k', s=30)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.legend(fontsize=8)
ax.set_title('2.1.23:  $x^2+y^2=(z+5)^2$')

plt.show()
