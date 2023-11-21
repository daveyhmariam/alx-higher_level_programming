#!/usr/bin/python3
"""class square"""


class Square():
    """ Square instance with input verification"""
    def __init__(self, size=0):
        """Initialize a new Square.

        Args:
            size (int): The size of the new square.
        """
        if size < 0:
            raise ValueError("size must be >= 0")
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        self.__size = size
