from sympy import *
from sympy.plotting import plot
import matplotlib.pyplot as plt
import numpy as np

x, t, r, phi = symbols('x t r phi', real=True)
y = Function('y')


# ---------------- 3.3.23 ----------------
# Загальний розв'язок: y'' + 4y' - 5y = x*e^x
ode = Eq(y(x).diff(x, 2) + 4*y(x).diff(x) - 5*y(x), x*exp(x))
sol = dsolve(ode, y(x))
print('3.3.23  ', sol)
print('        перевірка:', checkodesol(ode, sol))


# ---------------- 3.4.23 ----------------
# Задача Коші: y'' - 2y' + 2y = e^x*cos(x),  y(0) = 2,  y'(0) = -5
ode = Eq(y(x).diff(x, 2) - 2*y(x).diff(x) + 2*y(x), exp(x)*cos(x))
sol = dsolve(ode, y(x))
print('3.4.23  а) загальний: ', sol)
sol_c = dsolve(ode, y(x), ics={y(0): 2, y(x).diff(x).subs(x, 0): -5})
print('        б) частковий: ', sol_c)
print('        перевірка:', checkodesol(ode, sol_c))

p = plot(sol_c.rhs, (x, -3, 3), title='3.4.23', line_color='r', ylabel='y(x)')


# ---------------- 4.1.23 ----------------
# Система: x' = 2x + 3y + sin(t),  y' = -3x + 2y + cos(t)
X = Function('x')
Y = Function('y')
sys_ = [Eq(X(t).diff(t), 2*X(t) + 3*Y(t) + sin(t)),
        Eq(Y(t).diff(t), -3*X(t) + 2*Y(t) + cos(t))]
sol = dsolve(sys_, [X(t), Y(t)])
print('4.1.23  ', simplify(sol[0]))
print('        ', simplify(sol[1]))
print('        перевірка:', checkodesol(sys_, sol))


# ---------------- 1.2.23 ----------------
# Подвійний інтеграл (x - 2y + 5) по D: y = 0, y = 1, y = sqrt(-x), x = 2
# D: 0 <= y <= 1,  -y^2 <= x <= 2
xs, ys = symbols('x y', real=True)
I = integrate(xs - 2*ys + 5, (xs, -ys**2, 2), (ys, 0, 1))
print('1.2.23  I =', I)

Yv = np.linspace(0, 1, 200)
plt.fill_betweenx(Yv, -Yv**2, 2, color='orange')
Yc = np.linspace(0, 1.3, 200)
plt.plot(-Yc**2, Yc, 'b', label='$y=\\sqrt{-x}$')
plt.axhline(0, color='g', label='$y=0$')
plt.axhline(1, color='r', label='$y=1$')
plt.axvline(2, color='m', label='$x=2$')
plt.xlim(-2, 2.5)
plt.ylim(-0.5, 1.5)
plt.legend()
plt.title('1.2.23')
plt.grid()
plt.show()


# ---------------- 1.3.23 ----------------
# Площа D: x^2 + y^2 + 12y <= 0,  y >= sqrt(3)*x,  sqrt(3)*y <= x
# Полярна система: коло r = -12 sin(phi), промені phi = 7pi/6 і phi = 4pi/3
S_pol = integrate(integrate(r, (r, 0, -12*sin(phi))), (phi, 7*pi/6, 4*pi/3))
print('1.3.23  S (полярна)  =', simplify(S_pol))

# Декартова система: прямі перетинають коло в точках (-3sqrt3, -9) і (-3sqrt3, -3)
# частина 1: -6 <= x <= -3sqrt3, між дугами кола
# частина 2: -3sqrt3 <= x <= 0, між прямими y = sqrt(3)x і y = x/sqrt(3)
a = -3*sqrt(3)
S1 = integrate(2*sqrt(36 - xs**2), (xs, -6, a))
S2 = integrate(xs/sqrt(3) - sqrt(3)*xs, (xs, a, 0))
S_dec = simplify(S1 + S2)
print('        S (декартова) =', S_dec)
print('        збігаються:', simplify(S_pol - S_dec) == 0)

fig = plt.figure(figsize=(12, 6))

ax = fig.add_subplot(1, 2, 1)
T = np.linspace(0, 2*np.pi, 300)
ax.plot(6*np.cos(T), -6 + 6*np.sin(T), 'b', label='$x^2+y^2+12y=0$')
Xl = np.linspace(-7, 2, 100)
ax.plot(Xl, np.sqrt(3)*Xl, 'g', label='$y=\\sqrt{3}x$')
ax.plot(Xl, Xl/np.sqrt(3), 'r', label='$\\sqrt{3}y=x$')
F = np.linspace(7*np.pi/6, 4*np.pi/3, 100)
R = -12*np.sin(F)
ax.fill(np.concatenate([[0], R*np.cos(F)]), np.concatenate([[0], R*np.sin(F)]), color='orange')
ax.set_xlim(-8, 8)
ax.set_ylim(-13, 3)
ax.set_aspect('equal')
ax.legend(loc='lower right')
ax.grid()
ax.set_title('1.3.23 (декартова)')

ax = fig.add_subplot(1, 2, 2, projection='polar')
Fc = np.linspace(np.pi, 2*np.pi, 200)
ax.plot(Fc, -12*np.sin(Fc), 'b', label='$r=-12\\sin\\varphi$')
ax.plot([7*np.pi/6, 7*np.pi/6], [0, 13], 'r', label='$\\varphi=7\\pi/6$')
ax.plot([4*np.pi/3, 4*np.pi/3], [0, 13], 'g', label='$\\varphi=4\\pi/3$')
ax.fill_between(F, 0, R, color='orange')
ax.set_rmax(13)
ax.legend(loc='upper right')
ax.set_title('1.3.23 (полярна)')

plt.show()
