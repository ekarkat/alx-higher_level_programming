#!/usr/bin/python3
def roman_to_int(roman_string):
    roman = {"I": 1, "V": 5, "X": 10, "C": 100, "D": 500, "L": 50, "M": 1000}
    number = 0
    i = 0
    if roman_string is None or (type(roman_string) is not str):
        return 0
    while i < len(roman_string):
        if roman_string[i] in roman:
            val = roman[roman_string[i]]
            if i + 1 < len(roman_string) and val < roman[roman_string[i + 1]]:
                number = number + (roman[roman_string[i + 1]] - val)
                i = i + 2
            else:
                number = number + val
                i = i + 1
        else:
            return 0
    return number
