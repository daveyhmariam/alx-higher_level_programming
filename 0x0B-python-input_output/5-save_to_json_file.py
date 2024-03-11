#!/usr/bin/python3
"""write json to a file"""
import json


def save_to_json_file(my_obj, filename):
    """write json str to a file"""
    with open(filename, "w") as file:
        json.dump(my_obj, file)
