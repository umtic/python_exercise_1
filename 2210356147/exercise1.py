#!/usr/bin/env python
# coding: utf-8

# 1. Print a message which states whether a year which is taken as input is a leap year or not to the screen.

# In[ ]:


year = input("Enter Year: ")
if int(year)%4 == 0:
    if int(year)%100 != 0:
        if int(year)%400 != 0:
            print('Entered year is a leap year.')
if int(year)%4 == 0:
       if int(year)%100 == 0:
            if int(year)%400 != 0:
                print('Entered year is not a leap year.')
if int(year)%4 == 0:
       if int(year)%100 == 0:
            if int(year)%400 == 0:
                print('Entered year is a leap year.')
else:
    print('Entered year is not a leap year.')

