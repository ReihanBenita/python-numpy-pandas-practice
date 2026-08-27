"""
Pandas Creating and Inspecting a DataFrame

This file contains a practice exercise focused on creating
and inspecting a Pandas DataFrame.

Topics covered:
1. Creating a DataFrame from a dictionary.
2. Calculating the mean of a column.
3. Filtering rows based on a condition.

Technologies:
- Python
- Pandas

Author: Reihan(Benita)
"""

import pandas as pd

# Exercise 1: Creating and Inspecting a DataFrame

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Reihan'],
    'Age': [20, 22, 21, 23, 20],
    'Gender': ['F', 'M', 'M', 'F', 'F'],
    'Score': [85, 78, 92, 67, 95]
}

df = pd.DataFrame(data)

print("Student DataFrame:")
print(df)

# Calculating the Mean Score

mean_score = df['Score'].mean()

print("\nMean Score:", mean_score)

# Filtering Students with Scores Above 80

high_scorers = df[df['Score'] > 80]

print("\nStudents with scores above 80:")
print(high_scorers)
