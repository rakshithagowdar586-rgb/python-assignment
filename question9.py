def question9():
    # Input
    age = int(input("Enter age: "))
    day = input("Enter day of week: ").lower()
    tickets = int(input("Enter number of tickets: "))

 # Base price according to age
    if age < 3:
       price = 0
    elif age <= 12:
       price = 150
    elif age <= 59:
       price = 300
    else:
       price = 200

    base_price = price * tickets

 # Discount (only on Saturday and Sunday)
    if day == "saturday" or day == "sunday":
       discount = base_price * 0.20
    else:
       discount = 0

    final_price = base_price - discount

 # Output
    print("\n--- Ticket Summary ---")
    print("Base Price:", base_price)
    print("Discount:", discount)
    print("Price After Discount:", final_price)
    print("Total Amount:", final_price)
question9()