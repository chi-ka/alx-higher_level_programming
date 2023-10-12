#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    new = []
    for num in set_1:
        if num in set_2 or num in new:
            continue
        else:
            new.append(num)
            
    for num in set_2:
        if num in set_1 or num in new:
            continue
        else:
            new.append(num)
    return (new)
