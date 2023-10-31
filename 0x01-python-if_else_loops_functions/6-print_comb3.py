#!/usr/bin/python3
for i in range(10):
    for k in range(i + 1, 10):
        print("{}{}{}".format(i, k, ", " if i != 8 else "\n"), end="")
