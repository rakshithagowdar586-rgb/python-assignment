def question13():
    # Program to calculate Sum, Average, Maximum and Minimum

    n = int(input("How many numbers do you want to add? "))

    total = 0
    maximum = None
    minimum = None

    for i in range(n):
     num = int(input("Enter number: "))
    
    total += num
    
    if maximum is None or num > maximum:
        maximum = num
        
    if minimum is None or num < minimum:
        minimum = num

    average = total / n

    print("\nResults:")
    print("Sum =", total)
    print("Average =", average)
    print("Maximum =", maximum)
    print("Minimum =", minimum)
question13()