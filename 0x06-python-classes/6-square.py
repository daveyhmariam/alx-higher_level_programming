#!/usr/bin/python3
"""class square"""


class Square:

    """ Square instance with input verification"""
    def __init__(self, size=0, position=(0, 0)):
        """ initialiing method

            Arg:
                size(int): size of square
                position (int, int): position of square
        """

        self.size = size
        self.position = position

    @property
    def size(self):

        """getter method"""
        return self.__size

    @size.setter
    def size(self, value):
        """setter method"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):

        """getter method"""
        return self.__position

    @position.setter
    def position(self, value):
        """position setter"""

        if (not isinstance(value, tuple) or
                not all(isinstance(i, int) for i in value) or
                len(value) != 2 or
                not all(i >= 0 for i in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """ returns area of square"""
        return self.__size ** 2

    def my_print(self):

        """Print # in square area"""

        if self.__size == 0:
            print("")
            return
        [print("") for i in range(0, self.__position[1])]
        for i in range(self.__size):
            for k in range(self.__position[0]):
                print(" ", end="")
            for j in range(self.__size):
                print("#", end="")
            print("")
