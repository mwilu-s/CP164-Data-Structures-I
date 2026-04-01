"""
-------------------------------------------------------
Find, Index, Contains Methods -- Linked List
-------------------------------------------------------
Author:  Mwilu Siakachoma
ID:      169107092
Email:   siak7092@mylaurier.ca
__updated__ = "2025-02-14"
-------------------------------------------------------
"""
# Imports
from List_linked import List
from Movie_utilities import read_movies
# Constants

movieList = List()
fh = open("movies.txt", "r", encoding="utf-8")
mLst = read_movies(fh)
movieList.prepend(mLst[2])
movieList.append(mLst[1])
movieList.insert(0, mLst[3])

findMovie = movieList.find(mLst[1])
indexMovie = movieList.index(mLst[2])
containMovie = mLst[3] in movieList

print("find Movie ", mLst[1], ": \n\n", findMovie)
print("\nindex of Movie ", mLst[1], ": \n", indexMovie)
print("\nDoes list contain Movie ", mLst[1], ": \n", containMovie)
