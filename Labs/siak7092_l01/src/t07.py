"""
-------------------------------------------------------
Read Movies
-------------------------------------------------------
Author:  Mwilu Siakachoma
ID:      169107092
Email:   siak7092@mylaurier.ca
__updated__ = "2025-01-11"
-------------------------------------------------------
"""
# Imports
from Movie_utilities import read_movies
# Constants
filename = "movies.txt"
fh = open(filename, "r", encoding="utf-8")
movies = read_movies(fh)
print(movies)
fh.close()
