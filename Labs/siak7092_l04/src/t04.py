"""
-------------------------------------------------------
Index, Find, Contains, Count, Max and Min Methods
-------------------------------------------------------
Author:  Mwilu Siakachoma
ID:      169107092
Email:   siak7092@mylaurier.ca
__updated__ = "2025-01-31"
-------------------------------------------------------
"""
# Imports
from List_array import List
# Constants
llist = List()
llist.append(7)
llist.append(6)
llist.append(20)
llist.append(4)

index1 = llist.index(7)
print("The index of the first number 7 in the list is", index1)
findValue = llist.find(4)
print("\nThe value found for the key = 4:", findValue)
containsNum = 6 in llist
print("\nIs the number 6 in the list?", containsNum)
countNum = llist.count(10)
print("How many times does the number 10 appear in the list:", countNum)
maxV = llist.max()
minV = llist.min()
print(f"""\nThe maximum value in the list is {
      maxV} and the minimum value is {minV}""")
