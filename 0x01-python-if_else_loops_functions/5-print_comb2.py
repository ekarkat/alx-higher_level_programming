#!/usr/bin/python3
for i in range(100):
    deli = ", " if i < 99 else ""
    print("{:02d}".format(i), end=deli)
print()
