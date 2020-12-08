# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 10:35:09 2020

@author: Isabella.Glaze
"""

from datetime import datetime 

## this is a test file

print('Hello')

## okay but what if i change the code now ^ 

print('and now i have merged both the test branch and the another-one branch')

date = input('Please input start date (MM-DD-YYYY): ')
date = datetime.strptime(date, "%m-%d-%Y").date() 
