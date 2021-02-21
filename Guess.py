from random import randint
for _ in range(1):
    value = (randint(0, 100))

print("I picked a number between 1 and 100, let's see if you can guess it!")

guess = int(input("Guess the number: "))

while guess != value:
    if(guess > value):
        print("Go lower ")
        guess = int(input("Guess the number again: "))
    elif(guess < value):
        print("Go higher ")
        guess = int(input("Guess the number again: "))
else:
    print("You Win !!! it was " + str(value) )

import os
os.system('pause')