import warnings

warnings.filterwarnings("ignore", category=DeprecationWarning)
import math
import numpy as np

eps = 10 ** -6


# ex1
def calculate_b(A, s):
    n = len(s)
    b = np.zeros(n)

    for i in range(n):
        for j in range(n):
            b[i] += s[j] * A[i][j]

    return b


# ex2
def QR_householder(A, b):
    n = len(b)
    q = np.zeros((n, n))
    for i in range(0, n):
        q[i, i] = 1
    for r in range(0, n - 1):
        sigma = 0
        for i in range(r, n):
            sigma = sigma + A[i, r] ** 2
        if sigma <= eps:
            break
        k = np.sqrt(sigma)
        if A[r, r] > 0:
            k = -k
        beta = sigma - k * A[r, r]
        u = np.zeros((n, 1))
        u[r] = A[r, r] - k
        for i in range(r + 1, n):
            u[i] = A[i, r]
        for j in range(r + 1, n):
            sum = 0
            for i in range(r, n):
                sum = sum + u[i] * A[i, j]
            teta = sum / beta
            for i in range(r, n):
                A[i, j] = A[i, j] - teta * u[i]
        A[r, r] = k
        for i in range(r + 1, n):
            A[i, r] = 0
        sum = 0
        for i in range(r, n):
            sum = sum + u[i] * b[i]
        teta = sum / beta
        for i in range(r, n):
            b[i] = b[i] - teta * u[i]
        for j in range(0, n):
            sum = 0
            for i in range(r, n):
                sum = sum + u[i] * q[i, j]
            teta = sum / beta
            for i in range(r, n):
                q[i, j] = q[i, j] - teta * u[i]
    return q


# ex3
def solve_system_QR(A, b):
    Q, R = np.linalg.qr(A)
    x = np.linalg.solve(np.dot(Q, R), b)
    return x


def solve_system_householder(A, b):
    n = len(b)
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        sum = 0
        for j in range(i + 1, n):
            sum += A[i, j] * x[j]
        x[i] = (b[i] - sum) / A[i, i]
    return x


# ex4
def is_smaller(norm):
    if norm < eps:
        return True
    else:
        return False


# ex5
def inverse_matrix_QR(A, b, Q):
    n = len(A)
    for i in range(n):
        if math.fabs(A[i][i]) < eps:
            print('Inversa matricei A nu se poate calcula')
            exit(1)
    # se poate calcula inversa, calculam coloanele
    A_inversa = np.zeros((n, n))
    for j in range(n):
        b = np.zeros(n)
        for i in range(n):
            b[i] = Q[i][j]
        # se rezolva sis superior triunghilar R*x=b
        x = np.zeros(n)
        for i in range(n - 1, -1, -1):
            suma = 0.0
            for k in range(i + 1, n):
                suma += A[i][k] * x[k]
            x[i] = (b[i] - suma) / A[i][i]
        for i in range(0, n):
            A_inversa[i][j] = x[i]
    return A_inversa


##########################

# A = np.array([[0, 0, 4], [1, 2, 3], [0, 1, 2]])
# s = np.array([3, 2, 1])

n = 100
A = np.random.rand(n, n)
s = np.random.rand(n)

print("\n Exercitiu 1: \n")
b = calculate_b(A, s)
A_init = A.copy()
b_init = b.copy()
print("b este: ")
print(b)

print("\n Exercitiu 2: \n")
Q = QR_householder(A, b)
print("Q este: ")
print(Q.T)
print("R este: ")
print(A)

print("\n Exercitiu 3: \n")
x_QR = solve_system_QR(A, b)
print("x_QR este: ")
print(x_QR)
x_Householder = solve_system_householder(A, b)
print("x_Householder este: ")
print(x_Householder)
print("Norma euclidiana este:", np.linalg.norm(x_QR - x_Householder))

print("\n Exercitiu 4: \n")
error_Ax_b_Householder = np.linalg.norm(np.dot(A_init, x_Householder) - b_init)
error_Ax_b_QR = np.linalg.norm(np.dot(A_init, x_QR) - b_init)
error_x_s_Householder = np.linalg.norm(x_Householder - s) / np.linalg.norm(s)
error_x_s_QR = np.linalg.norm(x_QR - s) / np.linalg.norm(s)
print("Erorile sunt:")
print("Norma pentru metoda Householder:", error_Ax_b_Householder, "-> Norma e mai mica decat epsilon: ",
      is_smaller(error_Ax_b_Householder))
print("Norma pentru metoda QR:", error_Ax_b_QR, "-> Norma e mai mica decat epsilon: ", is_smaller(error_Ax_b_QR))
print("Norma pentru metoda Householder:", error_x_s_Householder, "-> Norma e mai mica decat epsilon: ",
      is_smaller(error_x_s_Householder))
print("Norma pentru metoda QR:", error_x_s_QR, "-> Norma e mai mica decat epsilon: ", is_smaller(error_x_s_QR))

print("\n Exercitiu 5: \n")
A_inversa_Householder = inverse_matrix_QR(A, b, Q)
print("Inversa matricei A folosind QR este: ")
print(A_inversa_Householder)
A_inv_lib = np.linalg.inv(A_init)
error_A_inv = np.linalg.norm(A_inversa_Householder - A_inv_lib)
print("Norma pentru diferenta dintre inversa calculata cu Householder si inversa biblioteca:",
      format(error_A_inv, '.15f'), "-> Norma e mai mica decat epsilon: ", is_smaller(error_A_inv))
