#!/usr/bin/python3
"""Defines a function to JSON file reading """
import json


def load_from_json_file(filename):
    """writes a Python object from a provided JSON-file"""
    with open(filename) as f:
        return json.load(f)
