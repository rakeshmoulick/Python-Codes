# -*- coding: utf-8 -*-
"""
Created on Fri Feb 18 09:54:20 2022

@author: Dr. Rakesh Moulick
"""
# Exercise on built-in methods and functions
Tuple1 = tuple("university")

# Built in Methods
print("Printing the frequency of occurences:")
print(Tuple1.count('i'))

print("Printing the index of a specific value:")
print(Tuple1.index('i'))

# Built-in functions

# Length of a tuple
print("Printing the length of the tuple:")
print(len(Tuple1))

# Sorting a tuple: Type changes from tuple to list
Tuple1 = (0,5,6,4,2,3,8,9,1,7)
print("Printing sorted tuple:")
print(sorted(Tuple1))

# Sum of the elements
print("Printing the sum of tuple:")
print(sum(Tuple1))

# Minimum value of the tuple
print("Printing the minimum and maximum of tuple:")
print(min(Tuple1), max(Tuple1))


