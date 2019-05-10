# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ret = []

        def postorder(root):
            if not root:
                return
            postorder(root.left)
            postorder(root.right)
            ret.append(root.val)

        postorder(root)
        return ret

