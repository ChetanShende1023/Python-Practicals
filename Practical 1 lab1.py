# Employee Salary Calculation Program

# Input employee details
name = input("Enter Employee Name: ")
emp_id = input("Enter Employee ID: ")
department = input("Enter Department: ")
basic_salary = float(input("Enter Basic Salary: "))

# Calculations
DA = 0.92 * basic_salary
HRA = 0.58 * basic_salary
TA = 0.30 * basic_salary
LIC = 500

total_salary = basic_salary + DA + HRA + TA - LIC

# Display result
print("\n----- Employee Details -----")
print("Name:", name)
print("Employee ID:", emp_id)
print("Department:", department)

print("\n----- Salary Details -----")
print("Basic Salary:", basic_salary)
print("DA:", DA)
print("HRA:", HRA)
print("TA:", TA)
print("LIC Deduction:", LIC)
print("Total Salary:", total_salary)