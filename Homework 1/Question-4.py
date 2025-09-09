import matplotlib.pyplot as plt
import numpy as np

def function(x):
    return -12 - 21*x + 18*x**2 - 2.75*x**3


def bisection_method(f, num_iter, lower_limit, upper_limit):
    interval = [lower_limit, upper_limit]
    midpoint = 0
    old_midpoint = 0

    for n in range(num_iter):
        midpoint = (interval[0] + interval[1]) / 2
        x_l, x_u = interval[0], interval[1]
        func_midpoint = f(midpoint)

        error_midpoint = abs((midpoint - old_midpoint) / midpoint) * 100

        decide = f(interval[0]) * func_midpoint

        if decide < 0:
            interval[1] = midpoint
        elif decide > 0:
            interval[0] = midpoint

        print(f"{n}: x_{n} = {midpoint} f(x_r) = {func_midpoint} f(x_l) * f(x_{n}) = {decide} "
              f"new interval: {interval} Error = {error_midpoint}%")
        old_midpoint = midpoint

def false_position(f, num_iter, lower_limit, upper_limit):
    interval = [lower_limit, upper_limit]
    old_midpoint = 0

    for n in range(num_iter):
        x_r = ((f(interval[0])*interval[1] - f(interval[1])*interval[0]) /
               (f(interval[0]) - f(interval[1])))
        function_x_r = f(x_r)

        error_midpoint = abs((x_r - old_midpoint) / x_r) * 100

        if function_x_r < 0:
            interval[0] = x_r
        elif function_x_r > 0:
            interval[1] = x_r
        print(f"x_{n} = {x_r} f(x_r) = {function_x_r} new_interval: {interval} Error = {error_midpoint}")
        old_midpoint = x_r

x_list = np.linspace(-2, 5)
y_list = function(x_list)

plt.plot(x_list, y_list)
plt.axhline(0, color='black')
plt.axvline(0, color='black')
plt.show()

# Run the bisection and false-position method 20 times
print("Bisection Method: ")
bisection_method(function, num_iter=20, lower_limit=-1, upper_limit=0)

print("\nFalse-Position Method: ")
false_position(function, num_iter=20, lower_limit=-1, upper_limit=0)
