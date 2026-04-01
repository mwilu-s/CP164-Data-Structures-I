"""
-------------------------------------------------------
PQ Split Key -- Functions
-------------------------------------------------------
Author:  Mwilu Siakachoma
ID:      169107092
Email:   siak7092@mylaurier.ca
__updated__ = "2025-02-01"
-------------------------------------------------------
"""
# Imports
from functions import pq_split_key
from Priority_Queue_array import Priority_Queue
# Constants

source = Priority_Queue()
source.insert(4)
source.insert(3)
source.insert(5)
source.insert(9)
source.insert(2)

key = 5
target1, target2 = pq_split_key(source, key)
print("Target 1:")
for i in target1:
    print(i)
print("\nTarget 2:")
for i in target2:
    print(i)
