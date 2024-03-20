#!/usr/bin/python3
"""pascal triangle
"""


def pascal_triangle(n):
    """ Pascal tringle using binomial theorem

    Args:
        n (int): level of pascal triangle
    Return: list of lists
    """
    if (n <= 0):
        return []
    pascal = []
    for i in range(n):
        pascal.append([int(fact(i) / fact(i - l) /
                           fact(l)) for l in range(i + 1)])
    return pascal


def fact(i):
    if (i <= 0):
        return (1)
    return (i * fact(i - 1))
