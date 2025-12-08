'''
Question 3 -
'''

import numpy as np
import matplotlib.pyplot as plt

x_vals = np.array([10, 20, 30, 40, 50, 60, 70, 80])
y_vals = np.array([25, 70, 380, 550, 610, 1220, 830, 1450])

x_square_vals = x_vals ** 2
sum_x_square = sum(x_vals ** 2)
sum_x_cube = sum(x_vals ** 3)
sum_x_four = sum(x_vals ** 4)

sum_x_y = sum(x_vals * y_vals)
sum_x_square_y = sum(x_square_vals * y_vals)

# Normal Equations
coeff_matrix = np.matrix([
                          [sum_x_square, sum_x_cube],
                          [sum_x_cube, sum_x_four]
                         ])

sum_x_y_matrix = np.matrix([
                        [sum_x_y],
                        [sum_x_square_y]
                    ])

b_matrix = np.linalg.solve(coeff_matrix, sum_x_y_matrix)

b1 = np.asarray(b_matrix[0][0]).item()
b2 = np.asarray(b_matrix[1][0]).item()

x_line = np.linspace(min(x_vals), max(x_vals))
y_line = (b1 * x_line) + (b2 * x_line ** 2)

plt.figure()
plt.xlabel('x')
plt.ylabel('y')
plt.title('Derived Least-Squares Fit of Model of Question 3')
plt.scatter(x_vals, y_vals, color='red', label='Sample data')
plt.plot(x_line, y_line, color='teal', label='Line of Best Fit')
plt.legend()
plt.show()
