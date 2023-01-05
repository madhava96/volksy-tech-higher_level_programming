#!/usr/bin/python3
def no_c(my_string):
    # if c is not in c
    lst = []
    for x in my_string:
        if x != 'c' and x != 'C':
            lst.append(x)
    return "".join(lst)
