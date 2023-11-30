#!/usr/bin/python3
"""Find a peak in a list of unsorted integers."""


def find_peak(list_of_integers):
    """Find a peak in a list of unsorted integers."""
    if not list_of_integers:
        return None
    elif len(list_of_integers) == 1:
        return list_of_integers[0]

    i = 1
    li = list_of_integers
    while i < len(list_of_integers) - 1:
        if li[i] > li[i - 1] and li[i] > li[i + 1]:
            return (li[i])
        i += 1
    return (max(list_of_integers))
