#!/usr/bin/python3
"""
a method to determine if a obj is only subclass of class
"""


def inherits_from(obj, a_class):
    """The function `inherits_from` checks if an object
    inherits from a specific class.

    Args:
        obj (instance variable): reference to a object
        a_class (class): class name
    Returns: True if type maches False otherwise
    """
    if (issubclass(obj.__class__, a_class)
            and obj.__class__ not in a_class.__mro__):
        return True
    return False
