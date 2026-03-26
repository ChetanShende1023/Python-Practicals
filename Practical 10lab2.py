"""
Lab Assignment-2
Question: Create a table showing information about 5 states such as:
Name of state, Area, Population. Generate the following reports:
a) Print the complete information of states
b) Print the name of the State having largest Area
c) Print the name of State having largest population
d) Create a mechanism to calculate the population density of States
e) Determine the name of State with highest population density
"""

import pandas as pd

# Initial Data
data = {
    'State': ['Maharashtra', 'Rajasthan', 'Goa', 'Uttar Pradesh', 'Sikkim'],
    'Area': [307713, 342239, 3702, 240928, 7096],
    'Population': [112374333, 68548437, 1458545, 199812341, 610577]
}
df_states = pd.DataFrame(data)

# a) Complete Information
print("\n--- a) State Information ---")
print(df_states)

# b) Largest Area
largest_area_state = df_states.loc[df_states['Area'].idxmax(), 'State']
print(f"\n--- b) Largest Area: {largest_area_state}")

# c) Largest Population
largest_pop_state = df_states.loc[df_states['Population'].idxmax(), 'State']
print(f"--- c) Largest Population: {largest_pop_state}")

# d) Calculate Population Density (Pop / Area)
df_states['Density'] = df_states['Population'] / df_states['Area']
print("\n--- d) Population Density Added ---")
print(df_states[['State', 'Density']])

# e) Highest Density
highest_density_state = df_states.loc[df_states['Density'].idxmax(), 'State']
print(f"\n--- e) State with Highest Density: {highest_density_state}")
