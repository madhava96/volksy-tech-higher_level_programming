#!/usr/bin/python3
"""string size"""


class Square:
    '''size'''
    def __init__(square, size):

        if type(size) != int:
            raise TypeError("value is not integer")
        if size < 0 :
            raise ValueError("size must be >= 0")

        square.__size = size
