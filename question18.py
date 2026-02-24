def question18():
    # Function Definitions

    def add(a, b):
        return a + b

    def subtract(a, b):
        return a - b

    def multiply(a, b):
        return a * b

    def divide(a, b):
        if b == 0:
           return "Error! Division by zero is not allowed."
        return a / b

    def modulus(a, b):
        return a % b

    def power(a, b):
        return a ** b


# Main Calculator Function
    def calculator():
        while True:
           print("\n===== SIMPLE CALCULATOR =====")
           print("1. Add")
           print("2. Subtract")
           print("3. Multiply")
           print("4. Divide")
           print("5. Modulus")
           print("6. Power")
           print("7. Exit")

           choice = input("Enter your choice (1-7): ")

           if choice == "7":
            print("Exiting Calculator")
            break

           if choice in ["1", "2", "3", "4", "5", "6"]:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))

            if choice == "1":
                print("Result =", add(a, b))

            elif choice == "2":
                print("Result =", subtract(a, b))

            elif choice == "3":
                print("Result =", multiply(a, b))

            elif choice == "4":
                print("Result =", divide(a, b))

            elif choice == "5":
                print("Result =", modulus(a, b))

            elif choice == "6":
                print("Result =", power(a, b))
   
            else:
                print("Invalid choice! Please select between 1-7.")

    calculator()
question18()