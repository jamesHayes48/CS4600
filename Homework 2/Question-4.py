'''
Question 4c - Implement steepest descent method in Python.
Print its contour and path of optimization
'''

import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
import math

x, y = sp.symbols('x y')

def steep_descent(f, h, starting_x, starting_y):
    # Differentiate the functions for gradient vector
    df_dx = sp.diff(f, x)
    df_dy = sp.diff(f, y)

    # Set first starting points to x_i
    x_i = starting_x
    y_i = starting_y

    # Store norm_gradient
    norm_gradient = 100

    # Store starting points
    x_array = [starting_x]
    y_array = [starting_y]

    # Store number of iterations
    num_itr = 0

    while norm_gradient > 10 ** -4:
        # Substitute the points of iteration
        substitute_dict = {x: x_i, y: y_i}
        dx_sub = df_dx.subs(substitute_dict).evalf()
        dy_sub = df_dy.subs(substitute_dict).evalf()

        # Find new points
        x_i = x_i - (h * dx_sub)
        y_i = y_i - (h * dy_sub)

        # Find norm of the gradient to continue
        norm_gradient = math.sqrt(((dx_sub ** 2) + (dy_sub ** 2)))

        # Add x to x_array
        # Add y to y_array
        x_array.append(x_i)
        y_array.append(y_i)
        num_itr += 1

    print(f"Number of Iterations: {num_itr}")
    return x_array, y_array


# Symbolic function for sympy and numeric for numpy
fxn_sym = sp.sin(x) + sp.cos(y) + ((x - y)**2) / 4
fxn_num = sp.lambdify((x,y), fxn_sym, 'numpy')

# Define step size and starting points
step_size = 0.2
x_0 = 1
y_0 = 2

# Find optimization path, store them into arrays for x and y
opt_x, opt_y =  steep_descent(fxn_sym, step_size, x_0, y_0)

# Plots for contour graph of function
x_list = np.linspace(-2, 8, 100)
y_list = np.linspace(-2, 8, 100)

X,Y = np.meshgrid(x_list, y_list)
Z = fxn_num(X, Y)

#
fig, ax = plt.subplots(figsize=(9,7))

# Plot contour of f(x,y)
plt.contour(X,Y,Z)

# Plot path of optimization in red
ax.plot(opt_x, opt_y, color='red')


ax.set_xlabel('x')
ax.set_ylabel('y')
plt.show()
