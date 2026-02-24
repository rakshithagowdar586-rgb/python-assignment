def question20():

    # 1. Factorial
    def factorial(n):
        if n < 0:
            return "Not defined for negative numbers"
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

    # 2. Prime Check
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

    # 3. Fibonacci
    def fibonacci(n):
        if n <= 0:
            return "Invalid input"
        elif n == 1:
            return 0
        elif n == 2:
            return 1
        a, b = 0, 1
        for _ in range(3, n + 1):
            a, b = b, a + b
        return b

    # 4. Sum of Digits
    def sum_of_digits(n):
        return sum(int(digit) for digit in str(abs(n)))

    # 5. Reverse Number
    def reverse_number(n):
        return int(str(abs(n))[::-1])

    # 6. Armstrong Number
    def is_armstrong(n):
        num_str = str(n)
        power = len(num_str)
        total = sum(int(digit) ** power for digit in num_str)
        return total == n

    # 7. GCD
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    # 8. LCM
    def lcm(a, b):
        return abs(a * b) // gcd(a, b)

    # 9. Perfect Number
    def is_perfect_number(n):
        if n <= 0:
            return False
        total = 0
        for i in range(1, n):
            if n % i == 0:
                total += i
        return total == n

    # 10. Menu
    while True:
        print("\n===== MATH MENU =====")
        print("1. Factorial")
        print("2. Prime Check")
        print("3. Fibonacci")
        print("4. Sum of Digits")
        print("5. Reverse Number")
        print("6. Armstrong Number")
        print("7. GCD")
        print("8. LCM")
        print("9. Perfect Number")
        print("10. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            n = int(input("Enter number: "))
            print("Result:", factorial(n))

        elif choice == "2":
            n = int(input("Enter number: "))
            print("Is Prime?:", is_prime(n))

        elif choice == "3":
            n = int(input("Enter position: "))
            print("Fibonacci:", fibonacci(n))

        elif choice == "4":
            n = int(input("Enter number: "))
            print("Sum of digits:", sum_of_digits(n))

        elif choice == "5":
            n = int(input("Enter number: "))
            print("Reversed number:", reverse_number(n))

        elif choice == "6":
            n = int(input("Enter number: "))
            print("Is Armstrong?:", is_armstrong(n))

        elif choice == "7":
            a = int(input("Enter first number: "))
            b = int(input("Enter second number: "))
            print("GCD:", gcd(a, b))

        elif choice == "8":
            a = int(input("Enter first number: "))
            b = int(input("Enter second number: "))
            print("LCM:", lcm(a, b))

        elif choice == "9":
            n = int(input("Enter number: "))
            print("Is Perfect Number?:", is_perfect_number(n))

        elif choice == "10":
            print("Exiting")
            break

        else:
            print("Invalid choice!")


question20()