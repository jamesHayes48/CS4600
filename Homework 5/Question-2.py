'''
Question 2 - Fit the data to the model found graphically
'''

import numpy as np
import matplotlib.pyplot as plt

# Load x and y from sample data
x_data = np.array([2, 4, 6, 7, 10, 11, 14, 17, 20])
y_data = np.array([4, 5, 6, 5, 8, 8, 6, 9, 12])

# Find Straight-line Least Squares Regression
# Find the sum of each for finding the slope a1
sum_yx = np.sum(y_data * x_data)
sum_x_square = np.sum(x_data ** 2)

# Find slope of the line
a_1 = sum_yx / sum_x_square

# Fit model with data
x_line = np.linspace(min(x_data), max(x_data))
y_line = a_1 * x_line

plt.figure()
plt.xlabel('x')
plt.ylabel('y')
plt.title('Scatter plot with Line of Best Fit')
plt.scatter(x_data, y_data, color='red', label='Sample data')
plt.plot(x_line, y_line, color='teal', label='Line of Best Fit')
plt.legend()
plt.show()
