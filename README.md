# Applied Mathematics

Laboratory assignments for the **Applied Mathematics** course (Software Engineering, Taras Shevchenko National University of Kyiv), implemented in **Python**.

The labs cover linear and vector algebra, 2D and 3D plotting, animation of curves and surfaces, basic calculus, and differential equations.

## Labs

| Lab | Topic | What it does | Folder |
|-----|-------|--------------|--------|
| 1 | Linear and vector algebra | Matrix polynomials, matrix equations `A·X·B = C`, systems of linear equations (SLAE), vector operations, area and volume of a solid from its vertices (NumPy, SymPy) | [lab1](./lab1) |
| 2 | 2D graphics with Matplotlib | Bar and pie diagrams, geometric primitives and a regular polygon, implicit, parametric and polar curves, function plots | [lab2](./lab2) |
| 3 | 3D graphics with Matplotlib | Hemisphere, arrow, pyramid, ellipsoid, box and cone, prism with arrow edges, surfaces of revolution, colored surfaces, 3D bar charts, mosaic of plots | [lab3](./lab3) |
| 4 | Animation | Curve moving back and forth with color changes, animated surface of revolution, animated polar curve (`FuncAnimation`) | [lab4](./lab4) |
| 5 | Calculus basics | Areas of plane figures (Cartesian, polar, parametric), arc lengths, roots of a complex number, Fourier series, sum of a numeric series (SymPy, Matplotlib) | [lab5](./lab5) |
| 6 | Differential equations and double integrals | General and particular solutions of linear ODEs, a system of ODEs, a double integral over a region, area of a region in Cartesian and polar coordinates (SymPy, Matplotlib) | [lab6](./lab6) |

## Tech stack

- Python 3
- NumPy
- SymPy
- Matplotlib (2D, 3D, animation)

## Getting started

```bash
git clone https://github.com/timstt/applied-math.git
cd applied-math
pip install numpy sympy matplotlib
```

Run a lab from its folder, for example:

```bash
python lab4/lab4.py
```

## Author

**Tymofii Stukalo**, software engineering student.
GitHub: [@timstt](https://github.com/timstt)
