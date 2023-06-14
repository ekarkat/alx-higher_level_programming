#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    list_t = []
    for key in a_dictionary:
        txt = "{}: ".format(key) + "{}".format(a_dictionary.get(key))
        list_t.append(txt)
    list_t.sort()
    for text in list_t:
        print("{}".format(text))
