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
    i = 0
    for i in range(n):
        new = []
        for ln in range(0, i + 1):
            new.append(int(fact(i) / fact(i - ln) / fact(ln)))
        pascal.append(new)
    return pascal


def fact(i):
    if (i <= 0):
        return (1)
    return (i * fact(i - 1))
