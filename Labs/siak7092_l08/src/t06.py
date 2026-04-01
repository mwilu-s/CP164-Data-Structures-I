"""
-------------------------------------------------------
Decode Morse
-------------------------------------------------------
Author:  Mwilu Siakachoma
ID:      169107092
Email:   siak7092@mylaurier.ca
__updated__ = "2025-03-07"
-------------------------------------------------------
"""
# Imports
from BST_linked import BST
from morse import fill_code_bst, decode_morse, DATA1
# Constants

bst = BST()
fill_code_bst(bst, DATA1)

morseCode = "... .... .-. . -.- .-.. --- ...- . ... -- . "
decoded = decode_morse(bst, morseCode)
print("Morse code: ", morseCode)
print("Decoded text: ", decoded)
