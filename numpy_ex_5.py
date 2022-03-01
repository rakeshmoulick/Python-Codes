# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 15:15:18 2022

@author: Dr. Rakesh Moulick
"""

import numpy as np
a = np.array([[1,2,3], [4,5,6], [7,8,9]])
b = np.array([1,4,3])

print("\nPrinting a:")
print(a)

print("\nPrinting b:")
print(b)

print("\nPrinting diagonal of a:")
print(np.diagonal(a)) # Principal diagonal

print("\nPrinting sub-diagonal of a:")
print(np.diagonal(a,1)) # first sub diagonal
print(np.diagonal(a,-1))

print("\nPrinting trace of a:")
print(np.trace(a)) # Sum of diagonal elements

print("\nPrinting identity matrix:")
print(np.identity(3)) # Identity Matrix


