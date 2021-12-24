"""
    Author: Jonathan Alston
    This class teaches how to search a binary tree and print in different orders.
    The different orders of traversal are inorder, preorder, and postorder.
    For example, the tree:
                    1
            2               3
        4       5
        would be returned as the following:
                                inorder = [4,2,5,1,3]
                                preorder = [4,2,1,5,3]
                                postorder = [4,5,2,3,1]

    For another example, the tree:
                    1
                        2
                            3
        would be returned as the following:
                                inorder = [1,3,2]
                                preorder = [1,2,3]
                                postorder = [3,2,1]
"""
class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution(object):

    def __init__(self, arr=[]):
        self.arr = arr
        
    def inOrderTraversal(self, root):
        if root != None:
            print(root.val)
        else:
            print("Kawasaki")
        if root:
            print("true")
            self.inOrderTraversal(root.left)
            self.arr.append(root.val)
            self.inOrderTraversal(root.right)

        return self.arr

    def preOrderTraversal(self, root):
        if root:
            self.arr.append(root.val)
            self.preOrderTraversal(root.left)
            self.preOrderTraversal(root.right)

        return self.arr

    def postOrderTraversal(self, root):
        if root:
            self.postOrderTraversal(root.left)
            self.postOrderTraversal(root.right)
            self.arr.append(root.val)

        return self.arr

# Below is two different ways of instantiating binary trees
c_node = TreeNode(3,None,None)
b_node = TreeNode(2,c_node,None)
a_node = TreeNode(1,None,b_node)

root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right = TreeNode(3)

first_answer = Solution(arr=[])
second_answer = Solution(arr=[])
third_answer = Solution(arr=[])
fourth_answer = Solution(arr=[])
fifth_answer = Solution(arr=[])
sixth_answer = Solution(arr=[])

print("The inorder traversal of the first list is {}".format(first_answer.inOrderTraversal(a_node)))
print("The inorder traversal of the second list is {}".format(second_answer.inOrderTraversal(root)))
print("The preorder traversal of the first list is {}".format(fifth_answer.preOrderTraversal(a_node)))
print("The preorder traversal of the second list is {}".format(sixth_answer.preOrderTraversal(root)))
print("The postorder traversal of the first list is {}".format(third_answer.postOrderTraversal(a_node)))
print("The postorder traversal of the second list is {}".format(fourth_answer.postOrderTraversal(root)))