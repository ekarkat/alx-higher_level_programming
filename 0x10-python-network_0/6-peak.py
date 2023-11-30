#!/usr/bin/python3

def find_peak(list_of_integers):
    """Find a peak in a list of unsorted integers."""
    if not list_of_integers:
        return None
    elif len(list_of_integers) == 1:
        return list_of_integers[0]
    else:
        i = 0
        pik = list_of_integers[1]
        lis = list_of_integers
        while i < len(list_of_integers) -1:
            if lis[i] >= lis[i + 1]:
                pik = lis[i]
            else:
                pik = lis[i + 1]
            i += 1
    return (pik)
