"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""


class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if root == None:
            return 0

        tempList = []
        for child in root.children:
            val = self.maxDepth(child) + 1
            tempList.append(val)
        # if tempList == []:
        #     return 0
        return max(tempList) if tempList != [] else 1
