#!/usr/bin/python3
'''Module 4'''
import json


def from_json_string(my_str):
    '''function that returns the JSON representation
        of an object (string):
    '''
    return (json.loads(my_str))
