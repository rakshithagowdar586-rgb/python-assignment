def question16():
    import random

    while True:
     number = random.randint(1, 100)
     attempts = 7
     guessed = False

     print("\n Welcome to the Number Guessing Game!")
     print("I have chosen a number between 1 and 100.")
     print("You have 7 attempts to guess it.")

     while attempts > 0:
        guess = int(input("\nEnter your guess: "))

        if guess == number:
            print(f" Congratulations! You guessed the number in {8 - attempts} attempts.")
            guessed = True
            break

        elif guess > number:
            attempts -= 1
            print("Too high!")
            print("Attempts remaining:", attempts)

        else:
            attempts -= 1
            print("Too low!")
            print("Attempts remaining:", attempts)

        if not guessed:
           print(f"\n You lost! The correct number was {number}.")

        play_again = input("\nDo you want to play again? (yes/no): ").lower()

        if play_again != "yes":
           print("Thanks for playing! ")
           break
       
question16()