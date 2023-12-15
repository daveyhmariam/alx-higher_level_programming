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
        """Return the JSON serialization of a list of dicts.

        Args:
            list_dictionaries (list): A list of dictionaries.
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    def from_json_string(json_string):
        """ Returns a list represented by json string

        Args:
            json_string (string): json string representation of objects
        """
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes jason representation to file

        Args:
            list_objs (list):
        """
        name = cls.__name__ + ".json"
        with open(name, 'w') as file:
            if list_objs is None or list_objs == []:
                file.write("[]")
            else:
                string = [obj.to_dictionary() for obj in list_objs]
                json_str = Base.to_json_string(string)
                file.write(json_str)

    def create(cls, **dictionary):
        """returns an instance with all attributes already set
        Args:
            **dictionary (dict): Key/value pairs of attributes to initialize.
        """
        if dictionary is not None or dictionary != {}:
            if cls.__name__ == "Rectangle":
                this = cls(1, 1)
            else:
                this = cls(1)
            this.update(**dictionary)
            return this
