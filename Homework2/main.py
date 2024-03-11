import numpy as np

epsilon = 10 ** -5


# descompunere LU
def is_lu_decomposable(A):
    n = A.shape[0]
    for i in range(n):
        if np.linalg.det(A[:i + 1, :i + 1]) == 0:
            return False
    return True


def crout_decomposition(A):
    if is_lu_decomposable(A):
        size = len(A)
        lu = np.ones((size, size))
        for i in range(size):
            for p in range(i + 1):
                if i == p:
                    lu[i][p] = (A[p][i] - np.sum([lu[p][k] * lu[k][i] for k in range(p)])) / lu[p][p]
                else:
                    if abs(lu[p][p]) <= epsilon:
                        print("Division by 0 at compute elem. col. p U, (" + str(p), str(p) + ")")
                        return None
                    lu[p][i] = (A[p][i] - np.sum([lu[p][k] * lu[k][i] for k in range(p)])) / lu[p][p]
                    lu[i][p] = A[i][p] - np.sum([lu[i][k] if k == p else lu[i][k] * lu[k][p] for k in range(p)])
        matrice_lu = np.array(lu)
        return matrice_lu


def extract_lu_components(lu):
    size = lu.shape[0]
    L = np.zeros((size, size))
    U = np.zeros((size, size))
    for i in range(size):
        for j in range(size):
            if i == j:
                U[i, j] = 1
                L[i, j] = lu[i, j]
            elif i > j:
                L[i, j] = lu[i, j]
            else:
                U[i, j] = lu[i, j]
    return L, U



# determinantul matricei
def determinant_LU(L, U):
    det_L = np.prod(np.diag(L))
    det_U = np.prod(np.diag(U))
    return det_L * det_U



# rezolvare sistem
def forward_substitution(L, b):
    n = L.shape[0]
    y = np.zeros(n)
    for i in range(n):
        y[i] = (b[i] - np.dot(L[i, :i], y[:i])) / L[i, i]
    return y


def backward_substitution(U, y):
    n = U.shape[0]
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = (y[i] - np.dot(U[i, i + 1:], x[i + 1:])) / U[i, i]
    return x



# generare si rezolvare matrici 100
def generate_and_solve(n=100):
    A = np.random.rand(n, n)
    b = np.random.rand(n)

    x = np.linalg.solve(A, b)

    mat = crout_decomposition(A)
    L, U = extract_lu_components(mat)
    y = forward_substitution(L, b)
    x_LU = backward_substitution(U, y)

    return np.linalg.norm(x_LU - x)


# initializare
# A = np.array([[2, -1, 0], [-1, 2, -1], [0, -1, 2]])
# b = np.array([1, 0, 1])
# A_init = np.array([[2, -1, 0], [-1, 2, -1], [0, -1, 2]])
# b_init = np.array([1, 0, 1])

# A = np.array([[2.5, 2, 2], [5, 6, 5], [5, 6, 6.5]])
# b = np.array([2, 2, 2])
# A_init = np.array([[2.5, 2, 2], [5, 6, 5], [5, 6, 6.5]])
# b_init = np.array([2, 2, 2])

A = np.array([[1, 2, 1, 1], [1, 4, -1 , 7], [4, 9 , 5, 11], [1, 0, 6, 4]])
b = np.array([0, 20, 18, 1])
A_init = np.array([[1, 2, 1, 1], [1, 4, -1 , 7], [4, 9 , 5, 11], [1, 0, 6, 4]])
b_init = np.array([0, 20, 18, 1])

# decompunere
matrice_lu = crout_decomposition(A)
print("Matricea LU")
print(matrice_lu)
L, U = extract_lu_components(matrice_lu)
print("\nMatrix L:")
print(L)
print("\nMatrix U:")
print(U)

# determinant
det_A = determinant_LU(L, U)
print("\nDeterminant of matrix A:", det_A, "\n")

# solutie sistem
y = forward_substitution(L, b)
x = backward_substitution(U, y)
print("The solution to the system Ax = b is: ", x, "\n")

# norma euclidiana
norm = np.linalg.norm(np.dot(A_init, x) - b_init)
print("The Euclidean norm of the difference is: {0:.16f}".format(norm))

# solutie sistem cu numpy vs lu
x_lib = np.linalg.solve(A, b)
print("\nThe solution to the system Ax = b using numpy is:")
print(x_lib)

print("\nThe solution to the system Ax = b using LU decomposition is:")
print(x)

# inversea matricii
A_inv_lib = np.linalg.inv(A)
print("\nThe inverse of the matrix A using numpy is:")
print(A_inv_lib)

# norme
norm1 = np.linalg.norm(x - x_lib)
norm2 = np.linalg.norm(x - np.dot(A_inv_lib, b))
print("\nThe norm ||xLU - xlib||2 is: {0:.16f}".format(norm1))
print("The norm ||xLU - A^-1lib binit||2 is: {0:.16f}".format(norm2))

# generare si rezolvare matrici 100
print("\nThe norm ||xLU - xlib||2 is: {0:.16f}".format(generate_and_solve(100)))
norm = generate_and_solve(100)
is_smaller = norm < 10 ** (-8)
print("The norm value is smaller than 10 ^ (-9): ", is_smaller)
