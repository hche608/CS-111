#Author: Hao CHEN
#Date: May 2014

import random

print("The object of this game is to guess a number between 1 and 100")
goal = random.randint(1,100)
guess = 0

while guess != goal:
    guess = int(input("Please guess the number:"))
    if guess < goal:
        print("Too low, try again.")
    elif guess > goal:
        print("Too high, try again.")
    else:
        print("Well doen!")
print("See you later.")
