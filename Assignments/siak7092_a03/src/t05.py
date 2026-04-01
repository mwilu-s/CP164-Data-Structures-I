"""
-------------------------------------------------------
Palindrome
-------------------------------------------------------
Author:  Mwilu Siakachoma
ID:      169107092
Email:   siak7092@mylaurier.ca
__updated__ = "2025-01-25"
-------------------------------------------------------
"""
# Imports
from functions import is_palindrome_stack
# Constants
string = "racecar"
string2 = "Able was I ere I saw Elba"
string3 = "Cool pool"
pal1 = is_palindrome_stack(string)
pal2 = is_palindrome_stack(string2)
pal3 = is_palindrome_stack(string3)
print(f"Is '{string}' a palindrome? {pal1}")
print(f"Is '{string2}' a palindrome? {pal2}")
print(f"Is '{string3}' a palindrome? {pal3}")
