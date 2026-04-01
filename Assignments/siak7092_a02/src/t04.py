"""
-------------------------------------------------------
Get By Genres
-------------------------------------------------------
Author:  Mwilu Siakachoma
ID:      169107092
Email:   siak7092@mylaurier.ca
__updated__ = "2025-01-17"
-------------------------------------------------------
"""
# Imports
from Movie_utilities import get_by_genres, read_movies
# Constants
filename = "movies.txt"
fh = open(filename, "r", encoding="utf-8")
movies = read_movies(fh)
genres = [1, 6]
movie_list = get_by_genres(movies, genres)
print(movie_list)
for m in movie_list:
    print(m, "\n")
fh.close()
