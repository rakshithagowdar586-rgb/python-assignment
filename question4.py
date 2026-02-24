def question4():
    import datetime

 #  birth year
    birth_year = int(input("Enter your birth year: "))

 # Get current date
    today = datetime.datetime.now()

 # Calculate age
    age = today.year - birth_year

    print("\n----- Age Details -----")
    print("Age in Years:", age)
    print("Age in Months:", age * 12)
    print("Age in Days:", age * 365)
    print("Age in Hours:", age * 365 * 24)
    print("Age in Minutes:", age * 365 * 24 * 60)
    print("Years until 100:", 100 - age)
question4()