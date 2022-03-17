# Guess My Number PC Edition
# The player picks a random number between 1 and 100
# The computer tries to guess it and the computer lets
# the computer know if the guess is too high, too low
# or right on the money


print("\nWelcome to Guess My Number Computer Edition!")
print("\nYou pick the number this time!")
print("The computer will have 5 chances!\n")

import random

# set the initial values
user_number = int(input("Pick a number from 1 to 100: "))
tries = 1
computer_guess = random.randint(1,100)

# guessing loop
while computer_guess != user_number:
    tries += 1
    if tries > 5:
        print("Ha, the user is better than the computer!")
        break
    computer_guess = random.randint(1,100)
    print("Is it", computer_guess, "?")
    print("No")

if computer_guess == user_number:
    print("You guessed it!  The number was", user_number)
    print("And it only took you", tries, "tries!\n")

    input("\n\nPress the enter key to exit.")
