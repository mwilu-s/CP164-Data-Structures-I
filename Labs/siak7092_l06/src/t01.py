"""
-------------------------------------------------------
Prepend, Append, Insert Methods -- Linked List
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
print("Here is each movie that has been prepended, appended and inserted:\n")
for m in movieList:
    print(m, "\n")


fh.close()
