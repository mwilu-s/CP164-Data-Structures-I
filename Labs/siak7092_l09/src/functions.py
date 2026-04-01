"""
-------------------------------------------------------
Functions
-------------------------------------------------------
Author:  Mwilu Siakachoma
ID:      169107092
Email:   siak7092@mylaurier.ca
__updated__ = "2025-03-13"
-------------------------------------------------------
"""
# Imports
from Movie import Movie

# Constants


def hash_table(slots, values):
    """
    -------------------------------------------------------
    Print a hash table of a set of values. The format is:
Hash     Slot Key
-------- ---- --------------------
 1652346    3 Dark City, 1998
  848448    6 Zulu, 1964
    Do not create an actual Hash_Set.
    Use: hash_table(slots, values)
    -------------------------------------------------------
    Parameters:
       slots - the number of slots available (int > 0)
       values - the values to hash (list of ?)
    Returns:
       None
    -------------------------------------------------------
    """
    print("Hash     Slot Key\n")
    print("-------- ---- --------------------")

    for v in values:
        movieKey = v.key()
        movieHash = hash(v)
        movieSlot = movieHash % 7
        print(f"{movieHash: 8d}{movieSlot: 5d} {movieKey}")

    return None
