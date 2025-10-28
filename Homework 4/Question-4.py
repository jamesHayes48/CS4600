'''
Question-4
'''

import numpy as np

# 4a finding eigenvalues with characteristic polynomial
coefficients_char_poly = [-1, 41, -499, 1744]

eigenvalues = np.roots(coefficients_char_poly)

print(eigenvalues)