# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if len(nums) == 0: return None
        left, right = 0, len(nums) - 1
        mid = (left + right) // 2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid + 1:])

        return root


# same as This question is nearly the same as 106. Construct Binary Tree from Inorder and Postorder Traversal https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/