"""
-------------------------------------------------------
Priority Queues Utilities
-------------------------------------------------------
Author:  Mwilu Siakachoma
ID:      169107092
Email:   siak7092@mylaurier.ca
__updated__ = "2025-01-24"
-------------------------------------------------------
"""
# Imports
from Priority_Queue_array import Priority_Queue
from Movie_utilities import read_movies
from utilities import array_to_pq, pq_to_array, priority_queue_test
# Constants
q1 = Priority_Queue()
filename = "movies.txt"
fh = open(filename, "r", encoding="utf-8")
source = [1, 2, 3, 4, 5]
movies = read_movies(fh)
array_to_pq(q1, source)
print("The source should now look like: ", source)
pq_to_array(q1, source)
print("The target looks like:", source)
priority_queue_test(movies)
fh.close()
