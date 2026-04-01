"""
-------------------------------------------------------
Stack Split Alt
-------------------------------------------------------
Author:  Mwilu Siakachoma
ID:      169107092
Email:   siak7092@mylaurier.ca
__updated__ = "2025-01-25"
-------------------------------------------------------
"""
# Imports
from Stack_array import Stack
from functions import stack_split_alt
# Constants
source = Stack()
source.push(3)
source.push(2)
source.push(4)
source.push(8)
source.push(6)
target1, target2 = stack_split_alt(source)
print("Target 1: ", target1)
print("Target 2: ", target2)
