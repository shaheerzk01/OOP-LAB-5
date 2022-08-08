# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 14:33:01 2021

@author: 21a-003-se
"""

def ispalindrome(number):
    return number==number[::-1]
    print(number)
number = (input("Enter an integer : "))
a = ispalindrome(number)
if a:
    print("yes")
else:
    print("no")