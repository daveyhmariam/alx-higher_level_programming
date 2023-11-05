#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    """
    Adds the 2 intries of two tuples

    Args:
        tuple_a: the first tuple

        tuple_b: the second tuple

    Return: tuple of two elements
    """
    list_a = list(tuple_a) + [0, 0]
    list_b = list(tuple_b) + [0, 0]
    sum = [(a + b + 0) for a, b in zip(list_a, list_b)]
    return (tuple(sum[0:2]))
