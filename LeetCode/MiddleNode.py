class Node():
	def __init__(self, val=None, nextVal=None):
		self.val = val
		self.nextVal = nextVal

class Solution():
	def middleNode(self, head):
		slow = head
		fast = head
		while fast and fast.nextVal:
			slow = slow.nextVal
			fast = fast.nextVal.nextVal
			print(slow.val)
		return slow

a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)
f = Node(6)
g = Node(7)
h = Node(8)

a.nextVal = b
b.nextVal = c
c.nextVal = d
d.nextVal = e
e.nextVal = f
f.nextVal = g
g.nextVal = h

solution = Solution()
answer = solution.middleNode(a)
while answer:
	print(answer.val)
	answer = answer.nextVal
