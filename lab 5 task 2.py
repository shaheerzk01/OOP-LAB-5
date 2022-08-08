# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 14:12:24 2021

@author: 21a-003-se
"""

def displaySortedNumbers(num1,num2,num3):
    if num1<num2<num3:
        print(num1,num2,num3)
    elif num1>num2>num3:
        print(num3,num2,num1)
    elif num2>num1>num3:
        print(num3,num1,num2)
    elif num2>num3>num1:
        print(num1,num3,num2)
def main():
    num1 = int(input("enter a number : "))
    num2 = int(input("enter a number : "))
    num3 = int(input("enter a number : "))
    displaySortedNumbers(num1,num2,num3)
main()

