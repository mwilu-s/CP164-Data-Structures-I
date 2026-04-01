"""
-------------------------------------------------------
Intersection Recursive Method
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
randomList1 = [2, 4, 5, 1]
randomList2 = [6, 3, 5, 2]

for v in randomList1:
    lst.append(v)

for v in randomList2:
    lst2.append(v)

intersectList = List()
intersectList.intersection_r(lst, lst2)

print("After intersecting the lists:")
for v in intersectList:
    print(v)
