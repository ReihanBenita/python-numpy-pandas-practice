"""
NumPy Linear Algebra Practice

This file contains practice exercises covering fundamental linear algebra
operations using NumPy.

Topics covered:
1. Solving a system of linear equations.
2. Calculating the determinant, rank, and trace of a matrix.
3. Calculating and sorting eigenvalues and eigenvectors.
4. Computing inner and outer products of vectors.

Technologies:
- Python
- NumPy

Author: Reihan(Benita)
"""

import numpy as np


# --------------------------------------------------
# Exercise 1: Solving a System of Linear Equations


A = np.array([
    [2, 3],
    [1, -2]
])

b = np.array([12, -3])

solution = np.linalg.solve(A, b)

print("Solution:", solution)


# --------------------------------------------------
# Exercise 2: Matrix Determinant, Rank, and Trace


B = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

det = np.linalg.det(B)
rank = np.linalg.matrix_rank(B)
trace = np.trace(B)

print("Matrix B:\n", B)
print("\nDeterminant:", det)
print("Rank:", rank)
print("Trace:", trace)


# --------------------------------------------------
# Exercise 3: Eigenvalues and Eigenvectors


C = np.array([
    [2, 1],
    [1, 3]
], dtype=float)

print("Matrix C:\n", C)

eigvals, eigvecs = np.linalg.eig(C)

print("\nEigenvalues:\n", eigvals)
print("\nEigenvectors (columns):\n", eigvecs)


# Sort eigenvalues in descending order
idx = np.argsort(eigvals)[::-1]

eigvals_sorted = eigvals[idx]
eigvecs_sorted = eigvecs[:, idx]

print("\nEigenvalues (sorted descending):\n", eigvals_sorted)
print("\nEigenvectors (sorted columns):\n", eigvecs_sorted)


# --------------------------------------------------
# Exercise 4: Inner and Outer Products


u = np.array([1, 2, 3])
v = np.array([4, 5, 6])

inner = np.inner(u, v)
outer = np.outer(u, v)

print("u =", u)
print("v =", v)

print("\nInner product:", inner)
print("\nOuter product:\n", outer)

# نشسته ام به در نگاه میکنم دریچه آه میکشد
# ریاضی فریبم داد، ماتریس عذابم میدهد، از نامپای وحشت دارم :)
#سخت بود ولی از پسش بر اومدم:)
