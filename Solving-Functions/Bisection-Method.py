"""
Bisection Method for Finding Roots

The Bisection Method is a numerical technique used to find the root of a function f(x).
It works by repeatedly narrowing down the interval [a, b] where the root exists.

How it works:
1. Start with an interval [a, b] where f(a) and f(b) have opposite signs (f(a)*f(b) < 0)
2. Find the midpoint c = (a + b) / 2
3. Evaluate f(c)
4. If f(c) ≈ 0, then c is the root
5. Otherwise, narrow the interval:
   - If f(a) and f(c) have opposite signs, the root is in [a, c]
   - If f(c) and f(b) have opposite signs, the root is in [c, b]
6. Repeat until convergence
"""

import numpy as np
import matplotlib.pyplot as plt


def bisection_method(func, a, b, tolerance=1e-6, max_iterations=100):
    """
    Find the root of a function using the Bisection Method.
    
    Parameters:
    -----------
    func : callable
        The function for which to find the root
    a : float
        Left endpoint of the interval
    b : float
        Right endpoint of the interval
    tolerance : float
        Convergence criterion (default: 1e-6)
    max_iterations : int
        Maximum number of iterations (default: 100)
    
    Returns:
    --------
    root : float
        The approximate root of the function
    iterations : int
        Number of iterations performed
    history : list
        History of interval midpoints for visualization
    """
    
    # Check if initial interval is valid
    if func(a) * func(b) > 0:
        raise ValueError("f(a) and f(b) must have opposite signs")
    
    history = []
    
    for i in range(max_iterations):
        c = (a + b) / 2  # Midpoint
        history.append(c)
        
        # Check convergence
        if abs(func(c)) < tolerance or abs(b - a) < tolerance:
            return c, i + 1, history
        
        # Narrow down the interval
        if func(a) * func(c) < 0:
            # Root is in [a, c]
            b = c
        else:
            # Root is in [c, b]
            a = c
    
    return c, max_iterations, history


# Example 1: Finding root of f(x) = x^2 - 4
print("=" * 60)
print("Example 1: Finding root of f(x) = x^2 - 4")
print("=" * 60)

def f1(x):
    return x**2 - 4

# The roots of x^2 - 4 = 0 are x = ±2
# We'll find the positive root in interval [1, 3]
root1, iterations1, history1 = bisection_method(f1, 1, 3, tolerance=1e-8)
print(f"Root found: {root1:.10f}")
print(f"f(root) = {f1(root1):.2e}")
print(f"Iterations: {iterations1}")
print(f"Expected root: 2.0\n")


# Example 2: Finding root of f(x) = cos(x) - x
print("=" * 60)
print("Example 2: Finding root of f(x) = cos(x) - x")
print("=" * 60)

def f2(x):
    return np.cos(x) - x

# The root is approximately 0.739
root2, iterations2, history2 = bisection_method(f2, 0, 1, tolerance=1e-8)
print(f"Root found: {root2:.10f}")
print(f"f(root) = {f2(root2):.2e}")
print(f"Iterations: {iterations2}\n")


# Example 3: Finding root of f(x) = e^x - 3x
print("=" * 60)
print("Example 3: Finding root of f(x) = e^x - 3x")
print("=" * 60)

def f3(x):
    return np.exp(x) - 3*x

# Finding root in interval [0, 1]
root3, iterations3, history3 = bisection_method(f3, 0, 1, tolerance=1e-8)
print(f"Root found: {root3:.10f}")
print(f"f(root) = {f3(root3):.2e}")
print(f"Iterations: {iterations3}\n")


# Visualization
print("=" * 60)
print("Visualization of Convergence")
print("=" * 60)

fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# Plot 1: f(x) = x^2 - 4 with root
x_vals = np.linspace(-1, 4, 500)
y_vals = x_vals**2 - 4
axes[0, 0].plot(x_vals, y_vals, 'b-', linewidth=2, label='f(x) = x² - 4')
axes[0, 0].axhline(y=0, color='k', linestyle='--', alpha=0.3)
axes[0, 0].plot(root1, 0, 'ro', markersize=10, label=f'Root = {root1:.6f}')
axes[0, 0].grid(True, alpha=0.3)
axes[0, 0].set_xlabel('x')
axes[0, 0].set_ylabel('f(x)')
axes[0, 0].set_title('Example 1: f(x) = x² - 4')
axes[0, 0].legend()

# Plot 2: f(x) = cos(x) - x with root
x_vals = np.linspace(0, 1, 500)
y_vals = np.cos(x_vals) - x_vals
axes[0, 1].plot(x_vals, y_vals, 'g-', linewidth=2, label='f(x) = cos(x) - x')
axes[0, 1].axhline(y=0, color='k', linestyle='--', alpha=0.3)
axes[0, 1].plot(root2, 0, 'ro', markersize=10, label=f'Root = {root2:.6f}')
axes[0, 1].grid(True, alpha=0.3)
axes[0, 1].set_xlabel('x')
axes[0, 1].set_ylabel('f(x)')
axes[0, 1].set_title('Example 2: f(x) = cos(x) - x')
axes[0, 1].legend()

# Plot 3: f(x) = e^x - 3x with root
x_vals = np.linspace(0, 2, 500)
y_vals = np.exp(x_vals) - 3*x_vals
axes[1, 0].plot(x_vals, y_vals, 'r-', linewidth=2, label='f(x) = eˣ - 3x')
axes[1, 0].axhline(y=0, color='k', linestyle='--', alpha=0.3)
axes[1, 0].plot(root3, 0, 'ro', markersize=10, label=f'Root = {root3:.6f}')
axes[1, 0].grid(True, alpha=0.3)
axes[1, 0].set_xlabel('x')
axes[1, 0].set_ylabel('f(x)')
axes[1, 0].set_title('Example 3: f(x) = eˣ - 3x')
axes[1, 0].legend()

# Plot 4: Convergence history for Example 2
iterations_range = range(1, len(history2) + 1)
errors = np.abs(np.array(history2) - root2)
axes[1, 1].semilogy(iterations_range, errors, 'b-o', linewidth=2, markersize=6)
axes[1, 1].grid(True, alpha=0.3, which='both')
axes[1, 1].set_xlabel('Iteration')
axes[1, 1].set_ylabel('|xₙ - root| (log scale)')
axes[1, 1].set_title('Convergence of Bisection Method (Example 2)')

plt.tight_layout()
plt.savefig('/home/icyvenus/Downloads/Venus/Numpy_-Theory/Solving-Functions/bisection_method_visualization.png', dpi=150)
plt.show()

print("Visualization saved as 'bisection_method_visualization.png'")
