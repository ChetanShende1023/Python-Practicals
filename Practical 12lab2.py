"""
Question 2: Create a program that reads "employee.xlsx" of Infosys Software Solutions.
a) Print list of employees in "Automotive" domain.
b) Print details of an employee by ID (user input).
d) Print list of all Developers.
"""

import pandas as pd

# Load the excel file
# Note: Ensure 'employee.xlsx' is in the same folder as your script.
try:
    df_emp = pd.read_excel('employee.xlsx')

    # a) Employees in "Automotive" domain
    # (Assuming the column name is 'Department' or 'Domain')
    print("--- Automotive Domain Employees ---")
    auto_employees = df_emp[df_emp['Department'] == 'Automotive']
    print(auto_employees[['Employee Name', 'Department']])

    # b) Employee details by ID
    search_id = int(input("\nEnter Employee ID to search: "))
    emp_details = df_emp[df_emp['Employee ID'] == search_id]
    
    if not emp_details.empty:
        print(f"\nDetails for ID {search_id}:")
        print(emp_details)
    else:
        print("Employee ID not found.")

    # d) List of all Developers
    print("\n--- List of Developers ---")
    developers = df_emp[df_emp['Designation'] == 'Developer']
    print(developers[['Employee Name', 'Designation']])

except FileNotFoundError:
    print("Error: 'employee.xlsx' file not found. Please create the file first.")
