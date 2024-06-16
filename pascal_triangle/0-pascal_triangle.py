#!/usr/bin/python3
"""Pascal Triangle"""


def pascal_triangle(n):
    """Returns a list of lists of integers representing
    the Pascal's triangle of n"""
    if n <= 0:
        return []
    res = [[1]]

    for i in range(n-1):
        row = []
        temp = [0] + res[-1] + [0]
        for j in range(len(res[-1]) + 1):
            row.append(temp[j] + temp[j+1])
        res.append(row)
    return res
