"""
-------------------------------------------------------
Read Movie
-------------------------------------------------------
Author:  Mwilu Siakachoma
ID:      169107092
Email:   siak7092@mylaurier.ca
__updated__ = "2025-01-11"
-------------------------------------------------------
"""
# Imports
from Movie_utilities import read_movie
# Constants
line = "Shrek|2005|Me|9.9|3,5"
movie = read_movie(line)
print(movie)
