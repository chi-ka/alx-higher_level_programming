#!/usr/bin/python3
for x in range(100):
    if x < 10:
        print("0{:d}".format(x), end=', ')
    elif x == 99:
        print("{:d}".format(x))
    else:
        print("{:d}".format(x), end=', ')
