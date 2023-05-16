#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    upd_list = []

    for i in my_list:
        if i % 2 == 0:
            upd_list.append(True)
        else:
            upd_list.append(False)
    return (upd_list)
