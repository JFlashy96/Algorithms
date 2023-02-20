# A linked list Node
class Node:
	def __init__(self, data=None, next=None):
		self.data = data
		self.next = next

# Helper function to print a given linked list
def printList(msg, head):

	print(msg, end='')
	ptr = head
	while ptr:
		print(ptr.data, end=' ->')
		ptr = ptr.next
	print('None')

def frontBackSplit(source):
	"""
		Split the given list's nodes into front and back halves,
		and return the two lists using a list.
		If the legnth is odd, the extra node should go in the front
		list. It uses the fast/slow reference strategy.
	"""

	# If the length is less than 2, handle is separately
	if source is None or source.next is None:
		frontRef = source
		backRef = None
		return frontRef, backRef

	slow = source
	fast = source.next

	# advance 'fast' two nodes and 'slow' by one node
	while fast:
		fast = fast.next
		if fast:
			slow = slow.next
			fast = fast.next

	# 'slow' is before the midpoint of the list, so split it in two
	# at that point.
	frontRef = source
	backRef = slow.next 
	slow.next = None

	return frontRef, backRef

if __name__ == '__main__':

	# input keys 
	keys = [6,3,4,8,2,9]

	# points to the head node of the linked list
	head = None

	# construct a linked list
	for i in reversed(range(len(keys))):
		head = Node(keys[i], head)

	first, second = frontBackSplit(head)

	# print linked list
	printList('Front List: ', first)
	printList('Back List: ', second)








