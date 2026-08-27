"""
Pandas Reading Data from a File

This file contains a practice exercise focused on reading
and analyzing data from a CSV file using Pandas.

Topics covered:
1. Reading data from a CSV file.
2. Inspecting the first rows of a DataFrame.
3. Calculating the mean score for multiple columns.
4. Finding the student with the highest Science score.

Technologies:
- Python
- Pandas

Author: Reihan(Benita)
"""

import pandas as pd

# Exercise 1: Reading Data from a CSV File
df = pd.read_csv('students.csv')

# Inspecting the First 3 Rows
print("First 3 rows of the data:")
print(df.head(3))

# Calculating Mean Scores
mean_scores = df[['Math', 'English', 'Science']].mean()

print("\nMean score for each subject:")
print(mean_scores)

# Finding the Top Student in Science
top_science = df.loc[df['Science'].idxmax()]

print("\nTop student in Science:")
print("Name:", top_science['Name'])
print("Science Score:", top_science['Science'])

# بماند به یادگار که به خاطر یه اسپیس کل کدم کار نمیکرد و کلی بهم ارور داد:)
# من آرومم:))))
