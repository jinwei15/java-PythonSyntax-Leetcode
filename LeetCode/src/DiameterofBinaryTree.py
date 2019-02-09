# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

        
        
# Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

# Example:
# Given a binary tree 

#           1
#          / \
#         2   3
#        / \     
#       4   5    
# Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

# Note: The length of path between two nodes is represented by the number of edges between them.

#
# class Solution:
#     def diameterOfBinaryTree(self, root):
#         """
#         :type root: TreeNode
#         :rtype: int
#         """
#         if root == None:
#             return 0
#
#         self.diameter = 0
#
#         self.dfs(root)
#
#         return self.diameter - 1
#
#
#     def dfs(self,root):
#         if root == None:
#             return 0
#         else:
#             L = self.dfs(root.left)
#             R = self.dfs(root.right)
#
#             self.diameter = max(self.diameter , L+R+1)
#             return max(L, R) + 1
#


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import collections, sys


class Solution:
    def diameterOfBinaryTree(self, root: 'TreeNode') -> 'int':
        if root == None:
            return 0
        self.biggest = -sys.maxsize - 1

        def dfs(root):
            if root == None:
                return 0

            left = dfs(root.left) + 1
            right = dfs(root.right) + 1

            if left + right > self.biggest:
                self.biggest = left + right
            return max(left, right)

        dfs(root)
        return self.biggest - 2








