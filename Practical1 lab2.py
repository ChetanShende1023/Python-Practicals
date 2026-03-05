# Vendor Annual Purchase Report Program

# Vendor details
name = input("Enter Vendor Name: ")
year = input("Enter Year of Association: ")
contact = input("Enter Contact Number: ")
email = input("Enter Email ID: ")

# Monthly purchases
total_purchase = 0

print("\nEnter purchase amount for 12 months:")

for i in range(1, 13):
    purchase = float(input(f"Month {i} Purchase: "))
    total_purchase += purchase

# Display report
print("\n----- Vendor Details -----")
print("Vendor Name:", name)
print("Year of Association:", year)
print("Contact Number:", contact)
print("Email ID:", email)

print("\n----- Annual Purchase Report -----")
print("Total Annual Purchase:", total_purchase)