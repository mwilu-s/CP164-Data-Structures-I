"""
-------------------------------------------------------
Reroute
-------------------------------------------------------
Author:  Mwilu Siakachoma
ID:      169107092
Email:   siak7092@mylaurier.ca
__updated__ = "2025-01-25"
-------------------------------------------------------
"""
# Imports
from functions import reroute
# Constants
opstring = "SSXSSXXX"
values = [5, 6, 7, 8]
values_out = reroute(opstring, values)
print(values_out)
