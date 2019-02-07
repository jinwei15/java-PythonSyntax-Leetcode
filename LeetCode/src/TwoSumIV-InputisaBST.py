# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findTarget(self, root: 'TreeNode', k: 'int') -> 'bool':
        checkSet = set()
        return (self.find(root, k, checkSet))

    def find(self, root, k, checkSet):
        if (root == None):
            return False
        if (k - root.val in checkSet):
            return True

        checkSet.add(root.val)

        return self.find(root.left, k, checkSet) or self.find(root.right, k, checkSet)

