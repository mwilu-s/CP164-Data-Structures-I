"""
-------------------------------------------------------
Radix -- Linked List
-------------------------------------------------------
Author:  Mwilu Siakachoma
ID:      169107092
Email:   siak7092@mylaurier.ca
__updated__ = "2025-03-26"
-------------------------------------------------------
"""
# Imports
from List_linked import List
from Sorts_List_linked import Sorts
# Constants

numList = List()
randValues = [2, 7, 7, 100, 4, 65, 23, 20, 1, 8]

for v in randValues:
    numList.append(v)

print("The original list:\n")
for v in numList:
    print(v)

Sorts.radix_sort(numList)

print("\nThe sorted list:\n")
for v in numList:
    print(v)
