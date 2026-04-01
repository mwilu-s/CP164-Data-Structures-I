"""
-------------------------------------------------------
Insert, Append and Remove Methods
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
print("Appending numbers 7,9,4 and 2 to the list\n")
llist.append(7)
llist.append(9)
llist.append(4)
llist.append(2)
print("The number(s) in the list:")
for i in llist:
    print(i)
print("\nNow inserting number 20 at position 3")
llist.insert(3, 20)
print("\nThe value at position 3 is", llist[3])
print("\nNow removing number 7")
value = llist.remove(7)
print("\nThe number removed is", value)
