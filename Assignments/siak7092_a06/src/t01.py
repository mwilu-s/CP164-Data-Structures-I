"""
-------------------------------------------------------
Testing Queue Linked Methods
-------------------------------------------------------
Author:  Mwilu Siakachoma
ID:      169107092
Email:   siak7092@mylaurier.ca
__updated__ = "2025-03-01"
-------------------------------------------------------
"""
# Imports
from Queue_linked import Queue
# Constants

q1 = Queue()
q2 = Queue()

rnd1 = [2, 3, 4, 5]
emptied = q1.is_empty()
print("We are checking if queue 1 is empty: ", emptied)
print("\nWe are checking if queue 2 is full: ", q2.is_full())
print("\nWe are populating queue 1 and queue 2")
for v in rnd1:
    q1.insert(v)
    q2.insert(v)

print("\nNow we check again if queue1 is empty: ", q1.is_empty())
num = len(q2)
print("\nHow many values are in queue 2? ", num)

v1 = q1.remove()
v2 = q2.remove()

print("\nWe have removed one value from queue 1 and queue 2 each. q1 value: ",
      v1, "and q2 value: ", v2)

peekVal = q2.peek()

print("\n we are peeking into queue 2 and the value is: ", peekVal)

q3 = Queue()
q3.combine(q1, q2)
print("\nWe have created a third queue and combined q1 and q2 into q3")
print("This is queue 3:")
for v in q3:
    print(v)

print("\nAre q1 and q2 empty? q1 emptied: ",
      q1.is_empty(), "and q2 emptied: ", q2.is_empty())
print("\nNow we are going to split q3 back into q1 and q2")
q1, q2 = q3.split_alt()

print("\nWe check to see if q3 is empty: ", q3.is_empty())

print("\nNow we will print q1:")
for v in q1:
    print(v)

print("\nPrinting q2:")
for v in q2:
    print(v)
equals = q1 == q2
print("We check to see if q1 and q2 are equal: ", equals)
