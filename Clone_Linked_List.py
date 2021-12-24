"""
    Python program to clone a linked list with next and arbitrary pointers.
    Big O is O(n) with O(1) extra space.
"""
 
class Node:
    """
        Structure of linked list node.
    """
 
    def __init__(self, data):
        self.data = data
        self.next = None
        self.random = None
 
def clone(original_root):
    """
        Clone a doubly linked list with random pointer
        with O(1) extra space.
    """
 
    # Insert additional node after every node of original list
    curr = original_root
    while curr != None:
        new = Node(curr.data)
        new.next = curr.next
        curr.next = new
        curr = curr.next.next
 
    # Adjust the random pointers of the newly added nodes
    curr = original_root
    while curr != None:
        curr.next.random = curr.random.next
        curr = curr.next.next
 
    # Detach original and duplicate list from each other'''
    curr = original_root
    dup_root = original_root.next
    while curr.next != None:
        tmp = curr.next
        curr.next = curr.next.next
        curr = tmp
 
    return dup_root
 
def print_dlist(root):
    """
        Function to print the doubly linked list.
    """
 
    curr = root
    while curr != None:
        print('Data =', curr.data, ', Random =', curr.random.data)
        curr = curr.next
 
# Create a doubly linked list
original_list = Node(1)
a = Node(2)
b = Node(3)
c = Node(4)
d = Node(5)

original_list.next = a
a.next = b
b.next = c
c.next = d

# Set the random pointers
# 1's random points to 3
original_list.random = a.next

# 2's random points to 1
a.random = original_list

# 3's random points to 5
b.random = d

# 4's random points to 5
c.random = d

# 5's random points to 1
d.random = original_list
 
print('Original list:')
print_dlist(original_list)
 
# Create a duplicate linked list'''
cloned_list = clone(original_list)
 
print('\nCloned list:')
print_dlist(cloned_list)
 