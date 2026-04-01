"""
-------------------------------------------------------
ByLetter
-------------------------------------------------------
Author:  Mwilu Siakachoma
ID:      169107092
Email:   siak7092@mylaurier.ca
__updated__ = "2025-03-07"
-------------------------------------------------------
"""
# Imports
from morse import ByLetter
# Constants
m = ByLetter('M', '--')
s = ByLetter('S', '...')

print("The letter M:", m)
print("The letter S:", s)

equals = m == s
before = m < s
beforeEqual = m <= s

print("Is M = S ?", equals)
print("Is M before S?", before)
print("Is M less than or equal to S?", beforeEqual)
