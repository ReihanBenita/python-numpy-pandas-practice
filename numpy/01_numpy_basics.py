#Numpy
#1

import numpy as np

arr = np.arange(1, 21)
even = arr[arr % 2 == 0]
odd = arr[arr % 2 != 0]

print("Even Numbers:", even)
print("Odd Numbers:", odd)

###############----------------------------------
#2
#Numpy
import numpy as np

I = np.eye(5)
A = np.random.rand(5, 5)


result = np.dot(A, I)

is_equal = np.allclose(A, result)


print("Matrix A:")
print(A)
print("\n Identity Matrix:")
print(I)
print("\n Product of matrices:")
print(result)
print("\n Is the product equal to A? ", is_equal)
print("______________________________________________________________")
#####################------------------------------
#3
#numpy
import numpy as np


B = np.random.randint(1, 51, size=(3, 3))
print("Matrix B:")
print(B)


max_rows = np.max(B, axis=1)
min_rows = np.min(B, axis=1)

max_cols = np.max(B, axis=0)
min_cols = np.min(B, axis=0)

print("\n Maximum value per row:", max_rows)
print("Minimum value per row:", min_rows)

print("\n Maximum value of each column:", max_cols)
print("Minimum value of each column:", min_cols)
print("______________________________________________________________")
#################-----------------------------------------------------
#4
#numpy
import numpy as np


arr = np.linspace(0, 1, 10)
print(arr)
print("______________________________________________________________")
##############-------------------