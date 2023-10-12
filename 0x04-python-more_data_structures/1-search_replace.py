#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new = []
    for letter in my_list:
        if letter == search:
            new.append(replace)
        else:
            new.append(letter)
    return (new)
