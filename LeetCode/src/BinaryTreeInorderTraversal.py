# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: 'TreeNode') -> 'List[int]':
        self.res = []
        def inorder(root):
            if not root:
                return

            inorder(root.left)
            self.res.append(root.val)
            inorder(root.right)
        inorder(root)
        return self.res