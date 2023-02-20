"""
	Author: Jonathan Alston
	Description: The purpose of this file is to practice while reading
				ADTs, Data Structures, and Problem Solving with C++. However,
				these linked list exercises will be implemented in Python.
"""
class Node:
	def __init__(self, val=None, next=None):
		self.val = val
		self.next = next

class LinkedList:
	def __init__(self):
		self.start_node = None

	def printList(self):
		"""
			Function that prints item in LinkedList.
			Input - LinkedList object
		"""
		if self.start_node is None:
			print("List has no element")
			return
		else:
			n = self.start_node
			while n is not None:
				print("{}".format(n.val))
				n = n.next

	def insert(self, data):
		"""
			Insert value into given linked list.
			Input head - Node 
			Input a - first Node in linked list.
		"""
		new_node = Node(data)

		# Case 1: The linked list is empty and this would be the first element.
		if self.start_node is None:	
			self.start_node = new_node
			return 

		# Case 2: Linked list is not empty. Will insert between two nodes or insert
		# at the end if the val will be the largest in the list.
		n = self.start_node
		while n.next is not None:
			# if value is larger than the previous node's value but smaller than 
			# the next node's value than insert in the middle
			if (n.val <= new_node.val and new_node.val <= n.next.val):
				new_node.next = n.next
				n.next = new_node
				return
			n = n.next
		n.next = new_node
		return 

if __name__ == "__main__":

	new_linked_list = LinkedList()
	new_linked_list.insert(5)
	new_linked_list.insert(10)
	new_linked_list.insert(15)
	new_linked_list.printList()
	print("done adding items to list")
	new_linked_list.insert(6)
	new_linked_list.insert(11)
	new_linked_list.insert(14)
	new_linked_list.insert(16)
	new_linked_list.printList()


