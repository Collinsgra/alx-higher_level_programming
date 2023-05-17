#!/usr/bin/python3

def multiply_list_map(my_list=None, num=0):
    if my_list is None:
        my_list = []
    return list(map(lambda x: x * num, my_list))
