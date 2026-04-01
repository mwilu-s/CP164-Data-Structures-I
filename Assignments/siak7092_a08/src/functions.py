"""
-------------------------------------------------------
Functions
-------------------------------------------------------
Author:  Mwilu Siakachoma
ID:      169107092
Email:   siak7092@mylaurier.ca
__updated__ = "2025-03-14"
-------------------------------------------------------
"""
# Imports
from BST_linked import BST
from Letter import Letter
# Constants


def do_comparisons(file_variable, bst):
    """
    -------------------------------------------------------
    Retrieves every letter in file_variable from bst. Generates
    comparisons in bst objects. Each Letter object in bst contains
    the number of comparisons found by searching for that Letter
    object in file_variable.
    Use: do_comparisons(file_variable, bst)
    -------------------------------------------------------
    Parameters:
        file_variable - the already open file containing data to evaluate (file)
        bst - the binary search tree containing 26 Letter objects
            to retrieve data from (BST)
    Returns:
        None
    -------------------------------------------------------
    """
    # Zeroes out all comparison values in tree nodes
    for node in bst:
        node.comparisons = 0

    line = file_variable.readline()
    lines = []

    while line != "":
        lines.append(line.strip())
        line = file_variable.readline()

    for line in lines:
        for l in line:
            if l.isalpha():
                tempL = Letter(l.upper())
                bst.retrieve(tempL)

    file_variable.close()

    return None


def comparison_total(bst):
    """
    -------------------------------------------------------
    Sums the comparison values of all Letter objects in bst.
    Use: total = comparison_total(bst)
    -------------------------------------------------------
    Parameters:
        bst - a binary search tree of Letter objects (BST)
    Returns:
        total - the total of all comparison fields in the bst
            Letter objects (int)
    -------------------------------------------------------
    """
    total = 0
    value = bst.inorder()

    for l in value:
        total = total + l.comparisons

    return total


def fill_BST(bst, data):
    for l in data:
        value = Letter(l)
        bst.insert(value)
    return None


def letter_table(bst):
    """
    -------------------------------------------------------
    Prints a table of letter counts for each Letter object in bst.
    Use: letter_table(bst)
    -------------------------------------------------------
    Parameters:
        bst - a binary search tree of Letter objects (BST)
    Returns:
        None
    -------------------------------------------------------
    """
    letters = bst.inorder()
    total = 0

    for l in letters:
        total += l.count

    print("Letter Count/Percent Table")
    print()
    print(f"Total Count: {total:}")
    print()
    print("Letter  Count       %")
    print("---------------------")

    for l in letters:
        percentage = l.count / total * 100
        print(f"{l.letter: >4s}{l.count: >7}{percentage: 9.2f}%")

    return None
