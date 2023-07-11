#!/usr/bin/python3
'''Module 1'''


def write_file(filename="", text=""):
    '''Function to write the content of a file'''
    with open(filename, 'w', encoding="utf-8") as f:
        return (f.write(text))
