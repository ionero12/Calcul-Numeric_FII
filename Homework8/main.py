import numpy as np


# Definirea funcției de test (puteți înlocui cu funcția dvs.)
def function_to_minimize(x, y):
    # return x ** 2 + y ** 2 - 2 * x - 4 * y - 1
    #return 3 * x ** 2 - 12 * x + 2 * y ** 2 + 16 * y - 10
    #return x ** 2 - 4 * x * y + 5 * y ** 2 - 4 * y + 3
    return x ** 2 * y - 2 * x * y ** 2 + 3 * x * y + 4

# Derivatele parțiale ale funcției de test (pentru gradientul analitic)
def function_gradient(x, y):
    # grad_x = 2 * x - 2
    # grad_y = 2 * y - 4
    # grad_x = 6 * x - 12
    # grad_y = 4 * y + 16
    # grad_x = 2 * x - 4 * y
    # grad_y = -4 * x + 10 * y - 4
    grad_x = 2*x*y - 2 * y ** 2 + 3 * y
    grad_y = x ** 2 - 4 *x * y + 3 * x
    return [grad_x, grad_y]


# Aproximarea gradientului utilizând diferențe finite (pentru gradientul aproximativ)
def approximate_gradient(function, x, y, epsilon=1e-5):
    grad_x = (function(x + epsilon, y) - function(x, y)) / epsilon
    grad_y = (function(x, y + epsilon) - function(x, y)) / epsilon
    return [grad_x, grad_y]


def function_minimization(epsilon, learning_rate_type, gradient_type):
    iterations = 0
    while True:
        x = np.random.uniform(-100, 100)
        y = np.random.uniform(-100, 100)
        k = 0
        while True:
            iterations += 1
            if gradient_type == 'Analitic':
                gradient = function_gradient(x, y)
            else:
                gradient = approximate_gradient(function_to_minimize, x, y)
            if learning_rate_type == 'Constant':
                learning_rate = 1e-3
            else:
                beta = 0.8
                learning_rate = 1
                p = 1
                while function_to_minimize(x - learning_rate * gradient[0], y - learning_rate * gradient[1]) > \
                        function_to_minimize(x, y) - learning_rate / 2 * np.linalg.norm(gradient) ** 2 and p < 8:
                    learning_rate = beta * learning_rate
                    p += 1
            x -= learning_rate * gradient[0]
            y -= learning_rate * gradient[1]
            k += 1
            if learning_rate * np.linalg.norm(gradient) < epsilon or k > 30_000 or learning_rate * np.linalg.norm(
                    gradient) > 1e10:
                break
        if learning_rate * np.linalg.norm(gradient) <= epsilon:
            #print(iterations)
            return [x, y]
        if k > 30_000:
            epsilon *= 10


# Testarea funcției de minimizare
epsilon = 1e-6
print("Minimizare cu rată de învățare constantă și gradient analitic:",
      function_minimization(epsilon, 'Constant', 'Analitic'))
print("Minimizare cu rată de învățare constantă și gradient aproximativ:",
      function_minimization(epsilon, 'Constant', 'Aproximare'))
print("Minimizare cu rată de învățare variabilă și gradient analitic:",
      function_minimization(epsilon, 'Variabila', 'Analitic'))
print("Minimizare cu rată de învățare variabilă și gradient aproximativ:",
      function_minimization(epsilon, 'Variabila', 'Aproximare'))