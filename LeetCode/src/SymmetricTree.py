# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def isSymmetric(self, root):
        if root is None:
            return True
        else:
            return self.isMirror(root.left, root.right)

    def isMirror(self, left, right):
        if left is None and right is None:
            return True
        if left is None or right is None:
            return False

        if left.val == right.val:
            outPair = self.isMirror(left.left, right.right)
            inPiar = self.isMirror(left.right, right.left)
            return outPair and inPiar
        else:
            return False

# class Solution:
#     def isSymmetric(self, root: 'TreeNode') -> 'bool':
#         self.inorder = list()

#         def helper(root):

#             if root == None:
#                 self.inorder.append('x')
#                 return

#             left = helper(root.left)
#             print(root.val)
#             self.inorder.append(root.val)
#             right = helper(root.right)


#         helper(root)
#         print(self.inorder)
#         return self.inorder[::-1] == self.inorder



