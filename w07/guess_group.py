import random

playing = "yes"

while playing == "yes":

    number = random.randint(1, 10)

    guess = int(input("\nWhat is your guess? "))
    count = 1

    while guess != number:
        count = count + 1

        if guess < number:
            print("Higher")
            guess = int(input("What is your guess? "))
        elif guess > number:
            print("Lower")
            guess = int(input("What is your guess? "))
    
    print("You guessed it!\n")

    print(f"It took you {count} guesses.")
    playing = input("Would you like to play again (yes/no)? ")

print("\nThank you for playing! TTYL :) \n")
