#!/usr/bin/python3
"""Square class that represents a square"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class inherits from Rectangle class

    Args:
        Rectangle (class): rectangle class
    """
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """calculates area of square"""
        return self.__size ** 2

    def __str__(self):
        """Readable string of object representation
        """
        return ("[{}] {}/{}"
                .format(self.__class__.__name__, self.__size, self.size))
