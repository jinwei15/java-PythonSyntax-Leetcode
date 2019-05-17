"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""


class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: Node
        :rtype: str
        """
        res = []

        def preorder(root):
            if root == None:
                return

            res.append(str(root.val))
            if root.children == []:
                res.append('None')
                res.append('None')
            for child in root.children:
                preorder(child)

        preorder(root)
        print(','.join(res))
        return ','.join(res)

    # 1 3 5 null null 6 null null 2 null null 4 null null

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: Node
        """
        self.data = collections.deque(data.split(','))

        def dePreorder():
            print(self.data)
            if self.data[0] == 'None':
                self.data.popleft()
                self.data.popleft()
                return

            root = Node(int(self.data.popleft()), [])
            print(root.val)

            while len(self.data) > 0 and self.data[0] != 'None':
                root.children.append(dePreorder())

            if len(self.data) > 0 and self.data[0] == 'None':
                self.data.popleft()
                self.data.popleft()
            return root

        res = dePreorder()
        return res

#             char = queue.popleft()
#             root = Node(int(char), [])
# 			# get back all children when the front element in the queue is not '#'
#             while queue[0] != '#':
#                 root.children.append(build_tree())
#             queue.popleft()   # ignore '#' and return root
#             return root

#         if not data: return None
#         return build_tree()

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))