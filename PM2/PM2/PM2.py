import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# =====================================================================
# ЗАВДАННЯ 1: Побудова діаграм з кількістю елементів (Варіант 23)
# =====================================================================
def task_1():
    plt.figure(figsize=(10, 5))
    groups = np.arange(28)
    d1, d2, d3, d4 = np.random.randint(1, 10, (4, 28))
    
    plt.bar(groups, d1, color='red', label='Секція 1')
    plt.bar(groups, d2, bottom=d1, color='blue', label='Секція 2')
    plt.bar(groups, d3, bottom=d1+d2, color='green', label='Секція 3')
    plt.bar(groups, d4, bottom=d1+d2+d3, color='orange', label='Секція 4')
    
    plt.title('1. Стовпчаста діаграма (28 груп)')
    plt.xlabel('Вісь X (Групи)')
    plt.ylabel('Вісь Y (Значення)')
    plt.legend()

    plt.figure(figsize=(8, 8))
    sizes = np.random.randint(10, 50, 28)
   
    explode = []
    for i in range(28):
        if i % 3 == 0:
            explode.append(0.1)
        else:
            explode.append(0)
            
    my_labels = []
    for i in range(28):
        my_labels.append("С" + str(i))
        
    plt.pie(sizes, explode=explode, labels=my_labels, autopct='%1.1f%%')
    plt.title('2. Кругова діаграма (28 секторів)')

    plt.figure(figsize=(10, 5))
    markers = ['o', 's', '^', 'D', 'x', 'v', 'p', '*']
    for i in range(0, 73, 10):
        chunk = min(10, 73 - i)
        
        group_number = str((i // 10) + 1)
        my_label = 'Група точок ' + group_number
        
        plt.scatter(np.random.rand(chunk), np.random.rand(chunk),
                    marker=markers[i//10], s=60, label=my_label)
    
    plt.title('3. Діаграма розкиду (73 точки)')
    plt.xlabel('Вісь X')
    plt.ylabel('Вісь Y')
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()

# =====================================================================
# ЗАВДАННЯ 2: Графічні примітиви та кольоровий 23-кутник
# =====================================================================
def task_2():
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.set_xlim(-10, 10)
    ax.set_ylim(-10, 10)
    ax.set_title('Завдання 2: Примітиви та 23-кутник')

    ax.add_patch(patches.Wedge((-5, 5), 2, 0, 180, color='cyan'))
    ax.add_patch(patches.FancyArrowPatch((-5, 2), (-2, 2), arrowstyle='->', color='red', mutation_scale=20))
    ax.add_patch(patches.Polygon([(-5,-2), (-3,-2), (-4,0)], color='green'))
    ax.add_patch(patches.Wedge((-5, -6), 2, 30, 90, color='orange'))
    ax.add_patch(patches.Polygon([(2,5), (4,7), (6,5), (4,3)], color='purple'))
    ax.add_patch(patches.Rectangle((2, 0), 4, 2, color='brown'))

    angles = np.linspace(0, 2*np.pi, 24)
    
    verts = []
    for a in angles[:23]:
        verts.append((4 + 3*np.cos(a), -5 + 3*np.sin(a)))
        
    ax.add_patch(patches.Polygon(verts, closed=True, facecolor='skyblue', edgecolor='none', zorder=1))
    
    for i in range(23):
     p1 = verts[i]
     p2 = verts[(i + 1) % 23]
     ax.add_patch(patches.FancyArrowPatch(p1, p2, arrowstyle='->', color='blue', mutation_scale=15, zorder=2))
        
    ax.text(4, -5, '23-кутник\nІПЗ-21', ha='center', va='center', zorder=3, fontweight='bold')

# =====================================================================
# ЗАВДАННЯ 3: ВАРІАНТ 23 (Криві та перетин графіків функцій)
# =====================================================================
def task_3():
    # --- 3.1 Неявна та параметрична криві ---
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    
    # a) Неявна крива
    x, y = np.meshgrid(np.linspace(-10, 10, 200), np.linspace(0.1, 10, 200)) 
    Z = 3 * y * np.log(y) - (x**2) * (y + 5)
    ax1.contour(x, y, Z, levels=[0], colors='blue')
    
    ax1.text(0, 2, '3y * ln(y) = x^2 * (y + 5)', color='blue', fontsize=12, ha='center', bbox=dict(facecolor='white', alpha=0.8))
    
    ax1.set_title('a) Неявна крива')
    ax1.set_xlabel('Вісь X'); ax1.set_ylabel('Вісь Y')

    # б) Параметрична крива
    t = np.linspace(-10, 10, 400)
    x_param = np.arcsin(t / (1 + t**2))
    y_param = np.arccos(1 / np.sqrt(1 + t**2))
    ax2.plot(x_param, y_param, color='red')
    
    param_text = 'x = arcsin(t / (1 + t^2))\ny = arccos(1 / sqrt(1 + t^2))'
    ax2.text(0, 0.5, param_text, color='red', fontsize=10, ha='center')
    
    ax2.set_title('б) Параметрична крива')
    ax2.set_xlabel('Вісь X'); ax2.set_ylabel('Вісь Y')

    # --- 3.2 Полярна крива ---
    plt.figure()
    ax = plt.subplot(111, projection='polar')
    phi = np.linspace(0, 2*np.pi, 200)
    rho = 1 / (1 - (1/3)*np.cos(phi)) 
    
    ax.plot(phi, rho, color='purple', label='rho = 1 / (1 - 1/3 * cos(phi))')
    
    ax.set_title('Полярна крива', pad=15)
    ax.legend(loc='upper right')

    # --- 3.3 Кольорова крива y^2+6y+5=0 ---
    plt.figure(figsize=(8, 4))
    x_c = np.linspace(-10, 10, 100)
    plt.plot(x_c[:33], np.full(33, -1), color='red', lw=3)
    plt.plot(x_c[33:66], np.full(33, -1), color='green', lw=3)
    plt.plot(x_c[66:], np.full(34, -1), color='blue', lw=3)
    plt.plot(x_c[:33], np.full(33, -5), color='blue', lw=3)
    plt.plot(x_c[33:66], np.full(33, -5), color='red', lw=3)
    plt.plot(x_c[66:], np.full(34, -5), color='green', lw=3)
    
    plt.text(0, -3, 'y^2 + 6y + 5 = 0', rotation=33, fontsize=14, ha='center', bbox=dict(facecolor='white', alpha=0.7, edgecolor='none'))
    
    plt.title('Кольорова крива')
    plt.xlabel('Вісь X'); plt.ylabel('Вісь Y')

    # --- 3.4 Функції f(x) та g(x) ---
    x_f = np.linspace(-2, 6, 10000)
    f_x = (x_f**2 - 1) / (x_f - 3)
    g_x = 9**(x_f + 1)

    x_z = np.linspace(3.0005, 3.002, 5000)
    diff = (x_z**2 - 1) / (x_z - 3) - 9**(x_z + 1)
    xi = x_z[np.argmin(np.abs(diff))]
    yi = 9**(xi + 1)

    fig2, (a1, a2, a3) = plt.subplots(3, 1, figsize=(8, 14))

    a1.plot(x_f, f_x, color='green', lw=1.5, label=r'$f(x)=\frac{x^2-1}{x-3}$')
    a1.set_ylim(-20, 20)
    a1.set_title('Графік f(x)')

    a2.plot(x_f, g_x, color='red', lw=3, label=r'$g(x)=9^{x+1}$')
    a2.set_ylim(-10, 1000)
    a2.set_title('Графік g(x)')

    a3.plot(x_f, f_x, color='green', lw=1.5, label=r'$f(x)=\frac{x^2-1}{x-3}$')
    a3.plot(x_f, g_x, color='red', lw=3, label=r'$g(x)=9^{x+1}$')
    a3.plot([], [], 'mo', label=f'Є перетин: ({xi:.4f}; {yi:.0f}), за межами графіка')
    a3.set_ylim(-10, 30)
    a3.set_title('Спільний графік')

    for axis in (a1, a2, a3):
        axis.set_xlabel('Вісь X')
        axis.set_ylabel('Вісь Y')
        axis.axhline(0, color='black', lw=1.5)
        axis.axvline(0, color='black', lw=1.5)
        axis.grid(True)
        axis.legend()

    plt.tight_layout(h_pad=3)

# =====================================================================
if __name__ == "__main__":
    task_1()
    task_2()
    task_3()
    plt.show()