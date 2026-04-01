"""
-------------------------------------------------------
Encode Morse
-------------------------------------------------------
Author:  Mwilu Siakachoma
ID:      169107092
Email:   siak7092@mylaurier.ca
__updated__ = "2025-03-07"
-------------------------------------------------------
"""
# Imports
from BST_linked import BST
from morse import fill_letter_bst, encode_morse, DATA1
# Constants

bst = BST()
fill_letter_bst(bst, DATA1)

text = "I LOVE SHREK"
morseCode = encode_morse(bst, text)
print("The original text:", text)
print("The morse code:", morseCode)
