#!/usr/bin/python3
def remove_char_at(str, n):
    str1 = ''
    for a in range(len(str)):
        if a != n:
            str1 = str1 + str[a]
    return str1