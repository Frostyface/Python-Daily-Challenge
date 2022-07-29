#!/bin/python3

"""
The exercise comes first (with a few extras if you want the extra challenge
or want to spend more time), followed by a discussion. Enjoy!

Ask the user for a number. Depending on whether the number is even or odd, print 
out an appropriate message to the user. Hint: how does an even / odd number react differently when divided by 2?

Extras:

If the number is a multiple of 4, print out a different message.
Ask the user for two numbers: one number to check (call it num) and one number 
to divide by (check). If check divides evenly into num, tell that to the user. If not, print a different appropriate message.
"""

number = int(input("Enter a number: "))
check = int(input("Enter a number to divide into the first number: "))

if number%check == 0:
    print("It evenly divides")
else:   
    print("It does not evenly divide")

'''
if number%4 == 0:
    print("Number is divisble by 4")
elif number%2 == 0:
    print("Number is even")
else:
    print("Number is odd")
'''