"""
Lab Assignment-1
Question: Create a class Employee inherits it into another class Manager. 
Add methods to get input & print information of employees. 
Consider the attributes name, age, salary, address etc. 
Process the information of 10 managers.
"""

class Employee:
    def __init__(self):
        # Initialize attributes
        self.name = ""
        self.age = 0
        self.salary = 0.0
        self.address = ""

    def get_input(self):
        # Method to take input for employee details
        self.name = input("Enter Name: ")
        self.age = int(input("Enter Age: "))
        self.salary = float(input("Enter Salary: "))
        self.address = input("Enter Address: ")

    def print_info(self):
        # Method to display employee details
        print(f"Name: {self.name} | Age: {self.age} | Salary: {self.salary} | Address: {self.address}")

class Manager(Employee):
    # Manager class inherits from Employee
    def get_manager_data(self, count):
        print(f"\n--- Enter details for Manager {count} ---")
        self.get_input()

def main():
    managers_list = []
    # Loop to process information for 10 managers
    for i in range(1, 11):
        m = Manager()
        m.get_manager_data(i)
        managers_list.append(m)

    print("\n" + "="*40)
    print("DISPLAYING INFORMATION OF 10 MANAGERS")
    print("="*40)
    for m in managers_list:
        m.print_info()

if __name__ == "__main__":
    main()
