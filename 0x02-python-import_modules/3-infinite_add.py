#!/usr/bin/python3
if __name__ == "__main__":
    """
    Adds command line args

    """
    from sys import argv
    sum = 0
    for i in argv:
        if i != argv[0]:
            sum = sum + int(i)
    print(f"{sum}")
