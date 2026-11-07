from sympy import *
from sympy.plotting import plot, plot_parametric
import matplotlib.pyplot as plt
import numpy as np

x, t, n = symbols('x t n', real=True)


# ---------------- 8.1.23 ----------------
# Площа фігури: y = sin^4(x)*sin(2x), y = 0, 0 <= x <= pi/3
f = sin(x)**4 * sin(2*x)
S = integrate(f, (x, 0, pi/3))
print('8.1.23  S =', S)

X = np.linspace(0, np.pi/3, 200)
Y = np.sin(X)**4 * np.sin(2*X)
plt.plot(X, Y, 'b')
plt.fill_between(X, Y, color='orange')
plt.title('8.1.23')
plt.grid()
plt.show()


# ---------------- 8.2.23 ----------------
# Площа спільної частини: r = sqrt(3)*cos(t), r = sin(t)   (t - полярний кут)
r1 = sqrt(3)*cos(t)
r2 = sin(t)
t0 = solve(Eq(r1, r2), t)[0] 
print('8.2.23  Точка перетину t0 =', t0)
S = integrate(r2**2, (t, 0, t0))/2 + integrate(r1**2, (t, t0, pi/2))/2
print('        S =', S)

T = np.linspace(0, np.pi, 200)
plt.plot(np.sqrt(3)*np.cos(T)*np.cos(T), np.sqrt(3)*np.cos(T)*np.sin(T), 'b')
plt.plot(np.sin(T)*np.cos(T), np.sin(T)*np.sin(T), 'r')
Ta = np.linspace(0, np.pi/3, 100)
Tb = np.linspace(np.pi/3, np.pi/2, 100) 
Xf = np.concatenate([np.sin(Ta)*np.cos(Ta), np.sqrt(3)*np.cos(Tb)*np.cos(Tb)])
Yf = np.concatenate([np.sin(Ta)*np.sin(Ta), np.sqrt(3)*np.cos(Tb)*np.sin(Tb)])
plt.fill(Xf, Yf, color='orange')
plt.axis('equal')
plt.title('8.2.23')
plt.grid()
plt.show()


# ---------------- 8.3.23 ----------------
# Площа: циклоїда x = 2(t - sin t), y = 2(1 - cos t) між прямими y = 2 і y = 3
xt = 2*(t - sin(t))
yt = 2*(1 - cos(t))
t1 = solve(Eq(yt, 2), t)[0] 
t2 = solve(Eq(yt, 3), t)[0] 
print('8.3.23  t1 =', t1, '  t2 =', t2)
width = xt.subs(t, 2*pi - t) - xt  
S = integrate(width * diff(yt, t), (t, t1, t2))
S = simplify(S)
print('        S =', S)

T = np.linspace(0, 2*np.pi, 300)
plt.plot(2*(T - np.sin(T)), 2*(1 - np.cos(T)), 'b')
plt.axhline(2, color='g')
plt.axhline(3, color='r')
Tl = np.linspace(np.pi/2, 2*np.pi/3, 100)   
Tr = np.linspace(4*np.pi/3, 3*np.pi/2, 100)
Xf = np.concatenate([2*(Tl - np.sin(Tl)), 2*(Tr - np.sin(Tr))])
Yf = np.concatenate([2*(1 - np.cos(Tl)), 2*(1 - np.cos(Tr))])
plt.fill(Xf, Yf, color='orange')
plt.axis('equal')
plt.title('8.3.23')
plt.grid()
plt.show()


# ---------------- 8.4.23 ----------------
# Довжина лінії y = 1 + arcsin(x) - sqrt(1 - x^2),  x від 0 до 3/4
f = 1 + asin(x) - sqrt(1 - x**2)
df = diff(f, x)
print("8.4.23  y' =", simplify(df))
print("        1 + y'^2 =", simplify(1 + df**2))        
L = integrate(sqrt(2/(1 - x)), (x, 0, Rational(3, 4)))
print('        L =', L)

p = plot(f, (x, 0, Rational(3, 4)), title='8.4.23', line_color='r')


# ---------------- 8.5.23 ----------------
# Довжина лінії x = 2(cos t + t sin t), y = 2(sin t - t cos t),  t від 0 до pi
xt = 2*(cos(t) + t*sin(t))
yt = 2*(sin(t) - t*cos(t))
dx = diff(xt, t)
dy = diff(yt, t)
print("8.5.23  x' =", simplify(dx), "   y' =", simplify(dy))
print("        x'^2 + y'^2 =", simplify(dx**2 + dy**2))     
L = integrate(2*t, (t, 0, pi))
print('        L =', L)

p = plot_parametric(xt, yt, (t, 0, pi), title='8.5.23', line_color='r', aspect_ratio=(1, 1))


# ---------------- 1.3.23 ----------------
# Усі корені кубічні з числа -216:  z^3 = -216
z = symbols('z')
korin = solve(z**3 + 216, z)
podpys = []
for w in korin:
    print('1.3.23  z =', w, '   |z| =', Abs(w), '   arg z =', arg(w))
    podpys.append({'text': '$' + latex(w) + '$', 'xy': (float(re(w)), float(im(w))),
                   'xytext': (6, 6), 'textcoords': 'offset points'})

p = plot_parametric(6*cos(t), 6*sin(t), (t, 0, 2*pi), title='1.3.23',
                    line_color='lightgray', aspect_ratio=(1, 1), annotations=podpys, show=False)
for i in range(3):
    A = korin[i]
    B = korin[(i + 1) % 3]
    AB = A + t*(B - A)                                
    p1 = plot_parametric(re(AB), im(AB), (t, 0, 1), line_color='r', show=False)
    p.extend(p1)
p.show()


# ---------------- 3.1.23 ----------------
# Ряд Фур'є: f(x) = 0 на (-pi, 0),  f(x) = 2x - 3 на [0, pi)
k = symbols('k', integer=True, positive=True)
a0 = integrate(2*x - 3, (x, 0, pi)) / pi
ak = simplify(integrate((2*x - 3)*cos(k*x), (x, 0, pi)) / pi)
bk = simplify(integrate((2*x - 3)*sin(k*x), (x, 0, pi)) / pi)
print('3.1.23  a0 =', simplify(a0))
print('        ak =', ak)
print('        bk =', bk)

N = 20                                              
S20 = a0/2 + summation(ak*cos(k*x) + bk*sin(k*x), (k, 1, N))

p = plot(S20, (x, -3*pi, 3*pi), title="3.1.23", line_color='r', show=False)
for m in [-2, 0, 2]: 
    p1 = plot(0, (x, (m - 1)*pi, m*pi), line_color='black', show=False)
    p2 = plot(2*(x - m*pi) - 3, (x, m*pi, (m + 1)*pi), line_color='black', show=False)
    p.extend(p1)
    p.extend(p2)
p.show()


# ---------------- 1.1.23 ----------------
# Сума ряду 1/((2n+3)(2n+5)), n від 1 до нескінченності
u = 1/((2*k + 3)*(2*k + 5))
print('1.1.23  u_k =', apart(u, k))
Sn = simplify(summation(u, (k, 1, n)))
print('        S_n =', Sn)
S = limit(Sn, n, oo)
print('        S = lim S_n =', S)

p = plot(Sn, Rational(1, 10), (n, 1, 30), title='1.1.23',
         ylim=(0, 0.11), axis_center=(0, 0), show=False)
p[0].line_color = 'b'
p[1].line_color = 'r'
p.show()
