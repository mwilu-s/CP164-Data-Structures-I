"""
-------------------------------------------------------
Hash Table
-------------------------------------------------------
Author:  Mwilu Siakachoma
ID:      169107092
Email:   siak7092@mylaurier.ca
__updated__ = "2025-03-13"
-------------------------------------------------------
"""
# Imports
from functions import hash_table
from Movie import Movie
from Hash_Set_array import Hash_Set
# Constants

movie1 = Movie("Shrek", 2005, "I am not sure", 10.0, [2, 4])
movie2 = Movie("Shrek 2", 2006, "I am not sure", 10.0, [2, 4])
movie3 = Movie("Shrek, The Third", 2007, "I am not sure", 10.0, [2, 4])
movie4 = Movie("Shrek Forever After", 2008, "I am not sure", 10.0, [2, 4])
movie5 = Movie("Shrek -- I hope this is not a flop",
               2009, "I am not sure", 10.0, [2, 4])

movieLst = []
movieLst.append(movie1)
movieLst.append(movie2)
movieLst.append(movie3)
movieLst.append(movie4)
movieLst.append(movie5)
hash_table(7, movieLst)
