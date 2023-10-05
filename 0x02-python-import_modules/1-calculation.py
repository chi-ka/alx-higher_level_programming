#!/usr/bin/python3
a = 10
b = 5
from calculator_1 import add, sub, div, mul
print("{} + {} = {}".format(a, b, add(a,b)))
print("{} - {} = {}".format(a, b, sub(a,b)))
print("{} * {} = {}".format(a, b, mul(a,b)))
print("{} / {} = {}".format(a, b, div(a,b)))
