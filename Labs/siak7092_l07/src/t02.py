"""
-------------------------------------------------------
Is Identical Recursive Method
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
lst2 = List()
lst3 = List()
randomList = [10, 9, 2, 6, 7, 4]
randomList2 = []

for v in randomList2:
    lst3.append(v)

for v in randomList:
    lst.append(v)
    lst2.append(v)

print("Now we test to see if the lists (1 and 2) are identical\n")

identical1 = lst.is_identical_r(lst2)
print("List 1 and List 2 are identical? ", identical1)

print("\nNow we test to see if the lists (1 and 3) are identical\n")
identical2 = lst.is_identical_r(lst3)
print("List 1 and List 3 are identical? ", identical2)
