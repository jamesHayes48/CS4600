'''
Question 6c - Implement steepest descent method in Python.
'''

import sympy as sp
import math
from sympy.physics.quantum.operatorordering import normal_ordered_form

x, y = sp.symbols('x y')

def steep_descent(f, h, starting_x, starting_y):
    # Differentiate the functions for gradient vector
    df_dx = sp.diff(f, x)
    df_dy = sp.diff(f, y)

    # Set first starting points
    x_i = starting_x
    y_i = starting_y

    substitute_dict = {x: x_i, y: y_i}

    dx_sub = df_dx.subs(substitute_dict).evalf()
    dy_sub = df_dy.subs(substitute_dict).evalf()


    # Find first norm of the gradient with starting point
    norm_gradient = abs(math.sqrt(((dx_sub ** 2) + (dy_sub ** 2))))

    opt_array = [(starting_x, starting_y)]

    while norm_gradient > 10 ** -4:
        # Substitute the points of iteration
        dx_sub = df_dx.subs((x, x_i ), (y, y_i))
        dy_sub = df_dy.subs((x, x_i ), (y, y_i))

        substitute_dict = {x: x_i, y: y_i}

        dx_sub = df_dx.subs(substitute_dict).evalf()
        dy_sub = df_dy.subs(substitute_dict).evalf()
        print(dy_sub)
        # Find new points
        x_i = x_i - (h * dx_sub)
        y_i = y_i - (h * dy_sub)

        # Find norm of the gradient to continue
        norm_gradient = abs(math.sqrt(((dx_sub ** 2) + (dy_sub ** 2))))

        # Add to optimization array
        opt_array.append((x_i, y_i))

    return opt_array


fxn = sp.sin(x) + sp.cos(y) + ((x - y)**2) / 4
step_size = 0.2
x_0 = 1
y_0 = 2
optimization =  steep_descent(fxn, step_size, x_0, y_0)
plot1 = sp.plotting.plot3d(fxn, (x, -10, 10), (y, -10, 10))
plot2 = sp.plotting.plot3d(optimization)
plot1.extend(plot2)