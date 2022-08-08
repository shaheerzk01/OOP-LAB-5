# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 15:50:11 2021

@author: 21a-003-se
"""

def numberOfDaysInAYear(year):
    for i in range(2010,year+1):
        if i%4==0 and i%100!=0 or i%400==0:
            print(f"{i}     Days:366")
        else:
            print(f"{i}     Days:365")
def main():
    numberOfDaysInAYear(2020)
main()