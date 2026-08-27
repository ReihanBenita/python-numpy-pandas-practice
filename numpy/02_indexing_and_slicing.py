#Numpy Indexing and Slicing 
#1
import numpy as np
arr = np.arange(1, 17).reshape(4, 4) 
print('First row:', arr[0, :]) 
print('Last column:', arr[:, -1]) 
print('2×2 submatrix:', arr[1:3, 1:3]) 
print("______________________________________________________________")
###################----------------------------
#Numpy Indexing and Slicing 
#2
import numpy as np

ar = np.arange(1, 16)
print("Original array:")
print(ar)

ar[ar % 2 != 0] = -1
print("\nModified array:")
print(ar)
print("______________________________________________________________")
###################----------------------------
#Numpy Indexing and Slicing 
#3
import numpy as np

A = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

print("Original 3×3 matrix:")
print(A)


flat = A.flatten()
print("\nFlattened array:")
print(flat)


reshaped = flat.reshape(3, 3)
print("\nReshaped 3×3 matrix:")
print(reshaped)
print("______________________________________________________________")
###################----------------------------
