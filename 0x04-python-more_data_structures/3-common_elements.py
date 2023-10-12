#!/usr/bin/python3
def common_elements(set_1, set_2):
    new = []
    for num in set_1:
        if num in set_2 and num not in new:
            new.append(num)
        else:
            continue
    return (new)
