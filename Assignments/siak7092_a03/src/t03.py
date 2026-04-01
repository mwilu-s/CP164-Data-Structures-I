"""
-------------------------------------------------------
Stack Reverse
-------------------------------------------------------
Author:  Mwilu Siakachoma
ID:      169107092
Email:   siak7092@mylaurier.ca
__updated__ = "2025-01-25"
-------------------------------------------------------
"""
# Imports
from Stack_array import Stack
from functions import stack_reverse
# Constants

s1 = Stack()
s1.push(3)
s1.push(2)
s1.push(1)
stack_reverse(s1)
print(s1.pop())
print(s1.pop())
print(s1.pop())
