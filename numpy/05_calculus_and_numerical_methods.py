"""
NumPy Calculus and Numerical Methods Practice

This file contains practice exercises involving trigonometric
functions, numerical differentiation, and numerical integration.

Topics covered:
1. Evaluating trigonometric functions using NumPy.
2. Approximating derivatives using the forward difference method.
3. Approximating definite integrals using the trapezoidal rule.

Technologies:
- Python
- NumPy

Author: Reihan(Benita)
"""

import numpy as np


# --------------------------------------------------
# Exercise 1: Trigonometric Functions


x = np.linspace(-2 * np.pi, 2 * np.pi, 100)

y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.sin(x) + np.cos(x)

print("First 5 sin(x):", y1[:5])


# --------------------------------------------------
# Exercise 2: Numerical Differentiation


def f(x1):
    return x1 ** 2


x1 = 2.0
h = 1e-5

forward_diff = (f(x1 + h) - f(x1)) / h

print("Approximate derivative at x=2:", forward_diff)
print("Exact derivative at x=2:", 2 * x1)


# --------------------------------------------------
# Exercise 3: Numerical Integration


def f(x2):
    return np.sin(x2)


a, b = 0, np.pi

n = 1000
x2 = np.linspace(a, b, n)
y = f(x2)

approx_integral = np.trapz(y, x2)

print("Approximate integral:", approx_integral)
print("Exact value:", 2)

#بلاخره:)
