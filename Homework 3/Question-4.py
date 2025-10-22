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
Q13 = Qa - Q12
Q23 = Qb + Q12
Q34 = Q23 + Q13 - Q3OUT

A = np.array([
    [Q13 + E13 + Q12, 0, -E13, 0],
    [-Q12, Q13 + E23, -E23, 0],
    [Q13, Q23, -(Q3OUT + Q34 + E13 + E34), E34],
    [0, 0, -Q34 - E34, E34 + Q34]
])

b = np.array([[Qa * ca],
              [Qb * cb],
              [0],
              [Load]
              ])

A_inv = np.linalg.inv(A)
c = np.dot(A_inv, b)

print(f"Concentrations in mg/m^3: \n {c}")

target_c2 = 20
fourth_col = A_inv[:, 3].reshape(-1, 1)
W_new = (target_c2 - c[1,0]) / fourth_col[1,0]

print(f"To reach c2 = 20 mg / m^3, Load from room 4 must be: {W_new}")