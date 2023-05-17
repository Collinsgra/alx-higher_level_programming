#!/usr/bin/python3
def weight_average(my_list=None):
    if my_list is None:
        my_list = []
    if my_list and len(my_list):
        numbber = 0
        num_denominator = 0
        for tup in my_list:
            numbber += (tup[0] * tup[1])
            num_denominator += (tup[1])
        return numbber/num_denominator
    return 0
