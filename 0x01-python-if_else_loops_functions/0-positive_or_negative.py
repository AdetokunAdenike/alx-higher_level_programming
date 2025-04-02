#!/usr/bin/python3
import random

number = random.randint(-10, 10)

print(number, end="")

if number > 0:
    print(" is positive\n")
elif number == 0:
    print(" is zero\n")
elif number < 0:
    print(" is negative\n")