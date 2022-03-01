# -*- coding: utf-8 -*-
"""
Created on Fri Feb 18 09:21:21 2022

@author: Dr. Rakesh Moulick
"""
# Creating empty tuple
Tuple1 = ()
print("Printing the initial tuple:")
print(Tuple1)

# Tuple of Strings
Tuple1 = ('University','College')
print("\nPrinting tuple of strings:")
print(Tuple1)

# Creating Tuple with lists
list1 = [1, 2, 3, 4]
print("\nPrinting Tuple using list:")
print(tuple(list1))

# Creating tuple with built-in function
Tuple1 = tuple('University')
print("\nPrinting Tuple with built-in function:")
print(Tuple1)

# Creating nested tuple
Tuple1 = ('Yes','No')
Tuple2 = (2,3,4,5)
Tuple3 = (Tuple1,Tuple2)
print('\nPrinting nested tuple:')
print(Tuple3)

# Creating tuple with repetition
Tuple1 = ('Yes',)*3
print('\nPrinting tuple with repetition:')
print(Tuple1)


