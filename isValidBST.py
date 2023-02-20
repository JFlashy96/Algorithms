class ListNode():
	def __init__(self, val=None, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

class Solution():
	def isValid(self, root):
		floor = float('-inf')
		ceiling = float('inf')
		return self.isValidBST(root, floor, ceiling)
	def isValidBST(self, root, floor, ceiling):
		if root is None: return True
		if root.val <= floor or root.val >= ceiling:
			return False
		return self.isValidBST(root.left, floor, root.val) and self.isValidBST(root.right, root.val, ceiling)

solution = Solution()
b = ListNode(2)
c = ListNode(1)
d = ListNode(3)

e = ListNode(5)
f = ListNode(1)
g = ListNode(4)
h = ListNode(3)
i = ListNode(6)

b.left = c
b.right = d

e.left = f
e.right = g
g.left = h
g.right = i

answer = solution.isValid(b)
secondAnswer = solution.isValid(e)

a = ''
j = ''
if answer:
	a = "is"
else:
	a = "is not"
if secondAnswer:
	j = "is"
else: 
	j = "is not"

print("The first tree {} a tree".format(a))
print("the second tree {} a tree".format(j))