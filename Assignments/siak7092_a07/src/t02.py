"""
-------------------------------------------------------
Testing Sorted List Linked Methods
-------------------------------------------------------
Author:  Mwilu Siakachoma
ID:      169107092
Email:   siak7092@mylaurier.ca
__updated__ = "2025-03-07"
-------------------------------------------------------
"""
# Imports
from Sorted_List_linked import Sorted_List
from Movie_utilities import read_movies
# Constants

filename = "movies.txt"
fh = open(filename, "r", encoding="utf-8")
movies = read_movies(fh)

movieLst = Sorted_List()
emptied = movieLst.is_empty()
print("Before we populate the list, is it empty?: ", emptied)
print("\nNow we will populate our list with the movies.")
for m in movies:
    movieLst.insert(m)

print("\nWe have populated the list, checking if it is empty: ", movieLst.is_empty())

rnd1 = [4, 25, 90, 19]
lst2 = Sorted_List()
equals = movieLst == lst2
print("\nWe will check to see if list 2 and the movie list are equal: ", equals)
found = movies[0] in movieLst
print("\nWe are going to check if the movie: ",
      movies[0], "is in the list:", found)

print("\nWe are now populating list 2.")
for r in rnd1:
    lst2.insert(r)

print("\nWe will clean up the movie list.")
movieLst.clean()

maxV = movieLst.max()
minV = movieLst.min()
print("\nThe maximum value in the list is:", maxV, "and the minimum is:", minV)

peekVal = movieLst.peek()
print("We will peek into the list and the first value is: ", peekVal)

findVal = movieLst.find(movies[3])
print("We are looking for the movie: ",
      movies[3], "the value returned is: ", findVal)

indexV = movieLst.index(movies[3])
print("We are looking for the index of the movie: ",
      movies[3], "the index returned is: ", indexV)

value = movieLst.remove_front()
print("\nNow we will just remove the first value in the list which is: ", value)

target1 = Sorted_List()
target2 = Sorted_List()

print("We will now update the movie list with the targets 1 and 2 and see for intersection")
movieLst.intersection(target2, target1)
print("\nWe check to see if the movie list has been emptied again: ",
      movieLst.is_empty())
print("\nWe will print the contents of the movie list:")
for m in movieLst:
    print(m)


movies2 = Sorted_List()
print("\nNow we will combine target 2 and 1 into a new movie list.")
movies2.combine(target2, target2)
print("\nWe will print the contents of the second movie list:")
for m in movies2:
    print(m)

print("\nWe will try to unite target1 and target2 into the second movie list")
movies2.union(target1, target2)

print("\nWe will print the contents of the second movie list:")
for m in movies2:
    print(m)

fh.close()
