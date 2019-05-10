# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ret = []
        def preorder(root):
            if not root :
                return
            ret.append(root.val)
            preorder(root.left)
            preorder(root.right)
        preorder(root)
        return ret