from sympy import *
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
xl = solve(Eq(ys, sqrt(-xs)), xs)[0]          # ліва межа: виражаємо x через y
print('1.2.23  ліва межа: x =', xl)
I = integrate(xs - 2*ys + 5, (xs, xl, 2), (ys, 0, 1))
print('        I =', I)

fx = lambdify(ys, xl)                         # формула -> функція для NumPy
Yv = np.linspace(0, 1, 200)
plt.fill_betweenx(Yv, fx(Yv), 2, color='orange')
Yc = np.linspace(0, 1.3, 200)
plt.plot(fx(Yc), Yc, 'b', label='$y=\\sqrt{-x}$')
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
circle = xs**2 + ys**2 + 12*ys
line1 = ys - sqrt(3)*xs                       # пряма y = sqrt(3)x
line2 = sqrt(3)*ys - xs                       # пряма sqrt(3)y = x

# Точки перетину прямих з колом
P1 = solve([circle, line1], [xs, ys])
P2 = solve([circle, line2], [xs, ys])
print('1.3.23  точки перетину:', P1, P2)

# Полярна система: кути променів беремо з точок перетину (atan2 дає кут від -pi до pi)
phi1 = atan2(P2[1][1], P2[1][0]) + 2*pi
phi2 = atan2(P1[1][1], P1[1][0]) + 2*pi
print('        промені: phi1 =', phi1, '  phi2 =', phi2)
# рівняння кола в полярних: підставляємо x = r cos(phi), y = r sin(phi) і розв'язуємо відносно r
rc = solve(circle.subs({xs: r*cos(phi), ys: r*sin(phi)}), r)[1]
print('        коло: r =', rc)
S_pol = integrate(r, (r, 0, rc), (phi, phi1, phi2))
print('        S (полярна)  =', simplify(S_pol))

# Декартова система: обидві точки мають x = -3sqrt3, тому область ділимо на дві частини:
# частина 1: від лівого краю кола до -3sqrt3, між дугами кола
# частина 2: -3sqrt3 <= x <= 0, між прямими y = sqrt(3)x і y = x/sqrt(3)
a = P1[1][0]
x0 = P1[0][0]                                 # вершина (0, 0), де перетинаються прямі
y1 = solve(line1, ys)[0]                      # виражаємо y з рівнянь прямих
y2 = solve(line2, ys)[0]
if (y2 - y1).subs(xs, (a + x0)/2) > 0:        # яка пряма зверху: перевіряємо в точці посередині
    y_top, y_bot = y2, y1
else:
    y_top, y_bot = y1, y2
print('        прямі: зверху y =', y_top, ', знизу y =', y_bot)
y_low, y_up = solve(circle, ys)               # нижня і верхня дуги кола
x_left, x_right = solve(y_up - y_low, xs)     # краї кола, де дуги сходяться
print('        дуги: y =', y_low, ',', y_up, '   краї кола: x =', x_left, ',', x_right)
S1 = integrate(y_up - y_low, (xs, x_left, a))
S2 = integrate(y_top - y_bot, (xs, a, x0))
S_dec = simplify(S1 + S2)
print('        S (декартова) =', S_dec)
print('        збігаються:', simplify(S_pol - S_dec) == 0)

fig = plt.figure(figsize=(12, 6))

ax = fig.add_subplot(1, 2, 1)
Xc = np.linspace(float(x_left), float(x_right), 300)
ax.plot(Xc, lambdify(xs, y_up)(Xc), 'b', label='$x^2+y^2+12y=0$')
ax.plot(Xc, lambdify(xs, y_low)(Xc), 'b')
Xl = np.linspace(-7, 2, 100)
ax.plot(Xl, lambdify(xs, y1)(Xl), 'g', label='$y=\\sqrt{3}x$')
ax.plot(Xl, lambdify(xs, y2)(Xl), 'r', label='$\\sqrt{3}y=x$')
f1 = float(phi1)
f2 = float(phi2)
fr = lambdify(phi, rc)
F = np.linspace(f1, f2, 100)
R = fr(F)
ax.fill(np.concatenate([[0], R*np.cos(F)]), np.concatenate([[0], R*np.sin(F)]), color='orange')
ax.set_xlim(-8, 8)
ax.set_ylim(-13, 3)
ax.set_aspect('equal')
ax.legend(loc='lower right')
ax.grid()
ax.set_title('1.3.23 (декартова)')

ax = fig.add_subplot(1, 2, 2, projection='polar')
Fc = np.linspace(np.pi, 2*np.pi, 200)
ax.plot(Fc, fr(Fc), 'b', label='$r=-12\\sin\\varphi$')
ax.plot([f1, f1], [0, 13], 'r', label='$\\varphi=7\\pi/6$')
ax.plot([f2, f2], [0, 13], 'g', label='$\\varphi=4\\pi/3$')
ax.fill_between(F, 0, R, color='orange')
ax.set_rmax(13)
ax.legend(loc='upper right')
ax.set_title('1.3.23 (полярна)')

plt.show()
