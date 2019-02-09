# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: 'TreeNode', sum: 'int') -> 'bool':
        self.addUp = 0
        self.found = False

        def dfs(root):
            if root == None:
                return True

            self.addUp += root.val
            left = dfs(root.left)

            right = dfs(root.right)

            if left and right and self.addUp == sum:
                self.found = True
                return True
            else:
                self.addUp -= root.val

        dfs(root)
        return self.found

