#!/usr/bin/python3
"""function of string-to-JSON"""
import json


def to_json_string(my_obj):
    """Returns the JSON of string"""
    return json.dumps(my_obj)
