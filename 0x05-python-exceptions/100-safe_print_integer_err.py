#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except(ValueError, NameError):
        error_message = "Exception: " + str(sys.exc_info()[1])
        sys.stderr.write(error_message + '\n')
        return False
