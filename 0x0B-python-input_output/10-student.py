#!/usr/bin/python3
"""Student class"""


class Student:
    """A Student class"""
    def __init__(self, first_name, last_name, age):
        """initialize Student object

        Args:
            first_name (str): first nae of student
            last_name (str): last nam of student
            age (int): age of student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """return dict representatio of object
        Args:
            attrs (list): (Optional) The attributes to represent.
        """
        if (type(attrs) == list and
            all(type(el) == str for el in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}

        return self.__dict__
