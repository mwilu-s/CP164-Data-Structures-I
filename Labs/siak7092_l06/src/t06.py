"""
-------------------------------------------------------
Get & Set Item Methods -- Linked List
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
movieList.append(mLst[0])
movieList.insert(0, mLst[4])
print("The list before we do anything to it:")
for m in movieList:
    print(m, "\n")
movieValue = movieList[2]
movieList[0] = "Shrek"
print("\nThe movie at index 2:", movieValue)
print("\nThe movie at index 0 is now:", movieList[0])
print("\nThe new movie list:")
for m in movieList:
    print(m, '\n')
