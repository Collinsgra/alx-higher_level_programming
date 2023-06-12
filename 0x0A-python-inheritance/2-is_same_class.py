#!/usr/bin/python3
"""
module function is_same_class
"""


def is_same_class(obj, a_class):
    """returns true if the object is exactly  an instance of the specified class ; else False"""
    return type(obj) == a_class
