# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# class Solution:
#     def isValidBST(self, root: 'TreeNode') -> 'bool':

#         if root == None: return True

#         def helper(root,min,max):


#             if root == None:
#                 return True


#             left = helper(root.left,min,root.val)
#             right = helper(root.right,root.val,max)


#             if left and right and min<root.val<max:
#                 return True
#             else:
#                 return False

#         return helper(root,-sys.maxsize-1,sys.maxsize)


import sys


class Solution:
    def isValidBST(self, root: 'TreeNode') -> 'bool':
        self.pre = -sys.maxsize - 1

        def inorder(root):
            if root == None:
                return True

            left = inorder(root.left)
            if self.pre < root.val:
                self.pre = root.val
            else:
                return False
            right = inorder(root.right)

            return left and right

        return inorder(root)








