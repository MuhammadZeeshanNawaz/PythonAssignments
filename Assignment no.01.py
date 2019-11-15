#!/usr/bin/env python
# coding: utf-8

# Question no 01


print ("Twinkle, twinkle, little star, \n\tHow I wonder what you are! \n\t\tUp above the world so high, \n\t\tLike a diamond in the sky. \nTwinkle, twinkle, little star \n\tHow I wonder what you are ")


# Question no 02


print ("My Python Version is:")
import sys
print (sys.version)


# Question no 03


import time
print ("Current date and time :")
print(time.ctime())


# Question no 04


from math import pi

print ("Enter the radius of a circle")
radius = int(input())
area = pi * (radius*radius)
print ("Your Area is ",round(area,2))


# Question no 05


print ("Enter Your Name")
fname = str(input())
lname = str(input())

print("Reversed name: ", lname, fname )


# Question no 06


print ("Enter Your First Number")
a = int(input())
print ("Enter Your Second Number")
b = int(input())
result = a + b
print ("Addition of your numbers is",result)

