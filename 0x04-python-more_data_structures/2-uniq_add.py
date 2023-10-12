#!/usr/bin/python3
def uniq_add(my_list=[]):
    new = []
    sum = 0
    for num in my_list:
        if num in new:
            continue
        else:
            sum += num
            new.append(num)
    return (sum)
