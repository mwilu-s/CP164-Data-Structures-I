"""
-------------------------------------------------------
Array to List and List to Array Methods
-------------------------------------------------------
Author:  Mwilu Siakachoma
ID:      169107092
Email:   siak7092@mylaurier.ca
__updated__ = "2025-02-01"
-------------------------------------------------------
"""
# Imports
from List_array import List
from utilities import array_to_list, list_to_array
# Constants
lst = List()
target = []
lst.append(1)
lst.append(2)
lst.append(3)
lst.append(4)
list_to_array(lst, target)
print("We have transfered the contents of the list to target. This is target", target)
