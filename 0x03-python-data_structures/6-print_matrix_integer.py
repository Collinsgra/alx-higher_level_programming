#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for house in matrix:
        for studs in house:
            if studs == house[-1]:
                print("{:d}".format(studs), end="")
            else:
                print("{:d}".format(studs), end=" ")
        print()
