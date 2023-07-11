#!/usr/bin/python3
'''Module 0'''


def read_file(filename=""):
    '''Function to print the content of a file'''
    with open(filename, encoding="utf-8") as f:
        f_content = f.read()
        print(f_content)
