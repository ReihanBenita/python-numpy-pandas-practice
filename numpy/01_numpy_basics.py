"""
NumPy Basics Practice

This file contains practice exercises covering fundamental NumPy concepts.

Topics covered:
1. Filtering even and odd numbers from a NumPy array.
2. Working with an identity matrix and matrix multiplication.
3. Finding minimum and maximum values across rows and columns.
4. Creating evenly spaced values using np.linspace.

Technologies:
- Python
- NumPy

Author: Reihan(Benita)
"""

import numpy as np


# --------------------------------------------------
# Exercise 1: Filtering Even and Odd Numbers
# --------------------------------------------------

arr = np.arange(1, 21)

even = arr[arr % 2 == 0]
odd = arr[arr % 2 != 0]

print("Even Numbers:", even)
print("Odd Numbers:", odd)


# --------------------------------------------------
# Exercise 2: Identity Matrix and Matrix Multiplication
# --------------------------------------------------

I = np.eye(5)
A = np.random.rand(5, 5)

result = np.dot(A, I)
is_equal = np.allclose(A, result)

print("Matrix A:")
print(A)

print("\nIdentity Matrix:")
print(I)

print("\nProduct of matrices:")
print(result)

print("\nIs the product equal to A?", is_equal)


# --------------------------------------------------
# Exercise 3: Minimum and Maximum Values by Row and Column
# --------------------------------------------------

B = np.random.randint(1, 51, size=(3, 3))

print("Matrix B:")
print(B)

max_rows = np.max(B, axis=1)
min_rows = np.min(B, axis=1)

max_cols = np.max(B, axis=0)
min_cols = np.min(B, axis=0)

print("\nMaximum value per row:", max_rows)
print("Minimum value per row:", min_rows)

print("\nMaximum value per column:", max_cols)
print("Minimum value per column:", min_cols)


# --------------------------------------------------
# Exercise 4: Creating Evenly Spaced Values with np.linspace
# --------------------------------------------------

arr = np.linspace(0, 1, 10)

print(arr)
