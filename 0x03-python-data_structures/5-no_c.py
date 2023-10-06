#!/usr/bin/python3
def no_c(my_string):
    new = ''
    for a in my_string:
        if a not in 'Cc':
            new += a
    return (new)
