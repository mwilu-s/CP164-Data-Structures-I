"""
-------------------------------------------------------
Combine Method
-------------------------------------------------------
Author:  Mwilu Siakachoma
ID:      169107092
Email:   siak7092@mylaurier.ca
__updated__ = "2025-02-01"
-------------------------------------------------------
"""
# Imports
from functions import queue_combine
from Queue_array import Queue
# Constants

q1 = Queue()
q2 = Queue()
q1.insert(1)
q1.insert(2)
q1.insert(3)

q2.insert(4)
q2.insert(5)
q2.insert(6)

q3 = Queue()
q4 = Queue()

q3.insert(7)
q3.insert(8)
q4.insert(9)

target = queue_combine(q1, q2)

target2 = queue_combine(q3, q4)

print("The resulting target of q1 and q2:")
for i in target:
    print(i)
print("\nThe resulting target of q3 and q4:")
for t in target2:
    print(t)
