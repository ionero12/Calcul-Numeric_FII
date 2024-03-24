import random
import sys

import numpy as np


def horner(coefficients, x):
    """
    Evaluarea polinomului utilizând schema lui Horner.
    """
    result = coefficients[0]
    for coeff in coefficients[1:]:
        result = result * x + coeff
    return result


def muller_method(coefficients, e, R):
    roots = []
    i = 0
    left_bound = -R
    increment = 0.05
    while left_bound <= R:
        x_0 = random.uniform(left_bound, left_bound + increment)
        x_1 = random.uniform(left_bound, left_bound + increment)
        x_2 = random.uniform(left_bound, left_bound + increment)
        delta_x = 0
        computed_values = 0
        while True:
            k = 3
            h_0 = x_1 - x_0
            h_1 = x_2 - x_1
            if (np.abs(h_0) < e or np.abs(h_1) < e or np.abs(h_1 + h_0) < e):
                break
            if (horner(coefficients, x_1) == float('inf') or horner(coefficients, x_0) == float('inf') or horner(
                    coefficients, x_2) == float('inf')):
                break
            delta_0 = (horner(coefficients, x_1) - horner(coefficients, x_0)) / h_0
            delta_1 = (horner(coefficients, x_2) - horner(coefficients, x_1)) / h_1
            a = (delta_1 - delta_0) / (h_1 + h_0)
            b = a * h_1 + delta_1
            c = horner(coefficients, x_2)
            if b <= 0:
                sign_b = -1
            else:
                sign_b = 1
            if b >= np.sqrt(sys.float_info.max) / 10 ** 5 or a >= np.sqrt(sys.float_info.max) / 10 ** 5 or c >= np.sqrt(
                    sys.float_info.max) / 10 ** 5:
                break
            if b ** 2 <= 4 * a * c:
                break
            if np.abs(b + sign_b * np.sqrt(b ** 2 - 4 * a * c)) < e:
                break
            delta_x = 2 * c / (b + sign_b * np.sqrt(b ** 2 - 4 * a * c))
            x_3 = x_2 - delta_x
            k += 1
            x_0 = x_1
            x_1 = x_2
            x_2 = x_3
            computed_values = 1
            if np.abs(delta_x) < e or k > 1000 or np.abs(delta_x) > 10 ** 8:
                break
        if np.abs(delta_x) < e and computed_values == 1:
            found = 0
            for root in roots:
                if np.abs(x_3 - root) < e:
                    found = 1
                    break
            if found == 0:
                roots.append(x_3)
        left_bound += increment
    return roots


def write_roots_to_file(roots, filename, epsilon):
    with open(filename, "w") as file:
        for i in range(len(roots)):
            for j in range(i + 1, len(roots)):
                if abs(roots[i] - roots[j]) <= epsilon:
                    roots[j] = float('inf')
        roots = [root for root in roots if root != float('inf')]
        for root in roots:
            file.write(str(root) + "\n")


# bonus
def f(x):
    if x <= 250:
        return np.exp(x) - np.sin(x)
    else:
        print(f"Error: For x = {x}, function return a number too large to be represented.")
        exit()


def f_prime(x):
    if x <= 250:
        return np.exp(x) - np.cos(x)
    else:
        print(f"Error: For x = {x}, function return a number too large to be represented.")
        exit()


def newton_fourth_order_method(f, f_prime, x0, epsilon, max_iter=1000):
    roots = []
    x_n = x0
    for _ in range(max_iter):
        f_xn = f(x_n)
        f_prime_xn = f_prime(x_n)
        y_n = x_n - f_xn / f_prime_xn
        x_np1 = x_n - (f_xn ** 2 + f(y_n) ** 2) / (f_prime_xn * f_xn - f(y_n))
        if np.abs(x_np1 - x_n) < epsilon:
            roots.append(x_np1)
            break
        x_n = x_np1
    return roots


def newton_fifth_order_method(f, f_prime, x0, epsilon, max_iter=1000):
    roots = []
    x_n = x0
    for _ in range(max_iter):
        f_xn = f(x_n)
        f_prime_xn = f_prime(x_n)
        y_n = x_n - f_xn / f_prime_xn
        z_n = x_n - (f_xn ** 2 + f(y_n) ** 2) / (f_prime_xn * f_xn - f(y_n))
        x_np1 = z_n - f(z_n) / f_prime_xn
        if np.abs(x_np1 - x_n) < epsilon:
            roots.append(x_np1)
            break
        x_n = x_np1
    return roots


# Exemplu de utilizare
coefficients = [1.0, -6.0, 11.0, -6]
n = len(coefficients) - 1
eps = 1e-10
R = 10

roots = muller_method(coefficients, eps, R)
if roots:
    print("Rădăcinile găsite:", roots)
    write_roots_to_file(roots, "roots.txt", eps)
else:
    print("Nu s-au putut găsi rădăcini în intervalul dat.")

# bonus
initial_guess = -3
roots = newton_fourth_order_method(f, f_prime, initial_guess, eps)
if roots:
    print("Roots found for newton_fourth_order_method:", roots)
else:
    print("No roots found with the given initial guess and tolerance.")

roots = newton_fifth_order_method(f, f_prime, initial_guess, eps)
if roots:
    print("Roots found for newton_fifth_order_method:", roots)
else:
    print("No roots found with the given initial guess and tolerance.")
