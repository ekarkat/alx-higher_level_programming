#!/usr/bin/python3
for i in range(100):
    deli = ", " if i < 99 else ""
    print("{}".format(i), end=deli)
print()
