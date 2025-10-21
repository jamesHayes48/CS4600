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
Q12 = 50 # m^3 / hr
E13 = 50 # m^3 / hr
E23 = 50 # m^3 / hr
Q3OUT = 50 # m^3 / hr
E34 = 90 # m^3 / hr
Load = 5000 # mg / hr

A = np.array([
    [(Q12 + E13 + Qa), 0, -E13, 0],
    [-Q12, (Qb + Q12 + E23), -E23, 0],
    [(Qa + E13), (Qb + Q12 + E23), -(Q3OUT + Qb + Q12 + Qa + E13 + E23 + E34), E34],
    [0, 0, -(Qb + Q12 + Qa + E34), (Qb + Q12 + Qa + E34)]
])

b = np.array([[Qa * ca],
              [Qb * cb],
              [0],
              [Load]
              ])

A_inv = np.linalg.inv(A)

print(f"Answer: \n {np.dot(A_inv, b)}")
