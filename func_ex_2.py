# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 15:50:46 2022

@author: Dr. Rakesh Moulick
"""
# A mutable list is passed on to a 
# function where it is modified
def squares(a):
    for i in range(len(a)):
        a[i] = a[i]**2
    

a = [1, 2, 3, 4]
squares(a)
print(a)


