# Definition for singly-linked list.

class Node(object):
    def __init__(self, dataval=0, nextval=None):
       self.dataval = dataval
       self.nextval = nextval

class Solution(object):

    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
              
        fast = slow = head
        for _ in range(n):
            fast = fast.nextval
        if not fast:
            return head.nextval
        while fast.nextval:
            fast = fast.nextval
            slow = slow.nextval
        slow.nextval = slow.nextval.nextval

        return head

list1 = Node()

"""
list1.headval = Node(1)
e1 = list1.headval
e2 = Node(2)
e3 = Node(3)
e4 = Node(4)
e5 = Node(5)

e1.nextval = e2
e2.nextval = e3
e3.nextval = e4
e4.nextval = e5

a = list1.removeNthFromEnd(e1, 2)
print("Answer is {}".format(a))
"""

"""
list1.headval = Node(1)
e1 = list1.headval

a = list1.removeNthFromEnd(e1,1)
print("Answer is {}".format([a]))
"""

list1.headval = Node(1)
e1 = list1.headval
e2 = Node(2)

e1.nextval = e2
a = list1.removeNthFromEnd(e1, 1)
print("Answer is {}".format(a.dataval))

