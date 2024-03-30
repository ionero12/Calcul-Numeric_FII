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


# def ex1_met2(filename):
#     values = []
#     ind_col = []
#     start_indices = [0]
#
#     with open(filename, 'r') as file:
#         n = int(file.readline())
#         for line in file:
#             value, j, _ = map(float, line.split(','))
#             values.append(value)
#             ind_col.append(int(j))
#             start_indices.append(len(values))
#
#     return n, values, ind_col, start_indices
#
#
# def ex1_b_met2(filename):
#     with open(filename, 'r') as file:
#         termeni_liberi = [float(line.strip()) for line in file]
#     return termeni_liberi

# def build_even_more_efficient_matrixes(txt):
#     valori = []
#     ind_col = []
#     with open(txt, "r") as file:
#         size_matrix = int(file.readline())
#         inceput_linii = [-1 for i in range(0, size_matrix + 1)]
#         for line in file:
#             line_array = line.split(", ")
#             line_array[-1] = line_array[-1].split("\n")[0]
#             line_array[0] = line_array[0].split(" ")[0]
#             if line_array == ['']:
#                 break
#             current_line = int(line_array[1])
#             current_column = int(line_array[2])
#             current_value = float(line_array[0])
#             if inceput_linii[current_line] == -1:
#                 inceput_linii[current_line] = len(valori)
#             flag = False
#             for i in range(inceput_linii[current_line], len(valori)):
#                 if ind_col[i] == current_column:
#                     valori[i] += current_value
#                     flag = True
#             if flag is False:
#                 valori.append(current_value)
#                 ind_col.append(current_column)
#     inceput_linii[-1] = len(valori) + 1
#     return valori, ind_col, inceput_linii


# def build_even_more_efficient_matrixes(matrix_lines):
#     valori = []
#     ind_col = []
#     inceput_linii = [-1] * (len(matrix_lines) + 1)
#
#     for current_line, line in enumerate(matrix_lines):
#         line_array = line.split(', ')
#         for current_column, value in enumerate(line_array):
#             if value != '0':
#                 current_value = float(value)
#                 if inceput_linii[current_line] == -1:
#                     inceput_linii[current_line] = len(valori)
#                 flag = False
#                 for i in range(inceput_linii[current_line], len(valori)):
#                     if ind_col[i] == current_column:
#                         valori[i] += current_value
#                         flag = True
#                 if not flag:
#                     valori.append(current_value)
#                     ind_col.append(current_column)
#
#     inceput_linii[-1] = len(valori) + 1
#     return valori, ind_col, inceput_linii, len(matrix_lines)


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


# a doua metoda
# n, valori, ind_col, inceput_linii = ex1_met2('tema4files/a_1.txt')
# b = ex1_b_met2('tema4files/b_1.txt')
# n, valori, ind_col, inceput_linii = ex1_met2('tema4files/a_2.txt')
# b = ex1_b_met2('tema4files/b_2.txt')
# n, valori, ind_col, inceput_linii = ex1_met2('tema4files/a_3.txt')
# b = ex1_b_met2('tema4files/b_3.txt')
# n, valori, ind_col, inceput_linii = ex1_met2('tema4files/a_4.txt')
# b = ex1_b_met2('tema4files/b_4.txt')
# n, valori, ind_col, inceput_linii = ex1_met2('tema4files/a_5.txt')
# b = ex1_b_met2('tema4files/b_5.txt')


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

# matrix_lines = [
#     "102.5, 0, 2.5, 0, 0",
#     "3.5, 104.88, 1.05, 0, 0.33",
#     "0, 0, 100.0, 0, 0",
#     "0, 1.3, 0, 101.3, 0",
#     "0.73, 0, 0, 1.5, 102.23"
# ]

#valori, ind_col, inceput_linii, n = build_even_more_efficient_matrixes(matrix_lines)

# print("n: ")
# print(n)
# print("valori: ")
# print(valori)
# print("ind_col: ")
# print(ind_col)
# print("inceput_linii: ")
# print(inceput_linii)

# x = np.zeros(n)
# x = ex2_met2(valori, ind_col, inceput_linii, b, x)
# print("\n x1: \n")
# print(x)
# print("\n ex3: \n")
# print(ex3_met2(valori, ind_col, inceput_linii, b, x))
