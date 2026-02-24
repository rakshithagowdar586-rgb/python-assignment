def question6():
    # Input marks
    m1 = int(input("Enter marks for subject 1: "))
    m2 = int(input("Enter marks for subject 2: "))
    m3 = int(input("Enter marks for subject 3: "))
    m4 = int(input("Enter marks for subject 4: "))
    m5 = int(input("Enter marks for subject 5: "))

 # Total and percentage
    total = m1 + m2 + m3 + m4 + m5
    percentage = total / 5

 # Pass or Fail
    if m1 >= 40 and m2 >= 40 and m3 >= 40 and m4 >= 40 and m5 >= 40:
       result = "Pass"
    else:
       result = "Fail"

 # Grade
    if percentage >= 90:
       grade = "A"
    elif percentage >= 75:
       grade = "B"
    elif percentage >= 60:
       grade = "C"
    elif percentage >= 50:
       grade = "D"
    else:
        grade = "F"

 # Output
    print("\nMarks:", m1, m2, m3, m4, m5)
    print("Total:", total)
    print("Percentage:", percentage, "%")
    print("Grade:", grade)
    print("Result:", result)
question6()