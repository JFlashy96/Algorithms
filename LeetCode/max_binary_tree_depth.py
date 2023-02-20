
class TreeNode(object):
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = None
		self.right = None

class Solution(object):
	def maxDepth(self, root):
		"""
		input root: TreeNode
		return int: depth of Binary Search Tree
		"""

		def dfs(root, depth):
			if not root: return depth 
			return max(dfs(root.left, depth + 1), dfs(root.right, depth + 1))

		return dfs(root, 0)

solution = Solution()

one = TreeNode(3)
two = TreeNode(9)
three = TreeNode(20)
four = TreeNode(15)
five = TreeNode(7)

one.left = two 
one.right = three
three.left = four
three.right = five 

depth = solution.maxDepth(one)

print(depth)
