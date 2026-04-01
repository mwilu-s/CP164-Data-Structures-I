"""
-------------------------------------------------------
Median Scores
-------------------------------------------------------
Author:  Mwilu Siakachoma
ID:      169107092
Email:   siak7092@mylaurier.ca
__updated__ = "2025-01-11"
-------------------------------------------------------
"""
# Imports
from functions import median_scores
# Constants

filename = "numbers.txt"
fh = open(filename, "r", encoding="utf-8")
median = median_scores(fh)
print(median)
fh.close()
