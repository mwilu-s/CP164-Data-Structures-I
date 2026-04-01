"""
-------------------------------------------------------
Testing Lists
-------------------------------------------------------
Author:  Mwilu Siakachoma
ID:      169107092
Email:   siak7092@mylaurier.ca
__updated__ = "2025-02-01"
-------------------------------------------------------
"""
# Imports
from utilities import list_test
from List_array import List
from Movie_utilities import read_movies
# Constants
lst = List()
filename = "movies.txt"
fh = open(filename, "r", encoding="utf-8")
movies = read_movies(fh)
list_test(movies)
fh.close()
