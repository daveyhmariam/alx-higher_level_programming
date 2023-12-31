#!/usr/bin/python3


def multiply_by_2(a_dictionary):
    """
    Multiplies a dictionary values by 2

    Args:
        a_ditionary: input dictioary
    Return: the new dictionary
    """
    keys = list(a_dictionary.keys())
    values = list(map(lambda x: x * 2, list(a_dictionary.values())))
    new_dictionary = {}
    for k, v in zip(keys, values):
        new_dictionary[k] = v
    return (new_dictionary)
