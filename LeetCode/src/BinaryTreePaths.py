# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:

        def helper(root, path):

            if root == None:
                return

            path += str(root.val)
            if root.left == None and root.right == None:
                paths.append(path)

            path += '->'
            helper(root.left, path)
            helper(root.right, path)

        paths = []
        res = helper(root, '')

        return paths
        # if res == []:
        #     return res
        # elif type(res[0]) == int and len(res) == 1:
        #     res = [str(e) for e in res]
        #     return res
        # elif type(res[0]) == int and len(res) >= 1:
        #     return ['->'.join(str(e) for e in res)]
        # else:
        #     for index, value in enumerate(res):
        #         res[index] = '->'.join(str(e) for e in value)
        #     return res


