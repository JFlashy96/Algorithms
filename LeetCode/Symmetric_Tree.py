"""
	Author: Jonathan Alston
	This class checks whether, given the root of a binary tree,
	if the tree is a mirror of itself.
	Example 1. Input = [1,2,2,3,4,4,3] (sorted breadth first)
							1
				2						2
			3		4				4		3
	Would return as true.
	Example 2. Input = [1,2,2,null,3,null,3]
					1
			2				2
				3				3
	Would return as false.
"""
class TreeNode(object):

	def __init__(self, val=0,left=None,right=None):
		self.val = val
		self.left = left
		self.right = right

class Solution(object):

	def helper(self, n, m):
		"""
			Takes the values of root and compares them to check
			symmetry.
			Input: val left - value of left node of root.
				   val right - value of right node of root.
			Output: Boolean True/False
		"""

		# Case 1: If the values of left and right are None then
		#		  then return True.
		if n == None and m == None:
			return True
		# Case 2: If one of the values of left or right are None
		#		  then return False.
		if (n == None and m != None) or (n != None and m == None):
			return False
		# Case 3: If the values of left and right do not match
		#		  then return False.
		if n.val != m.val:
			return False

		return self.helper(n.left, m.right) and self.helper(n.right, m.left)

	def checkSymmetry(self, root):
		"""
			Given a root of a binary tree, checks whether tree
			is a mirror of itself.
			Input: TreeNode root - root of a binary tree
			Output: Boolean True/False
		"""

		# Case 1: If tree is empty return true
		if not root:
			return True
		# Case 2: Tree has values. Check values
		return self.helper(root.left, root.right)

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right.left = TreeNode(4)
root.right.right = TreeNode(3)

second_root = TreeNode(1)
second_root.left = TreeNode(2)
second_root.right = TreeNode(2)
second_root.left.right = TreeNode(3)
second_root.right.right = TreeNode(3)

answer = Solution()
a = "" if answer.checkSymmetry(root) else " not"
b = "" if answer.checkSymmetry(second_root) else " not"
print("The first tree is{} symmetric".format(a))
print("The second tree is{} symmetric".format(b))



