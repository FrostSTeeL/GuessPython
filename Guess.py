# import
import random
import os

# variables
play_game = "y"

# game loop
while play_game.lower() == "y":

    # try counter variable
    tries = 1

    print("Hello, i am going to pick a number between 1 and any number you like and you will try to guess it")

    # game variables
    upper_limit = int(input("Choose a number: "))
    number = random.randint(1, int(upper_limit))

    # pussy check
    while upper_limit < 50:
        print("below 50 would be too easy don't you think?")
        upper_limit = int(input("Choose a number: "))
    print("I picked a number between 1 and " +
          str(upper_limit) + ", can you guess it?")
    guess = int(input("Take a guess: "))

    # guess computation
    while guess != number:
        tries = tries + 1
        if (guess > number):
            if (guess - number > upper_limit / 6):
                print("Your guess is really high")
            elif (guess - number <= upper_limit / 20):
                print("Really close now, go a little lower")
            elif (guess - number <= upper_limit / 6):
                print("Still a bit high, but close!")
            guess = int(input("Guess again: "))
        elif (guess < number):
            if (number - guess > upper_limit / 6):
                print("Your guess is really low")
            elif (number - guess <= upper_limit / 20):
                print("Really close now, go a little higher")
            elif (number - guess <= upper_limit / 6):
                print("Still a bit low, but close!")
            guess = int(input("Guess again: "))
    else:
        print("You win! Number was " + str(number) +
              " and it took you " + str(tries) + " tries to guess")

# try again?
    play_game = input("Wanna try again? y/n: ")

# exit
print("Thank you for playing!")
os.system("pause")
