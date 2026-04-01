"""
-------------------------------------------------------
Stack to Array
-------------------------------------------------------
Author:  Mwilu Siakachoma
ID:      169107092
Email:   siak7092@mylaurier.ca
__updated__ = "2025-01-17"
-------------------------------------------------------
"""
# Imports
from Stack_array import Stack
from utilities import stack_to_array, array_to_stack
# Constants

stack1 = Stack()
source1 = [1, "bob", 3, 4, "keke"]
array_to_stack(stack1, source1)
print(source1)
stack_to_array(stack1, source1)
print(source1)
