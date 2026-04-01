"""
-------------------------------------------------------
Deque Linked Methods Test
-------------------------------------------------------
Author:  Mwilu Siakachoma
ID:      169107092
Email:   siak7092@mylaurier.ca
__updated__ = "2025-03-01"
-------------------------------------------------------
"""
# Imports
from Deque_linked import Deque
# Constants

d1 = Deque()
d2 = Deque()

rnd1 = [8, 3, 1, 75]
rnd2 = [12, 5, 91, 6]

emptied = d1.is_empty()
print("We are checking if queue 1 is empty: ", emptied)
print("\nWe are populating deque 1 and deque 2 from the front")
for v in rnd1:
    d1.insert_front(v)
    d2.insert_front(v)

print("\nNow we check again if deque1 is empty: ", d1.is_empty())
num = len(d2)
print("\nHow many values are in deque 2? ", num)

print("\nWe are populating deque 1 and deque 2 from the rear")
for v in rnd2:
    d1.insert_rear(v)
    d2.insert_rear(v)
print("\nHow many values are in deque 2 now? ", len(d2))

v1 = d1.remove_front()
v2 = d2.remove_rear()

print("\nWe have removed one value from deque 1 and deque 2 each. d1 value from the front: ",
      v1, "and d2 value from the rear: ", v2)

peekVal = d2.peek_front()
peekVal2 = d1.peek_rear()
print("\n we are peeking into deque 2 and the value from the front is: ", peekVal)
print("\n we are peeking into deque 1 and the value from the rear is: ", peekVal2)

equals = d1 == d2
print("We check to see if d1 and d2 are equal: ", equals)
