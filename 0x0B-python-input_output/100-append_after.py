#!/usr/bin/python3
"""This Defines a text file function"""


def append_after(filename="", search_string="", new_string=""):
    """enters text after each line in a file
    """
    text = ""
    with open(filename) as a:
        for line in a:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as w:
        w.write(text)
