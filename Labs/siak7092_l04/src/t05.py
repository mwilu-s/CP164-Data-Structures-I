"""
-------------------------------------------------------
Get and Set Item
-------------------------------------------------------
Author:  Mwilu Siakachoma
ID:      169107092
Email:   siak7092@mylaurier.ca
__updated__ = "2025-01-31"
-------------------------------------------------------
"""
# Imports
from List_array import List
# Constants

llist = List()
llist.insert(1, 9)
value = llist[0]
print("The value at position 0 is", value)
llist[0] = 7
print("Now the value at position 0 is", llist[0])
