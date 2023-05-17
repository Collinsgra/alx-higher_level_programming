#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    rem_keyss = []
    for key in a_dictionary:
        if a_dictionary[key] == value:
            rem_keyss.append(key)
    for key in rem_keyss:
        del a_dictionary[key]
    return a_dictionary
