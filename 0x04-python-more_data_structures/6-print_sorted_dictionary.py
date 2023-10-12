#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    summ = []
    for key in a_dictionary.keys():
        summ.append(key)
        sorted_key = sorted(summ)
    for key in sorted_key:
        print(f"{key} : {a_dictionary[key]}")
