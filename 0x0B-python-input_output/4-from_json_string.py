#!/usr/bin/python3
"""From json to object"""
import json


def from_json_string(my_str):
    """deserialize string to object"""
    return (json.loads(my_str))
