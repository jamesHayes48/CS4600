'''
Question 4a: Visually estimate location of real root of function -12 - 21*x + 18*x**2 - 2.75*x**3

Question 4b: Numerically approximate leftmost real root of function with bisection method and
false-position. Run them with 17 iterations.
'''


import matplotlib.pyplot as plt
import numpy as np

# Function to run bisection and false-position method with
def function(x):
    return -12 - 21*x + 18*x**2 - 2.75*x**3


# Bisection method that takes function f, upper limit, and lower limit to bracket root.
def bisection_method(f, lower_limit, upper_limit):
    interval = [lower_limit, upper_limit]
    midpoint = 0
    old_midpoint = 0

    # Run bisection method for 20 iterations
    for n in range(20):
        midpoint = (interval[0] + interval[1]) / 2
        x_l, x_u = interval[0], interval[1]
        func_midpoint = f(midpoint)

        error_midpoint = abs((midpoint - old_midpoint) / midpoint) * 100

        # Change Interval based on sign of f(x_n) * f(x_r)
        decide = f(interval[0]) * func_midpoint
        if decide < 0:
            interval[1] = midpoint
        elif decide > 0:
            interval[0] = midpoint

        print(f"Iteration {n+1}: x_{n+1} = {midpoint} f(x_{n+1}) = {func_midpoint} f(x_l) * f(x_{n}) = {decide} "
              f"new interval: {interval} {'' if n==0 else f"Error = {error_midpoint}%"}")
        old_midpoint = midpoint


# False-position method that takes function f, lower limit and upper limit to bracket root.
def false_position(f, lower_limit, upper_limit):
    interval = [lower_limit, upper_limit]
    old_midpoint = 0

    # Run false-position method for 20 iterations
    for n in range(20):
        f_l = f(interval[0])
        f_u = f(interval[1])
        x_r = ((f_l*interval[1] - f_u*interval[0]) /
               (f_l - f_u))
        function_x_r = f(x_r)

        error_midpoint = abs((x_r - old_midpoint) / x_r) * 100

        # Change interval based on f(x_r)
        if function_x_r < 0:
            interval[0] = x_r
        elif function_x_r > 0:
            interval[1] = x_r

        print(f"Iteration {n+1}: x_{n+1} = {x_r} f(x_{n+1}) = {function_x_r} new_interval: {interval} "
              f"{'' if n==0 else f"Error = {error_midpoint}%"}")
        old_midpoint = x_r


# a. Graphical Estimation
# Graph the plot to visually estimate location of real roots.
x_list = np.linspace(-2, 5)
y_list = function(x_list)

plt.plot(x_list, y_list)
plt.axhline(0, color='black')
plt.axvline(0, color='black')
plt.show()

# b. Numerical root-finding
# Run the bisection and false-position method 20 times.
print("Bisection Method: ")
bisection_method(function, lower_limit=-1, upper_limit=0)

print("\nFalse-Position Method: ")
false_position(function, lower_limit=-1, upper_limit=0)
