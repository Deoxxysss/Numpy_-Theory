import numpy as np
import matplotlib.pyplot as plt


# ============================================================
# Fixed-Point Iteration Method
# ============================================================

def fixed_point_method(g, x0, tolerance=1e-10, max_iterations=100):
    x = float(x0)
    history = [x]

    for iteration in range(1, max_iterations + 1):

        x_new = float(g(x))

        if not np.isfinite(x_new):
            raise ValueError("The iteration diverged.")

        history.append(x_new)

        if abs(x_new - x) < tolerance:
            return x_new, iteration, history

        x = x_new

    raise ValueError(
        f"Method did not converge within {max_iterations} iterations."
    )


# ============================================================
# Example 1
# x^3 - 2x - 5 = 0
#
# x = cuberoot(2x + 5)
# ============================================================

print("=" * 60)
print("Example 1: Solve x^3 - 2x - 5 = 0")
print("=" * 60)


def g1(x):
    return np.cbrt(2 * x + 5)


x0 = 2

root1, iterations1, history1 = fixed_point_method(g1, x0)

print(f"Initial guess : {x0}")
print(f"Root          : {root1:.10f}")
print(f"Iterations    : {iterations1}")
print(f"f(root)       : {root1**3 - 2*root1 - 5:.10e}")


# ============================================================
# Example 2
# cos(x) - x = 0
#
# x = cos(x)
# ============================================================

print()
print("=" * 60)
print("Example 2: Solve cos(x) - x = 0")
print("=" * 60)


def g2(x):
    return np.cos(x)


x0_2 = 0.5

root2, iterations2, history2 = fixed_point_method(g2, x0_2)

print(f"Initial guess : {x0_2}")
print(f"Root          : {root2:.10f}")
print(f"Iterations    : {iterations2}")
print(f"f(root)       : {np.cos(root2) - root2:.10e}")


# ============================================================
# Create graph data
# ============================================================

x1 = np.linspace(1.5, 2.5, 400)

y1_g = g1(x1)
y1_x = x1


x2 = np.linspace(0, 1, 400)

y2_g = g2(x2)
y2_x = x2


# ============================================================
# Create Figure
# ============================================================

fig, axes = plt.subplots(1, 2, figsize=(14, 6))


# ============================================================
# Example 1 Graph
# ============================================================

axes[0].plot(
    x1,
    y1_g,
    label=r"$g(x) = \sqrt[3]{2x+5}$",
    linewidth=2
)

axes[0].plot(
    x1,
    y1_x,
    label=r"$y=x$",
    linewidth=2
)

axes[0].scatter(
    root1,
    root1,
    s=80,
    label=f"Root = {root1:.5f}"
)

axes[0].set_title(
    r"Example 1: $x^3 - 2x - 5 = 0$"
)

axes[0].set_xlabel("x")
axes[0].set_ylabel("y")
axes[0].grid(True)
axes[0].legend()


# ============================================================
# Example 2 Graph
# ============================================================

axes[1].plot(
    x2,
    y2_g,
    label=r"$g(x) = \cos(x)$",
    linewidth=2
)

axes[1].plot(
    x2,
    y2_x,
    label=r"$y=x$",
    linewidth=2
)

axes[1].scatter(
    root2,
    root2,
    s=80,
    label=f"Root = {root2:.5f}"
)

axes[1].set_title(
    r"Example 2: $\cos(x) - x = 0$"
)

axes[1].set_xlabel("x")
axes[1].set_ylabel("y")
axes[1].grid(True)
axes[1].legend()


# ============================================================
# Save the graph
# ============================================================

plt.tight_layout()

plt.savefig(
    "fixed_point_graph.png",
    dpi=150,
    bbox_inches="tight"
)

print()
print("Graph saved as: fixed_point_graph.png")

# Show graph
plt.show()