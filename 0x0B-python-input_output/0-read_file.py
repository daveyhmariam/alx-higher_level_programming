#!/usr/bin/python3
"""a function that reads a text file (UTF8) and prints it to stdout"""

def read_file(filename=""):
    """reads a text file (UTF8) and prints it to stdout

    Args:
        filename (str, optional): file to read from.defaults to"".
    """
    if filename:
        with open(filename, encoding="utf-8") as f:
            print(f.read(), end="")
