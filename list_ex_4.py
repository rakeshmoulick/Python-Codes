# -*- coding: utf-8 -*-
"""
Created on Fri Feb 18 10:25:11 2022

@author: Dr. Rakesh Moulick
"""
# Exercise for buuilt-in methods 
# and functions in list objects

l = [1,2,3,9,8,7,5,6,4,0,2] 

print("\nPrinting the initial list:")
print(l)

# Removing elements from the list
l.remove(0)
print("\nPrinting list after removal of 0:")
print(l)

l.remove(l[3])
print("\nPrinting list after removal of third element:")
print(l)

# counting the number 
print("\nPrinting the count of a number:")
print(l.count(2))

# Reversing the list
print("\nPrinting the reversed list:")
l.reverse()
print(l)

# Sorting a list
print("\nPrinting the sorted list:")
l.sort()
print(l)


# Clearing the list
l.clear()
print("\nPrinting list after clearing:") 
print(l)

