# Given preorder and inorder traversal of a tree, construct the binary tree.

# Note:
# You may assume that duplicates do not exist in the tree.

# For example, given

# preorder = [3,9,20,15,7]
# inorder = [9,3,15,20,7]
# Return the following binary tree:

#     3
#    / \
#   9  20
#     /  \
#    15   7


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# from collections import deque

# class Solution:
#     def buildTree(self, preorder: 'List[int]', inorder: 'List[int]') -> 'TreeNode':
#         def helper(preorder, inorder):
#             if not inorder:
#                 return None
            
#             # pick up the first element as a root
#             root_val = preorder.popleft()
#             root = TreeNode(root_val)

#             # root splits inorder list
#             # into left and right subtrees
#             index = inorder.index(root_val)

#             # recursion 
#             root.left= helper(preorder, inorder[:index])
#             root.right = helper(preorder, inorder[index + 1:])
#             return root
        
#         return helper(deque(preorder), inorder)

class Solution:
    def buildTree(self, preorder, inorder):
        if inorder:
            ind = inorder.index(preorder.pop(0))
            root = TreeNode(inorder[ind])
            root.left = self.buildTree(preorder, inorder[0:ind])
            root.right = self.buildTree(preorder, inorder[ind+1:])
            return root
        
