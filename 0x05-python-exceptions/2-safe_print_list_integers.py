#!/usr/bin/python3


def safe_print_list_integers(my_list=[], x=0):
    """Print list elements

    Args:
        my_list: list to print.

    Returns:
        number of printed elements
    """
    printed = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            printed += 1
        except (ValueError, TypeError) as e:
            continue

    print("")
    return printed
