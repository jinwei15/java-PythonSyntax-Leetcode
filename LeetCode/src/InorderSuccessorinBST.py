# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        orderList = []
        self.ret = None

        def inorder(root):

            if root == None:
                return
            inorder(root.left)
            orderList.append(root)
            if len(orderList) >= 2 and orderList[-2] == p:
                self.ret = orderList[-1]
            inorder(root.right)

        inorder(root)
        return self.ret

