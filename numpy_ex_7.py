# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 17:00:22 2022

@author: Dr. Rakesh Moulick
"""

import numpy as np
A = np.array([[4, -2, 1],
              [-2, 4, -2],
              [1, -2, 3]])

b = np.array([1, 4, 2])

print("\nPrinting inverse of A:")
print(np.linalg.inv(A)) 
print("\nPrinting solution:")
print(np.linalg.solve(A,b))

    
