'''
Question 4
b. Find matrix inverse and use it to calculate concentrations in the room
'''

import numpy as np
from scipy.linalg import lu, solve_triangular

Qa = 150 # m^3 / hr
ca = 1 # mg / m^3
Qb = 50 # m^3 / hr
cb = 40 # mg / m^3
Qc = 50 # m^3 / hr
Q12 = 50 # m^3 / hr
Q13 = 50 # m^3 / hr
Q23 = 50 # m^3 / hr
Q34 = 90 # m^3 / hr
Load = 5000 # mg / hr

A = np.array([[Q12 + Q13, 0 , Q13, 0],
            [-(Q12), Q23, Q23, 0],
            [-Q13, -Q23, -(Q23 - Q13 + Q34), -Q34],
            []
              ])