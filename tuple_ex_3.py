# -*- coding: utf-8 -*-
"""
Created on Fri Feb 18 09:35:55 2022

@author: Dr. Rakesh Moulick
"""
# Accessing Tuple
Tuple1 = tuple('University')
print("Printing the first element of Tuple:")
print(Tuple1[0])

# Tuple Unpacking
Tuple1 = ("Yes","No","Maybe")
a, b, c = Tuple1
print("\n Printing tuple after unpacking:")
print(a)
print(b)
print(c)

# Concatenation of tuple
Tuple1 = (0,2,4)
Tuple2 = ('Yes','No','Maybe')
Tuple3 = Tuple1 + Tuple2

print("\n Printing first tuple:")
print(Tuple1)
print("\n Printing second tuple:")
print(Tuple2)
print("\n Printing concatenated tuple:")
print(Tuple3)

# Slicing tuple
Tuple1 = tuple("university")
print("\n Printing tuple removing first element:")
print(Tuple1[1:])

# Reversing tuple
print("\n Printing reversed tuple:")
print(Tuple1[::-1])

# Deleting a tuple
Tuple1 = (1,2,3,4,5)
del Tuple1
print("\n Printing deleted tuple:")
print(Tuple1)


