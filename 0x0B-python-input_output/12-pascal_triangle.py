#!/usr/bin/python3
"""Pascal_s triangle function"""


def pascal_triangle(n):
    """Pascals Tris of n size
    """
    if n <= 0:
        return []

    list_int = [[1]]
    while len(list_int) != n:
        treia = list_int[-1]
        in_temp = [1]
        for i in range(len(treia) - 1):
            in_temp.append(treia[i] + treia[i + 1])
        in_temp.append(1)
        list_int.append(in_temp)
    return list_int
