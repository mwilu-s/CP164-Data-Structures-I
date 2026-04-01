"""
-------------------------------------------------------
Stack Test With Movie Objects
-------------------------------------------------------
Author:  Mwilu Siakachoma
ID:      169107092
Email:   siak7092@mylaurier.ca
__updated__ = "2025-01-18"
-------------------------------------------------------
"""
# Imports
from Movie_utilities import read_movies
from utilities import stack_test
# Constants
filename = "movies.txt"
fh = open(filename, "r", encoding="utf-8")
movies = read_movies(fh)
stack_test(movies)
fh.close()
