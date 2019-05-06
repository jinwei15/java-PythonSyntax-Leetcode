# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# class Solution:
#     def closestValue(self, root: 'TreeNode', target: 'float') -> 'int':
#         if root == None: return None

#         self.dis = sys.maxsize
#         self.result = None
#         if self.dis > abs(root.val - target):
#             self.dis = abs(root.val - target)
#             self.result = root.val

#         def dfs(root,target, result):
#             if root == None: return

#             if self.dis > abs(root.val - target):
#                 self.dis = abs(root.val - target)
#                 self.result = root.val

#             dfs(root.left, target, self.result)
#             dfs(root.right, target, self.result)

#         dfs(root.left, target, self.result)
#         dfs(root.right, target, self.result)

#         return self.result


class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:

        returnVal = root.val
        while (root != None):
            if abs(target - root.val) < abs(target - returnVal):
                returnVal = root.val

            root = root.left if target < root.val else root.right
        return returnVal



