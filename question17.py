def question17():
    
    value = input("Enter a word or number: ")
    
    value_lower = value.lower()   # ← Added ()
    reversed_value = value_lower[::-1]
    
    print("\nStep-by-step verification:")
    print("Original value  :", value_lower)
    print("Reversed value  :", reversed_value)

    if value_lower == reversed_value:
        print("\nResult: It is a Palindrome")
    else:
        print("\nResult: It is NOT a Palindrome")

question17()