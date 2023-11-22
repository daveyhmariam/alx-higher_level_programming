#!/usr/bin/python3
"""class square"""


class Square():

    """ Square instance with input verification"""
    def __init__(self, size=0):
        """ initialiing method

            Arg:
                size(int): size of square
        """

        self.__size = size

    @property
    def size(self):

        """getter method"""
        return __size

    @size.setter
    def size(self, value):
        """setter method"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ returns area of square"""
        return self.__size ** 2
    def my_print(self):

        """Print # in square area"""

        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
            print("")
        if self.__size == 0:
            print("")