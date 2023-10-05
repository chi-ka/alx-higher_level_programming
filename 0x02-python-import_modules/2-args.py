#!/usr/bin/python3
import sys
if __name__ == "__main__":
    num_arguments = len(sys.argv) - 1
    if num_arguments == 0:
        print("{0} arguments.".format(num_arguments))
    else:
        print("{0} arguments:".format(num_arguments))
        for i, arg in enumerate(sys.argv[1:], start=1):
            print("{0}: {1}".format(i, arg))
