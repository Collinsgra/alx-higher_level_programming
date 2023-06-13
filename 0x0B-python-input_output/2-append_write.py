#!/usr/bin/python3
"""Defines a function of file-appending ."""


def append_write(filename="", text=""):
    """appends a str to the end of a file
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
