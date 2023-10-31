#!/usr/bin/python3
def uppercase(str):
    for a in str:
        if ord(a) in range(65, 91):
            print(f"{chr(ord(a) + 32)}", end='')
        else:
            print(f"{a}", end='')
    print(f"\n")
