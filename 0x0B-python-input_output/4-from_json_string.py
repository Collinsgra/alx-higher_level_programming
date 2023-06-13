#!/usr/bin/python3
"""Defines a function to JSON-to-object """


import json


def from_json_string(my_str):
    """returns Python object"""
    return json.loads(my_str)
