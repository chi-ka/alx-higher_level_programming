#!/usr/bin/python3
def uppercase(c):
    x = 1
    for i in c:
        if ord('a') <= ord(i) <= ord('z'):
            n = ord(i) - ord('a') 
            print(chr(ord('A') + n), end='')
        else:
            print(i,end='')
        if x == len(c):
            print('')
        else:
            x += 1
