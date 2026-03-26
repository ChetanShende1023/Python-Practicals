"""
Question 1: Using the Diamonds DataFrame:
i) Calculate the mean of price for each cut.
ii) Print count, minimum, and maximum price for each cut.
iii) Calculate and print average value of parameter x, y, and z separately.
"""

import pandas as pd

# Creating the DataFrame based on the provided table
data = {
    'carat': [0.23, 0.21, 0.23, 0.29, 0.31],
    'cut': ['Ideal', 'Premium', 'Good', 'Premium', 'Good'],
    'color': ['E', 'E', 'E', 'I', 'J'],
    'clarity': ['SI2', 'SI1', 'VS1', 'VS2', 'SI2'],
    'depth': [61.5, 59.8, 56.9, 62.4, 63.3],
    'table': [55.0, 61.0, 65.0, 58.0, 58.0],
    'price': [326, 326, 327, 334, 335],
    'x': [3.95, 3.89, 4.05, 4.20, 4.34],
    'y': [3.98, 3.84, 4.07, 4.23, 4.35],
    'z': [2.43, 2.31, 2.31, 2.63, 2.75]
}
df = pd.DataFrame(data)

# i) Mean price for each cut
print("--- Mean Price per Cut ---")
print(df.groupby('cut')['price'].mean())

# ii) Count, Min, and Max price for each cut
print("\n--- Price Statistics per Cut ---")
stats = df.groupby('cut')['price'].agg(['count', 'min', 'max'])
print(stats)

# iii) Average values of x, y, and z
print("\n--- Average of x, y, and z ---")
print(f"Average x: {df['x'].mean():.2f}")
print(f"Average y: {df['y'].mean():.2f}")
print(f"Average z: {df['z'].mean():.2f}")
