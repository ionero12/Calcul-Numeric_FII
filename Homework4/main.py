import math

import numpy as np

eps = 10 ** -8
epsilon = 10 ** -8


def ex1_met1(filename):
    index = 0
    for line in open(filename):
        if index == 0:
            n = int(line.strip())
            m = list()
            for k in range(n):
                m.append(list())
            index += 1
        else:
            val, i, j = line.split(",")
            val = float(val.strip())
            i = int(i.strip())
            j = int(j.strip())
            if val:
                m[i].append((val, j))
            if i == j and abs(val) < eps:
                print("Elementele de pe diagonala matricei nu sunt nenule")
    return m, n


def ex1_b_met1(filename):
    i = 0
    for line in open(filename):
        if i == 0:
            b = list()
            i += 1
        else:
            b.append(float(line.strip()))
    return b


def ex2(a, b, x):
    iteration = 0
    while True:
        sum_squared_diff = 0
        for i in range(len(x)):
            product_sum = 0
            diagonal_value = None

            for element in a[i]:
                if i == element[1]:
                    diagonal_value = element[0]
                else:
                    product_sum += element[0] * x[element[1]]

            if diagonal_value is None:
                print("Elementele de pe diagonala principala sunt nule.")
                exit(0)

            old_x = x[i]
            x[i] = (b[i] - product_sum) / diagonal_value
            sum_squared_diff += (x[i] - old_x) ** 2

        norm = math.sqrt(sum_squared_diff)
        iteration += 1

        if norm < epsilon:
            print("Numarul de iteratii:", iteration)
            return x

        if norm > pow(10, 8):
            print("Divergenta")
            return x  # exit(1)


def ex3(a, b, x, n):
    max_value = 0
    for i in range(len(a)):
        sum_product = 0
        for element in a[i]:
            sum_product += element[0] * x[element[1]]
        diff = abs(sum_product - b[i])
        if diff > max_value:
            max_value = diff
    return max_value


# prima metoda
a, n = ex1_met1('tema4files/a_1.txt')
b = ex1_b_met1('tema4files/b_1.txt')
# a, n = ex1_met1('tema4files/a_2.txt')
# b = ex1_b_met1('tema4files/b_2.txt')
# a, n = ex1_met1('tema4files/a_3.txt')
# b = ex1_b_met1('tema4files/b_3.txt')
# a, n = ex1_met1('tema4files/a_4.txt')
# b = ex1_b_met1('tema4files/b_4.txt')
# a, n = ex1_met1('tema4files/a_5.txt')
# b = ex1_b_met1('tema4files/b_5.txt')



print("n1: \n")
print(n)
print("\n b1: \n")
# print(b)

x = np.zeros(n)
x = ex2(a, b, x)
print("\n x1: \n")
print(x)
print("\n ex3: \n")
print(ex3(a, b, x, n))


