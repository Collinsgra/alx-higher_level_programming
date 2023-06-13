#!/usr/bin/python3
"""Class Student"""


class Student:
    """reps a_student."""

    def __init__(self, first_name, last_name, age):
        """initialize student_new
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Gets representation of a Student"""
        return self.__dict__
