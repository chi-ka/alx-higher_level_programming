#!/usr/bin/python3
n = 0
for i in range(ord('z'), ord('a') - 1, -1):
    if n % 2 == 0:
        print("{:c}".format(i), end='') 
    else:
        print("{:c}".format(i-32), end='')  
    n += 1
