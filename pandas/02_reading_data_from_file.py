#Pandas Reading Data from a File 
#1
import pandas as pd

df = pd.read_csv('students.csv')


print("First 3 rows of the data:")
print(df.head(3))


mean_scores = df[['Math', 'English', 'Science']].mean()
print("\nMean score for each subject:")
print(mean_scores)


top_science = df.loc[df['Science'].idxmax()]
print("\nTop student in Science:")
print("Name:", top_science['Name'])
print("Science Score:", top_science['Science'])
#بماند به یادگار که به خاطر یه اسپیس کل کدم کار نمیکرد و کلی بهم ارور داد:)فقط به خاطر یه اسپیس کوچولو:)
#من آرومم:))))
print("______________________________________________________________")
###################----------------------------