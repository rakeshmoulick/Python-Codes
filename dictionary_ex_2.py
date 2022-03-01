# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 11:57:00 2022

@author: Dr. Rakesh Moulick
"""

# Creating an empty Dictionary
Dict = {}
print("Empty Dictionary: ")
print(Dict)

# Adding elements one at a time
Dict[0] = 'Yes'
Dict[2] = 'No'
Dict[3] = 1
print("\nDictionary after adding 3 elements: ")
print(Dict)

# Adding set of values to a single Key
Dict['Value_set'] = 2, 3, 4
print("\nAdding set of values to a single Key: ")
print(Dict)

# Updating existing Key's Value
Dict[2] = 'Welcome'
print("\nUpdated key value: ")
print(Dict)

# Adding Nested Key value to Dictionary
Dict[5] = {'Nested' :{'1' : 'Life', '2' : 'Geeks'}}
print("\nAdding a Nested Key: ")
print(Dict)



