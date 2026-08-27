# Pandas Deta Cleaning
#1
import pandas as pd
import numpy as np


data = {
    'Name': ['Ali', 'Sara', 'Reza', 'Neda', 'Omid'],
    'Age': [20, np.nan, 21, 23, np.nan],
    'Score': [85, 90, np.nan, 95, 70]
}

df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)


print("\nMissing values in each column:")
print(df.isnull().sum())


mean_age = df['Age'].mean()
df['Age'].fillna(mean_age, inplace=True)

df['Score'].fillna(0, inplace=True)

print("\nDataFrame after handling missing values:")
print(df)
