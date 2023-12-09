#!/usr/bin/python3
"""
a method to determine if an object is class or subclassed
"""


def is_kind_of_class(obj, a_class):
    """determines if an object is classed or subclassed
    Args:
        obj (instance variable): reference to a object
        a_class (class): class name
    Returns: True if type maches False otherwise
    """
    if isinstance(obj, a_class):
        return True
    return False
