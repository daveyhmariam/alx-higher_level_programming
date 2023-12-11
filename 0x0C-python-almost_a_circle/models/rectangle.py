#!/usr/bin/python3
"""Rectagle class"""
from models.base import Base


class Rectangle(Base):
    """This Rectangle class inherits from the base class

    Args:
        Base (class): superclass
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """This magic method initializes the object with certain parameters

        Args:
            width (_type_): _description_
            height (_type_): _description_
            x (int, optional): _description_. Defaults to 0.
            y (int, optional): _description_. Defaults to 0.
            id (_type_, optional): _description_. Defaults to None.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """getter/setter method for width
        """
        return self.__width

    @width.setter
    def width(self, value):
        if value < 0:
            raise ValueError("Width should be greater than 0")
        if not isinstance(value, (int, float)):
            raise TypeError("Width should be integer")
        else:
            self.__width = value

    @property
    def height(self):
        """getter/setter for height
        """
        return self.__height

    @height.setter
    def height(self, value):
        if value < 0:
            raise ValueError("Height should be greater than 0")
        if not isinstance(value, (int, float)):
            raise TypeError("Height should be integer")
        else:
            self.__height = value

    @property
    def x(self):
        """getter/setter for x
        """
        return self.__x

    @x.setter
    def x(self, value):
        if value < 0:
            raise ValueError("x should be greater than 0")
        if not isinstance(value, (int, float)):
            raise TypeError("x should be integer")
        else:
            self.__x = value

    @property
    def y(self):
        """getter/setter for y
        """
        return self.__y

    @y.setter
    def y(self, value):
        if value < 0:
            raise ValueError("y should be greater than 0")
        if not isinstance(value, (int, float)):
            raise TypeError("y should be integer")
        else:
            self.__y = value
