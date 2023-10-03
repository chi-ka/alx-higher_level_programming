#!/usr/bin/python3
def uppercase(s):
    result = ""
    for char in s:
        if 'a' <= char <= 'z':
            uppercase_ascii = ord(char) - 32
            result += chr(uppercase_ascii)
        else:
            result += char

    print(result)
