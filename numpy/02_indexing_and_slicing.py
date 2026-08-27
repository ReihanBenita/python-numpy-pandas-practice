"""
NumPy Indexing and Slicing Practice

This file contains practice exercises focused on indexing, slicing,
Boolean indexing, flattening, and reshaping NumPy arrays.

Topics covered:
1. Accessing rows, columns, and submatrices using indexing and slicing.
2. Using Boolean indexing to modify specific array elements.
3. Flattening and reshaping multidimensional arrays.

Technologies:
- Python
- NumPy

Author: Reihan(Benita)
"""

import numpy as np


# --------------------------------------------------
# Exercise 1: Indexing and Slicing a 4x4 Matrix
# --------------------------------------------------

arr = np.arange(1, 17).reshape(4, 4)

print("First row:", arr[0, :])
print("Last column:", arr[:, -1])
print("2x2 submatrix:", arr[1:3, 1:3])


# --------------------------------------------------
# Exercise 2: Boolean Indexing and Modifying Odd Values
# --------------------------------------------------

arr = np.arange(1, 16)

print("Original array:")
print(arr)

arr[arr % 2 != 0] = -1

print("\nModified array:")
print(arr)


# --------------------------------------------------
# Exercise 3: Flattening and Reshaping a Matrix
# --------------------------------------------------

matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print("Original 3x3 matrix:")
print(matrix)

flat = matrix.flatten()

print("\nFlattened array:")
print(flat)

reshaped = flat.reshape(3, 3)

print("\nReshaped 3x3 matrix:")
print(reshaped)
