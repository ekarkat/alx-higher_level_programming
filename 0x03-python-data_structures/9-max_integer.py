#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    temp = my_list[0]
    for i in range(len(my_list) - 1):
        if temp < my_list[i + 1]:
            temp = my_list[i + 1]

    return temp
