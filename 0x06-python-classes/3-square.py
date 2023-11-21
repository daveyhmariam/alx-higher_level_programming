#!/usr/bin/python3
"""class square"""


class Square():
    """ Square instance with input verification"""
    def __init__(self, size=0):
        if size < 0:
            raise ValueError("size must be >= 0")
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        self.__size = size

    def area(self):
        """ returns area of square"""
        return self.__size ** 2
