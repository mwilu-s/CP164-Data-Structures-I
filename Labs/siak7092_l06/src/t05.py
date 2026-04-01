"""
-------------------------------------------------------
Peek & Remove Methods -- Linked List
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
lst.append(20)
lst.append(10)
lst.append(2)
lst.append(7)
print("The list before removing anything:")
for v in lst:
    print(v)

peekValue = lst.peek()
print("\nThe peeked value before we remove anything: ", peekValue)
removeValue = lst.remove(10)
print("\nWe have removed the value", removeValue, "from the list")
print("\nNow the list looks like:")
for v in lst:
    print(v)
