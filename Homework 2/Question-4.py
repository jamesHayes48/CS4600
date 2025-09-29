'''
Question 6c - Implement steepest descent method in Python.
'''

import sympy as sp

x, y = sp.symbols('x y')

def steep_descent(f, h):
    df_dx = sp.diff(f, x)
    df_dy = sp.diff(f, y)
    norm_gradient = 0

    while abs()
    dx_sub = df_dx.subs(x: )


fxn = sp.sin(x) + sp.cos(y) + ((x - y)**2) / 4
step_size = 0.2
steep_descent(fxn, step_size)