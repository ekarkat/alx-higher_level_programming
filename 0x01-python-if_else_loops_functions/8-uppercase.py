#!/usr/bin/python3
def uppercase(str):
    for c in str:
        print("{}".format(chr(ord(c) - 32))
              if ord(c) >= ord('a') and ord(c) <= ord('z')
              else "{}".format(c), end="")
    print()
