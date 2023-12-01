#!/usr/bin/python3
from magic_calculation_102 import add, sub


def magic_calculation(i, j):
    if i < j:
        d = add(i, j)
        for a in range(4, 6):
            d = add(d, a)
        return (d)
    else:
        return sub(i, j)
