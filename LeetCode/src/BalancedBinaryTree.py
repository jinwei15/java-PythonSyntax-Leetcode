# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#
#
#
#
# check wether the tree is balanced
#

class Solution:
    def isBalanced(self, root: 'TreeNode') -> 'bool':

        
        def dfs(root):
            if root == None:
                return 0
            
            left = dfs(root.left)
            right = dfs(root.right)
            
            if left == -1 or right == -1 or abs(left-right) > 1:
                return -1
            else:
                return 1 + max(left, right)
            
        return dfs(root) != -1
            
