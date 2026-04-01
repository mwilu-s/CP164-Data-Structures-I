"""
-------------------------------------------------------
Combine Method for Queue_array
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
q1.insert(10)
q1.insert(20)
q1.insert(30)

q2.insert(40)
q2.insert(50)
q2.insert(60)

q3 = Queue()
q4 = Queue()

q3.insert(70)
q3.insert(80)
q4.insert(90)

target = Queue()
target.combine(q1, q2)
target2 = Queue()
target2.combine(q3, q4)

print("The resulting target of q1 and q2:")
for i in target:
    print(i)
print("\nThe resulting target of q3 and q4:")
for t in target2:
    print(t)
