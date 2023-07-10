#!/usr/bin/python3
'''Mylist child Class'''


class MyList(list):
    '''Mylist child class '''

    def print_sorted(self):
        '''Print a list in sorted ascending order.'''
        print(sorted(self))
