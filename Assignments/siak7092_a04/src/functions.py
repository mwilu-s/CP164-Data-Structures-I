"""
-------------------------------------------------------
Functions
-------------------------------------------------------
Author:  Mwilu Siakachoma
ID:      169107092
Email:   siak7092@mylaurier.ca
__updated__ = "2025-02-01"
-------------------------------------------------------
"""
# Imports
from Queue_array import Queue
from Priority_Queue_array import Priority_Queue
# Constants


def queue_combine(source1, source2):
    """
    -------------------------------------------------------
    Combines two source queues into the current target queue.
    When finished, the contents of source1 and source2 are interlaced
    into target and source1 and source2 are empty.
    Order of source values is preserved.
    (iterative algorithm)
    Use: target = queue_combine(source1, source2)
    -------------------------------------------------------
    Parameters:
        source1 - a queue (Queue)
        source2 - a queue (Queue)
    Returns:
        target - a queue (Queue)
    -------------------------------------------------------
    """
    target = Queue()

    if len(source1) == len(source2):
        i = 0
        while not source2.is_empty():
            if i == 0:
                target.insert(source1.remove())
            elif i % 2 == 0:
                target.insert(source1.remove())
            else:
                target.insert(source2.remove())

            i += 1

    else:
        if len(source1) > len(source2):
            i = 0
            while not source1.is_empty():
                if i == 0:
                    target.insert(source1.remove())
                elif i % 2 == 0:
                    target.insert(source1.remove())
                elif len(source2) == 0:
                    target.insert(source1.remove())
                else:
                    target.insert(source2.remove())

                i += 1

        else:
            i = 0
            while not source2.is_empty():
                if i == 0:
                    target.insert(source1.remove())
                elif i % 2 == 0:
                    target.insert(source1.remove())
                elif len(source1) == 0:
                    target.insert(source2.remove())
                else:
                    target.insert(source2.remove())

                i += 1

    return target


def pq_split_key(source, key):
    """
    -------------------------------------------------------
    Splits a priority queue into two depending on an external
    priority key. The source priority queue is empty when the method
    ends.
    Use: target1, target2 = pq_split_key(source, key)
    -------------------------------------------------------
    Parameters:
        source - a priority queue (Priority_Queue)
        key - a data object (?)
    Returns:
        target1 - a priority queue that contains all values
            with priority higher than key (Priority_Queue)
        target2 - priority queue that contains all values with
            priority lower than or equal to key (Priority_Queue)
    -------------------------------------------------------
    """
    target1 = Priority_Queue()
    target2 = Priority_Queue()

    while not source.is_empty():
        pq = source.remove()
        if pq > key:
            target2.insert(pq)
        else:
            target1.insert(pq)

    return target1, target2
