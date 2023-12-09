#!/usr/bin/python3
"""Base class """


class BaseGeometry:
    """This class has two instance method (public)
    that raises exception
    """
    def area(self):
        """raises an exception
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validated integer input

        Args:
            name (str): name of value
            value (int): value
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
