"""
Task 2:
Create a program to play a number guessing game
There should be a function:
title()
displays instructions and how to play

game()
plays the games
"""

import random

def title():
    print("pick a number between 1 and 10 and see if it matches the radndom number")

def game():
    num = int(input("number: "))
    randNum = int(random.randint(1,10))
    if num == randNum:
        print("correct")
    else:
        print(f"Wrong, the correct number was {randNum}")

title()

game()

    

