#!/usr/bin/python3
"""A function that dynamically adds attribute"""


def add_attribute(obj, att, value):
    """Add a new attribute to an object if possible.

    Args:
        obj (instance):
        att (instance variable):
        value (value of attribute):
    Raises:
        TypeError: If the attribute cannot be added.
    """
    if (hasattr(obj, '__dict__') or
            (hasattr(type(obj), '__slots__') and att in type(obj).__slots__)
        ):
        setattr(obj, att, value)
    else:
        raise TypeError("can't add new attribute")
