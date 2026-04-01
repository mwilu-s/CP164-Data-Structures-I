"""
-------------------------------------------------------
Comparison Methods
-------------------------------------------------------
Author:  Mwilu Siakachoma
ID:      169107092
Email:   siak7092@mylaurier.ca
__updated__ = "2025-03-14"
-------------------------------------------------------
"""
# Imports
from BST_linked import BST
from functions import comparison_total, do_comparisons, fill_BST
# Constants
DATA1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
DATA2 = "MFTCJPWADHKNRUYBEIGLOQSVXZ"
DATA3 = "ETAOINSHRDLUCMPFYWGBVKJXZQ"

bst1 = BST()
bst2 = BST()
bst3 = BST()

fill_BST(bst1, DATA1)
fill_BST(bst2, DATA2)
fill_BST(bst3, DATA3)

filename = "gibbon.txt"
filename2 = "otoos610.txt"
fv1 = open(filename, "r", encoding="utf-8")
fv2 = open(filename2, "r", encoding="utf-8")

print("Testing for DATA1 and File 1 (Gibbon):\n")
do_comparisons(fv1, bst1)
total1 = comparison_total(bst1)

print("Testing for DATA1 and File 2 (Gibbon):\n")
fv1 = open(filename, "r", encoding="utf-8")
fv2 = open(filename2, "r", encoding="utf-8")
do_comparisons(fv2, bst1)
total2 = comparison_total(bst1)

print("Testing for DATA2 and File 1 (Gibbon):\n")
fv1 = open(filename, "r", encoding="utf-8")
fv2 = open(filename2, "r", encoding="utf-8")
do_comparisons(fv1, bst2)
total3 = comparison_total(bst2)

print("Testing for DATA2 and File 2 (Gibbon):\n")
fv1 = open(filename, "r", encoding="utf-8")
fv2 = open(filename2, "r", encoding="utf-8")
do_comparisons(fv2, bst2)
total4 = comparison_total(bst2)

print("Testing for DATA3 and File 1 (Gibbon):\n")
fv1 = open(filename, "r", encoding="utf-8")
fv2 = open(filename2, "r", encoding="utf-8")
do_comparisons(fv1, bst3)
total5 = comparison_total(bst3)

print("Testing for DATA3 and File 2 (Gibbon):\n")
fv1 = open(filename, "r", encoding="utf-8")
fv2 = open(filename2, "r", encoding="utf-8")
do_comparisons(fv2, bst3)
total6 = comparison_total(bst3)

print("Comparing by order: ABCDEFGHIJKLMNOPQRSTUVWXYZ")
print(f"{total1 + total2}")
print("------------------------------------------------------------")
print("Comparing by order: MFTCJPWADHKNRUYBEIGLOQSVXZ")
print(f"{total3 + total4}")
print("------------------------------------------------------------")
print("Comparing by order: ETAOINSHRDLUCMPFYWGBVKJXZQ")
print(f"{total5 + total6}")
