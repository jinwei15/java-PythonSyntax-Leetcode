# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def hasPathSum(self, root: 'TreeNode', sum: 'int') -> 'bool':
        self.total = 0
        self.found = False

        def dfs(root):
            if root == None:
                return
            self.total += root.val
            # print(self.total)
            if self.total == sum and root.left == None and root.right == None:
                self.found = True
            dfs(root.left)
            dfs(root.right)
            self.total -= root.val

        dfs(root)
        return self.found

# class Solution:
#     def hasPathSum(self, root: 'TreeNode', sum: 'int') -> 'bool':
#         self.addUp = 0
#         self.found = False

#         def dfs(root):
#             if root == None:
#                 return True

#             self.addUp += root.val
#             left = dfs(root.left)

#             right = dfs(root.right)

#             if left and right and self.addUp == sum:
#                 self.found = True
#                 return True
#             else:
#                 self.addUp -= root.val

#         dfs(root)
#         return self.found


# class Solution:
#     def hasPathSum(self, root: 'TreeNode', sum: 'int') -> 'bool':
#
#         self.found = False
#         def dfs(root,total):
#             if root == None:
#                 return
#             total += root.val
#             # print(self.total)
#             if total == sum and root.left == None and root.right == None:
#                 self.found = True
#             dfs(root.left,total)
#             dfs(root.right,total)
#
#         dfs(root,0)
#         return self.found

