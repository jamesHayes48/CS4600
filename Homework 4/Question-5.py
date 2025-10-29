'''
Question 5b -  Find eigenvalues for matrix A
'''

import numpy as np

A = np.array([
    [-200, 0, 0],
    [200, -200, 0],
    [0, 200, -200]
])

eigenvalues = np.linalg.eigvals(A)

print(f"Eigenvalues: {eigenvalues}")