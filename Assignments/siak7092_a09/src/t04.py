"""
-------------------------------------------------------
More Methods
-------------------------------------------------------
Author:  Mwilu Siakachoma
ID:      169107092
Email:   siak7092@mylaurier.ca
__updated__ = "2025-03-20"
-------------------------------------------------------
"""
# Imports
from BST_linked import BST
# Constants

bst = BST()

bst.insert(7)
bst.insert(34)
bst.insert(416)
bst.insert(8351)

one, two, three = bst.node_counts()

print(one)
print(two)
print(three)

contained = 7 in bst

print("Is 7 in bst?: ", contained)

value = bst.parent(7)
value2 = bst.parent_r(4)

print(value, value2)
