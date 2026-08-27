"""
Pandas Merging and Joining Data Practice

This file contains a practice exercise focused on combining
multiple DataFrames and performing calculations on the merged data.

Topics covered:
1. Creating multiple DataFrames.
2. Merging DataFrames using a common key.
3. Calculating row-wise averages.
4. Finding the student with the highest average score.

Technologies:
- Python
- Pandas

Author: Reihan(Benita)
"""

import pandas as pd

# Exercise 1: Creating Student Information Data
students = pd.DataFrame({
    'ID': [1, 2, 3, 4, 5],
    'Name': ['Ali', 'Sara', 'Reza', 'Neda', 'Omid'],
    'Age': [20, 22, 21, 23, 22]
})


# Exercise 2: Creating Student Scores Data
scores = pd.DataFrame({
    'ID': [1, 2, 3, 4, 5],
    'Math': [85, 90, 75, 95, 60],
    'English': [78, 88, 80, 92, 65],
    'Science': [90, 95, 70, 98, 70]
})

print("Student Information:")
print(students)

print("\nScores:")
print(scores)

# Exercise 3: Merging the DataFrames
merged = pd.merge(students, scores, on='ID')

print("\nMerged Data:")
print(merged)


# Exercise 4: Calculating Average Scores
merged['Average'] = merged[['Math', 'English', 'Science']].mean(axis=1)

print("\nData with Average Column:")
print(merged)


# Exercise 5: Finding the Student with the Highest Average
top_student = merged.loc[merged['Average'].idxmax()]

print("\nStudent with the Highest Average:")
print(f"Name: {top_student['Name']}")
print(f"Average Score: {top_student['Average']:.2f}")

# Finally :)
# بلاخره تمام شد
# به پایان آمد این دفتر حکایت همچنان باقیست
