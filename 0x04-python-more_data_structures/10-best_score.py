#!/usr/bin/python3
def best_score(a_dictionary):
    max = 0
    if a_dictionary is None:
        return (None)
    for key in a_dictionary.keys():
        num = a_dictionary[key]
        if num > max:
            max = num
    for key in a_dictionary.keys():
        if max == a_dictionary[key]:
            return (key)
