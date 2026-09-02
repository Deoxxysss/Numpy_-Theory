NumPy & Numerical Root Finding

A learning-oriented Python project covering NumPy from the basics to advanced concepts, followed by implementations of three important numerical root-finding methods:

Bisection Method

Fixed-Point Iteration

Newton-Raphson Method

The project is intended as a practical reference for learning scientific computing and numerical methods with Python.

📁 Project Structure

NumPy_-Theory/
│
├── README.md
│
├── NumPy/
│   ├── 01_Basics.py
│   ├── 02_Indexing_and_Slicing.py
│   ├── 03_Array_Operations.py
│   ├── 04_Broadcasting.py
│   ├── 05_Vectorization.py
│   ├── 06_Linear_Algebra.py
│   ├── 07_Statistics.py
│   ├── 08_Random.py
│   ├── 09_Advanced.py
│   └── ...
│
└── Solving-Functions/
    └── Root-Finding-Methods.py

The filenames above are an example structure. Rename or organize the files according to the actual project layout.

1. NumPy

What is NumPy?

NumPy (Numerical Python) is a Python library designed for numerical and scientific computing.

Its central object is the ndarray, a multidimensional array that allows efficient mathematical operations on large collections of numbers.

NumPy is widely used in:

Scientific computing

Data analysis

Machine learning

Engineering

Physics

Statistics

Numerical methods

Linear algebra

Simulation

Install NumPy with:

pip install numpy

Import it with:

import numpy as np

2. NumPy Basics

Creating Arrays

import numpy as np

a = np.array([1, 2, 3, 4, 5])

print(a)

A two-dimensional array:

matrix = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

Array Properties

Important properties include:

a.shape
a.ndim
a.size
a.dtype

Example:

a = np.array([[1, 2, 3], [4, 5, 6]])

print(a.shape)   # (2, 3)
print(a.ndim)    # 2
print(a.size)    # 6
print(a.dtype)   # data type

Important concepts

Property

Meaning

shape

Dimensions of the array

ndim

Number of dimensions

size

Total number of elements

dtype

Data type of elements

3. Creating Special Arrays

NumPy provides convenient functions for generating arrays.

np.zeros((3, 3))
np.ones((2, 4))
np.full((2, 3), 7)
np.eye(4)

Sequences:

np.arange(0, 10, 2)
np.linspace(0, 1, 5)

Random arrays:

np.random.randint(1, 10, 5)
np.random.random(5)

4. Indexing and Slicing

NumPy indexing starts at 0.

a = np.array([10, 20, 30, 40, 50])

print(a[0])
print(a[2])

Slicing:

print(a[1:4])
print(a[:3])
print(a[2:])
print(a[::-1])

For two-dimensional arrays:

matrix[0, 1]
matrix[:, 0]
matrix[1, :]

5. Boolean and Fancy Indexing

Boolean indexing allows elements to be selected according to a condition.

a = np.array([1, 2, 3, 4, 5])

print(a[a > 3])

Multiple conditions:

print(a[(a > 1) & (a < 5)])

Fancy indexing:

indices = [0, 2, 4]
print(a[indices])

6. Array Operations

NumPy supports element-wise arithmetic.

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(a + b)
print(a - b)
print(a * b)
print(a / b)

Scalar operations:

a * 10
a + 5

These operations avoid writing explicit Python loops for many numerical tasks.

7. Universal Functions

NumPy provides optimized mathematical functions called ufuncs.

np.sqrt(a)
np.exp(a)
np.log(a)
np.sin(a)
np.cos(a)
np.abs(a)

Example:

x = np.array([0, np.pi / 2, np.pi])

print(np.sin(x))

8. Aggregation Functions

Common aggregation operations:

np.sum(a)
np.mean(a)
np.median(a)
np.min(a)
np.max(a)
np.std(a)
np.var(a)

For matrices, an axis can be specified:

matrix.sum(axis=0)
matrix.sum(axis=1)

Remember:

axis=0 operates down the rows

axis=1 operates across the columns

9. Reshaping Arrays

Arrays can be reshaped without changing their data.

a = np.arange(12)

b = a.reshape(3, 4)

print(b)

Other useful operations:

a.flatten()
a.ravel()
a.reshape(...)

Transpose:

matrix.T

10. Joining and Splitting Arrays

Joining:

np.concatenate((a, b))
np.vstack((a, b))
np.hstack((a, b))

Splitting:

np.split(a, 2)
np.array_split(a, 3)

11. Broadcasting

Broadcasting allows NumPy to perform operations on arrays with compatible shapes.

Example:

a = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

b = np.array([10, 20, 30])

print(a + b)

Conceptually:

[1, 2, 3]      [10, 20, 30]
[4, 5, 6]  +   [10, 20, 30]

Broadcasting is one of NumPy's most important concepts.

12. Vectorization

Instead of:

result = []

for x in a:
    result.append(x ** 2)

NumPy allows:

result = a ** 2

This is called vectorization.

Vectorized operations are generally faster and make numerical code more concise.

13. Copies and Views

This is an important advanced NumPy concept.

A view can reference the same underlying data:

b = a.view()

A copy creates independent data:

b = a.copy()

Changing a view may affect the original array, while changing a copy does not.

Understanding this prevents subtle bugs in numerical programs.

14. Missing and Special Values

NumPy provides tools for working with special values.

np.nan
np.inf

Checking values:

np.isnan(a)
np.isinf(a)
np.isfinite(a)

Example:

a = np.array([1, np.nan, 3])

print(np.isnan(a))

15. Sorting and Searching

np.sort(a)
np.argsort(a)
np.argmax(a)
np.argmin(a)
np.where(a > 3)

Example:

indices = np.where(a > 3)

16. Random Number Generation

Modern NumPy code can use a random generator:

rng = np.random.default_rng()

data = rng.integers(1, 100, size=10)

Random floating-point numbers:

rng.random(10)

Normal distribution:

rng.normal(0, 1, 1000)

17. Linear Algebra

NumPy provides many linear algebra operations.

A = np.array([
    [1, 2],
    [3, 4]
])

B = np.array([
    [5, 6],
    [7, 8]
])

Matrix multiplication:

A @ B

or:

np.matmul(A, B)

The dot product:

np.dot(A, B)

For vectors:

a = np.array([1, 2])
b = np.array([3, 4])

np.dot(a, b)

18. Solving Linear Systems

Given:

Ax = b

NumPy can solve the system directly:

A = np.array([
    [2, 1],
    [1, 3]
])

b = np.array([5, 6])

x = np.linalg.solve(A, b)

print(x)

Other useful functions:

np.linalg.det(A)
np.linalg.inv(A)
np.linalg.eig(A)
np.linalg.norm(A)

19. Numerical Root Finding

A root of a function is a value x for which:

f(x) = 0

For example:

f(x) = x² - 4

has roots:

x = -2
x = 2

This project implements three classical numerical methods for finding roots.

20. Bisection Method

The Bisection Method requires an interval [a, b] where:

f(a) × f(b) < 0

This indicates a sign change, assuming the function is continuous on the interval.

The midpoint is:

c = (a + b) / 2

The interval is repeatedly divided in half until the desired accuracy is reached.

Advantages

Simple

Reliable when its assumptions are satisfied

Guaranteed to converge under the standard continuity/sign-change conditions

Disadvantages

Relatively slow

Requires a suitable initial interval

21. Fixed-Point Iteration

The equation:

f(x) = 0

is rearranged into:

x = g(x)

Then the iteration is:

xₙ₊₁ = g(xₙ)

Starting from an initial guess x₀, the process continues until:

|xₙ₊₁ - xₙ| < tolerance

Advantages

Simple to implement

Conceptually straightforward

Disadvantages

Convergence depends heavily on the choice of g(x)

Some rearrangements converge slowly

Some rearrangements do not converge at all

A common local convergence condition is:

|g'(x)| < 1

near the fixed point.

22. Newton-Raphson Method

Newton-Raphson uses the derivative of the function.

The iteration formula is:

xₙ₊₁ = xₙ - f(xₙ) / f'(xₙ)

Starting with an initial guess x₀, the method repeatedly improves the approximation.

Advantages

Usually converges very quickly near a suitable root

Often much faster than Bisection

Disadvantages

Requires the derivative

Sensitive to the initial guess

Can fail when the derivative is zero or very small

Can converge to a different root than expected

23. Comparison of Root-Finding Methods

Method

Derivative Required

Initial Interval

Speed

Reliability

Bisection

No

Yes

Slow

Very high

Fixed-Point

No

No

Variable

Variable

Newton-Raphson

Yes

No

Usually fast

Variable

A useful mental model:

Bisection
    ↓
Reliable but slow

Fixed Point
    ↓
Simple but convergence-dependent

Newton-Raphson
    ↓
Fast but more sensitive

24. Choosing a Method

Use Bisection when reliability is more important than speed and you have a valid sign-changing interval.

Use Fixed-Point Iteration when the equation naturally has a good fixed-point form and convergence can be established.

Use Newton-Raphson when the derivative is available and you have a reasonably good initial guess.

In practical numerical computing, it is often useful to combine methods. For example, Bisection can first provide a safe approximation, followed by Newton-Raphson for faster convergence.

25. Convergence and Tolerance

Numerical methods usually stop when an approximation is sufficiently close to the root.

A typical condition is:

abs(x_new - x_old) < tolerance

For example:

tolerance = 1e-10

A maximum iteration count should also be used:

max_iterations = 100

This prevents an algorithm from running indefinitely when convergence fails.

26. Example Function

Consider:

f(x) = x**3 - x - 2

We want to solve:

x³ - x - 2 = 0

For Bisection, an interval such as:

[1, 2]

can be used because:

f(1) < 0
f(2) > 0

Newton-Raphson requires:

f'(x) = 3x² - 1

Fixed-Point Iteration requires rearranging the equation into a suitable:

x = g(x)

form.

27. Recommended Learning Order

If you are learning NumPy and numerical methods from scratch, follow this order:

1. Python fundamentals
        ↓
2. NumPy arrays
        ↓
3. Indexing and slicing
        ↓
4. Array operations
        ↓
5. Broadcasting
        ↓
6. Vectorization
        ↓
7. Statistics
        ↓
8. Random number generation
        ↓
9. Linear algebra
        ↓
10. Advanced NumPy
        ↓
11. Numerical methods
        ↓
12. Bisection
        ↓
13. Fixed-Point Iteration
        ↓
14. Newton-Raphson

28. Requirements

Python 3.9+ is recommended.

Install NumPy:

pip install numpy

If graphing functionality is included in the root-finding programs:

pip install matplotlib

29. Running the Project

From the project directory:

python path/to/file.py

For example:

python Solving-Functions/Root-Finding-Methods.py

If using a virtual environment:

python -m venv .venv

Activate it on Linux/macOS:

source .venv/bin/activate

Then:

pip install numpy matplotlib

30. Goals of the Project

This project is designed to build an understanding of:

Numerical arrays

Multidimensional data

Vectorized computation

Broadcasting

Array memory concepts

Statistics

Random data generation

Linear algebra

Numerical approximation

Iterative algorithms

Convergence

Error and tolerance

Root-finding algorithms

The overall goal is to move from basic NumPy syntax to using NumPy as a tool for actual numerical computing.

License

This project is intended for educational and learning purposes.








Root-Finding Methods

This program demonstrates three classical numerical methods for solving equations of the form:

f(x) = 0

The implemented methods are:

Bisection Method

Fixed-Point Iteration

Newton-Raphson Method

The implementations are intended for learning numerical methods and understanding how iterative algorithms approximate roots.

1. Bisection Method

The Bisection Method starts with an interval [a, b] such that:

f(a) × f(b) < 0

For a continuous function, this means there is at least one root inside the interval.

The midpoint is calculated using:

c = (a + b) / 2

The algorithm then determines which half contains the sign change and repeats the process.

Algorithm

1. Choose a and b.
2. Check that f(a) × f(b) < 0.
3. Calculate c = (a + b) / 2.
4. Evaluate f(c).
5. Select the half containing the sign change.
6. Repeat until the desired tolerance is reached.

Advantages

Very reliable when the assumptions are satisfied

Does not require a derivative

Easy to understand

Disadvantages

Converges relatively slowly

Requires a valid initial bracket

2. Fixed-Point Iteration

First rewrite:

f(x) = 0

as:

x = g(x)

The iteration is then:

xₙ₊₁ = g(xₙ)

Starting with an initial approximation x₀, the algorithm repeatedly evaluates g(x).

Algorithm

1. Rewrite f(x) = 0 as x = g(x).
2. Choose an initial guess x₀.
3. Calculate x₁ = g(x₀).
4. Calculate x₂ = g(x₁).
5. Continue until convergence.

A common local convergence condition is:

|g'(x)| < 1

near the fixed point.

Advantages

Simple implementation

Does not require the derivative of the original function

Disadvantages

The rearrangement x = g(x) strongly affects convergence

Can converge slowly

Can diverge

3. Newton-Raphson Method

Newton-Raphson uses both the function and its derivative.

The iteration formula is:

xₙ₊₁ = xₙ - f(xₙ) / f'(xₙ)

Algorithm

1. Choose an initial guess x₀.
2. Evaluate f(x₀) and f'(x₀).
3. Calculate:
       x₁ = x₀ - f(x₀) / f'(x₀)
4. Repeat using the new approximation.
5. Stop when the result has converged.

Advantages

Usually very fast near a suitable root

Often requires far fewer iterations than Bisection

Disadvantages

Requires a derivative

Sensitive to the initial guess

Can fail when the derivative is zero or very small

May converge to an unexpected root

Convergence Criterion

The program can use:

abs(x_new - x_old) < tolerance

as the stopping condition.

A maximum number of iterations should also be specified:

max_iterations = 100

This prevents an unsuccessful iteration from continuing forever.

Method Comparison

Method

Derivative

Initial Bracket

Typical Speed

Main Characteristic

Bisection

No

Yes

Slow

Reliable

Fixed-Point

No

No

Variable

Depends on g(x)

Newton-Raphson

Yes

No

Fast

Sensitive to starting point

Example

Consider:

f(x) = x³ - x - 2

We want:

x³ - x - 2 = 0

For Bisection:

[a, b] = [1, 2]

because the function changes sign across the interval.

For Newton-Raphson:

f'(x) = 3x² - 1

and an initial guess such as:

x₀ = 1.5

can be used.

For Fixed-Point Iteration, the equation must first be rearranged into a suitable:

x = g(x)

form.

Important Numerical Concepts

This program also demonstrates several ideas that appear throughout numerical computing:

Approximation

Iteration

Convergence

Tolerance

Initial guesses

Initial brackets

Error

Derivatives

Stability

Failure to converge

Numerical methods do not generally produce an exact symbolic answer. Instead, they produce an approximation that is sufficiently accurate according to a chosen tolerance.

Requirements

Python 3.9+ is recommended.

Install dependencies:

pip install numpy matplotlib

Running

From the project directory:

python Root-Finding-Methods.py

If the program is located inside Solving-Functions:

python Solving-Functions/Root-Finding-Methods.py

Suggested Extensions

Once the basic implementations work, the project can be extended with:

Iteration tables

Error plots

Convergence-rate comparisons

Automatic derivative calculation

Multiple initial guesses

Multiple roots

Relative error

Absolute error

Stopping conditions based on |f(x)|

User-defined functions

Interactive graphs

Comparison of iteration counts

Hybrid Bisection/Newton methods

These extensions turn the program from a basic demonstration into a more complete numerical-analysis toolkit.
