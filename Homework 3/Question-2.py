import numpy as np
import pprint

def maxrow(avec):
    # function to determine the row index of the
    # maximum value in a vector
    maxrowind = 0
    n = len(avec)
    amax = abs(avec[0])
    for i in range(1,n):
        if abs(avec[i]) > amax:
            amax = avec[i]
            maxrowind = i
    return maxrowind


def gausspivot(A, b):
    """
    gausspivot: Gauss elimination with partial pivoting
    input:
    A = coefficient matrix
    b = constant vector
    output:
    x = solution vector
    """
    (n, m) = A.shape
    if n != m:
        return 'Coefficient matrix A must be square'
    nb = n + 1
    # build augmented matrix
    Aug = np.hstack((A, b))

    # forward elimination
    for k in range(n-1):
        # partial pivoting
        imax = maxrow(Aug[k:n, k])
        ipr = imax + k
        if ipr != k:  # no row swap if pivot is max
            for j in range(k, nb):  # swap rows k and ipr
                temp = Aug[k, j]
                Aug[k, j] = Aug[ipr, j]
                Aug[ipr, j] = temp
        for i in range(k + 1, n):
            factor = Aug[i, k] / Aug[k, k]
            Aug[i, k:nb] = Aug[i, k:nb]-factor * Aug[k, k:nb]
    # back substitution
    x = np.zeros([n, 1])  # create empty x array
    x = np.matrix(x)  # convert to matrix type
    x[n-1]=Aug[n-1, nb-1] / Aug[n-1, n-1]
    for i in range(n-2, -1, -1):
        x[i] = (Aug[i, nb-1]-Aug[i, i+1:n] * x[i+1:n, 0]) / Aug[i, i]
    return x

# Set numbers and convert between units
# Constants set here
# Given Q0
Q0 = 14 # liters/min
Q0 = Q0 / 6000 # Convert to m^3 / s

# Calculate first part of KIJ
constant = (np.pi / (8 * 24))

# Given Pressure at node 7
P7 = 200000 # Pa

# Set coefficents
# Pipe 0 - 1
R01 = 10.4 # mm
R01 /= 1000 # convert to m
L01 = 40 # cm
L01 /= 100 # convert to cm
K01 = constant * ((R01 ** 4)/L01)

# Pipe 1 - 2
R12 = 7.85 # mm
R12 /= 1000 # convert to m
L12 = 60 # cm
L12 /= 100 # convert to cm
K12 = constant * ((R12 ** 4)/L12)

# Pipe 1 - 3
R13 = 7.85 # mm
R13 /= 1000 # convert to m
L13 = 60 # cm
L13 /= 100 # convert to cm
K13 = constant * ((R13 ** 4)/L13)

# Pipe 4 - 6
R46 = 7.85 # mm
R46 /= 1000 # convert to m
L46 = 150 # cm
L46 /= 100 # convert to m
K46 = constant * ((R46 ** 4)/L46)

# Pipe 5 - 6
R56 = 7.85 # mm
R56 /= 1000 # convert to m
L56 = 100 # cm
L56 /= 100 # convert to m
K56 = constant * ((R56 ** 4)/L56)

# Pipe 6 - 7
R67 = 26.7 / 2 # mm
R67 /= 1000 # convert to m
L67 = 100 # cm
L67 /= 100 # convert to m
K67 = constant * ((R67 ** 4)/L67)

# Valve Equation Coefficients
CV24 = 2.00e-09
CV35 = 2.75e-09


# Store matrix in pattern:

# Store the coefficient matrix A
coeff_matrix_A = np.array([[0, 0, *((0.0104**4 / 0.40)), -(np.pi / (8 * 24))*((0.0104**4 / 0.40)), 0, 0, 0, 0, 0],
                         [0, 0, 0, (np.pi / (8 * 24))*((0.00785**4 / 0.50)), -(np.pi / (8 * 24))*((0.00785**4 / 0.50)), 0, 0, 0, 0],
                         [0, 0, 0, (np.pi / (8 * 24))*((0.00785**4 / 0.50)), 0 , -(np.pi / (8 * 24))*((0.00785**4 / 0.50)), 0 , 0, 0],
                         [0, 0, 0, 0, 0, 0, (np.pi / (8 * 24))*((0.00785**4 / 1.50)), 0 , -(np.pi / (8 * 24))*((0.00785**4 / 1.50))],
                         [0, 0, 0, 0, 0, 0, 0, (np.pi / (8 * 24))*((0.00785**4 / 1.00)), -(np.pi / (8 * 24))*((0.00785**4 / 1.00))],
                         [0, 0, 0, 0, 0, 0, 0, 0, (np.pi / (8 * 24))*((0.00785**4 / 0.75))],
                         [0, 0, 0, 0, 2 * (10**(-9)), 0, -2 * (10**(-9)), 0 , 0],
                         [0, 0, 0, 0, 0, 2.75 * (10 ** -9), 0, -2.75 * (10 ** -9), 0],
                         [1, 1, 0, 0, 0, 0, 0, 0, 0]])

# Store constant vector b
constant_vector_b = np.array([[2.33 * (10 ** -3)],
                     [0],
                     [0],
                     [0],
                     [0],
                     [2.33 * (10 ** -3) + (np.pi / (8 * 24))*((0.00785**4 / 0.75)) * (200000)],
                     [0],
                     [0],
                     [2.33 * (10 ** -3)]])

'''
A = np.array([[ 0.00000000e+00,  0.00000000e+00,  4.78544148e-10, -4.78544148e-10,
   0.00000000e+00,  0.00000000e+00,  0.00000000e+00,  0.00000000e+00,
   0.00000000e+00],
 [ 0.00000000e+00,  0.00000000e+00,  0.00000000e+00,  1.24267416e-10,
  -1.24267416e-10,  0.00000000e+00,  0.00000000e+00,  0.00000000e+00,
   0.00000000e+00],
 [ 0.00000000e+00,  0.00000000e+00,  0.00000000e+00,  1.24267416e-10,
   0.00000000e+00, -1.24267416e-10,  0.00000000e+00,  0.00000000e+00,
   0.00000000e+00],
 [ 0.00000000e+00,  0.00000000e+00,  0.00000000e+00,  0.00000000e+00,
   0.00000000e+00,  0.00000000e+00,  4.14224719e-11,  0.00000000e+00,
  -4.14224719e-11],
 [ 0.00000000e+00,  0.00000000e+00,  0.00000000e+00,  0.00000000e+00,
   0.00000000e+00,  0.00000000e+00,  0.00000000e+00,  6.21337078e-11,
  -6.21337078e-11],
 [ 0.00000000e+00,  0.00000000e+00,  0.00000000e+00, 0.00000000e+00,
   0.00000000e+00,  0.00000000e+00,  0.00000000e+00,  0.00000000e+00,
   8.28449438e-11],
 [ 0.00000000e+00,  0.00000000e+00,  0.00000000e+00,  0.00000000e+00,
   2.00000000e-09,  0.00000000e+00, -2.00000000e-09,  0.00000000e+00,
   0.00000000e+00],
 [ 0.00000000e+00,  0.00000000e+00,  0.00000000e+00,  0.00000000e+00,
   0.00000000e+00,  2.75000000e-09,  0.00000000e+00, -2.75000000e-09,
   0.00000000e+00],
 [ 1.00000000e+00,  1.00000000e+00,  0.00000000e+00,  0.00000000e+00,
   0.00000000e+00,  0.00000000e+00,  0.00000000e+00,  0.00000000e+00,
   0.00000000e+00]])
'''
pprint(coeff_matrix_A)
print(gausspivot(coeff_matrix_A, constant_vector_b))
