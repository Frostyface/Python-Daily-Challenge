#!/bin/python3

'''
Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess 
the number, then tell them whether they guessed too low, too high, or exactly right. 
(Hint: remember to use the user input lessons from the very first exercise)

Extras:

Keep the game going until the user types “exit”
Keep track of how many guesses the user has taken, and when the game ends, print this out.
'''

import random

rand = random.randint(1,9)
guesses = 0


while True:

    guess = int(input("Enter a number between 1 and 9: "))

    if guess > rand:
        print("Guess is less than the number")
        guesses += 1
    elif guess < rand:
        print("Guess is greater than number")
        guesses += 1
    elif guess == rand:
        guesses += 1
        print("Congrats! You found the number in " + str(guesses) + " guesses!")
    else:
        print("Unexpected input....")

