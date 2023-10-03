#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
new = abs(number) % 10
if number < 0:
    new = -new
if new == 0:
    print(f'Last digit of {number} is {new} and is 0')
elif new > 5:
    print(f'Last digit of {number} is {new} and is greater than 5')
elif new < 6 and new != 0:
    print(f'Last digit of {number} is {new} and is less than 6 and not 0')
