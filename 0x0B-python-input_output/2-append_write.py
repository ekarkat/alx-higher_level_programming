#!/usr/bin/python3
'''Module 2'''


def append_write(filename="", text=""):
    '''Function to apppend a string at the end
       of a file
    '''
    with open(filename, 'a', encoding="utf-8") as f:
        return (f.write(text))
