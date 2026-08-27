"""
Pandas Grouping and Aggregation Practice

This file contains a practice exercise focused on grouping
and aggregating data using Pandas.

Topics covered:
1. Creating a DataFrame from sales data.
2. Grouping data by region.
3. Calculating total revenue for each region.
4. Calculating average revenue for each region.
5. Identifying the region with the highest total revenue.

Technologies:
- Python
- Pandas

Author: Reihan(Benita)
"""

import pandas as pd

# Exercise 1: Creating a Sales DataFrame
data = {
    'Region': [
        'North', 'South', 'East', 'West',
        'North', 'South', 'East', 'West'
    ],
    'Salesperson': [
        'Ali', 'Sara', 'Reza', 'Neda',
        'Omid', 'Mina', 'Hassan', 'Laleh'
    ],
    'Revenue': [
        12000, 15000, 11000, 18000,
        13000, 16000, 9000, 20000
    ]
}

df = pd.DataFrame(data)

print("Sales Data:")
print(df)

# Exercise 2: Total Revenue by Region
total_revenue = df.groupby('Region')['Revenue'].sum()

print("\nTotal Revenue per Region:")
print(total_revenue)


# Exercise 3: Average Revenue by Region
avg_revenue = df.groupby('Region')['Revenue'].mean()

print("\nAverage Revenue per Salesperson in each Region:")
print(avg_revenue)


# Exercise 4: Finding the Region with the Highest Revenue
top_region = total_revenue.idxmax()
top_revenue = total_revenue.max()

print("\nRegion with the Highest Total Revenue:")
print(f"{top_region} — ${top_revenue}")
