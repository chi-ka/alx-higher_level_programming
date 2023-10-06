#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0:
        return (mylist)
    elif idx > (len(my_list) - 1):
        return (mylist)
    else:
        new_list = my_list.copy()
        new_list[idx] = element
        return (new_list)
