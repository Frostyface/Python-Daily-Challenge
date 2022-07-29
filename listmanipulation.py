#!/bin/python3

'''
Take two lists, say for example these two:

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
and write a program that returns a list that contains
only the elements that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes.

Extras:

Randomly generate two lists to test this
Write this in one line of Python (dont worry if you cant figure this out at this point
- well get to it soon)
'''

import random

randomlist1 = []
for i in range(0,5):
    n = random.randint(1,30)
    randomlist1.append(n)

randomlist2 = []
for i in range(0,5):
    n = random.randint(1,30)
    randomlist2.append(n)

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = []

for elm in randomlist1:
    if elm in randomlist2:
        c.append(elm)

print(c) 



