# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# Invert a binary tree.

# Example:

# Input:

#      4
#    /   \
#   2     7
#  / \   / \
# 1   3 6   9
# Output:

#      4
#    /   \
#   7     2
#  / \   / \
# 9   6 3   1
# Trivia:
# This problem was inspired by this original tweet by Max Howell:

# Google: 90% of our engineers use the software you wrote (Homebrew), but you can’t invert a binary tree on a whiteboard so f*** off.


# invert using BFS queue
class Solution:
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return None
        
        queue = collections.deque()
        queue.append(root)
        
        while(len(queue)!=0):
            curr = queue.popleft()
            if curr!=None:
                queue.append(curr.left)
                queue.append(curr.right)
                temp = curr.left
                curr.left = curr.right
                curr.right = temp
        
        return root
            
            
            
        
