# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 15:24:10 2022

@author: Dr. Rakesh Moulick
"""
# matrix operations

import numpy as np
x = np.array([8,3])
y = np.array([1,2])
A = np.array([[2,4],[1,2]])
B = np.array([[1,1],[2,2]])

# Dot Product

print("dot(x,y) =\n", np.dot(x,y))  # {x}.{y}
print("dot(A,x) =\n", np.dot(A,x))  # [A]{x}
print("dot(A,B) =\n", np.dot(A,B))  # [A][B]

# Inner product
print("inner(x,y) =\n",np.inner(x,y)) # {x}.{y}
print("inner(A,x) =\n",np.inner(A,x)) # [A]{x}
print("inner(A,B) =\n",np.inner(A,B)) # [A][B_transpose]



