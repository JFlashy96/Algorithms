"""
	This program checks if a binary tree is BST (Binary Search Tree) or not
"""

INT_MAX = 4294967296
INT_MIN = -4294967296

# A binary tree node
class Node:

	# Constructor to create a new node
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

# Returns true if the given tree is a binary search tree (eficient version)
def isBST(node):
	return (isBSTUtil(node, INT_MIN, INT_MAX))

# Return true if the given tree is a BST and it's values
# >= min and <= max
def isBSTUtil(node, mini, maxi):

	# An empty tree is BST
	if node is None:
		return True

	# Otherwise check the subtrees recursively
	# tightening the min or max constraint
	return (isBSTUtil(node.left, mini, node.data-1) and 
		isBSTUtil(node.right, node.data+1, maxi))

# Driver program to test above function
root = Node(4)
root.left = Node(2)
root.right = Node(5)
root.left.left = Node(1)
root.left.right = Node(3)

second_root = Node(2)
second_root.left = Node(1)
second_root.right = Node(3)

third_root = Node(2)
third_root.right = Node(7)
third_root.right.right = Node(6)

tree_list = [root, second_root, third_root]

for tree in tree_list:
	if (isBST(tree)):
		print("Tree with root {} is a BST".format(tree.data))
	else:
		print("Tre with root {} is not a BST".format(tree.data))