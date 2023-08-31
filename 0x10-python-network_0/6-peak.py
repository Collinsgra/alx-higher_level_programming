#!/usr/bin/python3
"""Contains function inside a list"""


def find_peak(list_of_integers):
    """Find peak inside a list of integers"""
    if not list_of_integers:
        return None
    return max(list_of_integers)


# Test the function
input_list = [1, 3, 20, 4, 1, 0]
peak = find_peak(input_list)
print("Peak:", peak)
