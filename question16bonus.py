def question16bonus():
     import random

     best_score = None   # To store minimum attempts used

     while True:
       number = random.randint(1, 100)
       attempts = 7
       used_attempts = 0
       guessed = False

     print("\n Number Guessing Game (1-100)")
     print("You have 7 attempts to guess the number.")

     while attempts > 0:
           guess = int(input("\nEnter your guess: "))
           used_attempts += 1

           if guess == number:
             print(f"Correct! You guessed it in {used_attempts} attempts.")
             guessed = True

            # Update best score
           if best_score is None or used_attempts < best_score:
             best_score = used_attempts
             print(" New Best Score!")

             break

           elif guess > number:
             print("Too high!")
           else:
             print("Too low!")

        # Hint if close (within 5)
           if abs(guess - number) <= 5:
             print(" Very close! (within 5)")

           attempts -= 1
           print("Attempts remaining:", attempts)

           if not guessed:
            print(f"\nYou lost! The number was {number}.")

           if best_score is not None:
            print(" Best Score so far:", best_score, "attempt(s)")

           play_again = input("\nPlay again? (yes/no): ").lower()
           if play_again != "yes":
             print("Thanks for playing! ")
             break
question16bonus()