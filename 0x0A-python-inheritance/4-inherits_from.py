#!/usr/bin/python3
"""function that returns True if the object is an instance of a class that inherited
"""


def inherits_from(obj, a_class):
    """returns True else False
    """
    return issubclass(type(obj), a_class) and type(obj) != a_class
