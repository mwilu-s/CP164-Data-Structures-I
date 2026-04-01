"""
-------------------------------------------------------
Sorted List Array Test
-------------------------------------------------------
Author:  Mwilu Siakachoma
ID:      169107092
Email:   siak7092@mylaurier.ca
__updated__ = "2025-02-09"
-------------------------------------------------------
"""
# Imports
from Sorted_List_array import Sorted_List
from Movie import Movie
from Movie_utilities import read_movies
# Constants

fh = open("movies.txt", "r", encoding="utf-8")

movies = read_movies(fh)
listMovies = Sorted_List()
emptied = listMovies.is_empty()
print("The list of movies should be empty (True): ", emptied)

for m in movies:
    listMovies.insert(m)

emptied2 = listMovies.is_empty()
print("\nThe list of movies should not be empty (False): ", emptied2)

if not listMovies.is_empty():
    print("\nWe are getting the 2nd item in the list: ", listMovies[1])

print("\nNow we will clean the list. This is the list before cleaning: ")
for m in listMovies:
    print(m, "\n")

listMovies.clean()
print("\nNow the list has been cleaned and looks like this: ")
for m in listMovies:
    print(m, "\n")

print("\nNow we will be combine lists")
list1 = Sorted_List()
list2 = Sorted_List()
list1.insert(movies[2])
list2.insert(movies[1])
listMovies.combine(list1, list2)
print("The list after combining them: ")
for m in listMovies:
    print(m, "\n")

print("\nNow we will clean the list again: ")
listMovies.clean()
for m in listMovies:
    print(m, "\n")

list1 = listMovies
list1.intersection(list1, list2)
print("\nThe lists after intersecting them: ")
for m in list1:
    print(m, "\n")

num = listMovies.count(listMovies[2])
print("\nCounting how many times", listMovies[2], "appears: ", num)

finding = listMovies.find(listMovies[1])
print("\nCan we find", listMovies[1], "?:\n", finding)

index = listMovies.index(listMovies[3])
print("\nFinding the index of", listMovies[3], ": ", index)

if listMovies.is_empty():
    maximum = listMovies.max()
    minimum = listMovies.min()
    print("\nThe maximum value in the list is ", maximum)
    print("And the minimum value is ", minimum)

peeked = listMovies.peek()
print("\nWe are peeking at the first value of the list which is", peeked)

if listMovies.is_empty():
    listMovies.remove_many(movies[1])
print("\nThe list after removing many movies: ")
for m in listMovies:
    print(m, "\n")

if len(listMovies) > 0:
    list1, list2 = listMovies.split()
print("\nThe lists after splitting it: ")
print("List1:")
for l1 in list1:
    print(l1, "\n")
print("\nList2:")
for l2 in list2:
    print(l2, "\n")


if len(listMovies) > 0:
    list1, list2 = listMovies.split_alt()
print("\nThe lists after splitting it alternatively: ")
print("List1:")
for l1 in list1:
    print(l1, "\n")

print("\nList2:")
for l2 in list2:
    print(l2, "\n")


if len(listMovies) > 0:
    list1, list2 = listMovies.split_key(listMovies[2])
print("\nThe lists after splitting it using a key: ")
print("List1:")
for l1 in list1:
    print(l1, "\n")

print("\nList2:")
for l2 in list2:
    print(l2, "\n")


list1 = Sorted_List()
list2 = Sorted_List()
list1.insert(movies[4])
list2.insert(movies[1])
listMovies.union(list1, list2)
print("\nThe list after uniting them: ")
for m in listMovies:
    print(m, "\n")

equals = list1 == list2
print("\nNow testing if list 1 is equal to list 2: ", equals)

check = movies[2] in listMovies
print("\nDetermining whether", movies[2], "is in the list: ", check)

print("\nAnd finally, the list:")
for m in listMovies:
    print(m, "\n")

fh.close()
