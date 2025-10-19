'''
Question 3
c. Compute LU Factorization for this system
d. Use LU Factorization to compute matrix inverse
'''

import numpy as np
from scipy.linalg import lu, solve_triangular


# Q.c - Compute LU Factorization of system:
Q1_In,Q2_In,Q3_OUT = 100, 10, 110
c1_in, c2_in = 10, 200
Q12, Q13 = 5, 117
Q21 = 22
Q32 = 7
V1, V2, V3 = 100, 50, 150
k = 0.1

A = np.array([[-(Q12 + Q13 + (k * V1)), Q21, 0],
              [Q12, -(Q21 + (k * V2)), Q32],
              [Q13, 0,  -(Q32 + Q3_OUT + (k * V3))]
              ])


b_constant = np.array([[-(Q1_In * c1_in)],
              [-(Q2_In * c2_in)],
              [0]
              ])


P, L, U = lu(A)

print(f"L = {L}")
print(f"U = {U}")

# Q.d Use LU factorization to find matrix inverse
identity_matrix = np.eye(A.shape[0])
n = A.shape[0]
A_inv = np.zeros((n,n))
for i in range(n):
    # Grab column of identity matrix
    b = identity_matrix[:, i]

    # Solve for Ld = b
    d_i = solve_triangular(L, b, lower=True)

    # Solve for Ux = d
    x_i = solve_triangular(U, d_i, lower=False)
    A_inv[:, i] = x_i

print(f"Inverse of Coefficient matrix = \n {A_inv}")

