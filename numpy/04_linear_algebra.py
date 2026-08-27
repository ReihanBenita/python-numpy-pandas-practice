# Numpy Linear Algebra 
#1
import numpy as np
A = np.array([[2, 3], [1, -2]]) 
b = np.array([12, -3]) 
solution = np.linalg.solve(A, b) 
print('Solution:', solution)
print("______________________________________________________________")
###################----------------------------
# Numpy Linear Algebra 
#2
import numpy as np

B = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])


det = np.linalg.det(B)


rank = np.linalg.matrix_rank(B)

trace = np.trace(B)

print("Matrix B:\n", B)
print("\nDeterminant:", det)
print("Rank:", rank)
print("Trace:", trace)
print("______________________________________________________________")
###################----------------------------
# Numpy Linear Algebra 
#3
import numpy as np

C= np.array([[2, 1],
              [1, 3]], dtype=float)

print(" matrix C:\n",C)
eigvals, eigvecs = np.linalg.eig(C)

print("\nEigenvalues:\n", eigvals)
print("\nEigenvectors (columns):\n", eigvecs)


idx = np.argsort(eigvals)[::-1]  
eigvals_sorted = eigvals[idx]
eigvecs_sorted = eigvecs[:, idx]
print("\nEigenvalues (sorted desc):\n", eigvals_sorted)
print("\nEigenvectors (sorted, columns are eigenvectors):\n", eigvecs_sorted)
#نشسته ام به در نگاه میکنم دریچه آه میکشد 
#ریاضی فریبم داد، ماتریس عذابم میدهد،از نامپای وحشت دارم:)
print("______________________________________________________________")
###################----------------------------
# Numpy Linear Algebra 
#4
import numpy as np

u = np.array([1, 2, 3])
v = np.array([4, 5, 6])

inner = np.inner(u, v)
outer = np.outer(u, v)

print("u =", u)
print("v =", v)
print("\nInner product:", inner)
print("\nOuter product:\n", outer)
print("______________________________________________________________")
###################----------------------------
#Finally:)
#hooof