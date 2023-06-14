#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    moy, weight = 0, 0
    for lis in my_list:
        moy += lis[0] * lis[1]
        weight += lis[1]
    return (moy / weight)
