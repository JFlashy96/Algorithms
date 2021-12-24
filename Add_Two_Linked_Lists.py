"""
	Add two links and store in a third linked list.
	This is useful for storing values that are too large
	to be ints or long int
"""
class Node:
	
	def __init__(self, data=None, next=None):
		self.data = data
		self.next = next

def get_node_count(a):
	"""
		Returns the sum of a linked list. Useful for storing large numbers too large 
		for an int, long, or long long.
	"""
	count = a.data

	while (a.next != None):
		count += a.next.data
		a = a.next
	return count

def add_nodes(a, b):
	"""
		Adds two linked lists by indivually adding the values of nodes of both lists.
		Stores the result in a third linked list.		
	"""
	a_count = get_node_count(a)
	b_count = get_node_count(b)
	return a_count + b_count

def subtract_nodes(a, b):
	"""
		Subtracts linked list a from linked list b by getting the count of the two 
		linked lists and storing the result in a third linked list.
	"""
	a_count = get_node_count(a)
	b_count = get_node_count(b)

	return b_count - a_count

def multiply_nodes(a, b):
	"""
		Multiply two linked lists by getting the value of each linked list and 
		multiplying the results of one another.
	"""
	a_count = get_node_count(a)
	b_count = get_node_count(b)

	return a_count * b_count

number = Node(1)
a = Node(2)
b = Node(3)
c = Node(4)
d = Node(9)

number.next = a
a.next = b
b.next = c
c.next = d

second_number = Node(5)
d = Node(6)
e = Node(7)
f = Node(8)

second_number.next = d
d.next = e
e.next = f

add_result = add_nodes(number, second_number)
subtract_result = subtract_nodes(number, second_number)
multiply_result = multiply_nodes(number, second_number)
print("The value of adding the two linked lists is {}".format(add_result))
print("The value of subtracting the two linked lists is {}".format(subtract_result))
print("The value of multiplying the two linked lists is {}".format(multiply_result))