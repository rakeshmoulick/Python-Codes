# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 11:28:31 2022

@author: Dr. Rakesh Moulick
"""

# Accessing elements from a Dictionary

Dict1 = {1:'Yes', 2:'No', 3:'Maybe'}

print(Dict1)

print("Accessing an element using key:")
print(Dict1[1])
print(Dict1[2])
print(Dict1[3])

Dict2 = {1:'Yes', 'no':'No', 3:'Maybe'}
print(Dict2)

print("Accessing an element using key:")
print(Dict2[1])
print(Dict2['no'])
print(Dict2[3])


