"""
-------------------------------------------------------
List Linked Methods Testing
-------------------------------------------------------
Author:  Mwilu Siakachoma
ID:      169107092
Email:   siak7092@mylaurier.ca
__updated__ = "2025-03-07"
-------------------------------------------------------
"""
# Imports
from List_linked import List
from Movie_utilities import read_movies
# Constants
filename = "movies.txt"
fh = open(filename, "r", encoding="utf-8")
movies = read_movies(fh)

movieLst = List()
emptied = movieLst.is_empty()
print("Before we populate the list, is it empty?: ", emptied)
print("\nNow we will populate our list with the movies.")
for m in movies:
    movieLst.append(m)

print("\nWe have populated the list, checking if it is empty: ", movieLst.is_empty())
itemMovie = movieLst[2]
print("The third movie item in the list is: ", itemMovie)

rnd1 = [2, 3, 4]
lst2 = List()
equals = movieLst == lst2
print("\nWe will check to see if list 2 and the movie list are equal: ", equals)
print("\nWe are now populating list 2.")
for r in rnd1:
    lst2.append(r)

print("\nWe will clean up the movie list.")
movieLst.clean()

print("\nWe will prepend a movie to the front of the list.")
movieLst.prepend(movies[3])
print("\nNow the list looks like this:")
for m in movieLst:
    print(m)

print(
    "\nWe will now remove many items from the list that is the same as this movie: ", movies[3])
movieLst.remove_many(movies[3])
value = movieLst.remove_front()
print("\nNow we will just remove the first value in the list which is: ", value)

target1 = List()
target2 = List()

print("\nWe will now split the movie list")
target1, target2 = movieLst.split()
print("\nWe check to see if the movie list has been emptied: ", movieLst.is_empty())
print("\nNow we will print the contents of target1:")
for t in target1:
    print(t)
print("\nAnd now we will print the contents of target2:")
for t2 in target2:
    print(t2)

print("\nNow we will populate our list with the movies again and split them alternatively.")
for m in movies:
    movieLst.append(m)

target3 = List()
target4 = List()

target3, target4 = movieLst.split_alt()

print("\nWe check to see if the movie list has been emptied again: ",
      movieLst.is_empty())
print("\nNow we will print the contents of target1:")
for t3 in target3:
    print(t3)
print("\nAnd now we will print the contents of target2:")
for t4 in target4:
    print(t4)

print("We will now update the movie list with the targets 1 and 3 and see for intersection")
movieLst.intersection(target3, target1)
print("\nWe check to see if the movie list has been emptied again: ",
      movieLst.is_empty())
print("\nWe will print the contents of the movie list:")
for m in movieLst:
    print(m)


movies2 = List()
print("\nNow we will combine target 2 and 4 into a new movie list.")
movies2.combine(target2, target4)
print("\nWe will print the contents of the second movie list:")
for m in movies2:
    print(m)

print("\nWe will try to unite target1 and target4 into the second movie list")
movies2.union(target1, target4)

print("\nWe will print the contents of the second movie list:")
for m in movies2:
    print(m)

fh.close()
