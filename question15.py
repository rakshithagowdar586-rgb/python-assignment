def question15():
    # Check Prime Number

 num = int(input("Enter a number to check if it is prime: "))

 if num < 0:
    print("Negative numbers are not prime.")
    
 elif num == 0 or num == 1:
    print(num, "is not a prime number.")
    
 elif num == 2:
    print("2 is a prime number.")
    
 else:
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    
    if is_prime:
        print(num, "is a prime number.")
    else:
        print(num, "is not a prime number.")
        
        # Prime Numbers in a Range

 start = int(input("Enter start of range: "))
 end = int(input("Enter end of range: "))

 print("Prime numbers in the range are:")

 for num in range(start, end + 1):
    
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num)
question15()