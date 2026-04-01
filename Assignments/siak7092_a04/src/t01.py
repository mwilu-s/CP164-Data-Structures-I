"""
-------------------------------------------------------
Testing Circular Queue
-------------------------------------------------------
Author:  Mwilu Siakachoma
ID:      169107092
Email:   siak7092@mylaurier.ca
__updated__ = "2025-02-01"
-------------------------------------------------------
"""
# Imports
from Queue_circular import Queue
# Constants

q1 = Queue()
empty1 = q1.is_empty()
print("We have created a new queue. It should be empty: ", empty1)
print("\nNow we are populating the queue")
i = 1
while not q1.is_full():
    q1.insert(i)
    i += 1

empty2 = q1.is_empty()
qFull = q1.is_full()
print("\nNow the queue should not be empty: ", empty2)
print("\nWe populated it to its full potential so now it should be full:", qFull)
maxQ = q1.DEFAULT_CAPACITY
print("\nThe maximum values that the queue can hold is", maxQ)
lenQ = len(q1)
print("\nTherefore, the queue the length should equal the maximum:", lenQ)
value = q1.peek()
print("\nWe are peeking at the first value and it is:", value)
q2 = Queue()
print("\nWe hae created another queue that is empty")
equals = q1 == q2
print("\nWe will determine whether the fully populated queue is equal to the empty queue and it should be false:", equals)
removedQ = q1.remove()
print("\nWe are now going to remove a value from the original queue which is full. The value removed is: ", removedQ)
lenQ2 = len(q1)
print("\nThe queue should now be one less of the maximum capacity values",
      maxQ, "So now there are", lenQ2, "values in the queue")

print("We are now iterating through the queue:")
for q in q1:
    print(q)
