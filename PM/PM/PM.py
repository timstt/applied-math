import numpy as np
import sympy as sp

def task_1():
    print("Завдання 1: Знайти f(A)")
    print("якщо A = (2 -3 | 4 5), f(x)=(x^2-2x)(2x-1)")
    
    a1 = np.array([[2, -3], 
                   [4, 5]])

    part1 = (np.dot(a1, a1) - (2 * a1))
    part2 = (2 * a1 - np.eye(2))
    result1 = np.dot(part1, part2)
    
    print("Результат:")
    print(result1)
    print("\n")


def task_2():
    print("Завдання 2: Розв’яжіть матричне рівняння")
    print("A * X * B = C")
    
    a = np.array([[1, 2], 
                  [-3, -5]])
    b = np.array([[1, 3],
                  [-1, -2]])
    c = np.array([[2, 4],
                  [-6, -11]])

    interim = np.dot(np.linalg.inv(a), c) 
    x = np.dot(interim, np.linalg.inv(b)) 
    print("Результат (Матриця X):")
    print(x)
    print("\n")


def task_3():
    print("Завдання 3: Дослідіть СЛАР та знайдіть розв'язок")
    
    A = np.array([[1, -2, 3, -4],
                  [0, 1, -1, 1],
                  [1, 3, 0, -3],
                  [0, -7, 3, 1]])

    B = np.array([[4],
                  [-3],
                  [1],
                  [-3]])

    AB = np.hstack((A, B))

    rank_A = np.linalg.matrix_rank(A)
    rank_AB = np.linalg.matrix_rank(AB)

    print("\nРанг основної матриці -", rank_A)
    print("Ранг розширеної матриці -", rank_AB)
    if rank_A == rank_AB:
        print("Система сумісна")
        
        solution = sp.linsolve((sp.Matrix(A), sp.Matrix(B)))
        
        print("Розв'язок: ", solution)
        
    else:
        print("Система не сумісна")

def task_4():
    print("Завдання 4: Обчислити")

    a, b = sp.symbols('a b')
    expression = (a + b) * (a - 2 * b)
    expander_expr = sp.expand(expression)

    a_mag = 3
    b_mag = 4
    angle = np.pi / 3

    dot_product = a_mag * b_mag * np.cos(angle)

    result = expander_expr.subs({a**2: a_mag**2, b**2: b_mag**2, a*b: dot_product})

    print("\nРозкриття дужок: ", expander_expr)
    print("Результат обчислення: ",int(result))


    a_magnitube = 3
    b_magnitube = 4
    phi = np.pi / 3

    a_dot_b = a_magnitube * b_magnitube * np.cos(phi)
    
    a3_squared = 9 * (a_magnitube ** 2)
    b1_squared = 1 * (b_magnitube ** 2)

    result_b_squared = a3_squared + 6 * a_dot_b + b1_squared
    result_b = np.sqrt(result_b_squared)

    print("\nРезультат обчислення: ", np.round(result_b, decimals=10))

def task_5():
    print("Завдання 5: Обчисліть площу грані і об’єм , вершини якої містяться в точках: ")

    A = np.array([-2, -4, 0])
    B = np.array([4, -3, -1])
    C = np.array([3, -2, 0])
    D = np.array([2, -1, 5])

    AB = B - A
    AC = C - A

    cross_product = np.cross(AB, AC)

    area = 0.5 * np.linalg.norm(cross_product)

    AD = D - A

    volume = abs(np.dot(AD, cross_product)) / 6.0

    print(f"Площа грані ABC: {area}")
    print(f"Об'єм піраміди: {volume}")


if __name__ == "__main__":
    task_1()
    task_2()
    task_3()
    task_4()
    task_5()