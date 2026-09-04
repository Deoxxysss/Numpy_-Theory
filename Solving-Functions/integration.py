import numpy as np

x = 0
#finding integral of sin(x) from 0 to 10
def f(x):
    return np.sin(x)
def integral(f, a, b, n = 1000):
    dx = np.linspace(a, b, n + 1)[1] - np.linspace(a, b, n + 1)[0]
    total = 0
    for i in range(1, n + 1):
        total += f(a + i * dx) * dx
    return total

result = integral(f, 0, 10)
print(result)

#2nd method using numpy's trapz function
def integral_trapz(f, a, b, n = 1000):
    x = np.linspace(a, b, n + 1)
    y = f(x)
    return np.trapezoid(y, x)
result = integral_trapz(f, 0, 10)
print(result)

#simpson rule
def simpson_rule(f, a, b, n=1000):
    if n % 2 == 1:
        n += 1  # Simpson's rule requires an even number of intervals
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    y = f(x)
    S = y[0] + y[-1] + 4 * np.sum(y[1:-1:2]) + 2 * np.sum(y[2:-2:2])
    return S * h / 3

result = simpson_rule(f, 0, 10)
print(result)