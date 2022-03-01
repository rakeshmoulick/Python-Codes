# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 11:58:04 2022

@author: Dr. Rakesh Moulick
"""
import numpy as np
print("\nPrinting the array:")
print(np.arange(1,10,1))

print("\nPrinting the array:")
print(np.arange(1.0,10.0,2.0))

# Accessing and changing array elements
a = np.zeros((3,3))
print("\nPrinting a:")
print(a)

a[0] = [2,3,2]
a[1,1] = 8
a[2,0:2] = [8,-3]
print("\nPrinting a:")
print(a)

a[2,0:] = [8,-3,2]
print("\nPrinting a:")
print(a)


