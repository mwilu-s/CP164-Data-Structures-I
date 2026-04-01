"""
-------------------------------------------------------
Genre Counts
-------------------------------------------------------
Author:  Mwilu Siakachoma
ID:      169107092
Email:   siak7092@mylaurier.ca
__updated__ = "2025-01-17"
-------------------------------------------------------
"""
# Imports
from Movie_utilities import genre_counts, read_movies
# Constants
filename = "movies.txt"
fh = open(filename, "r", encoding="utf-8")
movies = read_movies(fh)
counts = genre_counts(movies)
print(counts)
fh.close()
