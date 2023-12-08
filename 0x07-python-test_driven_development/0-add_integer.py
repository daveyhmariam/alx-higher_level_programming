#!/usr/bin/python3
"""a function that adds two numbers"""


def add_integer(a, b=98):
    """Adds two integers
    Args:
        a (int, float): integer argument
        b (int, float): integer argument
    Raises:
        TypeError: If either of a or b is a non-integer and non-float.

    Returns: sum
    """
    if (not isinstance(a, int) and
            not isinstance(a, float)):
        raise (TypeError("a must be an integer"))
    if (not isinstance(b, int) and
            not isinstance(b, float)):
        raise (TypeError("b must be an integer"))
    return int(a) + int(b)
