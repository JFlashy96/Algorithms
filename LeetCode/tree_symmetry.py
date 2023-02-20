class TreeNode(object):
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right
class Solution(object):
	def isSymmetric(self, leftSide, rightSide):

		# Case 1: The left and right side are empty 
		if leftSide == None and rightSide == None:
			return True
		if (leftSide == None and rightSide != None) or (rightSide == None and leftSide != None):
			return False
		elif (leftSide.val != rightSide.val):
			return False

		return self.isSymmetric(leftSide.left,rightSide.right) and self.isSymmetric(leftSide.right,rightSide.left)

	def verify_symmetry(self, root):
		"""
		Input: head - TreeNode object part of tree
		Output: Boolean - whether or not tree is symmetrical
		"""

		if not root:
			return True
		return self.isSymmetric(root.left, root.right)


solution = Solution()
one = TreeNode(1)
two_left = TreeNode(2)
three_left = TreeNode(3)
four_left = TreeNode(4)
two_right = TreeNode(2)
three_right = TreeNode(3)
four_right = TreeNode(4)

one.left = two_left
one.right = two_right

two_left.left = three_left
two_left.right = four_left

two_right.left = four_right
two_right.right = three_right

answer = solution.verify_symmetry(one)
print("Whether the tree is symmetrical or not is {}".format(answer))

# Expected answer should be true

one = TreeNode(1)
two_left = TreeNode(2)
three_right = TreeNode(3)
two_right = TreeNode(2)
three_right = TreeNode(3)

one.left = two_left
two_left.right = three_left

one.right = two_right
two_right.right = three_right

answer = solution.verify_symmetry(one)
print("Whether the tree is symmetrical or not is {}".format(answer))

