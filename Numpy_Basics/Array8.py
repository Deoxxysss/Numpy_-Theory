import numpy as np

# ============================================================
# 1. XY PLANE: TWO EQUATIONS, TWO UNKNOWNs
# ============================================================
#
# Example:
#
#       2x + 3y = 8
#        x -  y = 1
#
# These are two lines in the XY plane.
# Their intersection is the solution.

print("=" * 60)
print("1. XY PLANE - TWO EQUATIONS")
print("=" * 60)

A_xy = np.array([
    [2, 3],
    [1, -1]
])

b_xy = np.array([8, 1])

solution_xy = np.linalg.solve(A_xy, b_xy)

print("Coefficient matrix A:")
print(A_xy)

print("\nConstants vector b:")
print(b_xy)

print("\nSolution [x, y]:")
print(solution_xy)

x, y = solution_xy
print(f"\nx = {x}")
print(f"y = {y}")

# Verify:
# A @ solution should equal b

print("\nVerification: A @ solution")
print(A_xy @ solution_xy)

print("\nExpected:")
print(b_xy)

print("\nCorrect?", np.allclose(A_xy @ solution_xy, b_xy))


# ============================================================
# 2. XY PLANE: ANOTHER EXAMPLE
# ============================================================
#
#       3x + 2y = 12
#        x -  y = 1
#
# Again, the two lines intersect at one point.

print("\n" + "=" * 60)
print("2. XY PLANE - ANOTHER EXAMPLE")
print("=" * 60)

A_xy2 = np.array([
    [3, 2],
    [1, -1]
])

b_xy2 = np.array([12, 1])

solution_xy2 = np.linalg.solve(A_xy2, b_xy2)

print("Equations:")
print("3x + 2y = 12")
print(" x -  y = 1")

print("\nSolution [x, y]:")
print(solution_xy2)

print("\nVerification:")
print(A_xy2 @ solution_xy2)


# ============================================================
# 3. XYZ SPACE: THREE EQUATIONS, THREE UNKNOWNs
# ============================================================
#
# Example:
#
#       2x + y + z = 7
#        x + 3y + 2z = 13
#       3x + 2y + 4z = 23
#
# In 3D, each linear equation represents a plane.
# The solution is the point where all three planes intersect.

print("\n" + "=" * 60)
print("3. XYZ SPACE - THREE EQUATIONS")
print("=" * 60)

A_xyz = np.array([
    [2, 1, 1],
    [1, 3, 2],
    [3, 2, 4]
])

b_xyz = np.array([7, 13, 23])

solution_xyz = np.linalg.solve(A_xyz, b_xyz)

print("Coefficient matrix A:")
print(A_xyz)

print("\nConstants vector b:")
print(b_xyz)

print("\nSolution [x, y, z]:")
print(solution_xyz)

x, y, z = solution_xyz
print(f"\nx = {x}")
print(f"y = {y}")
print(f"z = {z}")

print("\nVerification: A @ solution")
print(A_xyz @ solution_xyz)

print("\nExpected:")
print(b_xyz)

print("\nCorrect?", np.allclose(A_xyz @ solution_xyz, b_xyz))


# ============================================================
# 4. UNDERSTANDING A @ x = b
# ============================================================
#
# For the XYZ example:
#
# A =
# [2 1 1]
# [1 3 2]
# [3 2 4]
#
# x =
# [x]
# [y]
# [z]
#
# b =
# [7 ]
# [13]
# [23]
#
# Matrix multiplication gives:
#
# 2x +  y +  z = 7
#  x + 3y + 2z = 13
# 3x + 2y + 4z = 23

print("\n" + "=" * 60)
print("4. WHAT DOES A @ x = b MEAN?")
print("=" * 60)

print("""
A @ x = b

For the XYZ example:

[2 1 1] [x]   [ 7]
[1 3 2] [y] = [13]
[3 2 4] [z]   [23]

This is exactly:

2x + y + z = 7
x + 3y + 2z = 13
3x + 2y + 4z = 23
""")


# ============================================================
# 5. A REUSABLE FUNCTION
# ============================================================

def solve_system(A, b):
    """Solve Ax = b and verify the result."""
    try:
        solution = np.linalg.solve(A, b)

        print("\nSolution:")
        print(solution)

        print("\nVerification:")
        print(A @ solution)

        print("\nMatches b?",
              np.allclose(A @ solution, b))

        return solution

    except np.linalg.LinAlgError:
        print("This system does not have a unique solution.")
        return None


print("\n" + "=" * 60)
print("5. REUSABLE FUNCTION")
print("=" * 60)

A = np.array([
    [2, 3],
    [1, -1]
])

b = np.array([8, 1])

solve_system(A, b)


# ============================================================
# 6. NO UNIQUE SOLUTION
# ============================================================
#
# These equations describe the same line:
#
#       x + y = 2
#      2x + 2y = 4
#
# There are infinitely many solutions.
#
# np.linalg.solve() cannot return one unique answer.

print("\n" + "=" * 60)
print("6. SYSTEM WITHOUT A UNIQUE SOLUTION")
print("=" * 60)

A_bad = np.array([
    [1, 1],
    [2, 2]
])

b_bad = np.array([2, 4])

print("Equations:")
print("x + y = 2")
print("2x + 2y = 4")

solve_system(A_bad, b_bad)


# ============================================================
# 7. QUICK SUMMARY
# ============================================================

print("\n" + "=" * 60)
print("DAY 3 SUMMARY")
print("=" * 60)

print("""
XY plane:
    2 equations + 2 unknowns
    -> two lines
    -> intersection = solution

XYZ space:
    3 equations + 3 unknowns
    -> three planes
    -> common intersection = solution

NumPy:
    np.linalg.solve(A, b)

Matrix multiplication:
    A @ solution

Verification:
    np.allclose(A @ solution, b)

Main idea:
    A @ x = b
""")