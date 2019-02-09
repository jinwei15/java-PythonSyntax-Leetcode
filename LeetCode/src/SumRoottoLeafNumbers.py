# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumNumbers(self, root: 'TreeNode') -> 'int':
        self.numList = []
        self.res = 0

        def dfs(root):
            if root == None: return None

            self.numList.append(root.val)
            left = dfs(root.left)
            right = dfs(root.right)

            if left == None and right == None:
                self.res += self.listToInt(self.numList)
            self.numList.pop()
            return root

        dfs(root)
        return self.res

    def listToInt(self, numList):
        """
        """
        sumUp = 0
        for i in numList:
            sumUp = sumUp * 10 + i
        return sumUp
