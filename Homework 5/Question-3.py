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

sum_matrix = np.matrix([
                        [sum_x_y],
                        [sum_x_square_y]
                    ])

