"""
Import a dataset of new recruitments in companies such as Microsoft, Google, Amazon, IBM, Deliotte,
Capmemini, ATOS Origin, Amdocs etc.
Generate & visualize reports of new recruitments using:
a) Bar Chart, b) Pie Chart, c) Customize Pie Chart, d) Doughnut Chart
Compare the new recruitments in IBM & Amdocs using visualization.
"""

import matplotlib.pyplot as plt

# Dataset for new recruitments
companies = ['Microsoft', 'Google', 'Amazon', 'IBM', 'Deloitte', 'Capgemini', 'ATOS Origin', 'Amdocs']
hires = [1200, 1500, 1100, 950, 800, 600, 450, 700]

# a) Bar Chart
plt.figure(figsize=(10, 5))
plt.bar(companies, hires, color='skyblue', edgecolor='black')
plt.title('New Recruitments in Companies (2026)')
plt.xlabel('Company Name')
plt.ylabel('Number of Recruitments')
plt.xticks(rotation=45)
plt.show()

# b) & c) Pie Chart & Customized Pie Chart (Exploding IBM and Amdocs)
plt.figure(figsize=(8, 8))
explode = [0.1 if (c == 'IBM' or c == 'Amdocs') else 0 for c in companies]
plt.pie(hires, labels=companies, autopct='%1.1f%%', explode=explode, shadow=True, startangle=140)
plt.title('Recruitment Distribution (IBM & Amdocs Highlighted)')
plt.show()

# d) Doughnut Chart
plt.figure(figsize=(8, 8))
plt.pie(hires, labels=companies, autopct='%1.1f%%', pctdistance=0.85)
# Draw a white circle at the center to create the "hole"
centre_circle = plt.Circle((0,0), 0.70, fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)
plt.title('Recruitment Doughnut Chart')
plt.show()

# Comparison: IBM vs Amdocs
plt.figure(figsize=(6, 5))
comp_labels = ['IBM', 'Amdocs']
comp_values = [hires[3], hires[7]] # Indices for IBM and Amdocs
plt.bar(comp_labels, comp_values, color=['blue', 'green'])
plt.title('Comparison: IBM vs Amdocs New Recruitments')
plt.ylabel('Count')
plt.show()
