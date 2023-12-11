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
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """getter/setter for height
        """
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """getter/setter for x
        """
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """getter/setter for y
        """
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Returns area of rectangle
        """
        return self.width * self.height

    def display(self):
        """Visual representation of the rectangle in stdout
        """
        for i in range(self.__y):
            print()
        for i in range(self.__height):
            for j in range(self.__x):
                print(" ", end="")
            for j in range(self.__width):
                print("#", end="")
            print()

    def update(self, *args, **kwargs):
        """Updates the attribute values with given array of attributes
        Args:
            args (list, tuple): argument field
        """
        fields = ['id',
                  'width',
                  'height',
                  'x',
                  'y']
        if args:
            for i in range(len(args)):
                setattr(self, fields[i], args[i])
        else:
            for a, v in kwargs.items():
                setattr(self, a, v)

    def __str__(self):
        """string representation of instance object
        """
        return ("[Rectangle] ({}) {}/{} - {}/{}"
                "".format(self.id, self.__x,
                          self.__y, self.__width,
                          self.__height))
