import random
from math import trunc
from random import randint
import time
import keyboard

dadJokes = []


def titleScreen():
    choice = input("How well do you know the Avengeful Aryans? Press 1 to begin")
    if choice == "1":
        quiz()

def quiz():
    q1 = input("True or False: There are 2 people in our group named Aryan  (T/F)")
    if q1 == "T":
        print("Correct!")
    else:
        print("Incorrect. It's in our name, duh")


    q2 = input("True or False: One of the 2 Aryans lives in Europe  (T/F)")
    if q2 == "T":
        print("Nope, we're both from North America!")
    else:
        print("Correct, we're both from North America")

    q3 = input("True or False: One Aryan may or may not have stayed awake for 35 hours  (T/F)")
    titleScreen()
    if q3 == "T":
        print("Correct, unfortunately")
    else:
        print("Incorrect, this is all a part of the coding process")

titleScreen()
