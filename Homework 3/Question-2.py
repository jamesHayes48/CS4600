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
Q0 = Q0 / 60000 # Convert to m^3 / s

# Calculate first part of KIJ
constant = (np.pi / (8 * 24))

# Given Pressure at node 7
P7 = 200000 # Pa

# Set coefficients
# Pipe 0 - 1
R01 = 20.8 / 2 # mm
R01 /= 1000 # convert to m
L01 = 40 # cm
L01 /= 100 # convert to m
K01 = constant * ((R01 ** 4)/L01)

# Pipe 1 - 2
R12 = 15.7 / 2 # mm
R12 /= 1000 # convert to m
L12 = 60 # cm
L12 /= 100 # convert to m
K12 = constant * ((R12 ** 4)/L12)

# Pipe 1 - 3
R13 = 15.7 / 2 # mm
R13 /= 1000 # convert to m
L13 = 50 # cm
L13 /= 100 # convert to m
K13 = constant * ((R13 ** 4)/L13)

# Pipe 4 - 6
R46 = 15.7 / 2 # mm
R46 /= 1000 # convert to m
L46 = 150 # cm
L46 /= 100 # convert to m
K46 = constant * ((R46 ** 4)/L46)

# Pipe 5 - 6
R56 = 15.7 / 2 # mm
R56 /= 1000 # convert to m
L56 = 100 # cm
L56 /= 100 # convert to m
K56 = constant * ((R56 ** 4)/L56)

# Pipe 6 - 7
R67 = 26.7 / 2 # mm
R67 /= 1000 # convert to m
L67 = 75 # cm
L67 /= 100 # convert to m
K67 = constant * ((R67 ** 4)/L67)

# Valve Equation Coefficients
CV24 = 2.00e-09
CV35 = 2.75e-09

# Store the coefficient matrix A
coeff_matrix_A = np.zeros((9, 9))

# Assign Pipe Coefficients
coeff_matrix_A[0, 2], coeff_matrix_A[0, 3] = K01, -K01
coeff_matrix_A[1, 0], coeff_matrix_A[1, 3], coeff_matrix_A[1, 4] = 1, -K12, K12
coeff_matrix_A[2, 1], coeff_matrix_A[2, 3], coeff_matrix_A[2, 5] = 1, -K13, K13
coeff_matrix_A[3, 0], coeff_matrix_A[3, 6], coeff_matrix_A[3, 8] = 1, -K46, K46
coeff_matrix_A[4, 1], coeff_matrix_A[4, 7], coeff_matrix_A[4, 8] = 1, -K56, K56
coeff_matrix_A[5, 8] = K67

# Assign Valve coefficients
coeff_matrix_A[6, 4], coeff_matrix_A[6, 6] = CV24, -CV24
coeff_matrix_A[7, 5], coeff_matrix_A[7, 7] = CV35, -CV35

# Assign Flow equation coefficients
coeff_matrix_A[8,0], coeff_matrix_A[8,1] = 1, 1

# Store constant vector b
constant_vector_b = np.array([[Q0],
                     [0],
                     [0],
                     [0],
                     [0],
                     [Q0 + K67 * P7],
                     [0],
                     [0],
                     [Q0]])

answer = gausspivot(coeff_matrix_A, constant_vector_b)
print("Flows rates in m^3/s and liters/min")
print(f"Q1: {answer[0, 0]} m^3 / s, {answer[0, 0] * 60000} liters/min")
print(f"Q2: {answer[1, 0]} m^3 / s, {answer[1, 0] * 60000} liters/min")

print("Pressures in Pa and Psi")
print(f"P0: {answer[2, 0]} Pa, {answer[2, 0] / 6895} psi")
print(f"P1: {answer[3, 0]} Pa, {answer[3, 0] / 6895} psi")
print(f"P2: {answer[4, 0]} Pa, {answer[4, 0] / 6895} psi")
print(f"P3: {answer[5, 0]} Pa, {answer[5, 0] / 6895} psi")
print(f"P4: {answer[6, 0]} Pa, {answer[6, 0] / 6895} psi")
print(f"P5: {answer[7, 0]} Pa, {answer[7, 0] / 6895} psi")
print(f"P6: {answer[8, 0]} Pa, {answer[8, 0] / 6895} psi")