import matplotlib.pyplot as plt
import numpy as np

def function(x):
    return x**3 - 6*x**2 + 11*x -6.1


# a. Graph the function over [0,5]
x_list = np.linspace(0, 5)
y_list = function(x_list)

plt.plot(x_list, y_list)
plt.axhline(0, color='black')
plt.axvline(0, color='black')
plt.show()
