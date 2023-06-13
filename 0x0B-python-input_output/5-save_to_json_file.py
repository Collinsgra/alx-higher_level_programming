#!/usr/bin/python3
"""Defines a function of JSON file-writing """
import json


def save_to_json_file(my_obj, filename):
    """Writes to a text file using JSON"""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
