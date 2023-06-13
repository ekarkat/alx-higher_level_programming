#!/usr/bin/python3
def no_c(my_string):
    noc = ""
    for ch in my_string:
        if ch != 'c' and ch != 'C':
            noc = noc + "{}".format(ch)
    return (noc)
