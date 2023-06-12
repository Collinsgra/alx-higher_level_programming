#!/usr/bin/python3
"""Def a base geo class"""


class BaseGeometry:
    """reps a base geometry"""

    def area(self):
        """yet to be implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validating values
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
