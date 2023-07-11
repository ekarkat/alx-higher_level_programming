#!/usr/bin/python3
'''Module 6'''
import json


def load_from_json_file(filename):
    '''function that returns the JSON representation
        of an object (string):
    '''
    with open(filename, 'r', encoding="utf-8") as f:
        return json.load(f)
