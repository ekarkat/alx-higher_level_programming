#!/usr/bin/python3
def print_last_digit(number):
    newnumber = number
    if number < 0:
        newnumber = -number
    print("{}".format(newnumber % 10), end="")
    return newnumber % 10
