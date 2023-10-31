#!/usr/bin/python3

i = 122
for r in range(0, 26):
    if i % 2 == 0:
        print("{}".format(chr(i)), end='')
    if i % 2 != 0:
        print("{}".format(chr(i-32)), end='')
    i -= 1
