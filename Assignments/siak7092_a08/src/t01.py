"""
-------------------------------------------------------
Testing BST Methods
-------------------------------------------------------
Author:  Mwilu Siakachoma
ID:      169107092
Email:   siak7092@mylaurier.ca
__updated__ = "2025-03-14"
-------------------------------------------------------
"""
# Imports
from BST_linked import BST
# Constants

tree1 = BST()
tree2 = BST()
randomValues = [1, 2, 3, 4, 5, 6, 7]
print("We are inserting integers into both trees.\n")
for v in randomValues:
    tree1.insert(v)
    tree2.insert(v)

eqs = tree1 == tree2
print("We are checking to see if both trees are equal:", eqs, "\n")

value = tree2.remove(3)
print("We are removing the number 3 from tree 2. The value: ", value)
print("We are checking to see if both trees are equal now:", tree1 == tree2, "\n")

minV = tree1.min()
print("The minimum value in tree 1: ", minV)

oc = tree1.one_child_count()
tc = tree2.two_child_count()
lc = tree2.leaf_count()
print("One child count of tree 1: ", oc)
print("Two child count of tree 2: ", tc)
print("Leaf count of tree 2: ", lc)

lo = tree2.levelorder()
po = tree1.postorder()
pro = tree2.preorder()
io = tree1.inorder()
print("level order of tree 2: ", lo)
print("Post order of tree 1: ", po)
print("Pre-order of tree 2: ", pro)
print("In order of tree 1: ", io)

valid = tree2.is_valid()
balanced = tree1.is_balanced()
print("Checking validity of tree 2: ", valid)
print("Checking the if tree 1 is balanced: ", balanced)
