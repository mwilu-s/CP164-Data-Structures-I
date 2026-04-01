"""
-------------------------------------------------------
Insert and Remove
-------------------------------------------------------
Author:  Mwilu Siakachoma
ID:      169107092
Email:   siak7092@mylaurier.ca
__updated__ = "2025-03-14"
-------------------------------------------------------
"""
# Imports

from Movie import Movie
from Hash_Set_array import Hash_Set
# Constants

movie1 = Movie("Shrek", 2005, "I am not sure", 9.7, [2, 4])
movie2 = Movie("Shrek 2", 2006, "I am not sure", 10.0, [2, 4])
movie3 = Movie("Shrek, The Third", 2007, "I am not sure", 9.5, [2, 4])
movie4 = Movie("Shrek Forever After", 2008, "I am not sure", 7.5, [2, 4])
movie5 = Movie("Shrek 5 -- I hope this is not a flop",
               2009, "I am not sure", 8, [2, 4])

movieLst = Hash_Set(5)
movieLst.insert(movie1)
movieLst.insert(movie2)
movieLst.insert(movie3)
movieLst.insert(movie4)
movieLst.insert(movie5)
print("With Shrek Forever After:\n")
for m in movieLst:
    print(m, "\n")

movieLst.remove(movie4)
print("Without Shrek Forever After:\n")
for m in movieLst:
    print(m, "\n")
