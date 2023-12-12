#!/usr/bin/python3
"""Base class for subsequent geometric classes"""
import json


class Base:
    """Base class for all geometric ssubclasses
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Object initializer

        Args:
            id (int, optional): id number. Defaults to None.
        """
        if id is not None:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """JSON string representation of list_dictionaries

        Args:
            list_dictionaries (list): list of dictionaries
        """
        if not list_dictionaries:
            return []
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes jason representation to file

        Args:
            list_objs (list):
        """
        name = cls.__name__ + ".json"
        with open(name, 'w') as file:
            if list_objs is None:
                file.write("[]")
            else:
                string = [obj.to_dictionary() for obj in list_objs]
                json_str = Base.to_json_string(string)
                file.write(json_str)
