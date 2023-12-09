#!/usr/bin/python3
"""
a method to determine the class of an object
"""


def is_same_class(obj, a_class):
    """checkes if an object is instance of a class

    Args:
        obj (instance variable): reference to a object
        a_class (class): class name
    Returns: True if type maches False otherwise
    """
    if type(obj) == a_class:
        return True
    return False
