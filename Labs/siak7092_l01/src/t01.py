"""
-------------------------------------------------------
Genre String
-------------------------------------------------------
Author:  Mwilu Siakachoma
ID:      169107092
Email:   siak7092@mylaurier.ca
__updated__ = "2025-01-11"
-------------------------------------------------------
"""
# Imports
from Movie import Movie
# Constants

example = Movie("Shrek", 2005, "Me", 9.9, [2, 4])
genres = example.genres_string()
print(genres)
