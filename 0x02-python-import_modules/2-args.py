#!/usr/bin/python3
if __name__ == "__main__":
    """
    prints command line args

    """
    from sys import argv
    if len(argv) == 1:
        print("{len(argv) - 1} argumnt:".format(len(argv) - 1))
    else:
        print("{len(argv) - 1} arguments:".format(len(argv) -1))
    i = 1
    for str in argv:
        if str != argv[0]:
            print("{i}: {str}".format(i, str))
            i += 1
