# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 12:07:28 2022

@author: Dr. Rakesh Moulick
"""

# Initial Dictionary
Dict = { 5 : 'Welcome', 6 : 'To', 7 : 'University',
		'A' : {1 : 'University', 2 : 'For', 3 : 'Students'},
		'B' : {1 : 'University', 2 : 'Life'}}
print("Initial Dictionary: ")
print(Dict)

# Deleting a Key value
del Dict[6]
print("\nDeleting a specific key: ")
print(Dict)

# Deleting a Key from
# Nested Dictionary
del Dict['A'][2]
print("\nDeleting a key from Nested Dictionary: ")
print(Dict)


