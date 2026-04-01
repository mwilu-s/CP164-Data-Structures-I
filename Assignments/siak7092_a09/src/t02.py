"""
-------------------------------------------------------
Sorted Hash Set
-------------------------------------------------------
Author:  Mwilu Siakachoma
ID:      169107092
Email:   siak7092@mylaurier.ca
__updated__ = "2025-03-20"
-------------------------------------------------------
"""
# Imports
from functions import insert_words, comparison_total
from Hash_Set_sorted import Hash_Set
# Constants

filename = "gibbon.txt"
fv = open(filename, "r", encoding="utf-8")
hash_set = Hash_Set(20)

insert_words(fv, hash_set)
total, max_word = comparison_total(hash_set)

print("Using array-based Sorted List Hash_Set\n")
print("Total Comparisons: {:,}".format(total))
print("Word with maximum comparisons '{}': {:,}".format(
    max_word.word, max_word.comparisons))
