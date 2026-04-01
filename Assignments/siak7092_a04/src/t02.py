"""
-------------------------------------------------------
Equals for Queue Array
-------------------------------------------------------
Author:  Mwilu Siakachoma
ID:      169107092
Email:   siak7092@mylaurier.ca
__updated__ = "2025-02-01"
-------------------------------------------------------
"""
# Imports
from Queue_array import Queue
# Constants

q1 = Queue()
q2 = Queue()

i = 1
while i < 5:
    q1.insert(i)
    q2.insert(i)
    i = i + 1
    print("Item populated into Q1:", i)
    print("Item populated into Q2:", i)

print("Both queues have been populated now it is time to determine if they are equal.")
equals = q1 == q2
print("Are both queues equal? ", equals)
