#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
newnumber = number
if number < 0:
    newnumber = -number
if (newnumber % 10) == 0:
    print(f"Last digit of {number} is {newnumber % 10} and is 0")
elif (newnumber % 10) > 5:
    print(f"Last digit of {number} is {newnumber % 10} and is greater than 5")
elif (newnumber % 10) < 6:
    print(f"Last digit of {number} is {newnumber % 10} \
and is less than 6 and not 0")
