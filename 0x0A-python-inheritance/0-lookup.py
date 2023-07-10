#!/usr/bin/python3
'''attribute lookup function.'''


def lookup(obj):
    '''Return the list of available attributes and methods of an object'''
    return (dir(obj))
