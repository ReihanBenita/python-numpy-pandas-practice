# Pandas
#1
import pandas as pd

data = {
    'Region': ['North', 'South', 'East', 'West', 'North', 'South', 'East', 'West'],
    'Salesperson': ['Ali', 'Sara', 'Reza', 'Neda', 'Omid', 'Mina', 'Hassan', 'Laleh'],
    'Revenue': [12000, 15000, 11000, 18000, 13000, 16000, 9000, 20000]
}

df = pd.DataFrame(data)
print("Sales Data:")
print(df)

total_revenue = df.groupby('Region')['Revenue'].sum()
print("\nTotal Revenue per Region:")
print(total_revenue)

avg_revenue = df.groupby('Region')['Revenue'].mean()
print("\nAverage Revenue per Salesperson in each Region:")
print(avg_revenue)


top_region = total_revenue.idxmax()
top_revenue = total_revenue.max()
print("\nRegion with the Highest Total Revenue:")
print(f"{top_region} — ${top_revenue}")
