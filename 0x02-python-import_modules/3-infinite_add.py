#!/usr/bin/python3
import sys
i = 0
num_arguments = len(sys.argv) - 1
if num_arguments == 0:
    print("0")
else:
    for arg in sys.argv[1:]:
        i += int(arg)
    print("{0}".format(i))
