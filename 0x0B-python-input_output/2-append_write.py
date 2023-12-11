#!/usr/bin/python3
"""a function that appends a text file (UTF8) and prints it to stdout"""


def append_write(filename="", text=""):
    """appends a text file (UTF8) and prints it to stdout

    Args:
        filename (str, optional): file to write to.defaults to "".
        text (str, optional): txt to write.defaults to "".
    """
    if filename:
        with open(filename, 'a', encoding="utf-8") as f:
            return f.write(text)
