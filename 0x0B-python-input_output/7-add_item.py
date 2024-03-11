#!/usr/bin/python3
"""save list of arguments to a file"""
import sys


def add_item():
    """add arguments to a jason file"""
    save_to_json_file = \
        __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = \
        __import__('6-load_from_json_file').load_from_json_file
    try:
        arg = load_from_json_file("add_item.json")
    except FileNotFoundError:
        arg = []
    arg.extend(sys.argv[1:])
    save_to_json_file(arg, "add_item.json")


add_item()
