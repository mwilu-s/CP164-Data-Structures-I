"""
-------------------------------------------------------
Fill_letter_bst
-------------------------------------------------------
Author:  Mwilu Siakachoma
ID:      169107092
Email:   siak7092@mylaurier.ca
__updated__ = "2025-03-07"
-------------------------------------------------------
"""
# Imports
from BST_linked import BST
from morse import fill_letter_bst, DATA1
# Constants

bst = BST()
fill_letter_bst(bst, DATA1)

print("BST data: ")
for each in bst:
    print(each, "\n")
