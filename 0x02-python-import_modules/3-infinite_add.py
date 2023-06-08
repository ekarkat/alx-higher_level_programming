#!/usr/bin/python3
import sys
result = 0
if __name__ == "__main__":
    argv = sys.argv[1:]
    for i in range(len(argv)):
        result = result + int(argv[i])
    print("{}".format(result))
