def question14():
    # Factorial Program with Step-by-Step Display

 num = int(input("Enter a number: "))

 if num < 0:
    print("Factorial is not defined for negative numbers.")
    
 elif num == 0:
    print("0! = 1")
    
 else:
    factorial = 1
    print(f"\nStep-by-step calculation of {num}! :")
    
    for i in range(num, 0, -1):
        print(i, end="")
        if i != 1:
            print(" × ", end="")
        factorial *= i
    
    print("\n\nFactorial =", factorial)
question14()