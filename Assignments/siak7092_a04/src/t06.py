"""
-------------------------------------------------------
Split Key -- Priority Queue Array
-------------------------------------------------------
Author:  Mwilu Siakachoma
ID:      169107092
Email:   siak7092@mylaurier.ca
__updated__ = "2025-02-01"
-------------------------------------------------------
"""
# Imports
from Priority_Queue_array import Priority_Queue
# Constants
source = Priority_Queue()
source.insert(2)
source.insert(8)
source.insert(10)
source.insert(9)
source.insert(35)

key = 5
target1, target2 = source.split_key(key)
print("Target 1:")
for i in target1:
    print(i)
print("\nTarget 2:")
for i in target2:
    print(i)
