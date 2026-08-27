# Numpy Statistics and Probability 
#1
import numpy as np
data = np.random.randn(1000) 
print('Mean:', np.mean(data)) 
print('Std:', np.std(data)) 

print("______________________________________________________________")
###################----------------------------
# Numpy Statistics and Probability 
#2
import numpy as np


rolls = np.random.randint(1, 7, size=1000)

num_sixes = np.sum(rolls == 6)


probability = num_sixes / 1000

print("Number of 6s rolled:", num_sixes)
print("Estimated probability of rolling a 6:", probability)
print("______________________________________________________________")
###################----------------------------
# Numpy Statistics and Probability 
#3
import numpy as np

scores = np.array([11, 13, 10, 15, 18, 17, 20, 14, 12, 19,16])

mean = np.mean(scores)
median = np.median(scores)
variance = np.var(scores)
std_dev = np.std(scores)

print("Exam scores:", scores)
print("\nMean:", mean)
print("Median:", median)
print("Variance:", variance)
print("Standard Deviation:", std_dev)
