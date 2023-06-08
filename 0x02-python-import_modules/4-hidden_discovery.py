#!/usr/bin/python3
import hidden_4

if __name__ == "__main__":
    list = dir(hidden_4)
    for ar in list:
        if ar[:2] != "__":
            print("{}".format(ar))
