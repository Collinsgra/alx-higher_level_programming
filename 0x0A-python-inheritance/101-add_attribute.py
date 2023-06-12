#!/usr/bin/python3
"""this function that adds attrbs to objs"""


def add_attribute(obj, att, value):
    """if possible add atribs
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
