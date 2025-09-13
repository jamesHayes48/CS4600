import matplotlib.pyplot as plt
import numpy as np
import sympy as sp


x = sp.symbols('x')
def function(x):
    return x**3 - 6*x**2 + 11*x - 6.1


def newton_method(f, starting_point):
    # Get symbolic derivative of f
    x_r = starting_point
    deriv_f = sp.diff(function(x))

    # Initialize starting values
    count = 0
    error_calc = 100
    prev_value = 0

    # Run through Newton-Raphson method until error is below 10^-6
    while error_calc > 10**-6:
        prev_value = x_r
        x_r = x_r - (f(x_r)) / (deriv_f.subs({x: x_r}))
        count += 1
        error_calc = abs((x_r - prev_value) / x_r)

    # Print information with final approximation
    print(f"Final Approximation: {x_r} Initial Guess: {starting_point} "
          f"Number of Iterations: {count} Final Error Calculation: {error_calc * 100}%")


# a. Graph the function over [0,5]
x_list = np.linspace(0, 5)
y_list = function(x_list)

plt.plot(x_list, y_list)
plt.axhline(0, color='black')
plt.axvline(0, color='black')
plt.show()

# d. Find real roots with guesses with Newton Method
newton_method(function, 3.5)
newton_method(function, 2)
newton_method(function, 1)