#!/usr/bin/python3
"""Square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """This class inherits from the rectangle class

    Args:
        Rectangle (class): rectangle class that is subclass of the base class
    """
    def __init__(self, size, x=0, y=0, id=None):
        """Initializer of instance object

        Args:
            size (int): length of square
            x (int, optional): x coordinate. Defaults to 0.
            y (int, optional): y coordinate. Defaults to 0.
            id (_type_, optional): object id. Defaults to None.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """getter/setter for size attribute"""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Updates the attribute values with given array of attributes
        Args:
            args (list, tuple): argument field
        """
        fields = ['id',
                  'size',
                  'x',
                  'y']
        if args:
            for i in range(len(args)):
                setattr(self, fields[i], args[i])
        else:
            for a, v in kwargs.items():
                setattr(self, a, v)

    def to_dictionary(self):
        """Dictionary representation of rectangle object"""
        return {"id": self.id,
                "size": self.width,
                "x": self.x,
                "y": self.y}

    def __str__(self):
        """string representation of instance object
        """
        return ("[Square] ({}) {}/{} - {}"
                "".format(self.id, self.x,
                          self.y, self.width))
