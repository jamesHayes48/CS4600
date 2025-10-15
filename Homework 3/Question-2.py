import numpy as np

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


# Store the coefficient matrix A
coeff_matrix_A = np.array([[0, 0, (np.pi / (8 * 24))*((0.0104**4 / 0.40)), -(np.pi / (8 * 24))*((0.0104**4 / 0.40)), 0, 0, 0, 0, 0],
                         [0, 0, 0, (np.pi / (8 * 24))*((0.00785**4 / 0.50)), -(np.pi / (8 * 24))*((0.00785**4 / 0.50)), 0, 0, 0, 0],
                         [0, 0, 0, (np.pi / (8 * 24))*((0.00785**4 / 0.50)), 0 , -(np.pi / (8 * 24))*((0.00785**4 / 0.50)), 0 , 0, 0],
                         [0, 0, 0, 0, 0, 0, (np.pi / (8 * 24))*((0.00785**4 / 1.50)), 0 , -(np.pi / (8 * 24))*((0.00785**4 / 1.50))],
                         [0, 0, 0, 0, 0, 0, 0, (np.pi / (8 * 24))*((0.00785**4 / 1.00)), -(np.pi / (8 * 24))*((0.00785**4 / 1.00))],
                         [0, 0, 0, 0, 0, 0, 0, 0, (np.pi / (8 * 24))*((0.00785**4 / 0.75))],
                         [0, 0, 0, 0, 2 * (10**(-9)), 0 , -2 * (10**(-9)), 0 , 0],
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

print(gausspivot(coeff_matrix_A, constant_vector_b))
