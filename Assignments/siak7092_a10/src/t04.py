"""
-------------------------------------------------------
Gnome -- Deque Linked List
-------------------------------------------------------
Author:  Mwilu Siakachoma
ID:      169107092
Email:   siak7092@mylaurier.ca
__updated__ = "2025-03-26"
-------------------------------------------------------
"""
# Imports
from Deque_linked import Deque
from Sorts_Deque_linked import Sorts
# Constants

dqList = Deque()
randValues = [32, 7, 64, 101, 4, 91, 23, 19, 1, 2]

for v in randValues:
    dqList.insert_rear(v)

print("The original list:\n")
for v in dqList:
    print(v)

Sorts.gnome_sort(dqList)

print("\nThe sorted list:\n")
for v in dqList:
    print(v)
