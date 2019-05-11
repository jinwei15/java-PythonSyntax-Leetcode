# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        self.res = []

        def dfs(root, depth):
            if root == None:
                return
            if depth >= len(self.res):
                self.res.append([root.val])
            else:
                self.res[depth].append(root.val)
            dfs(root.left, depth + 1)
            dfs(root.right, depth + 1)

        dfs(root, 0)

        return self.res[::-1]


