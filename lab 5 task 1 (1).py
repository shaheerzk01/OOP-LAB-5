# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def sumDigits(a):
    summ = 0
    while a>0:
        digit = a%10
        summ +=digit
        a = a//10
    return summ
def main():
    x = 123
    print("Sum of digits is",sumDigits(x))
main()
        