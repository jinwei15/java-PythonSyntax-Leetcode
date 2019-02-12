# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import sys


class Solution:
    def maxPathSum(self, root: 'TreeNode') -> 'int':
        self.max = -sys.maxsize - 1

        def dfs(root):
            if root == None:
                return 0

            left = dfs(root.left)
            right = dfs(root.right)

            maxVal = max(left + right + root.val, root.val, left + root.val, right + root.val)
            if maxVal > self.max:
                self.max = maxVal

            return max(root.val, root.val + left, root.val + right)

        dfs(root)
        return self.max