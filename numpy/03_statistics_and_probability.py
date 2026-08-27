"""
NumPy Statistics and Probability Practice

This file contains practice exercises focused on basic statistical
analysis and probability concepts using NumPy.

Topics covered:
1. Generating random data and calculating the mean and standard deviation.
2. Simulating dice rolls and estimating the probability of rolling a six.
3. Calculating mean, median, variance, and standard deviation for exam scores.

Technologies:
- Python
- NumPy

Author: Reihan(Benita)
"""

import numpy as np


# --------------------------------------------------
# Exercise 1: Mean and Standard Deviation of Random Data


data = np.random.randn(1000)

print("Mean:", np.mean(data))
print("Standard Deviation:", np.std(data))


# --------------------------------------------------
# Exercise 2: Estimating the Probability of Rolling a Six


rolls = np.random.randint(1, 7, size=1000)

num_sixes = np.sum(rolls == 6)
probability = num_sixes / 1000

print("Number of 6s rolled:", num_sixes)
print("Estimated probability of rolling a 6:", probability)


# --------------------------------------------------
# Exercise 3: Statistical Analysis of Exam Scores


scores = np.array([
    11, 13, 10, 15, 18, 17, 20, 14, 12, 19, 16
])

mean = np.mean(scores)
median = np.median(scores)
variance = np.var(scores)
std_dev = np.std(scores)

print("Exam scores:", scores)
print("\nMean:", mean)
print("Median:", median)
print("Variance:", variance)
print("Standard Deviation:", std_dev)
