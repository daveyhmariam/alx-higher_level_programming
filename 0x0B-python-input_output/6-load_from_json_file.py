#!/usr/bin/python3
"""read json from a file"""
import json


def load_from_json_file(filename):
    """read a json string from a file into an object"""
    with open(filename, "r") as file:
        return (json.load(file))
