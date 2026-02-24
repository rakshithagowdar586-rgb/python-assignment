def question11():
    # Pattern Printing Program

    print("Choose a pattern:")
    print("Pattern 1")
    print("Pattern 2")
    print("Pattern 3")
    print("Pattern 4")

    pattern = input("Enter pattern name (Pattern 1-4): ").strip()
    height = int(input("Enter height of the pattern: "))

    print("\nPattern Output:")

    if pattern== "pattern 1":
        for i in range(1, height + 1):
            for j in range(1, i + 1):
                print(j, end=" ")
        print()

    elif pattern== "pattern 2":
          for i in range(1, height + 1):
             for j in range(i):
                 print(i, end=" ")
          print()

    elif pattern == "pattern 3":
         for i in range(height, 0, -1):
             for j in range(i, 0, -1):
                 print(j, end=" ")
         print()

    elif pattern == "pattern 4":
         for i in range(1, height + 1):
             for j in range(1, i + 1):
                 print(j, end="")
         for j in range(i - 1, 0, -1):
            print(j, end="")
         print()

    else:
     print("Invalid pattern name! Please enter Pattern 1, Pattern 2, Pattern 3, or Pattern 4.")
question11()