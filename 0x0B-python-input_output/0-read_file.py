#!/usr/bin/python3
"""This function defines a text file"""


def read_file(filename=""):
    """Prints content in a UTF8 file"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
