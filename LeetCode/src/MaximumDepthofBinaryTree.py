# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        self.depth = 0

        def dfs(root, dept):
            if root == None:
                return
            if dept > self.depth:
                self.depth = dept
            dfs(root.left, dept + 1)
            dfs(root.right, dept + 1)

        dfs(root, 1)

        return self.depth

# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, x):
# #         self.val = x
# #         self.left = None
# #         self.right = None

# class Solution:
#     def maxDepth(self, root: TreeNode) -> int:


#         if root == None:
#             return 0

#         left = self.maxDepth(root.left) + 1

#         right = self.maxDepth(root.right) + 1

#         return left if left > right else right


