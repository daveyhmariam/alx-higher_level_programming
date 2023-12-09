#!/usr/bin/python3
""" Empty base class """


class BaseGeometry:
    """This class has one instance method (public)
    that raises exception
    """
    def area(self):
        """raises an exception
        """
        raise Exception("area() is not implemented")
