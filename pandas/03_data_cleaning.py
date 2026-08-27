"""
Pandas Data Cleaning Practice

This file contains a practice exercise focused on identifying
and handling missing values in a Pandas DataFrame.

Topics covered:
1. Creating a DataFrame containing missing values.
2. Detecting missing values using isnull().
3. Calculating the mean of a column.
4. Filling missing Age values with the column mean.
5. Filling missing Score values with zero.

Technologies:
- Python
- Pandas
- NumPy

Author: Reihan(Benita)
"""

import pandas as pd
import numpy as np



# Exercise 1: Creating a DataFrame with Missing Values
data = {
    'Name': ['Ali', 'Sara', 'Reza', 'Neda', 'Omid'],
    'Age': [20, np.nan, 21, 23, np.nan],
    'Score': [85, 90, np.nan, 95, 70]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

# Exercise 2: Detecting Missing Values
print("\nMissing values in each column:")
print(df.isnull().sum())


# Exercise 3: Handling Missing Age Values
mean_age = df['Age'].mean()

df['Age'].fillna(mean_age, inplace=True)


# Exercise 4: Handling Missing Score Values

df['Score'].fillna(0, inplace=True)


print("\nDataFrame after handling missing values:")
print(df)
