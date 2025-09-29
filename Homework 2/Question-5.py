'''
Question 5d - Use simplex method to find optimal values of x_1 and x_2
'''

from scipy.optimize import linprog
import numpy as np

# 3x_1 + 2x_2 = Z
# Z = -3x_1 -2x_2
object_func = np.array([3, 2])
object_func *= -1

# Time: x_1 + 2x_2 = 6
# Raw Material: 2x_1 + x_2 = 6
ineq_equation = [[1, 2], [2, 1]]
rhs = [6, 6]

# Set bounds for x_1, x_2 > 0
x1_bnds = (0, None)
x2_bnds = (0, None)

# Find the optimal values for x_1 and x_2 using simplex method
res = linprog(object_func, ineq_equation, rhs, bounds=[x1_bnds, x2_bnds], method="simplex")
print(res)
