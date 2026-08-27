#pandas 
#1
import pandas as pd

students = pd.DataFrame({
    'ID': [1, 2, 3, 4, 5],
    'Name': ['Ali', 'Sara', 'Reza', 'Neda', 'Omid'],
    'Age': [20, 22, 21, 23, 22]
})

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

merged = pd.merge(students, scores, on='ID')
print("\nMerged Data:")
print(merged)

merged['Average'] = merged[['Math', 'English', 'Science']].mean(axis=1)
print("\nData with Average Column:")
print(merged)

top_student = merged.loc[merged['Average'].idxmax()]
print("\nStudent with the Highest Average:")
print(f"Name: {top_student['Name']}")
print(f"Average Score: {top_student['Average']:.2f}")
#بلاخره تمام شد
#به پایان آمد این دفتر حکایت همچنان باقیست