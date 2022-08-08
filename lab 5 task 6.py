# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 15:00:10 2021

@author: 21a-003-se
"""

def convertMilli(millis):
    c = millis*(2.778)*(10**-7)
    d = c-int(c)
    z = d*60
    f = int(c)*60*60
    e = int(z)*60
    l = e + f
    a = (millis*0.001)
    q = int(a)-l
    print("number of hours in milliseconds are",int(c))
    print("number of mintes in milliseconds are",int(z))
    print("number of seconds in milliseconds are",int(q))
def main():
    millis=int(input("Enter millisecods : "))
    convertMilli(millis)
main()