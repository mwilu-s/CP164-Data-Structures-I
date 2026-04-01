"""
-------------------------------------------------------
ByCode
-------------------------------------------------------
Author:  Mwilu Siakachoma
ID:      169107092
Email:   siak7092@mylaurier.ca
__updated__ = "2025-03-07"
-------------------------------------------------------
"""
# Imports
from morse import ByCode
# Constants

mCode = ByCode('--', 'M')
sCode = ByCode('...', 'S')

print("The code of M:", mCode)
print("The code of S:", sCode)

equals = mCode == sCode
before = mCode < sCode
beforeEqual = mCode <= sCode

print("Is the code of M = the code of S ?", equals)
print("Is the code of M before the code of S?", before)
print("Is the code of M less than or equal to the code of S?", beforeEqual)
