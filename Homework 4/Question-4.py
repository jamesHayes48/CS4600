'''
Question-4
'''

import numpy as np
from unicodedata import normalize


def small_eigenvalue_power(A, init_input, relative_limit):
    A_inv = np.linalg.inv(A)
    x = init_input
    relative_error = 100
    iter_count = 0
    eigen_val = 0

    while relative_error > relative_limit:
        prev_eigen = eigen_val
        A_inv_x = np.dot(A_inv, x)
        x = A_inv_x / np.linalg.norm(A_inv_x)
        eigen_val = np.dot(np.dot(A, x), x) / np.dot(x, x)

        if iter_count != 0:
            relative_error = relative_error = abs((eigen_val - prev_eigen) / eigen_val)
            print(f"Iteration {iter_count}: \n"
                  f"smallest eigenvalue: {eigen_val} \n"
                  f"eigenvector: {x} \n"
                  f"relative error: {relative_error} \n")
        else:
            print(f"Iteration {iter_count}: \n"
                  f"smallest eigenvalue: {eigen_val} \n"
                  f"eigenvector: {x} \n")
        iter_count += 1


# 4a finding eigenvalues with characteristic polynomial
coefficients_char_poly = [-1, 41, -499, 1744]
eigenvalues = np.roots(coefficients_char_poly)
print(eigenvalues)

# 4c Find the smallest eigenvalue with power method
symm_matrix = np.array([
                        [20, 3, 2],
                        [3, 9, 4],
                        [2, 4, 12]
                       ])
first_input = np.array([1, 1, 1])
error_limit = 10 ** -7

small_eigenvalue_power(symm_matrix, first_input, error_limit)