#!/usr/bin/python3
if __name__ == "__main__":
    """
    prints command line args

    """
    import sys
    if len(sys.argv) == 1:
        print("{} arguments:".format(len(sys.argv) - 1))
    elif len(sys.argv) == 2:
        print("{} argument:".format(len(sys.argv) - 1))
    else:
        print("{} arguments:".format(len(sys.argv) - 1))
    i = 1
    for str in sys.argv:
        if str != sys.argv[0]:
            print("{}: {}".format(i, str))
            i += 1
