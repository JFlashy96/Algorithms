class ListNode(object):
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next
class Solution(object):
	def reverse_linked_list(self, head):
		"""
		Input: node - ListNode object
		Output: node - ListNode object in reversed order
		"""

		prev = None

		while head:
			curr = head
			head = head.next
			curr.next = prev
			prev = curr
		return prev

solution = Solution()

a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
e = ListNode(5)

a.next = b
b.next = c 
c.next = d
d.next = e

f = solution.reverse_linked_list(a)
print(f)
# Expected output: 5