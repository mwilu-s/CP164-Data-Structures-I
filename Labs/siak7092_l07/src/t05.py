"""
-------------------------------------------------------
Union Recursive Method
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
rndLst = [2, 4, 6, 1, 3, 5, 7]
rndLst2 = [10, 3, 12, 4, 5, 20, 6]

for v in rndLst:
    lst.append(v)

for v in rndLst2:
    lst.append(v)


unionLst = List()
unionLst.union_r(lst, lst2)

print("After uniting list 1 and 2, this is the resulting list:")
for v in unionLst:
    print(v)
