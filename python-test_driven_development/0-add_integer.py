#!/usr/bin/python3


def add_integer(a, b = 98):

    '''integers addition'''
    if (type(a) != int and type(a) != float) or (type(b) != int and type(b) != float):
        raise TypeError("a must be an integer") or TypeError("b must be an integer")
    return int(a) + int(b)
