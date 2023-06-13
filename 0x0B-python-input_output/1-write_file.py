#!/usr/bin/python3
"""defines a function of file writing."""


def write_file(filename="", text=""):
    """string to utf8
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
