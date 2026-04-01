"""
-------------------------------------------------------
Queue Utilities
-------------------------------------------------------
Author:  Mwilu Siakachoma
ID:      169107092
Email:   siak7092@mylaurier.ca
__updated__ = "2025-01-24"
-------------------------------------------------------
"""
# Imports
from utilities import array_to_queue, queue_to_array, queue_test
from Queue_array import Queue
# Constants
q1 = Queue()
source = [1, 8, 3, 4, 5, 7]
array_to_queue(q1, source)
print("The source should now look like: ", source)
queue_to_array(q1, source)
print("The target looks like:", source)
queue_test(source)
