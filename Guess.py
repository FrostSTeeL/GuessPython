#Import
import os

#Generate number
from random import randint
for _ in range(1):
    value = (randint(0, 100))

print("I picked a number between 1 and 100, can you guess it?")
guess = int(input("Enter your guess: "))

#Guess processing
while guess != value:
    if(guess > value):
        if(guess - value > 10):
            print("Your guess is way too high!")
        else:
            print("Your guess is pretty close, a little bit lower!")
        guess = int(input("Try again!: "))
    elif(guess < value):
        if(value - guess > 10):
            print("Your guess is way too low!")
        else:
            print("Your guess is pretty close, a little bit higher!")
        guess = int(input("Try again!: "))
else:
    print("You win! it was " + str(value) + "!!")

#Pause
os.system('pause')