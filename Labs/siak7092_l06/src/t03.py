"""
-------------------------------------------------------
Count, Max, Min Methods -- Linked Lists
-------------------------------------------------------
Author:  Mwilu Siakachoma
ID:      169107092
Email:   siak7092@mylaurier.ca
__updated__ = "2025-02-14"
-------------------------------------------------------
"""
# Imports
from List_linked import List
# Constants

lst = List()
lst.append(1)
lst.append(7)
lst.append(8)
lst.append(5)
lst.append(1)
count = lst.count(1)
minV = lst.min()
maxV = lst.max()

print("Counting the number '1': ", count,
      "\nThe max Value: ", maxV, "\nThe min value: ", minV)
