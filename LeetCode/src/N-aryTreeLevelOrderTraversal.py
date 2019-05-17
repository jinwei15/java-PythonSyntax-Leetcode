"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        res = []

        def helper(root, depth):

            if root == None:
                return
            if depth >= len(res):
                res.append([])
            res[depth].append(root.val)
            for child in root.children:
                helper(child, depth + 1)

        helper(root, 0)
        return res
