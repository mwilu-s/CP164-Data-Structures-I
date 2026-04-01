"""
-------------------------------------------------------
Split Alt Recursive Method
-------------------------------------------------------
Author:  Mwilu Siakachoma
ID:      169107092
Email:   siak7092@mylaurier.ca
__updated__ = "2025-02-28"
-------------------------------------------------------
"""
# Imports
from List_linked import List
# Constants

lst = List()
entryNums = [1, 2, 3, 4, 5, 6, 7]

for v in entryNums:
    print("Entering", v, "into the list")
    lst.append(v)


even, odd = lst.split_alt_r()

print("\nThe EVEN list:")
for v in even:
    print(v)

print("\nThe ODD List:")
for v in odd:
    print(v)
