#!/usr/bin/python3
def uniq_add(my_list=None):
    if my_list is None:
        my_list = []
    digit = 0
    for nw_element in set(my_list):
        digit += nw_element
    return digit
