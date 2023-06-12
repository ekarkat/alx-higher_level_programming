#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    pair_num = [True if num % 2 == 0 else False for num in my_list]
    return pair_num
