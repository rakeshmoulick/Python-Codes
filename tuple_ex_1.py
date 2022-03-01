# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 10:44:30 2022

@author: Dr. Rakesh Moulick
"""
rec = ('Smith','John',(6,23,68))
A, B, C = rec

print('A = ', A)
print('B = ', B)
print('C = ', C)

D = C[2]
print('D = ', D)

name = rec[1] + ' ' + rec[0]
print('name = ', name)

print(rec[0:2])
