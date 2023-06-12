#!/usr/bin/python3
"""checks the obj is the same class
or an acquired class
"""


def is_kind_of_class(obj, a_class):
    """returns true ,otherwise false
    """
    return isinstance(obj, a_class)
