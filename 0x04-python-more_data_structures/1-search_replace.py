#!/usr/bin/python3
def search_replace(my_list, search, replace):
    def check_search(new_element):
        return new_element if new_element != search else replace
    return list(map(check_search, my_list))
