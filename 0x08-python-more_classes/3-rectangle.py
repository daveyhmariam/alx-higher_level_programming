#!/usr/bin/python3
"""Define A class"""


class Rectangle:
    """Rectangle class that does nothing"""
    def __init__(self, width=0, height=0):
        """
        Creates Rectangle Object

        Args:
            width (int): width of rectangle
            height (int): height of rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """property setter/getter"""
        return self.__width

    @width.setter
    def width(self, val):
        if not isinstance(val, int):
            raise TypeError("width must be an integer")
        if val < 0:
            raise ValueError("width must be >= 0")
        self.__width = val

    @property
    def height(self):
        """property setter/getter"""
        return self.__height

    @height.setter
    def height(self, val):
        if not isinstance(val, int):
            raise TypeError("height must be an integer")
        if val < 0:
            raise ValueError("height must be >= 0")
        self.__height = val

    
    def area(self):
        """Returns area of rectangle"""
        return self.__height * self.__width
    
    def perimeter(self):
        """returns perimeter of rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (2 * (self.__width + self.__height))

    def __str__(self):
        """
        String representarion of the rectangle with #
        """

        if self.__height == 0 or self.__width == 0:
            return ""
        else:
            str_ = []
            for r in range(self.__height):
                for c in range(self.__width):
                    str_.append("#")
                str_.append("\n")
            return "".join(str_)
