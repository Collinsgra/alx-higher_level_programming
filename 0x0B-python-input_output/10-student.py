#!/usr/bin/python3
"""class of Student"""


class Student:
    """student."""

    def __init__(self, first_name, last_name, age):
        """Initializes new student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """that retrieves a dictionary representation of a Student instance (same as 8-class_to_json.py):
If attrs is a list of strings, only attribute names contained in this list must be retrieved.
Otherwise, all attributes must be retrieved
        """
        if (type(attrs) == list and
                all(type(_lements) == str for _lements in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
