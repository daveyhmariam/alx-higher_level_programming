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
        supper().__init__(size, size)


