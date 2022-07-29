#!/bin/python

""""
Create a program that asks the user to enter their name and their age.
Print out a message addressed to them that tells them the year that they
will turn 100 years old. Note: for this exercise, the expectation is that you explicitly 
write out the year (and therefore be out of date the next year). 
If you want to do this in a generic way, see exercise 39.
"""

name = input("What is your name? ")
age = input("What is your age? ")
number = int(input("How many times would you like the results? "))

hundred = 100 - int(age)

response = ("Your name is: " + name + " and you will be 100 in " + str(hundred) + " years! \n")

print(response* 10)
