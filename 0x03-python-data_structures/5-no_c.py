#!/usr/bin/python3
def no_c(my_string):
    c_count = []
    """Creating a s list to stor index of 'c' in my_string"""
    for i in range(len(my_string)):
        if my_string[i] == 'C' or my_string[i] == 'c':
            c_count.append(i)
    """Declaring noc to stor the first letters without c"""
    noc = my_string[0:c_count[0]]
    """loop to fill the rest of noc from mystring"""
    for i in range(len(c_count) - 1):
        noc = noc + my_string[c_count[i] + 1:c_count[i + 1]]
    """adding last element manuly because the loop stop befor finish"""
    if c_count[-1] != len(my_string) - 1:
        noc = noc + my_string[c_count[-1] + 1:]
    return (noc)
