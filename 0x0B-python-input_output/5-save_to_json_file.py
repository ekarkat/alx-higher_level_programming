#!/usr/bin/python3
'''Module 5'''
import json


def save_to_json_file(my_obj, filename):
    '''function that returns the JSON representation
        of an object (string):
    '''
    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(my_obj, f)
