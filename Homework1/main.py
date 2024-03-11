import math
import random
from collections import defaultdict

import numpy as np


# ex1
def calculate_precision():
    p = 1.0
    while 1 + 10 ** (-p) != 1:
        p += 1
    print("Valoarea p-1 este: ", p - 1)
    # print("Valoarea u = 10 ** (-p) este: ", 10 ** (-(p - 1)))
    return 10 ** (-(p - 1))


# print(calculate_precision())
print()


# ex2

def check_non_associativity():
    x = 1.0
    y = z = calculate_precision()
    if not ((x + y) + z == x + (y + z)):
        return "The sum operation is non-associative"
    else:
        return "The sum operation is associative"


def check_multiplication_associativity():
    while True:
        a = random.random()
        b = random.random()
        c = random.random()
        if (a * b) * c != a * (b * c):
            return f"Multiplication is not associative for values: \n{a}\n{b}\n{c} \n"


print(check_non_associativity())
print(check_multiplication_associativity())
print()


# ex3
# T(i,a)
def T(i, a):
    if i == 1:
        return a
    elif i == 2:
        return 3 * a / (3 - a ** 2)
    elif i == 3:
        return (15 * a - a ** 3) / (15 - 6 * a ** 2)
    elif i == 4:
        return (105 * a - 10 * a ** 3) / (105 - 45 * a ** 2 + a ** 4)
    elif i == 5:
        return (945 * a - 105 * a ** 3 + a ** 5) / (945 - 420 * a ** 2 + 15 * a ** 4)
    elif i == 6:
        return (10395 * a - 1260 * a ** 3 + 21 * a ** 5) / (10395 - 4725 * a ** 2 + 210 * a ** 4 - a ** 6)
    elif i == 7:
        return (135135 * a - 17325 * a ** 3 + 378 * a ** 5 - a ** 7) / (
                135135 - 62370 * a ** 2 + 3150 * a ** 4 - 28 * a ** 6)
    elif i == 8:
        return (2027025 * a - 270270 * a ** 3 + 6930 * a ** 5 - 36 * a ** 7) / (
                2027025 - 945945 * a ** 2 + 51975 * a ** 4 - 630 * a ** 6 + a ** 8)
    elif i == 9:
        return (34459425 * a - 4729725 * a ** 3 + 135135 * a ** 5 - 990 * a ** 7 + a ** 9) / (
                34459425 - 16216200 * a ** 2 + 945945 * a ** 4 - 13860 * a ** 6 + 45 * a ** 8)


# generate the random values
random_numbers = np.random.uniform(-math.pi / 2, math.pi / 2, 10000)

# dictionary to store the sum of errors for each function
sum_errors = defaultdict(float)

# calculate T(i,a) for random values and write the results to a file
with open('results.txt', 'w') as f:
    for a in random_numbers:
        exact_value = math.tan(a)
        errors = []
        for i in range(1, 10):
            Ti_value = T(i, a)
            error = abs(Ti_value - exact_value)
            errors.append((i, error))
            sum_errors[i] += error

        # sort by error
        errors.sort(key=lambda x: x[1])

        # write the first 3 functions with the lowest error to the file
        f.write(f"For a = {a}, the best three functions are: {errors[:3]}\n")

# create a ranking of the functions based on their average errors
ranking = sorted(((i, error / len(random_numbers)) for i, error in sum_errors.items()), key=lambda x: x[1])

# print the ranking to the screen
for i, error in ranking:
    print(f"Function T({i},a) with total error: {error}")


# bonus

def s(n, a):
    return ((1 - T(n, (2 * a - math.pi)) / 4) ** 2) / ((1 + T(n, (2 * a - math.pi)) / 4) ** 2)


def c(n, a):
    return (1 - T(n, a / 2) ** 2) / (1 + T(n, a / 2) ** 2)


with open('results-sin-cos.txt', 'w') as f:
    for a in random_numbers:
        errors_s = []
        errors_c = []
        for i in range(1, 10):
            error_s = abs(s(i, a) - math.sin(a))
            error_c = abs(c(i, a) - math.cos(a))
            errors_s.append((i, error_s))
            errors_c.append((i, error_c))

        errors_s.sort(key=lambda x: x[1])
        errors_c.sort(key=lambda x: x[1])

        f.write(f"For a = {a}, the best three sin functions are: {errors_s[:3]}\n")
        f.write(f"For a = {a}, the best three cos functions are: {errors_c[:3]}\n")
