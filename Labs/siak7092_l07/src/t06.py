"""
-------------------------------------------------------
Reverse Recursive Method
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
rndLst = [2, 4, 6, 1, 3, 5, 7]

for v in rndLst:
    print("Entering", v, "into the list")
    lst.append(v)

print("\nThis is how the list looks before reversing")
for v in lst:
    print(v)

lst.reverse_r()
print("\nThis is the reversed list:")
for v in lst:
    print(v)
