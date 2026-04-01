"""
-------------------------------------------------------
Tests various array-based sorting functions.
-------------------------------------------------------
Author:  David Brown
ID:      999999999
Email:   dbrown@wlu.ca
Section: CP164 C
__updated__ = "2025-03-20"
-------------------------------------------------------
"""
# Imports
import random
from Number import Number
from Sorts_array import Sorts

# Constants
SIZE = 100  # Size of array to sort.
XRANGE = 1000  # Range of values in random arrays to sort.
TESTS = 100  # Number of random arrays to generate.

SORTS = (
    ('Bubble Sort', Sorts.bubble_sort),
    ('Insertion Sort', Sorts.insertion_sort),
    ('Merge Sort', Sorts.merge_sort),
    ('Quick Sort', Sorts.quick_sort),
    ('Selection Sort', Sorts.selection_sort),
    ('Bin. Ins. Sort', Sorts.binary_insert_sort),
    ('BST Sort', Sorts.bst_sort),
    ('Cocktail Sort', Sorts.cocktail_sort),
    ('Comb Sort', Sorts.comb_sort),
    ('Heap Sort', Sorts.heap_sort),
    ('Shell Sort', Sorts.shell_sort)
)


def create_sorted():
    """
    -------------------------------------------------------
    Creates a sorted list of SIZE Number objects with values
        from 0 up to SIZE-1.
    Use: values = create_sorted()
    -------------------------------------------------------
    Returns:
        values - a sorted list of SIZE Number objects (list of Number)
    -------------------------------------------------------
    """
    values = []

    for n in range(SIZE):
        number = Number(n)
        values.append(number)

    # your code here

    return values


def create_reversed():
    """
    -------------------------------------------------------
    Create a reversed list of SIZE Number objects with values
        from SIZE-1 down to 0.
    Use: values = create_reversed()
    -------------------------------------------------------
    Returns:
        values - a reversed list of SIZE Number objects (list of Number)
    -------------------------------------------------------
    """
    values = []

    for n in range(SIZE - 1, -1, -1):
        number = Number(n)
        values.append(number)

    # your code here

    return values


def create_randoms():
    """
    -------------------------------------------------------
    Create a 2D list of Number objects with TESTS rows and
    SIZE columns of values between 0 and XRANGE.
    Use: lists = create_randoms()
    -------------------------------------------------------
    Returns:
        arrays - TESTS lists of SIZE Number objects containing
            values between 0 and XRANGE (list of list of Number)
    -------------------------------------------------------
    """
    arrays = []

    for i in range(TESTS):
        array1 = []

        for j in range(TESTS):
            array1.append(Number(random.randint(0, XRANGE)))

        arrays.append(array1)

    # your code here

    return arrays


def test_sort(title, func):
    """
    -------------------------------------------------------
    Test a sort function with Number data and prints the number 
    of comparisons necessary to sort an array:
    in order, in reverse order, and a list of arrays in random order.
    Use: test_sort(title, func)
    -------------------------------------------------------
    Parameters:
        title - name of the sorting function to call (str)
        func - the actual sorting function to call (function)
    Returns:
        None
    -------------------------------------------------------
    """
    Sorts.swap = 0
    Number.comparisons = 0

    sortCreated = create_sorted()
    sortReversed = create_reversed()
    sortRandom = create_randoms()

    func(sortCreated)
    num1 = Number.comparisons
    num2 = round(Sorts.swaps, 0)
    Sorts.swaps = 0
    Number.comparisons = 0

    func(sortReversed)
    num3 = Number.comparisons
    num4 = round(Sorts.swaps, 0)
    Sorts.swaps = 0
    Number.comparisons = 0

    for s in sortRandom:
        func(s)
    num5 = Number.comparisons // TESTS
    num6 = Sorts.swaps // TESTS
    Sorts.swaps = 0
    Number.comparisons = 0

    print("{:14} {:8} {:8} {:8} {:8} {:8} {:8}".format(
        title, num1, num3, num5, num2, num4, num6))

    # your code here

    return None
