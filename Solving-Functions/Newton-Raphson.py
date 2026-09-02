"""
Newton-Raphson Method
=====================

What it is:
    The Newton-Raphson method is an iterative numerical technique used to find
    roots of a real-valued function f(x) = 0.

    If x_n is the current estimate, then the next estimate is:
        x_{n+1} = x_n - f(x_n) / f'(x_n)

    where f'(x) is the derivative of f(x).

How it works:
    - Start with an initial guess x0.
    - Compute the tangent line to the curve at x0.
    - Find where that tangent line crosses the x-axis.
    - Repeat until the change is very small or the function value is close to zero.

Why use it:
    - Very fast when the initial guess is close to the actual root.
    - It usually converges quadratically near simple roots.
    - Works well for smooth functions with known derivatives.

Using NumPy:
    NumPy helps with array operations, mathematical calculations, and plotting
    when needed. This example uses only standard NumPy math functions.
"""

import numpy as np


def newton_raphson(f, f_prime, x0, tol=1e-10, max_iter=100):
    """
    Solve f(x) = 0 using the Newton-Raphson method.

    Parameters
    ----------
    f : callable
        Function whose root is to be found.
    f_prime : callable
        Derivative of f.
    x0 : float
        Initial guess.
    tol : float, optional
        Tolerance for stopping criterion.
    max_iter : int, optional
        Maximum number of iterations.

    Returns
    -------
    x : float
        Approximate root.
    history : list of float
        Iteration history.
    """
    x = float(x0)
    history = [x]

    for _ in range(max_iter):
        fx = f(x)
        dfx = f_prime(x)

        if abs(dfx) < 1e-14:
            raise ValueError("Derivative is zero or too close to zero; Newton-Raphson fails.")

        x_new = x - fx / dfx
        history.append(x_new)

        if abs(x_new - x) < tol or abs(fx) < tol:
            return x_new, history

        x = x_new

    raise RuntimeError(f"Newton-Raphson did not converge within {max_iter} iterations.")


# Example 1: Solve x^3 - 2x - 5 = 0
# This equation has a real root near 2.0945.

def f1(x):
    return x**3 - 2*x - 5


def f1_prime(x):
    return 3*x**2 - 2


root1, history1 = newton_raphson(f1, f1_prime, x0=2.0)
print("Example 1:")
print("Root:", root1)
print("Iterations:", history1)
print("Check f(root):", f1(root1))
print()


# Example 2: Solve x^2 - 4 = 0
# Roots are x = ±2.

def f2(x):
    return x**2 - 4


def f2_prime(x):
    return 2*x


for guess in [1.0, 10.0, -10.0]:
    root2, history2 = newton_raphson(f2, f2_prime, x0=guess)
    print(f"Example 2 with initial guess {guess}:")
    print("Root:", root2)
    print("History:", history2)
    print("Check f(root):", f2(root2))
    print()


# Example 3: Solve sin(x) = 0 near x = 3
# Root is near x = pi (3.14159...)

def f3(x):
    return np.sin(x)


def f3_prime(x):
    return np.cos(x)


root3, history3 = newton_raphson(f3, f3_prime, x0=3.0)
print("Example 3:")
print("Root:", root3)
print("Check sin(root):", f3(root3))
print("History:", history3)
print()


# How to use it in your own code:
#
# 1. Define the function f(x) and derivative f'(x).
# 2. Choose an initial guess x0.
# 3. Call newton_raphson(f, f_prime, x0).
#
# Example:
#
# def my_function(x):
#     return x**3 - 9*x + 3
#
# def my_derivative(x):
#     return 3*x**2 - 9
#
# root, steps = newton_raphson(my_function, my_derivative, x0=2.5)
# print(root)


# Optional: plot the function and iterates if you are using matplotlib
# import matplotlib.pyplot as plt
# x_vals = np.linspace(-3, 3, 500)
# y_vals = f2(x_vals)
# plt.plot(x_vals, y_vals)
# plt.axhline(0, color='black', linewidth=1)
# plt.scatter(history2, [0]*len(history2), color='red')
# plt.show()


# Summary:
# Newton-Raphson is a powerful method when you know the derivative and have a
# reasonable initial guess. It usually reaches a root very quickly, but can fail
# if the derivative is zero or if the initial guess is poor.
