def question10():
    balance = 10000

    while True:
        print("\n1.Check Balance")
        print("2.Deposit")
        print("3.Withdraw")
        print("4.Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            print("Balance:", balance)

        elif choice == "2":
            amount = float(input("Enter deposit amount: "))
            balance += amount
            print("Deposited Successfully")
            print("Updated Balance:", balance)

        elif choice == "3":
            amount = float(input("Enter withdraw amount: "))

            if amount > balance:
                print("Not enough balance")
            elif balance - amount < 500:
                print("Minimum 500 balance required")
            else:
                balance -= amount
                print("Withdrawal Successful")
                print("Updated Balance:", balance)

        elif choice == "4":
            print("Exit")
            break

        else:
            print("Invalid choice")

question10()