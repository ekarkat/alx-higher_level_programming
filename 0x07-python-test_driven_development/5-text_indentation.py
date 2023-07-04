#!/usr/bin/python3
def text_indentation(text):

    if type(text) is not str:
        raise TypeError("text must be a string")
    lent = len(text)
    i = 0
    while i < lent:
        if text[i] == '.' or text[i] == '?' or text[i] == ':':
            print(text[i], end="\n\n")
            i = i + 1
        elif text[i] == ' ' and text[i - 1] == '.' \
                or text[i - 1] == '?' or text[i - 1] == ':':
            i = i + 1
        elif text[i] == ' ' and text[i - 1] == ' ':
            i = i + 1
        elif i == lent:
            break
        elif text[i] == ' ' and text[i + 1] == ' ':
            i = i + 1
        else:
            print(text[i], end="")
            i = i + 1    

