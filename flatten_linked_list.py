"""
	Author: Jonathan Alston
	Write a function that flattens a linked 
	list by taking possible down nodes and 
	merging them up between their parent and 
	their parent's next.
	Sample inputs - Expected outputs
	[1] -> [2] -> [3] -> [8] -> [10]
				   |	  |
				   | 	 [9]
				   |     
				  [4] -> [5] -> [6]
				  				 |
				  				[7] 
	The flattened list should look like th1is:
	[1] -> [2] -> [3] -> [4] -> [5] -> [6] -> 								   
	[7] -> [8] -> [9] -> [10]
"""

a = node(1,2,None)
b = node(2,3,None)
c = node(3,8,4)
d = node(8,10,9)
e = node(10,None,None)
f = node(9,None,None)
g = node(4,5,None)
h = node(5,6,None)
i = node(6,None,7)
j = node(7,None,None)

def node(self, val=None, nextNode=None, down=None):
	val = val
	nextNode = nextNode
	downNode = downNode

def flatten_list(head):
	"""
		Input: node head - node that can contain value, nextNode, and downNode
		Output: flattened list
	"""
	flattened_list = []

	curr = head
	top_node = curr

	# add to flattened list the down node value before moving to the next value
	if (curr.downNode != None):
		flattened_list.append(curr.downNode)
	elif (curr.nextNode != None):
		flattened_list.append(nextNode)

	curr = curr.nextNode
	flattened_list(curr)










