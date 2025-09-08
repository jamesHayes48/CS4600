import matplotlib.pyplot as plt
import numpy as np

def function(x):
    return -12 - 21*x + 18*x**2 - 2.75*x**3

def bisection_method(f, num_iter, lower_limit, upper_limit):
    interval = [lower_limit, upper_limit]

    for n in range(num_iter):
        midpoint = (interval[0] + interval[1]) / 2
        func_midpoint = f(midpoint)

        decide = f(interval[0]) * f(interval[1])

        if decide < 0:
            interval[0] = midpoint
        elif decide > 0:
            interval[1] = midpoint


x_list = np.linspace(-2, 5)
y_list = function(x_list)

plt.plot(x_list, y_list)
plt.axhline(0, color='black')
plt.axvline(0, color='black')
plt.show()