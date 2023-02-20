"""
    Author: Jonathan Alston
    
    This example script is taken from LeetCode's Problem #876. Middle of the LinkedList.
    Given the head of a singly linked list, return the middle node of the linked list.
    If there are two middle nodes, return the second middle node.

    The BigO time complexity of this solution is O(n) since the linked list is iterated over once.
"""
class Node:

    def __init__(self, dataval=None):
        """
            type dataval: In this example they are ints
            rtype: None
        """
        self.dataval = dataval
        print(type(dataval))
        self.nextval = None

class SLinkedList:

    def __init__(self):
        """
            Used to initialize LinkedList
        """
        self.headval = None

    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow = head
        fast = head
        print(slow.dataval,fast.dataval)
        while fast and fast.nextval:
            slow = slow.nextval
            fast = fast.nextval.nextval
            print(slow.dataval, fast.dataval)
        return slow

list1 = SLinkedList()
list1.headval = Node(1)
e1 = list1.headval
print(e1)
e2 = Node(2)
e3 = Node(3)
e4 = Node(4)
e5 = Node(5)

e1.nextval = e2
e2.nextval = e3
e3.nextval = e4
e4.nextval = e5

a = list1.middleNode(e1)
print("Answer is {}".format(a.dataval))