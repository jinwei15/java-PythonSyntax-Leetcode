# Definition for a binary tree node.
# Given a binary tree, return the vertical order traversal of its nodes' values. (ie, from top to bottom, column by column).
#
# If two nodes are in the same row and column, the order should be from left to right.
#
# Examples 1:
#
# Input: [3,9,20,null,null,15,7]
#
#    3
#   /\
#  /  \
#  9  20
#     /\
#    /  \
#   15   7
#
# Output:
#
# [
#   [9],
#   [3,15],
#   [20],
#   [7]
# ]
import sys,collections
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # nearly same implementatino of the level order travsal
    def verticalOrder(self, root: 'TreeNode') -> 'List[List[int]]':
        if root == None: return None
        mapCol = dict()
        queueNode = collections.deque([root])
        queueCol = collections.deque([0])
        minVal = sys.maxsize
        maxVal = -sys.maxsize - 1
        while (len(queueNode) != 0):
            currNode = queueNode.popleft()
            currCol = queueCol.popleft()
            if currCol > maxVal:
                maxVal = currCol
            if currCol < minVal:
                minVal = currCol

            if mapCol.get(currCol) == None:
                mapCol[currCol] = [currNode.val]

            else:
                # newList = mapCol.get(currCol).append(currNode.val)
                # print(newList)
                mapCol[currCol].append(currNode.val)


            if currNode.left != None:
                queueNode.append(currNode.left)
                queueCol.append(currCol - 1)
            if currNode.right != None:
                queueNode.append(currNode.right)
                queueCol.append(currCol + 1)
        res = []
        for i in range(minVal, maxVal + 1):
            res.append(mapCol[i])
        return res


root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

Solution().verticalOrder(root)

