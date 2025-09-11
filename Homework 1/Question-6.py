import matplotlib.pyplot as plt
import numpy as np
import sympy as sp


x = sp.symbols('x')
def function(x):
    return x**3 - 6*x**2 + 11*x -6.1


def newton_method(f, starting_point, num_iter):
    fxn = x**3 - 6*x**2 + 11*x - 6.1

    # Get derivative of f
    deriv_f = sp.Derivative(fxn, x).doit()
    print(type(deriv_f))



# a. Graph the function over [0,5]
x_list = np.linspace(0, 5)
y_list = function(x_list)

plt.plot(x_list, y_list)
plt.axhline(0, color='black')
plt.axvline(0, color='black')
plt.show()

# c. Find real root with Newton Method
newton_method(function, 3.5, 3)