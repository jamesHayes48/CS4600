'''
Question 2b: Perform bisection method with 17 iterations on function x**2 - 2
'''


import math

# function to estimate root
def function(x):
    return x**2 - 2


# Bisection method that takes function f, number of iterations to run and
# lower limit, upper limit to bracket root.
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

        print(f"Iteration {n + 1}: x_{n+1} = {midpoint} f(x_r) = {func_midpoint} f(x_l) * f(x_{n}) = {decide} "
              f"new interval: {interval} {'' if n==0 else f"Error = {error_midpoint}%"}")
        old_midpoint = midpoint

# 2b. Run bisection method 17 times
bisection_method(function, num_iter=17, lower_limit=1, upper_limit=2)
