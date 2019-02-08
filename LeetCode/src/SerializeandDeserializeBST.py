# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

import collections
class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str

        using dfs or bfs
        """
        encList = []

        def inorder(root):
            if root is None:
                encList.append(None)
                return

            encList.append(root.val)
            inorder(root.left)

            inorder(root.right)

        inorder(root)
        for i in range(len(encList)):
            if encList[i] == None:
                encList[i] = 'None'
            else:
                encList[i] = str(encList[i])
        # print(encList)
        return ','.join(encList)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode

        from inorder set back to tree
        """

        def deInorder(dList):
            if dList[0] == 'None':
                dList.popleft()
                return
            root = TreeNode(dList[0])
            dList.popleft()
            root.left = deInorder(dList)
            root.right = deInorder(dList)

            return root

        dataList = data.split(',')
        root = deInorder(collections.deque(dataList))

        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))