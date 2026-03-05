# Menu Driven Calculator

while True:
    print("\n--- CALC MENU ---")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 6:
        break

    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    if choice == 1:
        print("Result:", a + b)

    elif choice == 2:
        print("Result:", a - b)

    elif choice == 3:
        print("Result:", a * b)

    elif choice == 4:
        print("Result:", a / b)

    elif choice == 5:
        print("Result:", a % b)

    else:
        print("Invalid Choice")