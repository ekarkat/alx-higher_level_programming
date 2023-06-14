#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    newset_1 = set_1.difference(set_2)
    newset_2 = set_2.difference(set_1)
    newset = newset_1.union(newset_2)
    return newset
