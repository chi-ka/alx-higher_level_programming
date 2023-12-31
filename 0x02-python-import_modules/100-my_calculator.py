#!/usr/bin/python3
import sys
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    num_arguments = len(sys.argv) - 1
    if num_arguments != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    if (sys.argv[2] == '+'):
        print("{0} + {1} = {2}".format(a, b, add(a, b)))
    elif (sys.argv[2] == '-'):
        print("{0} - {1} = {2}".format(a, b, sub(a, b)))
    elif(sys.argv[2] == '*'):
        print("{0} * {1} = {2}".format(a, b, mul(a, b)))
    elif (sys.argv[2] == '/'):
        print("{0} / {1} = {2}".format(a, b, div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
