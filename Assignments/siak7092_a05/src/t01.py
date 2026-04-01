"""
-------------------------------------------------------
List Array Test
-------------------------------------------------------
Author:  Mwilu Siakachoma
ID:      169107092
Email:   siak7092@mylaurier.ca
__updated__ = "2025-02-09"
-------------------------------------------------------
"""
# Imports
from List_array import List
from Movie import Movie
from Movie_utilities import read_movies
# Constants

fh = open("movies.txt", "r", encoding="utf-8")

movies = read_movies(fh)
listMovies = List()
emptied = listMovies.is_empty()
print("The list of movies should be empty (True): ", emptied)

for m in movies:
    listMovies.append(m)

emptied2 = listMovies.is_empty()
print("The list of movies should not be empty (False): ", emptied2)

if not listMovies.is_empty():
    print("We are getting the 2nd item in the list: ", listMovies[1])

print("Now we will clean the list. This is the list before cleaning: ")
for m in listMovies:
    print(m, "\n")

listMovies.clean()
print("Now the list has been cleaned and looks like this: ")
for m in listMovies:
    print(m, "\n")

print("Now we will be combine lists")
list1 = List()
list2 = List()
list1.append(movies[3])
list2.append(movies[0])
listMovies.combine(list1, list2)
print("The list after combining them: ")
for m in listMovies:
    print(m, "\n")

print("Now we will clean the list again: ")
listMovies.clean()
for m in listMovies:
    print(m, "\n")

list1 = listMovies
list1.intersection(list1, list2)
print("The lists after intersecting them: ")
for m in list1:
    print(m, "\n")

listMovies.prepend(Movie("Shrek, A Tester", 2005, 10, None))
print("The list after prepending a movie: ")
for m in listMovies:
    print(m, "\n")

if listMovies.is_empty():
    listMovies.remove_many(movies[0])
print("The list after removing many movies: ")
for m in listMovies:
    print(m, "\n")

if len(listMovies) > 0:
    list1, list2 = listMovies.split()
print("The lists after splitting it: ")
print("List1:")
for l1 in list1:
    print(l1, "\n")
print("List2:")
for l2 in list2:
    print(l2, "\n")


if len(listMovies) > 0:
    list1, list2 = listMovies.split_alt()
print("The lists after splitting it: ")
print("List1:")
for l1 in list1:
    print(l1, "\n")

print("List2:")
for l2 in list2:
    print(l2, "\n")


list1 = List()
list2 = List()
list1.append(movies[3])
list2.append(movies[0])
listMovies.union(list1, list2)
print("The list after uniting them: ")
for m in listMovies:
    print(m, "\n")

equals = list1 == list2
print("Now testing if list 1 is equal to list 2: ", equals)

print("And finally, the list:")
for m in listMovies:
    print(m, "\n")

fh.close()
