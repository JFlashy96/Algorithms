
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution(object):
    def deleteNode(self, node):
       """
       Function to delete node from linked list.
       Input: node - node to be deleted. 
       Output: None - modify linked list in place
       """
       
       node.val = node.next.val
       node.next = node.next.next

first = ListNode(4)
second = ListNode(5)
third = ListNode(1)
fourth = ListNode(9)

first.next = second
second.next = third
third.next = fourth

a = Solution()
a.deleteNode(third)

trav = first
print(trav.val)
while (trav.next != None):
    trav = trav.next
    print(trav.val)
