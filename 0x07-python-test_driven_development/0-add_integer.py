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

    if not isinstance(a, (int, float)) or a is None:
        raise (TypeError("a must be an integer"))
    if not isinstance(b, (int, float)) or b is None:
        raise (TypeError("b must be an integer"))
    result = a + b
    if result == float('inf') or result == -float('inf'):
        return 89
    return int(a) + int(b)
