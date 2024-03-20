#!/usr/bin/python3
""" insert line in a file """


def append_after(filename="", search_string="", new_string=""):
    """ Insert certain line in a file

    Args:
        filename (str, optional): file to open. Defaults to "".
        search_string (str, optional): string to search. Defaults to "".
        new_string (str, optional): string to insert. Defaults to "".
    """
    if (filename and search_string and new_string):
        with open(filename, "r") as f:
            text = ""
            for line in f:
                text += line
                if search_string in line:
                    text += new_string
        with open(filename, "w") as f:
            f.write(text)
