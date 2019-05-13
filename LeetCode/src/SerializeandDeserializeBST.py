# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        res = []

        def postorder(root):
            if root == None:
                res.append('None')
                return

            postorder(root.left)

            postorder(root.right)

            res.append(str(root.val))

        postorder(root)
        return ','.join(res)

    #     def serialize(self, root):
    #         """Encodes a tree to a single string.

    #         :type root: TreeNode
    #         :rtype: str
    #         """
    #         res = []
    #         def preorder(root):
    #             if root == None:
    #                 res.append('None')
    #                 return
    #             res.append(str(root.val))
    #             preorder(root.left)
    #             preorder(root.right)
    #         preorder(root)
    #         return ','.join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        def dePostorder(data):
            if data[-1] == 'None':
                data.pop()
                return None
            # print(data)
            root = TreeNode(int(data.pop()))

            root.right = dePostorder(data)
            root.left = dePostorder(data)

            return root

        dataList = data.split(',')
        return dePostorder((dataList))

#     def deserialize(self, data):
#         """Decodes your encoded data to tree.

#         :type data: str
#         :rtype: TreeNode
#         """
#         def dePreorder(data):
#             if data[0] == 'None':
#                 data.popleft()
#                 return None
#             print(data)
#             root = TreeNode(int(data.popleft()))

#             root.left = dePreorder(data)
#             root.right = dePreorder(data)
#             return root
#         dataList = data.split(',')
#         return dePreorder(collections.deque(dataList))


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))