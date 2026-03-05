# Menu Driven Bank Account Program

balance = 0

while True:
    print("\n--- BANK MENU ---")
    print("1. Display Balance")
    print("2. Deposit Amount")
    print("3. Withdraw Amount")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("Current Balance:", balance)

    elif choice == 2:
        amount = float(input("Enter amount to deposit: "))
        balance += amount
        print("Amount Deposited Successfully")

    elif choice == 3:
        amount = float(input("Enter amount to withdraw: "))
        if amount <= balance:
            balance -= amount
            print("Amount Withdrawn Successfully")
        else:
            print("Insufficient Balance")

    elif choice == 4:
        break

    else:
        print("Invalid Choice")