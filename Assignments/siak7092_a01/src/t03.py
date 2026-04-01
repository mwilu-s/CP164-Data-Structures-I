"""
-------------------------------------------------------
File Ananlyse
-------------------------------------------------------
Author:  Mwilu Siakachoma
ID:      169107092
Email:   siak7092@mylaurier.ca
__updated__ = "2025-01-11"
-------------------------------------------------------
"""
# Imports
from functions import file_analyze
# Constants

filename = input("Enter the filename: ")
fh = open(filename, "r", encoding="utf-8")
upp, low, dig, whi, rem = file_analyze(fh)
print(f"""Upper: {upp}, Lower: {low}, Digit: {
      dig}, Whitespace: {whi}, Remaining: {rem}""")
fh.close()
