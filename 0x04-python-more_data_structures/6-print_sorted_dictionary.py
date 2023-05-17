#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for fl_keys in sorted(a_dictionary.keys()):
        print('{}: {}'. format(fl_keys, a_dictionary[fl_keys]))
