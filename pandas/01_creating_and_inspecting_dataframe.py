#Pandas Creating and Inspecting a DataFrame 
#1
import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Reihan'],
    'Age': [20, 22, 21, 23, 20],
    'Gender': ['F', 'M', 'M', 'F', 'F'],
    'Score': [85, 78, 92, 67, 95]
}

df = pd.DataFrame(data)
print("Student DataFrame:")
print(df)


mean_score = df['Score'].mean()
print("\nMean Score:", mean_score)


high_scorers = df[df['Score'] > 80]
print("\nStudents with scores above 80:")
print(high_scorers)



print("______________________________________________________________")
###################----------------------------
