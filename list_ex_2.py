# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 11:04:32 2022

@author: Dr. Rakesh Moulick
"""

a = [1.0, 2.0, 3.0]
print('a = ', a)

b = a
b[0] = 5.0 # change the first element of b

print('a = ', a)

c = a[:]
c[0] = 3.0

print('a = ', a)



