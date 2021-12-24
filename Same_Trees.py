"""
    Author: Jonathan Alston
    This class returns true if two binary trees are the same.
    Example 1:
    a.                                          b.
                1                               1
        2               3                2             3
    Example 1:
    Would return as True.
    Example 2:
    a.                      b.
                1           1
        2                           2
    Would return as False.
    Example 3:
    a.       
                1                               1
        2               1                1             2
    Would return as False.
"""
class TreeNode(object):    
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p, q):
        """
            Returns true if two trees are the same. Return false otherwise.
        """
        if(p == None and q == None): # 1. base case, the leafs.
            return True
        elif(type(p) != type(q)): # 2. see if only one is None
            return False
        elif(p.val != q.val): # 3. see if different values
            return False
        
        # 4. each level, checking (p.left q.left) and (p.right q.right)
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

b_root = TreeNode(1)
b_root.left = TreeNode(2)
b_root.right = TreeNode(3)

c_root = TreeNode(1)
c_root.left = TreeNode(2)

d_root = TreeNode(1)
d_root.right = TreeNode(2)

e_root = TreeNode(1)
e_root.left = TreeNode(2)
e_root.right = TreeNode(1)

f_root = TreeNode(1)
f_root.left = TreeNode(1)
f_root.right = TreeNode(2)

answer = Solution()

print("The answer is {}".format(answer.isSameTree(root, b_root)))
print("The answer is {}".format(answer.isSameTree(c_root, d_root)))
print("The answer is {}".format(answer.isSameTree(e_root, f_root)))
