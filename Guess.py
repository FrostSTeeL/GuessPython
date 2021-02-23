# Import
import os

# Generate number
from random import randint
for _ in range(1):
    value = (randint(1, 100))

tries = 1

print("I picked a number between 1 and 100, can you guess it?")
guess = int(input("Enter your guess: "))

# Guess processing
while guess != value:

    # Try counter
    tries = tries + 1
    
    # If the guess is higher
    if(guess > value):
        if(guess - value > 10):
            print("Your guess is too high, go way lower!")
        elif(guess - value <= 5):
            print("You are almost there, a tiny bit lower!")
        elif(guess - value <= 10):
            print("Your guess is pretty close, a little bit lower!")
        guess = int(input("Try again!: "))

    # If the guess is lower
    elif(guess < value):
        if(value - guess >= 10):
            print("Your guess is too low, go way higher!")
        elif(value - guess <= 5):
            print("You are almost there, a tiny bit higher!")
        elif(value - guess <= 10):
            print("Your guess is pretty close, a little bit higher!")
        guess = int(input("Try again!: "))
else:
    print("You win! it was " + str(value) + "!!")
    print("It took you " + str(tries) + " tries to guess the number!")

# Pause
os.system('pause')
