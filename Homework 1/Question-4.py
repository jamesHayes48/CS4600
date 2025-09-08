import matplotlib.pyplot as plt
import numpy as np

def function(x):
    return -12 - 21*x + 18*x**2 - 2.75*x**3

x_list = np.linspace(-2, 5)
y_list = function(x_list)

plt.plot(x_list, y_list)
plt.axhline(0, color='black')
plt.axvline(0, color='black')
plt.show()