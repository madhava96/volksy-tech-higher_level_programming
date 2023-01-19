#!/usr/bin/python3
"""number_of_lines"""


def number_of_lines(filename=""):
    """number_of_lines"""
    with open(filename, "r", encoding="UTF-8") as f:
        return len(list(f))
